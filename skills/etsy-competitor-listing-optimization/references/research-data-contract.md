# Research data contract and executable checks

Use these fields as a sidecar contract; do not silently migrate an established Dashboard or research packet. Preserve existing raw columns, source IDs and canonical keys. Build an explicit mapping when importing an older schema. The bundled template starts empty so it cannot be mistaken for researched data.

## Stable identity and provenance

- listing_key: `etsy:listing:<numeric_id>`; canonical_url: `https://www.etsy.com/listing/<id>`.
- shop_key: `etsy:shop:<numeric_id>` when known; otherwise `etsy:shopname:<casefolded_name>`. Keep aliases when a verified shop ID becomes available. Do not create a second shop or rewrite joins blindly.
- source_id: stable run-local identifier. Retain source_url, captured_at with timezone, method, market_scope, raw_file and SHA-256. Every claim/metric references a source_id.
- raw remains immutable. A source `text` map holds exact selected fields (title/description/age/review/etc.) copied from raw for quote checks. This is not a substitute for the raw capture. Record permitted decoding explicitly and preserve both forms.
- Never replace entity/source IDs with row numbers. Save capture time separately from normalization/review time.

## Minimal bundle

Top level: schema_version, run, sources, shops, listings, metrics, claims, inventory_pages, qualifications, keywords, corrections, social_accounts, qa.

`run`: run_id, mode research_only/listing_draft/authorized_application, stage draft/delivery, buyer_country, currency, language, collected_at, min_qualified_shops (integer/null), candidate_goal (integer/null), target_decision, inventory_expected (integer/null), inventory_stop verified_end/partial/not_requested, inventory_snapshot_id, scope_notes.

`sources[]`: source_id, source_url, captured_at, method, market_scope, raw_file, sha256, text object. Raw files may be outside delivery, but must remain available to reviewers. `--source-root` verifies their bytes and hash; without it, byte integrity is not checked.

`shops[]`: shop_key, shop_name, shop_id (string/null), source_id, age_raw (string/null), age_years (number/null), seller_location (string/null), observed_at. Age values always retain the raw string and source.

`listings[]`: listing_key, listing_id, shop_key, source_id, observed_at, title, description, tags array/null, tags_provenance, comparator_class direct/adjacent/excluded, selected (boolean), detail_captured (boolean), price_raw, price, currency, variant, quantity, shipping_raw, shipping_cost, shipping_scope. Missing strings/numbers use null, not fabricated defaults. Keep images captured versus actually viewed separately.

`metrics[]`: metric_id, entity_key, metric, source_id, raw_value, value (number/null), status observed/estimated/missing/unavailable/conflict, qualifier exact/less_than/greater_than/range/null, entity_scope shop/listing/query, period, market_scope, definition, caveat. Missing/unavailable values must be null. Shop_sales_cumulative must have shop scope and lifetime/as_displayed period; estimated fields stay estimated regardless of source verification.

`claims[]`: claim_id, entity_key, claim_type recipient/sender/buyer/writer/eventual_reader/deceased/material/process/occasion/other, value, status supported/unknown/conflict/hypothesis, source_id, source_field, quote, polarity positive/negative/conditional/quoted/unknown, target, reviewer, reviewed_at. A supported label requires exact quote in the referenced field, correct entity and reviewer. Negatives, options and quotations are not automatically positive cover facts. Claim status is a human/agent judgment, never a regex result.

`inventory_pages[]`: snapshot_id, page_key, previous_page_key (null for first), listing_ids array, displayed_count, observed_at, source_id. Keep raw duplicates; derived unique count removes them. Page sequence must end at verified_end; cursor repetition fails.

`qualifications[]`: shop_key, status well_supported/provisional/candidate/adjacent/excluded, comparable_claim_ids, relevant_product_evidence_ids, success_metric_ids, rationale, caveats, reviewed_at. Relevant product evidence IDs may cite supported claims that document linked journal reviews/catalog context, not merely an unrelated total. well_supported requires both comparable evidence and scoped success corroboration, with a reasoned reviewer decision; scripts cannot judge sufficiency.

`keywords[]`: keyword_id, phrase, normalized_query, provenance measured_exact_query/actual_listing_tag/own_listing_term/observed_wording/hypothesis, source_ids, metric_ids, decision accept/reject/hold, decision_reason, intended_field research/title/tag/description/category/attribute/image, coach_source_ids. Only measured_exact_query can carry demand metrics as its own; a tag with separately measured exact data can have a separate measurement record. Keep observed term provenance too. Use etsy-keyword-pool-cleaning for large export normalization without changing raw qualifiers.

`corrections[]`: correction_id, entity_key, field, before, after, source_ids, quote, reason, reviewer, corrected_at, affected_outputs. Preserve old IDs and all versions.

`social_accounts[]`: shop_key, platform, account_url, identity_status verified/likely/unverified, identity_evidence_source_ids, relationship_reason, access_status opened/not_opened/blocked/private_excluded, activity_status verified/unverified, observed_at. A verified association needs evidence; private personal profiles are excluded. Exhaustiveness is not asserted.

`qa`: extractor, independent_reviewer (null if unavailable), semantic_status pending/passed/blocked, audited_categories, errors_by_category object, expanded_categories, category_audit_complete object, semantic_audit_ref, source_integrity_status pending/passed/failed, output_checks array of {artifact, check, passed: true/false}, limitations. Delivery stage requires nonempty distinct extractor/reviewer names, a semantic audit evidence reference, audited categories, passed source-integrity status and explicitly true output checks. Incomplete/unverified scope stays draft with clear partial status; never label it fully verified delivery. Each category with errors must appear in expanded_categories and have completed full affected-category review before delivery. Reviewer identity must differ from extractor. A nonempty name alone is not proof: retain its audit artifact/source comparisons.

## Commands

Run from the skill directory, using absolute paths for task artifacts:

```text
python3 scripts/research_checks.py age '1.5 years on Etsy'
python3 scripts/research_checks.py inventory /path/to/research_bundle.json
python3 scripts/research_checks.py validate /path/to/research_bundle.json --source-root /path/to/raw-parent
python3 -m unittest discover -s tests -v
```

Exit 0 means covered deterministic checks pass; exit 1 means validation errors (including wrong field/container types); exit 2 means unreadable files, invalid JSON or usage errors. Output JSON includes limitations. `age` returns needs_review for ambiguous text and never guesses. `inventory` reports counts without changing records. No helper uses credentials, network, browser controls, or shop-write tools.

## Joining later exports

1. Preserve original CSV untouched and SHA-256 it. Label native export versus UI transcription and source/version.
2. Inspect real headers; record field mapping, data types, units, tool metric definitions, actual market and date/window.
3. Join listing/shop data on canonical IDs. For keyword data join normalized exact phrase plus compatible platform/country/window; never join only on similar wording.
4. Retain both observations on conflict. Do not average incompatible periods or overwrite Etsy counters with third-party estimates.
5. Add new measured rows with source IDs and keep prior evidence. Missing fields stay null. Re-run decision and qualification checks only where affected.
6. Regenerate all requested formats and replace the same Library items using retained version guards. Record per-file result; partial upload is partial delivery.
