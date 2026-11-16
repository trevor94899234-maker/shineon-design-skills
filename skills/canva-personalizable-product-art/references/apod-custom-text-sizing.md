# Native APOD custom-text sizing

Revision 2026.10.17.1. Owner-requested workflow, applied to each authorized product rather than a blanket retrofit of existing listings. Preserve approved fixed art, product-specific field contracts and original geometry for rollback. Native APOD text-field geometry is technical personalization work, not a substitute for the owner's image-generation requirement for new art or complete UGC thumbnails.

## Choose and execute

1. Record product/artwork/variant, selected native text layer, current text, font/style/size, alignment, geometry, actual print-safe area and neighboring elements. Verify current SKU template; editor pixels are not physical print units. Measure usable space before assuming the existing narrow box is the maximum. Expand/reposition only within approved layout space, without covering art, crossing bleed/safe boundaries or silently redesigning fixed art.
2. Inspect the actual native controls and record their labels. The two approaches are:
   - Fixed usable box, dynamic font: keep the approved available region and fit the entire input by font scaling. Choose a generously usable region first. Reject excessive shrinking below a documented per-product readability floor; a fitted string is not automatically an attractive or printable name.
   - Fixed font size, reserved expansion space: set the intended size and allow the text to occupy the space it needs within the deliberately designed area. Verify actual expansion direction, alignment, wrapping, clipping and edge behavior. Never assume this mode grows a safe box or prevents overflow. If a long input exceeds available space, adjust the authorized size/placement, choose dynamic fitting, or flag the exact input for review; do not truncate it silently.
3. Test a short, normal and realistically long input, including spaces or punctuation supported by the actual SKU. Check the rendered canvas changed, not only the form value. Check all characters, prominence, minimum legibility at intended print size, alignment, overlap, clipping and safe margins. Retain actual test strings and evidence. An 11-character sample is not a platform or universal product maximum. Only publish an input limit if that SKU's saved configuration and supported behavior substantiate it.
4. Restore the intended default text and chosen mode. Save through the authorized private-product workflow, reopen and verify text, mode, geometry and original art. Record unsaved trials separately from persisted changes. Do not repeatedly click save when the outcome is uncertain.
5. Inspect the actual supplier mockup separately. Identify the name it shows; a default-name mockup does not prove a long-name supplier render. Keep native-editor tests, supplier previews and physical print proof distinct. A readable editor preview or APOD Ready badge does not close rights, full fulfillment or release gates.

## Dated evidence and limits

Owner's spoken instruction on 17 October 2026:
“所有產品嗰個,打字個闊度呢,空間呢,都係可以,一係就,兩個選擇嘅,一個呢就係限制個框框,完成晒所有個字,無論幾大幾細,佢就會按住大小而變化,另一個呢就係,定咗個字嘅size,然後,就如果多啲字嘅話就壓多啲位,咁啊係個設計上要預留啲位,咁就得㗎啦,有兩個方案,佢哋呢個,anyway, POD係有兩個選擇俾我哋用嘅,寫死落去個,流程裡邊囉,execute到”

Observed 17 October 2026, Dad private product 621604 / artwork 1593211, cloud APOD native editor: text layer → More options → Personalization → Font Size exposes **Dynamic** and **Pre Set**. This is a dated observation of that editor/SKU, not a guarantee for every APOD product.

- Saved Dynamic geometry changed from width301/left100 to width391/left55, height71/top370/angle0 unchanged, base font shown53. Center stayed250.5; width increased29.9%. AL, CHRISTOPHER and CHRISTOPHER JAMES fit the expanded native canvas without observed overlap/truncation; the17-character sample became more prominent than in the old narrow band. No universal maximum was set.
- Temporary Pre Set inspection exposed Size53.402502. The17-character sample overflowed the box and page sides, touching the border. This is a negative test, not an approved fixed-size configuration. The failed trial was not saved; reload verified DAVID, Dynamic selected and Pre Set unselected. In this centered layer the overflow extended both left and right; do not generalize that direction to other alignments.
- Saved-default DAVID mockup was downloaded and inspected; it preserved the art and showed no overlap. It was not a supplier-rendered17-character test. Print-scale physical proof remains open.

Source receipts: product https://app.anywherepod.com/admin/products/621604 ; execution evidence `evidence-20261017-0829/Dad621604-expanded-name-readback.md` and `Dad621604-free-name-QA.md` in the task's cloud workspace, and `APOD-two-text-fit-modes-verified.md`. These evidence filenames are provenance, not a required future local filesystem path. Re-inspect actual current controls if unavailable or changed.

## Regression checks

- Long name fits a narrow box only by becoming tiny: review available area before accepting; retain readability gate.
- Pre Set text extends beyond page: FAIL, do not save as approved; explicit reserved space is required.
- Input field changed but canvas did not: NOT TESTED, trigger supported actual input/render and inspect again.
- Dynamic short/normal/long canvas passes; default supplier mockup only: record canvas PASS and long-name supplier proof NOT CHECKED separately.
- All products instruction: apply this checkpoint when working on each authorized SKU; no automatic bulk edits, publishing, price changes, rights assumptions or restriction bypass.
