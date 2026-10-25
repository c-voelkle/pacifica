# Timeline Lab — build brief

**25 October 2026 · Prototype brief, version 1**

This is the only document an implementing agent reads. The full specification in `docs/timeline-lab/` (revision 0.10) is a frozen reference. Do not load it into context, and do not add requirements from it unless the author asks.

## The question

What else could plausibly have happened in the 1927–28 Japan rescue and Concord crisis, depending on Julian's choices, and which of those histories make good plot?

The prototype succeeds if one evening with it gives the author a plot idea he would not otherwise have had. It fails if it only reproduces the canon or produces noise.

## What to build

A small local Python tool with four parts:

| Part | What it does | Rough size |
|---|---|---|
| `model.py` | World state, actor rules, monthly step, event log | 600–1,000 lines |
| `run.py` | Command line: run N worlds for a lever setting, run a lever grid, replay one seed, export JSON | 150–300 lines |
| `app.py` | Streamlit page: lever controls, outcome charts, history list, single-history timeline | 300–600 lines |
| `tests/` | The checks under "Done means" | 200–400 lines |

All scenario content lives in `scenarios/1927_rescue.yaml`. Code reads it; code never hard-codes actors, amounts or dates.

**Stop and report** if the prototype passes about 2,500 lines, or if a feature seems to need anything on the "Not now" list.

## Scope

- **Window:** March 1927 to December 1928, one step per month.
- **Actors:** the seven in the YAML. Julian is the only controlled actor. Everyone else decides by their own rule.
- **Pacifica levers:** credit size, public share, whether the credit is tied to the Concord, consent path (wait for the Senate, provisional application, or renegotiate first), offer month and the 1928 concessions offered to the Senate.
- **Uncertainty:** the drivers listed under `uncertainty` in the YAML, sampled per world.
- **Runs:** 1,000 worlds per sketch by default, 10,000 on request. Plain Python loops are fast enough at this size; no vectorization, compiled layout or parallelism.

## How it works

1. Load the YAML and validate it with a small Pydantic model. Reject unknown keys.
2. For each world, draw its uncertainties from `random.Random(seed)`, where the seed is derived from the scenario hash and world number. No global random state.
3. Each month, in fixed order: apply scheduled events; each actor builds its observation from what it has actually been told; each actor decides; resolve actions; update state; append to the event log.
4. Decisions are a small utility comparison plus noise, with the weights in the YAML. Beliefs are a few numbers per actor, updated only by events that actor observes.
5. **Branching:** replay the same seed to a chosen month, change one Pacifica decision, and continue. No state snapshots are needed because runs are deterministic.
6. Output per world: the event log and the final measures listed in the YAML.

## What the author sees

- Lever controls and a **Run** button. Results for 1,000 worlds should appear within a few seconds.
- **Outcome table:** counts of each end state (Concord consented, Concord lapsed, Japan stops paying, yen falls, cabinet falls, and so on), compared with the previous run under the same seeds.
- **Charts:** median and 10–90% band over time for four to six measures.
- **Five most different histories:** pick by distance between event sequences, so the list shows different plots rather than five near-copies of the median.
- **Timeline of one history:** month by month, marking Julian's decisions, other actors' responses and chance events separately.
- **Grid sweep:** run every combination of a few lever values and plot two measures against each other, so trade-offs are visible.
- **Export:** one history as JSON, so the author can paste it into a chat and ask for narration, explanation or a scene.

## Rules that always hold

1. Julian controls only Pacifica's decisions. Other actors can refuse, counter or change course.
2. No actor sees the future or another actor's private state. Beliefs change only through observed events.
3. Failures, collapses and illegal outcomes stay in every count. Nothing is filtered to make results look better.
4. Unknown is never zero. A missing value stops the run with a clear error.
5. No Excel, database server or network access at runtime.
6. Canon outcomes in the YAML are references for comparison, never forced events.
7. Every number carries its label: `MODEL` from the canon's own estimates, `LAB` invented for this prototype. The tool shows the label.
8. Generated histories are drafts, never canon. Nothing the tool produces changes `book-agent/`.
9. Protected ambiguities stay unresolved. The Altai secret stays withheld; no actor learns it.
10. Persons stay distinct from institutions. Takahashi stays in Tokyo and is not a common minister in any generated history unless the author adds that as an explicit premise.

## Done means

- [ ] A fixed seed gives an identical event log on every run.
- [ ] A world run alone and inside a batch of 1,000 gives the same result.
- [ ] An actor never reacts to an event it did not observe (test with a concealed event).
- [ ] With canon lever settings, the canon sequence appears among the outcomes, but other outcomes appear too.
- [ ] Changing one lever with the same seeds changes some histories and leaves the matched external draws identical.
- [ ] Replaying a seed to a month and changing one decision reproduces every earlier month exactly.
- [ ] Credit drawn never exceeds credit committed; public exposure equals drawn credit times public share.
- [ ] The app runs locally with `streamlit run app.py` and shows all views above.

Then the author uses it for an evening and decides what, if anything, to build next.

## Not now

Each of these is in the 0.10 specification. None is part of this prototype:

- LLM extraction of story content, source audits and omission tests
- The full ontology, conduct profiles and simultaneous resource settlement
- Optimizers (NSGA-II, MAP-Elites), adversarial search, held-out assessment
- History-type clustering beyond "five most different"
- Exact decimal ledger, six-fixture parity, finance-skill integration
- DuckDB, Parquet, manifests, compiled array layouts, memory and disk budgeting
- React, FastAPI, general catalog editor, built-in LLM narration
- Formal author-trial protocols and p95 benchmarks

## Working rules for agents

- Read this brief, the YAML and the code. Nothing else from `docs/timeline-lab/`.
- Read `book-agent/` sources only when the author asks to add or check content, and then only the named passage.
- Keep changes small and runnable. Run the tests before reporting.
- Ask before adding an actor, lever, dependency or requirement.
- Report actual size, run time for 1,000 and 10,000 worlds, and anything that did not fit.
