# Complete listing field packet and final readback

Read for a full listing build, affected-field update or delivery audit. Reuse an existing packet; [field-packet.csv](../assets/field-packet.csv) is a starting checklist. Every applicable field has a value/disposition, evidence, action authority, actual editor availability and persisted readback. This is not permission to edit every field.

Use the current scope and these statuses: `APPLIED_VERIFIED`, `UNCHANGED_VERIFIED`, `PREPARED_NOT_APPLIED`, `NOT_EXPOSED`, `EXCLUDED_BY_OWNER`, `NOT_APPLICABLE` with reason, or `BLOCKED`. Distinguish a local draft from saved/reopened state. A field left untouched can be `UNCHANGED_VERIFIED` only after actual relevant readback. A future Etsy task is not complete because APOD cannot expose its field.

## Identity, source and production surface

| Field / decision | Prepare and check | Final evidence / boundary |
|---|---|---|
| Product, variant, SKU, catalog/template | Bind actual IDs, selected option and supplier catalog revision; retain before-state | Reopened same IDs/variant/SKU; title alone is not identity |
| Original artwork and design provenance | Identify original source file/hash, production-artwork ID/revision, front/back position and source authority; distinguish user artwork, supplier template, AI scene and brand source | Source master unchanged unless that exact edit was authorized; no generated lifestyle image promoted into manufacturing art |
| Template placement and print readiness | Actual canvas/print area, placed dimensions/effective PPI, bleed/safe area and current template mapping when production work requires them | Save/preview/render evidence if edited under authority; native source pixels or a gallery export alone do not prove fit |
| Same-product mockup | Actual exported/rendered file for the current artwork/variant with hash and visual inspection | Template placeholder, Ready badge or pending render is not an actual file |
| Supplier / fulfillment provider | Verified actual supplier and its selected product/variant | APOD supplier identity is separate from Etsy production-partner disclosure/mapping |
| Physical vs digital / who designed or made it | Truthful product type, designed-by/made-by/production method and required disclosure | Do not claim handmade, original authorship or a downloadable file merely from a template or POD label |
| Quantity and included contents | Actual single-item/bundle quantity, accessories, packaging and source | Distinguish props, delivery cartons and gift packaging; no invented included box |
| Materials, finish, print, colors, dimensions | Exact source wording/units and measurement scope; fixed art versus selectable colors | Printed gold color is not foil; scene scale/texture is not a tested specification |

A bounded digital preflight may use the actual official SKU template plus source/output and placement evidence. Separate canvas dimensions, density metadata, native raster detail, native text and effective PPI; label template document scale separately from independently verified physical mapping. Unknown factory behavior or an unpublished threshold is not by itself a new mandatory RIP-document or paid-sample gate. Preserve actual SKU requirements, observed defects and any required supplier/sample proof; record physical print results and production release separately. A conclusion for one template/revision does not waive another SKU's checks.

## Buyer-facing fields

| Field | Prepare | Save/readback test |
|---|---|---|
| Title | Clear item, actual differentiator and supported buyer phrase; current editor limit and real character count | Read entire persisted title; no internal DRAFT/status labels |
| Description | Opening benefit, exact item/quantity, specs, personalization, fixed/variable design, supported care, processing/shipping distinction, scope-appropriate limitations and honest image provenance | Compare **entire** clean value, including all paragraphs/disclosures, after final media/video save; a count or opening excerpt is insufficient |
| Tags | Required current contract count (13 for the full MyGiftStyle build), distinct truthful exact strings, current limit and evidence/bounded-test status | Enumerate actual saved tags/chips, not a blank search widget; compare complete set and duplicate/count conditions |
| Category / taxonomy | Correct current physical-product taxonomy when actually exposed | Actual selected label/ID from UI; no guessed taxonomy ID |
| Materials / colors / occasion / room / recipient / other attributes | Choose only supported applicable options actually offered by the editor | Read actual selected fields; putting facts into description does not apply Etsy attributes |
| Image alt text / shop section | Truthful accessible drafts and intended section when requested | Apply only where exposed and authorized; gallery captions/filenames are not alt text |
| Care / contents / image disclosure | Supported care and what arrives; supplier mockup, AI staged scene and information-card provenance | No real-customer-photo, testimonial, metallic foil, outdoor performance or supplied-packaging claim without evidence |

Retain natural American English for US buyers. A field packet may use owner-approved wording, authorized draft wording or `AGENT_IMPLEMENTATION` copy locked under delegated authority. Record that status and preserve exact downstream copy. Routine wording does not need line-by-line owner approval; an owner-required human gate or a new material product/offer promise still applies.

## Personalization, live preview and printable fit

