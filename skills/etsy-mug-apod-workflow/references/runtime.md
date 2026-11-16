# Local / SE / agent execution and recovery

“SE” is treated as the user's intended agent runtime, not a verified product/API name. This Skill is portable instructions plus records. It cannot promise authentication, browser capability, provider availability or access to local source files on an unidentified remote host.

## Preflight the actual environment

Verify relevant capabilities, not a hardcoded vendor implementation: readable Skill dependencies; actual source bytes; a writable task directory; image view/decode/hash support; authorized research access; required ChatGPT web generation route; APOD page access; a human-input channel if needed; save/reopen verification. Use currently documented tools. Where a service plugin can perform the task adequately, prefer it; where the user specifies a route, preserve that choice.

Missing capability blocks only its dependent phase. A prompt prepared on a remote agent is not an image generated in the browser. A local path written into a cloud handoff is not file access. A ZIP delivered is not a remotely installed Skill. Existing logged-in access may be used within scope; acquiring login/OTP/CAPTCHA or sensitive access follows current human requirements. Do not extract cookies/tokens or invent private endpoints.

## Portable handoff contract

Transfer only the authorized minimum: relative task paths, original sources/brand hashes, current plan and scope, actual human decision evidence, technical findings, exact use bindings, last saved-state receipts, pending jobs and cumulative attempt/cost counters. Keep secrets, browser profiles, tokens and unnecessary private content out. Preserve safe public URLs when useful, not bearer tokens or signed secrets.

The receiving operator verifies manifest hashes and source identity, discovers its own tools/paths, reads current state, checks for an active operator and resumes the next allowed action. It does not re-interview already-answered questions, re-download everything, regenerate completed roles, reset attempts or presume old tab IDs still work. Use a dedicated operator assignment in the task record; workers return source/copy/QA artifacts without controlling that browser.

Installation in an identified destination is a separate authorized action: inspect its existing catalog, compare versions/hashes, back up conflicts and apply only the approved change set. Never bulk-overwrite a newer Skill with a bundled snapshot. Local installation and read-only test evidence do not establish remote installation or live integration.

## Recovery decision table

| Observed issue | Safe next action within existing authorization | Do not do |
|---|---|---|
| Empty attachment error for a valid reference | Inspect file decode/size and actual composer. If documented route permits, use an ASCII alias or lossless transport copy; verify decoded pixel identity and new attachment order before Send | Count it as a generation, change artwork silently, or submit with missing references |
| Composer restores old attachments after refresh | Inspect actual names/thumbnails; remove only identified obsolete task attachments, then verify final mapping | Assume previous prompt indices still match |
| File chooser/control not found | Re-read current accessibility/UI and tool docs, then use the observed role/control | Guess selector names repeatedly or inject hidden app state |
| Generation call observer times out | Reinspect the same conversation/job and retrieve existing output if completed | Send the prompt again before determining outcome |
| Media download handle expires | Reinspect the actual generated result and documented download controls; bind recovered file to that result, decode and hash | Pick the newest unrelated download or guess private media URLs |
| Save/upload times out | Read actual product/library/selection and determine whether it persisted; apply only still-missing authorized operation | Blindly upload duplicate files or save stale full-form values |
| Tool connection fails normally | Use documented reconnect/reselect and revalidate URL/state | Treat every connection failure as account logout or immediately ask user |
| Explicit browser safety/policy stop | Follow that tool's stop/recovery instructions; preserve state and continue unrelated offline work | Reset runtime, switch controllers/browser, guess URL or reattempt to bypass the stop |
| Native file too small or malformed | Verify actual returned original; recover a missing original if supported, otherwise hold affected row | Upscale to claim native compliance or fabricate a new accepted file |
| Systematic product/logo redraw | Diagnose with original sources and attempt history; obey method stop and current bounded owner instructions | Restart counters on another agent, replace source with generated approximation, silently composite |
| Unexpected APOD drift / another operator | Record exact conflict; hold mutation and establish ownership | Overwrite another task's work or assume older local snapshot is current |

Transport diagnostics and QA previews are not final image editing. If a final-image method changes, current method authority is required. Preserve byte and pixel checks with what each proves; same dimensions alone are not pixel identity.

## Minimal reliable operations journal

Before mutation record operation ID, product/role/revision, expected result, actual selected input hashes, operator, status `PREPARED`. On submit store observed job/asset locator and status `SUBMITTED`. After uncertainty use `OUTCOME_UNKNOWN`, then inspect. After actual readback record `PERSISTED_VERIFIED` or a specific failure. Treat these as record states, not a guarantee the tool is idempotent.

A receiver's first action for `SUBMITTED` or `OUTCOME_UNKNOWN` is inspection. Only a demonstrated absent/failed operation plus still-valid authority permits a new attempt. A retry limit is not permission to duplicate a successful submission.
