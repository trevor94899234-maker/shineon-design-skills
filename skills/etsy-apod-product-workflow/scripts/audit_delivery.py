"""Read-only record/byte audit; not visual QA, live verification or permission approval."""
import argparse
import hashlib
import json
import re
import sys
import unicodedata
from datetime import datetime
from pathlib import Path


def audit(manifest_path):
    manifest_path = Path(manifest_path).resolve()
    base = manifest_path.parent
    data = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
    errors = []

    def require(condition, message):
        if not condition:
            errors.append(message)

    def artifact(ref, label):
        if not isinstance(ref, str) or not ref:
            errors.append(f"{label}: missing relative artifact path")
            return None
        raw = Path(ref)
        if raw.is_absolute() or re.match(r"^[A-Za-z]:", ref) or "\\" in ref:
            errors.append(f"{label}: use a portable relative path")
            return None
        path = (base / raw).resolve()
        if not path.is_relative_to(base):
            errors.append(f"{label}: path escapes task directory")
            return None
        if not path.is_file() or path.stat().st_size == 0:
            errors.append(f"{label}: artifact missing or empty: {ref}")
            return None
        return path

    def digest(ref, expected, label):
        path = artifact(ref, label)
        if not isinstance(expected, str) or not re.fullmatch(r"[0-9a-fA-F]{64}", expected):
            errors.append(f"{label}: invalid SHA-256")
            return None
        if path is None:
            return None
        hasher = hashlib.sha256()
        with path.open("rb") as stream:
            for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                hasher.update(chunk)
        actual = hasher.hexdigest()
        require(actual == expected.lower(), f"{label}: bytes differ from recorded hash")
        return actual

    def timestamp(value):
        if not isinstance(value, str):
            raise ValueError("timestamps must be ISO-8601 strings with timezone")
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            raise ValueError("timestamps must include timezone")
        return parsed

    def readback(row, label):
        artifact(row.get("receipt"), f"{label} receipt")
        require(timestamp(row.get("verified_at")) >= last_mutation,
                f"{label}: readback predates last mutation")

    def norm(value):
        if isinstance(value, str):
            return unicodedata.normalize("NFC", value.replace("\r\n", "\n").replace("\r", "\n"))
        return value

    require(data.get("version") == 1, "unsupported manifest version")
    scope = data["scope"]
    require(scope.get("mode") in {"FULL_PRIVATE_BUILD", "SCOPED_PRIVATE_UPDATE"},
            "helper only audits private APOD scopes")
    roles = scope["roles"]
    fields_required = scope["required_fields"]
    if not isinstance(roles, list) or not all(isinstance(x, str) and x for x in roles):
        raise ValueError("scope.roles must be a list of role IDs")
    if not isinstance(fields_required, list) or not all(isinstance(x, str) and x for x in fields_required):
        raise ValueError("scope.required_fields must be a list of field names")
    require(len(roles) == len(set(roles)), "duplicate requested role IDs")
    require(len(fields_required) == len(set(fields_required)), "duplicate required field names")
    require(bool(roles or fields_required), "scope needs requested roles or fields")
    if "tags" in fields_required:
        tag_count = scope.get("tag_count")
        require(isinstance(tag_count, int) and not isinstance(tag_count, bool) and tag_count > 0,
                "required tags need a positive integer count")
    product = data["product"]
    identity_keys = ("id", "variant_id", "artwork_id")
    require(all(isinstance(product.get(k), str) and product[k] for k in identity_keys),
            "exact product/variant/artwork binding is required")
    for key in ("authority_receipt", "source_receipt", "coverage_receipt"):
        artifact(data.get(key), key)
    last_mutation = timestamp(data["last_mutation_at"])
    for exclusion in scope.get("exclusions", []):
        require(bool(exclusion.get("item")), "exclusion needs an item")
        artifact(exclusion.get("receipt"), "owner exclusion")
        require(exclusion.get("item") not in fields_required, "required field also listed as excluded")

    files = data["files"]
    require(isinstance(files, list), "files must be a list")
    by_role = {}
    native_hashes = []
    exception_count = 0
    for row in files:
        role = row["role"]
        require(role in roles, f"unexpected local role: {role}")
        require(role not in by_role, f"duplicate local role: {role}")
        by_role[role] = row
        actual = digest(row.get("path"), row.get("sha256"), f"native {role}")
        if actual:
            native_hashes.append(actual)
        artifact(row.get("qa_receipt"), f"QA {role}")
        if row.get("technical") == "HOLD":
            exception_count += 1
            exception = row.get("exception", {})
            require(exception.get("purpose") == "private_apod", f"{role}: private exception purpose missing")
            require(isinstance(exception.get("sha256"), str)
                    and exception["sha256"].lower() == str(row.get("sha256")).lower(),
                    f"{role}: exception is not bound to current exact file")
            artifact(exception.get("receipt"), f"owner exception {role}")
        else:
            require(row.get("technical") == "PASS", f"{role}: unsupported technical status")
    require(set(by_role) == set(roles), "missing requested native roles")
    require(len(files) == len(roles), "native file count differs from requested roles")
    require(len(native_hashes) == len(set(native_hashes)), "duplicate native bytes across roles")

    gallery = data["gallery"]
    require(all(gallery.get("product", {}).get(k) == product.get(k) for k in identity_keys),
            "gallery destination identity mismatch")
    artifact(gallery.get("readback_receipt"), "gallery readback")
    require(timestamp(gallery.get("verified_at")) >= last_mutation, "gallery readback predates last mutation")
    selected = gallery.get("selected", []) if roles else []
    if roles:
        require(gallery.get("unchanged") is not True, "requested image delivery cannot be marked unchanged")
        require([r.get("role") for r in selected] == roles, "selected gallery count/order differs from requested roles")
        require(gallery.get("primary_role") == roles[0], "primary role mismatch")
    else:
        require(scope.get("mode") == "SCOPED_PRIVATE_UPDATE", "zero roles only valid for scoped field updates")
        require(gallery.get("unchanged") is True, "text-only update needs explicit preserved-gallery evidence")
        require("selected" not in gallery and "primary_role" not in gallery,
                "text-only audit must reference preserved gallery receipt, not an empty replacement selection")
    remote_ids = [r.get("asset_id") for r in selected]
    require(all(isinstance(x, str) and x for x in remote_ids), "remote asset ID missing")
    require(len(remote_ids) == len(set(remote_ids)), "duplicate selected remote asset IDs")
    byte_count = 0
    visual_count = 0
    for row in selected:
        role = row.get("role")
        native = by_role.get(role, {})
        local_hash = str(native.get("sha256", "")).lower()
        require(str(row.get("local_sha256", "")).lower() == local_hash and bool(local_hash),
                f"remote {role}: current native identity mismatch")
        artifact(row.get("receipt"), f"remote mapping {role}")
        if row.get("proof") == "byte_match":
            actual = digest(row.get("remote_path"), local_hash, f"remote bytes {role}")
            if actual and actual == local_hash:
                byte_count += 1
        elif row.get("proof") == "visual_mapping":
            visual_count += 1
            if row.get("remote_path"):
                artifact(row["remote_path"], f"transformed remote {role}")
        else:
            errors.append(f"remote {role}: unknown proof type")

    field_names = []
    for row in data["fields"]:
        name = row["name"]
        field_names.append(name)
        require(row.get("status") in {"APPLIED_VERIFIED", "UNCHANGED_VERIFIED"}, f"{name}: field not verified")
        readback(row, f"field {name}")
        expected, saved = row["expected"], row["saved"]
        if name == "tags":
            if not all(isinstance(v, list) and all(isinstance(x, str) and x for x in v) for v in (expected, saved)):
                raise ValueError("tags must be lists of nonempty strings")
            expected, saved = [norm(x) for x in expected], [norm(x) for x in saved]
            require(len(saved) == scope["tag_count"], "saved tag count mismatch")
            require(len(saved) == len(set(x.casefold() for x in saved)), "duplicate saved tags")
            require(len(expected) == len(set(x.casefold() for x in expected)), "duplicate intended tags")
            require(sorted(expected) == sorted(saved), "saved tags differ from intended tags")
        else:
            require(norm(expected) == norm(saved), f"{name}: saved value differs from intended value")
    require(len(field_names) == len(set(field_names)), "duplicate field records")
    require(set(fields_required).issubset(field_names), "missing required field readback")

    safety = data["safety"]
    require(safety.get("auto_fulfill") == "OFF", "required AutoFulfill OFF not established")
    readback(safety, "fulfillment safety")
    video = data["video"]
    require(isinstance(video.get("required"), bool), "video.required must be boolean")
    if scope.get("mode") == "FULL_PRIVATE_BUILD":
        require(len(roles) == 20, "full MyGiftStyle build requires 20 requested roles")
        require({"title", "description", "tags"}.issubset(fields_required), "full build missing core text fields")
        require(scope.get("tag_count") == 13, "full MyGiftStyle build requires 13 tags")
        require(video.get("required") is True, "full build video requirement omitted")
    if video.get("required") is True:
        artifact(video.get("capability_receipt"), "video capability")
        count = video.get("required_count")
        require(isinstance(count, int) and not isinstance(count, bool) and count > 0, "invalid required video count")
        items = video.get("items", [])
        require(len(items) == count, "required video delivery count mismatch")
        video_hashes = []
        for index, row in enumerate(items):
            label = f"video {index + 1}"
            actual = digest(row.get("path"), row.get("sha256"), label)
            if actual:
                video_hashes.append(actual)
            artifact(row.get("qa_receipt"), f"{label} QA")
            artifact(row.get("save_receipt"), f"{label} saved readback")
            require(timestamp(row.get("verified_at")) >= last_mutation, f"{label}: stale readback")
            duration = row.get("duration_seconds", 0)
            minimum = video.get("minimum_duration_seconds", 0)
            require(isinstance(duration, (int, float)) and not isinstance(duration, bool)
                    and duration > 0 and duration >= minimum, f"{label}: duration requirement not met")
        require(len(video_hashes) == len(set(video_hashes)), "duplicate video bytes")
    else:
        require(bool(video.get("reason")), "non-required video needs a scope reason")

    return {
        "status": "RECORD_CHECK_FAIL" if errors else "RECORD_CHECK_PASS",
        "product_id": product.get("id"), "requested_roles": len(roles),
        "native_files": len(files), "selected_assets": len(selected) if roles else None,
        "gallery_state": "SELECTED_SET_CHECKED" if roles else "UNCHANGED_RECORDED",
        "byte_matches": byte_count, "visual_mappings": visual_count,
        "technical_holds_with_recorded_exception": exception_count,
        "errors": errors,
        "limitation": "Record and byte checks only; no live, visual, permission, print or publication certification."
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()
    try:
        result = audit(args.manifest)
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as error:
        print(json.dumps({"status": "MALFORMED_OR_UNREADABLE", "error": str(error)}, ensure_ascii=False))
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] == "RECORD_CHECK_PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
