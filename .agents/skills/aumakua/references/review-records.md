# Records for substantial consistency audits

Use these fields when a review spans several sections, must be repeated, or will support a before/after comparison. Markdown is sufficient; use structured data only when the task benefits from it. Keep the review record outside canonical prose.

## Scope and coverage

Record the review question, date, repository revision, source hashes where needed, authority order, and any unavailable sources. List the sections directly read, the files searched only, and relevant material not inspected. State whether earlier findings were withheld, already known, or consulted after the independent sweep. Describe tool checks actually executed and their limits.

A clean mechanical check is evidence only for the condition it checks. Do not translate “stable IDs validate”, “arithmetic reconciles” or “SHACL conforms” into “the story is consistent”.

## Issue ledger

For each material issue record:

| Field | Content |
| --- | --- |
| Stable ID | Retain on later reviews; avoid renumbering surviving issues. |
| Classification | Contradiction, suspected contradiction, integration mismatch, missing bridge, or numerical/model discrepancy. A compatible reading or intentional ambiguity may be recorded as a non-finding. |
| Lifecycle | Open, retained, resolved, not reproduced, or outside scope; keep this distinct from classification. |
| Evidence | Both passages, source revision/hash, precise locator and short exact quotation. Include the governing approval when relevant. |
| Aligned scope | Entity, time, place/jurisdiction, conditions, status, narrative stance, and quantity basis as applicable. |
| Incompatibility | The commitments that cannot coexist; show an arithmetic or membership comparison where it matters. |
| Alternative readings | Supported reconciliations, assumptions that would be needed, and missing evidence. |
| Consequence | What continuity or reader understanding is affected; distinguish certainty from importance. |
| Repair options | Smallest alternatives and affected passages; mark proposals and unresolved author choices. |
| Prior issue mapping | Earlier IDs and disposition, when a prior review exists. |
| Ontology trace | Finding IRI, paired SourcePassage IRIs, relevant existing Claim IDs with bounded relevance, and missing extraction. For ontology-assisted audits read [ontology-workflow.md](ontology-workflow.md). |
| Detection origin | Prose first, graph suggested, or prior-issue reconciliation. Preserve the frozen prose-first record. |

Use “not reproduced” when the current pass cannot substantiate the earlier issue; explain why. Use “resolved” only with evidence showing how both sides now agree or why the earlier comparison had the wrong scope. A presumed off-page event is not resolution.

## Review conclusion

Lead with the most consequential supported findings. State the audit's actual coverage and material uncertainties. Separate new detections from retained issues and separate confirmed conflicts from requests for clarification. If no contradiction was found, report that bounded result rather than certifying the whole text.
