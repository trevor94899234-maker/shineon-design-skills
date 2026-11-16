---
name: etsy-apod-product-workflow
description: Coordinate a selected physical POD product from buyer positioning and actual product mockup through evidence-based listing text, approved thumbnails, and saved/reopened private Anywhere POD fields and gallery. Use for end-to-end APOD preparation, 20-thumbnail plus listing requests, or resuming that workflow across local or remote agents. Preserve narrower image-only requests and owner exclusions; never infer Etsy publication or paid-service authority.
---

# Product → thumbnails → private APOD

Release: 1.1.1 · 2026-10-28.

Use one current task record to carry the identified product to the requested, verifiable endpoint. This Skill coordinates existing specialists; it does not replace their production methods or create additional agents. Answer the user's outcome request without making them choose Skills or technical routing.

## Start or resume

1. Read applicable environment/project rules, the latest owner request and the current task record. Recover exact prior decisions and receipts before asking anything. Read history only to resolve a current gap or conflict.
2. Bind the destination product, variants, artwork revision, immutable source files and current private state. Never bind by product title alone. Reuse a valid same-version actual mockup; do not re-render just to restart this workflow.
3. Recover the execution charter: `FULL_PRIVATE_BUILD`, `SCOPED_PRIVATE_UPDATE`, `IMAGES_ONLY`, `FILES_ONLY`, or `AUDIT`; requested count/active rows, fields, video, exclusions, exact route, method exceptions, cumulative attempts/budget, acceptance gates and private-write authority. Fill it from existing decisions, not a mandatory owner questionnaire. Follow the latest explicit narrower instruction.
4. Check actual runtime capabilities using [runtime and recovery](references/runtime-and-recovery.md). A Windows path in a handoff is not cloud-readable source evidence. A tool description is not a successful connection.
5. Use [decision and question rules](references/autonomy.md) before asking. Target zero routine questions; use at most one consolidated necessary intake bundle when possible. Reuse confirmed direction, pilot, source order and delegated judgment. A real unresolved human gate can require a bounded later question; it blocks only dependent steps. Do not add a fresh intake, plan or finish approval to every invocation.

Create a tracked goal only if the user explicitly requests one. A request that merely mentions an earlier goal is not a new goal instruction. Keep an existing goal aligned with the owner's current scope.

## One owner per phase

| Phase | Production Skill | Return to this coordinator |
|---|---|---|
| Buyer, gift occasion, positioning | `brand-marketing-growth` | One supported direction, locked claims and buyer questions |
| Product evidence, research, listing copy | `etsy-coach-integrated` | Source-linked field packet, exact copy, limits and unresolved claims |
| Thumbnail plan execution and visual QA | `etsy-listing-image-studio` | Actual native files, hashes, per-file QA, attempts and exact exceptions |
| Private APOD application and delivery | This Skill | Saved/reopened field and asset reconciliation, completion receipt |

Resolve these Skills by frontmatter name from the current environment, then read only the phase's required references. Relative sibling links in the portable package are conveniences, not proof a Skill is installed. When called by a specialist, resume the existing record; when calling a specialist, pass `phase_only` and return here. Never bounce back to another entrypoint or create a second plan. Merely referencing a Skill does not invoke another model or grant delegation permission.

For ornaments, retain `etsy-ornament-apod-workflow` and Studio's ornament profile. For mats/floor products, use Studio's [mat and floor-plane profile](../etsy-listing-image-studio/references/mat-floor-plane-profile.md); do not force book-cover camera geometry onto the floor. For personalized home-blessing wall art, use the adaptable [home-blessing profile](references/home-blessing-profile.md). Profiles transfer methods, never another SKU's facts or approvals.

For mugs, resolve `etsy-mug-apod-workflow` by name and load its `references/mug-profile.md` plus `references/decisions.md` when relevant. Attach its capacity/handle/print evidence and decision rules to this same record; do not re-enter its coordinator entry or restart intake. If unavailable, retain ordinary generic operation within available evidence and identify the missing specialized profile; do not invent mug facts. The adapter's direct entry also returns to this coordinator once.

## Ordered execution

