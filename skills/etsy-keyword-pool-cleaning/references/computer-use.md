# Computer-use execution card

Read this before the first browser action. Use the computer/browser tool documentation actually available in the execution environment. A skill does not grant computer access.

## Observe → identify → act → verify
1. Capture a fresh screenshot/UI snapshot. Record current page title, URL when exposed, account/project, selected market, selected research source, visible date range, and any dialog. Say which browser belongs to whom.
2. Name the single next goal. Find the control in the current snapshot by its visible label/role and surrounding section. A label in this skill is a conceptual purpose, not a promise that the UI uses those words.
3. If the control is not visible, inspect the relevant section or scroll one screen, then capture again. Do not guess a URL, selector, off-screen position, button label, or stale coordinate.
4. Name only controls visible on the current snapshot; if navigation requires returning through an intermediate page, observe that page before choosing its next control. Perform one logical operation: open one item, change one filter, enter one exact value, or download one file. Multi-keystroke entry in one field is one operation; changing unrelated fields is not.
5. Capture again. Verify the requested state is visible: exact query, market/filter chips, selected listing ID, displayed table, filename, or saved value. A click succeeding is not proof of task success.
6. Append evidence: step ID, timestamp, page/source, observed state before, action, observed state after, screenshot/artifact reference, next state. Never record secrets.
7. Only continue after verification. On failure use the routes below.

## Control recipes
- Search: locate visible search input → focus → replace existing query → enter exact query → submit by visible search control or Enter if supported → verify query and results heading.
- Filter: open current filter control → inspect visible options → choose requested market/platform/period → apply only if an apply control is present → verify resulting filter chips and results.
- Read a row: locate keyword/listing text and its column headings → read across that same row → preserve units, currency, period, and qualifiers (`0`, `<20`, `Unknown`) → save source reference. Do not infer a hidden value from neighboring rows.
- Open detail: capture row identifier/URL → open its actual link → verify detail identity before collecting data → capture source/date/definitions.
- Export: record current filters and displayed count → activate observed export/download control → choose existing format only if prompted → verify file completed, actual filename and openability → compare header and count with scope. A download toast alone is insufficient. Preserve original export unchanged.
- Edit a research copy: verify copy identity and destination → change the intended field → inspect resulting value/formula → save if required → reopen/read back. Do not edit the original raw export.
- Pagination: record current page and row count → use visible next-page control → verify page changed and first row changed. Stop at disabled/absent next control; log partial coverage on errors.
- Dialog: read its complete visible consequence before choosing. Cancel unexpected purchases, permission grants, destructive operations, or external publishing and ask for the required authorization.

## Failure routes
- Wrong account, shop, project, market, or product: stop dependent work; correct only using authorized visible controls, otherwise ask.
- Login, CAPTCHA, security warning, access denial, new permission or payment: follow platform policy and obtain required user action; never bypass. Save resumable state.
- Loading: observe again after a short wait; if still loading, inspect for a visible error. Retry a read-only operation at most once after checking state. Do not repeatedly click or duplicate writes.
- Missing control: inspect page navigation/help once; if still absent, log exact blocker and use an authorized export/connector alternative only if it does not bypass a restriction.
- Missing or ambiguous data: mark unknown and ask only if it changes the decision. Never fill a metric with zero to mean missing.
- Uncertain save/download: inspect existing state before any retry; report unverified if it cannot be established.
- Large data: do not claim full manual coverage after sampling. Use a verified bulk operation or deterministic helper with available permissions; otherwise deliver the inspected subset and clear remaining count.

## Resume record
Save task, input identifiers, shop/product, market/platform/period, current state, completed step IDs, source files, output paths, last verified page, unresolved questions, and required next action. On resuming, reload the actual source/UI and validate identity; do not reuse coordinates.
