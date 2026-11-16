#!/usr/bin/env python3
"""Validate an evidence-release audit sidecar; never certify semantic truth or demand."""
import argparse
import hashlib
import json
import re
from pathlib import Path

STAGES = ["draft", "evidence-qualified", "text-QA-passed", "image-QA-passed", "owner-approved", "applied"]
MODES = {"exact_only", "near_match_aggregate", "provider_unspecified"}
STATUSES = {"numeric_display", "observed_zero", "threshold", "unknown", "missing", "unavailable"}

def norm(value):
    return " ".join(value.casefold().split())

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def validate(packet, directory=Path("."), expected_baseline_sha256=None):
    errors = []
    def require(condition, message):
        if not condition:
            errors.append(message)
    synthetic = packet.get("synthetic_fixture") is True
    version = packet.get("artifact_version")
    require(bool(version), "artifact version missing")
    baseline = packet.get("baseline", {})
    baseline_hash = baseline.get("sha256")
    require(bool(baseline_hash), "baseline hash missing")
    if expected_baseline_sha256 is not None:
        require(baseline_hash == expected_baseline_sha256, "baseline differs from external immutable lock")
    elif not synthetic:
        require(False, "real packet requires --baseline-sha256 from original baseline record")
    overlay = packet.get("overlay", {})
    require(bool(overlay.get("version")), "overlay version missing")
    require(overlay.get("baseline_sha256") == baseline_hash, "overlay points to a different baseline")
    def check_file(record, label):
        if not synthetic:
            path = record.get("path")
            require(bool(path), label + " path missing")
            if path:
                actual = directory / path
                require(actual.is_file(), label + " file unavailable")
                if actual.is_file():
                    require(digest(actual) == record.get("sha256"), label + " hash mismatch")
    check_file(baseline, "baseline")
    check_file(overlay, "overlay")
    sources = packet.get("raw_sources", [])
    ids = [s.get("id") for s in sources]
    require(bool(ids) and all(ids) and len(ids) == len(set(ids)), "raw-source index absent or duplicate IDs")
    for source in sources:
        require(source.get("kind") in {"native_csv", "raw_ui", "raw_table"}, "summary cannot replace a raw source")
        require(source.get("full_index_checked") is True, "raw-source full index not checked: " + str(source.get("id")))
        check_file(source, "source " + str(source.get("id")))
    obs_list = packet.get("observations", [])
    observations = {o.get("id"): o for o in obs_list}
    require(len(observations) == len(obs_list) and None not in observations, "observation IDs absent or duplicated")
    for o in obs_list:
        require(o.get("source_id") in ids, "observation source not in raw index")
        for key in ("query", "raw_locator", "market", "market_verification", "measurement_window", "capture_status", "provider"):
            require(bool(o.get(key)), "observation " + str(o.get("id")) + " lacks " + key)
        require(o.get("measurement_mode") in MODES, "measurement matching mode absent")
        for metric in o.get("metrics", {}).values():
            state, raw = metric.get("state"), metric.get("raw")
            require(state in STATUSES, "unrecognized metric state")
            require("raw" in metric, "raw metric missing")
            if state == "numeric_display":
                require(bool(re.fullmatch(r"[0-9]+(?:,[0-9]{3})*(?:\.[0-9]+)?%?", str(raw).strip())) and str(raw).strip() not in {"0", "0.0"}, "numeric display is not a qualified nonzero number")
            if state == "observed_zero":
                require(str(raw).strip() in {"0", "0.0"}, "observed zero must preserve zero")
                if metric.get("ui_raw") in {"-", "—"}:
                    require(metric.get("representation_resolution") == "verified_zero", "native zero/UI dash discrepancy is unresolved")
            if state == "threshold":
                require(isinstance(raw, str) and bool(re.fullmatch(r"[<>]=?\s*[0-9]+(?:\.[0-9]+)?%?", raw.strip())), "threshold qualifier lost")
            if state == "unknown":
                require(str(raw).casefold().strip() == "unknown", "Unknown coerced into another value")
    uses = packet.get("phrase_uses", [])
    actual = packet.get("actual_fields", {})
    expected = [("tag", norm(x)) for x in actual.get("tags", [])] + [("title_query", norm(x)) for x in actual.get("title_queries", [])]
    actual_uses = [(u.get("field"), norm(u.get("phrase", ""))) for u in uses if u.get("field") in {"tag", "title_query"}]
    require(sorted(actual_uses) == sorted(expected), "phrase ledger must cover every actual tag/title query exactly once")
    for u in uses:
        phrase, relation = u.get("phrase", ""), u.get("relation")
        require(relation in {"direct", "related", "composed", "unresearched"}, "phrase relation missing")
        require(bool(u.get("reason")) and bool(u.get("product_intent_review")), "phrase allocation/intent rationale absent: " + phrase)
        linked = u.get("observation_ids", [])
        require(all(i in observations for i in linked), "phrase references absent observation")
        if relation == "direct":
            require(bool(linked), "direct phrase has no evidence")
            require(all(norm(observations[i].get("query", "")) == norm(phrase) for i in linked if i in observations), "direct phrase uses a different query: " + phrase)
        claims = u.get("numeric_claims", [])
        require(not claims or relation == "direct", "related/composed/unresearched phrase cannot inherit numbers: " + phrase)
        for claim in claims:
            oid = claim.get("observation_id")
            o = observations.get(oid, {})
            require(oid in linked, "numeric claim not joined to the phrase evidence")
            require(norm(o.get("query", "")) == norm(phrase), "numeric claim query mismatch: " + phrase)
            metric = o.get("metrics", {}).get(claim.get("metric"), {})
            require(bool(metric), "numeric claim metric missing from observation")
            require(claim.get("raw") == metric.get("raw") and claim.get("state") == metric.get("state"), "numeric claim changed raw value or qualifier")
            require(metric.get("state") in {"numeric_display", "observed_zero", "threshold"}, "unknown/missing is not quantified demand")
            require(claim.get("measurement_mode") == o.get("measurement_mode"), "exact query confused with exact-only measurement")
            require(claim.get("market") == o.get("market") and claim.get("measurement_window") == o.get("measurement_window"), "numeric claim changed market/window")
            require(claim.get("market_verification") == o.get("market_verification"), "numeric claim changed market verification")
    for gap in packet.get("missing_or_requery", []):
        require(set(gap.get("checked_source_ids", [])) == set(ids), "missing/requery claim has not checked the full raw index")
        require(bool(gap.get("unresolved_field")) and bool(gap.get("reason")), "missing/requery claim lacks specific unresolved field")
        found = [o for o in obs_list if norm(o.get("query", "")) == norm(gap.get("query", "")) and gap.get("unresolved_field") in o.get("metrics", {})]
        if found:
            require(gap.get("purpose") == "refresh" and bool(gap.get("refresh_reason")), "requested metric already exists; recover it before requery")
    coverage = packet.get("category_attribute_coverage", {})
    require(coverage.get("state") in {"verified", "unknown"}, "category/attribute coverage status absent")
    if coverage.get("state") == "verified":
        require(bool(coverage.get("source_ref")) and "selected_values" in coverage, "verified category coverage lacks actual source/values")
    stage = packet.get("stage", "draft")
    require(stage in STAGES, "unrecognized release stage")
    index = STAGES.index(stage) if stage in STAGES else 0
    gates = packet.get("gates", {})
    needed = []
    if index >= 1:
        needed += ["evidence"]
        require(bool(packet.get("competitor_review_refs")), "evidence-qualified needs actual competitor/intent review")
    if index >= 2:
        needed += ["text_qa"]
    if index >= 3 and packet.get("images_required"):
        needed += ["image_qa"]
    if stage == "image-QA-passed":
        require(packet.get("images_required") is True, "image-QA-passed requires actual image scope")
    if index >= 4:
        needed += ["owner_approval"]
    if index >= 5:
        needed += ["applied"]
    for key in needed:
        gate = gates.get(key, {})
        require(gate.get("passed") is True and gate.get("artifact_version") == version and bool(gate.get("evidence_ref")), "stage prerequisite missing/stale: " + key)
    if packet.get("images_required") and index >= 3:
        qa = gates.get("image_qa", {})
        require(type(qa.get("accepted_count")) is int and qa.get("accepted_count", 0) > 0 and qa.get("accepted_count") == qa.get("required_count"), "image briefs/previews are not accepted exports")
    if packet.get("release_label") in {"ready", "final", "research-complete", "production-ready"}:
        require(index >= 1, "draft cannot carry a ready/final release label")
        required_stage = {"research": 1, "text": 2, "image_production": 2, "images": 3, "application": 4, "applied": 5}
        scope = packet.get("release_scope")
        require(scope in required_stage, "ready/final label needs an explicit release scope")
        if scope in required_stage:
            require(index >= required_stage[scope], "release scope exceeds completed stage")
        if packet.get("release_label") == "production-ready":
            require(scope == "image_production", "production-ready must name image_production scope")
        judge = packet.get("independent_review", {})
        require(judge.get("independent_of_author") is True and judge.get("artifact_version") == version, "independent outcome review missing/stale")
        require(judge.get("verdict") == "PASS" and {"evidence", "outcome"}.issubset(set(judge.get("scope", []))), "narrow/failed review cannot certify evidence and outcome")
        require(bool(judge.get("report_ref")), "independent outcome report missing")
        require(not synthetic, "synthetic fixture cannot be released ready/final")
    return errors

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packet", type=Path)
    parser.add_argument("--baseline-sha256")
    args = parser.parse_args()
    try:
        packet = json.loads(args.packet.read_text())
        errors = validate(packet, args.packet.parent, args.baseline_sha256)
    except (OSError, ValueError, TypeError, AttributeError) as exc:
        errors = ["invalid packet: " + str(exc)]
    print(json.dumps({"mechanical_pass": not errors, "semantic_or_market_proof": False, "errors": errors}, ensure_ascii=False, indent=2))
    return int(bool(errors))

if __name__ == "__main__":
    raise SystemExit(main())
