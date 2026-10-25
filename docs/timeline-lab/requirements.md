# Pacifica Timeline Lab requirements

**Draft for review · 25 October 2026 · Requirements version 0.9**

Timeline Lab is a strategic wargame and plot-exploration tool. The author sketches decisions, inspects causal alternatives and retains useful histories; campaigns search strong adaptive Pacifica strategies and supported routes to declared narrative conditions. Strategic objectives, actor intentions and author preferences remain separate. The author controls Pacifica in ordinary policy search; other actors respond independently.

The [product vision](product-vision.md) defines this end goal, the researched measurement framework and the intended user experience. The six authored timelines are financial regression references and comparators, not the space of possible outcomes.

Strategy discovery, multiple objectives, independent other actors and Excel-free execution remain confirmed goals. Revision 0.9 incorporates the v0.8 review: separate agency evidence dimensions, isolated action comparisons, explicit source-to-playable-content activation, protected ambiguity and bounded relational actions. It adds data-population estimates and aggregate memory/disk/retention budgets. The existing ontology and release sequence remain sufficient for M0; active mechanisms, exact start phase and pilot limits are selected and measured there.

## 1. Product purpose and users

The primary user is the Pacifica author, who needs consequential choices, intelligible surprises, distinct causal alternatives and credible strategic trade-offs. The model maintainer defines supported mechanisms and evidence; the finance skill proposes quantities and derivations.

Two loops use the same semantic model:

- **Sketch:** evaluate a supported policy, compare matched outcome fans, inspect beliefs/plans and adjudicated events, branch at a decision and retain useful histories.
- **Campaign:** define strategic objectives or author narrative conditions, search within a declared intervention space, assess independent responses and fresh worlds, and inspect both strategic trade-offs and useful story alternatives.

R0 proves one financing/commitment dilemma with indispensable actors, selected beliefs/intentions, material timing, one supported actor-scoped conduct comparison, complete decision reconstruction, applicability checks and deterministic summaries. R1 adds assessed strategy and bounded narrative-condition search. R2 adds general editing, structural generation, optional LLM narration and detailed financial fidelity.

Monte Carlo evaluates outcomes; optimization searches policies; diversity organizes behavior; narrative conditions express author interest. A dominated policy can be bookmarked without changing its strategic score. A targeted story sample cannot establish ordinary success probability.

Ordinary strategy discovery controls only Pacifica decisions and never chooses lucky seeds or counterpart compliance. Author overrides and imposed events remain conditional consequence experiments. A regenerated history under explicit changed premises may support those premises only; it never certifies the original package. Generated histories, motives and prose remain drafts; adopting a model or query does not approve canon.

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
| R0 bounded dramatic sketch | One agreed financing/commitment dilemma with selected character/institutional agency | Native independent checks, ontology invariants, belief/plan updates, observation-safe attempts, simultaneous resource resolution, one supported actor-scoped conduct case, full decision forks, applicability propagation, story bookmarks, recovery and author usefulness review |
| R1 strategy and plot discovery | Assessed strategy search and bounded narrative-condition/minimum-change search | Global/per-cell archives, adaptive sampling, own-interest responses and separate stress, fresh assessment, history types, stated selection denominators and repeated author review |
| R2 tools and detailed fidelity | General authoring and detailed financial evidence | General editor, structural generation, optional grounded narration, full instrument forensic/policy reassessment, six-fixture parity, finance-skill derivations and deep inspection |
| R3 expansion | Wider supported questions and collaboration | New actors/regions/mechanisms and rebases pass their own checks; hosted mode receives a separate design |

A requirement's release is its **first required obligation**. Later `phase_gates` add explicit Must criteria at their own release. Existing IDs remain stable; AC-036-R1 retains its legacy identifier while its generation check moves to R2 with TL-066.

M0 selects a Japan financing/commitment dilemma, actor roster, a few consequential propositions/plans, one supported breach comparison and its consequence mechanisms. A shorter slice within 1904–1932 is permitted. It cannot claim omitted theatres, unsupported human/welfare outcomes or universal psychology.

| Capability | R0 foundation | Later extension |
|---|---|---|
| Author controls | Targeted levers, explicit profiles/intervention modes, narrative filters and bookmarks | Targeted campaign/query forms in R1; general editor in R2 |
| Semantics | Active ontology subset, minimal validated types, explicit bindings and invariants | Structural generation in R2; new domains in R3 |
| Agency | Independent responses plus selected belief/plan updates and observed versus actual feasibility | Bounded response/stress and narrative-condition search in R1 |
| Accounts | Owned resources, reservations, material timing and independent changed-input checks | Full instrument ledger and fixture parity in R2 |
| Replay | Complete decision-state reconstruction, typed explanations and deterministic summary | History types in R1; optional LLM prose and detailed reassessment in R2 |
| Credibility | Applicability, coverage, semantic and financial tests, and author usefulness | Fresh search assessment in R1; full evidence inspection in R2 |

Only the active bounded ontology subset must execute in R0. A universal ontology generator, complete personality model, general editor and LLM provider are not R0/R1 prerequisites. The author gate precedes broad tooling and search-scale commitments; a failed gate requires an explicit design/scope revision.

R0 also requires independent open proposal generation and separate plausibility, controller-generation and isolated-consequence evidence. Test one plausible action change under unchanged continuation rules, trace a material consequence and different next dilemma, and include a low-effect contrast. Independently plausible overrides may support conditional consequences without becoming actor-generated witnesses. Add a relational chain producing distinct plots with similar finances. This bounded demonstration belongs to TL-042/TL-069/TL-072/TL-073/TL-075; broad finalist counterfactual analysis remains TL-050 in R1.

## 4. Domain model and ontology

TL-077 activates a versioned ExperimentContentManifest: starting facts, active obligations, future reference outcomes, explicit external assumptions and author constraints have different roles. Source authority, identity, valid/knowledge times and transitive mechanism dependencies must be resolved or explicitly excluded. Protected ambiguity cannot become a sampled hidden fact. See [the population plan](data-population-plan.md) for source measurements, staged review and estimated work.

[ontology.md](ontology.md) defines the semantic contract and its 16 invariants; `draft-model-catalog.json.ontology_contract` mirrors its 29 record definitions. These are design contracts, not implemented schemas. Future typed models, validators, runtime layouts and migrations must preserve them.

