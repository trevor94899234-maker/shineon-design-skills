# Dashboard research loop

This is the local MyGiftStyle execution layer. It is a workflow contract, not an Etsy requirement or a claim about Etsy's ranking algorithm.

## Purpose

Turn evidence-backed research into a controlled sequence:

`product context -> intent anchors -> bulk screen -> selected individual CSVs -> merge/deduplicate -> gap analysis -> candidate proposal -> owner approval -> research tasks -> listing brief -> first-party learning`

## Source reconciliation before decisions

Apply [evidence-release-gates.md](evidence-release-gates.md). Keep the original baseline bytes/hash and historical states immutable; derive the current view from explicitly versioned overlays joined by exact phrase, scope, period and provider. A current `direct` state describes query coverage, not numeric demand or product fit. Reconcile all available raw files and full row indexes before marking evidence missing or creating replacement research tasks. Summaries and old queue counts are insufficient. Keep this audit as a sidecar if the existing packet schema has no compatible fields; do not overwrite the baseline or silently redesign the Dashboard.

## Evidence packet rules

Every imported file should retain:

- product and listing context;
- research round and query;
- source tool and export date;
- raw rows and a normalized phrase;
- value status such as confirmed, estimated, missing, invalid, or confirmed-zero;
- lineage to the candidate or decision that used it.

Separate acquisition completion from decision sufficiency. An exact query whose actual UI/export explicitly returns Unknown or no data can be a completed check while numeric demand or monthly-series evidence remains unavailable. Record the observed source and scope; do not automatically requeue it as unqueried or repeat the same query without a reason. A partial/unread export is not complete acquisition, and a file containing mostly Unknown values is not numeric demand evidence. Never infer zero from a blank or Unknown cell.

## Round pattern

1. Begin with a small set of intent anchors. The current local default is five anchors when the product context is clear.
2. Use eRank bulk research for quick breadth and comparison.
3. Select only the strongest or most informative anchors for individual research and export their complete CSVs.
4. Merge and de-duplicate phrases while preserving source lineage.
5. Mark which required intent dimensions are covered and which remain open.
6. For an open dimension, the assistant may propose a candidate set. Candidate phrases are hypotheses until the owner chooses them and the selected phrases receive research evidence.
7. After approval, create only the needed research tasks. Do not create a new round, alter the Listing Brief, publish, or edit Etsy automatically.
8. After an owner-approved listing test, use Etsy Stats and search terms to learn what actually brought traffic and conversions.

The older archive mentions 30–50 phrases and a three-round structure. The current adaptive Dashboard may use a different count. Never treat either number as an Etsy rule; use the active packet and current Dashboard contract.

## Current gap-candidate contract

When the current `product-research-analysis` packet asks for a gap proposal:

- target only a required dimension that is not already covered;
- use only support rows from the current packet and product/round context;
- produce exactly 25 raw drafts for the local validator;
- each draft has `query`, `targetDimension`, `extensionLogic`, and `supportingRowIds`;
- queries should be clean, natural, independently researchable phrases, normally two to four words;
- before ranking or owner selection, classify each valid draft with the relevant layers from [keyword-combination-matrix.md](keyword-combination-matrix.md): buyer, recipient/role, occasion, product, use case, personalization, and buyer language/emotion;
- distinguish buyer from recipient, and prefer a shortlist that covers complementary intent combinations rather than five to eight near-synonyms;
- do not force all seven layers into one query or invent an occasion, use case, personalization option, or emotional promise that the product evidence does not support;
- do not duplicate completed queries, invent evidence, or use OCR-only or stale rows as confirmed support;
- the validator must find at least 15 valid drafts before the proposal is ready;
- the owner can edit, reject, or select the proposed phrases; the local Dashboard typically requires 5–8 approved candidates to create the next research tasks;
- if the packet lacks the exact gap dimension or eligible support rows, report the missing evidence instead of fabricating 25 candidates.

The number 25 is a local candidate-generation requirement for this Dashboard handoff, not a claim that Etsy recommends 25 keywords.

## Candidate ranking lens

Rank only after validity checks. Use, in order:

1. relevance to the uncovered buyer or intent dimension;
2. support from current evidence rows and a clear extension explanation;
3. honest product and personalization fit;
4. useful coverage across the keyword-combination matrix without duplicating another candidate's primary intent;
5. researchability and clean phrasing;
6. likely differentiation from existing listings;
7. demand and competition signals when actually confirmed by a current source.

Do not let a high estimated search volume override an invalid product fit, a missing support row, a duplicate intent, or a high cannibalization risk.

## Owner gates and states

Keep these states separate:

`draft suggestion -> validated proposal -> owner-approved candidates -> research task -> evidence received -> listing brief -> owner-approved listing draft -> published test -> measured result`

The assistant can explain, generate, validate, and prepare packets. The owner decides whether to accept candidates, change listing content, publish, advertise, or declare the experiment successful.
