# Timeline Lab data-population and capacity plan

**Draft for review · 25 October 2026 · Revision 0.10**

The first useful delivery needs a small, executable content package. A full list of names is insufficient, and full dynamic simulation of the entire novel is not a prerequisite. Start with the 1927–1928 Japan rescue/Concord dilemma, including selected private commitments, information and cooperation effects. M0 fixes the exact starting date/phase, horizon and active mechanism set. Future authored outcomes stay references, not queued events or actor foresight.

This plan implements TL-077 and TL-078 in the [requirements](requirements.md) and [backlog](backlog.json). The [ontology](ontology.md) defines the corresponding manifest, temporal roles, ambiguity policies and agency evidence; the [architecture](model-architecture.md) assigns execution and storage responsibilities. All costs and hardware figures below are planning estimates unless explicitly marked measured. No data import, runtime benchmark or approval of narrative canon is claimed by this documentation update.

## Measured source baseline

Inventory measured against main commit `cc6e017780970433ab63bc95d0e3749510b44d49`. Files live under `book-agent/revision/`. Counts use decoded text characters; words are whitespace-delimited. Source provenance links in a future importer must include blob identity and exact span offsets or stable anchors, not line numbers alone.

| File | Characters | Pinned blob SHA |
|---|---:|---|
| master_storyline.md | 265,242 | f398ff96b6f8394e40100f36728e754a66ae251e |
| character_bible.md | 181,144 | 62746351f1c0bc81871702e2cbbbaa2ed3813e7b |
| historical_background.md | 70,977 | 009546b11d3422e331dc65737ebff33a18641893 |
| war_base_assumptions.md | 30,172 | 7000a9daaaa48c20ed954335fa4a32fe5c245ce1 |
| character_registry.json | 274,427 | 4db0208b3fc219df639118f07fcb16195e7137a9 |
| change_requests.json | 727,646 | e539f1a11b8b78190c6cec4a5114395e6d046d84 |
| legacy_character_crosswalk.json | 112,548 | 0ce29a50e08674ec843850798a6de7c1e87e5afd |
| Total | 1,662,156 | Includes repeated narrative and revision history |

The master storyline has 39,321 words and 37 numbered sections. The registry has 151 identities: six retired and 145 active/provisional, with 141 explicit links. The legacy crosswalk describes 250 profiles; these are not 250 additional people. Preserve stable registry identities and reconcile aliases before creating anything new. Change requests contain alternatives and historical states, so their volume must not be treated as additional canonical fact volume. Verify source authority and supersession locally, rather than assigning one status to every statement in a file.

**Estimated inventory, not an extraction result:** a useful whole-story catalog may require 600–1,200 identities across people, offices, institutions, factions, places, assets and instruments, and 6,000–15,000 semantic records for dated facts, relationships, claims, information, commitments and model bindings. These are total planning ranges, including reused registry identities. A first R0 package may reference 50–100 entities but should activate only a few decision-makers. Referenced entities need not all have controllers, and many records remain background/reference-only. Dependency closure and writing tasks determine relevance, not an arbitrary entity quota.

## Population workflow

### Source coverage and omission audit

Create SourceCoverageLedger for the selected slice using the fields in the ontology contract. Define selected documents/sections and stable passage units directly from the pinned source text, independently of the first extraction output. Each unit maps to extracted record revisions, a reviewed exclusion with a reason, or a named unresolved question and its affected claims. Follow relevant cross-references or record a justified scope boundary.

A mapped passage can still omit a consequential claim. Build a small reference sample in a separate source-first review pass before consulting the extraction output. Cover identities, promises/obligations, vetoes/authority, actor knowledge restrictions and chronology; declare the sample and examine exclusions. Compare expected claims, dates and authority with the proposed records. Record sample size, omissions, false additions, repairs and limits rather than claiming whole-corpus recall.

Deliberately remove a consequential promise or veto and its direct references while keeping the remaining dependency graph valid. The independent expected-claim comparison must detect the omission and block affected activation until repair or explicit rescoping. Unresolved material discrepancies cannot be silently passed. Retain source ledger, sample review and author-decision queue refs in the activated manifest and reconcile them on source changes.

### Staged preparation

Use scripts and validated files first. The workflow does not require a new graph database, universal extraction service or general editor.