The contract also specifies additive conduct-category sets, query claim admissibility, the resolved-experiment manifest, open proposal coverage and bounded agency evidence. These refine existing records and services; they do not require another general ontology layer.

| Semantic area | Required distinctions |
|---|---|
| Identity | Person, office, institution, faction and community; dated role tenure and explicit succession/transfer rules |
| Truth and information | Typed proposition, underlying branch fact, source/public assertion, delivered observation and actor-specific belief |
| Intention | Institutional/personal goals, persistent plans and promises; legal obligations arise only through declared formation rules |
| Action | Perceived eligibility, selected attempt, actual adjudication, legal status, disposition, realized event and disclosed observation |
| Relations | Qualified parties, terms, subject, consent, authority, conditions, dates and termination; ownership/control/access remain separate |
| Time and branch | Effective/valid dates, event/receipt/known dates and author save time; scoped immutable ancestry and established prefix |
| Mechanism | Inputs/outputs, state read/write ownership, clock, lag/solver, applicability, evidence, uncertainty and reference/counterexample tests |
| Experiment | Profiles, policies, decision checkpoints, three intervention modes, narrative queries, campaigns and assessment populations |
| Retention and explanation | Author bookmarks independent of Pareto pruning; typed prerequisites, dependencies, modeled effects, associations and interpretations |

R0 exercises the active semantic subset with unknown/disputed consent, a dated role/obligation case, selected belief/plan updates, observation-safe eligibility and resource resolution. Missing, false, refused, disputed and unmodeled values cannot be substituted for one another. Contradictory source assertions retain their provenance; material unresolved underlying truth requires a hypothesis branch or blocks the mechanism using it.

Active predicates specify argument roles, value domains, cardinality, target time, state keys and authoritative writers. Immutable fact/belief revisions and delivered payloads preserve historical knowledge under delayed reports. DecisionContext binds person/principal/role/authority/resources and the executed procedure; DecisionRecord captures actual used inputs and considered alternatives. These contracts must be proven in the M0 semantic prototype before optimized runtime interfaces are fixed.

Conduct is bound by actor/action family and time to additive permission sets. All profiles allow lawful execution; apparent_authority adds supported mistaken-authority execution and breach_exploration adds supported intentional breach. Actual legality is independent of the profile label. Broader permissions never compel misconduct or invent consent; independent choices, covered consequences and hidden information remain binding.

Actor-visible menus, previews and rejection messages obey the same information limits as decision inputs. The adjudicator may know underlying truth, but only its observation rule can disclose that truth. Ordinary response analysis does not reveal Pacifica's private policy code to counterparties.

Lawful execution and supported breach exploration are separate profiles. Physical/accounting invariants and locked authorial premises hold in both. A breach family needs registered resistance/enforcement/institutional and obligation consequences before it is enabled; later cure preserves the prior breach interval.

Economic and response rules remain registered versioned code, not runtime LLM inventions or executable formula strings in data. Source/assumption IDs, semantic references and basic dependency/status propagation apply from R0; the full impact inspector remains R2.

## 5. Financial and temporal semantics

Every metric identifies entity, geography, units/currency, nominal/real basis, period, quantity kind and aggregation. Core, crown, common, private and foreign resources remain separate. Partner output is not sovereign GDP; a loan/concession does not transfer all revenue or jurisdiction.

Classify principal, repayments, interest, expenditure, asset purchases, losses and financing separately. A creditor write-down does not by itself extinguish the borrower's legal obligation. Avoided expenditure is not extra GDP; private syndicate claims are not Treasury property.

**Timing applies from R0.** Annual reporting sums flows and selects stock endpoints. Resolve months or event dates when a rollover, draw, supply interruption or payment changes available actions. A positive annual balance cannot certify liquidity. A deliberately coarser experiment states the risk it omits.

**Validation has distinct meanings.** Fast arithmetic checks use declared per-module tolerances. Baseline calibration has pinned series/bands. Independent changed-input examples test specific behavior and feasibility. Assessed fast-to-detailed discrepancies use their own projection/error rules. A changed acceptance, feasible action or terminal-loss state is material even inside an aggregate calibration band.

Both fidelity levels share mechanism definitions with explicit aggregation and instrument implementations. M0/R0 checks accepted/refused/counteroffered credit, changed rates/maturities/dates, failed rollover and an interim shortage against independently derived reference calculations. A baseline fit cannot establish off-baseline correctness.

**Detailed R2 assessment has two modes.** Forensic checking preserves recorded actions/events, finds discrepancies and identifies the first impossible commitment without forcing it to execute. Policy re-evaluation runs the same conditional policy and exogenous-world design against detailed states; observations, actor responses and subsequent choices may change. It creates a new linked history and cannot silently overwrite fast results.

C's C0 continuation, D's unresolved denominators and other fixture conditions remain explicit. Never substitute D's institutions into C or core GDP for North American GDP. Report or bound post-horizon debt, guarantees, maintenance, restoration and treaty duties. Defeat/default remain outcomes; computational errors remain separately counted unknowns rather than arbitrary utility penalties.

The interface keeps narrative authority, evidence, execution, accounting, funding, coverage, fidelity, applicability and selection mode separate from the first sketch. Unknown consent, an unlawful event and a physically impossible effect are different states.

## 6. Dashboard and authoring workflow

**Sketch:** select a pinned world and actor conduct bindings → edit a supported lever → stream matched outcomes and causal candidates before strategic pruning → inspect actual decision reasons and dramatic consequences → explore without an ending, filter or bookmark spontaneously → reconstruct a decision and branch → save explicitly.

**Campaign:** choose strategic optimization or an explicit narrative search mode → declare target quantification, temporal conditions, interventions, sampling, population and budget → inspect trade-offs or causal routes with result status → assess responses and freeze policies/models where reliability is claimed → evaluate fresh unconditioned worlds → retain useful histories and assumptions.

| View | Purpose | Release |
|---|---|---|
| Sketch and quantity inspector | Targeted levers, matched reference, counts, units, sources, coverage, applicability and fidelity | R0 |
| Timeline and actor perspective | Attempts, observations, selected beliefs/plans, legal status, counterpart responses, realized events and deterministic summary | R0 |
| Decision branch | Complete state reconstruction; separate decision, premise and imposed-event modes; first material divergence | R0 |
| Story exploration and archive | Open causal candidates before pruning, supported dramatic views, typed filters and spontaneous bookmarks | R0 |
| Campaign and narrative query | Targeted objective/constraint/descriptor and narrative forms, budgets, allowed interventions and selection denominators | R1 |
| Trade-offs, response and history types | Global/per-cell strategy archives, independent responses/stress, fresh assessment and representative histories | R1 |
| General catalog editor and optional narration | Broader supported fields and reviewed typed-claim-based prose | R2 |
| Detailed accounts and evidence | Full schedules, forensic checking, policy re-evaluation, derivations and impact previews | R2 |

