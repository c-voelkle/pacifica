# Pacifica Timeline Lab prototype

The bounded sketch in [BRIEF.md](BRIEF.md): seven actors, monthly steps, matched worlds, a CLI and a local Streamlit app. The author's evening with it is the test of whether it produces useful plot ideas. The engine's counts do not establish historical likelihood.

## Run locally

Python 3.12 or later. Create a virtual environment, activate it, then install the requirements:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
streamlit run app.py
```

On macOS/Linux, activate with `source .venv/bin/activate`. Run commands from `timeline-lab/`. The app binds to localhost and disables Streamlit usage telemetry. It has no external service, Excel, database or LLM calls. Network access is needed only to install dependencies.

## Explore

- Run the reference choices, then change a lever and run again. Equal-size runs use matching world numbers and external draws; the outcome table shows count differences.
- Inspect six median / 10–90% charts and five histories selected for differing dated event sequences. Every failed rescue, collapse and illegal outcome stays in the totals.
- Replay any world or change one decision at a selected month. Earlier events remain identical. The app rejects changes to credit already settled or consent already obtained.
- Sweep a small grid and compare two outcome measures. Grid points reuse the same worlds. Export one history as JSON for a writing conversation.
- Read **Assumptions** before interpreting a result. It shows the entire scenario, labels, protected facts and remaining open items.

## CLI examples

```powershell
python run.py batch --worlds 1000 --output exports/reference.json
python run.py batch --worlds 1000 --set credit_size_musd=400 --output exports/smaller-credit.json
python run.py replay --world 37 --output exports/world-37.json
python run.py replay --world 37 --branch-month 1928-01 --change 'concessions_1928=[]' --output exports/branch-37.json
python run.py grid --axis 'credit_size_musd=[400,600]' --axis 'public_share=[0.25,0.5]' --worlds 1000 --output exports/grid.json
python run.py benchmark --output exports/benchmark.json
python -m unittest discover -s tests -v
```

Export filenames must be new. Within the repository, the CLI writes only under `timeline-lab/exports/`; it never overwrites canon, scenario inputs or code. Exports include the full scenario, its hash, seed, world number, lever settings, branch edit, draws, events and measures. Replay requires those same scenario inputs and engine version; seeds alone are not portable between model changes.

## Explicit LAB interpretations

All source content lives in [the scenario YAML](scenarios/1927_rescue.yaml). Its `execution` section identifies actor/world roles, dates, event bindings and numerical assumptions needed to execute the original prose. Code contains role rules, not character identities or financial amounts. Changing actors, levers, dependencies or requirements still requires the author's agreement under the brief.

Actors decide from facts delivered to them before resolution. Votes, offers, subscriptions and observed institutional conditions are public; trust, utilities and private draws are author-visible only. One actor's same-month decision cannot give another actor advance knowledge. The full random tape is drawn before the first decision and reused for matched comparisons and branches.

Responses carry the offer revision they address. If Julian changes terms while other actors answer an earlier offer, those answers remain in the history but do not authorize the revised offer; the actors must respond again next month. Competing offers affect the government's choice only after a private notification is delivered to it.

The public external-need estimate equals the source baseline plus short foreign funding times the deviation in nonrenewal from the source baseline rate, floored at zero. This linear sensitivity is a LAB approximation. Existing bank-loss, recapitalization, BOJ and named foreign-holding figures remain scenario context; this prototype does not reconstruct bank balance sheets, fiscal cash, repayment or the full financial workbook.

The YAML explicitly assigns a LAB $375m reserve buffer to separate the six-week reserve target from bills due. Payment need is the remaining target after that buffer, floored at zero. Missing the reserve target can cause a second run even when June's bills are paid; it is not automatically a payment default. The app flags that distinction. This decomposition is a prototype assumption, not a new canon or financial-model approval. The moratorium month suppresses run-pressure loss; it does not stop political obstruction.

The scheduled payment deadline occurs before that month's decisions. A late offer may therefore fail even if actors agree later that month. Counteroffers request more or untied credit but do not automatically change Julian's levers. Concessions arrive in the configured settlement month, or earlier under `renegotiate_first`. Failure to obtain consent by the sketch's end lapses conditional ratification; this end-date rule is LAB. Changing control settings never gives the executive other actors' votes.

A public cap limits capacity while retaining the offered underwriting ratio. If the executive selects `private_only` after a loan refusal, the effective public share becomes zero and the private commitment limits the facility. The export and timeline series record that effective share; public drawing always equals actual drawing times that share. Credit without an appropriation is explicitly logged, and never supplies treaty authority.

Canon-reference text is a comparison only. Generated decisions carry LAB status even when they resemble an APPROVED reference. Protected secrets are not represented as discoverable state; the engine cannot generate their revelation or invent a murderer. Persons listed inside institutions remain descriptive people, not additional controlled actors.

The YAML is validated before a run. Missing numerical inputs, extra record keys, unsupported executable keys, invalid lever values and nonfinite inputs stop execution. Editing YAML changes the scenario hash and the world seeds; compare levers within one scenario for matched external draws. No general scenario editor or new scenario mechanism is included.

## Validation on 25 October 2026

All 21 unittest checks passed, including the Streamlit run, matched comparison, branch, grid and export controls. `pip check` and `git diff --check` passed. A live localhost browser run rendered the outcome table, six charts and history timeline; 1,000 worlds took 4.58 seconds in that UI run. CLI single-history export also passed.

The final CLI benchmark measured **3.29 seconds for 1,000 worlds** (52,021 events) and **254.93 seconds for 10,000 worlds** (519,718 events). These are single local measurements, not a latency guarantee. The optional 10,000-world run is currently slow; start with 1,000. Timing covers simulation, not subsequent chart rendering.

Size: 1,448 Python lines including tests, approximately 2,020 lines including the scenario, brief, setup and documentation, and approximately 114 KB of source files. Installed dependencies and generated exports are additional. No feature from the brief was dropped or taken from the frozen full specification. The remaining acceptance step is the author's evening of exploration: automated checks do not establish plot quality or historical probabilities.
