---
name: etsy-keyword-pool-cleaning
description: Clean, deduplicate, classify, and audit Etsy keyword pools from research-tool exports or spreadsheets, retaining metric qualifiers and source provenance. Use for repeated keyword-library maintenance and computer-use export workflows; not for publishing shop listings.
---

# Etsy Keyword Pool Cleaning

Revision: 2026.10.15.1. Add durable per-batch checkpoints and explicit metric/date separation after the October recovery audit; retain the existing normalization, selection and historical-library policies.

Produce a traceable research library, not a list of plausible keywords. Work on copies and keep every raw export unchanged. Follow the numbered states in order. For computer use, read [references/computer-use.md](references/computer-use.md) first. Read [references/data-contract.md](references/data-contract.md) before processing rows. For bulk exports or this user’s historical ALL CSV workflow, read [references/helper-and-source-profile.md](references/helper-and-source-profile.md); it defines the tested helper, exact prerequisites, five-library mapping, and documented corrections.

## State 0 — Scope and inputs
Record user request, target shop/product, platform, country, period, source locations, desired output, classification taxonomy, and authority to save outputs. Separate current instructions from historical settings. A historical 714-file run does not mean today's run has 714 files. Never assume Amazon ASIN terminology applies to Etsy.

Identify available paths: visible research UI/spreadsheet; supplied exports; permitted deterministic helper. Do not assume shell/Python is available. If the data is too large for reliable UI processing, ask for a supported export/helper environment or explicitly offer a bounded sample. Never claim hundreds of thousands of rows were cleaned by inspecting several screens.

## State 1 — Inventory
Open each authorized source location. Record exact filenames/IDs, source tool, source type, country/platform/period, explicit dates, modified times, row counts, columns and coverage. Record unavailable files separately. Preserve raw originals. Create a new dated output destination; do not overwrite prior deliverables silently.

For multi-batch live collection or recovery after a workspace restore, apply [durable collection checkpoints](references/durable-collection-checkpoints.md) before the next query. Reuse compatible saved raw observations first; a missing aggregate packet does not authorize re-querying or reconstructing its rows.

## State 2 — Map columns
Inspect actual headers and five representative rows per distinct schema. Map headers to the contract. Keyword-tool exports, competitor listing exports, and user's own listing data are different source types. Do not merge listing titles into keyword queries. Stop a schema group when keyword field or metric meaning is ambiguous; retain it in rejected_sources with reason.

## State 3 — Normalize and qualify
Preserve raw keyword and metric text. Build the normalized key using the contract. Exclude blank/placeholder keywords with a reason. Preserve all real keywords in the audit; under the historical active-library policy, a winning missing-search-volume row is excluded from the active library after dedupe and retained with its reason in audit. Never backfill it from an older row. Other missing metrics remain missing; alternative retain-review behavior is a run setting. Preserve 0 and threshold values such as <20. Preserve Unknown as missing evidence, not a number. Do not invent demand, trend or sales.

## State 4 — Choose observations
Group only within comparable platform, market and metric scope. Determine best observation using the configured date rule in the contract. Never mix newest search volume with an older competition value while presenting them as one coherent snapshot. Keep every source occurrence in provenance. Conflicting equal-priority observations remain review items.

## State 5 — Classify
Use the provided taxonomy, verified product facts and exact keyword meaning. Separate physical and digital formats. Assign primary library, subcategory, confidence and reason; ambiguous items go to review rather than forced fit. Keep taxonomy and any inclusion/exclusion rules in the output. Do not copy a previous project's categories without checking relevance.

## State 6 — Build outputs
Create the requested workbook/library plus audit files using the contract. When output is a workbook, include Keywords, Overview and Source Files, plus unresolved/rejected records as needed. Record each count transition; totals must reconcile. Read back the actual saved files, not only in-memory data.

## State 7 — Quality gate and delivery
Check every input is accounted for; raw values preserved; comparisons use compatible market/period; newest selection has date basis; duplicates and ties are traceable; unknowns aren't zero; classifications have reasons; source filenames resolve; and output can be reopened. Report exact processed/rejected/partial counts and unresolved blockers. Provide the actual deliverables through supported attachments/links. Never equate a path or download toast with delivered files.

Stop as COMPLETE only when all quality gates pass. Otherwise use PARTIAL with precise remaining scope or BLOCKED with next action. Skill completion does not authorize listing writes, paid tool use, publication, deletion, or ongoing monitoring.
