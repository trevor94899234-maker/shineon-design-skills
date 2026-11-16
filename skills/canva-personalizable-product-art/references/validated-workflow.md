# Verified workflow evidence

## Contents

- [Current status](#current-status)
- [Product and approved originals](#product-and-approved-originals)
- [Transfer route and recovery](#transfer-route-and-recovery-observed-on-2026-10-06)
- [Actual Canva route](#actual-canva-route)
- [Initial export route and files](#actual-initial-export-route-and-files)
- [Repair and name-length evidence](#repair-and-name-length-evidence)
- [Received revised PNG evidence](#received-revised-png-evidence)
- [Final local files and archive](#final-local-files-and-archive)
- [Remaining gates](#remaining-gates)
- [Inspector validation scope](#inspector-validation-scope)

## Current status

EDITABLE TEXT, NAME COLOR, AND LOCAL EXPORT BYTES VERIFIED. Both actual local version-2 PNGs are 1410 × 2220 RGBA, nonblank and transparent, with brown names. Visible name remnants were removed. A small couples margin cleanup also changed nearby green/gold artwork pixels, so exact-art preservation is flagged rather than passed. Reduced chat/Library copies are not the production-size files. Supplier preview, safe-area approval, and physical print proof remain unverified; do not call the designs fully production-approved.

Use the exact observed route below only as a checkpoint guide. Re-observe the current UI; do not treat old control locations or account state as permanent.

## Product and approved originals

The owner supplied a ShineOn Graphic Journal FRONT specification of 1410 × 2220 px. No added bleed specification was supplied. Do not reuse those dimensions automatically for other variants.

Grandson original:
- Filename: Ethan.png
- Native: 1000 × 1573, RGBA; 1,161,516 bytes
- SHA-256: 1f8fd2f83bff746380eb99a53b74a98bb353a9e36c30ef372e347621067d9080
- Library identity: libfile_826cdfc87c2081919638a71f4926de0e

Couples original:
- Filename: Queen.png
- Native: 999 × 1574, RGBA; 1,697,296 bytes
- SHA-256: 6a010d9dd9142d8ffc0cc1a0754ff0db1341cd6f2e68ebde297cd4edbc7c89bc
- Library identity: libfile_adce241da37881919a294b0c27e44d65

Earlier generated name-removal trials introduced haze/ghosts and art drift, including changes near the cross. They failed preservation and were not substituted for these originals.

## Transfer route and recovery observed on 2026-10-06

1. The owner's Chrome showed an authenticated Canva home and an available Custom size control.
2. A Library transfer downloaded bytes, then its required helper failed on Windows because the attempted os.setxattr operation was unsupported. The incomplete transfers were not used.
3. The owner identified a separate local-originals folder. The task verified those files and used that explicit local route. This did not bypass the failed transfer or convert its partial bytes into approved assets.

Do not generalize this one failure to all Windows transfers. Use current supported tooling for a new task.

## Actual Canva route

- Create two new private custom designs at 1410 × 2220 px.
- Upload one approved original image per design.
- Preserve image proportions when fitting it to the canvas.
- With the image selected, open Eraser → Pixel Eraser. This was the observed control, not Magic Eraser. No paid prompt appeared for this step.
- Clear the baked-in name; checkerboard was visible in the erased area. This visual cue alone did not clear residual-mark QA.
- Add the replacement as a separate Canva text element.
- Verify the header states All changes saved and Only you can access.
- Keep these original-derived artwork layers and text layers separate.

Grandson master:
- Verified edit URL: https://www.canva.com/design/DAHXMHoUdBk/ifPpEuCNCpEWAg3rQYO9TQ/edit
- Image UI dimensions: 1410 × 2217.93; X 0, Y 1
- Editable text: Ethan
- Actual font/style: Libre Baskerville Bold
- Canva font-size value: 240; centered; Y 290
- Change test: Ethan → Noah → Undo; original value restored
- Intended/UI-reported color: #340e01
- Initial export result: glyphs actually black, RGB (0, 0, 0); text-color QA FAIL

Couples master:
- Verified edit URL: https://www.canva.com/design/DAHXMEdCv4k/7-cediCdtOUcpBRlcQFqMw/edit
- Image UI dimensions: 1408.97 × 2220; X 0.515, Y 0
- Editable text: The Bennetts
- Actual selection: Libre Baskerville Regular, then Italics applied to the full text
- Canva font-size value: 60; X 423.25, Y 1160
- Change test: The Bennetts → The Parkers → Undo; original value restored
- Intended/UI-reported color: #340e01; initial export brown verified
- Initial export result: tiny isolated marks left of the name; cleared-area QA FAIL

These fonts are observed Canva selections, not identifications of the original AI/raster font. The initial change/Undo tests established editable text. The later short/long-name checks are recorded below. Font-size units and unreported design titles were not independently captured.

## Actual initial export route and files

Observed UI settings:
- PNG, intended page
- 1×; 1410 × 2220
- High quality
- Transparent background checked
- Save download settings off

Canva showed completion. Automated download events timed out and blocked entries appeared in download history; the task honored the blocks. Those signals alone did not establish a saved file. The owner later provided independent local exports, which were inspected.

Grandson initial export:
- 1410 × 2220, RGBA, nonblank; light/dark inspection performed
- 2,362,920 bytes
- SHA-256: e4d218d61a0f8fd0b883ba25ace365ee665cd085dad3d9633934fce2d393e496
- Fully transparent pixel count reported: 2,225,103
- Metadata/transparency checks: PASS
- Intended name color: FAIL, actual black rather than #340e01

Couples initial export:
- 1410 × 2220, RGBA, nonblank; light/dark inspection performed
- 3,695,745 bytes
- SHA-256: f6faf21ffd8045eabb0d480dbbee69b9c8b3d486eb8a4c3aae8b6835eca86fb8
- Fully transparent pixel count reported: 1,871,611
- Metadata/transparency checks: PASS
- Brown name color: PASS
- Clean name area: FAIL, isolated residual marks at the left

## Repair and name-length evidence

Observed later on the same design URLs:

Grandson repair:
- Select ALL characters of the name and apply #340e01.
- Inspect the rendered name after leaving the selection highlight; it appeared brown.
- Preserve Libre Baskerville Bold, size 240, for the restored sample Ethan.
- Noah fit at size 240.
- Christopher wrapped at size 240; it fit one line at size 120.
- Undo restored the original sample. Do not assume all longer names fit 240 or apply 120 universally.

Couples repair:
- Select the artwork image and use Eraser → Pixel Eraser at a reported 125% inspection zoom.
- Clear the isolated marks. The wreath appeared preserved in the UI; later pixel comparison found the art-edge change recorded below.
- Keep the independent The Bennetts text italic, size 60, #340e01.
- The Lees and The Montgomerys fit at size 60.
- Undo restored the original sample.

Both revised export UIs were configured for PNG at 1410 × 2220 with transparent background; Canva showed Completed. No revised files or download paths were received at that UI checkpoint. The owner was asked to download the files. Later received-file inspection is recorded below; it must remain distinct from the UI settings and any original local export bytes.

## Received revised PNG evidence

The owner supplied two revised images to chat/Library. Their actual bytes were audited independently from the Canva UI:

Grandson received v2:
- Library identity: libfile_f809983a50f081918d1d6492b88af11e
- 1301 × 2048 RGBA; 1,546,405 bytes
- SHA-256: ae7533c1762656d4948ca979b686ce10308165a820ff9b030678b697017fd603
- 71,469 of 71,469 sampled fully opaque name glyph pixels were RGB (52, 14, 1), #340E01; zero opaque black in that tested region
- Right artwork clearance reported at alpha ≥ 32: 18 pixels

Couples received v2:
- Library identity: libfile_d1b03131bb248191b53b98cb05b4d865
- 1301 × 2048 RGBA; 2,328,197 bytes
- SHA-256: f217210d3562f787effa53742423fc5691ce98cafe19ab632f253612d8893711
- 4,352 of 4,352 sampled fully opaque name glyph pixels were RGB (52, 14, 1), #340E01; zero opaque black in that tested region
- Immediately-left name gap, x420–429/y1100–1139: zero nonzero-alpha pixels
- Wider adjacent botanical-edge region, x395–429/y1070–1169: 217 pixels at alpha 1–5; no pixels at alpha ≥ 8
- Right artwork clearance reported at alpha ≥ 32: 38 pixels

Both images had alpha minimum 0/maximum 255 and nonblank visible artwork. Light/dark composites showed correct name spelling, visually centered replacement names, and apparently preserved botanical design at that viewing scale. This was a visual appearance check, not pixel-identical preservation; the later local comparison identified a small art-edge change. No hard clipping was seen. Visible stray-mark QA passed; this is not a claim that every background pixel has zero alpha.

Result: corrected-color and visible-cleanup checks PASS; received-file dimension gate FAIL. Both hashes differ from the first-version exports. The aspect-ratio similarity does not establish why the files are smaller. Verify the local originals before diagnosing export versus transport. Do not silently enlarge the received files.

## Final local files and archive

A read-only check of the actual local version-2 exports established:

Grandson local v2:
- 1410 × 2220 RGBA; nonblank and transparent; name #340E01
- 2,365,334 bytes
- SHA-256: 79c9ee6dbeffee4400b66ba59a29a20790875911b4b9db38ca934924865fdbbd

Couples local v2:
- 1410 × 2220 RGBA; nonblank and transparent; name #340E01
- 3,694,659 bytes
- SHA-256: d555b5477f2bfc15ad8d0e6852a23437784f48c5f136b88b0f63e54f0bd5f30d
- The two previously observed mark locations are fully transparent.
- Cleanup changed 1,342 pixels in a small margin rectangle, including some green/gold art-edge pixels. Outside that rectangle, the comparison was identical to version 1.
- Flag the art-edge alteration. Do not claim pixel-identical preservation or that only unwanted name remnants changed. The user was informed of this limitation; approval of the alteration is not established by disclosure alone.

A local archive containing the two PNGs and a manifest was verified:
- 6,044,598 bytes
- SHA-256: 0108e559515d91f3da1b689844609fee6fcccbb5ace8d6adbd2fb82049d4b515
- Both PNG members were checked against the actual local files.
- Archive verification establishes this package's contents; it does not by itself prove that a recipient received byte-identical files.

The local files meet the pixel-dimension gate. The earlier 1301 × 2048 chat/Library copies do not. Why those received copies differ is UNCONFIRMED; do not label either Canva or the chat service as the established cause. Use the measured full-size local originals and verify any delivered/extracted package against their hashes.

## Remaining gates

- Treat the two Canva links as editable masters and the full-size local PNGs as verified export files, with the disclosed art-edge caveat.
- Confirm that the final delivery route preserves the measured local PNG bytes. Do not substitute the reduced chat/Library copies or reuse their hashes as full-size evidence.
- Obtain the user's decision before treating the couples art-edge alteration as approved, or restore that edge from the preserved original if requested. Keep the file review-only for exact-art-fidelity purposes until resolved.
- Re-check all fixed wording against the originals and record saved-state persistence/reopen evidence where not already observed.
- Keep supplier safe-area/preview and any necessary physical print proof pending. Narrow artwork margins have not been approved by the supplier.

The source raster detail remains 1000 × 1573 and 999 × 1574. The fitted artwork and full-size exports are resampled from those native originals; larger dimensions do not add native detail.

## Inspector validation scope

The bundled read-only inspector passed 14 synthetic tests: transparent/opaque/blank cases, dimension and format mismatch, larger export vs source, misleading partial transparency, opaque/transparent/out-of-bounds pixel probes, and expected delivery-hash matching/mismatch. These validate file-inspection logic only. Actual Canva correctness depends on the observed checks above.
