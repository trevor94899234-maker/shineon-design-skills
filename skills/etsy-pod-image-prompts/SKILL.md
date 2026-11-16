---
name: etsy-pod-image-prompts
description: Create, revise, audit, or standardize image-generation prompts for Etsy print-on-demand product listings, including thumbnails, feature infographics, personalization guides, size/material close-ups, lifestyle scenes, and multi-panel images. Use when prompts must preserve an uploaded product reference, exact artwork, text, materials, construction, dimensions, personalization, or other product details, especially when product accuracy must override composition and styling.
---

# Etsy POD Image Prompts

For ornament / 聖誕掛飾 prompt planning, use [Studio's ornament profile](../etsy-listing-image-studio/references/ornament-thumbnail-profile.md) for product-specific source/role constraints; the actual generation and QA remain in Studio. Full Growth-to-APOD requests may enter [etsy-ornament-apod-workflow](../etsy-ornament-apod-workflow/SKILL.md). Prompt-only work remains prompt-only; an existing phase handoff does not restart the upstream workflow.

## Current thumbnail execution handoff — owner 2026-10-27

For MyGiftStyle thumbnail creation, corrections and per-file QA, read and use the exact local `etsy-listing-image-studio` as the sole production entrypoint, even when this prompt skill was selected first. Studio's default is ChatGPT web image creation through the in-app browser; follow its reference-led method, active-row authority, native-size requirements and exact-file QA/owner decisions. Do not wait for the owner to name Studio again. If Studio or its browser route is unavailable, report the blocker; do not run the old built-in generator or an API as a fallback without an explicit owner route change.

This skill supplies source-grounded role/prompt specifications when needed; a prompt-only request remains prompt-only and does not launch generation. Do not route back to Growth for the same production handoff or copy a second execution method here. Before actual generation, report the production skill actually read, chosen route and current source/row scope. A skill handoff is not a separate agent or extra execution/spending permission.

This owner update supersedes older thumbnail-specific built-in-generator commands throughout this skill's references, including dated method notes; read them for applicable source/role/quality evidence, not as permission to restore an older route. Preserve count, recovery limits, evidence and QA requirements. Original product-design artwork and editable-master rules remain separately scoped and unchanged; this is not a hard merge or a source-asset replacement.

Geometry amendment 2026-10-26, explicitly owner-authorized: apply the [product geometry lock](references/product-geometry-lock.md) before every thumbnail prompt and to every rendered candidate. Verified physical width/height, angle and measured product-face ratio are separate from square output dimensions. A wrong or unmeasurable product proportion cannot pass because the artwork, style or wording looks correct. The method detects/rejects failures; it does not guarantee the image generator obeys geometry.

Geometry scope clarification, 2026-10-27: for irregular / non-rectangular ornaments, use the geometry lock's ornament branch and [Studio's ornament source-view profile](../etsy-listing-image-studio/references/ornament-thumbnail-profile.md), not the journal four-corner algorithm. Unknown physical dimensions remain TBC and block dimension/scale claims; source-supported visual roles may receive SOURCE_VIEW_REVIEW, never a numerical physical-ratio PASS. Existing rectangular-product tests and any explicit owner-required geometry gate remain binding.

Revision: 2026.10.20.1. Add the owner-requested per-SKU 20-thumbnail completion gate before starting its 15-second product video, with independent role/file/QA accounting. Retain all stricter source, native-resolution, brand and generation-method requirements. Previous revision: 2026.10.19.1. Require the built-in image generator to produce each complete thumbnail, including scene, text, branding and lighting, in one output; preserve product-art Canva work and every fidelity/release gate. See [16 October method correction](references/thumbnail-method-change-2026-10-16.md) for source and superseded routes. Previous revision: 2026.10.15.1. Add the source-first designer/LED and bounded thumbnail pilot workflow after the 14–15 October audit; retain every prior role, fidelity, reference-quality and APOD gate. Previous revision: 2026.10.12.1. Add the owner-requested mockup-first APOD delivery bridge and saved-gallery/video evidence boundary; retain 2026.10.11.7. Reconcile verified Faithful 1–3 customer-chosen letters beneath the leaf without changing Love’s 1–2-character corner contract. Reconcile saved Love v6 corner personalization and complete buyer-order instruction coverage; preserve separate APOD/Etsy and production gates. Retain 2026.10.11.5: Raise the listing-image requirement to the owner’s latest reference-level minimum quality, with a fully specified prompt contract and whole-scene lighting/contact/naturalness gates. Retain the 20-role workflow, exact product/brand locks and production-art rules; stronger saved requirements do not establish stable rendered output.

