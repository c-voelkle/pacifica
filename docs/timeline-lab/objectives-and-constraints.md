# Pacifica objectives and constraints draft

**25 October 2026 · Design revision 0.6 · Draft for author review**

The search should find Pacifica policies that improve prosperity and security while retaining fiscal resilience and limiting human costs. Compare their distributions and trade-offs. Each experiment defines its beneficiaries, objectives, constraints and uncertainty before the optimizer sees results.

The proposed starting set is **core prosperity, security and freedom of action, Treasury resilience, and human cost**. Four additional families cover partnerships, institutions, ecology and partner prosperity. The author has confirmed multiple objectives, Pacifica-controlled decisions, independent other actors and a native model. The metric selection, quantiles, three-month cash proposal and acceptable risks below remain for review.

Use this sheet with the [action and actor catalog](action-and-actor-catalog.md) and [structured draft catalog](draft-model-catalog.json). The JSON carries each measure's complete beneficiary, geography, information, failure, coverage and source contract. These are design records, not executable simulation rules. The [ontology](ontology.md) defines their semantic identities, observation/intentionality boundaries, profiles and intervention modes. R0 selects a narrower financing/commitment dilemma and only the measures it covers; the full objective set below describes the broader proposed campaign.

## Proposed experiment

| Field | Draft choice |
|---|---|
| Decision window | 1 January 1904 through 31 December 1932; earlier-decision campaigns need their own fork. |
| Controlled decisions | Pacifica's executive agenda and authorized actions. Domestic institutions retain reserved powers; other parties decide independently. This control granularity is proposed. |
| Starting state | Versioned balances, population, assets, laws, rights, obligations, beliefs and capability at the fork. A 1932 endpoint cannot initialize 1904. |
| Clock | Annual strategy/budgets, monthly finance and actor responses, finer crisis/logistics steps where necessary. |
| Objectives | OBJ-01–04 as a starting proposal; no single weighted score. |
| Risk summaries | Lower 10th or upper 90th percentile as specified below; acceptable constraint-exceedance probabilities remain open. |
| End of horizon | Show remaining debt, guarantees, maintenance, restoration and treaty duties; model a continuation or bound its consequences before ranking. |
| Search result | A best-found feasible trade-off set with distributions, failures and sensitivity to model/actor assumptions. |

A common-start policy contest uses the same initial world, objective definitions and exogenous-world design. A scenario-package comparison may change earlier accession, the 1904–1905 confrontation or other premises, but must expose those differences. A/B's changed war assumptions and C/D's earlier accession cannot be mistaken for the isolated effect of later policy.

The [fixture manifest](fixture-manifest.json) identifies the shared-change control, first diverging in 1904. It is not a no-action strategy. Its exact inputs still need retrieval from the frozen bundle before policy reconstruction. C's frozen calculation uses the labelled C0 peaceful commercial continuation; C's unresolved later narrative cannot be filled with D's institutions. The six files remain financial regression references.

## Author narrative conditions

Actor goals and strategic objectives remain separate from what the author wants to explore. A narrative query can request a rescue followed by institutional conflict, a choice made under a mistaken belief or a minimal change that averts a crisis. These examples do not add events or motives to canon.

R0 filters and bookmarks supported recorded histories; R1 searches bounded routes or minimum changes. Declare predicates, temporal order, allowed decision/premise interventions, evidence limits, budget and change-cost units or lexicographic order. Imposed events remain conditional experiments. Counterparties retain their decisions, and no narrative predicate enters actor observations.

Preserve author-selected policies and histories independently of strategic dominance. Selection frequencies retain their denominator; freeze selected policies and assess fresh unconditioned worlds before reporting ordinary success distributions. General editing and optional prose follow in R2, after the bounded author workflow is demonstrated.

## Proposed objective set

A measure needs units, beneficiary and geographic scope, price basis where applicable, time aggregation, distribution statistic, failure treatment, coverage and provenance. A proposal or activity count does not establish its intended outcome.

