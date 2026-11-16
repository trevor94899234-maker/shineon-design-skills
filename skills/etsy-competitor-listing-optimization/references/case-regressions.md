# Historical research faults and regression targets

This is the corrected MyGiftStyle Christian family/friends gift research captured on 2026-10-05, not live inventory and not universal sample-size or success requirements. The available delivered JSON tables and correction audit were inspected while building this module. Earlier original raw directories were no longer mounted; do not claim they were freshly reread. Raw preservation is therefore a mandatory future workflow gate, not a claim that unavailable files were recovered.

## Counts and limits

- Fresh owner inventory: 77 unique active listings over 36 + 36 + 5 cards, then 77 detail records. An earlier web result crawled the prior week showed 126. The reason for the difference was not established; do not infer deletion/archive/activity changes.
- Connected detail batch requested 77 but returned a capped subset; actual response lengths had to be checked, then remaining batches completed. Never assume requested count equals returned count.
- Captured candidate shops: 83. Presentation main pool: 50 shops. Selected listings for the 50-shop pool: 53. Deep competitor listing records: 88. First-page competitor cards: 1,389, explicitly partial inventory.
- Re-audited shops: 27; well-supported comparators: 22; provisional: 5. User goal for that run: at least 20. Do not call all 50 main-pool shops independently successful or require 50 in another run.
- Exact listing tags came from connected detail responses. They did not contain keyword demand, volume, profit or actual selected-listing sales.

## Faults that structural QA missed

1. Ten shop-age fields changed: nine fractional-year parses and one month conversion. “1.5 years” was previously parsed as 5. Fix the full number and retain the dedicated display field.
2. Twenty-two listing rows needed material/finish corrections. Optional engraving, negative claims, accessory targets and words in shop names require sentence/subject reading.
3. All 88 recipient/sender rows were semantically reviewed and standardized. This does not mean all 88 original labels were wrong. Preserve multi-role, giver versus recipient, writer versus eventual reader and deceased/grief context.
4. All 165 owner/competitor price-currency pairs were verified unchanged in that audit; 77 explicitly sourced owner shipping zeros were added with US/tool-context limitations. A missing value was not simply filled with zero.
5. Counts, links and workbook formatting had passed earlier. Their pass did not catch semantic faults. Require independent raw-source sampling, then expand any failed category across the affected population.
6. Review counters from the detail connector could be shop-wide. Selected items with zero reviews remained zero even when related journal reviews supported the shop-level comparison.
7. A visual evidence object is not proof an image was inspected. Explicit visualVerified=false remains unverified. Denied image checks and canceled source calls were not retried through alternative routes.
8. Native monetary values may use amount/divisor. Preserve both and divide only by a verified positive divisor; currency and variant stay attached.

## Product-truth regression examples from owner corpus

- Listing IDs 4518229340, 4518229112 and 4518229530 contained guided-storytelling claims while the owner-confirmed SKU was lined-only. Flag the product-truth conflict before keyword optimization; do not silently change the live listing.
- Listing 4517034664 explicitly offered two journals for USD 89.95. A different “parents set” title with USD 49.95 starting price is an option/quantity question, not automatically a pricing error.
- Listing 4367038818 was a 50th-birthday journal with the observed tag “friend 40th tea cup”. Reject the wrong occasion and product type; tag existence does not establish suitability or demand.
- Four exact-title pairs also had identical tag arrays and were overlap candidates. They did not establish actual traffic cannibalization or authorize deactivation.

## Reproducible source references

User-owned research artifacts: Christian_Family_Gift_Competitor_Research.xlsx, Competitor_Gallery.html and Competitor_Research_CSV_JSON.zip. Resolve current versions in Library rather than relying on this historical version. Relevant tables: Owner inventory, Listings, Shops, Coverage, Qualification audit, Qualification impact, Correction log, Correction QA; material_finish_audit.json and correction_summary.json preserve detailed findings. All share canonical IDs. Do not expose private capture paths in user-facing exports.

Execute bundled regression tests for numeric/scope/identity guardrails. For semantic forward testing, give an independent agent raw title/description/role examples plus this skill, without supplying expected labels. Inspect its exact claim quotes and uncertainty states, not just whether it produces the desired count.
