# Prompt Patterns

## Compact template

```text
Create [IMAGE ROLE] for [PRODUCT], [FORMAT].

STRICT PRODUCT ACCURACY IS REQUIRED.
Use [REFERENCE] as the exact and authoritative product reference. Do not redesign, enhance, reinterpret, simplify, or invent product details. If styling conflicts with accuracy, preserve the product and adjust the styling.

PRODUCT SPECIFICATION
- [confirmed construction, material, dimensions, color]
- [decoration/manufacturing method]
- [exact artwork, wording, personalization, accessories]

ACCURACY-CRITICAL REQUIREMENTS
- [fragile feature]
- [what it must never become]

COMPOSITION
- [product placement, scale, angle, crop]
- [panels, callouts, footer, empty space]

EXACT TEXT
- Product: "[verbatim text]"
- Overlay: "[verbatim text]"
- Footer: "[verbatim text]"

QUALITY
[lighting, texture, shadows, realism, marketplace readability]

DO NOT
[product-specific failure modes, extra text, distortion, watermark, cropping]
```

## New POD product demonstration: embroidered-look print blanket

User request: Create an Etsy hero image for a personalized family-name sherpa blanket. The sellable product uses a flat printed design that resembles stitched lettering; it is not embroidered.

```text
Create a premium square 1:1 Etsy hero image for a personalized family-name sherpa blanket. The blanket should fill most of the frame while its overall rectangular shape and finished edges remain understandable.

STRICT PRODUCT ACCURACY IS REQUIRED.
Treat the supplied blanket mockup and artwork as the exact and authoritative product references. Reproduce the sellable product faithfully before applying any room styling, folds, lighting, or marketing treatment. Do not redesign, enhance, reinterpret, simplify, or invent any product detail. If styling conflicts with product accuracy, preserve the blanket and adjust the styling.

PRODUCT SPECIFICATION
- Rectangular throw blanket with a smooth printed front and white sherpa reverse.
- Preserve the exact blanket proportions, edge finish, front color, and white sherpa backing shown in the reference.
- Preserve the exact family name, established year, typography, botanical border, artwork placement, spacing, and scale.
- The front decoration is a flat sublimation-style print. The artwork may visually resemble stitched lettering, but the physical product is not embroidered and has no raised thread.

ACCURACY-CRITICAL REQUIREMENTS
- Keep the printed artwork flat, straight, centered, proportional, and fully recognizable across the fabric surface.
- Natural fabric folds may affect the blanket surface slightly, but must not rewrite, duplicate, stretch, skew, or rearrange the design.
- Show a small, physically plausible turned corner revealing the white sherpa reverse; do not make the entire front fluffy.
- Do not add piping, tassels, fringe, quilting, stitching, zippers, or labels unless present in the reference.

COMPOSITION
- Arrange the blanket neatly over the lower portion of a warm neutral sofa, with the personalized front facing the camera.
- Use a near-front three-quarter view that keeps the design legible and avoids extreme perspective distortion.
- Keep props minimal and outside the printed design area. Do not cover the family name or established year.
- Leave restrained clean space around the product; no overlay text is required.

QUALITY
Photorealistic premium lifestyle product photography, warm natural window light, realistic shadows, accurate smooth-front fabric texture, tactile white sherpa detail, balanced neutral interior, and strong Etsy-thumbnail readability.

DO NOT
No real embroidery, raised thread, chenille lettering, appliqué, embossing, knitted design, furry printed front, altered artwork, misspelled personalization, duplicated border, warped typography, extra text, people, hands, gift box, watermark, white halo, artificial cutout edge, cropped product, or implausible floating folds.
```

Why this follows the method: it identifies the reference, locks the sellable construction, distinguishes printed appearance from actual embroidery, limits folds that could deform artwork, and makes room styling subordinate to product fidelity.