A new edit invalidates current-view identity immediately. Superseded work cannot update the new view. Guard saves and publish complete durable artifacts/manifests before index registration. Bookmarks retain assets independently of archive pruning or clustering.

Narrative queries inspect recorded outcomes without entering actor observations. Targeted story frequencies show their selection denominator; ordinary policy distributions require fresh unconditioned assessment. A chosen provisional continuation or imposed event remains conditional in comparisons and exports.

Charts and tables share selections, units and statuses. Basic structured replay, narrative filtering and summaries work offline; general editing and optional LLM narration follow the demonstrated author workflow.

## 7. Requirements and acceptance register

The backlog is authoritative for Given/When/Then acceptance. This register mirrors every statement, release and later gate. Revision 0.9 preserves prior IDs and adds TL-077/TL-078: 78 requirements, 76 Must and 2 Should; first obligations are R0 49, R1 18, R2 9 and R3 2, with 12 later phase gates and 37 demonstrations.

### 7.1 Register

| ID | Requirement | Priority | First release | Later phase gates |
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
| TL-024 | Edit decisions and model assumptions | Must | R2 | — |
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
| TL-036 | Version the data contract | Must | R0 | R2 |
| TL-037 | Run without Excel | Must | R0 | — |
| TL-038 | Version the world catalog as validated text | Must | R0 | — |
| TL-039 | Separate calculation from persistence and presentation | Must | R0 | — |
| TL-040 | Separate accounting identities from economic assumptions | Must | R0 | — |
| TL-041 | Define success before search | Must | R1 | — |
| TL-042 | Generate attempts under declared action profiles | Must | R0 | — |
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
| TL-065 | Narrate recorded facts with bounded claims | Must | R2 | — |
| TL-066 | Generate structural schemas with explicit runtime bindings | Must | R2 | — |
| TL-067 | Store batched results with recoverable manifests | Must | R0 | — |
| TL-068 | Define and enforce world semantics | Must | R0 | — |
| TL-069 | Connect selected beliefs and intentions to actual choices | Must | R0 | — |
| TL-070 | Adjudicate attempts without leaking hidden information | Must | R0 | — |
| TL-071 | Scope lawful and supported exceptional conduct by actor | Must | R0 | — |
| TL-072 | Branch from a complete decision state | Must | R0 | — |
| TL-073 | Discover varied story candidates and search explicit narrative targets | Must | R0 | R1 |
| TL-074 | Enforce mechanism applicability and provisional continuations | Must | R0 | — |
| TL-075 | Demonstrate usefulness for plot development | Must | R0 | R1 |
| TL-076 | Resolve simultaneous commitments consistently | Must | R0 | — |
| TL-077 | Prepare and activate traceable experiment content | Must | R0 | — |
| TL-078 | Bound memory disk use and result retention | Must | R0 | — |

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

**TL-011 Make runs reproducible.** Calculation, evaluation and branch identities shall share a canonical resolved-experiment manifest pinning complete semantic inputs, conduct, fidelity, policies, actor/mechanism versions, schemas/bindings, uncertainty/draw design and environment; reproducibility guarantees shall state their supported environment.

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

**TL-041 Define success before search.** Each strategic optimization or policy-reliability search shall pin its objective/target-and-constraint set, beneficiaries, scope, units, horizon, aggregation, thresholds and coverage. Narrative filtering, open exploration and existential or premise search use TL-073 contracts and require no strategic objective set or Pareto output.

**TL-042 Generate attempts under declared action profiles.** The simulator shall expose parameterized Pacifica action attempts with observation-safe eligibility, costs, duration, legal status, physical constraints and declared effects; adjudication shall distinguish attempted conduct from lawful authority and realized execution.

**TL-043 Search adaptive policies without future knowledge.** Policies shall map Pacifica's observable history, declared beliefs and policy randomness to attempted actions, with observation-safe eligibility and messages; neither policy inputs nor feasibility filtering may reveal hidden state or future draws.

**TL-044 Represent independently responding actors.** Other actors shall select actions using their own versioned objectives, information, capabilities, constraints and response policies; Pacifica's optimizer shall not directly choose their actions.

**TL-045 Model strategic capability and sustainment.** The bounded pilot shall connect economics and public accounts to force availability, mobilisation, sustainment, geography/access, political support and independent actor decisions at declared resolutions.

**TL-046 Represent uncertainty explicitly.** The model shall distinguish stochastic variation, uncertain parameters and alternative structural/actor models, with justified ranges, dependence assumptions and probability status.

**TL-047 Evaluate policies across repeated generated futures.** Policies shall be evaluated in reproducible ensembles using a versioned draw-address scheme independent of batch partition or worker scheduling, with separate namespaces for world uncertainty, policy randomness, actors and optimization.

**TL-048 Search a set of multiobjective strategies.** The optimizer shall generate and improve candidate policies, enforce constraints and maintain an estimated nondominated set across selected distributional objectives within an explicit budget.

**TL-049 Test finalists on unseen futures and actor models.** Finalists shall receive adaptive additional sampling when rankings or tail estimates are uncertain, then assessment on fresh world samples and alternative actor/structural models not used to tune policies.

**TL-050 Explain strategic strengths and failures.** The lab shall identify the decisions, constraints and conditions associated with each policy's success or failure and support controlled reruns for decision-relevant counterfactuals. R0 already requires a bounded local agency contrast under TL-072 and TL-075; this requirement adds broader finalist analysis in R1.

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

**TL-068 Define and enforce world semantics.** Supported records shall enforce registered predicate signatures, state keys and ownership, immutable revisions, target/valid/belief/receipt times, qualified relationships and branch scope, with machine-checkable invariants for the active ontology subset.

**TL-069 Connect selected beliefs and intentions to actual choices.** Every modeled choice shall bind its decision-maker, represented institution, dated authority, resource owners, permitted information and executed decision procedure; selected goals, beliefs, plans and commitments shall influence decisions only through that procedure and retain inspectable reasons.

