# Before and after the ontology-enabled Aegis review

26 October 2026

The ontology-enabled rerun reaches essentially the same recommendation as the [original assessment](../../docs/power-review/ontology/inputs/assessment.md): retain the 5% baseline, clarify early collection and institutional transmission, investigate a staged assay/remittance service, and distinguish explaining an existing coordination bargain from negotiating a new one. It supplies a more precise, inspectable argument. It supplies no new historical evidence, net benefit estimate or quantified increase in Julian's power.

Read the [new assessment](after/assessment.md) for the full dated chain, alternatives and claim/link IDs. The [comparison protocol](comparison-protocol.md) defines the matched sources and independence limits. Both reviews use the same [master storyline](../../book-agent/revision/master_storyline.md) at `4ea16e3a739c807a5f20bbb8ffb98450b84215c7`; the objective and substantive success criteria remain unchanged.

## What changed in the result

| Topic | Before | After | Assessment |
|---|---|---|---|
| Main recommendation | Clarify the chain, investigate collection services, pair with an accession/crisis coordination explanation | Explicitly retain baseline/5%; prioritize exposition; keep collection services and a new bargain conditional | Substantive verdict stable; conditions and intervention types are clearer |
| 1918 cutoff | Described as something the master says Julian does; its local PROPOSED label is not repeated in the transmission row | C18 retains PROPOSED; L10 separately records the missing instrument for private-issuer compliance | Better preservation of a local qualification; the old review did not approve the event, but its summary was easier to misread |
| Ownership and effective control | Correctly separates public/private assets, but the accession row uses the missing transfer into a royal purse as part of its limitation | C15/L09 ask which institutional actions Julian can reliably obtain through cooperation; no ownership transfer is required | A more appropriate test of practical power |
| Durability of the Crown–estates bargain | Questions the categorical stability of the regency bargain | Also confronts the statement that Altai breaks the arrangement in 1921, asking what supports later cooperation | A more specific transmission/breach question from an unchanged source; see new assessment's accession row and L09 |
| Institutional descendants | Tracks the Development Fund, Crown shares and private establishments broadly | Adds separate surplus claims, sector-specific equity, banking without Crown equity, and foreign gold bought into reserves | Finer control and resource boundaries, not an additional fiscal or power gain |
| Alternative E | Explaining cooperation and developing a substantive bargain share one alternative row | AC is exposition only; AD changes the world and must specify costs, assent, refusal, breach and expiry | Prevents a new power from being presented as a clarification |
| Endpoint outcomes | Identifies bounded common command and rejects GDP as automatic power | Separately compares mobilizable resources, implementation, leverage and freedom to act | Easier to see trade-offs without inventing a composite score |
| Traceability | Prose tables, source sections, dossier and calculation files | Dated Claims, MechanismLinks, EvidenceApplications, case-specific Judgments, pinned inputs and executed query views | Reusable, machine-checkable representation of the reasoning |
| Coverage | Includes two early textual consistency flags and selected 1848 workbook reconciliation | Does not revisit those two textual flags; directly replays only saved 1849–1852 arithmetic | The new pass is not a complete replacement for all earlier findings or checks |

The most useful new writing question is therefore not “how do all the estates become Julian's property?” It is which instructions the institutions will execute, why, at what cost, and how their cooperation survives breach or must be rebuilt after 1921. The 1932 renewal provides a specific command instrument within its negotiated scope and term; it does not retrospectively establish every intermediate link from early gold.

## Earlier issues carried forward

| Earlier finding | Treatment in the new pass | Continuing disposition |
|---|---|---|
| The 90% collection factor is assumed | Retained as MODEL, with unavailable historical calibration and explicit entitlement-to-receipt links | Open; do not treat the number as observed capture |
| Early assay/mint commissioning is incomplete | Retained through L02/L30/L31 and the staged-service alternative | Open; require a supported operating schedule and cost before stronger conclusions |
| First coupon/1848 debt timing is unresolved | Inherited debt note and conditional Payno analogue retained; workbook equations not independently replayed | Open; preserve the original reconciliation as earlier work, without claiming a new workbook audit |
| Secrecy head count may conflict | Not revisited in the independent rerun | Carry forward the source's five-versus-apparently-seven wording question; check the proposition and time before declaring an actual contradiction |
| Council of State appears in 1848 before its 1852 establishment | Not revisited in the independent rerun | Carry forward the body/identity/chronology question; do not silently invent a provisional institution |
| Personal-control bridge is incomplete | Refined into accession, private-issuer compliance and post-breach continuity questions | Open; retain independently held assets and specify the instrument or bargain |

