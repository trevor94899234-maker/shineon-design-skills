"""No-network fixtures for consequential false-completion cases."""
import copy
import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from audit_delivery import audit


class DeliveryChecks(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "evidence.txt").write_text("Synthetic test receipt; not live evidence.", encoding="utf-8")
        now = "2026-10-28T10:00:00+00:00"
        product = {"id": "test-product", "variant_id": "test-variant", "artwork_id": "test-art"}
        self.data = {
            "version": 1, "product": product,
            "scope": {"mode": "SCOPED_PRIVATE_UPDATE", "roles": ["01", "02"],
                      "required_fields": ["title", "tags"], "tag_count": 13, "exclusions": []},
            "authority_receipt": "evidence.txt", "source_receipt": "evidence.txt",
            "coverage_receipt": "evidence.txt", "last_mutation_at": now,
            "files": [], "gallery": {"product": copy.deepcopy(product), "verified_at": now,
                "readback_receipt": "evidence.txt", "primary_role": "01", "selected": []},
            "fields": [{"name": "title", "status": "APPLIED_VERIFIED", "expected": "Test title",
                "saved": "Test title", "receipt": "evidence.txt", "verified_at": now},
                {"name": "tags", "status": "APPLIED_VERIFIED", "expected": [f"tag {i}" for i in range(13)],
                 "saved": [f"tag {i}" for i in reversed(range(13))], "receipt": "evidence.txt", "verified_at": now}],
            "safety": {"auto_fulfill": "OFF", "receipt": "evidence.txt", "verified_at": now},
            "video": {"required": False, "reason": "Scoped text and two images"}}
        for role in self.data["scope"]["roles"]:
            blob = f"Synthetic role {role} binary identity fixture".encode()
            path = f"{role}.bin"
            (self.root / path).write_bytes(blob)
            (self.root / f"remote-{path}").write_bytes(blob)
            sha = hashlib.sha256(blob).hexdigest()
            self.data["files"].append({"role": role, "path": path, "sha256": sha,
                "technical": "PASS", "qa_receipt": "evidence.txt"})
            self.data["gallery"]["selected"].append({"role": role, "asset_id": f"asset-{role}",
                "local_sha256": sha, "proof": "byte_match", "remote_path": f"remote-{path}", "receipt": "evidence.txt"})

    def run_audit(self):
        path = self.root / "manifest.json"
        path.write_text(json.dumps(self.data), encoding="utf-8")
        return audit(path)

    def assert_failed(self, contains):
        result = self.run_audit()
        self.assertEqual(result["status"], "RECORD_CHECK_FAIL")
        self.assertTrue(any(contains in e for e in result["errors"]), result)

    def test_valid_scope_and_reordered_tags(self):
        result = self.run_audit()
        self.assertEqual(result["status"], "RECORD_CHECK_PASS")
        self.assertEqual(result["byte_matches"], 2)

    def test_changed_file_after_exception(self):
        row = self.data["files"][0]
        row["technical"] = "HOLD"
        row["exception"] = {"sha256": "f" * 64, "purpose": "private_apod", "receipt": "evidence.txt"}
        self.assert_failed("exception is not bound")

    def test_recorded_exception_does_not_become_pass(self):
        row = self.data["files"][0]
        row["technical"] = "HOLD"
        row["exception"] = {"sha256": row["sha256"], "purpose": "private_apod", "receipt": "evidence.txt"}
        result = self.run_audit()
        self.assertEqual(result["status"], "RECORD_CHECK_PASS")
        self.assertEqual(result["technical_holds_with_recorded_exception"], 1)

    def test_wrong_product(self):
        self.data["gallery"]["product"]["id"] = "another-product"
        self.assert_failed("destination identity mismatch")

    def test_wrong_primary_and_order(self):
        self.data["gallery"]["selected"].reverse()
        self.data["gallery"]["primary_role"] = "02"
        self.assert_failed("primary role mismatch")

    def test_missing_role(self):
        self.data["files"].pop()
        self.assert_failed("missing requested native roles")

    def test_duplicate_remote_asset(self):
        self.data["gallery"]["selected"][1]["asset_id"] = "asset-01"
        self.assert_failed("duplicate selected remote")

    def test_transformed_bytes_not_called_match(self):
        (self.root / "remote-01.bin").write_bytes(b"transformed content")
        self.assert_failed("bytes differ")
        self.data["gallery"]["selected"][0]["proof"] = "visual_mapping"
        result = self.run_audit()
        self.assertEqual((result["byte_matches"], result["visual_mappings"]), (1, 1))
        self.assertEqual(result["status"], "RECORD_CHECK_PASS")

    def test_post_media_field_overwrite(self):
        self.data["fields"][0]["saved"] = "Stale title"
        self.assert_failed("saved value differs")

    def test_stale_readback(self):
        self.data["fields"][0]["verified_at"] = "2026-10-28T09:59:59+00:00"
        self.assert_failed("readback predates")

    def test_duplicate_tags(self):
        self.data["fields"][1]["saved"][0] = self.data["fields"][1]["saved"][1]
        self.assert_failed("duplicate saved tags")

    def test_missing_authority_receipt(self):
        self.data["authority_receipt"] = "nonexistent.txt"
        self.assert_failed("artifact missing")

    def test_receipt_cannot_escape_package(self):
        self.data["authority_receipt"] = "../outside.txt"
        self.assert_failed("path escapes")

    def test_full_build_does_not_omit_video(self):
        self.data["scope"]["mode"] = "FULL_PRIVATE_BUILD"
        self.assert_failed("video requirement omitted")

    def test_on_is_not_safe(self):
        self.data["safety"]["auto_fulfill"] = "ON"
        self.assert_failed("AutoFulfill OFF")

    def test_duplicate_native_content_is_not_two_roles(self):
        first = self.data["files"][0]
        self.data["files"][1].update(path=first["path"], sha256=first["sha256"])
        self.assert_failed("duplicate native bytes")

    def test_missing_required_personalization(self):
        self.data["scope"]["required_fields"].append("personalization")
        self.assert_failed("missing required field readback")

    def test_zero_required_tags_rejected(self):
        self.data["scope"]["tag_count"] = 0
        self.data["fields"][1].update(expected=[], saved=[])
        self.assert_failed("positive integer count")

    def test_text_only_preserves_gallery_without_zero_selection_claim(self):
        self.data["scope"]["roles"] = []
        self.data["files"] = []
        gallery = self.data["gallery"]
        gallery.pop("selected")
        gallery.pop("primary_role")
        gallery["unchanged"] = True
        result = self.run_audit()
        self.assertEqual(result["status"], "RECORD_CHECK_PASS", result)
        self.assertEqual(result["gallery_state"], "UNCHANGED_RECORDED")
        self.assertIsNone(result["selected_assets"])
        self.assertEqual(result["byte_matches"], 0)
        gallery["selected"] = []
        self.assert_failed("not an empty replacement selection")

    def test_full_twenty_with_two_saved_videos(self):
        self.data["scope"]["mode"] = "FULL_PRIVATE_BUILD"
        for i in range(3, 21):
            role = f"{i:02d}"
            self.data["scope"]["roles"].append(role)
            path = f"{role}.bin"
            blob = f"Synthetic full-build role {role}".encode()
            (self.root / path).write_bytes(blob)
            sha = hashlib.sha256(blob).hexdigest()
            self.data["files"].append({"role": role, "path": path, "sha256": sha,
                "technical": "PASS", "qa_receipt": "evidence.txt"})
            self.data["gallery"]["selected"].append({"role": role, "asset_id": f"asset-{role}",
                "local_sha256": sha, "proof": "byte_match", "remote_path": path, "receipt": "evidence.txt"})
        self.data["scope"]["required_fields"].append("description")
        self.data["fields"].append({"name": "description", "status": "APPLIED_VERIFIED",
            "expected": "Line 1\r\nLine 2", "saved": "Line 1\nLine 2", "receipt": "evidence.txt",
            "verified_at": self.data["last_mutation_at"]})
        self.data["video"] = {"required": True, "required_count": 2,
            "capability_receipt": "evidence.txt", "minimum_duration_seconds": 15, "items": []}
        for i in range(2):
            blob = f"Synthetic video {i}".encode()
            path = f"video-{i}.bin"
            (self.root / path).write_bytes(blob)
            self.data["video"]["items"].append({"path": path, "sha256": hashlib.sha256(blob).hexdigest(),
                "qa_receipt": "evidence.txt", "save_receipt": "evidence.txt", "duration_seconds": 15,
                "verified_at": self.data["last_mutation_at"]})
        result = self.run_audit()
        self.assertEqual(result["status"], "RECORD_CHECK_PASS", result)
        self.assertEqual(result["byte_matches"], 20)
        self.data["video"]["items"][0]["duration_seconds"] = 14
        self.assert_failed("duration requirement not met")
        self.data["video"]["items"].pop()
        self.assert_failed("video delivery count mismatch")
        self.data["scope"]["tag_count"] = 0
        self.data["fields"][1].update(expected=[], saved=[])
        self.assert_failed("full MyGiftStyle build requires 13 tags")


if __name__ == "__main__":
    unittest.main(verbosity=2)