| Stage | Deliverable and acceptance |
|---|---|
| 1. Pin sources and authority | Record commits/blobs, source precedence, approved changes and local APPROVED/PROPOSED/OPEN/MODEL status. Identify conflicts and protected ambiguity before extraction. |
| 2. Stage evidence-linked proposals | Declare source scope and passage units before examining extraction output. Extract dated records with exact spans and maintain extracted/excluded/unresolved dispositions. Keep proposals outside active bundles; inferred motives and estimates remain model assumptions. |
| 3. Reconcile identities | Reuse registry IDs and the legacy crosswalk; distinguish people, offices and institutions, succession and resource ownership. Resolve collisions and retired aliases explicitly. Re-importing the same source creates no duplicates. |
| 4. Assign temporal and information roles | Set start phase and horizon; classify starting facts, live obligations, future references, external assumptions and narrative constraints. Separate target/valid time, receipt time and actor belief time. Initialize each active actor's information through supported rules. |
| 5. Bind the executable slice | Connect active predicates, units, schedules, controllers, goals, commitments, conduct, ambiguity and mechanisms. Compute transitive dependency closure for the selected writing tasks. Missing dependencies are sourced, explicit assumptions, excluded with affected claims disabled, or blocking unresolved. |
| 6. Validate and review | Check executable dependencies and independently audit a source-first reference sample for omissions/false additions, including the injected missing-promise/veto test. Run identity/time, information, ambiguity, relational-counterexample and financial checks. Record reviewer decisions and an author-decision queue; waiting is not approval. |
| 7. Activate and measure | Publish a reviewed manifest with source-coverage/sample/decision-queue refs. Run the predeclared retain-and-branch trial and save/replay the resulting chain. Measure complete audited-package tokens, active AI time, repairs, author labor/waiting and resources separately; revise larger estimates before expansion. |
| 8. Maintain incrementally | New source revisions produce proposals and an impact report identifying affected records, mechanisms and experiments. Retain old source bundles and identities for replay; publish a new manifest after review. Never silently mutate earlier runs or canonical source files. |

No importer may resolve deliberately protected ambiguity, invent a missing approval, or assume that absence means false. Responsibility for Noe's death stays unresolved. Supported testimony and suspicion may affect beliefs and choices; the importer and sampler cannot select a secret culprit. Withhold a dependent computation that genuinely requires the answer, while permitting independent supported activity. Changing an authorial ambiguity lock is an explicit premise revision, never an optimizer variable.

## From source chronology to playable state

Valid unknown state is an intentional representation of the story. It has a predicate, scope, explicit tag/reason and resolution policy and must survive initialization, hashing, saving and replay. Missing a required schema, owner, unit or runtime binding is instead a configuration error. A mechanism needing unavailable truth is withheld; supported suspicion and testimony can still drive action. Noe's death remains unresolved as to responsibility, without a sampled culprit.

ExperimentContentManifest is a versioned configuration artifact in the existing experiment bundle, not a thirtieth world record. Its required fields and exact roles are mirrored in `ontology_contract.content_manifest_contract`.

| Content role | Example and executable treatment |
|---|---|
| initial_fact | A settled pre-start officeholding or balance can initialize state under its evidence/authority status. A proposed interpretation stays an explicit assumption. |
| active_obligation | A pre-existing payment or promise due later remains scheduled and conditional; the obligation does not guarantee settlement or compliance. |
| reference_outcome | The authored 1928 settlement is retained for comparison when starting in 1927. It neither runs automatically nor becomes knowledge of an actor. |
| external_scenario_assumption | An expressly assumed external shock/distribution has timing, applicability and observation rules. It cannot conceal a forced endogenous counterparty response. |
| narrative_constraint | A desired ending filters or guides search; it cannot directly change world state. An imposed event remains a separately labelled conditional intervention. |

Every active dependency needs a disposition and every active claim needs actual mechanism coverage. Referentially complete JSON is insufficient. The package pins source hashes/spans, authority and supersession, start phase/horizon, active records, per-actor information, controller and mechanism bindings, conduct/ambiguity, exclusions, validation and review. All executable semantics enter resolved_experiment_id; reference-only annotation does not change calculation identity until used semantically. Retain provenance even when it does not affect the calculation key.

M0 should demonstrate a private commitment, selective disclosure, belief revision, costly choice, cooperation change and a next dilemma. Give at least two candidates similar financial results but different supported relational consequences. A plausible manual action intervention can isolate consequences under unchanged continuation rules; separately test whether the controller generates intention-sensitive behavior. Do not force the same controller to produce both alternatives merely to satisfy a causal test. The source may not specify every private motive: clearly reviewed modeling assumptions are allowed, with their effect visible and canon unchanged.

The relational tests also cover hidden betrayal without unearned knowledge, a legally permissible breach of a nonbinding promise, and truthful disclosure that fails to produce belief or cooperation. Keep the respective update rules, information channels, legal status and promise fulfillment separate.

