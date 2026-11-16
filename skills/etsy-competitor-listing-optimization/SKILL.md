---
name: etsy-competitor-listing-optimization
description: Research and qualify Etsy competitors, reconcile live shop inventory, audit recipient/material/metric claims, and draft product-accurate listing improvements. Use for repeatable cloud or authorized local competitor research, source-backed success comparisons, research corrections, keyword evidence, and controlled listing optimization.
---

# Etsy Competitor Listing Optimization

Move through one state at a time. Read [references/computer-use.md](references/computer-use.md) before UI work and [references/evidence-and-output.md](references/evidence-and-output.md) before collecting facts. For continuation work, read [references/continuation-and-case.md](references/continuation-and-case.md) to reconstruct the full query ledger, fill gaps only, and choose a bounded stop condition. Default to a reviewable local draft unless the current user request explicitly authorizes a specific shop edit.

## Research module and tool routing
For multi-shop research, inventory reconciliation, competitor qualification, or correcting existing research, execute [the research runbook](references/research-runbook.md). Read [semantic evidence rules](references/semantic-evidence-rules.md) before labeling roles, material, process, age or success. Use [the data contract and checks](references/research-data-contract.md) to preserve raw sources, canonical IDs and reusable exports. Start from [the empty bundle template](assets/research_bundle.template.json); do not silently change an existing packet schema.

Use [Coach integration](references/coach-integration.md) before queries, during corrections/qualification, and when allocating keywords. The Integrated Coach remains the recommendation entrypoint when available; this skill supplies research evidence and execution. Use [case regressions](references/case-regressions.md) only as historical examples, never as current inventory or universal targets.

Keep the existing 0–8 lifecycle below. The research module deepens states 1–4 and 6; it does not require full listing copy or authorize shop edits. Run scripts/research_checks.py and tests/test_research_checks.py for deterministic checks; require a separate independent source-based semantic audit.

## State 0 — Lock product and scope
Identify exact own listing/product, shop, market, language, physical/digital format, research question and output. Read the current product reference and user/supplier facts. Record deliverable mode: research-only, listing draft, or explicitly authorized application. A research-only request does not require full title/tags/description; a new product may have no existing listing. Build confirmed/unknown fact lists. Never borrow competitor dimensions, material, page count, manufacturing process or shipping promise. Missing facts stay unknown; ask if they prevent accurate drafting.

Separate buyer, recipient, sender and occasion/use. Separate buyer-market country from seller location. Treat material as a secondary comparison unless the user specifies a hard requirement; never infer a competitor supplier from appearance.

Record authorized sources and any research limits. Historical examples such as focused SERP research or at most five new keywords are settings for that run, not universal limits. If no limit is supplied, propose a small relevant sample and state coverage; do not imply market completeness.

## State 1 — Establish baseline
For an existing listing, read current title, description, visible attributes and available tags from the actual own listing or authorized export. For a new product, mark baseline not yet created; use the authoritative product facts and do not invent a listing URL or force shop access. Log URL/ID/date. Hidden tags remain unavailable unless a reliable authorized source exposes them. Save a baseline copy before any authorized edits. Record what the user wants improved and what must remain unchanged.

When inventory completeness matters, paginate the live source, deduplicate actual item cards by canonical listing ID and reconcile fresh displayed counts with unique IDs and detail-response counts. Cached counts, first-page cards and batches silently capped by a tool are not complete inventory. Preserve discrepancies and timestamps; do not invent a reason for changes.

## State 2 — Gather comparable competitors
Search actual relevant queries in the selected market. Verify query/filter state after each action. Record result position as observed, sponsored status if visible, and collection date. Distinguish connector-returned order from observed UI position; neither alone proves organic ranking, sales or US demand. Open each chosen listing and verify identity. Separate direct competitors (same product/format/purchase intent) from adjacent ideas. Exclude digital downloads from direct comparison with physical journals. Record exclusions and reasons.

