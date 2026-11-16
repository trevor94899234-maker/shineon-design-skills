---
name: etsy-listing-image-studio
description: Generate and quality-check Etsy listing thumbnails or fidelity pilots from a scoped product brief, preserving original design and exact supplied copy.
---

# Etsy Listing Image Studio

Use this skill for a scoped fidelity pilot or an Etsy thumbnail production brief. A pilot needs the inputs used by that image; a full set also needs its approved listing/positioning and per-row plan. It supports local draft creation and review; it does not authorize upload, publication, or listing edits.

## Scope boundary

For an entire selected-product workflow that also includes research, listing fields and actual private APOD saves, route to [etsy-apod-product-workflow](../etsy-apod-product-workflow/SKILL.md). This Studio remains the sole thumbnail production/QA method. If already handed an active image phase, return files, hashes, attempts and QA to that existing coordinator; do not restart research or add platform-write authority. Image-only/pilot requests remain here. The coordinator reduces redundant questions, not source/route/QA gates. Owner exceptions follow the acceptance reference's exact-file or expressly delegated bounded-batch rules; no permission is inferred from ordinary continuation.

For mugs, resolve `etsy-mug-apod-workflow` by name and read only its `references/mug-profile.md` for variant/handle/print/light evidence. Keep the active image phase and existing coordinator; do not launch another product workflow. The profile supplies no inherited product facts, batch exceptions or method-switch authority.

This is the image-production step, not the research or listing-decision step. It does not choose keywords, write the listing title, decide product positioning, or create final overlay copy. Those inputs must be locked upstream under current authority: `OWNER_APPROVED`, `OWNER_DRAFT_AUTHORIZED`, or `AGENT_IMPLEMENTATION` within an explicitly delegated brief. The last status is a valid production input, not fictional owner approval. It may flag a conflict or suggest a correction, but must not silently change locked wording or strategy.

Read [references/handoff-intake.md](references/handoff-intake.md) when receiving another agent's brief, reconciling owner answers, or deciding what actually blocks the requested image. Reuse current owner confirmations and readable assets before asking questions. Separate missing handoff data, a new owner decision, and a rendering limitation; do not make the owner resupply data to solve a tool problem.

For a 20-thumbnail brief, generate exactly 20. Do not assume every Etsy listing needs 20; use the image count explicitly approved in the brief. This skill does not perform data research or make the image count decision.

## Ornament / 掛飾 profile

For ornament thumbnails, fidelity pilots or image QA, read [references/ornament-thumbnail-profile.md](references/ornament-thumbnail-profile.md) alongside the current acceptance rules. It covers irregular silhouettes, hole/cord contact, source-supported surfaces, personalization, distinct buyer questions and the scoped logo-only exception. It does not transfer another SKU's material, copy or permissions, and it does not apply journal geometry tests to ornaments.

When the user instead requests the entire Growth-to-private-APOD process, resolve [etsy-ornament-apod-workflow](../etsy-ornament-apod-workflow/SKILL.md). An active image-phase handoff stays here: return exact files/QA to the existing task record without restarting research, creating a second plan or adding upload authority.

## Owner generation-route default

For a new product or materially new direction, prepare a short plan: exact product/source, buyer/giver/recipient, occasion/use, authorized N distinct roles, exact copy/personalization scope and actual route. Recover any current owner direction confirmation or explicit delegation of that direction before asking. Routine composition within a locked brief is `AGENT_IMPLEMENTATION` and needs no new direction confirmation. If a material direction remains owner-controlled and unanswered, confirm it once before the initial authorized pilot. Inspect the pilot's actual file before continuing already-authorized rows. A passing pilot does not pre-pass later files or authorize extra attempts; row-specific gaps stop only dependent work. A matching plan/pilot is reused on resume, not approved again.

When this owner invokes this skill for authorized thumbnail or fidelity-pilot generation, use ChatGPT web's Create image / image-creation mode through the in-app browser by default. This is the owner's standing route preference; do not ask them to repeat it for each product. A later explicit owner route instruction takes precedence.

Use the reference-led whole-image method in [references/reference-led-geometry.md](references/reference-led-geometry.md): same-product sources, original artwork/logo, sourced physical proportions, optional silhouette/role layout and per-file QA. Do not silently substitute Codex's built-in image-generation tool, an API, another service or pasted-product compositing. If the web route is unavailable, report the actual blocker and continue independent preparation; obtain an explicit route change before substituting. Handle any login or sensitive interaction under the existing owner/browser rules.

