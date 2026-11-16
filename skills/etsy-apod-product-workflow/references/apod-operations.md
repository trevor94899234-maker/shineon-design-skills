# Private APOD application and persistence

These are behavior checks, not a hardcoded API or permanent selector inventory. Observe the current editor. Use normal documented tools and visible upload/download controls; no private endpoints, cookies or token extraction. Keep one browser operator.

## Before any write

- Confirm URL/product ID, variant/SKU and artwork against the active record. Capture current text, personalization, selected gallery asset IDs/order/primary, videos, price, shipping and AutoFulfill where relevant.
- Check exact private action authority and exclusions. Preserve a recoverable before snapshot. Inspect drift since the prior snapshot; do not overwrite concurrent user edits blindly.
- Have the actual clean field packet and accepted-file role/hash map ready. Do not upload from a folder glob containing rejected versions or review contact sheets.
- Confirm each current file is technical PASS or has a matching allowed exact-file private exception; required human acceptance still applies. A supplier master, generated candidate and delivery file are different objects.

## Text and options

1. Populate the authorized title, complete description and actual tags in the correct product. Respect current editor limits; tags may be chips rather than a single text field.
2. Apply authorized personalization instructions/options from verified source fields. Do not change the production template or name length simply to fit a sentence. Distinguish field capacity from tested printable fit and Etsy mapping.
3. Use the real save action. Reopen/reload the product and read complete persisted values; a toast or filled input is insufficient.
4. Compare full normalized values with the packet. Normalize line endings and Unicode only as documented; preserve words, punctuation, sections and intentional line breaks. Verify tags as distinct actual values, filtering empty search widgets and removing UI delete-glyphs only after observing them.
5. Keep APOD-unexposed fields in the coverage matrix. Never click Push to Etsy to finish a private task.

If opening a modal times out, inspect whether it opened before clicking again. Use currently visible labeled controls; avoid assuming an input's HTML `type` attribute exists just because its runtime type is text. Multiple Close buttons may include hidden/background dialogs: identify the active dialog. Do not save unrelated checkbox changes.

## Gallery upload

1. Resolve accepted role → exact local file/revision/hash → intended position. Preserve old selected asset IDs/order for recovery.
2. Observe whether the chooser supports multiple files. If it accepts only one, upload one file at a time; wait for the actual asset/selected count and idle state before proceeding. Do not assume a tool timeout means no upload.
3. Reconcile every successful/uncertain upload with the actual new asset. If a duplicate appears, distinguish repeated source media from the selected delivery set; do not delete source assets to make counts look right.
4. Select only eligible delivery assets. Recoverably deselect replaced old media within authorized scope after checking variant/shared effects; do not use Delete Mockup.
5. Order by the explicit role map, with the intended hero first. Verify actual order after every reorder method. If normal drag is ineffective, the UI may support reversible deselect/reselect in the desired order; use it only after confirming behavior and retaining recovery mapping.
6. Freshly inspect selectors after each rerender. A selection tool may report detached-state failure after successfully applying the click. Inspect state before retrying. Lazy-loaded `data-src`/`src` differs by UI; use the currently observed mapping, never a stale index.
7. Save Selection (or the actual current equivalent), confirm completion, reopen the selector and enumerate **selected** media only. Count available-library images separately.

## Identity proof after save

For each selected position record actual remote asset ID/observed source, role, local hash, proof type and receipt. Prefer supported retrieval of original remote media, then SHA-256 equality to the accepted native file. If a direct download fails, a documented page-asset export may retrieve the same observed asset; never guess a URL or treat an export request as downloaded bytes.

If the service transforms bytes, preserve native and transformed hashes separately and inspect the actual transformed image against the exact native. Record `visual_mapping` plus transformation evidence; unequal hashes are not byte identity. If remote bytes are unavailable, use the supported visible mapping and disclose its weaker proof. Do not claim all files byte-verified based on filenames or thumbnails.

A screenshot can show a count and only part of a scrollable gallery. Keep full selected asset/order readback separately; do not pretend one screenshot visually contains all items.

## Final cross-save check

After the last gallery/video save, reopen product fields again. Recheck title, full description, actual tags, required personalization, identity/variant, price and excluded-setting preservation, AutoFulfill and warnings. Reopen selected media and compare count, uniqueness, order and primary. Any changed final bytes, field values or selection invalidates the affected earlier receipt.

Observed pitfalls from product 627699 (2026-10-28), to re-check rather than assume: chooser was single-file; selection rerendered each click; drag did not reorder; selection sequence did; a hidden tag listbox looked empty while actual chips held 13; SKU was in an expandable column; some dialogs opened despite a timeout. These are recovery hypotheses, not guaranteed present-day APOD behavior.
