# Durable collection checkpoints

Revision 2026.10.15.1. Use during authorized multi-batch keyword collection or recovery. This is a preservation requirement, not permission for new queries, uploads, spending, schema changes or master imports.

## Before a new query

Inventory actual accessible raw exports and saved provider lists, preserving market/platform, exact terms, headers, capture date, metric window, monthly points and provider Last Updated separately. Reuse compatible observations for the current decision. A historical cumulative count or a summary mentioning a revision is not that revision's data. Determine a decision-changing gap and check the current task's query authority and stop conditions; do not restart cancelled batches or support/outreach tasks.

## Commit each observed batch before continuing

1. Preserve the full returned/exported raw rows and headings unchanged, plus exact submitted terms, source URL/provider feature, country/platform/filter scope, capture time, observed row count and pagination completeness. Keep threshold, zero, dash and Unknown values distinct. Do not store passwords, session tokens or authentication payloads in raw receipts.
2. Save an immutable local raw receipt and a manifest containing file size, SHA-256 where bytes are available, source/batch ID, expected rows and links to any derived observations. Read the actual file back and reconcile schema/rows before declaring the batch captured. Parsed tables are derived files, never replacements for raw evidence.
3. Preserve the raw receipt and manifest through an already authorized durable destination, such as Library, before the next quota-consuming query or risky environment transition. Record the returned durable file ID/version and verify the successful retained-file result; where supported read/materialize it and compare bytes/hash. Keep retention confirmed versus byte-round-trip verified distinct. A local path, filename, upload request or accepted chat delivery is not proof that the user opened the file. If durable saving is unsupported, unapproved or fails, stop further collection and report the exact checkpoint gap; continue analysis of safely preserved rows.
4. Record quota before/after, submitted batch count, term count and actual outcome separately. One observed 20-term submission changing 184 to 183 is one recorded batch event, not twenty charges or a guarantee that all providers/plans behave identically. For an uncertain response, check captured results/quota and durable receipts before considering another request; preserve policy-specific denial/retry limits.
5. Save a resume cursor with last verified batch, pending exact terms, active task scope, durable IDs and unresolved gaps. Advance only after the raw batch checkpoint is retained. Do not overwrite the previous known-good packet; version a derived packet and bind it to raw receipts and hashes.

## After restore or missing packet

Locate the original retained file or original worker's verified receipt. Check actual bytes and expected hash before calling a revision recovered. If the working packet is absent but raw batches survive, rebuild only derived data under the current authorized schema from those actual rows, retaining source joins and a new version; do not claim byte-identical recovery unless proven. If raw rows are missing, report the lost coverage explicitly. Never synthesize terms, metrics, sources or completed rows from aggregate counts, hashes, chat recollection or pending queues. A known hash can verify found bytes, not reconstruct them.

Keep inherited stop instructions in force. Read-only inventory and reuse do not grant new-query authority, and receipt preservation is not a master-library import, Dashboard update or local Vault synchronization. If a new task separately authorizes fresh research, name its scope rather than treating it as resumption of a stopped missing packet.

## Dated audit basis and regression cases

15 October recovery record: an expected r15 packet/hash was not found after workspace/Library/branch checks; reported totals of 913 terms, 1480 observations and 118 sources were explicitly last-recorded, not reverified rows. The packet was not reconstructed. A separate listing-keyword task retained five saved lists totaling 225 UI rows (45+43+50+50+37), not 225 unique or relevant terms, and a raw 20-term USA/Etsy bulk response with capture time 03:23:54 UTC and observed quota 184→183. The worker confirmed the saved-project packet and bulk raw receipt were retained in Library; that is not byte-round-trip verification or recovered r15. List Last Updated labels ranged 2022–2026 while row trend labels were Sep26/September 2026; keep those meanings distinct. These receipts support preservation and metric/date distinctions, not a universal quota policy or a recovered r15. Durable IDs and completion status belong in each run's manifest, not in a permanently hard-coded queue.

Regression: missing r15 plus known totals → missing packet, not rebuilt evidence; a saved average plus September point → separate metrics; Last Updated today → no automatic freshness claim; one successful batch not durably retained → checkpoint blocked before next collection; authorized analysis with a cancelled query → analyse existing rows only; local download and chat attachment → do not claim the user opened it.