Verify the actual ChatGPT page and image-creation control through the current documented browser tools. This default chooses the service workflow, not a guaranteed backend model/version or geometry lock. Keep the current brief's count, attempt/spending limits, source requirements and QA gates; invoking this skill alone does not authorize new generations or subscriptions.

## Mat / floor-plane profile

For welcome mats and other floor products, read [references/mat-floor-plane-profile.md](references/mat-floor-plane-profile.md). Ground product and printed art in the scene's floor perspective; an oblique floor mat must not remain a front-facing rectangle. The profile includes adaptable 16 lifestyle + 4 information roles, authorized logo-only/inset boundaries and per-file floor/occlusion QA. Its historical role count, product facts and approvals are not new defaults. Keep native video QA in the active coordinator after the thumbnail gate.

## Owner thumbnail format default

For this owner's Etsy thumbnails, default to native 1:1 square composition and request 2000 x 2000 pixels or higher when supported. Owner update, 2026-10-27: native 1245 x 1245 pixels or larger is acceptable, including 1254 x 1254; 2000 x 2000 remains the preferred requested size, not the default hard minimum. Record the preferred request, the minimum acceptable native size and the actual decoded dimensions separately. Validate width == height and both axes >= 1245 unless the owner explicitly locks another acceptance minimum for that brief. Never upscale to satisfy a native minimum. This owner-specific size change does not approve artwork/logo differences or waive other QA and exact-file owner-review gates. An explicit future owner override takes precedence; non-thumbnail uses retain their approved formats. Follow the detailed format and workflow checks in the acceptance reference.

## Acceptance gate

Read [references/thumbnail-acceptance.md](references/thumbnail-acceptance.md) before planning, generation and QA. Lock the approved count and use its per-image and set gates before claiming completion or publication readiness. Logo-awaiting or undersized drafts remain incomplete; workflow changes require approval when not already covered.

