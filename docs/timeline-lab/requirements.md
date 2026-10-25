# Pacifica Timeline Lab requirements

**Draft for review · 25 October 2026 · Requirements version 0.3**

Timeline Lab is a strategic simulation and policy-search tool. It should generate thousands of possible histories, discover adaptive Pacifica strategies and compare distributions of several success variables. The author controls Pacifica; other actors respond through their own objectives, information and constraints.

The [product vision](product-vision.md) defines this end goal, the researched measurement framework and the intended user experience. The six authored timelines are financial regression references and comparators, not the space of possible outcomes.

Strategy discovery, multiobjective trade-offs, independent other actors and Excel-free execution are confirmed requirements. Exact success measures, thresholds, actor mechanisms, uncertainty distributions and pilot boundaries still need definition. Database and UI choices remain provisional until those contracts and the native model's performance are understood.

## 1. Product purpose and users

The primary user is the Pacifica author, who needs to:

- Define success, constraints and the decisions available to Pacifica.
- Generate new paths without writing their outcomes in advance.
- Search for adaptive policies across uncertain futures and independent actor responses.
- Compare prosperity, security, fiscal resilience and other selected outcomes as distributions and trade-offs.
- Inspect the choices, assumptions, resource bottlenecks and failure conditions behind a policy.
- Replay a selected path and export a reproducible strategy or draft storyline.

The model maintainer defines dynamics, actor-response models and evidence. The finance skill proposes quantities and derivations. These are workflow roles, not a requirement for multi-user permissions in the pilot.

The product performs counterfactual simulation and decision analysis. Monte Carlo estimates outcomes under a specified policy and uncertainty model; optimization searches over policies. It must not choose a lucky random path and call it the best strategy.

Success means that the author can start from a world state and success definition, discover new conditional strategies, inspect their assessed trade-offs and replay their successes and failures. A six-case viewer or calculator alone does not satisfy the goal.

## 2. Evidence and current state