This reconciliation is the parent reviewer's comparison, performed after the separate evaluator completed its assessment. The independent assessment itself is preserved. The shared skill workflow now explicitly carries omitted unresolved issues forward in repeat reviews. Its evaluated version is archived in `before/evaluated-ontology-workflow.md`; the carry-forward instruction was added after this comparison exposed the omission.

## Financial comparison

The [matched arithmetic check](financial-parity.json) independently replays the saved original JSON and passes twenty checks. The evaluator's [financial handoff](after/financial-diagnostic.md) separately documents its bounded calculation.

| Fixed-output quantity | Before | After |
|---|---:|---:|
| 1849–1852 metal output, million period USD | 237 | 237 |
| Gross royalty, 5% rate and inherited 90% collection | 10.665 | 10.665 |
| Gross royalty, 3% rate and complete collection | 7.110 | 7.110 |
| Gross room from ten percentage points more collection at 5% | 1.185 | 1.185 |
| Collection needed at 3% to match the inherited benchmark | 150% | 150% |
| Net service benefit and additional power in 1932 | Unavailable | Unmodeled with explicit reasons |

The old pass read the supplied workbook and replayed selected equations, including an 1848 receipt adjustment. The new pass deliberately uses inherited JSON and notes only; it excludes that 1848 replay. Matching the four-year totals establishes arithmetic parity within this scope, not fresh workbook validation. A collection increase is a hypothetical sensitivity, not an estimated response to the candidate service.

## Skill integration and executed checks

[Aegis](../../.agents/skills/aegis/SKILL.md) now owns the case/claim/transmission/judgment graph and reconciles it with readable prose. [Clio](../../.agents/skills/clio/SKILL.md) supplies located evidence applications with applicability limits. [Chryseis](../../.agents/skills/chryseis/SKILL.md) supplies qualified quantity records alongside reproducible calculations. The maintained finance skill is renamed to Chryseis with its prior financial references retained. Standalone research and finance keep the user's requested output format.

The installed packages match the maintained sources, and all three pass the skill-creator validator. The runner accepts custom `--data` and `--manifest` arguments and does not merge a previous pilot into a new review. Twenty behavioral tests pass, including checks for that separation, incompatible status schemes, case leakage, unknown versus zero/false, and unsupported unconditional power improvements.

The [new graph](after/review.ttl) conforms to SHACL and verifies eleven local inputs. Its 45 Claims, 21 MechanismLinks, 37 EvidenceApplications, six cases and seven judgments are descriptive counts, not a quality score. All five [query views](after/validation.json) execute and retain eight unresolved links. The original pilot still validates separately.

The forward test found one operational issue: Windows cp1252 stdout could not print Hawaiian names in full JSON. Using `python -X utf8` fixed execution; the skill workflow and examples now state that invocation. No ontology-schema change was needed. `after/run_review.py` reproduces calculation, graph construction and validation. Its manifest records the separate evaluator's actual skill/profile versions; the later carry-forward instruction is documented above rather than attributed to that initial pass.

## What this comparison supports

The observed benefit is a more explicit and reusable account of authority, ownership, cooperation, conditions and evidence. The stable main verdict and unchanged financial results are appropriate: adding an ontology should not manufacture evidence or strengthen Julian's position in the story.

Coverage remains a separate editorial responsibility. The two omitted textual flags show why successful graph validation cannot establish that the entire story was checked. This one tailored case, with different review passes and revised instructions, cannot isolate the ontology's causal effect or establish general performance. Preserve both assessments, use the new records to guide targeted writing/research, and retain the carried-forward issue list.
