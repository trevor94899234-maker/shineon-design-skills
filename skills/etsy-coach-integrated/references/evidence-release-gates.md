# Evidence-to-listing release gates

Mandatory for keyword decisions, listing text, research corrections and ready/final verdicts. Use with the keyword workflow, seven-layer matrix and council contract. These are local quality controls, not Etsy rules or a guarantee of sales or error-free work.

## 1. Establish the source before the task expands

- Preserve the requested sequence. For the MyGiftStyle full APOD-build trigger, first complete the actual mockup generation/export/inspection gate in [apod-ready-listing-build.md](apod-ready-listing-build.md); the research sequence below starts only after that gate. For a scoped research → listing/title → description → tags → 20 images request, do the decision-relevant research first, carry the same product and intent through every artifact, then make images. A preliminary copy or image brief may remain a draft while its gate is open.
- Inventory **all** available native CSVs, raw visible-UI captures, source tables, source hashes, baseline files and overlays. Read full raw row indexes, headers and relevant rows before relying on a summary. Record file, hash, row/anchor, query, provider, capture/receipt dates separately, market verification, period and measurement definition.
- Before saying “missing” or asking the owner to repeat research, search the raw index for the exact phrase and metric across every relevant source/version. Write what was checked and the actual unresolved field. A short summary omitting competition is not evidence that the original CSV omits it. Recover the existing cell first. Do not claim a scan occurred merely because files exist.
- Keep the original baseline and historical observations immutable. Record its hash; add a dated, versioned overlay with source lineage and a pointer to that baseline. Derive a current view without replacing prior `not_queried`, related-only or null states. Mark superseded conclusions while retaining the old observation. Reconcile conflicting observations by provider/scope/window/capture, not “latest file wins” regardless of meaning.
- Audit current coverage and value qualifiers separately. For example, a corrected 859/859 direct-query ledger can still contain thresholds and Unknowns; it is not 859 numerical demand measurements. Counts in this example are historical, never a required pool size.

## 2. Join exact phrases without manufacturing demand

Create a compact phrase-evidence ledger for **every actual tag** and every title phrase actually researched, compared numerically or claimed as demand-supported. Include raw phrase, field, normalized phrase, direct/related/composed/unresearched status, evidence row IDs, market/window/date, raw metrics and qualifiers, product/intent fit, role in the field and keep/reject/hold/test reason. Join by casefold plus whitespace collapse only; do not silently stem, reorder, translate, synonym-merge or drop words.

- `gift from grandma` does not inherit the metrics of `gift for grandson from grandma`; neither does a shortened or recombined tag. A longer phrase can support related-language reasoning, clearly labeled, but no numerical claim for the shorter phrase.
- Distinguish **exact submitted query** from the provider's measurement matching. An exact query can return near-match aggregated metrics; a table's Match:Exact filter is another scope. Record both, never call exact submission proof of exact-only search volume.
- Preserve numerical display, observed zero, `<20` threshold, `Unknown`, blank/null, not queried, related-only and unavailable as different states. A CSV zero rendered as a UI dash stays an unresolved representation discrepancy unless the provider meaning is established. Keep native raw and UI raw values separately.
- Keep market requested versus independently visible/verified, 12-month average versus named month, period bounds known versus undocumented, capture date versus receipt date, and Etsy versus Google metrics separate. Do not infer a trend from one month, convert average into the latest month, sum overlapping phrase estimates, or turn CTR into conversion rate.
- A truthful composed title is allowed without an exact full-title search-volume result. Label the construction rationale and buyer intent; attach component evidence without transferring or adding their numeric values to the full title. Do not require every possible title n-gram to be queried.
- Unknown or low-volume but relevant language can remain a small, reasoned test or an essential identity term. State the uncertainty and opportunity cost. Do not ban every Unknown tag, set arbitrary volume cutoffs, or turn low competition into a “blue ocean.” No quota of lookups creates sufficient evidence by itself.

## 3. Check whether the market evidence fits this product

Use the seven intent layers: buyer, recipient/role, occasion, product, use case, personalization, buyer language/emotion. Within that matrix explicitly identify payer, sender, recipient/user, actual writer and eventual reader. Keep different roles and occasions separate unless the product and context support combining them.

Inspect decision-relevant **actual competitor listing pages**, not only search volume, search-result snippets, thumbnail impressions or shop totals. Record URLs/IDs, date, actual product/interior, recipient, sender/writer when visible, occasion, personalization, promise and comparable differences. Check at least a plausible competing interpretation/counterexample; select for relevance, not only apparent success. Explain sample and access limitations rather than inventing a fixed competitor quota.

A guided prayer journal, prewritten legacy-letter book, downloadable template, engraved leather item or low-priced generic notebook may not validate a printed, name-only, 200-lined-page leatherette journal. Separate demand for the query family from evidence for this deliverable. Competitor tags do not prove traffic; estimated competitor sales or reviews do not prove this design will sell. If page evidence is unavailable, keep product-market fit provisional and the research gate open; useful drafts may continue within known facts.

