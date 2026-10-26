# Compact Pacifica review ontology

Version 0.1.0 · 26 October 2026

This profile makes a bounded power review inspectable across claims, evidence, institutions and time. It represents the gold-to-revenue assessment as qualified records. It does not approve story changes, establish new historical facts, or calculate Julian's power. The [master storyline](../../../book-agent/revision/master_storyline.md) and approval register retain their authority.

## Files and execution

| File | Purpose |
|---|---|
| `ontology.ttl` | Six core record families, supporting source records and relationship meanings |
| `vocabularies.ttl` | Separate SKOS schemes for authority, support, values, outcomes and other bounded vocabularies |
| `shapes.ttl` | SHACL Core and SHACL-SPARQL constraints |
| `gold-review.ttl` | Maintained pilot records: three principal transitions, their gaps and alternatives A–E |
| `queries.rq` | Five named SELECT queries for unresolved links, control, dependencies, quantities and evidence |
| `inputs/` | Three original pilot documents and a checksum manifest |
| `validate.py`, `test_ontology.py` | Offline integrity, validation, queries and behavioral counterexamples |
| `consistency/`, `test_consistency.py` | Additive Aumakua findings, passage/claim coverage, quotation checks and conservative comparison suggestions |

From the repository root, using Python 3.12:

```sh
python -m venv .venv-review
# Activate the environment using the command appropriate to your shell.
python -m pip install -r docs/power-review/ontology/requirements.txt
python -X utf8 docs/power-review/ontology/validate.py
python -X utf8 docs/power-review/ontology/validate.py --json
python -X utf8 docs/power-review/ontology/validate.py --data outputs/REVIEW/review.ttl --manifest outputs/REVIEW/input-manifest.json --repository . --json
python -X utf8 -m unittest discover -s docs/power-review/ontology -p 'test_*.py' -v
```

Dependencies are needed at installation. Validation and queries subsequently use local files only. No remote ontology imports, rule expansion, database service or RDF 1.2 features are used. Turtle files are the maintained review representation; JSON query output is generated. The query file uses `# query: NAME` separators; each block is an independently executable SPARQL SELECT query.

The custom-data command is an example for a review you have authored. Each `--data` file replaces the default pilot; repeat the option to assemble contributions. An explicit custom graph requires its own `--manifest`. Schema and vocabulary are shared; earlier pilot conclusions are not silently merged into a new assessment. The UTF-8 switch keeps Hawaiian names and source text serializable in Windows pipelines.

## Record meanings

| Core family | Meaning |
|---|---|
| Entity | A distinct person, office, institution, collective, resource, instrument or jurisdiction |
| Claim | One proposition with bound participants, target period, case, jurisdiction, authorial qualification and provenance |
| EvidenceApplication | One located passage applied to one claim or link, including its applicability boundary |
| MechanismLink | A typed explanatory relationship, its support, prerequisites, refusal conditions and burdens |
| ComparisonCase | A pinned baseline or explicit exposition/world-change alternative |
| Judgment | A comparison with a named outcome dimension, verdict, sensitivity and material dependencies |

QuantityClaim specializes Claim. SourceDocument and SourcePassage support provenance. Namespace IRIs use `urn:pacifica:ontology:review:`, `urn:pacifica:vocab:review:` and `urn:pacifica:review:gold-20261026:`. They do not require an online resolver. Characters reuse `urn:pacifica:character:CT-…` and the existing registry IDs; an Entity is not a SKOS concept.

The separately loaded [consistency profile](consistency/README.md) adds Aumakua audit, finding and coverage records under `urn:pacifica:ontology:consistency:` and `urn:pacifica:vocab:consistency:`. It reuses these source/claim identities without changing their meanings or forcing textual issues into power Claims. Its validator requires explicit audit data and an input manifest; the core validator alone does not validate the extension.

`pc:subject`, `pc:predicate` and `pc:object` describe a proposition; they do not assert the embedded world triple. A known relational assertion additionally supplies `pc:truthValue true` or `false`. An unknown relation may retain its bound object but has a reason and no truth value. A QuantityClaim instead supplies a decimal value, or a missingness state and reason. Zero, false, unknown, disputed, unmodeled, not applicable and explicitly absent remain distinct.

Authorial status, claim basis, narrative explanation, historical applicability, quantitative basis and verdict basis have separate schemes. `Known` means a supplied value within the stated claim basis; a known value in a proposed narrative does not become approved canon. `Unspecified` retains a passage without assigning an approval status from its lack of a local tag. Approval still depends on the source's actual scope and the approval register. A value in one scheme cannot replace a value from another.

`owns`, `hasClaimOn`, `holdsOffice`, `hasAuthorityOver`, `canMobilize`, `cooperatesWith` and `commands` have different meanings. None implies another. A royalty entitlement does not establish collection; an office does not establish compliance; dependable cooperation need not transfer asset ownership. The review relations `enables`, `requires`, `preserves`, `transmits`, `constrains` and `precedes` are not declared transitive. A century-long path does not quantify the marginal effect of its earliest node.