**TL-070 Adjudicate attempts without leaking hidden information.** The engine shall separate perceived eligibility, selected attempts, actual adjudication, realized effects and disclosed observations, including rejection, delay, partial implementation and failure.

**TL-071 Scope lawful and supported exceptional conduct by actor.** Experiments shall bind explicit additive conduct permissions to named actors/action families; every profile permits lawful conduct, while perceived authorization, actual legality, intention, physical execution and discovery consequences remain distinct.

**TL-072 Branch from a complete decision state.** The author shall branch at a recorded decision point using a complete checkpoint or deterministic reconstruction and a declared decision, premise or imposed-event intervention, preserving established history and explicit lineage.

**TL-073 Discover varied story candidates and search explicit narrative targets.** R0 shall generate actor-admissible alternatives through a declared open-exploration proposal method and budget independent of strategic fitness, then expose supported story candidates, narrative filters and spontaneous bookmarks before pruning; R1 shall distinguish existential-history, policy-reliability and minimum-premise-change searches with explicit claim admissibility, temporal semantics, populations and statuses.

**TL-074 Enforce mechanism applicability and provisional continuations.** Every active mechanism shall declare an executable applicability predicate, read/write ownership, evidence and counterexample tests; leaving its supported domain shall invalidate dependent claims or create an explicitly selected provisional continuation.

**TL-075 Demonstrate usefulness for plot development.** Release evidence shall separately demonstrate plausible alternatives, intention-sensitive controller generation and isolated choice-to-consequence-to-next-dilemma effects with a low-effect contrast, plus useful ideas on prepared/open/held-out tasks against a manual-workflow comparator.

**TL-076 Resolve simultaneous commitments consistently.** The engine shall resolve simultaneous and sequential interactions through registered phases, resource reservations, allocation/tie rules and settlement semantics that are independent of incidental module or actor iteration order.

**TL-077 Prepare and activate traceable experiment content.** A staged ingestion workflow shall reconcile canonical sources into a versioned ExperimentContentManifest with explicit temporal roles, authority, actor information, ambiguity policies and complete active dependency dispositions before a slice runs.

**TL-078 Bound memory disk use and result retention.** Runs shall declare batch/worker, application-memory, output-retention and temporary-disk budgets; the scheduler shall enforce aggregate limits, preserve pinned evidence and recover cleanly when a budget or free-space limit is reached.

### 7.3 Additional phase gates

| Requirement | Release | Acceptance | Dependencies |
|---|---|---|---|
| TL-015 | R2 | Budgets, interest, repayment, losses, currencies and borrower/lender schedules reconcile under declared decimal and rounding rules. | TL-061 |
| TL-019 | R2 | Exact fixture labels, C0 conditions, aliases and distinct scenario premises remain visible. | TL-002, TL-009 |
| TL-021 | R2 | Full schedules, rights, claims and losses link to the impact preview. | TL-007 |
| TL-025 | R2 | Formula/module, inputs, instrument postings and source derivations are linked; optional worksheet mappings remain technical provenance. | TL-061, TL-010 |
| TL-027 | R2 | Original bytes and unknown fields remain intact; formulas remain inert source evidence. | TL-002 |
| TL-032 | R1 | Optimizer state, evaluation order, archive tie rules, draw addresses and budgets restore under the declared deterministic-resume contract. | TL-013, TL-048 |
| TL-036 | R2 | CI detects artifact drift; supported migrations remain explicit. The acceptance ID is retained from v0.5; its release moves to R2 with TL-066. | TL-066 |
| TL-036 | R2 | Supported fields, unknown source fields, labels and original bytes survive losslessly. | TL-002, TL-026 |
| TL-053 | R1 | Enumerable benchmarks, simple-policy/random-search comparisons, response/stress sensitivity and fresh assessments support the declared bounded search claim. | TL-048, TL-049, TL-062, TL-063 |
| TL-053 | R2 | Fixture parity remains a financial equivalence check; independent actor/physical validation is still required. | TL-028, TL-061 |
| TL-073 | R1 | Declare mode, target quantification, temporal expression, allowed interventions, sampling, evidence, population and budget. existential_history asks for a supported witness; policy_reliability compares target satisfaction on fresh unconditioned worlds; minimum_premise_change searches permitted edits using declared costs/order and ties. A rare supported witness need not be reliable. Story sampling may target declared uncertain conditions with recorded selection/weight contracts, but never grants actor foresight, forced counterparties or policy control over random seeds. Premise packages remain separately assessed. Distinguish found_supported, found_conditional, no_match_within_budget, unsatisfiable_within_exhaustive_scope and unsupported_query. Unresolved temporal predicates never pass; impossibility/minimality claims require the stated exhaustive bounded check. Return causally distinct best-found routes and inspectable unsuccessful searches. Imposed-event histories are conditional consequence experiments, not supported witnesses that a policy generated the event. Freeze selected policies and evaluate fresh unconditioned worlds before reporting ordinary distributions. Root-world, evaluation and branch denominators remain separate; targeted shares never establish unconditional success. R1 existential-history search may rank supported decision/policy edits by explicit change costs without altering premises; such ranking needs units/order, bounds and ties and claims minimality only after exhaustive bounded checking. found_supported requires a satisfied target and admissible actor-generated history over the assessed lineage under explicit premises. Author decision overrides and imposed/provisional histories can return found_conditional only when allowed; otherwise they are excluded with reasons, never counted as predicate-false evidence for exhaustive impossibility. A fully regenerated changed-premise witness is supported only under the separately named premise package. | TL-048, TL-049, TL-050, TL-055 |
| TL-075 | R1 | Review causal variety, meaningful agency, branch comprehensibility and useful retained ideas against the R0 workflow; report sample and protocol limits. Neither 100,000 rollouts nor attractive prose substitutes for author acceptance; shortcomings are recorded before expansion. Repeat open exploration and the manual-workflow comparison with a fresh held-out question if earlier assessment feedback informed development; report novelty, assumption disclosure and repair burden. | TL-048, TL-049, TL-064, TL-073 |

### 7.4 End-to-end demonstrations

