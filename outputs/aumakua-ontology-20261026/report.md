# Aumakua ontology integration

26 October 2026

Aumakua now uses the project's ontology for a substantial audit when the profile is available. It freezes the independent prose sweep, then links findings to quoted SourcePassages and relevant existing Claims, records extraction gaps and actual coverage, and executes conservative graph queries to suggest further comparisons. Narrow passage questions can remain prose answers.

## Implemented and executed

The additive [consistency profile](../../docs/power-review/ontology/consistency/README.md) uses Turtle, separate SKOS schemes, PROV-O source provenance and SHACL with the existing RDFLib/pySHACL stack. It introduces Audit, Finding and CoverageRecord without changing the power schema or turning textual issues into power Claims. Classifications, lifecycle, detection origin and reading mode remain separate. A source-only finding is valid with an explicit claim gap; a contextual claim link does not imply that the conflicting propositions were extracted.

The [audit graph](audit.ttl) converts the five findings in the [saved independent prose review](../aumakua-pilot-20261026/actual/review.md). The original review is pinned unchanged as the prose-first snapshot. Its source narrative remains commit `4ea16e3a739c807a5f20bbb8ffb98450b84215c7`; the selected graph is the explicitly pinned Aegis rerun. This is a retrospective representation of earlier findings, **not another blind detection test**. No new graph-suggested finding was adopted.

| Check or view | Observed result |
| --- | --- |
| Core + consistency SHACL | Conforms |
| Pinned local inputs | 13 verified |
| Exact quotations in source line windows | 11 verified |
| Findings | Five retained from the saved prose review, preserving their classifications and open lifecycle |
| Coverage records | 11: ten evidence fragments and the original continuous §§4–8 sweep |
| Relational/quantity comparison candidates | Zero / zero on the selected existing graph |
| Finding/claim link rows | 14, including source-only findings with explicit gaps |
| Passage coverage rows | 17, because a broad sweep maps several existing Claims |
| Read passages without complete declared Claim mapping | Ten fine-grained evidence fragments |
| Regression tests | 35 pass: 20 existing and 15 new consistency tests |

The [executed JSON](validation.json) contains all five query views; [execution provenance](execution.json) pins the skill/profile versions and archived output bytes. [Tests](tests.txt) cover candidate detection, exclusion of differing cases/jurisdictions/statuses/units/bases/periods, unknown values, directly-read evidence, valid source-only findings, quotation identity and resolution evidence. Source hashes and quote checks verify recorded text, not its interpretation or authorial authority. Installation is backed up and hash-verified in [installation.json](installation.json).

## What the zero candidates mean

The original power graph does not fully encode the secrecy count, Council founding/report dates or the other conflicting commitments as comparable Claims. A query cannot recover an assertion that extraction omitted. The integration therefore preserves the prose findings and shows the missing fine-grained mappings rather than treating an empty candidate view as clearance.

Existing C01 supplies discovery/secrecy context; C06 supplies the 1852 administration context; C03 supplies receipt/mint context. The link notes explicitly limit their relevance. Abigail's stance issue and the Edo treaty-authority bridge remain source-only. No artificial power Claim was added to hide those gaps.

The two suggestion queries compare exact shared identity, relation, case, jurisdiction and status, with overlapping year bounds; quantities also share units, accounting basis and kind. They do not infer identity, convert units, count prose knowledge sets or reason about institution-foundation chronology. Conditions, narrator stance, finer dates and changes in law still require reading. These are deliberately conservative initial suggestions, not a complete contradiction engine or an accuracy score.

## Reproduce

With the core requirements installed, run `python -X utf8 outputs/aumakua-ontology-20261026/build_audit.py` to rebuild the linked records, then `python -X utf8 outputs/aumakua-ontology-20261026/run_validation.py` to execute and archive validation/views. The latter records the existing test log; run the unittest command in `execution.json` separately to repeat tests. A rebuild can change Turtle serialization bytes; regenerated execution checksums identify the new run. The maintained workflow is in [Aumakua's ontology reference](../../.agents/skills/aumakua/references/ontology-workflow.md).

Canonical prose, approvals, character identities, workbook and earlier audit artifacts remain unchanged. Successful structural validation supplies traceability and testable review boundaries; it does not approve a narrative repair or establish whole-book consistency.