Check title, tags, description, category/attributes, offer and images against the same matrix. Read the actual selected category/attribute values before claiming they already cover a tag's meaning. If unverified, mark coverage unknown; do not remove `lined journal` solely because a category might cover it. Prefer complementary intent coverage over cosmetic variants, while retaining truthful product identity.

## 4. Keep quality checks and completion states separate

Track each stage against an artifact version/hash and the checks actually performed:

1. **Draft:** coherent hypothesis; unresolved evidence and product/source facts visible.
2. **Evidence-qualified:** the complete phrase ledger, raw-source reconciliation, meaningful competitor/intent check and uncertainty-aware allocation pass. This may contain justified Unknown-volume tests; it does not mean every term has proven demand.
3. **Text-QA-passed:** active title/description/tags and machine-readable fields agree; counts, lengths, spelling, claims and field allocation pass. Record this subcheck even when the overall artifact must remain a draft for an evidence gap.
4. **Image-QA-passed:** actual exported files pass the requested dimensions, format, product fidelity, text and source/policy checks, for the named slots. Twenty briefs, prompts or rejected previews are not twenty accepted images; keep attempted/rejected/accepted counts distinct.
5. **Owner-approved:** explicit approval for the specific artifact version and intended action. Approval of copy, a method, a sample or one image does not approve all images or publishing.
6. **Applied:** verify the authorized change at its actual destination. Approved or saved locally is not applied to Etsy. Measured results are a later separate observation.

The overall stage cannot skip an unresolved relevant predecessor. Individual subchecks may pass out of order but cannot promote the overall status. For text-only work, image QA is explicitly not applicable; for an image set it remains required. A ready/final label must name its scope (research, text, image production, accepted images, application or applied); readiness for one never implies the next. Keep source-dependent image slots blocked individually rather than blocking all truthful private drafts. State both the authorized next step and any publication-specific gate.

Readable copy, 13 tags within the current character limit and consistent JSON/TXT prove only those checks. They do not validate search demand or commercial positioning. Verify current Etsy guidance: 140 characters is a ceiling, not a fill target; a suggested word count is not a binding ranking rule. Keep a defensible title as a market test, not a proven winner. Do not declare a title superior without appropriate first-party comparative evidence.

## 5. Independent adversarial outcome review

Before describing a researched listing/package as **ready**, **final**, research-complete or ready for the next production stage, use a fresh independent reviewer where tools, authorization and cost allow. The reviewer must not be the author or a renamed Coach perspective. Give the task, source artifacts, product/owner constraints and exact candidate version; do not preload the desired verdict, earlier consensus or an answer key. Nine framework lenses are not nine independent judges, and even independent judges are not market proof.

Require the reviewer to inspect the earliest unsupported link and look for counterexamples, missing source joins, summary-only false gaps, overwritten baselines, wrong time/market scopes, product/role mismatches and semantic claims hidden behind format QA. Return:

- scope and version reviewed, raw sources actually opened and limits;
- decision-critical assertions with support, counterevidence or missing evidence;
- stage-specific PASS / REVISE / BLOCKED, including which private draft work may continue;
- concrete corrections, smallest remaining evidence request and what would change the decision.

A limited correction recheck cannot certify the full research strategy. Log scope explicitly, preserve old findings, and reopen affected checks when evidence or copy changes. If independent review is unavailable, disclose that gate and deliver a draft; do not simulate a pass. The author reconciles findings against sources rather than blindly accepting a reviewer. Record an unresolved evidence conflict honestly. No reviewer, council or script warrants a zero-failure promise.

## 6. Mechanical sidecar validation

For a release packet, build a sidecar matching `assets/evidence-gate-fixture.json` and run `python3 scripts/validate_evidence_gates.py packet.json --baseline-sha256 ORIGINAL_BASELINE_SHA256`, taking the lock from the preserved original record rather than recomputing it after an edit. For the synthetic fixture only, omit the hash argument. Run `python3 scripts/test_evidence_gates.py` after changing the validator. Resolve sidecar file paths relative to its directory. Preserve the existing Dashboard schema; this sidecar is an audit contract, not a replacement or import instruction.

The validator checks phrase identity, evidence/value joins, coverage of actual tags/title queries, raw-index coverage before new research, hash-locked baselines, overlay pointers and stage prerequisites. Numeric claims must copy a qualified raw metric from the same exact query and name its actual measurement mode. Related/composed language can be retained without quantitative claims. For a real release provide file paths and hashes; the bundled synthetic fixture tests structure only.

Mechanical checks cannot determine whether a screenshot was read accurately, a competitor is truly comparable, an explanation is honest or a title will sell. Human/independent semantic review must supply those judgments with source anchors. A script's exit 0 is not a research, image or commercial-success certificate.

## 7. Diverse semantic assurance supplement (2026-10-09)

For a full keyword/listing research release, also apply [panel-assurance-2026-10-09.md](panel-assurance-2026-10-09.md). The companion structural check records distinct decision specialties, actual independence claims, product/intent/evidence judgments and weak-signal dispositions. It does not replace this gate or authenticate review execution. Both checks may pass while market outcomes remain unmeasured. A source-based AI perspective is not an actual human coach consultation.
