# Timeline Lab — build brief

**25 October 2026 · Bounded dramatic sketch, version 2 · engine/schema 0.2**

This brief implements the author's request to bring the 1927–28 prototype toward the original revision 0.10 design: explicit ontology, relationship-driven choices, story exploration and traceable metrics. That request supersedes version 1's exclusions and 2,500-line stop rule for these named capabilities. Keep the bounded implementation under approximately 5,000 source/documentation/test lines; do not expand the setting or add dependencies without authorization.

## The question

What else could plausibly happen in the 1927–28 Japan rescue and Concord crisis, and which consequential choices suggest a useful plot idea and another dilemma?

The author must be able to inspect assumptions, retain an idea, change a policy at a dated fork and replay a saved bookmark. Automated tests establish modeled behavior. Actual novelty and literary usefulness remain an author judgment.

## Scope and implementation

- March 1927–December 1928, monthly steps, the existing seven acting roles. Persons inside institutions remain separately identified descriptive entities; they gain no new controllers. The executive person and office remain distinct identities.
- Existing financing/consent/concession policies plus two LAB controls: assurance_strategy (none/private/public) and commitment_priority (honour_assurance/preserve_discretion).
- The complete scenario, goals, differentiated concession effects, assurance terms, credibility rules, coefficients and metric definitions live in scenarios/1927_rescue.yaml. No new private promise is asserted as canon.
- model.py retains deterministic simulation and finance/authority rules. ontology.py supplies closed types and selected-history evidence materialization; relationships.py executes the assurance mechanism; stories.py supplies deterministic candidates, open policy exploration and bookmarks; metrics.py supplies unit-bearing traces; views.py and app.py present results. run.py supports offline execution and export.
- Pydantic, Streamlit and the already approved PyYAML remain the only declared dependencies. No calculation network, Excel, language model or database is required.

## Relationship mechanism

An executive policy may offer a nonbinding political assurance to the mediator. Private assurances are delivered only to the executive and mediator. The assurance's oversight terms are distinct from loan obligations and legal authority.

At settlement, the honour priority adds promised oversight terms to the requested offer; preserve_discretion retains the requested offer even if it breaches the assurance. Actual and requested terms are both recorded. The recipient assesses only terms actually delivered, then may support cooperation, withdraw privately or disclose an observed breach. A private withdrawal is not a public accusation. Audiences use their own declared credibility thresholds; a truthful report need not produce belief or cooperation.

Each of the four concessions has separately declared legislative and mediation effects. Those are LAB interpretations, not historical coefficients. Original financial, conditional ratification and illegality assumptions retain their visible limitations.

## Explicit ontology and explanation

Use closed validated records for entities, goals, world facts, assertions, observations, beliefs, commitments, plans, decision contexts/records, attempts, adjudications, realized events, metrics, story candidates and bookmarks. Common evidence records carry stable IDs, scenario revision and provenance. Links pin the saved scenario and engine version.

A decision records its role/capacity, delivered information, private inputs, selected policy, scoped alternatives, goals/commitments, procedure reason and random address. Alternatives do not claim a general planner exhaustively evaluated every option. A plan's recorded actual outcome does not invent an owner's subjective assessment. Unsupported motives and sacrifices remain explicitly unassessed.

The implemented subset is not full v0.10 R0 conformance: general temporal predicates, resource reservations, all conduct/intervention modes, independent source extraction audits and formal author acceptance remain open in the linked backlog.

## Author workflow

1. Run the reference or edited policy with 1,000 worlds; 10,000 remains optional and must be measured separately.
2. Discover a bounded family of assurance/priority/concession policies using 25 or 100 matched external worlds per policy. Show policy counts, distinct root worlds and policy-world evaluations separately.
3. Surface causal representatives across assurance/disclosure strata before selecting remaining event-pattern variety. Failures and strategically inferior outcomes remain eligible. Filters do not imply a rare result is a reliable policy.
4. Show goal, obstacle, choice, assessed cost, supported consequence, assumptions and a clearly marked next-question prompt. The next question is not an already simulated future event.
5. Inspect decision reasons, received information, commitments and beliefs. Follow synchronized monthly finances and institutional states.
6. Trace each named metric to its units, owner, horizon, scenario hash/seed, engine/mechanism, declared input values and event evidence. Treasury cash and vote margins remain unavailable; trust/influence remain LAB indices. Unknown never becomes zero.
7. Branch one continuing policy setting from a month. Preserve earlier events and random draws; show matched metric differences. These author overrides are conditional consequence experiments, not proof the actor would choose them. An assurance already made cannot be erased retroactively.
8. Save an immutable local bookmark and download its portable scenario/history/evidence bundle. Verify/replay a downloaded bookmark. Hosted filesystem persistence is not guaranteed; downloading retains the evidence outside the server.

## Invariants and verification

- Fixed-seed, single/batch and reordered-input identity; matched draws and unchanged branch prefix.
- No reaction to an undisclosed promise or hidden actual breach. Delivered disclosure precedes belief updates.
- A nonbinding political breach does not itself create illegality. Law, promise fulfilment, belief and cooperation remain distinct.
- Similar financing can produce different commitments, cooperation and constitutional outcomes. Equal-size concession packages can differ.
- Credit drawing respects actual capacity; public drawing equals total drawing times effective public share. All failures remain in counts.
- Ontology references resolve; people, institutions and office identities stay distinct. Source secrets remain protected.
- Metrics have units/provenance/coverage; unavailable quantities retain missing reasons.
- Bookmark replay reproduces events and outcomes and rejects tampered inputs or narratives.
- Streamlit run/comparison/discovery/filter/branch/grid/export flows work locally. Run regression checks before publishing.

## Still outside this delivery

Whole-novel population; new acting characters; general-purpose personality/planning models; full proposition/temporal query algebra; premise and imposed-event search; multiobjective optimizers; calibrated vote counts or macroeconomics; detailed cash/debt/import-cover accounts; full conduct/resource-reservation protocol; six-fixture parity; automatic LLM narration; a general editor or hosted multi-user architecture.

The original specification remains the design reference. timeline-lab/backlog.json records this slice and remaining work; docs/timeline-lab/backlog.json records partial coverage without marking the full R0 requirements accepted. Narrative source files remain read-only for this implementation.