### Concrete author trial

Before tuning, record actual prepared and open tasks, at least one supported-domain question withheld from model/output tuning, the notes/manual comparator and task order/exposure, and numeric session/repair budgets. The author must retain at least one previously unconsidered idea judged usable after assumption disclosure, branch from that idea into a subsequent supported dilemma, and save/replay the chain. Record bookmark/branch/assessment refs, novelty and usefulness judgments, time to idea and branch, explanation gaps, manual repair, comparator observations and explicit acceptance.

Draft candidates can carry not_assessed or unresolved evidence, and missing dramatic elements need explicit statuses/reasons; they do not pass mandatory agency cases. Failure of a declared limit or required case needs repair/reassessment or a prospective protocol/scope revision. Held-out feedback used for tuning requires a fresh question. The single-author comparison records prior exposure and learning limitations; neither an attractive summary nor a filled sacrifice slot establishes usefulness.

## Effort estimates

Calibrate these ranges on a complete first package, including the independent omission audit, behavioral-data preparation, repairs and trial support. Keep the author-decision queue visible: each item records the question, source refs, affected claims, blocking status, responsible reviewer, decision status and waiting time. Excluding waiting from active AI hours does not remove its effect on elapsed delivery. Record author review labor separately. The first measurement may justify changing the ranges; v0.10 does not claim a new measured estimate.

These are **cumulative alternative scopes**, not additive stages. The broader rows include much of the narrower work. Tokens count model input, repeated context, output and reasoning where available; they are not source tokens, database size or an exact billing forecast. Hours mean active elapsed work by one AI agent, including tool use, checking and retries. They exclude waiting for author decisions and are estimated independently of token counts, not computed from a nominal tokens-per-second rate. Parallelism can shorten elapsed time but may add reconciliation work; none is assumed here.

| Deliverable | Total model tokens | Active AI hours | Practical result |
|---|---:|---:|---|
| Name index only | 0.2–0.6 million | 2–6 | Searchable names and aliases; cannot support simulation by itself |
| First usable R0 dilemma content | 0.8–2 million | 10–25 | Reviewed 1927–1928 content package with a few active actors and supported dependencies |
| Whole-story semantic catalog | 3–7 million | 35–80 | Dated, sourced and searchable facts/relationships; much remains non-executable |
| Catalog plus several substantial playable periods | 6–15 million | 70–180 | Knowledge, behavior, parameterization and validation for selected periods, using implemented mechanisms |

Use **1.5 million tokens and 18 active hours** as a first-slice planning allowance, and **10 million tokens and 120 active hours** for broader practical coverage. These are judgmental centers, not probability bounds or delivery promises. Whole-story identities and all playable state are not the same deliverable. Full dynamic coverage of 1824–1932 would add mechanism development and validation beyond these population estimates.

Illustrative allocation of those centers, to make the work budget inspectable:

| Work | First package: million tokens / hours | Broader coverage: million tokens / hours |
|---|---:|---:|
| Inventory, authority and scope | 0.15 / 2 | 0.5 / 8 |
| Extraction and identity reconciliation | 0.30 / 4 | 2.0 / 24 |
| Temporal roles and actor information | 0.35 / 4 | 2.0 / 24 |
| Behavioral data and existing-mechanism bindings | 0.35 / 4 | 3.0 / 34 |
| Consistency checks, review preparation and repairs | 0.25 / 3 | 2.0 / 24 |
| Activation, measurements and maintenance baseline | 0.10 / 1 | 0.5 / 6 |
| Total | 1.50 / 18 | 10.0 / 120 |

Included: source reconciliation, temporal normalization, model-data preparation, binding to existing executable mechanisms, tests and repair. Excluded: implementing the general simulator/UI, creating new domain mechanisms, extensive historical research, author review labor and decision waiting. Sparse source evidence, identity conflicts, missing dates or changed canon push work toward or beyond the high end. Extraction alone is relatively cheap; reconciling authority, knowledge and behavior determines whether the tool is useful.

Record an activity log for the first package with source/version, records proposed/accepted/repaired, unresolved questions, dependency coverage, tokens and their metering limits, active time and waiting time. Include all calls and rereads rather than only final output. Do not count guessed or unobservable reasoning tokens as measured. Re-estimate before population expands; no model-independent guarantee of tokens or AI speed is implied.

The quality log also records source units reviewed, sample size and selection, expected claims, omissions, false additions, excluded claims and repairs. A valid reference graph or a high extracted-record count is not an extraction-quality measure. Source coverage and author-decision queue maintenance belong inside the existing preparation/checking allowances, whose adequacy must be tested by M0.