The baseline is pinned to repository main commit `cc6e017780970433ab63bc95d0e3749510b44d49`. The alternatives are pinned separately to `626ffbb0bd6486c19164f89104569d78321ebd55`. The proposal file `CR-032.md` supplies the case labelled A; B, C and D remain separate alternatives. See the [pinned proposal index](https://github.com/c-voelkle/pacifica/blob/626ffbb0bd6486c19164f89104569d78321ebd55/book-agent/revision/alternatives/CR-032/README.md).

The existing [Ledger reference](https://github.com/c-voelkle/pacifica/blob/cc6e017780970433ab63bc95d0e3749510b44d49/finance/Pacifica-Ledger.md) describes a CR-021 rev8 display snapshot. It supplies useful dashboard domains, but its numbers are not the current experiment baseline. Its live interface was not inspected for this specification.

Six local JSON bundles now contain 87 annual periods, 1846–1932, and 73 annual metrics. They total 25,473,049 bytes and contain 17 labelled run records with 14 distinct input hashes. Baseline, control and A each reuse their native input for the matched-downturn label; these are not additional independent calculations.

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

[fixture-manifest.json](fixture-manifest.json) records exact file hashes, sizes, variants and selected 1932 values. The six result files and supporting adapter scripts are local project outputs and are **not included in this requirements commit**. Their exact bytes must be staged in versioned project storage before regression implementation begins.

## 3. Scope of the first release

The first usable release is a bounded but complete strategy-discovery pilot. It includes an action catalog, independent actor responses, uncertain world evolution, adaptive policies, repeated evaluation, multiobjective search, held-out assessment, explanation and replay.

The pilot must still provide the existing financial requirements: source pinning, imports, immutable versions, quantity proposals, accounting identities, geographic/ownership boundaries and export. These support the strategic model.

| Capability | First-release behavior |
|---|---|
| Problem definition | Pin objectives, constraints, beneficiaries, horizon and uncertainty semantics. |
| Pacifica action catalog | Generate feasible decisions with costs, delays, authority, physical limits and supported effects. |
| Financial/programme mechanisms | Recalculate spending, loans, debt, claims, income and supported investment effects. |
| Diplomacy and other actors | Model offers, refusals, counteroffers and commitments under independent interests and constraints. |
| Strategic capability | Connect usable forces, mobilisation, supply, access and relevant political support to feasible commitments. |
| Policy search | Generate conditional strategies and assess each across many futures; no authored ending is required. |
| Assessment and export | Present trade-offs, downside, coverage and failure conditions, with reproducible policy/path export. |

A 1904–1932 decision window is proposed for the pilot; exact actors, geography and action families remain open. Finer crisis/logistics steps may be necessary within annual strategic reporting. The 1846–1932 financial fixture horizon remains a separate regression obligation.

Register new event and response families through explicit model contracts. CR numbers identify sources and fixtures, not the engine's branching rules. If a mechanism or objective is unsupported, identify the coverage gap before the optimizer can benefit from it.

Later scope includes broader geography, additional actor types and mechanisms, richer national accounts and rebase/conflict resolution. Real-time collaboration, automatic canon integration and a universal tactical simulation are outside the pilot. Stochastic evaluation and strategy search are core first-release capabilities.

## 4. Domain model

Use stable identities and an immutable snapshot plus dated overlays. PostgreSQL is the proposed store for typed world data, accounts and run evidence; versioned Python modules own the state transitions and calculations. A complete input bundle must run without a live database or dashboard. The [product vision](product-vision.md) governs the goal and measurement design; [model and database architecture](model-architecture.md) describes the provisional implementation. The event/dependency structure is a logical model; it does not require a graph database.

| Object | Meaning and required distinction |
|---|---|
| Source snapshot | Pinned narrative documents, workbook/data hashes and their authority status. A newer main does not replace an existing snapshot. |
| Entity and geography | Sovereign, Treasury, firm, syndicate, lender, borrower or territory, with ownership and jurisdiction valid over stated dates. |
| Event/change | A dated set, add, remove, shift or replace operation targeting a stable ID, with preconditions and declared effects. |
| Instrument/right | Loan, bond, grant, concession, guarantee or treaty entitlement with counterparties, effective dates, cash flows and termination rules. |
| Assumption/quantity proposal | A value or schedule, evidence class, source, derivation, bounds and explicit uncertainties. Unknown is distinct from zero. |
| Scenario | A starting-world configuration with authority, conditions and assumptions; an authored path may be retained as a comparator. |
| Scenario version | An immutable parent reference, overlay and applied assumption set. A working draft becomes a new version when saved for a run. |
| Experiment/search campaign | A declared question, objective set, decision space, actor/uncertainty models, horizon, optimizer configuration and evaluation budget. |
| Policy | Versioned conditional rules mapping Pacifica's observed history to feasible actions; fixed plans are labelled comparators. |
| Actor model | Another actor's objectives, observations, capabilities, constraints and response rules. |
| Information state | What an actor can observe or infer at a decision point, distinct from the simulation's hidden state and future draws. |
| Uncertainty specification | Stochastic processes, parameter ranges, structural alternatives, dependence assumptions and probability status. |
| Objective set | Selected success metrics, directions, thresholds, time/future aggregation and evidence requirements. |
| Run/rollout | One generated trajectory under a policy and world realization, with immutable inputs, random-stream identity, observations, actions, outputs and checks. |
| Policy assessment | Aggregated outcomes across rollouts, estimated trade-off position, held-out evidence and uncertainty. |
| Observation/check | A typed quantity for an entity and period, or an evaluated identity/constraint with its residual, tolerance and coverage. |

```mermaid
flowchart LR
    Sources["Pinned world and mechanisms"] --> Campaign["Objectives, actions and uncertainty"]
    Campaign --> Search["Generate Pacifica policies"]
    Search --> Worker["Native world simulation"]
    Actors["Independent actor models"] --> Worker
    Worker --> Evaluate["Outcome distributions and checks"]
    Evaluate --> Search
    Evaluate --> Assess["Held-out assessment"]
    Assess --> Dashboard["Trade-offs, explanations and replay"]
```

The finance skill proposes; the native engine computes reproducibly for fixed models, inputs and random streams. A run must not ask a language model to invent a missing value midway through calculation. The author may apply a validated batch of MODEL assumptions without a separate approval prompt for every cell.

## 5. Financial and temporal semantics

Every metric must identify its entity, geographic boundary, currency/unit, nominal or real price basis, period, quantity kind (stock, flow, rate, ratio or index) and aggregation rule. Core Pacifica GDP, Japanese output, Russian output and network GDP remain separate. Real GDP uses the stated base year; nominal Treasury flows cannot be compared directly with real GDP without a declared conversion.

Account for spending, lending principal, repayments, interest, asset acquisition, losses and financing separately. Avoided expenditure is not automatically additional GDP. Private or foreign syndicated lending is not all Treasury property. A removed or expired concession must lose its associated rights and receipts unless another event independently creates them.

Annual summaries sum flows and take the stated endpoint for stocks; ratios are recomputed from compatible components. Monthly liquidity schedules remain available because annual totals can hide a cash shortage. Finer timing must not be implied where the model only supports annual dates.

Run checks must cover budget/cash reconciliation, debt roll-forward, claims, lender-borrower schedules, timing and each supported resource constraint. A balanced accounting identity can coexist with an unfunded programme. Unsupported capital, FX, personnel or transport limits must be labelled unmodelled.

Date-aware evaluation is mandatory. The pilot's 1923 earthquake-loan dependency and 1928 Union-capacity sensitivity are regression examples: a later assumption must not alter earlier periods without a declared anticipation effect. A same-period cycle requires an explicit solver and convergence criteria or a clear failure.

C's 1932 output relies on its named C0 peaceful commercial continuation. D's institutions must not fill C's unresolved branches. D's North American defence/debt targets cannot be certified using core Pacifica GDP; unavailable denominators produce unavailable checks, with proxy ratios separately labelled. Complete net external claims are also not yet supplied.

The interface must maintain separate states for narrative authority, evidence quality, job execution, accounting validation, funding feasibility and model coverage. A completed computation may describe an infeasible or conditional draft.

## 6. Dashboard and authoring workflow

The main journey is **define objectives → choose decision space and uncertainty → search → inspect trade-offs → assess failures → replay → refine or export**.

| View | Author's task |
|---|---|
| Problem | Define objectives, constraints, controlled decisions, horizon and model coverage. |
| Search | Start, inspect, pause/resume and budget policy/world evaluations. |
| Trade-offs | Explore the estimated Pareto set, objective distributions, downside and joint target attainment. |
| Policy | Inspect conditional rules, actor responses and conditions associated with success or failure. |
| Timeline | Replay a selected generated path, separating Pacifica decisions, other actors and chance events. |
| Accounts | Inspect financial identities, claims, cash, resources and terminal obligations. |
| Evidence and checks | Inspect sources, assumptions, model validity, funding gaps and unsupported dimensions. |

The existing six cases remain available as comparators. Detailed line charts may limit simultaneous series for readability, but that limit must not constrain campaign size.

Selecting a quantity exposes its definition, policy/run identity, formula/module, assumptions and sources. Workbook mappings remain technical provenance. Charts require equivalent tables and statuses that do not rely on color.

Changed inputs mark results stale. Search results remain attached to their original objective, policy and model versions. Changing weights, bounds or distributions may require new evaluation; incompatible outputs cannot be silently reranked.

“Explain difference” shows changed decisions and dependency paths. Additive account decompositions must reconcile. Sensitivity associations must not be relabelled causal effects; controlled reruns require valid matched uncertainty.

Hold exogenous shocks constant where comparisons permit it while recomputing endogenous effects and actor choices. Distinguish assumed probability distributions, exploratory ranges and structural alternatives. Missing probabilities must not be invented to make a chart look complete.

## 7. Requirements and acceptance register

The normative individual statements, source links, dependencies and Given/When/Then criteria are in [backlog.json](backlog.json). The register contains 57 requirements: 55 Must requirements for R1 and two Should requirements for R2. Strategy discovery, multiobjective comparison, independent actor agency and Excel independence are user requirements; detailed acceptance thresholds remain proposed. Their acceptance criteria describe future verification; none has been satisfied merely by writing this specification.

| Requirement | Capability | Proposed priority/release | Acceptance |
|---|---|---|---|
| TL-001 | Pin every experiment | Must / R1 | AC-001 |
| TL-002 | Import the six bundles | Must / R1 | AC-002 |
| TL-003 | Define quantities explicitly | Must / R1 | AC-003 |
| TL-004 | Separate approval from calculation | Must / R1 | AC-004 |
| TL-005 | Fork without changing history | Must / R1 | AC-005 |
| TL-006 | Use dated semantic changes | Must / R1 | AC-006 |
| TL-007 | Track dependencies | Must / R1 | AC-007 |
| TL-008 | Review rebases and conflicts | Should / R2 | AC-008 |
| TL-009 | Handle unresolved continuations | Must / R1 | AC-009 |
| TL-010 | Integrate the finance skill | Must / R1 | AC-010 |
| TL-011 | Make runs reproducible | Must / R1 | AC-011 |
| TL-012 | Respect time and detect cycles | Must / R1 | AC-012 |
| TL-013 | Control calculation jobs | Must / R1 | AC-013 |
| TL-014 | Show fresh results accurately | Must / R1 | AC-014 |
| TL-015 | Reconcile the accounts | Must / R1 | AC-015 |
| TL-016 | Expose resource constraints | Must / R1 | AC-016 |
| TL-017 | Preserve ownership and geography | Must / R1 | AC-017 |
| TL-018 | Aggregate time correctly | Must / R1 | AC-018 |
| TL-019 | Compare like with like | Must / R1 | AC-019 |
| TL-020 | Run bounded sensitivities | Must / R1 | AC-020 |
| TL-021 | Explain differences honestly | Must / R1 | AC-021 |
| TL-022 | Compare the main trajectories | Must / R1 | AC-022 |
| TL-023 | Inspect the timeline | Must / R1 | AC-023 |
| TL-024 | Edit decisions and model assumptions | Must / R1 | AC-024 |
| TL-025 | Trace any displayed number | Must / R1 | AC-025 |
| TL-026 | Export a reproducible experiment | Must / R1 | AC-026 |
| TL-027 | Protect sources and validate execution inputs | Must / R1 | AC-027 |
| TL-028 | Validate the native engine against frozen evidence | Must / R1 | AC-028 |
| TL-029 | Keep the initial lab private | Must / R1 | AC-029 |
| TL-030 | Meet measured responsiveness targets | Must / R1 | AC-030 |
| TL-031 | Make comparisons readable and accessible | Must / R1 | AC-031 |
| TL-032 | Recover without corrupting work | Must / R1 | AC-032 |
| TL-033 | Register models and capabilities | Must / R1 | AC-033 |
| TL-034 | Extend the world state | Should / R2 | AC-034 |
| TL-035 | Evaluate policy limits with valid denominators | Must / R1 | AC-035 |
| TL-036 | Version the data contract | Must / R1 | AC-036 |
| TL-037 | Run without Excel | Must / R1 | AC-037 |
| TL-038 | Persist a versioned domain model | Must / R1 | AC-038 |
| TL-039 | Separate calculation from persistence and presentation | Must / R1 | AC-039 |
| TL-040 | Separate accounting identities from economic assumptions | Must / R1 | AC-040 |
| TL-041 | Define success before search | Must / R1 | AC-041 |
| TL-042 | Generate legal decisions from an action catalog | Must / R1 | AC-042 |
| TL-043 | Search adaptive policies without future knowledge | Must / R1 | AC-043 |
| TL-044 | Represent independently responding actors | Must / R1 | AC-044 |
| TL-045 | Model strategic capability and sustainment | Must / R1 | AC-045 |
| TL-046 | Represent uncertainty explicitly | Must / R1 | AC-046 |
| TL-047 | Evaluate policies across repeated generated futures | Must / R1 | AC-047 |
| TL-048 | Search a set of multiobjective strategies | Must / R1 | AC-048 |
| TL-049 | Test finalists on unseen futures and actor models | Must / R1 | AC-049 |
| TL-050 | Explain strategic strengths and failures | Must / R1 | AC-050 |
| TL-051 | Run large campaigns within a declared budget | Must / R1 | AC-051 |
| TL-052 | Explore outcome distributions and trade-offs | Must / R1 | AC-052 |
| TL-053 | Establish model credibility for its intended use | Must / R1 | AC-053 |
| TL-054 | Replay and export a discovered strategy | Must / R1 | AC-054 |
| TL-055 | Score distributions without hiding their assumptions | Must / R1 | AC-055 |
| TL-056 | Demonstrate discovery without prewritten outcomes | Must / R1 | AC-056 |
| TL-057 | Gate metrics on usable evidence and coverage | Must / R1 | AC-057 |

Additional end-to-end demonstrations connect the requirements:

1. **Import and inspect:** import the exact six files twice. Show six identities, 17 run records and 14 distinct inputs; preserve original bytes. Select 1932 GDP and debt and reconcile with the manifest, then check the full annual series.
2. **Fork and date an edit:** fork D, change a registered financing-capacity parameter from 1928, and rerun. The original remains unchanged, earlier values remain equal and all affected schedules update. Export/reimport retains both versions.
3. **Remove an instrument:** remove a supported loan or concession-producing event. Its claims, interest, repayments, losses and rights appear in the impact preview and cease according to the declared rules. An unmapped consequence prevents a complete-result claim.
4. **Preserve C's condition:** compare C0 with D. The condition remains visible in charts, inspectors and exports; missing C assumptions never become zero or inherited D benefits.
5. **Separate shocks from responses:** compare native and matched external-shock runs. Inspect which shock inputs were held fixed and which endogenous rescue or credit effects changed.
6. **Diagnose a failure:** inject a broken debt roll-forward and an unconfigured calculation cycle. Show the entity/period/identity residual or cycle path, preserve the last successful run and avoid publishing partial output as complete.
7. **Respect financing semantics:** apply D's adverse Union case. Capacity changes start in 1928, bond cash proceeds use the stated issue-price factor rather than face value, and absent North American denominators remain unavailable.
8. **Use the skill contract:** import a quantity proposal for a new supported programme, inspect its derivation and bounds, apply it as a batch, run and trace a resulting Treasury quantity back to the proposal.
9. **Prove native execution:** export resolved inputs, stop the application and database, and run a supported new change from the command line on Windows and Linux without Office. Results reconcile with application-driven runs; no cached fixture or workbook fallback substitutes for computation.

10. **Discover a strategy:** start from a world state and action catalog with no authored future. Generate adaptive policies, independent refusals/counteroffers and at least 100,000 pilot paths; assess a multiobjective trade-off set on held-out worlds and replay failures.

## 8. Exchange and model contracts

Adopt a machine-validated contract independent of workbook layout. Use [JSON Schema 2020-12](https://json-schema.org/draft/2020-12) for the exchange definition, with explicit migrations and model capability versions. The formal product schema is implementation work; the current pilot format is provisional.

| Contract | Minimum contents |
|---|---|
| Scenario version | Stable ID, parent, pinned baseline, event overlays, assumption set, source references, conditions and authority. |
| Quantity proposal | Target ID, value/schedule, units and price basis, dates, entities/counterparties, evidence class, source references, derivation, bounds and dependencies. |
| Module capability | Inputs/outputs and units, state transition, dependencies, supported operations, period resolution, constraints and checks. |
| Policy/actor model | Decision rules, observation limits, own objectives, constraints, module versions and supported actions. |
| Campaign/rollout | Objective set, policy family, optimizer configuration, evaluation budget, actor/uncertainty models, random-stream allocation, resolved-input hashes, execution states and artifact references. |
| Result catalog | Metric definitions plus typed observations, schedules, checks, coverage, conditions and provenance; no required worksheet address. |

A normalized observation can be keyed by run, metric, entity/geography and period, with value and missing-value reason. Large shared definitions should be stored once and referenced, while each export remains replayable with declared dependencies.

The pilot adapter must preserve the source files, unknown fields and original run labels, migrate supported content losslessly and reject unsupported schema majors without modifying the catalog. “Replayable” means it states required external assets and workers; the JSON results alone do not contain a portable executable model.

Imports are data. Uploaded scripts and spreadsheet formulas remain inert provenance. Read-only workbook inspection may extract source evidence during migration; every Lab calculation must execute native model modules without Excel or a spreadsheet formula runtime.

## 9. Proposed technology and execution design

The [product vision](product-vision.md) specifies a strategic world simulator plus policy search. The provisional [model and database architecture](model-architecture.md) retains a native stock-and-flow foundation. State includes cash, debt, claims, capital and other supported world quantities. Dated events and explicit rules generate changes; economic responses remain distinguishable from accounting identities.

| Layer | Recommendation | Reason |
|---|---|---|
| World data and run catalog | PostgreSQL with typed relational tables and versioned migrations | Persist entities, assumptions, events, instruments, accounts and immutable run evidence with structural integrity. [PostgreSQL constraints](https://www.postgresql.org/docs/current/ddl-constraints.html). |
| Native simulation core | Versioned Python world and actor modules | Generate trajectories reproducibly from policies, observations and uncertainty without Excel or live database access. |
| Policy search and assessment | Bounded multiobjective search and repeated evaluation | Generate new strategies, retain trade-offs and assess finalists on held-out worlds; implementation candidates are discussed in product-vision.md. |
| Application API | FastAPI and Pydantic | Validate requests, resolve scenario versions and orchestrate jobs. [FastAPI features](https://fastapi.tiangolo.com/features/). |
| Interface | React, TypeScript and Vite | Typed scenario forms and reusable comparison views. [React TypeScript guidance](https://react.dev/learn/typescript); [Vite guide](https://vite.dev/guide/). |
| Charts | Apache ECharts, with matching HTML tables | Multiple trajectories and interactive inspection. [ECharts documentation](https://echarts.apache.org/en/index.html). |
| Exchange | JSON Schema 2020-12 and immutable input/result artifacts | Portable replay and explicit migration boundaries. |
| Legacy evidence | Source workbook and frozen pilot JSON | Read-only extraction and regression references; never a runtime or fallback calculation engine. |

PostgreSQL is a proposed choice, not a deployed service. It adds installation, migration and backup work. SQLite remains adequate for a deliberately local product; selecting it would not change the requirement for a native engine. Choose one storage backend, and keep the calculation interface independent of it.

**Every supported calculation must run without Excel from the first usable release.** No Office COM worker, remote spreadsheet service or automatic spreadsheet-formula interpreter is permitted as the execution path. A missing native module produces an explicit coverage gap.

The database stores the world, policies and evaluation evidence; the engine advances the world through time, and the search layer generates and assesses candidate policies. SQL constraints and application transactions protect records, while Python modules define accounting, contracts and economic responses. Shared entity and instrument revisions must be immutable so that later corrections cannot alter an old run.

The calculation pipeline resolves overlays and assumptions into a complete portable bundle, validates units and coverage, constructs dated dependencies, runs modules, evaluates checks and atomically publishes immutable results. Cache identity includes resolved world inputs, policy and actor-model versions, source/model/engine versions, uncertainty specification and random-stream allocation. Display labels and timestamps do not define calculation equivalence.

Start with objective definitions, feasible actions, actor information and evidence-backed dynamics. Prove a bounded native kernel, then repeated evaluation and search, before the full dashboard. Workers should batch results and retain compact summaries plus replay inputs; large trajectory artifacts may use columnar storage. Detailed schema and execution choices follow profiling of this workload.

## 10. Quality targets and release gates

The following are proposed acceptance targets, subject to D-004, not measurements of an existing application:

| Dimension | Proposed target |
|---|---|
| Import | Entire 25.5 MB pilot set within 5 seconds at p95 on a documented reference machine. |
| Interaction | Cached comparison/year/reference updates within 250 ms at p95. |
| Search throughput | Proposed: 1,000 distinct candidate policies and 100,000 bounded-pilot trajectories within 30 minutes on 8 CPU workers and 16 GB RAM. Unmeasured; validate or revise explicitly before commitment. |
| Progress | Stage/progress heartbeat at least every 15 seconds; cancellation and bounded execution. |
| Benchmark method | UI/import: at least 20 measured trials after warm-up. Campaigns: three complete measured trials after warm-up, with model fidelity, hardware, policies, worlds, rollouts, memory, storage and failure counts recorded. |
| Usability | Core workflow usable at 1280×800 by keyboard, with visible focus, textual errors and chart-equivalent tables. |
| Recovery | Transactional saves and result publication; process interruption or two editing tabs cannot overwrite newer versions. |

Numeric comparison uses `abs(actual − reference) ≤ max(absolute tolerance, relative tolerance × abs(reference))`. Start with an absolute tolerance of 0.000001 for monetary observations expressed in millions and a relative tolerance of 1e-9; ratios expressed as fractions use 1e-10 absolute and 1e-9 relative. Dates, IDs and integer counts require exact equality. Scale accounting residual checks by the largest term in the identity. Additional metric kinds require a declared tolerance before regression; any metric-specific exception must be versioned and explained.

The native-engine release gate compares all 87 annual periods and 73 metrics in every pilot run, plus supplied finer schedules and conditions. Independent accounting tests are also required: reproducing a spreadsheet error is not evidence of model correctness. Intentional corrections need an explicit version and reconciliation note. Both frozen cases and new input variations must calculate on supported Windows and Linux environments without Office. The first usable release must also pass the strategy-discovery demonstration and independent mechanism checks. Financial regression alone cannot validate actor behavior or predicted probabilities.

| Milestone | Exit evidence |
|---|---|
| M0: Define the strategic problem | Confirm the measurement catalog, actor roles, controllable actions, observation rules, horizon, uncertainty semantics and evidence needs. Pin the six financial fixtures as engineering references. |
| M1: Build and verify the native world kernel | A bounded world advances under Pacifica and independent actor decisions; financial, sustainment, timing and information constraints are tested without Excel. Saved fixtures are reconciled separately. |
| M2: Discover and assess strategies | The search generates policies, evaluates repeated futures, estimates the trade-off frontier, tests finalists on unseen worlds and passes the documented campaign benchmark. Trivial and small exhaustive cases expose optimizer errors. |
| M3: Deliver the strategic exploration dashboard | Users define objectives, start searches, inspect trade-offs and risk, replay paths and export policies. The discovery demonstration passes; a six-case viewer alone cannot satisfy release. |
| M4: Expand the model domain | Additional regions, actor types and event families pass their own evidence and behavior checks while using the same strategy/rollout contracts. |

No calendar estimate is asserted here. M0 must define the decision problem and reveal evidence, actor-response and model-coverage gaps before implementation estimates are made. Release requires evidence for every in-scope acceptance criterion, a recorded disposition of failures and an explicit scope revision for any deferred Must requirement.

## 11. Decisions still open

The end goal, multiobjective mode, Pacifica-only control and Excel independence are confirmed. Metric definitions, limits, horizon and implementation details remain open or proposed as indicated in backlog.json.

| Decision | Recommended default | Consequence |
|---|---|---|
| D-001: Product end goal | Discover adaptive Pacifica strategies across thousands of generated histories, compare outcome distributions and trade-offs, and inspect failures. The six cases serve as regression references. | A scenario viewer or six-case calculator does not satisfy the product objective. |
| D-002: Hosting and users | One author, private local browser UI and loopback API, with a native worker that also runs without a desktop on Linux. | Hosting and multi-user access remain open; neither option may introduce an Excel runtime dependency. |
| D-003: Bounded pilot mechanisms | Choose a coherent pilot spanning financing/investment, diplomatic commitments and strategic readiness/sustainment, with independent actor response and endogenous outcomes. | The exact action families, actors and geographic detail must be agreed after the measurement and evidence review; a universal world model is not assumed. |
| D-004: Performance and numerical targets | Benchmark a bounded 1904–1932 pilot at 100,000 trajectories in 30 minutes on 8 CPU workers and 16 GB RAM; preserve the existing UI latency targets. Treat all throughput figures as unmeasured proposals. | Profile the native core before committing to scale; report policies, futures, rollouts, fidelity and storage separately. |
| D-005: Fixture distribution | Stage the exact six frozen JSON bundles and their provenance in versioned private project storage. Preserve the old adapter as archival evidence; it is not an executable test dependency. | This requirements PR contains metadata only. A new checkout does not yet have the six files or local adapter scripts. |
| D-006: Broader power and geography measures | Use the researched measurement catalog in product-vision.md to select a small set of objectives and constraints; preserve separate security, prosperity, fiscal, political, partnership and human-cost measures. | Final success variables, beneficiaries, thresholds, horizons and probability assumptions remain open; no composite national-power score is authorized. |
| D-007: Storage and model foundation | Keep a native Python simulation core and a versioned data store; evaluate PostgreSQL, batch workers and columnar result artifacts after the action/actor/objective contracts and performance profile are clear. | The database supports the model. Actor behavior, objective definitions and credible dynamics determine the design first; no infrastructure is provisioned. |
| D-008: Excel runtime independence | Run every supported calculation natively from the first usable release; retain Excel files and existing results only as import and reference evidence. | The native financial and GDP modules require upfront implementation. Missing coverage cannot be hidden by falling back to the workbook. |
| D-009: Objective mode | Compare trade-offs among several success variables with a visible estimated Pareto set; do not require a single weighted score. | The user chooses among competing outcomes after inspecting distributions and risks. |
| D-010: Control and agency | Optimize Pacifica's decisions only. Other actors respond using their own objectives, observations and constraints. | The optimizer cannot prescribe cooperation, select opponent actions or choose favorable random outcomes. |
| D-011: Success definitions and evidence | Review the researched measure families, choose approximately three to five objectives per experiment, and specify constraints, geography, beneficiaries, horizon and risk measures. | Numerical success thresholds and acceptable risk are not yet defined; research categories are proposals, not adopted scores. |
| D-012: Pilot horizon and resolution | Use 1904–1932 as a bounded first decision window with annual strategic decisions and finer crisis/logistics steps where needed; retain 1846–1932 financial regression fixtures. | The pilot must demonstrate strategy discovery even if geography and action families are restricted. |

The principal risks are incorrect actor responses, poorly defined objectives, unsupported probabilities, optimizer exploitation of missing mechanisms, future-information leakage and selection of lucky paths. These require evidence review, matched evaluation, held-out assessment, explicit coverage and small enumerated benchmarks in addition to accounting checks. Six-case parity remains a financial engineering check.

## 12. Source and authority notes

The source catalog in [backlog.json](backlog.json) maps every requirement to user needs or inspected project evidence. S1 pins the [repository rules](https://github.com/c-voelkle/pacifica/blob/cc6e017780970433ab63bc95d0e3749510b44d49/AGENTS.md), [master storyline](https://github.com/c-voelkle/pacifica/blob/cc6e017780970433ab63bc95d0e3749510b44d49/book-agent/revision/master_storyline.md) and [finance documentation](https://github.com/c-voelkle/pacifica/blob/cc6e017780970433ab63bc95d0e3749510b44d49/finance/README.md). S2 pins the alternatives, S3 the result fixtures, S4 the finance skill and S5 the local adapter evidence. S6–S8 record primary wargaming and decision-analysis research; product-vision.md distinguishes those sources from proposed Pacifica adaptations.

Review and adoption of these software requirements are separate from narrative canon decisions. Source documents and the supplied workbook remain immutable references. Implementation and any later canon proposal follow their own review branches.
