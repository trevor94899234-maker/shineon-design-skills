# Product geometry lock

Owner-authorized 26 October 2026 after repeated journal width/height drift. This supplements product fidelity, exact artwork, original logo, natural-scene and whole-output generation gates; it does not authorize image generation, pixel compositing, publication, unlimited retries or lower another QA gate.

## Choose the applicable shape method

The numeric W/H, four-front-corner prompt, measurement algorithm and optional script below apply to products with an appropriate rectangular front face and verified physical dimensions, such as the evidenced journals. They must not be forced onto an irregular silhouette, circle or custom-cut ornament.

For irregular / non-rectangular ornaments, read [Studio's ornament profile](../../etsy-listing-image-studio/references/ornament-thumbnail-profile.md). Record exact SKU/source, supported view, visible silhouette landmarks, tab/hole/cord and artwork placement. When physical W/H is unavailable, keep it TBC; use SOURCE_VIEW_REVIEW for the actual source-supported visual comparison, not the numeric ratio script or a physical-dimension PASS. Dimensions, measured-scale images and other dependent claims stay HOLD. Other authorized image roles may continue only if their own source/fidelity checks pass. An explicit current brief requiring verified physical geometry still blocks its dependent work; this branch is not a waiver. Rectangular-product requirements below remain unchanged.

## Before generation: source and geometry record

For each SKU record physical front-face width W, height H, units, source path/URL and date, target ratio r=W/H, exact product/variant identity, geometry reference and its scope. Unknown dimensions stay TBC; do not infer inches from a photograph or borrow another journal's dimensions. A 1000-square source photograph or 1254-square generated canvas is not a square book. The print-area pixel ratio can differ from the physical cover and must not replace it.

Owner photographs may illustrate silhouette, thickness, rounded corners and finish without establishing exact SKU identity or real-world dimensions. Explicitly label each input as geometry-only, exact sellable product, artwork, logo or style. Do not transfer another reference's name, design, faith text, accessories or packaging. If source dimensions and the owner's required physical shape conflict, resolve the conflict instead of silently distorting artwork or inventing a measurement.

Example for the currently evidenced vow journal ONLY: physical width5.8in / height8.5in gives r=0.68235294, H/W=1.46551724. D.webp supplied by the owner is an oblique geometry-only appearance anchor, not an exact dimensional measurement or permission to copy its Jesus Follower / Patricia design. Other products need their own verified ratio.

## Prompt contract: geometry outranks scene

Put actual numbers and reference roles into every prompt; retain the independent artwork/brand locks. Example:

> Preserve the actual front cover's width-to-height ratio W/H={r}, physical width {W}{unit} and height {H}{unit}. Height is {H/W} times width. Keep the cover near front-facing, camera facing the cover plane with minimal perspective distortion and all four front-face corners visible. Rotation within the image plane is allowed, but do not stretch, widen, shorten or skew the product to fill the square canvas. Adjust camera distance, margins, people and surrounding scene instead. Preserve artwork and print-relative placement. The geometry-only reference supplies shape, never its other product design or text.

When proportion is the defect under repair, use a near-frontal view and simplify grip/occlusion before requesting dramatic angles. Keep meaningful recipient/giver/occasion/use-case action; do not replace a required gift/use scene with a decorative image to get an easy ratio pass. Any source-supported alternate angle must keep a separately identified view reference; apparent silhouette ratio under perspective is not intrinsic physical ratio.

## Every-output geometry QA

Check the full native image before thumbnail crops. Mark the four **front-face** corners in cyclic TL,TR,BR,BL order, excluding spine, page-block depth, ribbon, cast shadow and any bounding rectangle around a rotated object. Rounded covers require consistent extrapolated straight-edge intersections; record uncertainty rather than pretending subpixel exactness. Product resizing for a comparison may only be uniform. Never repair an output by nonuniform stretching, free projective warping, cutouts or later re-pasting the cover under the whole-output method.

For an independently judged nearly frontal, minimally perspective-distorted face, calculate mean opposing width / mean opposing height and compare with r. Record native-pixel anchors, physical source, tolerance and why it fits this task's corner uncertainty. No universal tolerance is imposed: select and disclose a task-specific screening tolerance before grading; do not loosen it after a failure. Report signed/relative error and the actual measurements. If corner uncertainty exceeds the tolerance, view/hand occlusion prevents measurement or dimensions are unverified, HOLD geometry.

For tilted/foreshortened scenes, opposing edges, angles and vanishing directions help detect projection, but they do not prove physical ratio. A four-point homography forced onto the desired rectangle can turn *any* quadrilateral into that ratio, so it is not verification. A min-area rectangle, raw rotated bounding box or segmentation outline is also not proof of physical geometry. Use a calibrated/view-matched source when available; otherwise choose a more frontal generation or keep the geometry gate HOLD. Even a perfect 2D rectangle can hide orthographic foreshortening; rendered-ratio consistency alone is never a physical-product certificate.

The optional `scripts/check_product_geometry.py` performs a conservative mathematical screen of **supplied** native-pixel front-face anchors. Require `dimension_source_review=verified` plus an actual non-placeholder `physical_dimension_source`; unknown/TBC dimensions HOLD. This supplied review flag is not source authentication. The tool neither detects the product automatically nor authenticates corner annotations, view declarations or actual SKU geometry. Its SCREEN_PASS is a subcheck, not overall QA/owner acceptance; unverified view, excessive perspective, out-of-bounds/invalid anchors or ratio failure cannot become PASS. Pair it with visual product/brand/anatomy/contact/role and150/300px checks.

## Acceptance and batch control

Keep separate counts: generated candidates, geometry-screen pass, full visual-QA pass, owner accepted and source-proven roles. Owner acceptance of an exact candidate does not prove its measured physical ratio. Every final image needs its own geometry record, even after one successful pilot. Flag ratio errors before delivery; candidate batches explicitly requested for owner judge may still be delivered with per-file failures/HOLDs visible, never called20 qualified roles. Updating this Skill does not reset previous failures or confer a new retry budget. Stop or revise within actual owner-authorized scope; no third-party service/compositing fallback or hidden extra attempts.