When a brief requests thumbnails followed by a product video, apply the [thumbnail-before-video gate](references/thumbnail-acceptance.md#thumbnail-before-video-gate) before starting that SKU's video generation or rendering. Keep its video phase blocked until the matching thumbnail set passes the referenced acceptance and delivery requirements.

## Workflow

### 1. Lock the product and evidence

- Inspect the user-supplied product photos/mockups and the relevant listing source before generating. Treat the supplied product image as the visual source of truth for shape, cover layout, colors, visible hardware, and sample text.
- Separate verified product facts from draft copy, owner statements, inference, and unknowns. Keep unsupported attributes `TBC`; do not invent dimensions, materials, interior pages, personalization fields, packaging, processing time, shipping time, or customer feedback.
- Adopt explicit, SKU-matched owner confirmations for the claims they support, with that provenance; do not require supplier re-verification unless the brief or a real conflict requires it. A confirmed fact does not prove the appearance of an unseen surface. Do not ask already-answered questions again.
- If multiple source images conflict, preserve the conflict and pause only the image concept that depends on the disputed fact.
- Use an approved logo asset when available. Do not redraw or alter it. If the logo asset is missing, ask for it or clearly label the draft as awaiting the logo.

### 2. Check the approved production brief

- First lock the phase and authorized active rows. For a fidelity pilot, require a readable same-product reference, exact printed/overlay text, the required logo asset, a supported view/scene, workflow, output target and existing attempt history. When its copy and context introduce no new listing claim, missing title/keyword research, interior photos or the remaining set plan do not block this pilot. It remains a fidelity pilot, not an accepted SEO set.
- For a full production set, also check the upstream locked listing title/positioning, keyword context when used by the brief, and the per-image copy/role plan with its authority status. Delegated `AGENT_IMPLEMENTATION` wording is usable within that brief without another line-by-line owner approval. For a 20-image set, keep one 20-row plan with distinct buyer questions. A 20-row plan does not authorize generating all 20 when only a pilot is active.
- Explicit instructions to generate local drafts can authorize using supplied draft copy verbatim without making it final-approved copy. Do not seek another approval merely to repeat the already-authorized draft task. Merely receiving a draft document is not a generation instruction.
- Pause only rows that depend on a missing input or unresolved conflict. Explain the dependency and continue authorized independent work. Omit optional unsupported claims instead of manufacturing a question or blocking an unrelated row. If the user only wants visual concepts, label them as non-final concepts without SEO claims.
- Treat the approved listing title and keyword plan as consistency checks. Do not paste the whole title onto an image or add extra keyword phrases. Render only the exact per-image text authorized for the current draft or final phase.

### 3. Build the image plan

- Execute the approved image count and selected rows; do not choose or reduce the count. A platform maximum is a ceiling, not a target. Verify current Etsy guidance only when the task depends on a current platform rule; an owner-locked format does not itself require a fresh policy lookup.
- Give each image one main job, such as product clarity, personalization, scale, material, features, use case, gift context, or ordering. Avoid near-duplicates that only change a prop, person, or background.
- Map the approved Product, Buyer, Recipient, Sender/Giver, Occasion, Use case, Personalization and emotional meaning separately. Buyer, giver and user may be the same person; use not applicable where appropriate. Show the relationship and action that answer each row's buyer question, rather than borrowing another product's gift story. Mark illustrative scenarios as such.
- Plan camera angles across the batch using the acceptance reference: vary supported views while preserving legible technical/personalization views. Angle quality and product/artwork fidelity must pass independently; retain original assets until explicit replacement approval.
- Respect Etsy's first-image guidance. If the user requests overlay text or a logo on every image, including the hero, follow that explicit direction and make the resulting tradeoff visible in the plan.

### 4. Generate with product fidelity

For reference-led trials, identify the actual same-SKU, same-revision personalized mockup and each other reference's purpose. Prefer the fewest sources that still establish the needed facts, without assuming that fewer references improve fidelity. For a controlled comparison, change a meaningful supported input or control and retain the exact prompt, references, candidate files and prior attempt history. A single result cannot establish a success rate.

- For the default ChatGPT web workflow, read [references/reference-led-geometry.md](references/reference-led-geometry.md), including its reusable request and QA record, before generation. Also use it for proportion drift under an explicitly approved alternate route. Use original same-product references, a verified physical ratio and per-file screening; neither a model name nor one passing pilot guarantees later geometry.
- Check the actual exposed tool controls before a new attempt. For a background-only trial, record whether the operation was a prompt-only request, an actually drawn UI selection/mask (with its scope), or another observed control. Prompt-only wording is not selection evidence; a real selection still does not prove unchanged pixels outside it. Prompted dimensions, reference-strength language and model claims are not tool settings. Record requested versus measured native dimensions. After a systematic failure, change a supported control or method before retrying; never promise native 2K or exact logo preservation because the prompt requests it. If the current route cannot establish the locked acceptance minimum, report a tool limitation rather than requesting unrelated product data. Missing the preferred 2000 x 2000 request alone does not fail a file that meets the owner's current native minimum. Keep the one-pass rule and existing attempt budget; do not silently switch to paid APIs, compositing or upscaling.
- Keep the product's natural proportions and straight edges. Do not stretch, skew, reshape, or add cover features.
- Keep overlay copy outside the product itself so a viewer cannot mistake it for printed product content. Use exact upstream locked wording under its recorded authority, and inspect every line for spelling, punctuation, and legibility.
- Add text and logo in the same image-generation pass when the user explicitly requires one-pass output. Otherwise, choose a workflow that best preserves accurate typography and logo fidelity; never claim an approximate generated mark is the official logo.
- For long exact text, use the source text verbatim and inspect the generated image at full size. If the text is altered or unreadable, regenerate or deliver an explicitly marked layout draft; do not present it as copy-accurate.
- UGC-inspired means staged lifestyle context unless genuine customer media is supplied and authorized. Never fabricate a review, rating, customer quote, endorsement, or real-customer identity. Avoid legible incidental text on props.
- For Scripture, legal wording, or other exact source text, retain the cited source and any user-defined distinction between preview text and what is printed on the product. Make that distinction prominent in the image when a buyer could otherwise misunderstand it.

### 5. Review and package

For each image, check:

- The product still matches the reference and has natural geometry.
- The image has the requested overlay and logo, with readable and accurate copy.
- Overlay text stays off the product and does not turn an unknown into a claim.
- The image has a distinct role and composition within the set.
- No fake review, customer evidence, or unsupported prop/product claim appears.
- Dimensions and format meet the current platform recommendation, or the resolution limitation is clearly disclosed.

For larger sets, provide a numbered folder, a contact sheet, and a ZIP when useful. Preserve earlier versions rather than overwriting them. Report the verified count, dimensions, unresolved `TBC` items, and whether anything was uploaded or published.

## Approval boundary

Local drafts and reversible edits are allowed within the user's requested scope. Uploading, publishing, editing a live listing, spending money, or changing shop settings requires separate explicit owner approval.