Source/change record: owner corrections on 11 October 2026 at 10:00 UTC (`Sentinel_fae793accd54819191d76dc75bfd6035`) establish the MyGiftStyle UGC requirement; the 11:10 UTC instruction (`Sentinel_86fb1dd88c9081919478e76a0d566047`) requests detailed execution of the agreed 20 roles, only the specified folder for style references, readable integrated typography/branding and anatomically correct hands. See the dated source boundaries in the workflow reference. The later instruction `Sentinel_2826fa3dd2148191962695c66bb9a52d` raises the latest 24 supplied JPEG references to a minimum quality floor, not optional inspiration. These revisions change listing presentation and execution, not approved product art or production-file requirements.

## Product-design artwork method lock (20 October 2026)

First apply the current explicit owner method and applicable project instructions. The historical built-in-generation/Canva defaults below apply only where no more specific valid method is in force; preserve other projects' existing source locks. Where the applicable ShineOn Graphic Design project/owner instructions select ChatGPT web art-only generation plus native APOD fixed/custom text, follow that choice without requiring a Canva master/export. This precedence adds no API, service, compositing, spending or platform-write authority and does not permit visual reconstruction.

For MyGiftStyle product-design artwork under that historical default, all new or revised visual art must come from the built-in image-generation tool. Preserve the original generated style. Canva may only edit authorized wording or add independent custom-name/text fields, place the unchanged generated art on the verified supplier canvas and export it. Do not replace illustration with Canva shapes/assets, abstract stock elements, hand-drawn/vector reconstruction, SVG/code art or another design engine. A resolution or print-detail failure remains HOLD: use a permitted built-in generation correction when feasible, never reinterpret it as native vector art or claim upscale pixels are native detail. Retain the original generated file and generation provenance, and record each text-only Canva change separately. Supplier originals and actual mockups remain evidence/reference/QA sources, not permission to invent new art. This scope is product-design artwork; it does not prohibit authorized educational-web code or separately authorized video editing/overlays. The stricter complete-output thumbnail rule below remains unchanged. Within its applicable scope, this historical source lock supersedes older generic “native master” or Canva-rebuild suggestions, not existing source records or their historical status.

Source: owner message Sentinel_3afca01140c88191987498f65338a00f.

## APOD full-build handoff

When images are part of “開始 listing building” or an equivalent MyGiftStyle full build, resolve etsy-coach-integrated and read its references/apod-ready-listing-build.md first. Do not begin thumbnails before the exact APOD product/design has generated and exported an actual inspected mockup, followed by the authorized keyword/copy stage. Supplier facts and actual visual reference are distinct. Produce 20 distinct accepted roles per product under the existing quality floor; Hero role 01 must be first. After generation/QA, return actual files with hashes and role map for authorized APOD upload, selection/order, save and reopened asset reconciliation; files or prompts alone do not complete the build. Preserve unique assets, recoverably deselect only in-scope irrelevant duplicates and retain rollback evidence.

Natural light/contact/anatomy, exact readable product text and product fidelity remain mandatory. AI UGC-style scenes are illustrative, never real reviews/customer evidence. Do not pass missing real-photo, delivery or buyer-field proof by filling the slot with decoration. Required native videos, their actual two-if-supported/otherwise-at-least-one capability, playback/frame/duration checks and AutoFulfill OFF are owned by the same APOD contract. No “all ready” verdict from 20-image count alone; no automatic Etsy push or payment. This bridge changes completion scope, not product-art approval or the 20-role facts.

## Per-SKU thumbnail-before-video gate

