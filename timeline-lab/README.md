# Pacifica Timeline Lab — bounded dramatic sketch 0.2

Explore the March 1927–December 1928 rescue and Concord crisis through independent actor responses, explicit commitments, causal story candidates and traceable metrics. All generated histories and additional relationship premises are DRAFT / LAB. Whether an idea is useful remains the author's judgment.

## Start locally

From timeline-lab/ with Python 3.12 or later:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
streamlit run app.py
```

On macOS/Linux use `source .venv/bin/activate`. Dependencies remain the approved Pydantic, Streamlit and PyYAML. There are no external model/calculation services or database requirements. For Community Cloud select this branch and `timeline-lab/app.py` with forward slashes; private repositories require Streamlit's repository access. Dependencies are beside the entry point. The local theme/localhost configuration applies when launched from this directory.

## Try a relationship-driven fork

1. Open **Story exploration** and select **Discover story alternatives**. The bounded family varies assurances, priority and concession packages; it shows policy settings, shared external worlds and total evaluations separately.
2. Filter **Broken assurance** or **Disclosed breach**. Read the goal, obstacle, actual choice, supported consequences and the next-question prompt. Causal representatives include financially similar histories and failures, independently of strategic rank.
3. Open **Why did they choose this?** to inspect the actual procedure, alternatives, observed information and private inputs. Private information is visible to the author, not automatically to other actors.
4. Use **Metric definitions, inputs and evidence** to inspect quantities. Missing cash or consent dates remain explicit; trust and influence are LAB proxies.
5. Select a history with a private assurance and omitted requested concessions. At the configured settlement month, branch `commitment_priority` between `honour_assurance` and `preserve_discretion`. Compare actual oversight terms, cooperation, legality and the recorded outcomes under the same external draws.
6. Keep an idea with **Bookmark this history** and download its bundle. A downloaded bookmark embeds the scenario, history and ontology evidence and can be verified/replayed through the upload control. Cloud server files may be temporary; downloading retains the bundle independently.

The baseline financing and consent controls, outcomes, six ensemble charts, world replay, lever grid and raw history export remain available. A branch changes one continuing policy setting from a month; it is conditional consequence evidence. It is not a general isolated-action, premise or imposed-event intervention service, and an already-made assurance cannot be erased.

## CLI

```powershell
python run.py batch --worlds 1000 --output exports/reference-v2.json
python run.py explore --worlds 25 --output exports/story-alternatives-v2.json
python run.py replay --world 0 --set assurance_strategy=private --set commitment_priority=preserve_discretion --set 'concessions_1928=[]' --output exports/private-breach-v2.json
python run.py restore-bookmark exports/bookmarks/BOOKMARK_ID.json --output exports/restored-v2.json
python run.py grid --axis 'credit_size_musd=[400,600]' --axis 'public_share=[0.25,0.5]' --worlds 100 --output exports/grid-v2.json
python run.py benchmark --output exports/benchmark-v2.json
python -m unittest discover -s tests -v
```

New export filenames are required. Repository outputs are restricted to timeline-lab/exports/. Bookmarks reject a conflicting overwrite. Scenario schema 0.2 is closed and intentionally does not silently migrate 0.1 exports: retain the older commit/runtime to replay old histories. A seed alone does not identify an experiment.

## Model meaning and limits

[BRIEF.md](BRIEF.md) defines the authorized extension; [ONTOLOGY.md](ONTOLOGY.md) describes implemented records and distinctions; [backlog.json](backlog.json) maps partial original-spec coverage and remaining work. This is not full revision 0.10 R0 acceptance.

The private/public settlement assurance is an explicit LAB premise, not newly adopted canon. Honouring it adds the configured oversight terms to the requested offer. A discretion-first policy may breach it. The mediator reacts only after receiving the actual terms, may withdraw without public disclosure, and may publish a breach report. Other recipients apply their own credibility thresholds. A political breach can be lawful; legality, fulfilment, belief and cooperation are separate states.

Concessions have different declared legislative and mediation effects. The model records actual offered terms when the intention-sensitive procedure differs from the requested package. Original trust and military scores remain simplified indices, not universal psychology. The legislative threshold remains a utility rule, not a counted two-thirds vote; no seat margin is displayed. Story cards are deterministic evidence views; unassessed sacrifice and subjective intentions remain unassessed. A proposed next dilemma is not a simulated future event.

Funding need uses the original external-need estimate plus a linear sensitivity to nonrenewal. A LAB $375m reserve decomposition distinguishes bills due from the funding target; it is not a newly approved model amount. A reserve miss can cause a second run even when payments are met. Bank losses, capital, BOJ and lender holdings remain context, not a reconstructed financial ledger. Treasury opening cash, fiscal spending, repayments and import-cover weeks remain unmodelled.

The deadline precedes that month's replies. Counteroffers do not automatically change Julian's levers. A public cap retains the underwriting ratio; private-only fallback records an effective zero public share. Drawing respects usable capacity and public drawing equals total drawing times effective public share. Credit without appropriation is logged and grants no treaty authority. Conditional ratification lapses at the configured horizon under a LAB rule; no court judgment is invented. Future canon text is reference-only. Protected secrets are not discoverable state.

Automated verification covers replay, privacy, relationship counterexamples, differentiated concessions, matched financial outcomes, ontology links, missing metrics, narrative selection, bookmark integrity and Streamlit workflows. The author's retain-and-branch trial remains pending. Timings and measured size are recorded with the implementation validation after the final run; version 0.1 timings do not establish version 0.2 performance.

## Measured validation

On 25 October 2026, all 36 regression checks passed, including both Streamlit flows. The 14 focused ontology/relationship/bookmark checks also passed after the final evidence-link addition. CLI open exploration and bookmark restore passed; a live browser displayed a disclosed-breach scenario. Dependency and diff checks passed.

The host simulation benchmark measured **2.68 seconds for 1,000 worlds** and **28.17 seconds for 10,000 worlds**. These are single measurements, not p95 or rendering guarantees. The bounded source, scenario, docs and tests total approximately 3,500 lines (approximately 200 KB), below the revised brief budget; virtual environments and exports are additional.
