---
session: 20261105-dynamic-layer
started: 2026-11-05
updated: 2026-11-05
mode: draft
status: paused-for-author
baseline:
  commit: 961ebae
  files:
    finance/Pacifica_financial_model_1846-1932.xlsx: sha256:cba70b3147a71cc9c0a4b977eeae3bca5de69313255723b167d5dc398c87059e
    energy/Pacifica_energy_model_1846-1932.xlsx: sha256:89807a6664a2beebc3056f289f8cef17467c2955b2438fbb9d98778acd8dfc17
independence: separate-context review of the build (general-purpose agent, given the scripts, the note, the energy diff, AGENTS.md, storyline §33–§34 and the design note)
---

# A switchable dynamic layer for the financial workbook: the second- and third-order effects of Pacifica's investments

## Brief

- **Desired outcome:** a dynamic layer on top of the accounting baseline that turns physical investment into productivity, prices, wages, hours and household life, with a "life in Pacifica" table for the storyline.
- **Authorization:** author, 5 November 2026: "Can you please build the model described here?" (the handoff of 5 November); then, on the design note: "either replace Paths!L after about 1900 with growth derived from capital, power and spillovers, or keep it as the frontier baseline and add the new channels on top. Then compare the result against Pacifica's own story, not against US history." No canon change.
- **Sources:** the handoff; `finance/investment-share-note.md` v2; `finance/CR-051-054-055-workbook.md`; `finance/CR-052-workbook.md`; `energy/CR-052-workbook.md`; the workbooks' formulas.

## Author decisions and open choices

| ID | Type | Statement | Source | Status |
| --- | --- | --- | --- | --- |
| D1 | author decision | Build both modes (replace `Paths!L`; frontier plus channels) and compare with Pacifica's own story | author, 5 Nov | applied (`dyn_mode` 1, 2) |
| Q1 | open choice | Does "frontier baseline" keep the rule of counting only Pacifica's lead over the Union? (`dyn_vs_us`, saved 1) | review finding | open |
| O1 | open choice | Which mode, if any, becomes Story | CR-056 note, decision 2 | open |
| O2 | open choice | §34's 1932 sentences fail in the accounting model (money ahead from 1924, real from 1930) | CR-056 note, decision 3 | open |
| O3 | open choice | The slump: keep it monetary or make the power estate countercyclical | CR-056 note, decision 4 | open |
| O4 | open choice | Verify the life table's US anchors | CR-056 note, decision 5 | open |

## Round log and stop reason

| Round | Date | What changed | Stop reason |
| --- | --- | --- | --- |
| 1 | 2026-11-05 | Design note `finance/dynamics-design-note.md` | Blocked on Q1–Q12 |
| 2 | 2026-11-05 | Build: `cr056_dynamics.py`, `cr056_layers.py`, `cr056_identity.py`, energy exports, workbook note | Review |
| 3 | 2026-11-05 | Review fixes: no electricity term in mode 2; `dyn_vs_us`; Fund netting on C4/C5; women into Labour B; Union comparator and GDP deflator; §34 tests split and run on 1932; slump against the 1920s trend; figures corrected | Author's choice of mode (O1) and Q1 |

## Resume here

Workbook `a579fee5…` on branch `finance/dynamics-layer`, saved at `dyn_mode` 0 (identity holds in Story and Stress). PR open for the author; do not merge before the author answers. On the author's answers: set the chosen mode and `dyn_vs_us` as Story, re-run `cr056_layers.py`, and if a mode is adopted let the energy workbook read it and re-sync the storyline's MODEL figures.
