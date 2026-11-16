# Completion, proof and optional record audit

## Completion checklist

Use the active endpoint, not the most ambitious possible endpoint. Every required item must be verified or explicitly removed by the owner; unknown is not complete. Keep genuine unavailable requirements partial rather than silently excluding them.

1. Exact product/variant/artwork and unchanged source hashes still match.
2. N requested distinct roles have N eligible current native files. Verify actual bytes, decoded dimensions, native provenance and per-file QA. Exact-file exceptions remain visible; rejected versions are excluded.
3. N distinct selected remote assets map to those N current files, with expected order and primary, after save/reopen. No duplicate role or duplicate native hash padding. Disclose byte-match versus visual/transformed mapping per file.
4. Every requested applicable field is saved/reopened or intentionally preserved/rechecked. Full clean text and actual tags match; personalized fields and variant mapping are correct. Read back fields after media saves.
5. Full field-coverage matrix includes unexposed/not-applicable/owner-excluded rows with reasons. Price, shipping, policies and production partner are not assumed applied.
6. Required video is actually saved, played and inspected, with capability/count/duration and final file/asset proof. If not required by the narrow scope, say so once.
7. Required fulfillment state and all warnings are read back. Resolve required safety issues; preserve release/print/manual-review gaps.
8. Deliver actual final native files, manifest, useful contact sheet and listing packet through a user-accessible route. Preserve sources and before snapshots. A preview contact sheet is not a substitute for every original image.
9. If an archive is supplied, verify entry count, CRC, exact native hashes, manifest and scope. Include accepted delivery files only unless the user asked for all candidates; “all generated originals” includes rejected candidates in a separately labeled collection.

Status wording:

- `PREPARED_LOCAL`: files/copy exist; no persisted remote claim.
- `PARTIAL_APOD_APPLIED`: named fields/assets persisted; required work remains.
- `COMPLETE_AUTHORIZED_PRIVATE_SCOPE`: every item in the actual scope verified, with explicit exceptions/exclusions reported. This is not a technical-fidelity, production or publication certificate.
- `APOD_READY_FOR_OWNER_REVIEW`: use only when the stricter controlling full-build gates actually pass, including necessary production/mapping/video checks.
- `ETSY_PUBLISHED`: only after separately authorized actual publication and live readback; this workflow does not grant that authority.

Do not infer goal completion from elapsed time, budget or file count. If a goal exists, mark complete only when the active objective is achieved; otherwise use its documented continuation/blocking behavior.

## Optional `audit_delivery.py`

This read-only Python 3.9+ standard-library helper checks **the supplied record and local bytes**. It does not browse, upload, certify source truth, decode images, judge visual roles, authenticate owner approval, test real print fit or prove live persistence. A passing result cannot replace those reviews. Never fill missing evidence with fabricated receipts to obtain PASS.

Run using the runtime's actual Python executable:

```text
python scripts/audit_delivery.py /authorized/task/delivery-audit.json
python scripts/test_audit_delivery.py
```

Exit 0: consistent records and referenced byte checks. Exit 1: failed requirement. Exit 2: malformed/unreadable manifest. Output is JSON on stdout; no network or modifications. Paths in the manifest are relative to its directory and must stay inside it. Every receipt is a real nonempty file. A historical receipt can be referenced after a supported transfer into the task package; no cloud use of inaccessible local paths.

Manifest format version 1:

```json
{
  "version": 1,
  "product": {"id": "product-id", "variant_id": "variant-id", "artwork_id": "artwork-id"},
  "scope": {
    "mode": "SCOPED_PRIVATE_UPDATE",
    "roles": ["01", "02"],
    "required_fields": ["title", "description", "tags"],
    "tag_count": 13,
    "exclusions": [{"item": "shipping", "receipt": "evidence/owner-scope.txt"}]
  },
  "authority_receipt": "evidence/owner-scope.txt",
  "source_receipt": "evidence/source-binding.json",
  "coverage_receipt": "field-packet.csv",
  "last_mutation_at": "2026-10-28T08:00:00+00:00",
  "files": [{
    "role": "01", "path": "native/01.png", "sha256": "actual-64-hex-digest",
    "technical": "PASS", "qa_receipt": "evidence/qa-01.md"
  }],
  "gallery": {
    "product": {"id": "product-id", "variant_id": "variant-id", "artwork_id": "artwork-id"},
    "verified_at": "2026-10-28T08:02:00+00:00",
    "readback_receipt": "evidence/gallery.json", "primary_role": "01",
    "selected": [{
      "role": "01", "asset_id": "actual-remote-id", "local_sha256": "actual-64-hex-digest",
      "proof": "byte_match", "remote_path": "remote/01.png", "receipt": "evidence/gallery.json"
    }]
  },
  "fields": [{
    "name": "title", "status": "APPLIED_VERIFIED", "expected": "Actual intended title",
    "saved": "Actual intended title", "verified_at": "2026-10-28T08:03:00+00:00",
    "receipt": "evidence/fields.json"
  }],
  "safety": {"auto_fulfill": "OFF", "verified_at": "2026-10-28T08:03:00+00:00", "receipt": "evidence/fields.json"},
  "video": {"required": false, "reason": "Narrow thumbnails and text scope"}
}
```

This abbreviated schema illustration is intentionally not a complete passing delivery record: supply every requested role and required field from actual evidence. Do not copy example identifiers, dates, receipts or hashes as evidence.

For technical HOLD with an allowed owner exception, a file also needs:

```json
"exception": {"sha256": "same-current-file-digest", "purpose": "private_apod", "receipt": "evidence/exact-owner-decision.txt"}
```

For `visual_mapping` remote proof use `receipt` identifying actual mapping/inspection and, if available, `remote_path`; the helper counts it separately and never calls it byte-matched. For `byte_match`, remote bytes are mandatory and must hash to the eligible native.

For video-required scope add `capability_receipt`, `required_count` and `items` under `video`; each item needs `path`, `sha256`, `qa_receipt`, `save_receipt`, `verified_at` and positive `duration_seconds`. If a hard minimum duration applies, add `minimum_duration_seconds`. Full private build requires 20 roles, title/description/13 tags and video; current live capability and controlling contract determine the video count, not the example. A required tags field needs a positive integer count; a full build cannot weaken its 13-tag contract through the manifest.

For a text-only `SCOPED_PRIVATE_UPDATE`, use `scope.roles: []`, `files: []` and the actual nonempty `required_fields`. Under `gallery`, retain identity, `verified_at` and the real preservation/readback receipt, add `unchanged: true`, and omit `selected` and `primary_role`. This means preserve the existing gallery, **not select zero images**. The result reports `gallery_state: UNCHANGED_RECORDED` and `selected_assets: null`; no delivered-image or new byte-match claim is made. Full builds cannot use this shorthand.

The helper checks receipts exist, not whether their content is truthful. The executing agent remains responsible for source review, full field coverage, current authority, actual browser evidence and distinct visual roles. Report its result as `RECORD_CHECK_PASS`, never “Etsy approved” or a blanket QA PASS.
