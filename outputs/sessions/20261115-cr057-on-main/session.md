---
session: 20261115-cr057-on-main
started: 2026-11-15
updated: 2026-11-16
mode: integration
status: paused-for-author
baseline:
  commit: 28b7263
independence: self-review only (no fresh-context reviewer was run); the merge and the model rebuild are by the drafter
---

# CR-057 (with CR-056) rebuilt on `main` after the Civil War integration

## Brief

- **Finding (author, 15 November 2026, 21:51):** the project marks CR-057 approved and integrated on 6 November, but `main` still has the old Development Fund paragraph, the Crown's 25% and no Reserve Bank of 1857. Cause: CR-057's integration sat on PR #66 (draft, never merged), and the Civil War model of PR #72 was built without CR-056 and CR-057.
- **Authorization (author, 21:57):** "Yes please" to rebuilding PR #66 on today's `main`: re-applying the canon text, rebuilding the model chain with the Civil War steps, re-running population and the checks, then closing #65 and #66 in favour of the new PR.
- **Branch:** `adopt/cr057-on-main` from `main` at 28b7263 (PR #72 merged).

## What was done

- **Standalone files** taken from `draft/cr057-economic-order` unchanged: CR-057.md, the CR-056 and CR-057 workbook notes and build scripts, the dynamics design note, the energy build and workbook, the Mises review and the session records of 5–6 November.
- **Text files** merged three ways (base 961ebae, `main`, PR #66): the storyline, bible, background, AGENTS, finance README, ledger and register. Every conflict was an append and both sides are kept, CR-057 before CR-058 in numeric order. In one paragraph (CR-027's regency government) CR-057's change to the Crown's shares and the Patrimony was combined with CR-058-R1's Doheny sentence. The character registry was merged entry by entry: the text merge had dropped main's 69 new persons, which are restored. The result is 302 identities. A line check confirms that no added line from either side was lost.
- **Model:** `cr057_rebuild_pair.py` now runs the Civil War steps between CR-051/054/055 and CR-056. It converged in five passes. See `finance/CR-057-on-main-workbook.md`.
- **Population** re-run; 18 tests pass. The storyline's population figures are re-synced (about 37 million; 5.8 against 4.8 million).
- **Consistency read of the merged storyline (self-review):** CR-069's "choice of paper" is the Union's and does not touch the convertible Reserve Bank. CR-069's run of 1862 ("this time they carry themselves") reads correctly after a Reserve Bank of 1857, which never needs to lend. CR-070's five per cent royalty predates the Patrimony (1880). No passage states the Crown's twenty-five percent or the old Development Fund rule.

## Findings for the author

1. **Stress: 51 failed year-checks** (PR #66: 52; the Civil War workbook alone: 15, ceiling 17). They are CR-057's own (nominal commitments under falling prices). One is new: 1902, private saving short by $0.4m of $793m. The Civil War years are a little easier than before.
2. **"Development Fund credit" before 1880.** CR-059 V9 and Part IX finance Oregon's and Columbia's works of 1868–75 on Development Fund credit. In the storyline, both before and after CR-057, the Development Fund begins in 1880, as the Patrimony's lending arm under CR-057. This predates CR-057 and is not changed here. A naming decision (for example "the Treasury's works credit" before 1880) would need a small CR.
3. **The 1862 run and the Reserve Bank.** The storyline does not say what the Reserve Bank does during the run of January 1862. Nothing contradicts it, but a reader may ask. Left as is.

## 16 November 2026: Deseret

- **Authorization (author, 07:02):** "Yes go ahead and add it", on the proposal of 06:57: a line for the Saints in the model, the gathering continuing after 1887 (no Edmunds–Tucker), plural marriage adding no births by itself.
- `finance/build/deseret_gathering.py` (Deseret sheet, five levers; identity build exact), added as the chain's last step; the pair re-converged in five passes. `population/canon.py` reads the sheet and carries the stream "Deseret" (gap test passes; reconciliation 0.2% in 1932). Residents 37.06m; Story 0, Stress 51. See `finance/Deseret-workbook.md`.
- The storyline is unchanged: its figures hold, and the gathering's survival is not yet stated there (proposed for the author).

## Resume here

- PR for `adopt/cr057-on-main` waits for the author's sign-off; do not merge before it.
- After the merge, close PR #66 (`draft/cr057-economic-order`) and PR #65 (`finance/dynamics-layer`) as superseded, and retire their branches with `adopt/cr059-070`, `revision/cr069-gold` and `models/cr059-068-civil-war` (this session cannot delete branches).
- Open for the author: a Stress ceiling for the combined workbook; findings 2 and 3 above; a fresh-context review of the merged storyline if wanted (not run).