Qualify shop comparators with relevant product/buyer-mission fit plus scoped trading evidence and relevant linked reviews/catalog corroboration. Separate candidate count from well-supported count; use the user’s minimum and an explicit evidence threshold without padding. Shop lifetime sales are not proof that the selected listing sells or is profitable.

## State 3 — Capture evidence
Fill the competitor schema from the source. Capture price/currency/variant, shipping destination and any observed fee separately. If a research tool supplies sales/revenue/search volume, label it an estimate, preserve period and tool name, and do not present it as Etsy-verified. Read exact metric definitions if they determine ranking. Unknown is not zero. Do not infer tags from title words or bestseller status from ordering.

## State 4 — Evaluate keywords
Use supplied clean keyword pool first. Build a complete deduplication ledger from all briefs, raw batches and audit candidates; a selected copy-ready shortlist is not the full query history. Join by normalized exact query and compatible market/platform/period; inspect raw source on conflicts. Add only the permitted number of new researched queries. Each proposed query needs product relevance, buyer intent, exact data/source and uncertainty. Classify EACH proposed tag/phrase separately as measured exact query, existing own-listing term (unmeasured unless separately researched), observed actual competitor tag (unmeasured demand unless separately matched to exact-query evidence), observed non-tag competitor wording, or new copywriting hypothesis. Never say “all other terms are measured” without an exact per-phrase ledger match. A high-volume irrelevant term cannot override product truth. Separate measured evidence from copywriting hypotheses.

## State 5 — Draft changes
For research-only mode, provide findings and requested title architecture/candidates only, then skip full copy drafting unless asked. Respect any title limit (the historical case requested at most two). Listing-ready tags are produced only when requested.

Write original copy supported by confirmed own-product facts. Use natural language and relevant phrases rather than competitor copying or keyword stuffing. Verify current Etsy field constraints with official guidance or the current editor; do not rely on an old count limit stored in memory. Include before/after, rationale and evidence links for each field. Do not insert unknown material/specifications, unsupported superlatives, fabricated testimonials or promises.

For requested image prompt work, use available etsy-pod-image-prompts and the authoritative image. If absent, retain product accuracy and exact text as constraints; don't invent access to it. Drafting text overlays is not generating or delivering image files.

Before selection, retain accept/reject/hold, reason, evidence IDs, intended field and only relevant grounded Coach source IDs. Product-truth conflicts stop affected claims before keyword optimization.

## State 6 — Quality gate
Run the checklist in the output contract. Structural pass does not establish semantic truth: an independent reviewer must inspect a risk-stratified raw-source sample. Any error opens a full affected-category audit, correction log and recheck of dependent qualification and every delivered view. Mark each pass/fail/blocked with evidence. Reconcile competitor counts and keyword budget. Verify saved artifact opens and includes full copy, not just summaries. Distinguish proposed changes, authorized applied changes and unverified changes.

## State 7 — Optional authorized application
Only enter this state when the current request authorizes the exact listing and fields. Re-open correct shop/listing and compare current values to baseline; stop if changed unexpectedly. Enter only approved values one field at a time; verify each. Before any save/publish control read its consequence and follow applicable confirmation requirements. Do not alter price, inventory, shipping, ads or permissions as a side effect. After authorized save, reopen and read back exact values; if uncertain inspect first rather than duplicate the write. Retain before/after evidence.

## State 8 — Deliver and stop
Deliver the requested competitor/keyword evidence and, only when requested, the copy-ready listing packet with actual accessible file/link. Preserve all raw sources and stable entity/source IDs for later CSV joins; keep private capture metadata out of user-facing exports. Replace existing Library artifacts with the same identity and current version guard, verifying each result. State scope, significant uncertainties, and whether anything was applied. Stop when the requested packet or authorized edit is verified, or return BLOCKED/PARTIAL with exact next action. This skill does not authorize recurring monitoring, purchases, external outreach or unrelated shop changes.
