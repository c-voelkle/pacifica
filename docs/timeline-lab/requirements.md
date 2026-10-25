# Pacifica Timeline Lab requirements

**Draft for review · 25 October 2026 · Requirements version 0.5**

Timeline Lab is a fast strategic wargame and policy-search tool for developing the Pacifica plot. The author sketches an idea and sees the spread of generated histories within seconds; when the idea deserves rigour, the Lab searches for strong and distinct adaptive Pacifica strategies and compares distributions of several success variables. The author controls Pacifica; other actors respond through their own objectives, information and constraints.

The [product vision](product-vision.md) defines this end goal, the researched measurement framework and the intended user experience. The six authored timelines are financial regression references and comparators, not the space of possible outcomes.

Strategy discovery, multiple objectives, independent other actors and Excel-free execution remain confirmed goals. Revision 0.5 incorporates the review of the supplied revision 0.4: a narrower R0 with early credibility checks, explicit fidelity/policy reassessment, per-cell Pareto archives, separate response and hostile stress analysis, adaptive sampling and synchronized release dependencies. Exact risk limits, metrics, actor mechanisms and pilot boundaries remain to select.

## 1. Product purpose and users

The primary user is the Pacifica author, who needs to sketch a decision, inspect generated histories, discover distinct conditional strategies and understand their trade-offs and failures. The model maintainer defines supported mechanisms and evidence; the finance skill proposes quantities and derivations.

Two loops serve that workflow:

- **Sketch:** evaluate a supported author policy without search, progressively compare outcome fans under matched external worlds, inspect paths and save a named version.
- **Campaign:** define objectives/constraints/descriptors, search policies, inspect global and within-cell trade-offs, test responses and hostile stresses, assess fresh futures and inspect history types.

R0 provides one bounded financing/commitment question with indispensable actor roles, actual resource/timing limits, basic provenance and offline structured summaries. It is a foundation release. R1 delivers the discovery goal. Full financial fixture parity, instrument-level inspection and detailed policy reassessment follow in R2.

Monte Carlo evaluates outcomes; optimization searches policies; diversity describes behavior. None may choose lucky random seeds or prescribe other actors' consent. Generated histories and optional narration remain drafts, with calculation separate from canon approval.

## 2. Evidence and current state

