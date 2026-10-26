# Aumakua consistency profile

Version 0.1.0 · 26 October 2026

This additive profile connects prose consistency findings to the project's compact ontology. It reuses core SourceDocuments, SourcePassages and existing Claims; it adds Audit, Finding and CoverageRecord, with separate SKOS schemes for classification, lifecycle, detection origin and reading mode. It uses the same Turtle/RDFLib/pySHACL stack and local-only validation. The power schema and its old datasets are unchanged.

The maintained [Aumakua workflow](../../../../.agents/skills/aumakua/references/ontology-workflow.md) keeps the independent prose sweep first. It freezes that record, then consults explicitly selected graphs and prior issues. A graph suggestion is an invitation to inspect the source, not a contradiction judgment.

## Records

| Record | Required meaning |
| --- | --- |
| Audit | Pinned narrative revision and prose-first snapshot, actual coverage, exposure/order note, and any explicitly inspected graph |
| Finding | At least two quoted source fragments; classification, separate lifecycle and detection basis; aligned scope, reasoning, compatible readings; relevant existing Claims with bounded relevance or an explicit extraction gap |
| CoverageRecord | Passage, reading mode, reviewer-declared Claim mappings and an extraction note; contextual links alone do not claim complete extraction |

Findings are analyst review records, not power Claims or unqualified story facts. A source-only finding remains valid when the conflicting commitments have not been extracted. Classifications include compatible readings and intentional ambiguity so rejected suggestions can be preserved without calling them contradictions. Resolution needs evidence. The profile records earlier stable finding IRIs without silently importing old reviews.

Quote-bearing SourcePassages reuse `prov:specializationOf` to identify the pinned source document and retain precise locators. Short exact `ac:quotation` strings are checked against local UTF-8 text; optional inclusive line windows are checked too. Every finding passage needs directly-read coverage in the same audit. These checks establish text identity and record structure, not interpretation, source authority or that someone actually completed the reading.

## Execute

From the repository root, with the [core requirements](../requirements.txt) installed:

```sh
python -X utf8 docs/power-review/ontology/consistency/validate_consistency.py \
  --data outputs/REVIEW/audit.ttl \
  --data outputs/EXPLICITLY-SELECTED/review.ttl \
  --manifest outputs/REVIEW/input-manifest.json --repository .
```

Omit the second data option when there is no selected existing graph. Explicit data and the audit's own manifest are required. Core and consistency SHACL run together, followed by source-hash/character-ID checks, quotation checks and five named SELECT views. No old pilot, remote imports, inference or rule expansion are loaded. The input manifest covers the union of local SourceDocuments in all selected fragments. Its format and `ExactBytes`/`LFNormalizedText` conventions match the core validator.

## Suggestions and limits

`candidate-relational-disagreements` finds opposite known truth values for the same subject, predicate, object, case, jurisdiction and authorial status with overlapping year bounds. `candidate-quantity-differences` finds different known values sharing subject, predicate, case, jurisdiction, authorial status, unit, accounting basis and quantity kind, again with overlapping years.

Both queries are conservative and incomplete. Exact-string units and bases can miss equivalent expressions; coarse years can combine different instants. Conditions, metric definitions, narrative stance and changing law still need prose interpretation. Cases and statuses that differ are intentionally excluded from these views; reviewers must still inspect integration mismatches across approvals and versions. No automatic entity merging, unit conversion, knowledge-set counting, institutional-before-foundation reasoning or full-text extraction is claimed.

The other views expose finding-to-claim links, passage coverage and directly-read passages without a declared Claim mapping. Absence of a mapping is an extraction question, not proof of inconsistency; a mapped passage may still be incompletely extracted. None of the queries writes a Finding or changes a lifecycle or authorial status.

The [linked pilot](../../../../outputs/aumakua-ontology-20261026/report.md) converts the saved independent prose audit into this profile. It preserves the five original findings and explicitly shows missing fine-grained extraction. Its zero candidate rows do not clear the text: the known disagreements were never fully represented as comparable core Claims. The [tests](../test_consistency.py) separately exercise candidate detection, compatible scope differences, missingness, quotation identity and finding lifecycle boundaries.