Control claims identify the institutional capacity through which the actor acts, the control instrument or its specific unresolved gap, conditions, refusal, expiry and burdens. Explicitly unresolved text is allowed: the ontology records research gaps instead of filling them. Period labels retain source precision; integer start/end years are inclusive coverage bounds, not exact commencement or legal expiry dates. A seasonal event is not silently assigned a day.

PROV-O records document derivation and the extraction activity. Evidence support/challenge/analogy and fictional causal mechanisms use the Pacifica vocabulary. `prov:wasDerivedFrom` does not mean that a source proves a claim or that one story event caused another.

## What the pilot demonstrates

The dataset follows gold entitlement to receipts and establishments, accession to dependable estate cooperation and the proposed 1918 cutoff, and rescue finance to the 1932 command arrangement. It represents 17 claims, six mechanism links, seven evidence applications, six cases and five judgments. It is a bounded manual extraction, not a complete conversion of the story or an automated historical audit.

- The 90% collection factor remains a MODEL assumption. The dossier supplies no historical percentage.
- Mint sources are analogies to settlement and commissioning. Their access is reported by the prior dossier; this package does not claim to have retrieved them anew. The Smithsonian lead remains unretrieved.
- The 1918 private-issue cutoff retains its local PROPOSED qualification. Its compliance instrument remains a gap.
- Estate capacity, Crown office and private claims remain distinct. The regency Crown's lack of its own purse is a known negative statement; it is not evidence that later cooperation is impossible.
- The 1932 common command has a 1937 renewal boundary and excludes the home army outside a Concord war. It does not become ownership of all Japanese resources.
- Exposition-only improvements B and E1 are separate from world-change candidates C, D and E2. The new bargain's terms and effects remain unassessed.
- Reported conditional fiscal results remain distinct from net benefits and endpoint power. No new workbook recalculation or calibrated power estimate is claimed.

Expected query row counts are 4 unresolved links, 4 control boundaries, 14 provisional dependency rows, 5 quantity records and 7 evidence applications. Dependency rows describe declared links, not independent pieces of evidence.

## Source integrity and revision

Baseline commit: `4ea16e3a739c807a5f20bbb8ffb98450b84215c7`. `inputs/manifest.json` pins the master, character registry, approval register and the three bundled original pilot documents. Bundled originals preserve exact bytes through `.gitattributes`; their original relative links refer to the pilot's old layout. Use the RDF document paths and this README to navigate this package.

Checksums of repository source text normalize CRLF to LF so the same pinned revision validates on Windows and Linux. Bundled inputs use exact-byte checksums. Both the hash and its basis must agree between the RDF and manifest. Source files are read only. A changed source causes a stale-input error; refresh the review as an explicit new revision, review affected claims and update both representations. Do not merely replace the hash to hide a changed premise. CI watches the pinned repository inputs as well as this package.

SHACL checks required structure, scheme membership, case consistency, quantitative metadata and several prohibited promotions. An unconditional world-power improvement cannot depend on a declared proposed/open premise, unknown result, unresolved narrative link or missing control instrument. Exposition-only cases cannot establish world-power improvements. The validator cannot establish historical truth, complete a missing dependency list, prove actor compliance, identify every contradiction, or certify causal sufficiency.

## Relationship to Timeline Lab and the skills

This is a review profile aligned with the [Timeline Lab semantic contract](../../timeline-lab/ontology.md), not a replacement for the Lab's full state or an extension to its executable prototype.

| Review concept | Corresponding Lab meaning |
|---|---|
| Entity | Entity and existing character identity references |
| Claim | Grounded Proposition plus a qualified Assertion; never automatically a WorldFact |
| EvidenceApplication and source records | Provenance and scoped support links |
| MechanismLink | ExplanationLink; not automatically an executable MechanismContract |
| ComparisonCase | Pinned comparison/intervention description, without a generated run |
| Judgment | Author-visible assessment with explicit claim basis |

No runtime adapter or Pydantic model change is implemented. Runtime state and maintained review assertions retain different roles. The updated Aegis, Clio and Chryseis skills use the shared [ontology workflow](../../../.agents/skills/aegis/references/ontology-workflow.md). Clio supplies bounded evidence applications, Aegis owns the transmission argument and comparison judgments, and Chryseis supplies qualified quantities. Full Aegis reviews save and validate their own graph, manifest and query output; scoped standalone research and finance retain the requested output format. The original assessment and pilot dataset remain preserved for comparison.

Standards: [RDF 1.1 Turtle](https://www.w3.org/TR/turtle/), [SKOS](https://www.w3.org/TR/skos-reference/), [PROV-O](https://www.w3.org/TR/prov-o/), [SHACL](https://www.w3.org/TR/shacl/). Implementation: [RDFLib](https://rdflib.readthedocs.io/en/stable/) and [pySHACL](https://github.com/RDFLib/pySHACL).