The baseline is pinned to repository main commit `cc6e017780970433ab63bc95d0e3749510b44d49`. The alternatives are pinned separately to `626ffbb0bd6486c19164f89104569d78321ebd55`. The proposal file `CR-032.md` supplies the case labelled A; B, C and D remain separate alternatives. See the [pinned proposal index](https://github.com/c-voelkle/pacifica/blob/626ffbb0bd6486c19164f89104569d78321ebd55/book-agent/revision/alternatives/CR-032/README.md).

The existing [Ledger reference](https://github.com/c-voelkle/pacifica/blob/cc6e017780970433ab63bc95d0e3749510b44d49/finance/Pacifica-Ledger.md) describes a CR-021 rev8 display snapshot. It supplies useful dashboard domains, but its numbers are not the current experiment baseline. Its live interface was not inspected for this specification.

Six local JSON bundles contain 87 annual periods, 1846–1932, and 73 annual metrics. They total 25,473,049 bytes and contain 17 labelled run records with 14 distinct input hashes. Baseline, control and A each reuse their native input for the matched-downturn label; these are not additional independent calculations.

| Pilot case | First model divergence from baseline | Branch divergence from control | Run records |
|---|---:|---:|---:|
| Baseline master-storyline model | — | — | 2 |
| Shared-change control | 1904 | — | 2 |
| A: war and coalition victory | 1904 | 1918 | 2 |
| B: negotiated 1917 peace | 1904 | 1916 | 2 |
| C: prewar diplomacy, conditional C0 continuation | 1904 | 1907 | 2 |
| D: completed no-general-war proposal | 1904 | 1907 | 7 |

The dates above are financial-model divergence metadata, not assertions that every narrative consequence begins in that year. The control isolates the common changes before comparing the alternatives.

The pilot used native Excel full recalculation. Its baseline evidence includes a 48,940-cell reconciliation, and the exported checks cover accounting, dated divergence and financing constraints. These checks establish consistency with the pinned model; they do not establish historical truth. Alternative GDP paths still depend on declared MODEL assumptions.

The current adapter contains CR-specific logic. There is no implemented Timeline Lab importer, authoring interface or portable world engine. The [finance skill](https://github.com/c-voelkle/pacifica/blob/507c56b68621a3447e07e70338aa10d4a9e54a48/.agents/skills/pacifica-scenario-finance/SKILL.md) is separately proposed in [draft PR 7](https://github.com/c-voelkle/pacifica/pull/7).

[fixture-manifest.json](fixture-manifest.json) records exact file hashes, sizes, variants and selected 1932 values. The six result files and supporting adapter scripts are local project outputs and are **not included in this requirements commit**. Their exact bytes must be staged in versioned project storage before ledger regression work (R2) begins. Pin read-only baseline calibration and independent small reference evidence earlier for M0/R0; fitting a baseline does not test changed-input responses.

## 3. Release tiers

| Release | Purpose | Required evidence |
|---|---|---|
| R0 bounded sketchpad | One agreed financing/commitment question, a few indispensable actor roles and supported effects | Native fast accounts, independent baseline/changed-input checks, refusal/counteroffer, material monthly timing, ownership/coverage/basic tracing, progressive fans, saved versions, recovery and offline structured timelines/template summaries |
| R1 strategy discovery | Search and assess distinct adaptive policies | Global frontier and within-cell Pareto sets, budgeted adaptive sampling, own-interest responses plus separate hostile stress, fresh assessment, history types, general editing, useful structural generation and optional bounded LLM narration |
| R2 detailed fidelity and evidence | Full instruments and financial equivalence | Forensic path checking, separate policy re-evaluation, six-fixture parity, finance-skill derivations, full tracing and impact previews |
| R3 expansion | Wider supported questions and collaboration | New actors/regions/mechanisms and rebases pass their own checks; hosted mode receives a separate design |

A requirement's release is its **first required obligation**. Later `phase_gates` in backlog.json add explicit Must criteria at their own release; moving a detailed UI later does not defer basic integrity. Counts describe contracts rather than estimates of development effort.

The R0 question is proposed as a Japan financing/commitment decision, with terms/timing, acceptance/refusal/counteroffer, actual funding/draws and supported readiness effects. M0 agrees actors, observations, external conditions and evidence. A shorter actual slice within 1904–1932 is allowed when declared; it cannot claim all theatres, global diplomacy or unsupported welfare/human-cost outcomes.

| Capability | R0 foundation | Later extension |
|---|---|---|
| Controls | Narrow supported levers and uncertainty sets | General catalog editor in R1 |
| Accounts | Owned cash/debt/claims, actual resource constraints and material finer timing | Full instrument ledger and fixture schedules in R2 |
| Evidence | Definition, source/assumption IDs, basic module trace, coverage and independent reference cases | Deep derivations/formulas and full provenance UI in R2 |
| Actor agency | Competent authority, independent acceptance/refusal/counteroffers | Response search, hostile stress and alternative structural assessment in R1 |
| Replay | Recorded events and deterministic template summary | History types/optional LLM narration in R1; detailed checking/re-evaluation in R2 |
| Data contracts | Minimal typed schemas, versions and explicit runtime bindings | Structural generators/form scaffolds where useful in R1 |

R0 does not require a universal ontology generator, general-purpose editor or LLM provider. Its claims remain bounded by coverage; a six-case viewer alone cannot satisfy R1. Original attachments remain immutable and every calculation is native from R0.

## 4. Domain model and ontology

Shared typed declarations define supported world, mechanism, experiment and provenance structures. R0 uses minimal machine-validated schemas and explicit runtime bindings. R1 may generate structural schemas, result types, form scaffolds and layout metadata. A declaration alone cannot supply behavior, initialization, legal procedure, migration or interface design.

| Layer | Contents |
|---|---|
| World | Entities, territories, populations, capacity, instruments, rights, forces, routes and relations |
| Mechanism | Actions/events, actor models, observation rules, transitions, constraints, metrics and modules |
| Experiment | Sketches, objective/descriptor sets, policies, campaigns, rollouts, assessments and history types |
| Provenance | Sources, hashes, calibration/reference evidence, engine/environment versions and narration claims |

| Object | Required distinction |
|---|---|
| Source snapshot | Pinned original bytes, authority/evidence status and retained asset location |
| Entity and geography | Sovereign, Treasury, private firm, lender, borrower or territory with dated ownership/jurisdiction; practical access is separate |
| Dated overlay | Stable target and effective periods with declared supported set/add/remove/shift/replace effects |
| Instrument/right | Parties, terms, dates, cash flows, authority, obligations and termination |
| Assumption proposal | Units, evidence, derivation, bounds, effective date and uncertainty; unknown differs from zero |
| Saved version | Pinned parent, Git commit, resolved-content hash and immutable referenced definitions |
| Sketch | Versioned world plus supported levers, uncertainty/world design and evaluation budget, without optimization |
| Campaign | Question, objective/constraint/descriptor set, policy space, actor models, search and sampling budgets |
| Policy/actor model | Observation-limited rules and explicit preferences/resources; Pacifica cannot choose other actors' actions |
| Descriptor | Registered aggregate of behavior over a common world design, with never/undefined cases, sample uncertainty and cell-instability treatment |
| Runtime layout | Versioned dimensions, indices, activation masks, initialization and update ownership; overflow cannot truncate silently |
| Rollout | Policy/world/draw identity, observations, actions, events, checks, outcomes and execution status |
| Assessment | Evidence scope, aggregate distributions, global/per-cell trade-offs, response/stress sensitivity and fresh-world status |
| Detailed mode | Forensic check of a recorded history, or policy re-evaluation with a new linked trajectory |
| History type | Registered cluster/features, tested share, distinguishing associations and actual representative; rare/terminal paths retained |
| Narration claim | Typed statement with event/quantity/motive/causal support references and bounded verification status |

Economic and response rules live in versioned modules; no runtime LLM or data-stored formula string supplies missing mathematics. Source/assumption IDs remain present from R0 even when the full inspector is deferred.

## 5. Financial and temporal semantics

Every metric identifies entity, geography, units/currency, nominal/real basis, period, quantity kind and aggregation. Core, crown, common, private and foreign resources remain separate. Partner output is not sovereign GDP; a loan/concession does not transfer all revenue or jurisdiction.

Classify principal, repayments, interest, expenditure, asset purchases, losses and financing separately. A creditor write-down does not by itself extinguish the borrower's legal obligation. Avoided expenditure is not extra GDP; private syndicate claims are not Treasury property.

**Timing applies from R0.** Annual reporting sums flows and selects stock endpoints. Resolve months or event dates when a rollover, draw, supply interruption or payment changes available actions. A positive annual balance cannot certify liquidity. A deliberately coarser experiment states the risk it omits.

**Validation has distinct meanings.** Fast arithmetic checks use declared per-module tolerances. Baseline calibration has pinned series/bands. Independent changed-input examples test specific behavior and feasibility. Assessed fast-to-detailed discrepancies use their own projection/error rules. A changed acceptance, feasible action or terminal-loss state is material even inside an aggregate calibration band.

Both fidelity levels share mechanism definitions with explicit aggregation and instrument implementations. M0/R0 checks accepted/refused/counteroffered credit, changed rates/maturities/dates, failed rollover and an interim shortage against independently derived reference calculations. A baseline fit cannot establish off-baseline correctness.

**Detailed R2 assessment has two modes.** Forensic checking preserves recorded actions/events, finds discrepancies and identifies the first impossible commitment without forcing it to execute. Policy re-evaluation runs the same conditional policy and exogenous-world design against detailed states; observations, actor responses and subsequent choices may change. It creates a new linked history and cannot silently overwrite fast results.

C's C0 continuation, D's unresolved denominators and other fixture conditions remain explicit. Never substitute D's institutions into C or core GDP for North American GDP. Report or bound post-horizon debt, guarantees, maintenance, restoration and treaty duties. Defeat/default remain outcomes; computational errors remain separately counted unknowns rather than arbitrary utility penalties.

The interface keeps narrative authority, evidence, execution, accounting, funding, coverage and fidelity separate from the first sketch.

## 6. Dashboard and authoring workflow

**Sketch:** select the bounded world → edit a supported lever → stream current-identity fans against a matched reference → inspect a path and its deterministic summary → save explicitly or seed a campaign.

**Campaign:** define objectives/constraints/descriptors → search → inspect global and within-cell trade-offs → allocate extra samples → analyze own-interest responses and separate hostile stresses → freeze candidates/models → assess fresh worlds → inspect histories and export.

| View | Purpose | Release |
|---|---|---|
| Sketch | Narrow levers, matched reference, progressive counts/bands and coverage/fidelity states | R0 |
| Timeline | Recorded observations, Pacifica decisions, independent responses, chance and offline template summary | R0 |
| Basic quantity inspector | Definition, version, module, source/assumption IDs and coverage | R0 |
| Problem/general editor | Objective/constraint/descriptor sets and broader supported catalog editing | R1 |
| Search | Budgets, sampling precision, actual counts, checkpoints and errors | R1 |
| Trade-offs/strategy map | Global frontier and within-cell Pareto representatives, descriptor uncertainty and assessment status | R1 |
| Policy/response | Triggers, bottlenecks, own-interest replies, separately labelled hostile stress and failure sensitivity | R1 |
| History types/narration | Empirical types and representatives; optional typed-claim-based prose | R1 |
| Detailed accounts/evidence | Full schedules, forensic checks, policy re-evaluation, derivations and impact previews | R2 |

A changed input invalidates current-view identity immediately. Superseded work cannot update a newer sketch. Explicit saves use guarded version writes; durable artifacts/manifests precede catalog registration. Interrupted work, orphan files and stale tabs recover without replacing the last complete version.

Charts and tables share selections, units and statuses. Comparisons require compatible definitions and matched exogenous worlds where appropriate; endogenous events recompute. Basic structured replay works offline. LLM narration is later and optional; matching numbers/IDs cannot certify invented motives or causal claims.

## 7. Requirements and acceptance register

The synchronized register contains **67 requirements: 65 Must and 2 Should**. First obligations are **38 in R0, 21 in R1, 6 in R2 and 2 in R3**, with **10 explicit later phase gates**. A criterion is not satisfied by writing this specification.

[backlog.json](backlog.json), revision 0.5, is the machine-readable authority for the full Given/When/Then criteria, source references, prerequisites and phase gates. This register and the statements below mirror it. There is no temporary precedence over an older backlog. A mismatch, unresolved reference, dependency cycle or prerequisite in a later release blocks the documentation gate.

### 7.1 Register

| Requirement | Capability | Priority | First obligation | Later gates |
|---|---|---|---|---|
| TL-001 | Pin every experiment | Must | R0 | — |
| TL-002 | Import the six bundles | Must | R2 | — |
| TL-003 | Define quantities explicitly | Must | R0 | — |
| TL-004 | Separate approval from calculation | Must | R0 | — |
| TL-005 | Fork without changing history | Must | R0 | — |
| TL-006 | Use dated semantic changes | Must | R0 | — |
| TL-007 | Track dependencies | Must | R2 | — |
| TL-008 | Review rebases and conflicts | Should | R3 | — |
| TL-009 | Handle unresolved continuations | Must | R2 | — |
| TL-010 | Integrate the finance skill | Must | R2 | — |
| TL-011 | Make runs reproducible | Must | R0 | — |
| TL-012 | Respect time and detect cycles | Must | R0 | — |
| TL-013 | Control calculation jobs | Must | R1 | — |
| TL-014 | Show fresh results accurately | Must | R0 | — |
| TL-015 | Reconcile the accounts | Must | R0 | R2 |
| TL-016 | Expose resource constraints | Must | R0 | — |
| TL-017 | Preserve ownership and geography | Must | R0 | — |
| TL-018 | Aggregate time correctly | Must | R0 | — |
| TL-019 | Compare like with like | Must | R0 | R2 |
| TL-020 | Run bounded sensitivities | Must | R1 | — |
| TL-021 | Explain differences honestly | Must | R1 | R2 |
| TL-022 | Compare the main trajectories | Must | R0 | — |
| TL-023 | Inspect the timeline | Must | R0 | — |
| TL-024 | Edit decisions and model assumptions | Must | R1 | — |
| TL-025 | Trace any displayed number | Must | R0 | R2 |
| TL-026 | Export a reproducible experiment | Must | R1 | — |
| TL-027 | Protect sources and validate execution inputs | Must | R0 | R2 |
| TL-028 | Validate the native engine against frozen evidence | Must | R2 | — |
| TL-029 | Keep the initial lab private | Must | R0 | — |
| TL-030 | Meet measured responsiveness targets | Must | R0 | — |
| TL-031 | Make comparisons readable and accessible | Must | R1 | — |
| TL-032 | Recover without corrupting work | Must | R0 | R1 |
| TL-033 | Register models and capabilities | Must | R0 | — |
| TL-034 | Extend the world state | Should | R3 | — |
| TL-035 | Evaluate policy limits with valid denominators | Must | R1 | — |
| TL-036 | Version the data contract | Must | R0 | R1, R2 |
| TL-037 | Run without Excel | Must | R0 | — |
| TL-038 | Version the world catalog as validated text | Must | R0 | — |
| TL-039 | Separate calculation from persistence and presentation | Must | R0 | — |
| TL-040 | Separate accounting identities from economic assumptions | Must | R0 | — |
| TL-041 | Define success before search | Must | R1 | — |
| TL-042 | Generate legal decisions from an action catalog | Must | R0 | — |
| TL-043 | Search adaptive policies without future knowledge | Must | R0 | — |
| TL-044 | Represent independently responding actors | Must | R0 | — |
| TL-045 | Model strategic capability and sustainment | Must | R0 | — |
| TL-046 | Represent uncertainty explicitly | Must | R0 | — |
| TL-047 | Evaluate policies across repeated generated futures | Must | R0 | — |
| TL-048 | Search a set of multiobjective strategies | Must | R1 | — |
| TL-049 | Test finalists on unseen futures and actor models | Must | R1 | — |
| TL-050 | Explain strategic strengths and failures | Must | R1 | — |
| TL-051 | Run large campaigns within a declared budget | Must | R1 | — |
| TL-052 | Explore outcome distributions and trade-offs | Must | R1 | — |
| TL-053 | Establish model credibility for its intended use | Must | R0 | R1, R2 |
| TL-054 | Replay and export a discovered strategy | Must | R1 | — |
| TL-055 | Score distributions without hiding their assumptions | Must | R1 | — |
| TL-056 | Demonstrate discovery without prewritten outcomes | Must | R1 | — |
| TL-057 | Gate metrics on usable evidence and coverage | Must | R0 | — |
| TL-058 | Sketch interactively | Must | R0 | — |
| TL-059 | Simulate on an explicit compiled layout | Must | R0 | — |
| TL-060 | Validate the fast model on baseline and changed cases | Must | R0 | — |
| TL-061 | Check paths and re-evaluate policies with the detailed ledger | Must | R2 | — |
| TL-062 | Map diverse strategies without forced scalar quality | Must | R1 | — |
| TL-063 | Separate own-interest responses from hostile stress tests | Must | R1 | — |
| TL-064 | Group histories into inspectable types | Must | R1 | — |
| TL-065 | Narrate recorded facts with bounded claims | Must | R1 | — |
| TL-066 | Generate structural schemas with explicit runtime bindings | Must | R1 | — |
| TL-067 | Store batched results with recoverable manifests | Must | R0 | — |

### 7.2 Requirement statements

**TL-001 Pin every experiment.** Each saved sketch, campaign and result shall pin its source/model inputs, Git commit, resolved-content hash, actor/policy/uncertainty versions and execution environment; later edits shall not change an old run.

**TL-002 Import the six bundles.** The importer shall ingest pacifica.timeline-lab.scenario.v0.1 losslessly through a versioned adapter, preserving original bytes, run labels, unknown fields and provenance.

**TL-003 Define quantities explicitly.** Every plotted or calculated metric shall declare entity, geography, units, currency where applicable, price basis, temporal resolution, quantity kind (stock, flow, rate, ratio or index), aggregation rule and missing-value semantics.

**TL-004 Separate approval from calculation.** The interface shall distinguish narrative authority, evidence quality, execution state, accounting validation, funding feasibility, coverage and engine fidelity from R0.

**TL-005 Fork without changing history.** A user shall fork any scenario version, edit a draft and save a new immutable version with parentage and a semantic change summary.

**TL-006 Use dated semantic changes.** Changes shall target stable event, entity, parameter or instrument IDs with explicit effective periods and set, add, remove, shift or replace operations; unsupported operations shall be identified before running.

**TL-007 Track dependencies.** The system shall identify downstream schedules, claims, receipts, rights and outputs affected by a change and invalidate dependent results.

**TL-008 Review rebases and conflicts.** Changing a parent version or combining overlays shall require explicit resolution of conflicting targets and dependent assumptions.

**TL-009 Handle unresolved continuations.** The system shall distinguish unestimated quantities from unresolved political branches and support named conditional continuations.

**TL-010 Integrate the finance skill.** The finance skill shall produce versioned quantity proposals containing units, dates, counterparties, source evidence, derivations, bounds and dependencies for application to a scenario draft.

**TL-011 Make runs reproducible.** Run identity and caching shall pin resolved inputs, layout/mapping versions, policies, actor models, environment and dependency builds, uncertainty and indexed random-draw allocation; reproducibility guarantees shall state their supported environment.

**TL-012 Respect time and detect cycles.** The engine shall evaluate dated dependencies in order and reject unconfigured same-period cycles; any iterative solver shall declare convergence criteria and failure behavior.

**TL-013 Control calculation jobs.** Jobs shall have queued, running, succeeded, failed and cancelled states, bounded execution, progress updates and cancellation that protects user files and applications.

**TL-014 Show fresh results accurately.** Each view shall distinguish imported snapshots, newly calculated outputs, stale results, partial coverage and reused identical runs.

**TL-015 Reconcile the accounts.** Every engine shall reconcile the identities it supports each step using declared per-module numeric tolerances; aggregate fast accounts, independent reference calculations and full ledger postings shall have distinct validation scopes.

**TL-016 Expose resource constraints.** For every supported module, declared funding, FX, capital, personnel and transport constraints shall produce dated gaps and explicit responses; unsupported constraint dimensions shall be marked unmodelled, and residual borrowing shall not establish feasibility.

**TL-017 Preserve ownership and geography.** The model shall distinguish sovereign, private and foreign ownership, domestic value added, partner output, legal jurisdiction and time-limited rights.

**TL-018 Aggregate time correctly.** Annual views shall sum flows, use declared stock endpoints and compatible ratio components, while the fast model retains subannual timing whenever it can change liquidity, action feasibility or a material outcome.

**TL-019 Compare like with like.** Experiments shall support baseline, control, authored and generated-policy comparisons with matched exogenous uncertainty and compatible objective definitions, while allowing endogenous outcomes and other actors' decisions to change.

**TL-020 Run bounded sensitivities.** The lab shall support named downside cases, finite parameter sweeps and stochastic ensembles with explicit uncertainty semantics, budgets and distinct policy/world/rollout counts.

**TL-021 Explain differences honestly.** A result difference shall link to changed assumptions and dependent quantities; additive account decompositions shall reconcile, and causal contributions shall require a stated attribution method.

**TL-022 Compare the main trajectories.** The dashboard shall show sketch outcome fans and matched differences with synchronized year selection, levels, sample counts and selected paths; later campaign views shall aggregate large ensembles without limiting search size.

**TL-023 Inspect the timeline.** A structured timeline shall show recorded Pacifica decisions, independent actor responses, chance events, conditions, observations and divergence points linked to results, with a deterministic summary usable without LLM narration.

**TL-024 Edit decisions and model assumptions.** The editor shall distinguish Pacifica decision levers, actor-response models and uncertainty assumptions, exposing only supported fields and preventing the optimizer from treating other actors or random outcomes as controllable choices.

**TL-025 Trace any displayed number.** Every displayed R0 quantity shall expose its definition, run/input identity, producing module/version, basic assumption/source IDs and coverage/fidelity status; detailed formula and instrument inspection shall follow in R2.

**TL-026 Export a reproducible experiment.** Users shall export a scenario bundle, experiment manifest, selected results and validation summary with enough input and engine references to replay the calculation.

**TL-027 Protect sources and validate execution inputs.** Imports shall be treated as data; only registered model operations may execute, and source attachments shall remain immutable.

**TL-028 Validate the native engine against frozen evidence.** The detailed ledger shall reconcile all declared outputs of the six frozen cases and pass independent accounting tests in R2; fixture agreement shall remain distinct from empirical or strategic validation.

**TL-029 Keep the initial lab private.** The first release shall run for a single author in a local private workspace, with no automatic upload or publication of models and drafts.

**TL-030 Meet measured responsiveness targets.** Responsiveness targets shall be measured end to end on declared hardware and fidelity: 1,000 sketch rollouts displayed within 1 second at p95, 10,000 within 10 seconds, cached interactions within 250 ms at p95 and compact 100,000-rollout queries within 1 second; targets remain provisional until the M0 spike.

**TL-031 Make comparisons readable and accessible.** Core flows shall work by keyboard, use visible focus and textual status, and provide tables and labels that do not rely on color alone.

**TL-032 Recover without corrupting work.** From R0, draft saves and result publication shall protect prior versions, reject stale writes and publish complete manifests only after artifacts are durable; interruption recovery shall distinguish orphan files, incomplete jobs and completed runs.

**TL-033 Register models and capabilities.** Each model module shall declare versioned inputs, outputs, units, state transitions, dependencies, supported events, temporal resolution and validation checks.

**TL-034 Extend the world state.** The scenario and run contracts should extend beyond the bounded strategy-search pilot to additional regions, actor types, event families and richer demographic, industrial, trade, military-logistics and institutional modules.

**TL-035 Evaluate policy limits with valid denominators.** Targets shall specify geography, years, exceptions and numerator/denominator definitions; missing denominators shall produce unavailable checks.

**TL-036 Version the data contract.** Catalog and exchange contracts shall have machine-validated schema versions, explicit supported migrations and self-contained resolved bundles; R0 shall validate typed files and reject unknown major versions without requiring a full schema-generator framework.

**TL-037 Run without Excel.** Every supported Lab calculation shall run in the native engine without Excel, Office COM, an interactive desktop, spreadsheet formula evaluation or an Excel fallback.

**TL-038 Version the world catalog as validated text.** World, scenario overlays, assumptions and catalogs shall be schema-validated text in the project Git repository; saved versions use a pinned parent, commit and resolved-content hash, with valid references and immutable run inputs.

**TL-039 Separate calculation from persistence and presentation.** The model core shall accept a complete immutable input bundle and return state trajectories, postings, checks and provenance without requiring a dashboard, live database or network service.

**TL-040 Separate accounting identities from economic assumptions.** The engine shall advance explicit opening stocks through dated flows and valuation or other changes, reconcile financial postings, and identify behavioural equations and calibration assumptions separately from accounting identities.

**TL-041 Define success before search.** Each search shall pin an objective-and-constraint set defining beneficiaries, scope, units, direction, horizon, aggregation across time and futures, thresholds, and evidence/coverage requirements.

**TL-042 Generate legal decisions from an action catalog.** The simulator shall expose parameterized Pacifica actions with preconditions, duration, costs, authority, physical limits and declared state effects, from which new paths can be generated without authored outcome prose.

**TL-043 Search adaptive policies without future knowledge.** Policies shall map Pacifica's observable history and declared policy randomness to feasible actions, support fixed comparators and prevent access to hidden state or future draws; optimization adds candidate search in R1.

**TL-044 Represent independently responding actors.** Other actors shall select actions using their own versioned objectives, information, capabilities, constraints and response policies; Pacifica's optimizer shall not directly choose their actions.

**TL-045 Model strategic capability and sustainment.** The bounded pilot shall connect economics and public accounts to force availability, mobilisation, sustainment, geography/access, political support and independent actor decisions at declared resolutions.

**TL-046 Represent uncertainty explicitly.** The model shall distinguish stochastic variation, uncertain parameters and alternative structural/actor models, with justified ranges, dependence assumptions and probability status.

**TL-047 Evaluate policies across repeated generated futures.** Policies shall be evaluated in reproducible ensembles using a versioned draw-address scheme independent of batch partition or worker scheduling, with separate namespaces for world uncertainty, policy randomness, actors and optimization.

**TL-048 Search a set of multiobjective strategies.** The optimizer shall generate and improve candidate policies, enforce constraints and maintain an estimated nondominated set across selected distributional objectives within an explicit budget.

**TL-049 Test finalists on unseen futures and actor models.** Finalists shall receive adaptive additional sampling when rankings or tail estimates are uncertain, then assessment on fresh world samples and alternative actor/structural models not used to tune policies.

**TL-050 Explain strategic strengths and failures.** The lab shall identify the decisions, constraints and conditions associated with each policy's success or failure and support controlled reruns for decision-relevant counterfactuals.

**TL-051 Run large campaigns within a declared budget.** The runner shall support a bounded base campaign of at least 1,000 distinct candidate policies and 100,000 complete trajectories with budgets, progress, checkpoints and per-evaluation status; screening, resampling, response search and assessment costs shall be reported separately and together.

**TL-052 Explore outcome distributions and trade-offs.** The dashboard shall show objective distributions, estimated Pareto trade-offs, joint target attainment, uncertainty sensitivity and selected path replays across the full campaign.

**TL-053 Establish model credibility for its intended use.** Credibility gates shall apply from R0 to the bounded claim: independent reference checks, accounting/physical limits, actor refusal and intervention tests; later search and full-ledger evidence shall extend rather than replace these gates.

**TL-054 Replay and export a discovered strategy.** A saved search result shall include policy, initial state, objective definition, actor/uncertainty models, model/engine versions, random-stream plan and traceable evaluation artifacts.

**TL-055 Score distributions without hiding their assumptions.** Objective evaluation shall support means, quantiles, cumulative/path measures, tail losses and joint threshold attainment with clear probability/weight semantics, horizon treatment and missing-data rules.

**TL-056 Demonstrate discovery without prewritten outcomes.** R1 shall demonstrate discovery and assessment of new adaptive policies in a bounded domain with independent actors; R0 is a foundation release and six scripted histories cannot satisfy the discovery goal.

**TL-057 Gate metrics on usable evidence and coverage.** Every displayed or scored state/success measure shall identify definition, scale, boundary, sources/assumptions, module coverage and uncertainty from R0; unsupported claims shall be unavailable or explicitly labelled conditional proxies.

**TL-058 Sketch interactively.** Editing a supported R0 lever shall evaluate the bounded policy without search, stream progressive outcome fans and compare with a pinned reference under matched exogenous worlds; only the declared narrow controls are required initially.

**TL-059 Simulate on an explicit compiled layout.** The fast engine shall advance many worlds on a versioned fixed-shape layout with explicit state bindings and isolation; compiled per-world kernels are allowed when profiling favors them, while repeated interpreted Python dispatch is kept out of the hot path.

**TL-060 Validate the fast model on baseline and changed cases.** The fast model shall fit declared aggregate baseline series within pinned calibration bands and pass independent changed-input reference cases for the bounded claim; baseline fitting alone is insufficient.

**TL-061 Check paths and re-evaluate policies with the detailed ledger.** Detailed-ledger assessment shall support immutable forensic checking of a recorded history and separate policy re-evaluation under detailed states, using shared mechanism definitions and explicit fidelity projections rather than independently invented economics.

**TL-062 Map diverse strategies without forced scalar quality.** The strategy map shall retain a bounded nondominated policy set within each author-chosen behavior cell, with explicit descriptor aggregation, uncertainty, capacity and deterministic pruning rules alongside the global Pareto set.

**TL-063 Separate own-interest responses from hostile stress tests.** Finalists shall face bounded best/near-best response analysis under each actor's own declared preferences, information and resources, plus a separately labelled hostile stress search with explicit plausibility and acceptable-own-outcome bounds.

**TL-064 Group histories into inspectable types.** Rollouts shall be grouped using registered event/trajectory features into history types with empirical shares, distinguishing associations and representative paths, preserving rare and terminal outcomes.

**TL-065 Narrate recorded facts with bounded claims.** Optional LLM narration shall render a selected structured history after calculation using a typed claim record and inserted result values; R0 shall remain fully usable with deterministic templates and the timeline.

**TL-066 Generate structural schemas with explicit runtime bindings.** Shared typed declarations shall generate supported structural artifacts such as catalog/exchange schemas, result schemas and form/layout metadata; simulation semantics, runtime mappings, migrations and interaction design remain explicit reviewed code.

**TL-067 Store batched results with recoverable manifests.** Outcomes and selected trajectories shall be written in batches as immutable content-addressed columnar artifacts, with retained manifests and a rebuildable local query catalog; time steps shall not write rows individually.

### 7.3 Additional phase gates

These criteria extend requirements already introduced earlier; they do not postpone their basic R0 obligation. Their full Given/When/Then records are in the backlog.

| Requirement | Phase | Additional evidence | Additional prerequisites |
|---|---|---|---|
| TL-015 | R2 | Budgets, interest, repayment, losses, currencies and borrower/lender schedules reconcile under declared decimal and rounding rules. | TL-061 |
| TL-019 | R2 | Exact fixture labels, C0 conditions, aliases and distinct scenario premises remain visible. | TL-002, TL-009 |
| TL-021 | R2 | Full schedules, rights, claims and losses link to the impact preview. | TL-007 |
| TL-025 | R2 | Formula/module, inputs, instrument postings and source derivations are linked; optional worksheet mappings remain technical provenance. | TL-061, TL-010 |
| TL-027 | R2 | Original bytes and unknown fields remain intact; formulas remain inert source evidence. | TL-002 |
| TL-032 | R1 | Optimizer state, evaluation order, archive tie rules, draw addresses and budgets restore under the declared deterministic-resume contract. | TL-013, TL-048 |
| TL-036 | R1 | CI detects artifact drift; supported migrations remain explicit. | TL-066 |
| TL-036 | R2 | Supported fields, unknown source fields, labels and original bytes survive losslessly. | TL-002, TL-026 |
| TL-053 | R1 | Enumerable benchmarks, simple-policy/random-search comparisons, response/stress sensitivity and fresh assessments support the declared bounded search claim. | TL-048, TL-049, TL-062, TL-063 |
| TL-053 | R2 | Fixture parity remains a financial equivalence check; independent actor/physical validation is still required. | TL-028, TL-061 |

### 7.4 End-to-end demonstrations

| # | Demonstration | Stage | Requirements |
|---|---|---|---|
| 1 | Independent reference: baseline plus accepted/refused/counteroffered credit, changed terms/dates, failed rollover and interim shortage; compare values and later feasibility. | M0/R0 | TL-040, TL-053, TL-060 |
| 2 | Sketch a supported financing/commitment lever; show provisional 1,000/10,000-path targets, counts, coverage, current identity and offline replay; explicitly save a version. | R0 | TL-022, TL-023, TL-058 |
| 3 | Identical observations and policy randomness give identical pre-shock decisions; single/batch/partition runs preserve indexed draws and logical events in the pinned environment. | R0 | TL-011, TL-043, TL-047, TL-059 |
| 4 | Compute a saved sketch and a changed input on supported Windows/Linux without Office, a network calculation service or a server database. | R0 | TL-037, TL-039 |
| 5 | Interrupt publication around file/index boundaries and save from a stale tab; recover the last complete version and rebuild the index from manifests. | R0 | TL-032, TL-067 |
| 6 | Discover at least 1,000 policies/100,000 generated paths with actual independent refusals, adaptive choices, reported total budgets and fresh assessment. | R1 | TL-048, TL-049, TL-051, TL-056 |
| 7 | An enumerable multiobjective problem reproduces global and per-cell nondominated sets; bounded pruning and never/uncertain descriptor cases follow declared rules. | R1 | TL-048, TL-062 |
| 8 | A counterparty cooperates under its own goals; hostile stress has separate plausibility bounds. Lost advantage is sensitivity. A seeded real model defect needs a reproducible counterexample before an exploit label. | R1 | TL-063 |
| 9 | Keep rare/terminal histories and empirical shares; reject narration with an invented motive even if its event ID and number are correct. Offline structured summaries remain usable. | R1 | TL-064, TL-065 |
| 10 | A detailed funding shortage invalidates a recorded commitment in forensic mode; policy re-evaluation produces a new linked action/response history under matched external worlds. | R2 | TL-061 |
| 11 | Import exact six files twice; preserve six identities, 17 run labels and 14 distinct inputs, conditions and aliases; compare 87 annual periods/73 metrics plus finer schedules. | R2 | TL-002, TL-028 |
| 12 | Fork a fixture's parameter from 1928, inspect removed loan/concession obligations, preserve C0 and keep absent North American denominators unavailable. | R2 | TL-007, TL-009, TL-019, TL-021, TL-035 |
| 13 | Apply a finance-skill proposal as validated model inputs and trace a detailed quantity to its source, derivation and instrument. | R2 | TL-010, TL-025 |
| 14 | Inject a broken cash/debt identity and an unconfigured cycle; show the terms/residual or cycle path without inheriting an old success badge. | R0; detailed R2 | TL-012, TL-014, TL-015 |

## 8. Exchange and model contracts

R0 contracts use versioned typed declarations and explicit bindings. Structural generation in R1 may produce JSON Schema 2020-12, form scaffolds, result types and layout metadata; semantic migrations and execution rules remain reviewed code.

| Contract | Minimum contents |
|---|---|
| Resolved version | Commit/parent, source assets, complete inputs, authority/conditions and content hash |
| Quantity proposal | Stable target, units/basis, dates, parties, value/schedule, evidence, derivation, bounds and dependencies |
| Module/fidelity | Inputs/outputs, units, transitions, dependencies, period resolution, resource/check rules, aggregation/projection and supported fidelity |
| Policy/actor | Observation limits, own preferences, capabilities, legal/physical constraints, rules and supported actions |
| Sketch | Version, narrow lever values, measures/coverage, world design, draw allocation and evaluation budget |
| Campaign | Objectives/constraints/descriptors, search/archive/pruning rules, sampling/stopping budgets and actor/structural alternatives |
| Rollout | Policy/world/input identity, environment, layout/bindings, draw addresses, observations/events, outcomes/checks and status |
| Detailed assessment | Forensic or policy-re-evaluation mode, original run and policy, detailed model, matched-world design, discrepancy rules and new lineage |
| Result manifest | Durable artifact hashes, completeness, definitions, statuses, covered/unavailable measures and replay assets |
| History/narration | Feature/clustering configuration, empirical shares, representative paths and typed claim/support records |

Normalized observations key run, metric, entity/geography and period, with value or explicit missing reason. Shared definitions are referenced rather than duplicated, but retained bundles/manifests must resolve old inputs without a live server.

Treat imports as data. Protect original bytes and hashes; unsupported majors fail without mutation. R2's fixture adapter preserves unknown source fields, labels and migration provenance. Spreadsheet formulas remain inert evidence, and no supported calculation delegates to Excel or a formula interpreter.

## 9. Proposed technology and execution design

| Layer | Recommendation | Boundary |
|---|---|---|
| Types/contracts | Minimal typed Python models and validated schemas in R0; structural generation where useful in R1 | Runtime mappings, behavior, migrations and interface decisions remain explicit |
| World versions | Git text, overlays and resolved-content hashes | Temporary edits need no Git branch; named saves guard the parent |
| Fast core | Profiled NumPy batching and Numba-compiled kernels on declared layouts | Compiled loops are allowed; no silent capacity overflow or hidden state sharing |
| Randomness | Philox or equivalent with versioned logical draw addresses | Pin transformations/builds/environment; a seed alone cannot promise partition independence |
| Reference/detailed accounts | Independent small cases in M0/R0; full instruments/Decimal postings in R2 | Separate forensic checking from policy re-evaluation; precision does not establish economic truth |
| Search | Multiobjective frontier and within-cell Pareto sets with explicit pruning | No hidden scalar elite or automatic algorithm choice by objective count |
| Responses | Own-interest best/near-best analysis plus separate hostile stress | Sensitivity is not automatically an exploit; response model and stress bounds are explicit |
| Assessment | Adaptive extra samples, fresh worlds and alternative structures | Initial 100-world screening cannot certify sparse tail risks |
| Results | Immutable Parquet, retained manifests, rebuildable DuckDB query catalog | Single coordinator; recovery spans files, catalog and guarded Git refs |
| Application | Local FastAPI and React/TypeScript with streamed current-identity summaries | Narrow controls/structured summaries first; general editing and optional LLM rendering later |

See [model-architecture.md](model-architecture.md) for bindings, draw addresses, publication/recovery and fidelity contracts. The core consumes complete inputs and has no UI, network or storage dependency during transitions. Changing rule equations creates a model version; parameters remain typed data.

Read-only source extraction can obtain calibration/reference values. Every supported calculation runs natively from R0. Missing models remain explicit, and source workbooks are not a fallback runtime.

## 10. Quality targets and release gates

All targets are **proposed and unmeasured** until the realistic M0 spike. Pin hardware, actors, steps, fidelity, memory and included stages; confirm or explicitly revise before commitments.

| Dimension | Provisional target and measurement | Stage |
|---|---|---|
| First sketch view | 1,000 paths displayed within 1 second at p95 after an edit | R0 |
| Refined sketch | 10,000 paths within 10 seconds | R0 |
| Cached interaction | Year/reference/selection update within 250 ms at p95 | R0 |
| Compact query | Summaries over 100,000 paths within 1 second | R0 store; R1 campaigns |
| Base campaign | 1,000 policies × 100 screening worlds within 5 minutes on 8 CPU workers and 16 GB RAM | R1 |
| Detailed recorded-path check | One selected 1904–1932 path within 10 seconds; policy re-evaluation timed separately | R2 |
| Fixture import | Entire 25.5 MB set within 5 seconds at p95 | R2 |
| Progress | Current edit count/state visible; campaign update at least every 5 seconds | R0/R1 |
| Recovery | Stale saves rejected; interrupted files/index registration reconciled and index rebuildable | R0 |
| Accessibility | Keyboard actions, visible focus, textual status and equivalent tables at 1280×800 | R1 |

Sketch benchmarks use at least 20 warm measured trials and separately report cold start/compilation. Campaigns use three warm complete trials. Include realistic negotiation, queues, material finer timing, checks, logs, summaries, persistence and visible delivery, with kernel timing separately reported. Do not claim a whole-world monthly workload from an annual-only benchmark.

The base campaign count is an initial screening workload. Extra sampling, response/stress search, fresh assessment, clustering and narration receive explicit budgets and total-cost reporting. Record actual unique policies/behaviors, worlds, evaluations, cache reuse and error counts; shared evaluations count once.

**Numerical policies are distinct.** Fast identity checks scale tolerances to identity terms. Baseline calibration bands describe a named fit, while assessed off-baseline fidelity rules describe other cases. A decision/feasibility or terminal-loss reversal triggers review even within a calibration band. The proposed detailed regression rule remains `abs(actual − reference) ≤ max(absolute tolerance, relative tolerance × abs(reference))`: monetary quantities in millions use 0.000001 absolute and 1e-9 relative; ratios use 1e-10 and 1e-9; dates, IDs and integer counts match exactly. Other types and exceptions need versioned explicit policies.

**M0/R0 correctness precedes recommendations.** Independently derive baseline/changed-input expectations and inspect acceptance/refusal, dates/terms, rollover and interim liquidity. Keep evidence for ownership, feasible resources, observation limits and terminal duties. Full fixture parity remains R2 and cannot validate actor probabilities or missing physical mechanisms.

| Milestone | Exit evidence |
|---|---|
| M0 Define the bounded question and prove correctness and speed | Agree the narrow financing/commitment slice, actors, observations, evidence and temporal resolution; check baseline plus independent changed-input cases and profile a realistic kernel with queues, checks, logs and delivery. Confirm or revise performance targets. Minimal typed contracts and explicit bindings suffice; no full generator or LLM renderer is required. |
| M1 Deliver the credible bounded sketchpad | Independent responses, constrained commitments, correct timing, versioned inputs, coverage/trace labels, recovery and progressive fans work for the declared question; offline structured replay is usable without a general editor or LLM narration. |
| M2 Discover and assess diverse policies | Pareto/frontier and per-cell archives, adaptive sampling, own-interest responses, separate stress, fresh assessments, history types and optional bounded narration deliver the discovery demonstration. |
| M3 Deliver detailed policy reassessment and full financial regression | Forensic checks and separate policy re-evaluation report feasibility changes; full ledger, six-fixture parity, skill derivations and deep inspection satisfy R2 phase gates. |
| M4 Expand the supported world | Additional actors/regions/modules and semantic rebases pass their own evidence and behavior checks; any hosted mode is separately designed. |

No calendar estimate or implemented benchmark is asserted. Each in-scope acceptance and phase gate needs release evidence; unresolved Must criteria require an explicit scope revision. R0 is the credible bounded foundation, and R1 must demonstrate generated strategy discovery.

## 11. Decisions still open

The search goal, multiple objectives, independent other actors and Excel independence remain confirmed. Incorporating the design recommendations does not choose numerical risk tolerances, metrics or all implementation details.

| Decision | Status | Recommendation | Consequence |
|---|---|---|---|
| D-001 Product end goal | required by user | Support fast sketches and discover adaptive Pacifica strategies across generated histories with multiobjective trade-offs and inspectable failures. | R0 is a foundation; only R1's discovery loop satisfies the search goal. |
| D-002 Hosting and users | proposed | One author, loopback local browser application and headless native worker on supported Windows/Linux environments. | Hosted/multi-user mode needs its own access, storage and concurrency design. |
| D-003 Bounded pilot question | proposed | Begin with one Japan financing/commitment question, a few indispensable actor roles, explicit external conditions, monthly cash where material and supported readiness effects. | Agree actor roster and evidence boundary in M0; the slice cannot claim global diplomacy or all-eight-objective coverage. |
| D-004 Performance and sampling budgets | proposed unmeasured | Target 1,000 sketch paths in 1 second at p95, 10,000 in 10 seconds, and 100,000 base evaluations in 5 minutes on 8 workers/16 GB. Benchmark realistic queues/checks/logs/delivery before commitment. | Pin hardware and hot/cold timing; 100 worlds per policy is initial screening. Extra sampling, response/stress and final assessment have explicit budgets and precision rules. |
| D-005 Fixture distribution | proposed | Stage exact frozen files and provenance in versioned private artifact storage before R2; pin calibration/reference evidence needed for R0 earlier. | No legacy adapter runtime or Office dependency; metadata alone is not the six result files. |
| D-006 Success and scope boundaries | open | Use the objective sheet and researched families; enable only covered measures and explicitly named proxies. | Final beneficiaries, thresholds and acceptable risk remain open; no mandatory national-power score. |
| D-007 Storage foundation | proposed | Git-versioned validated text, immutable Parquet artifacts, retained manifests and a single-process DuckDB query catalog. | The index is rebuildable; durable publication/recovery spans files, manifests and guarded Git refs. PostgreSQL is a future hosted option. |
| D-008 Excel independence | required by user | Every calculation executes native modules without Office or spreadsheet-formula fallback from R0. | Source workbooks are read-only evidence; missing mechanisms remain explicit. |
| D-009 Multiple objectives and strategy diversity | confirmed multiobjective proposed archive details | Keep the global frontier and a bounded nondominated set per behavior cell with explicit pruning; no hidden scalar best-per-cell score. | Cell capacity, descriptor summaries and pruning rules need selection; archive diversity does not establish robustness. |
| D-010 Agency and response assessment | confirmed pacifica control proposed assessment details | Control Pacifica decisions only. Model others' own-interest responses, then separately stress hostile but plausible near-best responses. | Changed advantage means sensitivity; an exploit finding needs an identified model defect. Response bounds and hostility assumptions remain explicit. |
| D-011 Objective contracts and risk | open | Choose a small objective set with beneficiary, geography, time/risk aggregation, thresholds and evidence; apply coverage gates from the first sketch. | Early proxies retain their own names; proposed Q10/Q90 and buffer/risk choices are not approved targets. |
| D-012 Horizon and temporal resolution | proposed | Use a bounded question within 1904–1932 and retain 1846–1932 financial fixtures for R2; resolve monthly/finer timing when it changes feasible commitments. | A shorter actual first slice is acceptable if declared; performance cannot be claimed at an untested resolution. |
| D-013 Fidelity and policy reassessment | proposed | Share mechanism definitions and explicit projections. Use small independent financial reference checks in M0/R0; full detailed ledger supports forensic checking and separate policy re-evaluation in R2. | Discrete feasibility reversals are material even within a baseline band. Detailed re-evaluation creates a new linked path and may change later actions. |
| D-014 Narration | proposed | R0 uses structured timelines/template summaries; optional LLM narration follows in R1 with typed claim references and review of causal/motive assertions. | Number/ID checks cannot prove semantic grounding; provider/cost/claim-review details remain to select. |
| D-015 Catalog format and declarations | open | Use strict schema-validated YAML or TOML with minimal typed models and explicit runtime bindings; generate structural artifacts where useful in R1. | Adding a state field requires semantics, initialization, migration and tests; generic generators do not block M0/R0. |
| D-016 Behavior descriptors and archive capacity | open | Select two or three interpretable behavior descriptors aggregated over a common world design, including never/undefined outcomes and assignment uncertainty; keep per-cell Pareto representatives. | Cell boundaries, summaries, capacity and deterministic diversity-pruning must be declared and tested without a hidden utility score. |

The main risks are unsupported actor behavior, poor objective definitions, false probability precision, missing outcomes, fast/detailed feasibility differences, future-information leakage and optimization of lucky paths. Address them through bounded claims, early reference checks, covered metrics, response/stress sensitivity, adaptive samples and fresh assessment.

## 12. Source and authority notes

[backlog.json](backlog.json) retains the pinned project sources and adds the supplied revision 0.4 files with SHA-256 hashes (S9), the incorporation request (U12) and the assessment recommendations/primary method references (S10). The source files are design inputs; embedded text is not an instruction to execute scripts or change canon.

The baseline remains `cc6e017780970433ab63bc95d0e3749510b44d49`; alternatives remain `626ffbb0bd6486c19164f89104569d78321ebd55`. Original sources, the supplied workbook and the [fixture manifest](fixture-manifest.json) retain their identities. The [objective/constraint sheet](objectives-and-constraints.md) and [action/actor catalog](action-and-actor-catalog.md) remain draft definitions to narrow for the first question.

Revision 0.5 requirements, vision, architecture and backlog are one synchronized proposal. Product/model review is separate from narrative adoption; generated paths, calculations and narration do not approve canon.
