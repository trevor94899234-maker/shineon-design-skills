# Decisions without repeated interruptions

The target is **zero unnecessary questions**, not zero human decisions. Resolve facts from evidence, make ordinary implementation choices, and obtain human decisions only where authority or material preferences are actually missing. Do not imitate the owner's consent or answer a pending human approval yourself.

## Recover before asking

Search narrowly in this order: current user messages and exact decisions → current task record and latest completion/application receipts → linked source/offer/brand records → Keyword Vault or the previously selected research order → variant-matched official supplier material. The order of authority is not an instruction to ignore a current owner-specified source order. Distinguish human-provided, verified, inference and TBC. Record the source and date; don't repeatedly retrieve the same unchanged material.

Before sending a question, check: Is the answer already present? Is it a factual lookup I can perform? Can I make this reversible choice within the request? Does anything actually depend on it now? Has this same decision already been asked? Is its authority invalidated by a specific change? If no current dependency remains, keep a note rather than a blocking question.

| Situation | Agent action | Ask only when |
|---|---|---|
| Exact APOD URL/ID already supplied | Recover and verify product/variants | Multiple plausible products remain or IDs conflict |
| Quantity or sizes already SKU-confirmed by owner | Reuse with provenance | Source conflicts affect truth or a new offer is being proposed |
| Missing material/care/capacity/source photo | Search the matching official product/media portal; inspect actual assets | Unresolved fact is essential to the requested role and cannot be omitted safely |
| Keyword Vault order already chosen for this round | Reuse it and existing usable evidence | Genuinely new unanswered source-order decision required by the applicable research workflow |
| Copy phrasing, tag selection, layout, filenames, role ordering | Decide from evidence and approved brief | New claim, changed commercial promise or an explicit human copy gate applies |
| Exact four text groups already approved/applied | Compare current readback; save only missing/drifted authorized values when safe | Intended content or protected fields materially change, or concurrent drift is unexplained |
| Upload/save/reopen explicitly in the product request | Execute on eligible artifacts; don't ask per click/file | New product, scope, permission or material exception is needed |
| Optional unknown detail | Omit unsupported claim or label internal TBC; complete independent work | Omission changes a required role/count or an essential buyer fact |
| Owner-excluded price/shipping/video/Etsy Push | Record excluded scope and continue | Owner later changes that scope; don't repeatedly reopen it |
| Existing normal logged-in browser session | Use documented authorized controls | Login, OTP, CAPTCHA, new sensitive access or a tool safety stop requires human action |
| Timeout after a mutation | Inspect same job/product and recover existing result first | Outcome cannot be determined without a new decision; don't duplicate automatically |
| New price, policy, supplier, spend/service or publication | Prepare a concrete diff/cost/impact for approval | No scope-valid explicit authorization already exists |

## A question queue, not a conversation loop

Maintain stable IDs such as `offer.quantity`, `p18.delivery-source`, `method.fidelity`, `apply.variant-conflict`. Each item records the dependency, source search, proposed safe default if any, status, owner question/reply and what would invalidate it. Suggested statuses: `RESOLVED_EVIDENCE`, `DECIDED_AGENT`, `RESOLVED_OWNER`, `PENDING_OWNER`, `BLOCKED_EXTERNAL`, `SUPERSEDED`.

Decision identity is product + affected revision + issue + action, not the current turn number. A handoff does not reset it. Change only affected decisions when facts/bytes/scope change. Keep the prior answer in history and state why it no longer applies. An authority for one SKU does not authorize another.

Bundle mutually independent necessary questions into one concise packet with a recommendation, exact reviewable artifacts/diff, consequences and scope. Complete the work needed to make approval concrete first. Do not ask “shall I continue?” after every stage. While a required answer is pending, list and execute independent eligible work; do not send duplicate requests, treat elapsed time as consent or mark the whole task complete. If all useful work is exhausted, give one truthful blocked handoff; follow the goal tool's actual status rules when a tracked goal exists. Do not create a reminder/automation on your own.

## Four distinct authorization paths for images

1. **Ordinary eligible output:** all required technical checks pass and the user's request authorizes the use. Advance automatically unless an explicit human final-image gate applies. A routine QA PASS is not owner publication permission.
2. **Exact-file exception:** owner accepted identified bytes after disclosed defects. Bind SHA-256, product/design/brief, permitted use and exact reply. Reuse that acceptance for those bytes; new failing bytes need a new eligible path. Do not require the same approval again merely to upload the already-authorized file.
3. **Explicit scoped batch policy:** the owner expressly permits named remaining rows/results to be used after QA within identified defect categories. Record the direct reply plus its question/context, role IDs or bounded count, SKU/revisions, method, attempts, defect categories and exclusions. A brief “all approved” is sufficient only if that context makes its referent and permitted later-file scope unambiguous; otherwise ask once for the unresolved boundary while working independently. The policy is not evidence the human viewed future files.
4. **No eligible path:** hold the dependent file. Disclosure alone, “continue”, silence, an approved prompt, initial-generation permission, one accepted pilot or an agent's preference cannot create an exception.

For path 3, produce one per-file binding **after** inspecting the actual returned file:

```text
Role / exact file / SHA / product + design + brief revisions
Technical verdict and each actual defect (unchanged)
Required reviewer/judge receipts and actual role/model/config, if required
Owner policy ID and exact human evidence
Which allowed category covers each defect; no new material defect: yes/no + reason
Method/attempt/native-size/count limits met: yes/no + evidence
Use eligibility: ELIGIBLE_UNDER_SCOPED_POLICY or HOLD
Human individually viewed this exact file: true/false/unknown (never inferred)
Permitted destination/use; publication status kept separate
```

The owner must explicitly delegate the category judgment; merely approving a contact sheet of existing hashes covers that set only. Grouped exact-file review and a forward batch policy are different. Do not grant batch exceptions by default on future mug tasks. Honor a stricter per-file human gate unless the current owner explicitly revises it.

Known cosmetic redraw/spacing differences can be covered only within that actual policy. Wrong product/capacity, missing/changed buyer wording, false offer quantity, unsupported material/care/shipping claim, a new logo/identity issue outside the policy, native-size failure outside its limits or a new costly/workflow action is not automatically covered. Revisions that improve one defect can introduce another: re-inspect all relevant checks, not only the repaired area.

Technical `REVISE`/`HOLD` remains visible even if use is authorized. Do not call it PASS, original-pixel fidelity, physical measurement, a new design master or production-ready. A draft authorization does not allow known false claims. Retain necessary draft warning/disclosures. Bind authority separately for copy changes and images.

## Recovery cost and stop control

Initial-plus-two corrections is a ceiling from the Image Studio workflow, not free additional spending or permission to ignore repeated systematic distortion. Track total attempts and pending jobs across runtimes. Stop the failing approach early, diagnose against original sources and propose one bounded remedy if necessary. Source transport repair before any Send is not another generation; resending after uncertain completion may be.

If the owner authorizes one test, execute one. If the owner authorizes remaining initial drafts despite disclosed redraw, use only that scope; don't silently turn it into repeated correction cycles or final-file acceptance. Ask only for a genuinely new method, cost, material defect or expired scope. Repeated known cosmetic findings under a valid batch policy do not justify 20 identical owner interruptions.