| ID | Demonstration | Release | Requirements |
|---|---|---|---|
| 1 | Independent reference: baseline plus accepted/refused/counteroffered credit, changed terms/dates, failed rollover and interim shortage; compare values and later feasibility. | M0/R0 | TL-040, TL-053, TL-060 |
| 2 | Sketch a supported financing/commitment lever; show provisional 1,000/10,000-path targets, counts, coverage, current identity and offline replay; explicitly save a version. | R0 | TL-022, TL-023, TL-058 |
| 3 | With actor/controller version, initial private state, preferences, goals, policy settings, observations and randomness pinned, eligibility, previews, pre-resolution messages and pre-shock decisions match despite different hidden facts; single/batch/partition runs retain addressed draws. | R0 | TL-011, TL-043, TL-047, TL-059, TL-070 |
| 4 | Compute a saved sketch and a changed input on supported Windows/Linux without Office, a network calculation service or a server database. | R0 | TL-037, TL-039 |
| 5 | Interrupt publication around file/index boundaries and save from a stale tab; recover the last complete version and rebuild the index from manifests. | R0 | TL-032, TL-067 |
| 6 | Discover at least 1,000 policies/100,000 generated paths with actual independent refusals, adaptive choices, reported total budgets and fresh assessment. | R1 | TL-048, TL-049, TL-051, TL-056 |
| 7 | An enumerable multiobjective problem reproduces global and per-cell nondominated sets; bounded pruning and never/uncertain descriptor cases follow declared rules. | R1 | TL-048, TL-062 |
| 8 | A counterparty cooperates under its own goals; hostile stress has separate plausibility bounds. Lost advantage is sensitivity. A seeded real model defect needs a reproducible counterexample before an exploit label. | R1 | TL-063 |
| 9 | Keep rare/terminal histories and empirical shares in R1; R2 narration rejects an invented motive even if its event ID and number are correct. Offline structured summaries remain usable. | R1; narration R2 | TL-064, TL-065 |
| 10 | A detailed funding shortage invalidates a recorded commitment in forensic mode; policy re-evaluation produces a new linked action/response history under matched external worlds. | R2 | TL-061 |
| 11 | Import exact six files twice; preserve six identities, 17 run labels and 14 distinct inputs, conditions and aliases; compare 87 annual periods/73 metrics plus finer schedules. | R2 | TL-002, TL-028 |
| 12 | Fork a fixture's parameter from 1928, inspect removed loan/concession obligations, preserve C0 and keep absent North American denominators unavailable. | R2 | TL-007, TL-009, TL-019, TL-021, TL-035 |
| 13 | Apply a finance-skill proposal as validated model inputs and trace a detailed quantity to its source, derivation and instrument. | R2 | TL-010, TL-025 |
| 14 | Inject a broken cash/debt identity and an unconfigured cycle; show the terms/residual or cycle path without inheriting an old success badge. | R0; detailed R2 | TL-012, TL-014, TL-015 |
| 15 | Validate disputed/unknown consent, contradictory claims and succession: preserve institution-owned obligations, individual identities, valid dates and actor-specific beliefs. | R0 | TL-068, TL-069 |
| 16 | A pinned personal/institutional decision rule uses beliefs and competing commitments; its recorded reasons identify actual inputs and rejected alternatives. Changed relevant belief changes the choice; later attached motives cannot justify it. | R0 | TL-069, TL-070 |
| 17 | Two simultaneous offers compete for one resource; reordering actors/modules preserves registered allocation, settlement and release of refused reservations. | R0 | TL-076 |
| 18 | Bind lawful conduct to Pacifica and supported exceptional conduct to an independent counterparty; test strict rejection, apparent authority with delayed discovery, intentional breach and later cure without invented consent. | R0 | TL-071, TL-076 |
| 19 | Resume an unchanged decision state exactly, then fork a Pacifica decision, a dated premise and an imposed event separately; preserve prefix, hidden state and selection labels. | R0 | TL-072 |
| 20 | Open exploration surfaces a causally distinct dominated history before strategic pruning, supports a spontaneous bookmark and deduplicates numeric variants; R1 distinguishes witness, reliability and premise searches. | R0; bounded search R1 | TL-073, TL-062, TL-064 |
| 21 | Cross an institutional applicability boundary, propagate unavailable claims, then explicitly choose a registered provisional continuation with conditional results and preserved denominator. | R0 | TL-074 |
| 22 | Evaluate prepared and open-ended writing tasks plus a supported question withheld from tuning against notes/manual workflow; record new causal ideas, assumption disclosure, repair and author acceptance before expansion. | M0/R0; repeat R1 | TL-075 |
| 23 | Reports about March cash arrive out of order in June; current truth, target period, historical beliefs and immutable delivered payloads remain distinct. Overlapping resolved state conflicts fail validation. | R0 | TL-068, TL-070 |
| 24 | Substitute an officeholder while preserving institutional liabilities; decision authority, private beliefs and commitments follow explicit bindings. MetricSample data cannot enter the actor view without an Observation channel. | R0 | TL-017, TL-044, TL-069 |
| 25 | A run censored in 1930 leaves no-default-through-1932 unresolved; distinguish exhausted search from exhaustively proved infeasibility, and a rare supported witness from policy reliability. | R0 temporal evaluation; R1 search | TL-073, TL-055 |
| 26 | 100 root worlds with 20 unsupported parent paths and 20 provisional continuations retain 100 parent evaluations and 120 branch executions; separate conditional results, retries and cache reuse without inventing independent evidence. | R0 accounting; R1 assessment | TL-047, TL-055, TL-067, TL-074 |
| 27 | Two histories with similar financial outcomes but different frustrated plans remain distinct story candidates; numerical jitter of one conflict does not create another. Derived dramatic claims cite decisions and effects and never mutate the world. | R0 | TL-023, TL-073 |
| 28 | Compare valid and concealed invalid authority under additive conduct permissions with matched actor inputs: the attempt stays the same, legality/execution/disclosure differ appropriately, and a breach-capable counterparty can honour its agreement. | R0 | TL-071, TL-043 |
| 29 | Force a refusal: retain conditional consequences but do not claim controller generation. A separate plausibility assessment can qualify an isolated action intervention for consequence evidence; unsupported motives cannot. Regenerated policy/premise variants keep distinct claim scopes. | R0 classification; R1 search statuses | TL-069, TL-072, TL-073, TL-075 |
| 30 | Change cash premises, conduct bindings or fidelity while keeping policy/model versions fixed: experiment and evaluation keys change; display labels do not. Preserve valid matched root IDs and separate branch/retry accounting. | R0 identity; R1 aggregate use | TL-011, TL-055, TL-074 |
| 31 | From an enumerable allowed proposal family, open exploration generates and surfaces a distinctive dominated route missed by its declared strategic comparator under fixed budgets; no target ending or pre-inserted path is supplied. | R0; integrate strategic search in R1 | TL-073, TL-048 |
| 32 | Compare two independently plausible actions at one checkpoint with unchanged continuation rules and matched other inputs; trace the changed consequence and next dilemma, plus a low-effect contrast. Test intention-sensitive controller generation separately. | R0 | TL-069, TL-072, TL-075 |
| 33 | Hold continuation policy and all other mechanisms fixed while changing one plausible action; a separate policy-rule change must be labelled a policy comparison. Generation evidence and conditional consequence evidence cannot substitute for each other. | R0 | TL-069, TL-072, TL-075 |
| 34 | Activate a 1927 snapshot: the authored 1928 settlement is reference-only, an existing debt schedule remains due, and no actor knows later events by import. Re-import is idempotent; source correction creates a new bundle and dependency-impact report. | R0 | TL-077, TL-068, TL-038 |
| 35 | Preserve a locked unresolved culpability while characters react to supported testimony and suspicion. Import, sampling, queries and explanations cannot choose a secret culprit; a truth-dependent mechanism is withheld without suppressing valid unrelated behavior. | R0 | TL-068, TL-077 |
| 36 | A scoped private commitment, selective disclosure and belief update change a costly decision, cooperation and the next dilemma; two candidates remain causally distinct despite similar financial outcomes. | R0 | TL-042, TL-069, TL-073, TL-075 |
| 37 | Run and query under low RAM/disk budgets, adapt concurrency or stop cleanly, then recover. Preserve all outcomes/status counts and pinned replay/bookmark assets; measure process-tree peak memory and retained/temporary bytes. | R0 | TL-078, TL-059, TL-067, TL-032 |