For a requested 20-thumbnail / 15-second product-video package, use `etsy-listing-image-studio` and its current thumbnail-before-video acceptance gate by default. The [batch workflow evidence](references/mygiftstyle-batch-workflow.md#per-sku-twenty-thumbnail-gate-before-video) supplies supporting per-SKU accounting, not a competing renderer. Complete and QA all 20 individual thumbnail roles for each SKU before starting that SKU's video production. Two products require two separately verified 20-role sets, never 20 files shared between them. Record exact files, technical findings and scoped owner acceptance; planning, prompts, contact sheets and other SKUs' accepted files do not unlock video. Preserve Studio's native dimensions, logo identity and other requirements; explicit exact-file exceptions must remain documented without relabeling failed technical findings. Studio is not an alias of this skill and must not be overwritten from it.

## MyGiftStyle execution entrypoint

For this shop's thumbnail/listing work, read these references before planning or generating:
- [Source-first production and thumbnail workflow](references/source-first-thumbnail-workflow-2026-10-15.md): read first for supplied designer assets, LED text conversion, repeat imagegen failures or batch restart; preserve native artwork/text and audit before generation.
- [Reference-level minimum quality](references/mygiftstyle-reference-quality-floor.md): latest owner reference standard, complete prompt contract, whole-scene acceptance and dated [24-file identity record](references/mygiftstyle-quality-reference-sources-2026-10-11.json).
- [20-role execution plan](references/mygiftstyle-20-role-execution.md): each slot's buyer question, source requirements, scene, copy examples and acceptance/rejection tests.
- [Visual acceptance gates](references/mygiftstyle-visual-qa.md): style-reference isolation, typography, exact branding, product fidelity and hand anatomy.
- [Batch workflow and source contracts](references/mygiftstyle-batch-workflow.md): current product-field scope, evidence inventory, representative proofs, per-file map and release boundaries.

The 20 roles are the owner's current journal brief, not a universal Etsy or APOD rule. Preserve role intent when current SKU facts differ; mark missing evidence HOLD rather than fabricating content or replacing a blocked function with a decorative image. Example overlays are adaptable drafts, never universal fixed copy or owner-approved text.

Treat product fidelity as the controlling requirement. Build prompts as production specifications, not loose mood descriptions.

## Establish the source of truth

1. Identify and visually inspect the authoritative product reference before reference-based generation: uploaded image, supplied artwork, written specification, or a combination. Read the complete visible artwork and exact name/text; a filename, prompt description or cropped motif is not sufficient source inspection.
2. Separate confirmed facts from assumptions. Do not invent details that are not visible or specified.
3. Preserve exact product identity: shape, proportions, material, color, construction, accessories, artwork, typography, wording, placement, scale, and personalization.
4. Ask only if an unresolved detail would materially change the product. Otherwise choose a simpler view that avoids exposing the unknown detail.

Start reference-based prompts with a product lock:

> STRICT PRODUCT ACCURACY IS REQUIRED. Treat the uploaded product image as the exact and authoritative reference. Reproduce the product faithfully before applying any scene, lighting, composition, or marketing requirements. Do not redesign, enhance, reinterpret, simplify, or invent any product detail. If a styling instruction conflicts with product accuracy, preserve the product and adjust the styling.

## Lock the artifact and method

Record whether the task is original product artwork, an editable print master, a listing thumbnail, another listing image or a real product photograph. Route original-design selection to Integrated Etsy Coach and an authorized editable Canva/print-art task to Canva Personalizable Product Art; this listing-image skill does not replace those workflows. Keep simultaneous tasks and their buyer angles separate; approval of a seasonal/newlywed variation does not replace the original year-round/anniversary brief.

Record source-native pixels, requested artwork canvas, measured export dimensions and listing-image dimensions separately. A product-artwork size does not change a thumbnail target. Preserve a bare dimension pair as supplied and label any inferred units or width/height order; obtain supplier-template confirmation before production approval. Do not invent bleed or safe areas.

For thumbnail creation and corrections, hand off to `etsy-listing-image-studio` and its current authorized route. Keep source-grounded product, scene, requested text/callouts, brand treatment, lighting and shadows together in one complete output under the whole-image brief. Supply the inspected exact product/mockup, original brand asset and authorized appearance references. Do not assemble thumbnails in Canva, paste product cutouts or insert text/logo later. Preserve the source-first recovery limit, explicit no-overlay briefs and real-photo provenance requirements; no corrective counter resets on handoff.

Canva remains only for authorized text changes, independently editable names and unchanged-image placement/export on supplier canvases, not creating/reconstructing visual artwork or thumbnail assembly. Text-only LED lettering changes must preserve the generated visual art. Source inspection, read-only QA, measured previews and separately authorized APOD media uploads remain allowed; do not confuse them with thumbnail editing. A named product proof from the product-art workflow may be an input reference, never a later pasted replacement.

The owner's “Image 2”, “Image 2.5” or historical built-in-tool wording is not proof of the backend model actually exposed. Report Studio's actual service route separately from any verified per-call backend metadata; otherwise keep the exact version TBC. This does not authorize a CLI/API workaround, external model switch, new paid service or spend. Method instructions are targets, not guarantees of exact pixels, spelling or logo identity: inspect the actual output and preserve failed/HOLD findings and separately scoped owner decisions. Do not revive older thumbnail compositing/overlay permissions or fallback proposals.

Read [listing-image-readiness.md](references/listing-image-readiness.md) when choosing listing slots, calling an image Etsy-ready, or preparing a publication-readiness judgment.

## Words for Your Days product profile

Resolve `canva-personalizable-product-art` and its current product profile for original artwork/editable masters. For listing instructions, first bind the exact design/version to the verified field contract in [batch workflow](references/mygiftstyle-batch-workflow.md). Current Love v6 APOD has required full name plus explicit PRINT/NO PRINT corner branches; read the scoped profile/status record for actual IDs, font labels and manual validation gaps. Prior Love v5 name-only remains historical/NO PRINT. Faithful now has verified saved APOD PRINT initials / NO PRINT branches: PRINT requires 1–3 exact customer-chosen letters beneath the leaf, never bottom-right or inferred from the name. Main Daniel remains fixed Playfair Display 900; Love’s main Elizabeth remains fixed Tinos. Read the scoped profile for branch IDs, three verified fonts, native maxlength bypasses and manual review. Prior Faithful v4 name-only is historical/NO PRINT. Never treat other requested changes as implemented. For Courage, Hope and Stillness, retain the required full name and explicit PRINT/NO PRINT corner branch only where confirmed for that exact draft. PRINT uses 1–2 customer-chosen visible characters, not inferred initials; blank remains unresolved. Use only actually verified current corner-font mappings, never historical A/B/C labels as proof of available options. Main-name font stays fixed unless specifically verified otherwise. No profile authorizes account edits, production orders or publication.

## Core creative gate: one story with emotional resonance

Apply this gate during planning, generation and review, not only after technical QA. A pleasing pattern or correct PNG is not enough.

- **Plan:** name one specific buyer, recipient/relationship and occasion or life moment. In one sentence, state what the recipient should feel—such as seen, loved, encouraged or supported—and why this exact gift can express it. Treat that response as a creative hypothesis, not a promised buyer reaction or sales result.
- **Generate:** make the design title/headline, body message and visual composition tell one original story. Give each element a clear role; choose the intended hierarchy among name, message and motif so a decorative arch/title cannot accidentally overwhelm the personal meaning. Do not stack generic faith phrases, ornaments and symbols without a coherent connection. Keep listing copy consistent with that story and actual product facts; do not add text to an explicit no-overlay brief or silently rewrite approved wording.
- **Review:** read the title and body aloud with the image: does their combined meaning speak to the chosen person and moment, or is this merely attractive decoration? Compare a new variant with its actual prior version for message clarity, emotional fit and hierarchy before expanding into eight designs or another bulk set. Describe what improved and what remains uncertain; one technical pass or isolated attractive detail does not approve the whole series.

Use respectful faith language. An original blessing is not a Bible quotation; verify the text, translation and applicable usage rights before attributing wording to scripture. Do not invent verses, promise spiritual/medical outcomes or guarantee resonance, conversion or profit. Preserve the owner's approved words and artwork unless a specific revision is authorized.

Keep three decisions separate: technical/product-fidelity pass, evidence-backed creative recommendation, and the owner's approval of that exact creative version. A previously generated variant or a reviewer preference is not owner approval and must not become a universal template. Report this gate briefly as the intended feeling, how text and visual support it, and the remaining approval—not a heavy new checklist.

For new personalizable gift artwork, make the recipient and their name the protagonist: the fixed title, body and illustration should support that person, not turn the name into a small afterthought. Compose a compact, intentional name area integrated with the message and visual rhythm—not a large empty void. This is scoped to original personalized product art, not a requirement to add name overlays to every listing image or redesign approved art.

For newly generated original personalized product artwork only, use the built-in image-generation route for the complete fixed title/body/visual composition while omitting the custom name entirely; Canva then adds only the native editable name in a coordinated, actually available font. Fixed text need not be rebuilt as separate native elements unless a verified error, layout need or explicit editability request requires it. Check all fixed wording. Before extending the direction into a series, inspect actual rendered named proofs with representative short and long names and the intended final name at the product's print scale; a name-free preview alone cannot pass this gate. Check prominence, compact spacing, balance, clipping and whether the message still feels addressed to the recipient. Reuse the latest explicit authorization for the identified version/expansion; do not ask for the same approval again. Proof review does not authorize production orders or publication.

## Mandatory production-art rules

Apply these owner-required rules to standalone original production artwork and its handoff, not to the background of a listing lifestyle scene. The default complete production-art deliverable is a background-free transparent PNG, one complete file per design/SKU/print area; only an explicit verified supplier/process exception changes that requirement. Distinguish an intermediate illustration asset, complete artwork composition, editable Canva master, review board/product mockup and verified final production file. Do not call the current transparent decoration asset a finished product unless the complete composition, editable name and actual export gates have passed.

1. **Generate transparency natively.** For standalone print artwork, explicitly request a transparent background and enable the generation tool's real transparency option (for example, `transparent_background: true`) when exposed. Do not generate a brown, cream, leather-textured, paper-colored, product-shaped or fake-checkerboard backdrop intending to remove it later. Show substrate color, material and lighting only in a separate accurate preview. Prompt wording alone does not establish native alpha. If the selected route cannot produce transparent output, report the blocker instead of silently changing the deliverable to opaque art.
2. **Preserve editable names.** Generate the static art without baking in the custom name; reserve a clear name area. Add each name as an independent native Canva text element in the editable master, verifying selection, editing and saved persistence through `canva-personalizable-product-art`. A name inside a PNG is never proof of editable text. Do not erase or regenerate an already approved design without the necessary limited-change approval.
3. **Keep raster art print-simple.** Prefer a small number of clear motifs, strong readable linework, sufficient stroke width and open gaps at the actual physical print size. Avoid dense ornament, microtext, hairlines, tiny isolated marks and intricate detail that may close up or disappear. Inspect the artwork at its intended print dimensions using the actual SKU/template and print process; a large screen preview is insufficient. Use supplier-specific minimum strokes, gaps and type sizes where available; unknown limits stay unknown, never invent a universal pixel rule. Upscaling does not create detail or make an overcomplicated design printable.
4. **Generate each design as its own complete composition.** Verify the intended SKU, printable surface, physical dimensions, canvas/aspect ratio, resolution, bleed and safe-area requirements before production-oriented generation. Record unknown requirements and keep that output provisional. Three series designs require three separately generated complete artwork compositions with their own clear name area, not one triptych/contact sheet/collage. Never extract cropped panels, patch missing portions, or use a later review board as a production source. Assemble review boards only after the independent artwork files exist. A decorative illustration asset is an intermediate, not a finished product design.
5. **Match the real canvas without false native-resolution claims.** Request the verified aspect ratio with the generator's available controls; measure the actual generated dimensions. Tool limitations may prevent an exact requested pixel size. Place the complete standalone composition on the verified Canva supplier canvas, add the independent native text and export one complete file per design. Do not plan to crop or stretch a collage into shape. If the ratio/layout does not fit, correct the approved composition or regenerate rather than cutting off or reconstructing missing art; disclosed non-destructive fitting is not extra native detail. Report actual native pixels separately from the Canva canvas and final export; no upscaling-quality claim.
6. **Compose separately for every confirmed SKU and print area.** A shared theme is a design system, not a universal bitmap. A journal and an acrylic plaque require two independent complete compositions; bags, shirts, variants and additional print areas each need their own verified mapping and layout. Generate/compose each separately for the real width/height units and pixels, ratio, bleed, safe area, print process and background requirements. Do not stretch, crop or reuse one universal production image to make different products fit. The historical journal 1410 × 2220 and plaque 3540 × 3186 values are examples, not verified requirements for the current SKU. If requirements are missing, label the file provisional and block direct production use.
7. **Label and map every file.** Include product, confirmed SKU/variant, print area, actual dimensions and ratio, artifact role and verification status in the filename where practical and in a small mapping manifest. Separately record native generation size, supplier-required canvas and measured export size; a filename is not verification. The manifest must bind each preview to its exact complete master/export. For a multi-product offer, reuse `brand-marketing-growth`'s existing Bundle checks for each item's cost, packaging and possible separate shipments; matching artwork is not proof of a fulfilable or profitable bundle.
8. **Verify actual output.** Check downloaded pixels, dimensions and required alpha, including light/dark background inspection for opaque fills, halos, remnants and fake checkerboard. Keep visual/print-size review distinct from metadata checks. Missing checks remain unverified; do not claim production readiness from a generation setting or attractive preview.

A supplier-confirmed full-bleed background, engraving/cut workflow or another non-transparent specification is an explicit, recorded exception: use that SKU's actual file/process requirements, not a transparent-PNG default. State the reason and approval/specification source. Transparency by itself never proves print suitability.

These rules constrain new designs and authorized revisions. They do not authorize simplifying approved artwork inside a fidelity-locked mockup. If approved source detail fails the print-size check, preserve it, explain the affected detail and obtain approval for a simplified revision before altering it.

## Apply the priority order

Resolve conflicts in this order:

1. Product identity and accuracy
2. Artwork and design integrity
3. Exact wording and personalization
4. Material, construction, dimensions, and accessories
5. Composition and layout
6. Marketing information and overlays
7. Scene, props, lighting, and mood

Never sacrifice an earlier item to improve a later one. Simplify the angle, scene, or styling when necessary.

## Build the prompt

Use only sections relevant to the requested image:

1. **Task and format** — image role, aspect ratio, pixel size if supplied, and intended marketplace use.
2. **Product lock** — authoritative reference and non-redesign requirement.
3. **Product specification** — material, construction, size, color, printing method, accessories, and exact design elements.
4. **Accuracy-critical details** — fragile features that image models commonly change.
5. **Composition** — crop, camera angle, scale, orientation, panel arrangement, callout positions, and empty space.
6. **Exact text** — distinguish product text, overlay copy, labels, and footer. Quote every required string verbatim.
7. **Scene and quality** — lighting, surface, background, shadows, texture, realism, and customer-facing mood.
8. **Negative constraints** — likely failure modes specific to this product and image type.

Repeat a critical constraint where the model is likely to violate it, but keep ordinary instructions concise.

## Describe manufacturing truthfully

State both what the decoration is and what it is not. Examples:

- flat printed ink, not engraving, embossing, debossing, embroidery, foil stamping, vinyl, or raised transfer;
- fully clear transparent acrylic, not frosted, tinted, smoky, opaque, or solid-backed;
- continuous smooth hardcover wrap, with no hinge groove, recessed channel, score line, or spine depression.

Do not use material or process language merely for visual effect when it changes the sellable product.

## Control multi-panel consistency

Require every repeated product to retain identical construction, artwork, typography, personalization, proportions, and accessories. Permit only the explicitly requested variable—such as LED glow color, viewing angle, or use context—to change.


## Plan gift imagery around buyer questions

For a coordinated listing set, assign each image one distinct buyer question or useful product view before generating. Separate recipient/occasion recognition, relationship gift moments, personalization instructions, verified features and everyday use. A new crop, background or headline alone is not a new function. For MyGiftStyle, default listing thumbnails and supporting listing images to UGC-style natural phone-photo human-use or gifting scenes unless the owner explicitly changes the style for the identified task. Use believable everyday surroundings, coherent motivated window or practical-lamp light and a credible use/gifting context (human action only where relevant), with strong, short buyer-intent overlays that remain readable at thumbnail scale when overlays are requested. Do not substitute white studio/editorial infographics, isolated cut-out product cards or repeated template cards. Keep size, material and personalization explanations grounded in a truthful lifestyle scene where feasible, with concise legible callouts; factual clarity and product fidelity still take priority. Preserve explicit no-overlay briefs. Treat generated scenes as illustrative marketing, never actual customer photographs, reviews, testimonials, endorsements or customer proof; they do not replace the actual finished-product photography required for a primary listing image. Preserve scene and prop truth.

**Pre-batch style gate:** before expanding any listing set, inspect an actual rendered representative scene at full composition and 300/150 px, and compare it with the active brief and approved appearance reference. Confirm natural UGC-style human use/gifting, short readable overlays where requested, and exact complete product artwork, name, material, construction and original branding. Follow Studio's single initial authorized pilot and inspect its actual output before continuation. Check size/personalization and other role families within their remaining authorized rows before scaling that family; do not require an extra second initial pilot, extra generation calls or repeated approval of unchanged rows. A written prompt, good file count or attractive white card does not pass this gate. Correct a style or fidelity failure before batch generation; retain the passing reference file and apply the same gate to every final. Reuse existing explicit owner approval within its scope rather than asking again, and keep QA separate from owner acceptance.

Treat approved appearance references as visual evidence, not new product facts or blanket brand rules. Read design documents in their stated scope. Reserve natural negative space before positioning the product; keep short buyer-intent overlays outside the cover. Judge gift-worthiness, typographic elegance and emotional action alongside readability. Do not repair a weak layout with heavy black text, a dark gradient, product cards or label boxes. Freeze the approved direction and retain its actual file; approval of that direction does not make later files automatically correct.

For a complete listing set, read [listing-function-coverage.md](references/listing-function-coverage.md). Map every function required by the active brief to actual final files and visible evidence. Check file count/delivery, visual QA, factual accuracy, functional coverage, owner acceptance and publication readiness separately. Twenty delivered images or many attractive gift scenes do not prove that the listing answers its practical buyer questions. Missing specifications, interior evidence or processing facts remain explicit gaps rather than invented images or claims.

## Preserve source artwork and original brand assets

Use Studio's current complete-output generation route above, binding the exact master/mockup and branding as inspected input references. Prefer a simpler source-supported view instead of an untruthful angle. [Source-preserving gift imagery](references/source-preserving-gift-imagery.md) is retained as historical method/QA evidence, not an active thumbnail fallback; old compositing permissions do not override the 16 October correction.

Do not confuse use of the supplied brand reference with permission to invent a logo or omit branding. Include the verified original MG A5 asset among the generation inputs, specify its unchanged geometry, spelling and colors, and generate its placement outside the product as part of the same complete output unless the owner directs otherwise. Do not later insert it in Canva. Compare actual generated branding against the original; a reference or prompt cannot guarantee identity. Missing, substituted, distorted or product-obscuring branding fails delivery: make only an eligible targeted retry on the current Studio route, otherwise HOLD and explain the exact defect.

## Verify the rendered deliverable

Inspect each final at full composition and at actual 300 px and 150 px. When an overlay heading is requested, require the primary buyer-intent heading to survive 150 px; require any essential instructions and personalization limits to read at 300 px. Preserve explicit no-overlay briefs. Do not promise tiny cover details or logo descriptors are readable at 150 px. Review original logo fidelity, perspective, foreground hands, contact shadows, edges and any reference-visible accessories. For a journal that actually includes them, check its elastic and single connected ribbon. Require visible, coherent physical support and a shared contact plane; hold an ambiguous or impossible pose even when all source pixels match. Pixel fidelity and natural integration are separate gates: neither compensates for failure of the other.

Measure actual export dimensions and color profile. A 2000-square file derived from a smaller generated scene or source master is a derived export, not native 2000-pixel detail. Preserve approved originals, version corrections, record source/asset hashes and final file hashes, and retain complete generated outputs, prompts and input references, plus any existing historical masks/transform records where applicable; do not create compositing artifacts for the current thumbnail method. Have an independent reviewer inspect consequential product/brand invariants before bulk delivery. Report completed counts accurately and distinguish visual QA from owner acceptance or marketplace publication.

## Audit before delivery

Check:

- Did the pre-batch rendered style gate pass, and does every MyGiftStyle final retain the required UGC-style lifestyle direction rather than a white studio/template card?
- Is it unmistakably the same product as the visually inspected reference?
- Are artwork, wording, spelling, typography hierarchy, and personalization preserved?
- Are material, manufacturing method, construction, dimensions, and accessories accurate?
- Did any scene or composition instruction implicitly force a product change?
- Are all panels internally consistent?
- Does the actual set satisfy each required buyer function in its source-grounded coverage map, independently of image count and visual quality?
- Are overlay strings exact and readable at Etsy thumbnail size?
- Does the negative list target realistic failure modes without contradicting the positive specification?
- Are unsupported details omitted rather than invented?
- Is required original branding present and faithful in the exported file?
- Do source preservation and physical integration both pass, including foreground hands and product edges?
- Are dimensions, color profile and native-versus-derived resolution reported truthfully?

Deliver the finished copy-ready prompt first. Add a short assumptions note only when useful.

For patterns and a new-product example, read [references/prompt-patterns.md](references/prompt-patterns.md).

## Transfer video lessons without changing thumbnail method
For a task crossing images and video, read [video method boundary](references/video-method-boundary.md). Video repair success does not override the current complete-output thumbnail workflow.