| ID | Family | Path measure | Proposed distribution summary |
|---|---|---|---|
| OBJ-01 | Core prosperity | Cumulative real household consumption per usual resident | Improve the lower 10th percentile |
| OBJ-02 | Security and freedom of action | Days a required security condition is materially unmet | Reduce the upper 90th percentile |
| OBJ-03 | Treasury resilience | Minimum monthly unrestricted cash coverage | Improve the lower 10th percentile |
| OBJ-04 | Human cost | Cumulative conflict/disruption deaths across affected populations | Reduce the upper 90th percentile |
| OBJ-05 | Voluntary cooperation | Time a selected functional agreement has valid consent and fulfilled obligations | Improve the lower 10th percentile, separately by relationship |
| OBJ-06 | Institutional durability | Days of material unauthorized action or interruption of the agreed constitutional order | Reduce the upper 90th percentile |
| OBJ-07 | Ecological resilience | Cumulative minimum-stream-flow deficit for a named watershed | Reduce the upper 90th percentile |
| OBJ-08 | Partner prosperity | Separately scoped partner real consumption per resident | Improve the lower 10th percentile, separately by partner |

### Core prosperity

**OBJ-01.** For each path, sum annual real household consumption per usual resident times the fraction of year, in constant 1913-price currency. Use the financial model's core economic perimeter; report Hawaii, the Philippines and sovereign partners separately unless a different explicit perimeter is selected. Declare how guest workers qualify as usual residents.

Consumption needs a bridge from production through taxes, domestic/foreign income flows and remittances to households. Existing nominal/real GDP does not supply it. A real-GDP/person proxy is permitted only under its own name and claims. Report the 1932 level, worst-year change and distribution across groups alongside the cumulative measure.