## 8. Exchange and model contracts

Calculation/evaluation/branch packages share the canonical resolved_experiment_id, including premise state, policy/controller/actor/mechanism versions, conduct, fidelity, schemas/bindings, uncertainty/draw design and environment. Root-world IDs remain separate for compatible matching; exact calculation keys govern cache reuse. NarrativeQuery, StoryCandidate and StoryBookmark retain claim_basis and intervention lineage. Open exploration records proposal coverage separately from retained candidates. See the ontology contracts for canonicalization, admissibility and accounting rules.

R0 contracts use versioned typed declarations and explicit bindings. Structural generation in R2 may produce JSON Schema 2020-12, form scaffolds, result types and layout metadata; semantic migrations and execution rules remain reviewed code.

| Contract | Minimum contents |
|---|---|
| Resolved version | Commit/parent, source assets, complete inputs, authority/conditions and content hash |
| Quantity proposal | Stable target, units/basis, dates, parties, value/schedule, evidence, derivation, bounds and dependencies |
| Module/fidelity | Inputs/outputs, read/write ownership, units, transitions, dependencies, clock/solver, resource rules, runtime applicability, evidence/tests and aggregation/projection |
| Policy/actor | Observation-safe inputs/eligibility/messages, selected beliefs/goals/plans, own preferences, public policy knowledge, capabilities, profiles and supported attempts |
| Sketch | Version, narrow lever values, measures/coverage, world design, draw allocation and evaluation budget |
| Campaign | Objectives/constraints/descriptors, search/archive/pruning rules, sampling/stopping budgets and actor/structural alternatives |
| Rollout | Policy/world/input identity, environment, layout/bindings, draw addresses, observations/events, outcomes/checks and status |
| Detailed assessment | Forensic or policy-re-evaluation mode, original run and policy, detailed model, matched-world design, discrepancy rules and new lineage |
| Result manifest | Durable artifact hashes, completeness, definitions, statuses, covered/unavailable measures and replay assets |
| History/narration | Feature/clustering configuration, selection denominators, representative paths and typed event/motive/explanation records |
| Decision checkpoint/intervention | Complete world/actor/queue/obligation state or verified reconstruction; prefix/draw identity; decision, premise or imposed-event mode |
| Narrative query/candidate/bookmark | Explicit mode/quantification, temporal/search statuses, sampling/interventions, evidence/costs, population, supported dramatic view and spontaneous retained history/policy |
| Author review | Prepared/open/held-out writing tasks, manual comparator, novelty after assumption disclosure, judgments, retained ideas, timings, repair and acceptance |

MetricSample records key run, metric, entity/geography and period, with value or explicit missing reason, units/basis and population. Observation exclusively means information delivered to an actor through a channel. EvaluationPopulation distinguishes root worlds, policy-world evaluations, branch runs and retries with explicit membership, selection and weights; row count is not an inferred denominator. Shared definitions and retained bundles resolve old inputs without a live server.

Treat imports as data. Protect original bytes and hashes; unsupported majors fail without mutation. R2's fixture adapter preserves unknown source fields, labels and migration provenance. Spreadsheet formulas remain inert evidence, and no supported calculation delegates to Excel or a formula interpreter.

## 9. Proposed technology and execution design

| Layer | Recommendation | Boundary |
|---|---|---|
| Types/contracts | Minimal typed Python models and validated schemas in R0; structural generation where useful in R2 | Runtime mappings, behavior, migrations and interface decisions remain explicit |
| World versions | Git text, overlays and resolved-content hashes | Temporary edits need no Git branch; named saves guard the parent |
| Fast core | Profiled NumPy batching and Numba-compiled kernels on declared layouts | Compiled loops are allowed; no silent capacity overflow or hidden state sharing |
| Randomness | Philox or equivalent with versioned logical draw addresses | Pin transformations/builds/environment; a seed alone cannot promise partition independence |
| Reference/detailed accounts | Independent small cases in M0/R0; full instruments/Decimal postings in R2 | Separate forensic checking from policy re-evaluation; precision does not establish economic truth |
| Search | Multiobjective frontier and within-cell Pareto sets with explicit pruning | No hidden scalar elite or automatic algorithm choice by objective count |
| Responses | Own-interest best/near-best analysis plus separate hostile stress | Actor knowledge of Pacifica policy, unilateral/joint response assumptions and stress bounds are explicit |
| Assessment | Adaptive extra samples, fresh worlds and alternative structures | Initial 100-world screening cannot certify sparse tail risks |
| Results | Immutable Parquet, retained manifests, rebuildable DuckDB query catalog | Single coordinator; recovery spans files, catalog and guarded Git refs |
| Semantics and adjudication | Typed ontology, private actor state, explicit phases/reservations, profiles and applicability | Only the supported subset executes; no hidden feasibility leak or incidental-order allocation |
| Author workflow | Complete decision branches, narrative queries, durable bookmarks and author review | Selected stories and conditional experiments retain their own assessment semantics |
| Application | Local FastAPI and React/TypeScript with streamed summaries | Targeted forms/structured summaries first; general editing and optional LLM rendering in R2 |