Read [workflow and field coverage](references/workflow.md) before a new end-to-end build; resume at the first unmet dependency.

1. Recover scope, authority, sources, current fields/media and backup.
2. Bind the actual same-product exported APOD mockup and inspect the real file. For a full build, this precedes substantive keyword selection, listing copy and thumbnails. A narrowly authorized fidelity pilot follows Studio's minimum brief instead.
3. Reuse the current research round's source order and saved exact evidence; close only decision-changing authorized gaps.
4. Prepare truthful title, full description, tags, personalization and [complete field coverage](references/listing-field-matrix.md). When price/offer analysis is in scope, use [fees and offer calculations](references/fees-and-offer.md); never call product-cost subtraction net profit.
5. Plan distinct roles, confirm only an unconfirmed material direction, inspect one pilot, then produce all remaining authorized roles within the approved attempt/budget limits. Inspect every final file.
6. Apply authorized text; save and reopen. Upload accepted files, select/order them, save and reopen. Use [APOD operations](references/apod-operations.md).
7. Produce and verify video only where required by the active scope, using [native APOD video](references/native-video.md). A MyGiftStyle full build retains the Coach's current video contract; a specifically scoped thumbnails/text update does not silently expand to video.
8. Re-read the whole affected record after the last save, reconcile files/roles/fields, and deliver usable artifacts and exact remaining exclusions.

## Authority and questions

The user asking for actual private APOD preparation authorizes the identified private fields/media actions within that request. Do not repeatedly ask to upload each already-eligible file or save each already-authorized field. Copy/layout choices within the locked brief are routine production decisions; material product/offer changes are not.

This invocation never grants publication, Etsy sync/push, sending messages, purchases, ads, new subscriptions, account changes, credential handling, destructive cleanup or changes to unrelated products. Preserve current price/shipping unless the user authorized the specific change. A user exclusion such as “skip shipping, I will handle it” removes that action from this task; it does not verify shipping or authorize a guess.

Visual QA and owner acceptance are separate. Record each human gate as `NOT_REQUIRED` with basis, `REQUIRED_PENDING`, `SATISFIED` or `INVALIDATED`. Technical PASS proceeds within authority when no human gate applies; do not request per-file/per-field approval. Failed fidelity needs bounded correction or applicable explicit owner exception authority: exact-file acceptance, or an expressly delegated bounded batch policy followed by per-file QA and hash binding as defined in [autonomy.md](references/autonomy.md). No policy is inferred from “continue” or one pilot. Queue unresolved method, budget and fidelity decisions, finish independent eligible rows, then present one concrete batch of previews/hashes and incremental costs. Preserve the failed findings and requested count.

Preserve the existing owner requirement to ask source order once for a genuinely new research round without an answer. Merge this with other necessary intake decisions. Never ask again for the same round. No new universal Vault-first rule is introduced here.

## Resume and delivery artifacts

Use an equivalent existing ledger rather than rewriting a completed task into this template. For new work, copy [the task record](assets/task-record.md) and [field coverage table](assets/field-packet.csv) into the authorized task directory. Keep one current-state document; append-only events are history, not competing current summaries.

Before claiming completion, follow [completion and audit](references/completion.md). The optional portable `scripts/audit_delivery.py` checks record consistency, local/remote hashes, selected order and required field readback. It never performs uploads or certifies visual quality, permissions, live persistence, print readiness or publication readiness. Read its contract before using it; do not synthesize missing receipts to make it pass.

Final response distinguishes:

- What was actually saved/uploaded/selected/reopened at the named APOD product.
- Native delivered count, primary/order and the strength of identity proof.
- Exact owner exceptions, skipped work and remaining Etsy/production gaps.
- Local deliverable links or accessible remote artifacts; local paths alone are not a remote handoff.

Use Cantonese/Traditional Chinese for the owner and natural American English for US buyer copy unless the task specifies otherwise. Do not repeat the whole execution log.

For provenance or a similar mat/video failure only, read the dated [completed 627772 case](references/case-627772.md). It separates the final accepted endpoint from superseded pending checkpoints. Do not preload all references, reopen completed case work or promise flawless operation across services.
