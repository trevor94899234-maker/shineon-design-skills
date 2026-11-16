# Digital delivery integrity

Reviewed 2026-10-16. Use after the existing real-file and content QA gates, or for authorized packaging-only maintenance. This does not restart ten reader reviews for unchanged content, replace physical/user testing, or authorize a new send, upload, publication or unrelated edit.

## 1 Bind the exact release

Keep one manifest joining product, paper format, role (buyer/preview/owner), technical version, source filename, size/hash and retained-file ID/version. Record which version was actually reviewed. When replacing only selected products or formats, map each old identity/hash to its replacement explicitly; leave other files and earlier archives unchanged. A replacement pair does not supersede the whole bundle. Keep source and review material out of buyer packages.

## 2 Verify the transport at the right layer

- **Original bytes:** record measured source/export size and SHA-256 before transfer. Never overwrite this baseline with the service's later hash.
- **Retained delivery:** use the supported read/materialize route when available; record the actual returned file ID/version, filename, size and measured hash. Retention, local round-trip verification and accepted chat-send evidence are different states. None establishes that the user downloaded or opened a file. Check an uncertain send before retrying it.
- **Unchanged binary or archive:** a matching measured hash establishes byte identity. For a ZIP, also read its members, check CRC, expected paths/counts and member hashes against the release manifest. Matching archive bytes alone does not validate the contents' correctness.
- **A service-rewritten PDF:** a hash mismatch proves different bytes, not by itself damaged pages. Inspect the actual source and returned copies before attributing a cause. Where bytes changed, compare every page's count, boxes, extracted text, links/destinations, outlines and rendered pixels at a recorded engine/resolution. Compare metadata and any observable added structure separately. Report byte mismatch plus the exact dimensions of parity proved, rather than calling the files identical. If forms, annotations, attachments, accessibility tags or signatures matter, inspect those too; basic page parity does not cover them.
- Do not assume every mismatch is a credentials/metadata change. Missing, altered or unreadable content remains a failed or unresolved delivery gate. Do not strip credentials, rewrite a signed file, silently upscale or regenerate approved pages to force matching hashes. Keep both copies and seek the smallest authorized correction.

For source-preserving delivery, a supported archive can retain the exact original files when that format is suitable and authorized. Verify its extracted members; do not present a transformed direct PDF and an original archived PDF as byte-identical versions. No new upload or send is implied by preparing a manifest.

## 3 Check the whole archive set before giving unpack instructions

- Inspect member paths without executing bundled code. Reject unsafe paths and validate each archive's CRC/member hashes and expected role coverage using available tools.
- Compare normalized member paths across **all** parts the buyer or owner is told to extract together. A valid archive can still overwrite another part's guide or index. Account for case-insensitive destinations where relevant. Same path with different bytes is a collision; same path/same bytes is a duplicate to document, not a second unique asset.
- Give each part's guide/index a unique path, or deliberately retain separate part folders with matching instructions. Do not flatten parts into one folder when this would overwrite distinct files. Preserve product/format mapping and buyer-versus-owner separation.
- Verify references in the final guide resolve to supplied files or accessible authorized links. If a historical receipt is absent, label a fresh verification as new; do not impersonate or reconstruct the old receipt from summary counts.
- Reopen the final package and read its actual member list and hashes after packaging. A packaging-only change can reuse earlier content QA only when the member identities are verified unchanged. State what was checked now and what remains historical.

## Dated evidence and limits

The 16 October 2026 P19 v3.2 round-trip record contained two ten-page PDFs whose delivered hashes/sizes differed from the production PDFs. All twenty page instances matched the recorded 144-DPI rendered pixels, extracted text, page boxes and links; outlines matched while document metadata differed. This is one observed transport result, not a guarantee about future Library files or every PDF feature.

The same day's independent audit found twelve original buyer ZIPs with unique product PDF paths but repeated root guide/index filenames containing part-specific content. Each ZIP passed CRC; extracting them together with overwrite could still lose eleven guides/indexes. A later five-product maintenance package explicitly replaced ten mapped PDFs and preserved the held products and separate P19 revision. These findings support the two verification layers and scoped supersession, not a new complete content/rights certification.

## Regression decisions

1. Hashes differ but every inspected PDF page/content feature matches: report the measured byte mismatch and bounded content-parity pass, not corruption or byte identity.
2. A single link destination differs despite matching page pixels: fail that parity check; do not excuse it as metadata-only.
3. Every ZIP passes CRC but two parts contain different START_HERE files at the same extraction path: hold common-folder unpack instructions until collision-safe packaging or separate folders are verified.
4. Only two products are replaced: map their exact old/new members; preserve other products' state and prior QA rather than declaring the entire bundle refreshed.
5. Library contains the file but no accepted-send receipt is established: say retained, delivery unconfirmed; do not infer never sent or resend automatically.