See [model-architecture.md](model-architecture.md) for bindings, draw addresses, publication/recovery and fidelity contracts. The core consumes complete inputs and has no UI, network or storage dependency during transitions. Changing rule equations creates a model version; parameters remain typed data.

Read-only source extraction can obtain calibration/reference values. Every supported calculation runs natively from R0. Missing models remain explicit, and source workbooks are not a fallback runtime.

## 10. Quality targets and release gates

TL-078 makes resource admission and retention correctness requirements. Planning allowances are 10–30 GB for the first workspace, 50 GB free SSD space at installation, 16 GB host RAM for a bounded start and 32 GB recommended. They are unmeasured and do not guarantee the latency targets below. Account for application-wide memory, query spill and retained artifacts; batch worlds, preserve pinned evidence and stop cleanly at limits. See [capacity arithmetic and qualifications](data-population-plan.md#disk-and-memory-planning).

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
| M0 Define the dramatic question and prove the bounded model | Activate a traced 1927–1928 rescue/Concord content package and prove the bounded semantic prototype: protected ambiguity, temporal content roles, dated information, independent choice, additive conduct and resource settlement. Separate plausibility/controller/consequence evidence, demonstrate a relational chain and low-effect contrast, and measure real data-preparation effort plus peak memory/disk/latency before optimized interfaces. |
| M1 Deliver a useful bounded strategic sketchpad | Pass content activation, semantic/reference, isolated-action and resource-budget cases. Generate distinct open candidates, including a dominated route and relational alternatives with similar finances. Pass prepared/open/held-out author tasks with conditional evidence, assumptions and repair costs explicit. |
| M2 Discover strategies and narrative alternatives | After the R0 author gate, demonstrate assessed strategic search and distinct existential-history, policy-reliability and minimum-premise-change modes, correct temporal/search statuses and population accounting. Repeat causal discovery and author review with a fresh held-out task; targeted forms suffice. |
| M3 Extend authoring tools and detailed financial fidelity | Deliver the general editor, structural generation and optional grounded narration after the author workflow is established; satisfy full ledger forensic/policy-reassessment, fixture parity and deep provenance gates. |
| M4 Expand the supported world | Additional actors/regions/modules and semantic rebases pass their own evidence and behavior checks; any hosted mode is separately designed. |

No implementation calendar or measured benchmark is asserted. Data-population effort ranges are separate planning estimates in the population plan. Each in-scope acceptance and phase gate needs evidence; unresolved Must criteria require an explicit scope revision. R0 must pass the agreed author usefulness review as well as technical checks. R1 must demonstrate assessed strategy and bounded narrative-condition discovery. Author acceptance is recorded separately from technical validity; no automated story-quality score replaces it.

## 11. Decisions still open

Strategy discovery, multiple objectives, independent other actors, Excel independence and incorporation of the v0.5 review are confirmed. The design contracts below do not settle quantitative risks, character motives, behavioral coefficients, breach consequences or author narrative conditions.

| Decision | Status | Recommendation | Consequence |
|---|---|---|---|
| D-001 Product end goal | required by user | Support credible strategic sketches and plot exploration, then discover adaptive Pacifica strategies and histories satisfying declared author conditions. | Actor objectives and author narrative conditions remain separate; useful dominated histories may be retained without changing their strategic assessment. |
| D-002 Hosting and users | proposed | One author, loopback local browser application and headless native worker on supported Windows/Linux environments. | Hosted/multi-user mode needs its own access, storage and concurrency design. |
| D-003 Bounded pilot question | proposed | Use the 1927–1928 Japan rescue and Concord dilemma for the first content package, with few active decision-makers, selected commitments/information and material monthly cash. | M0 fixes the exact start phase, horizon, mechanisms and dependency closure; the canonical 1928 outcome is a reference unless explicitly selected as an author condition. |
| D-004 Performance and sampling budgets | proposed unmeasured | Target 1,000 sketch paths in 1 second at p95, 10,000 in 10 seconds, and 100,000 base evaluations in 5 minutes on 8 workers/16 GB. Benchmark realistic queues/checks/logs/delivery before commitment. | Keep throughput targets provisional. Budget memory across processes and disk across retained/temporary artifacts; measure on the 16-GB benchmark and recommend 32-GB RAM with 50-GB free SSD space for comfortable author use, subject to retention. |
| D-005 Fixture distribution | proposed | Stage exact frozen files and provenance in versioned private artifact storage before R2; pin calibration/reference evidence needed for R0 earlier. | No legacy adapter runtime or Office dependency; metadata alone is not the six result files. |
| D-006 Success and scope boundaries | open | Use the objective sheet and researched families; enable only covered measures and explicitly named proxies. | Final beneficiaries, thresholds and acceptable risk remain open; no mandatory national-power score. |
| D-007 Storage foundation | proposed | Git-versioned validated text, immutable Parquet artifacts, retained manifests and a single-process DuckDB query catalog. | The index is rebuildable; durable publication/recovery spans files, manifests and guarded Git refs. PostgreSQL is a future hosted option. |
| D-008 Excel independence | required by user | Every calculation executes native modules without Office or spreadsheet-formula fallback from R0. | Source workbooks are read-only evidence; missing mechanisms remain explicit. |
| D-009 Multiple objectives and strategy diversity | confirmed multiobjective proposed archive details | Keep the global frontier and a bounded nondominated set per behavior cell with explicit pruning; no hidden scalar best-per-cell score. | Cell capacity, descriptor summaries and pruning rules need selection; archive diversity does not establish robustness. |
| D-010 Agency and response assessment | confirmed pacifica control proposed assessment details | Control Pacifica decisions only. Model others' own-interest responses, then separately stress hostile but plausible near-best responses. | Changed advantage means sensitivity; an exploit finding needs an identified model defect. Response bounds and hostility assumptions remain explicit. |
| D-011 Objective contracts and risk | open | Choose a small objective set with beneficiary, geography, time/risk aggregation, thresholds and evidence; apply coverage gates from the first sketch. | Early proxies retain their own names; proposed Q10/Q90 and buffer/risk choices are not approved targets. |
| D-012 Horizon and temporal resolution | proposed | Use a bounded question within 1904–1932 and retain 1846–1932 financial fixtures for R2; resolve monthly/finer timing when it changes feasible commitments. | A shorter actual first slice is acceptable if declared; performance cannot be claimed at an untested resolution. |
| D-013 Fidelity and policy reassessment | proposed | Share mechanism definitions and explicit projections. Use small independent financial reference checks in M0/R0; full detailed ledger supports forensic checking and separate policy re-evaluation in R2. | Discrete feasibility reversals are material even within a baseline band. Detailed re-evaluation creates a new linked path and may change later actions. |
| D-014 Narration | proposed | R0/R1 use structured timelines and deterministic summaries. Optional LLM narration follows in R2, grounded in typed event, motive and causal records. | The author usefulness gate precedes prose tooling. Provider/cost/review details remain open; narration does not add world facts. |
| D-015 Catalog format and declarations | open | Use ontology.md and the structured ontology contract for semantic identities and invariants; minimal validated types and explicit bindings execute the bounded slice. General structural generation follows in R2. | Choose YAML or TOML later; storage choice does not supply semantics. Future schemas/validators must implement the ontology contracts. |
| D-016 Behavior descriptors and archive capacity | open | Select two or three interpretable behavior descriptors aggregated over a common world design, including never/undefined outcomes and assignment uncertainty; keep per-cell Pareto representatives. | Cell boundaries, summaries, capacity and deterministic diversity-pruning must be declared and tested without a hidden utility score. |
| D-017 Author narrative conditions | incorporated design parameters open | Use an independently budgeted open proposal method and pre-pruning selector in R0; R1 adds distinct narrative search modes with actor-generated versus mechanical-consequence claim admissibility. | Specify bounded proposal coverage and retention separately. A forced choice may be a useful conditional idea but cannot certify actor-generated discovery. |
| D-018 Semantic and intention scope | incorporated design subset open | Register predicate/state/time semantics and immutable revisions; bind choices to a DecisionContext and executed DecisionRecord using selected beliefs, goals and commitments. | M0 separates alternative plausibility, actual controller selection and isolated one-action effects; protects deliberate ambiguity and activates only sourced or explicitly assumed content. |
| D-019 Legality and adjudication profiles | incorporated design mechanisms open | Bind additive permitted-conduct sets by actor/action family; all profiles permit lawful execution, supported exceptions add possibilities, and actual legality remains independently adjudicated. | M0 defines one exceptional-conduct family, its variant-specific coverage and discovery rules; enabling breach never compels misconduct. |
| D-020 Decision point interventions | incorporated design | Provide decision, premise and imposed-event branch modes with complete state reconstruction, dated information and immutable prefix lineage. | Ordinary optimization controls only Pacifica. Overrides and imposed outcomes retain conditional lineage and cannot certify actor-generated success; regenerated changed premises have their own evidence scope. |
| D-021 Applicability and provisional continuation | incorporated design envelopes open | Check mechanism validity envelopes during execution. Allow explicitly selected registered provisional assumptions as linked conditional continuations. | Invalidity propagates to dependent claims; conditional and structural-model populations are not silently pooled into certified rankings. |
| D-022 Creative usefulness gate | incorporated design protocol open | Agree prepared, open-ended and held-out writing tasks plus a manual-workflow comparator; demonstrate causal novelty and author usefulness before expansion. | Review generated intention-sensitive decisions and separately supported conditional causal contrasts, relational novelty and a low-effect case; manual comparison and held-out tasks remain required. |

Material risks include unsupported behavior, inadequate objective or narrative definitions, hidden information through interfaces, discarded interesting paths, silent extrapolation, inaccurate decision-state reconstruction and false probability claims. Use bounded mechanisms, explicit semantic contracts, independent tests, preserved selection modes and direct author evaluation.

## 12. Source and authority notes

U16 requests revision 0.9 and the existing draft PR update, population estimates and disk/RAM expectations. S15 records the review of v0.8 commit `b98837ac0c0be3f3cd183c8060b8ce78fcf1b355`; S16 records capacity planning, which is estimated rather than benchmarked. Four review issues and the population/resource additions map to requirements and documents in backlog.review_traceability. The new [population plan](data-population-plan.md) pins its measured source corpus separately from inferred effort.

U15 requests revision 0.8 and the existing draft PR update. S14 records the review of commit `4a0dd6367cd23d3f4cc0bd7cecbcd489095ac730`; its five substantive recommendations and the decision-equivalence correction map to existing requirements. Earlier review mappings remain in backlog review history.

[backlog.json](backlog.json) preserves pinned project sources and the supplied revision 0.4 input hashes. U13 records the request to incorporate the v0.5 review into v0.6 and update the existing PR. S11 records that review against commit `f0da5c000541352ccbfd2a49264614a248af8eb6`; S12 supplies the narrative-planning precedents for intentions, beliefs and conflicting plans. Their centralized planning algorithms are not adopted as actor controllers.

U14 requests revision 0.7 and the existing draft PR update. S13 records the critical review of commit `30b6f11b2e0dbd965fcb5f9101fc65045e7689a0`; its nine recommendations map to strengthened existing requirements. The v0.6 traceability is retained in backlog review history.

The baseline remains `cc6e017780970433ab63bc95d0e3749510b44d49`; alternatives remain `626ffbb0bd6486c19164f89104569d78321ebd55`. Original sources, the supplied workbook and [fixture manifest](fixture-manifest.json) retain their identities. The [objective sheet](objectives-and-constraints.md), [action/actor catalog](action-and-actor-catalog.md), [ontology](ontology.md) and [structured catalog](draft-model-catalog.json) are synchronized design definitions.

Revision 0.9 vision, architecture, ontology, requirements and backlog form one proposal. The backlog's review traceability maps each accepted recommendation to requirements and documents. Product/model review is separate from narrative adoption; generated paths, personal motives, calculations and narration do not approve canon.
