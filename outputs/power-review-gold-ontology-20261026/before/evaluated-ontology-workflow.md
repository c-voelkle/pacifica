# Shared ontology workflow for Pacifica reviews

Use this reference for a full Aegis review and for Clio/Chryseis contributions to one. It describes the handoff; the repository's compact profile owns the schema and vocabulary definitions.

## Locate and pin

Find the intended Pacifica checkout, following its AGENTS.md and source authority. The maintained profile is `docs/power-review/ontology/`. Read its README, `ontology.ttl`, `vocabularies.ttl` and relevant `shapes.ttl` constraints. Reuse `queries.rq` and `validate.py`; do not load the old `gold-review.ttl` as the new assessment or treat a previous judgment as a source fact. A prior graph may be reused only as an explicitly pinned, re-examined earlier review.

Pin the narrative/approval/identity/financial baseline independently from the skill and ontology revisions. Record skill/profile hashes and version, source locators, material coverage and exclusions. Existing character IDs use `urn:pacifica:character:CT-…`; other entities need stable, distinct review IDs. Do not merge offices, institutions or differently dated bodies by name.

If no profile is available, locate the maintained repository copy before creating another schema. If it cannot be accessed, continue the supported prose/qualified-record work and state that integration is unavailable; do not claim RDF validation. An unavailable dependency does not authorize installing tools or changing other projects outside the user's scope.

## Material records and ownership

| Owner | Records and meaning |
|---|---|
| Aegis | ComparisonCases, material Claims, MechanismLinks and Judgments; assembles contributions and owns the transmission argument |
| Clio | SourceDocument/SourcePassage records and EvidenceApplications targeting the supplied IDs; distinct supporting, conflicting, analogous and unavailable historical evidence |
| Chryseis | QuantityClaims and located calculation provenance, consistent with the financial package's cases, units, ownership and missing results |

Create only records that can affect a recommendation, a control boundary or an unresolved dependency. A full review normally saves `<review>/review.ttl` and `<review>/input-manifest.json`; contributions may be separate Turtle fragments. Reuse the repository profile instead of copying it into each output or installed skill. Prose remains the principal assessment; cite material claim/link IDs where they make the reasoning checkable.

Use the profile's existing predicates and separate SKOS schemes. Entitlement, ownership, office, legal authority, mobilization, cooperation and practical command are different relations. Control claims identify the actor, represented office/institution, action/resource, jurisdiction, period, instrument or instrument gap, conditions, refusal, expiry and burdens. Show dependable cooperation where supported without requiring a transfer into a personal purse.

Keep authorial qualification, claim basis, narrative explanation, historical applicability, quantitative origin and verdict basis separate. A locally PROPOSED event remains proposed even inside the authored baseline. Unlabelled wording is not automatically approved. A negative relational fact may have `truthValue false`; unknown and unmodeled values have typed states and reasons, not zero or fabricated truth. Preserve approximate dates rather than assigning exact timestamps.

EvidenceApplications name a precise target and applicability boundary. PROV-O derivation records where a record came from; it does not say that a passage proves a mechanism. Record known source dependence and preserve conflicting explanations. Reusing a dossier preserves its original retrieval status; access reported by that dossier is not a new retrieval by the current reviewer.

MechanismLinks distinguish temporal order, enabling conditions, necessary prerequisites, preservation, transmission and constraints. Do not infer causation, necessity or a numerical power share from graph reachability. Judgments identify a baseline, alternative, outcome dimension, material dependencies and sensitivities. Exposition-only changes and substantive world changes require separate cases. Reassess affected downstream assumptions when the world changes.

## Execute and inspect

Use the supported Python runtime with the profile's declared dependencies. Invoke it with `-X utf8` so names and source text remain serializable in Windows pipelines. For a custom review, pass its own Turtle and manifest explicitly; multiple `--data` arguments assemble fragments:

```sh
python -X utf8 docs/power-review/ontology/validate.py \
  --data outputs/REVIEW/review.ttl \
  --manifest outputs/REVIEW/input-manifest.json \
  --repository . --json
```

The manifest's `files` maps repository-relative source paths to `sha256` and `hash_basis` (`ExactBytes` or `LFNormalizedText`); retain the baseline commit and source origin. Each `LocalPinned` SourceDocument must match a manifest entry. Pin calculation code and relevant sources without editing them. Use source and dossier locators for unavailable remote evidence, without inventing local bytes or claiming retrieval.

Save the executed output and inspect all five query views: unresolved links, control boundaries, provisional dependencies, quantities/gaps and evidence boundaries. Correct structural failures and accidental promotions in the graph, then reconcile the assessment's material statements and recommendation with those records. A missing mechanism is a finding to retain, not a blank to complete for conformance. Validation success does not prove historical truth, complete coverage, consent, causal sufficiency or general improvement of the skill.

For a before/after comparison, preserve the old assessment and pin a matched narrative, source set and numerical scope. Declare new evidence or changed calculations separately. Compare actual conclusions, qualified control, unresolved dependencies and reproducibility. An analyst comparison on one tailored case is not a controlled benchmark; do not invent scores or claim independent testing without a separate evaluator.
