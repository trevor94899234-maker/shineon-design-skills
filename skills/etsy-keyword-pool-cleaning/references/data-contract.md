# Keyword data contract

## Run settings
Record: run_id; requested_at; platform; country; metric_period; source_tool; metric_definition; product_fact_source; input_locations; output_location; taxonomy; date_policy; normalization_policy; mode (UI/helper/hybrid); coverage_limit. Confirm scope before applying historical settings.

## Row schema
- keyword_raw: original text, unchanged
- keyword_normalized: trim, collapse whitespace, lowercase; preserve punctuation, matching the verified source pipeline. Treat any stronger Unicode or punctuation normalization as an explicitly documented change
- platform, country, language, metric_period, source_tool, metric_definition: required comparability keys; unknown blocks cross-source selection until resolved
- source_type: keyword_export / listing_export / own_listing / manual_observation
- source_id, source_filename_or_url, source_row, source_row_basis (CSV logical record including header / displayed data row / physical line / unknown), captured_at. Do not convert a screenshot display row into a claimed physical CSV line. Preserve visibly quoted leading/trailing spaces in keyword_raw; normalize only the separate key.
- explicit_export_date; file_modified_at; observation_date; date_basis (explicit/proxy/unknown)
- provider_last_updated: exact provider field and its stated meaning, separately from captured_at/export/file timestamps; unknown meaning stays unknown
- metric_window and monthly_points: retain averages and individually labelled month/value points as separate observations; record the window/qualifier for each, never overwrite one with the other
- metrics_raw: exact source values and headings
- metrics_parsed: separate numeric value/operator/status for each metric; status observed/missing/threshold/unparsed/text
- library, subcategory, classification_reason, confidence
- selection_status: selected / duplicates / review / rejected (conflict is a review reason)
- selection_reason; all_source_occurrences

Do not create missing observations from memory. A keyword_raw value equal to the placeholder Unknown is rejected as a non-keyword; an unknown source/date field is a provenance/review issue, not automatic rejection of a valid keyword; a valid keyword with an Unknown metric is preserved in audit with metric status missing. For the active library, apply the configured missing-search-volume policy only after selecting latest; never use an older row to hide the latest unknown. Zero is observed zero, not missing. `<20` is threshold evidence, never exact 20 or 0.

For example, an Avg Searches value and a Sep 2026 trend point read on 15 October are three distinct facts: average, named month and capture date. A saved list's Last Updated label does not establish that every metric was measured that day. Do not promote any of these into current-month demand without the provider's actual definition. Keep the raw headings and date semantics even when the output view is compact.

## Date selection
Use the run’s explicit policy; the verified historical source uses effective-latest: use explicit export/observation date when parseable, else file modified time marked proxy, else unknown. Do not treat the file modified time as a real observation date. Record timezone/granularity; do not invent clock times. Compare rows only within compatible source/market/metric scopes. For equal effective dates, compare recorded modification timestamps (UTC in the new helper), then known-search-volume and populated-metric quality only for exact timestamp ties. Equal-priority differing metrics go to review. Explicit date and proxy precedence across different files must be declared in run settings before selecting a winner. A proxy-only file may win under explicit effective-latest policy, but that is not proof its metrics are newer. If files were recently copied/touched, establish actual export dates or use an explicitly agreed alternative; disclose proxy winners.

## Workbook and audit output
Keywords: one selected row per comparable normalized keyword key; all required fields, raw metrics and provenance reference.
Overview: scope, taxonomy, date/normalization rules, input and output counts, category counts, qualifier counts, unknowns, conflicts, exclusions, caveats and quality-gate result.
Source Files: one row per input, identifier, type, date/basis, headers, row counts, processing status and errors.
Audit: one source-row record per input row with final disposition and selected key; preserve duplicates and exclusions outside the selected view.
Review: tied observations, uncertain taxonomy, incomplete market/date/schema and product conflicts.

Count invariant: input data rows = selected source rows + duplicate source rows + rejected source rows + unresolved source rows. If one source row appears in more than one classification view, do not double-count it in this invariant. Header/blank lines must be counted separately and consistently. Missing files are not processed rows.

## Disposition consistency
The selected output contains only selection_status selected. Review rows go in Review; exclusions and duplicate rows remain in Audit, not the active selected sheet. Every record has exactly one primary disposition across all outputs. Reconcile counts using those dispositions before delivery. Classification uncertainty is a separate flag and cannot silently change a selected row into a review row in only one file.
