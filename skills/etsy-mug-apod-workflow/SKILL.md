---
name: etsy-mug-apod-workflow
description: Complete or resume a physical mug product's private Anywhere POD listing, from source and keyword research through thumbnails, listing fields and saved-state verification. Use for personalized ceramic mug workflows that need variant/handle/print fidelity, fewer repeated owner questions, or local-to-agent handoff. Adapts the existing APOD coordinator; not a publishing or standalone image-generation tool.
---

# Mug to private APOD

Release: 1.0.0 · 2026-10-28.

Use one task record and one artifact owner to finish the user's authorized endpoint. Reply to the owner in Traditional Chinese/Cantonese; buyer copy defaults to natural American English. Do not infer a new goal, 20 images, a video, paid services or Etsy publication merely from loading this Skill.

## Enter once, then resume

1. Recover the latest user scope, applicable rules, current product record, source identities, previous answers, accepted files and actual APOD receipts before asking anything. Read the current completion record before old checkpoints. Historical pending states do not invalidate later verified receipts.
2. Select this Skill's mug profile, then load **`etsy-apod-product-workflow` by name** as the single end-to-end coordinator. If it is already active, attach the profile to that same record; do not start another plan or call this entry recursively. See [integration.md](references/integration.md).
3. Keep Growth for positioning, Integrated Coach for research/listing evidence, Image Studio for image production. Loading another Skill is not permission to spawn agents or operate another user's chat. Use existing task-specific evaluator/model instructions; otherwise choose QA proportional to risk.
4. For a full run read [runbook.md](references/runbook.md), [decisions.md](references/decisions.md) and [mug-profile.md](references/mug-profile.md). For a resumed phase read only its relevant section and the current record. Read [runtime.md](references/runtime.md) when changing machine/agent or recovering an uncertain action, and [completion.md](references/completion.md) before claiming completion.

## Keep work moving without inventing authority

- Retrieve answers from current human decisions, SKU records, Keyword Vault and matching official supplier sources. Routine wording, layout, filenames, QA and already-authorized saves are agent decisions. Do not ask the owner to browse for publicly accessible facts the agent can obtain.
- Use one decision queue with stable issue IDs. An unanswered item blocks only its dependent operation. Continue independent source work, copy, eligible image roles and receipts. Consolidate actual unresolved owner decisions into one clear packet where practical; do not repeatedly present the same question after a turn, agent or runtime change.
- Exact-file acceptance stays exact-file. A **current, explicit, bounded owner batch policy** may authorize later files within named roles and disclosed defect categories, after per-file QA and exact-hash binding. This is not individual human viewing or technical PASS. “Continue”, silence, a generation grant or one accepted pilot does not create that policy. New wrong wording, wrong variant/quantity, unsupported claims or other material unapproved defects hold the affected file. Details and eligibility record: [decisions.md](references/decisions.md).
- Persistent redraw still stops the failing method unless the owner explicitly authorizes the bounded continuation or another method. No hidden retries, no automatic composite fallback, no silent new spend. Approved initial drafts are not automatic approval of every result.
- Preserve hard gates for identity, safety, new commercial choices, sensitive access and explicitly required human acceptance. Reuse existing scope-valid authorization rather than asking for it again. Do not manufacture “owner approval” to meet a question-count target.

## Mug invariants

Bind **each capacity to its own source/artwork/variant branch**. A larger 11 oz picture is not proof of a 15 oz product. Preserve cup and handle proportions, rim, base contact, light/reflection, exact print/name and original brand source. Inspect transparent artwork against a contrasting QA background before declaring text missing.

One mug, a choice of sizes, and two views of one mug are different offers. Verify offer quantity and both-side mapping. Supplier production/transit estimates do not establish the shop's shipping policy, buyer fee or guaranteed arrival. UI character limits do not establish print-safe name fit. See the profile for evidence requirements and a configurable 20-role example.

Use the user's required generation route. Under the existing owner setup this is **ChatGPT web Create image**, whole-image generation; verify the actual UI and record backend model/version as TBC when not exposed. Do not substitute an API or local compositing because the user calls it “image2.5”. Follow current Image Studio native-format and acceptance rules; record requested, minimum and decoded actual size separately.

## Output and completion

Keep one [current record](assets/current-record.md), a [role ledger](assets/roles.csv), [field matrix](assets/fields.csv) and [decision queue](assets/decisions.csv), or equivalent existing records—do not create duplicates just to match templates. Store exact source/native hashes, technical QA, scope-valid use authority and actual saved-state evidence separately.

Completion means the **authorized endpoint**: distinct required native images, eligible use, actual APOD selection/order/primary/save/reopen verification, all applicable field dispositions, and required video only when in scope. Re-read text and protected fields after the last media save. An uploaded library file is not necessarily selected or saved. Private-draft completion does not remove warnings or certify publication readiness.

The 627726 [case study](references/case-627726.md) explains the workflow's evidence and failure lessons. Its counts, prices, supplier estimates, model costs and appearance exceptions are not defaults or permissions for another product.