Continue welfare accounting after defeat or default using a defined successor/continuation state. Where that model is incomplete, show an outcome interval rather than inventing consumption or dropping the path. Source context: [SRC-STORY](https://github.com/c-voelkle/pacifica/blob/cc6e017780970433ab63bc95d0e3749510b44d49/book-agent/revision/master_storyline.md), [SRC-FINANCE](https://github.com/c-voelkle/pacifica/blob/cc6e017780970433ab63bc95d0e3749510b44d49/finance/CR-031-review.md).

### Security and freedom of action

**OBJ-02.** Before search, specify required sovereign conditions, essential routes and defensive commitments, their beneficiaries, acceptable interruption and recovery. Count days when at least one condition is materially unmet; simultaneous failures do not multiply the headline day count. Show causes separately.

A treaty signature does not establish usable access. Inventory does not establish readiness, and readiness does not establish sustainment. Use declared mission/contingency tests so peaceful histories can still reveal inadequate capability. Irrecoverable loss counts through the remaining horizon. The condition list must value functions that peaceful and wartime institutional arrangements can both provide.

Enable this measure only with threat, rights, readiness and logistics mechanisms. No universal national-power index is assumed. Source context: [SRC-STORY](https://github.com/c-voelkle/pacifica/blob/cc6e017780970433ab63bc95d0e3749510b44d49/book-agent/revision/master_storyline.md), [SRC-AUDIT](https://github.com/c-voelkle/pacifica/blob/cc6e017780970433ab63bc95d0e3749510b44d49/book-agent/revision/war_base_assumptions.md), [SRC-ALT](https://github.com/c-voelkle/pacifica/blob/626ffbb0bd6486c19164f89104569d78321ebd55/book-agent/revision/alternatives/CR-032/README.md).

### Treasury resilience

**OBJ-03.** At each monthly opening, calculate:

`cash coverage in months = 12 × unrestricted Treasury cash / unavoidable cash outlays due in the next 12 months`

The path measure is its minimum. Commitments cannot be deleted from the denominator, and the same available cash cannot fund two commitments. Identify the essential-service basket and forecast error. A zero-outlay case needs an explicit no-obligation result, not division by zero.

Keep core, crown, local, common-institution and Reserve Bank accounts distinct. Gold reserves and private subscriptions are not unrestricted Treasury cash. Report arrears, gross debt, interest, contingent exposure and public net worth alongside coverage. Coverage becomes zero from a sovereign payment failure until a modelled resolution restores it.

This needs native monthly cash, maturity, guarantee and service schedules. Source context: [SRC-FINANCE](https://github.com/c-voelkle/pacifica/blob/cc6e017780970433ab63bc95d0e3749510b44d49/finance/CR-031-review.md), [SRC-AUDIT](https://github.com/c-voelkle/pacifica/blob/cc6e017780970433ab63bc95d0e3749510b44d49/book-agent/revision/war_base_assumptions.md).

### Human cost

**OBJ-04.** Count modelled military and civilian conflict/disruption deaths once, across all materially affected populations. Include foreign civilians, guests and displaced communities. Report civilian/military and partner breakdowns, displaced persons and person-years of deprivation separately.

Natural mortality and policy-related deaths require separate categories. Count delayed consequences and continue after political, military or fiscal failure. Missing foreign losses are unknown, not zero. Enable the objective only with a casualty/disruption model and declared population coverage. Source context: [SRC-STORY](https://github.com/c-voelkle/pacifica/blob/cc6e017780970433ab63bc95d0e3749510b44d49/book-agent/revision/master_storyline.md), [SRC-VISION](product-vision.md).

### Optional objectives

**OBJ-05** tests a named function, such as reliable voluntary cooperation or transit, rather than counting treaties. A different lawful agreement may fulfil it. Show consent, reciprocal performance and autonomy separately; coerced continuation does not count as voluntary success.

**OBJ-06** uses observable powers, votes, law and institutional actions. A later indemnity does not erase earlier breach days. Where political acceptance requires qualitative assessment, use anchored states rather than an invented 0–100 legitimacy score.

**OBJ-07** integrates `max(0, adopted minimum stream flow − actual flow)` over time in cubic metres. Keep reef condition, restoration debt, smoke exposure and public access separate. Hydrology and engineering thresholds remain to define.

**OBJ-08** applies a separate prosperity contract to a selected partner. It requires that partner's accounts, population and independent behavior. Never add partner GDP, reserves or tax capacity to Pacifica's sovereign resources. Each relationship/partner component is separately selected rather than hidden in a weighted total. Source context: [SRC-STORY](https://github.com/c-voelkle/pacifica/blob/cc6e017780970433ab63bc95d0e3749510b44d49/book-agent/revision/master_storyline.md), [SRC-B](https://github.com/c-voelkle/pacifica/blob/626ffbb0bd6486c19164f89104569d78321ebd55/book-agent/revision/alternatives/CR-032/CR-032b.md), [SRC-D](https://github.com/c-voelkle/pacifica/blob/626ffbb0bd6486c19164f89104569d78321ebd55/book-agent/revision/alternatives/CR-032/CR-032d.md).

## Diagnostic measures

- **DIA-01 — Forces and readiness:** Available mission-capable units; Mobilisation time; Training and maintenance backlog; Sustainable force-days.
- **DIA-02 — Logistics and communications:** Bottleneck freight capacity and demand; Fuel/ammunition days; Civilian rail allocation; Port/ship availability; Vital-link interruption and repair time.
- **DIA-03 — Finance and monetary capacity:** Public cash, debt and service; Guarantees and draws; National monetary gold by owner; External liquidity by currency; Bank capital and losses.
- **DIA-04 — Income and ownership:** Nominal and real GDP by territory; GNI and household-income bridge; Foreign coupons/dividends; Employment and remittances; Household/group outcomes.
- **DIA-05 — Relative position:** Core/Union real-output ratio on a common price basis; Network output shown separately; Supply and financing concentration; Cost and time to discharge or decline a named commitment.
- **DIA-06 — Governance and measurement:** Observed/published versus underlying state; Report delay and coverage; Legal consent and treaty performance; County and Gulf public measures; Beneficiaries and harms excluded by a metric.
- **DIA-07 — Search credibility:** Distinct policies and realized behaviors; Worlds and completed trajectories; Sampling uncertainty and structural sensitivity; Computational errors; Unresolved terminal outcomes; Training versus held-out assessment.

A nominal-output ratio may improve because prices changed or another country collapsed. Show nominal and real output, sovereign and network quantities, and partner outcomes separately. Relative position may be deliberately selected later; it is not an automatic substitute for security or welfare.

Keep underlying and published conditions separate. The master includes falsified official reporting: an official table cannot overwrite actual losses. Actors receive dated, uncertain observations; scoring uses the registered underlying quantities.

## Constraint sheet

| Type | Interpretation |
|---|---|
| ENGINE INVARIANT | A calculation or accounting violation is a model error. Diagnose it and withhold affected rankings; keep the error count visible. |
| ACTION PRECONDITION | Perceived eligibility and actual adjudication are separate; a reasonable attempt can fail without revealing hidden feasibility beforehand. |
| LEGAL REQUIREMENT | Lawful execution requires authority/consent; a supported breach profile records unauthorized conduct and consequences. |
| PHYSICAL LIMIT | Actual resource, technology and time limits constrain execution in every profile. |
| AUTHORIAL CONSTRAINT | A locked experiment premise; it is distinct from in-world law and any permitted change needs an explicit premise branch. |
| POLICY BOUND | A limit on Pacifica's choices. Record breaches caused by shocks separately from deliberate commitments. |
| OUTCOME BOUND | A realized outcome limit. Keep violating futures in the sample and mark the policy's feasibility and loss. |
| EVIDENCE GATE | A ranking or measure is unavailable until definitions, mechanisms and data cover the intended claim. |

An action restriction limits orders; an outcome requirement may still fail because another actor or shock intervenes. Keep those losses in the sample. Engine failure, policy infeasibility and an adverse world are different results.

The lawful profile respects competent consent. The selected `breach_exploration` profile enables only registered physically possible breaches with covered resistance, enforcement, institutional and obligation consequences; unsupported breach families remain disabled. R0 demonstrates one M0-selected comparison. Both profiles retain physical/accounting invariants, independent responses and locked authorial premises. Later cure preserves prior breach days. Baseline replay retains the illegal 1927 provisional Concord application and 1928 cure; that source event does not enable a general consent bypass.

| ID and status | Rule or proposed bound | Treatment |
|---|---|---|
| CON-01 — Required model rule | Balance accounts, counterparties and resource movements; no borrowing-as-income, syndicate-as-Treasury or avoided-spending-as-GDP. | Diagnose model errors; withhold affected rankings and show error counts. |
| CON-02 — Required model rule | Real inputs, lead times and usable capacity; no simultaneous double allocation or instant technology. | Adjudicate actual failure/partial execution/delay after an observation-consistent attempt; never realize impossible capacity. |
| CON-03 — Required model rule | Information limits cover policy inputs, menus, previews, messages and response knowledge. | A hidden-information leak is a model/policy error; actual adjudication discloses only permitted observations. |
| CON-04 — Legal requirement and profile | Competent authority/consent before lawful execution; physical control and legal title remain distinct. | Lawful mode rejects unauthorized execution; a selected supported breach variant records consequences without inventing consent or title. |
| CON-05 — Required model rule | Separate core/crown/local/common/foreign ownership, budgets, GDP and reserves. A concession is not sovereignty. | Diagnose model errors; withhold affected rankings and show error counts. |
| CON-06 — Authorial premise | Apply CR-031-R1's paid professional construction and free, well-paid Kolyma premise; no invented cost/productivity uplift. | Reject an infeasible order; later shortages/violations by others remain outcomes. |
| CON-07 — Source planning convention | Peacetime military/overseas spending ≤4% of North American GDP. Post-1900 continuation is a planning convention. | Restrict Pacifica's commitments; record shock-induced breaches and consequences. |
| CON-08 — Source planning convention | Public interest due ≤15% of ordinary public revenue on the same fiscal perimeter. | Keep breaches in the distribution and report severity, duration and feasibility. |
| CON-09 — Source planning convention | Gross public debt ≤30% of North American GDP; disclose guarantees and common/partner exposure. | Keep breaches in the distribution and report severity, duration and feasibility. |
| CON-10 — Proposed threshold | Proposed cash protection: three months of unavoidable outlays; test one/three/six months. Existing essential duties remain funded. | Restrict Pacifica's commitments; record shock-induced breaches and consequences. |
| CON-11 — Model rule with source rescue target | Separate bank solvency, domestic liquidity and external currency. Baseline Japan rescue retains six weeks of imports as a model target. | Keep breaches in the distribution and report severity, duration and feasibility. |
| CON-12 — Model rule with unvalidated benchmarks | Only sustainable deployments with actual access, stocks and rail/sea capacity, including required civilian allocation. | Reject an infeasible order; later shortages/violations by others remain outcomes. |
| CON-13 — Open threshold | Human-loss ceiling and accepted exceedance risk remain open; include affected foreign populations. | Keep breaches in the distribution and report severity, duration and feasibility. |
| CON-14 — Source policy; engineering values open | Apply environmental/land duties once legally effective; flow/discharge engineering thresholds remain open. | Restrict Pacifica's commitments; record shock-induced breaches and consequences. |
| CON-15 — Source institutional rule | Gulf admission requires all continuing measures and parity tests, other compact conditions and valid consent. | Reject an infeasible order; later shortages/violations by others remain outcomes. |
| CON-16 — Source rule with time scope | Respect applicable Korean sovereignty, Chinese railway ownership, running rights and local rights; new terms require consent. | Reject an infeasible order; later shortages/violations by others remain outcomes. |
| CON-17 — Required model rule | Preserve the established prefix; ordinary discovery generates future outcomes. Explicit imposed events are separately conditional. | Earlier causes require an earlier fork; forced outcomes cannot certify ordinary policy success. |
| CON-18 — Required model rule | Retain terminal failures and post-1932 obligations. Model a continuation or give bounds; never drop failed paths. | Keep breaches in the distribution and report severity, duration and feasibility. |
| CON-19 — Required model rule | Enable covered measures and check mechanism applicability during evolution. Missing data is unknown. | Withhold affected claims or explicitly select a registered provisional continuation with propagated conditional status. |
| CON-20 — Open risk tolerances | Choose acceptable outcome risks; assess joint feasibility without multiplying marginal pass rates. | Keep breaches in the distribution and report severity, duration and feasibility. |

The 4%/15%/30% source limits use consistent North American/public perimeters. Japanese GDP does not enlarge Pacifica's denominator. Crisis exceptions require a real registered trigger, scope, cost and expiry; declaring an action “war” cannot manufacture an exemption. The audit identifies these as planning rules, with later numerical feasibility still under review. Source context: [SRC-STORY](https://github.com/c-voelkle/pacifica/blob/cc6e017780970433ab63bc95d0e3749510b44d49/book-agent/revision/master_storyline.md), [SRC-AUDIT](https://github.com/c-voelkle/pacifica/blob/cc6e017780970433ab63bc95d0e3749510b44d49/book-agent/revision/war_base_assumptions.md).

For **CON-12**, the source's approximately 28,000-person contingent and 50,000 troops reaching the Ob within two weeks are proposed/MODEL tests, not established capacity. The five railway sections, seasonal routes, depots and civilian freight need independent evidence. A Yenisei fallback does not remove eastern bottlenecks.

For **CON-15**, the five general measures are infant mortality, literacy, real wages, homicide and typhoid against the specified weakest former-territory comparator. Both parity tests require a joint medical-and-literacy examination pass-rate ratio for Black/freedmen twenty-year-olds versus white twenty-year-olds of at least 0.95 and a Black/freedmen-to-white infant-mortality ratio no higher than 1.05. Registers must cover at least 90% of specified records; fiscal, debt, standards and other compact conditions remain necessary. Carry inherited streaks and the twenty-five-year continuity rule explicitly. Baseline replay preserves non-membership through 1932; discovery cannot bypass the rules or force Gulf acceptance. Source context: [SRC-STORY](https://github.com/c-voelkle/pacifica/blob/cc6e017780970433ab63bc95d0e3749510b44d49/book-agent/revision/master_storyline.md), [SRC-CR](https://github.com/c-voelkle/pacifica/blob/cc6e017780970433ab63bc95d0e3749510b44d49/book-agent/revision/change_requests.json).

## Assessment and evidence

Mechanisms declare their applicable institutional/scale/time domain, read/write ownership, independent intervention/counterexample cases and unsupported behavior. If a trajectory leaves that domain, propagate unsupported status to dependent claims. A registered provisional continuation can support a labeled story experiment, but cannot silently enter stronger rankings. Conditional, terminal and computationally failed paths remain counted; unresolved aggregates need explicit bounds or remain unavailable.

Alternative structural-model assessments remain separate unless a justified weighting contract supports pooling. A new random sample does not resolve disagreement between behavioral theories.

For probability-weighted experiments, show full distributions, sample uncertainty and joint target attainment. For unweighted plausible worlds, show tested-scenario fractions, vulnerability, robustness and regret against a declared reference set. Neither scenario quantiles nor deterministic financial fixtures establish historical probabilities.

Separate random events, parameter uncertainty and alternative structural/actor models, preserving correlations and persistence. Tune on development worlds and assess finalists on fresh worlds and opponent assumptions. Assessment worlds used to redesign a policy become development data. Match exogenous draws when appropriate; endogenous crises and responses must differ when decisions change.

A policy is dominated when another improves at least one selected objective without worsening any other. Show a provisional region where sampling, unresolved terminal outcomes or structural assumptions change dominance. If no feasible policy is found, display the conflicts and best-found violations. Do not silently relax bounds or add arbitrary penalties to combine deaths, cash, constitutional breaches and GDP.

| Area | Evidence needed |
|---|---|
| Native financial accounts | Native equations, actual six frozen bundles and provenance; monthly obligations and essential-service coverage; full North American GDP perimeter. |
| Household prosperity | Consumption/household-income bridge, price basis, residency and guest treatment, foreign income/remittances and distribution. |
| Military and logistics | Independent capacity/cost/lead-time evidence, route conditions, stockpiles, serviceability, civilian allocation and mission tests. |
| Actors and institutions | Acceptance/refusal rules, plausible alternatives and capacity, observation delays and faction evidence; alternative structural response models. |
| Human consequences | Scalable casualty/disruption model, affected population coverage and post-failure continuation. |
| Ecology and public measures | Thresholds/denominators, coverage, hydrology/ecological response and restoration costs. |

The existing financial references include 1913-price real GDP, but not household consumption or complete North American geographic coverage. Every enabled metric must distinguish observed evidence, analogues and explicit assumptions. More rollouts cannot repair a missing mechanism.

## Decisions for review

M0 also selects the active ontology, selected character beliefs/intentions, supported breach consequences and author usefulness protocol. Evaluate distinct causal alternatives, consequential agency, branch clarity, useful retained ideas, time to a retained idea and repair burden before broad tooling or search-scale commitments. Author judgment is separate from technical validation.

| ID | Decision | Starting proposal |
|---|---|---|
| REV-01 | Select objectives and beneficiaries | Begin with OBJ-01–04, after evidence gates; add partner/autonomy and environmental components as supported. |
| REV-02 | Select risk preference and hard outcome limits | Review the draft Q10/Q90 summaries, three-month cash proposal and source 4%/15%/30% conventions; choose loss limits and exceedance risks. |
| REV-03 | Approve actor/control granularity | Optimize the executive agenda and authorized actions; retain institutional and foreign consent. Instantiate all indispensable negotiating parties. |
| REV-04 | Select pilot scope | Start with one bounded dilemma within the broader 1904–1932 campaign; include selected beliefs/plans, supported consequences and the author review. |
| REV-05 | Resolve evidence and continuation gaps | Obtain the consumption/price bridge, resource/logistics data, actor response cases, human-cost model and terminal-liability treatment before claiming strategic rankings. |
| REV-06 | Choose comparison design | Use common-start policy contests; separately label premise packages and imposed-event experiments. |
| REV-07 | Select semantic and narrative slice | Active records, character/proposition/plan subset, predicates and one supported lawful/breach comparison. |
| REV-08 | Approve author evaluation and search contracts | Writing tasks and acceptance procedure; minimum-change costs, allowed interventions and selection denominators. |

Adopting an experiment or metric does not adopt a generated history as canon. The [master storyline](https://github.com/c-voelkle/pacifica/blob/cc6e017780970433ab63bc95d0e3749510b44d49/book-agent/revision/master_storyline.md) and its local APPROVED, PROPOSED, OPEN and MODEL distinctions retain narrative authority.
