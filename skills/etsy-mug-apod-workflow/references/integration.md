# Placement and phase contract

This is a product adapter. The existing `etsy-apod-product-workflow` remains the only generic coordinator. Do not copy its full generic workflow into a new independent orchestrator or create another plan/state file per supporting Skill.

| Entry or phase | Owner of that phase's artifact | Contract |
|---|---|---|
| Direct mug request / `$etsy-mug-apod-workflow` | Current coordinator agent | Recover scope, attach mug profile, enter generic coordinator once |
| Generic APOD coordinator already active | Same coordinator | Load mug-specific references only; return to current phase |
| `brand-marketing-growth` | Positioning/marketing phase | Return supported audience, gift intent, claims and buyer-question coverage; no second end-to-end launch |
| `etsy-coach-integrated` | Research/copy phase | Return evidence-linked keywords, copy and field matrix; existing full-build vs narrowed-scope contract controls |
| `etsy-listing-image-studio` | Thumbnail phase | Return actual native files, role mapping, technical QA and use eligibility; do not restart research or application |
| `image25-mockup-workflow` if specifically applicable | Existing image handoff phase | Reuse the same role/asset ledger; not a replacement research/coordinator owner |
| APOD application | Current coordinator and one browser operator | Apply only eligible authorized changes, save/reopen and reconcile exact remote state |

`phase_only` is a written handoff convention, not a universal API parameter. Pass the task record, product/variant/artwork IDs, phase scope, source paths/hashes, current decisions, required outputs and next permitted action. A worker returns artifacts to the coordinator; it does not modify the shared browser or another worker's files.

## Discovery and compatibility

Resolve dependencies using the current skill catalog, then read their actual `SKILL.md`. Do not hardcode a Windows user path, cached plugin version, tab ID, account token or tool implementation. The adapter was initially checked against coordinator 1.0.0 and integrated with completed 1.1.0 as 1.1.1. Later optional references may be used only if present. Core required capabilities are: scope recovery, field coverage, APOD save/readback and explicit completion boundaries. A newer release number alone is not compatibility evidence.

The standard complete workflow uses four companion Skills: `etsy-apod-product-workflow`, `brand-marketing-growth`, `etsy-coach-integrated`, `etsy-listing-image-studio`. Conditional dependencies (for example the actual browser skill, a research connector or video tool) must be discovered in the running environment. They are not installed or authorized by a ZIP. Avoid loading unrelated ornament/mat profiles.

Existing Growth/Coach/Studio routes converge on the generic coordinator. Coordinator 1.1.1 and the accompanying Studio update resolve this adapter's mug profile by name without recursively invoking its entry. Explicit invocation remains a deterministic entry after installation; when the runtime exposes its description, a mug-specific request may also select it implicitly. If the runtime's catalog is cached, refresh/restart a task using the runtime's documented mechanism; do not claim it has loaded an unlisted Skill.

## Missing capability or concurrent writer

If a required Skill is missing, finish independent source/local draft work, provide the exact dependency name and prepared handoff, and report that end-to-end execution is unavailable. Do not claim full execution using a silently invented fallback. A user-authorized alternative can be adopted explicitly.

Only one operator writes a product at a time. Before application compare actual APOD state with the recorded baseline. Unexpected drift or another active writer pauses that mutation; independent work continues. For shared Skill files, keep a separate staged contribution while another task owns them; do not overwrite its WIP or send it messages without human authorization. Verify hashes immediately before any authorized installation/update.

Changes to this adapter do not change Global AGENTS, remove downstream acceptance checks or create permanent permission for publishing, paid usage or customer-data changes. A current explicit user exception takes precedence only within its stated scope.
