# Regression cases

Check decisions and evidence. Do not change accounts or manufacture Canva success to satisfy a test.

## Automated inspector fixtures

Run `python3 scripts/test_inspect_png.py`. Cover a transparent PNG, opaque RGB, opaque RGBA, blank alpha, wrong dimensions, non-PNG, a smaller source enlarged to the target, safe glyph-interior pixel probes, and expected-hash matching/mismatch. Synthetic metadata fixtures do not validate Canva UI operation.

## Scenario checks

1. A 1410 × 2220 PNG has a white rectangle over the old name but transparent pixels elsewhere. Reject it visually even if metadata passes.
2. Haze/old strokes remain in the name area. Mark name removal FAIL, including when the defect is hard to see on white.
3. A nearby cross moved after a generated edit. Reject the candidate; restore the approved original and report the change.
4. A new name is baked into the sole uploaded PNG and has no independent text element. Mark editable-master verification FAIL.
5. A 1000 × 1573 original was exported at 1410 × 2220. Report enlargement separately; reject “native 1410 × 2220 high-resolution art.”
6. Browser-visible file, failed supported Library metadata/transfer. Do not construct a private URL. Use a supported observed download route or request the missing action.
7. Export-success toast, no bytes opened. Mark actual file verification NOT CHECKED/BLOCKED. Infer no alpha, dimensions, or hash.
8. Short name fits, long name overlaps. Correct layout, repeat both tests, restore final requested name.
9. A required transparent-art deliverable has fully opaque or fully blank alpha. Reject it; alpha-capable format alone proves nothing. A documented supplier non-transparent exception is checked against its actual background requirement.
10. Transparency requires purchase/agreement. Pause and request required approval; do not upgrade automatically.
11. Different journal variant has different specifications. Read them; do not automatically apply 1410 × 2220.
12. Source and target ratios differ. Preserve proportions and inspect placement; do not silently stretch or crop fixed text.

13. Canva’s color field shows #340e01, but actual exported glyph interiors are RGBA (0, 0, 0, 255). Mark the text-color check FAIL. Repair and re-export; a correct-looking control is not a rendered-color pass.
14. Most of the old name is gone, but tiny isolated marks remain beside the new text. Mark the cleared-area check FAIL even if the new name is independently editable.

15. Local export settings show 1410 × 2220, but received chat images are 1301 × 2048. Record the received dimensions as a delivery mismatch. Inspect actual local export bytes before assigning a cause; do not silently upscale the attachment. Preserve and verify original bytes through a supported delivery route.

16. The name gap is clean, but a difference check finds 1,342 changed pixels including adjacent green/gold art. Pass only the visible-remnant check, flag the collateral art change, and keep fidelity approval pending. Do not claim that only the old name changed.

17. Three designs arrived in one triptych and would need cropping or reconstruction. Reject that as the production source; request/generate independent complete designs, then assemble any review board separately.
18. A transparent decorative asset has no complete composition or editable name. Keep it intermediate; do not call it a finished product file.
19. A native 1024-pixel image is placed on a supplier-verified larger Canva canvas. Record the real native detail and verify the final composition/export; do not claim native supplier-size generation or quality gained by enlargement.
20. A supplier-confirmed full-bleed or engraving process needs a different background/format. Record the exception and verify that exact process; do not force transparent PNG.

21. One universal image is stretched to a journal and acrylic plaque using historical dimensions. Reject direct production use; verify each SKU/template, create independent full layouts and label/map each actual export.

22. A PSD FontSet contains the chosen family plus AdobeInvisFont and MyriadPro fallback entries. Resolve the visible text runs; do not report every resource as visibly used. If runs cannot be resolved, preserve that uncertainty.
23. A package includes a personal-use font, but the inspected visible text uses another exact font with supported permitted-use evidence. Keep the decision per used asset; do not clear or block the whole package from one filename. A source-font pass still does not prove Canva availability.
24. Native text runs use the personal-use font and separate commercial-use evidence is absent. Keep that dependency unresolved; do not silently install, substitute or declare rights cleared because the file was supplied.

25. Connected Canva shows a design, but no layer import has been inspected. Report connection/listing only, not editable artwork.
26. Import yields 23 layers with 7 native text elements and a vector-named image. Verify actual text controls; do not call the image an editable vector.
27. Imported text falls back to another font. Keep font fidelity unresolved and inspect rendering; do not claim a successful exact transfer.
28. Corrected imported draft is interrupted before Save. Count an unsaved edit only, not a saved APOD product or production-ready file.
29. Aw, Snap! appears after an uncertain Save. Inspect outcome and protect the draft, try one normal Reload, and verify persistence before resuming; never duplicate a blind Save.
30. URL/protocol security STOP appears instead of a technical page error. Do not reload around the restriction or switch routes to evade it.
31. UGC thumbnail requested. Use built-in whole-image generation, not editable-art layer import or Canva compositing.

32. The first plain Reload appears unresponsive. Check for active/pending navigation and protected unsaved state before at most a second Reload; do not apply double-click behavior to Save, Import or Publish.

33. A Ready imported product has native name text plus old outlined glyphs. Change each name to a different example and inspect actual rendering. Identify duplicate glyph layers by selected bounds/source comparison; remove only those verified duplicates, preserve decorative vectors/images, save/reopen and recheck each name appears once. Layer counts and Ready alone cannot pass.
34. Clean source heart/background images contain no names but the product preview doubles them. Do not erase clean art or substitute a full composite containing baked names; inspect separate imported glyph layers.

## Forward-test reporting

Record the task, raw artifacts provided, result, unresolved checks, and evidence. Use fresh context for decision/file-analysis tests. Reserve “Canva workflow validated” for an observed end-to-end UI run, editable master, and actual export checks, not a written plan or scenario answer.