## Disk and memory planning

The proposed CPU-based native engine does not require a local LLM or GPU. Optional later local narration, development toolchains, large attachments and retained backups need separate space. These allowances use decimal GB and are unmeasured; M0 must report the actual environment and process-tree peak memory. Source character counts are not UTF-8 byte measurements. The six frozen finance bundles are 25,473,049 bytes, while indexed source text is small compared with simulation results.

| Storage component | Planning allowance |
|---|---:|
| Packaged application and native dependencies | 2–5 GB |
| Curated catalog, text evidence, indexes and modest Git working history | 0.1–1 GB |
| First usable workspace including application, recent bounded results and temporary headroom | 10–30 GB total |
| Free SSD space recommended before starting | 50 GB |
| Sustained use with retained campaigns | 50–100 GB or more; no fixed upper bound without retention limits |

The total workspace row includes the earlier components; do not add all rows. Space for a second checkout, package caches, developer dependencies, backup copies and growing Git history can be additional. Plain entities and facts are small; retained traces, checkpoints and query spill dominate. Importing more identities does not inherently require a server-scale database.

### Result-storage arithmetic

For 100,000 evaluations and 100 float64 metrics, before compression, identifiers, metadata, indexes and extra trace fields:

| Retained values | Arithmetic | Raw numeric storage |
|---|---|---:|
| One summary per evaluation | 100,000 × 100 × 8 bytes | 80 MB |
| 29 annual snapshots | 100,000 × 100 × 29 × 8 bytes | 2.32 GB |
| 348 monthly snapshots | 100,000 × 100 × 348 × 8 bytes | 27.84 GB |

These are campaign-level metrics, not per-entity full state. Full entity histories can be far larger; repeated campaigns multiply retained space. Parquet may compress values, but no compression ratio is assumed. Retain compact summaries and bounded selected traces by default, plus pinned inputs/replay assets. Full trajectories are opt-in with a size forecast. Preserve status counts for every evaluation even when detailed traces are discarded. Queries and publication need extra temporary space; the entire free-space allowance cannot be consumed by retained output.

### RAM and concurrency

| Host RAM | Intended use | Illustrative total Lab application budget |
|---|---|---:|
| 16 GB | Practical bounded starting target, subject to M0 measurement | 4–8 GB, leaving room for OS/browser/other work |
| 32 GB | Recommended normal use and campaigns | 10–20 GB, selected from actual available memory |
| 64 GB | Optional larger parallel or detailed replay studies | Configure from measured workload; not required for the first slice |

The application budget includes the parent, workers, queues/buffers and query service, with UI usage accounted for in the host budget. These are not measured minimums or promises of a particular worker count. The earlier 8-worker/16-GB, five-minute screening target stays provisional; correctness and memory limits may require fewer workers or smaller batches. Measure cold/warm latency separately and revise performance scope explicitly if the target fails.

For scale intuition only: 1,000 entities × 64 numeric fields × 8 bytes × two state buffers = 1,024,000 bytes per live world. A batch of 256 worlds on each of eight workers consumes 2.097152 GB for those arrays alone. Queues, beliefs, trace buffers, Python processes and queries add memory. Holding 100,000 such worlds at once would require 102.4 GB just for the two numeric state buffers. Batch execution is therefore essential; the number of retained evaluations does not have to equal the number of live worlds. Actual active-state dimensions and structure-of-arrays layout are determined by M0.

DuckDB can spill supported operations to disk, while its configured memory limit concerns the buffer manager rather than every allocation. Consequently neither a per-query setting nor spill support replaces aggregate application budgets and disk headroom. This follows the official [memory configuration guidance](https://duckdb.org/docs/2.0/configuration/pragmas) and [larger-than-memory workload guidance](https://duckdb.org/docs/2.0/guides/performance/how_to_tune_workloads); these links explain the operational behavior, not the Lab's estimated capacities or a dependency version choice.

Preflight reports projected persistent and temporary bytes and selects bounded worker/batch/query concurrency. Observe actual use during execution. On pressure, reduce future concurrency, pause safely or refuse with a reason; never truncate queues, omit results or silently change fidelity. Cleanup is restricted to disposable unpinned artifacts after transitive bookmark/replay dependencies are checked. Saved results and source evidence cannot be evicted to hide over-budget growth. Test low-disk and low-memory recovery, preserving complete prior results and marking interrupted work incomplete. TL-078 and demonstration 37 make these release requirements, not optional operational advice.
