# Evidence and output contract

## Authority order
Own product identity: user's explicit current facts and authoritative supplied product/supplier reference; verified own listing as baseline; then unknown. Competitor information never establishes own-product construction. Conflicting own sources require clarification before a factual claim.
Competitor observation: actual listing page for visible facts; tool export for clearly labelled tool-specific estimates; screenshots/transcripts with date and scope; unsupported inference last and labelled hypothesis.
Keyword evidence: exact source metric with tool/platform/market/period/date; qualitative SERP observations separately. Search result count, search volume and sales are different metrics.

## Required records
Product fact sheet: product_id, own_listing_url, fact, value, status confirmed/unknown/conflict, source, observed_at, immutable constraints.
Competitor row: listing_url/id, shop, observed_at, query, market, result_position, sponsored_status, comparator_class direct/adjacent/excluded, reason, title, format, visible price, currency, selected variant, shipping scope, visible attributes, tags_source_or_unavailable, metrics_with_period_and_estimated_flag, evidence_reference.
Keyword row: query, normalized_query, existing_or_new, phrase_provenance (measured exact query / current own-listing term / observed actual competitor tag (unmeasured demand) / observed non-tag competitor wording / copywriting hypothesis), source, market/platform/period, raw metrics, observed_at, relevance_reason, intent, recommendation, confidence, unknowns. Count new researched queries once, even when repeated across pages.
Change row: field, before, proposed, product_facts_used, keywords_used, rationale, source references, validated_field_constraint, status draft/approved/applied/verified/blocked.
For multi-shop research, supplement these records with the research-data-contract sidecar rather than replacing existing IDs or schemas.

Run log: state, timestamp, observed UI identity, action, verification, evidence pointer, next state.

## Packet
Match current requested scope: research-only includes findings, evidence and next action; listing-draft adds the requested copy fields; authorized application adds verification receipt. Do not force full copy into a research-only deliverable.
1. Product facts and unresolved details.
2. Competitor comparison with exclusions and scope.
3. Keyword shortlist with measured versus inferred evidence.
4. Full proposed title, each tag separately, complete description and optional requested image brief.
5. Before/after change table, quality gate, unresolved questions and next action.
6. Application receipt only if actually authorized and verified.

## Quality gate
- Required packet sections are limited to requested deliverable mode; a new product baseline may legitimately be absent.
- Conflicting source estimates retain tool, scope, date and definitions separately; never average incompatible numbers. Item reviews/ratings/sales stay separate from store-level figures.
- All own-product factual claims trace to authoritative own-product sources.
- Every competitor URL resolves to the collected item; no fabricated source links.
- Direct competitors share relevant format and buyer intent; excluded/adjacent items labelled.
- Estimates, qualifiers, period, currency and market preserved.
- Tags distinguished from title words; unavailable tags not invented.
- Keyword research stays within any stated budget; missing metrics not converted to zero. Each tag and claimed keyword has an exact per-phrase provenance row; an attribute-derived phrase is a hypothesis even when the attribute itself is confirmed. Existing tags do not imply measured demand. Preserve no-analytics warnings alongside displayed zeros.
- Proposed fields obey current verified platform limits and avoid prohibited/misleading claims.
- Exact personalization, spelling, translation and artwork constraints preserved.
- No competitor copy or unsupported material, page count, shipping or sales claims.
- Files reopen; full draft present; delivery mechanism supported.
- External mutations are absent unless specifically authorized and read back.
