# Native font evidence

Reviewed 2026-10-16. Read only when a supplied layered source or font binary can resolve an actual font dependency. This extends the existing designer-source triage, not a new font inventory, installation route or blanket licence review.

## Resolve the text that is actually visible

- Preserve the exact source identity and hash where bytes are available. Inspect visible text layers, text content and style/run ranges using an already available, permitted reader. Do not install a parser merely to satisfy this step without the applicable authority.
- Resolve each visible character range to its referenced family/style. Keep hidden layers, zero-length or terminator-only runs and fallback resources separate. A PSD FontSet can contain AdobeInvisFont or MyriadPro even when its visible heading uses another family; the table alone cannot identify every rendered font.
- Keep native text, rendered appearance and OCR evidence distinct. Native spelling can confirm an actual source-text defect; OCR alone cannot. A source defect does not prove the current live listing still shows that version.
- If run semantics or mixed styles cannot be resolved, record the candidate fonts and uncertainty rather than guessing. Source-level identification is useful for matching and rights triage but does not prove that Canva has loaded, selected or rendered the same font. Verify that separately in the intended master.

## Bind rights evidence to the used asset and intended action

Record the delivered file identity, embedded family/style/version and licence information where available, and the relevant authoritative publisher/licence source. Distinguish ordinary artwork/POD use from font-file redistribution, embedding, hosting or upload. A filename, embedded licence string or unrestricted embedding flag alone is not an all-rights clearance or proof of upstream binary authenticity. Preserve contradictory or missing evidence; use the existing bounded licence-evidence/substitution decision.

A font bundled but unused in the inspected design does not block that design by association. Conversely, the presence of another openly licensed family does not clear a visibly used personal-use font. Record the result for this design/version/use, not the whole shop. Do not add raw font binaries to a buyer package merely because artwork use is supported.

## Dated evidence and scope

The 16 October 2026 source audit resolved MD1362 Design3's visible heading/name to MADE TOMMY Bold; supplied files were labelled PERSONAL USE and separate commercial evidence was not established. Its native caption text also confirmed that garbled wording was not only OCR error. MD1362 Design4's primary source families were Cambria-Bold and Shoika-Regular despite additional fallback resources.

Separately, MD1301's exact delivered Outfit files carried version 1.100 and SIL OFL 1.1 metadata, supported by the [publisher repository](https://github.com/Outfitio/Outfit-Fonts) and [official OFL FAQ](https://openfontlicense.org/ofl-faq/). That supported the recorded ordinary artwork-use assessment for those files, not authenticity by upstream hash equality, all-assets clearance or font redistribution without its notices. These are historical source-audit findings, not current Canva-picker checks or permanent approvals for later files.

Apply the three native-source scenarios in the existing regression cases. A decision-only test does not validate Canva operation, rendering or legal clearance.
