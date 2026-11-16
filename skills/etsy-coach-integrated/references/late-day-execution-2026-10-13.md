# Late day execution lessons

Release 2026.10.13.4. Reviewed 13 October 2026, Asia/Hong_Kong. Extend the existing physical/digital routes and APOD readiness contract; do not create another listing pipeline.

## Save uncertainty and exact state

An HTTP error or timeout after Save is an uncertain outcome, not proof that nothing persisted. Use an authorized read-only reopen of the exact product and compare the intended fields, tags, selected assets and version before retrying. Never recreate a digital listing solely because the response failed. If the read itself is denied, stop and report the unresolved state; do not bypass the denial. Successful readback can verify the saved fields while other requested fields remain incomplete.

The reviewed journal case saved title, description and 13 tags despite an initial 502; reopening confirmed persistence. Its observed USD 29.95 price already matched three comparable journal records, so there was no basis to claim a price change. The measured native video was 14 seconds, not a promised 15 seconds. Five rejected generated image pilots meant zero accepted new gallery images, not five completed images. These are bounded observations, not universal platform facts or demand proof.

## Approval and pilot accounting

Keep method approval, a specific draft preview, committing edits, final export, APOD upload and Etsy publication as distinct states. Approval to use Canva does not automatically approve a particular pending preview. A generated design URL or pending transaction does not prove a committed design; a 600-pixel preview does not verify a 2000-pixel export. Keep exact supplier product images and the original logo as locked sources when approved; do not replace them with visually similar generation. An upload cancelled or denied remains unavailable for that operation; do not silently substitute another asset or route.

A 20-image request remains a 20-image target after a pilot. Reject product drift before scaling. Use the existing role manifest to track requested, generated, accepted, saved and independently verified counts separately.

## Digital private preparation

Record actual file/page count, file hash, destination file ID and delivery-enabled state separately from pricing, category, tags, market validation and publication. A private 10-page PDF attached to a digital draft is a real saved result but is not a ready-to-sell listing when commercial fields or review are outstanding. Keep source rights, scripture translation licensing and original content checks attached to the delivery route.

## Supplier template precedence

For production artwork, compare the current exact SKU/print-area setting, supplier's official downloadable template, current supplier specification table, native file dimensions, in-image dimension labels and DPI metadata. Preserve any conflict rather than collapsing them into one number. Old labels or 72-DPI metadata do not override verified current pixel dimensions; pixel dimensions alone do not prove physical print size.

Read actual shape-specific safe zones, bleed and hole keep-outs from the template; do not substitute a generic equal-margin inset. A measured raster hole-outline bounding box is not a certified physical hole diameter or manufacturing tolerance. Keep template overlays out of final production art and retain the unmodified official file and hash for reference. A blocked source does not authorize evading it; an independently available official public source may be used only within existing read permission and without bypassing the denied action.

A user-confirmed supplier plan can establish the plan context but cannot establish combined shipping, current cost or a finished bundle. Preserve existing full-cost, single-supplier preference, recipient-versus-writer, licensing and zero-ad/limited-time experiment constraints.

## Regression checks

- Save returns 502 and exact product readback matches: record applied fields, avoid duplicate recreation, keep remaining gaps.
- Canva route is approved but one preview is pending: do not commit/upload or report the batch complete.
- Only 5 of 20 images were generated and all fail fidelity: accepted count is 0.
- Digital file is attached, but price/category/tags are blank: private applied, not release ready.
- Template pixel dimensions conflict with an old printed label: disclose each observation and verify the exact current SKU before production.
- A source fetch or UI action is cancelled: stop that action; never use a fallback as a permission bypass.
