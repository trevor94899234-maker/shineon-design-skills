# Large-export helper and source profile

## Choose execution mode
Use pure computer use for selecting scope, observing headers, downloading authorized exports, opening outputs and visual spot checks. For hundreds of thousands of rows, use a deterministic bulk engine; do not imply screen-by-screen cleaning is practical or verified. The included helper requires permitted local Python 3 file execution. XLSX output additionally needs `xlsxwriter`; if absent, keep NDJSON/audit output or use an authorized existing workbook tool. Do not install software or access another machine without the required permission.

The bundled classifier implements the five-library taxonomy below only. If the current task requests a different taxonomy, do not silently substitute these five libraries; use an authorized reviewed mapping/UI workflow or adapt and test the helper for that requested taxonomy.

Read the helper before first execution if its behavior materially matters. Inputs are read-only. Output must be a new directory outside the input tree. No network, credentials or shop writes are used. File timestamps are reported in UTC, a deliberate improvement over the historical machine-local timestamps.

## Prepare scope JSON
Create this from verified source headings/settings, never guess a market from the user's residence:

```json
{"default":{"platform":"Etsy","country":"US","language":"en","metric_period":"2026-09","source_tool":"eRank","metric_definition":"average monthly searches; exact source definition verified"},"files":{"export.csv":{"explicit_export_date":"2026-10-03","encoding":"utf-8-sig"}}}
```

Use a `files` override whenever a source differs. Required keys are platform, country, language, metric_period, source_tool and metric_definition. They all participate in the dedupe key; different tools or metric definitions are never pooled automatically. Missing/unknown required scope blocks that file. If all export dates vary but period means rolling average, record that actual definition; do not falsely call it a calendar month. Mixed or ambiguous matching metric headers block the file until an explicit `field_map` maps canonical fields to actual verified header strings, for example `"field_map":{"searches":"Average Searches USA"}`. USA-labelled fields cannot populate a non-US scope. Generic headers require independently verified scope. `explicit_export_date` must be ISO YYYY-MM-DD and evidenced. Otherwise a valid first YYYYMMDD token in filename is used, then actual mtime as a labelled UTC proxy. The helper only scans immediate `.csv` files, not subfolders. Inventory nested inputs separately and explicitly choose scope before staging copies.

## Run
Replace every bracketed path with a verified accessible path. Do not literally run placeholders.

```text
python3 [skill]/scripts/clean_keywords.py --input-dir [raw_csv_folder] --output-dir [new_run_folder] --scope-json [verified_scope.json] --date-policy effective-latest --xlsx
```

`--date-policy` is mandatory:
- `effective-latest`: compare explicit date or mtime-proxy date, then mtime; matches the historical cleaner's date concept while making timezone explicit.
- `explicit-first`: prefer any explicitly dated source over proxy-only sources, then newest effective date. Use only when the current run specifies this preference.

Default `--unknown-policy exclude` excludes a winning unknown-volume observation from the active library, but keeps its original evidence and disposition in audit. It never fills it with an older known-volume row. Use `--unknown-policy retain-review` when the user wants missing-volume candidates in the review file. Neither mode silently calls an unknown zero. `--english-only` is off by default; enable only for explicitly English-only noise filtering. Without it, non-Latin alphabetic keywords are retained, generally for classification review.

## Outputs and verification
- `selected.ndjson`: active selected rows, with raw fields, parsed metric status, scope, provenance and rule-based category.
- `audit.ndjson`: every processed data row and disposition, including duplicates, placeholders and excluded latest-unknown rows.
- `review.ndjson`: conflicting tied observations, unparsed volumes, or requested retained-unknown records.
- `manifest.json`: per-source status/errors/header map/date/scope, counts, corrections and quality state.
- `audit.sqlite`: local working evidence store; not a substitute for deliverables.
- With `--xlsx`, five new workbooks under `workbooks/`, each `Keywords`, `Overview`, `Source Files` in that order. The Keywords sheet has 25 columns: the historical first 18, a UTC timestamp column replacing local timestamp, then Platform, Country, Language, Metric Period, Source Tool, Metric Definition. These extra fields prevent unsafe cross-market interpretation.

Observed numeric metrics are numeric spreadsheet cells for sorting; threshold/missing strings stay text. Exact raw tokens remain in NDJSON/audit, and percent display uses source units.

Exit 0 means automated structural gates passed, not visual/live-UI verification. Exit 2 or manifest PARTIAL/BLOCKED/EMPTY requires inspecting source errors/review/counts; do not deliver as complete. Empty/no-supported-source runs are never COMPLETE; empty workbooks are not generated. Malformed CSV rows are preserved with raw fields and reason; unread remainder is explicitly unknown. Source-file errors may leave successfully read rows in audit but make the run PARTIAL. Fix the source mapping/encoding with evidence and rerun into another new directory. Never delete or overwrite the raw source to make the tool pass.

Read the manifest, verify count invariant, read selected and rejected examples, and open every workbook if a spreadsheet UI is available. Inspect first/middle/last rows, <20, 0, latest-unknown exclusion, source links, filters/frozen headers and column legibility. If visual opening is blocked, label visual QA unverified; retain structural evidence. Deliver all required files via a supported attachment/link, not just a filesystem path.

## Confirmed historical pipeline, 2026-10-04
The user's ALL CSV project had 714 sources / 530,174 rows. Its manifest recorded 120,617 distinct keys before filtering, 409,557 duplicate rows, 426 latest unknown-volume removals, 49 noise removals and 120,142 retained rows. These are historical audit numbers, not expected counts for new data.

Historical broad libraries:
1. Occasions, Faith & Holidays: Faith & Religious; Wedding & Anniversary; Birthday & Milestones; Seasonal & Holidays; Memorial & Remembrance.
2. Recipients & Relationships: Family & Relationships; Pet Gifts.
3. Products & Personalization: Journal & Stationery; Personalized Gifts.
4. Gifts & Keepsakes: Gift Ideas.
5. Needs Review (TBC): Unclassified or unknown category.

Classifier uses first matching specific category in the order above, retaining all matches as theme tags. It is a heuristic, not semantic validation. The helper corrects the original birthday backspace/word-boundary bug and substring matches such as `cat` inside unrelated words. Preserve ambiguous/short words for owner review rather than declaring them meaningless.

Historical normalization trimmed/lowercased/collapsed whitespace and preserved punctuation. Keep this default for continuity. Historical cleaner deduped globally, did not partition markets, decoded invalid UTF-8 with replacement, silently skipped some bad headers and counted empty strings in same-date quality. The helper deliberately fixes those defects: scope-keyed dedupe, strict decoding, registered errors, nonempty/valid completeness scoring and conflict review. Do not present the original run as having these fixes. There is no exact bug-for-bug compatibility mode.

Historical positional `records.ndjson` and `cleaned_records.ndjson` have different schemas (20 versus 21 fields); the helper accepts raw CSV only. Do not feed either NDJSON into the CSV importer. To reuse archived intermediates, inspect the generating code and manifest, map by verified index into the current contract, and validate separately.
