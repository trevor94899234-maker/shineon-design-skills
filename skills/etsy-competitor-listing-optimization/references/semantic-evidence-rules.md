# Semantic evidence: read the claim, its subject and its limits

## Decision tree for every factual label

1. Is the exact phrase present in an authoritative captured field for this entity? If not, mark missing/hypothesis. A word in the shop name, adjacent search result or another product is not evidence.
2. Is it the seller's assertion, a quotation, negation, example, conditional or option? Preserve polarity and quotation context. Do not keyword-match the whole page.
3. What is its subject: journal cover, pages, optional pen, bundle, packaging or another item? Label that subject only.
4. Does another source/section contradict it? Keep both claim IDs and mark conflict; do not silently select the attractive one.
5. What inference, if any, is still needed? Mark seller_stated versus independently_verified; copying a seller statement accurately does not verify manufacture.
6. Read the complete surrounding sentence before asserting a value. A validator can flag risky spans; only the reviewer resolves meaning.

## Recipient, buyer, sender, writer, user and deceased are different roles

Store multiple supported roles instead of assigning the first kinship word. Record actor + role + exact quote + certainty:

- “To my daughter. Love, Mom and Dad.” Daughter is recipient; Mom and Dad are senders. Buyer is unknown unless purchase text identifies them.
- “Tell me your story, Dad.” Dad may be gift recipient and writer; child may be eventual reader. A “from daughter” phrase supports sender, not automatic buyer.
- “Letters to my daughter.” Daughter is addressee/eventual reader; the writer/initial product recipient may be a parent and must remain unknown unless stated.
- “In memory of Dad. A grief journal for my daughter.” Dad is deceased/reference person; daughter is recipient. Do not treat a memorial as a living-father gift.
- “For mother, sister or friend.” Preserve alternative recipients; do not collapse to mother.
- “Not a gift for mother; a memorial journal for her grieving son.” Negation must remain attached to mother; son is the supported recipient.
- A generic family/Christian title does not establish every family relationship. Occasion/use and faith theme do not prove who is buying.

Review title, description, personalization instructions and visible design together when available. Contradictory roles remain conflict. Never copy another listing's roles. Preserve unknown buyer/sender rather than fill an intuitively plausible relationship.

## Material versus decoration/process

Separate material, process, target and variant. Examples:

- “Vegan leather cover. This journal is printed, not engraved.” Material = seller-stated vegan leather; cover process = printed; explicit negative engraved.
- “The phrase ‘not engraved’ is printed inside.” The quoted text is design/content, not proof of the cover's manufacturing process. Read quotation scope.
- “Optional engraved pen included with bundle.” Pen may be engraved; journal-cover process remains unknown.
- “We can engrave a logo on the front.” Available option, not evidence every default cover/name design is engraved.
- A shop named “InkedCustomPrints” does not prove printing; an engraved-looking image does not prove engraving.
- “Leather” alone does not prove genuine leather; “leatherette”, “PU”, “vegan leather” and “genuine leather” retain exact seller terms. Do not upgrade certainty or merge conflicting composition claims.
- Printed lined pages do not establish printed cover. A visual foil effect does not establish metal/foil manufacturing.
- Owner-confirmed printed lined-only supplier SKU outranks competitor patterns. A seller description promising guided prompts on that SKU is a truthfulness conflict to review, not useful keyword evidence.

## Display age

Use `parse_age` on the exact dedicated age string only. Accept 1.5 years as 1.5, 2.5 years as 2.5, 9 months as 0.75 display years; never capture the trailing “5”. A display duration is rounded and does not prove an exact opening date. Mixed durations are additive only when explicit (“1 year 6 months”). Multiple incompatible age statements require manual review. Calendar opening year, seller biography, birthdays and review dates are different fields.

## Metrics and prices

Keep raw value, normalized value, qualifier, missing reason, status, entity scope, period/window, market, provider and capture date together.

- shop lifetime sales ≠ selected listing sales ≠ recent/monthly sales ≠ US sales ≠ revenue ≠ profit.
- listing reviews ≠ listing sales; shop reviews are not listing reviews; reviews linked to other journals can support a shop's relevant product line only.
- Etsy source observations may be actual public counters; eRank/EverBee sales/revenue are estimates. Accurate transcription never changes estimated to actual.
- “<20” remains less_than, not 20 or 0. Missing remains null; a displayed zero beside “analytics unavailable” preserves raw 0 but interpreted_value is null/unavailable.
- Query result count is not search volume; actual tags are not measured demand; a shortened/recombined tag does not inherit a researched phrase's volume.
- Price and shipping are separate. Quantity/variant must be verified before comparing a one-item starting price to a two-item bundle. Never flag a wrong price solely from a title or assume all options share it.

## Semantic audit response

Build a risk-stratified independent sample from raw sources, not only the normalized table. One error opens a complete audit of the affected category; check dependent qualification and outputs. If role logic is defective, re-read every affected role record, not only rows matching the old regex. Preserve a correction trail rather than overwriting history.