| Field / state | Required distinction |
|---|---|
| Editable field inventory | Enumerate actual field names/types/order and mapped artwork variables; do not infer names/date/fonts from a sample image |
| Required vs optional | Read the actual saved required flag; instructions saying “required” do not establish that flag. Test an optional blank in the real preview/save/reopen flow. It must not print a placeholder, sample or orphan delimiter, and the remaining layout must stay readable. Automatic reflow is not required unless the brief or actual platform contract requires it |
| Exact instruction/example | Specify whether the buyer supplies full wording, prefixes such as “The,” spelling/case and supported separators; preserve exact saved instruction |
| Fixed content | Identify blessing, artwork, closing, decorative marks and any other fixed elements; avoid implying unsupported customization |
| Field character limit | Read current software capacity without changing it to fit copy; it is not a printable-name guarantee |
| Printable fit | Use authorized template tests for the supported lengths/line breaks, font and print area; retain tested cases/render evidence and untested extremes as TBC |
| Option layout / variant mapping | Actual combined/separate controls, variant/SKU mapping and artwork-managed status |
| Finite choice vs free text | Record the real control type and supported values, e.g. Mom/Mum. Free text is not proof of a finite selector; preserve requested options and mark unimplemented/untested mapping without blocking independent design work |
| Composite sender / name | Identify fixed prefixes/closings and whether the buyer supplies a whole line or only a name. A source layer such as “Love, Oliver” does not prove a separate baby-name field; verify the actual editable field and changed preview |
| Live preview | Read actual enabled/disabled state and whether the buyer experience was tested. OFF means no live-preview promise; ON alone does not prove correct mapping or printable fit |
| Manual review / AutoFulfill | Retain warnings and the controlling fulfillment requirement. Required personalization does not establish fully automated safe fulfillment |

If printable fit remains untested but the owner authorized a bounded private listing preparation, record that exclusion/gap explicitly. Do not claim production-ready or enable automatic fulfillment from input capacity alone. Never alter production art or enable live preview as an incidental copy edit.

## Offer, Etsy-only settings and commercial authority

| Field / decision | Check and boundary |
|---|---|
| Price, currency, discount, paid personalization | Current per-variant values and specific approved change; use [fees and offer](fees-and-offer.md) for calculations. A recommendation is not permission to save a new price |
| Inventory quantity / renewal / listing type | Actual Etsy quantity, renewal choice and physical/digital type where exposed; one APOD variant is not stock quantity or Etsy renewal policy |
| Processing / made-to-order | Source-supported production time versus shop promise; no invented rush option or delivery guarantee |
| Shipping origin / destinations / profile / buyer charge | Real eligibility, supplier shipping cost, buyer charge and service; preserve explicit owner exclusion without reopening it |
| Production partner | Actual Etsy partner identity, role and listing linkage; supplier name in APOD is not proof this mapping exists |
| Returns / cancellations / policy / buyer preview service | Current shop terms and actual offered service; no new refund promise, approval preview or cancellation window by inference |
| Gallery / primary / order | Eligible exact files mapped to actual saved selected assets; count selected items separately from the library |
| Video | Actual required count/duration, source order, clip QA, persisted player and any exact human gate; [native video](native-video.md) |
| Push / publish | Separately authorized Etsy action and live readback only; private APOD work grants neither |

APOD's inspected editor may not expose category, Etsy attributes, partner mapping, policies, inventory/renewal/type or alt text. Record `NOT_EXPOSED` based on the actual surface inspected, not a claim that APOD can never support them. Prepare truthful drafts where useful and identify the later owner/Etsy stage. Do not Push to Etsy merely to fill gaps or inspect fields.

## Cross-save readback — one final full comparison

After the **last** gallery/video/field save:

1. Reopen the same product and applicable modal/expanded variant surface. Capture actual title, entire description and all actual tags; compare to the intended packet. Normalize only documented line endings/Unicode; do not normalize away changed words or punctuation.
2. Read personalization field/type/required flag/instructions, current capacity, option layout, live-preview state and artwork mapping. Preserve untested print-fit caveats.
3. Read variant/SKU/artwork identity, current price/currency, AutoFulfill and warnings, plus any relevant excluded-setting preservation. Do not reopen an excluded shipping task to change it.
4. Reopen the selected gallery and actual product video. Compare count/order/primary and saved clip to their final manifests. A tutorial player or save toast is insufficient.
5. Mark each row with its actual status and receipt time after the relevant final mutation. Reconcile any unexpected overwrite before completion; preserve concurrent owner edits and ask only if there is a material conflict.

A local script that serializes observed values is a record of browser evidence, not itself live access. Distinguish operator-observed persistence, independent local evidence review and owner acceptance in the final handoff.
