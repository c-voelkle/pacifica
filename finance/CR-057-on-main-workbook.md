# CR-056 and CR-057 rebuilt on the Civil War workbook (15 November 2026)

**Updated 16 November 2026:** the Deseret step now follows the growth engine in the same chain ([Deseret-workbook.md](Deseret-workbook.md)); residents at the end of 1932 are 37.06m and the workbook's SHA-256 is `6bc8d2aa…`. The figures below are those of 15 November.

SHA-256 of the financial workbook: `5563e1c1f97a6a677fca3f98e46b714697f553fa6d46c090f3d323187a324511` (energy workbook `2c918cc0…`). 81,290 formulas; recalculated in LibreOffice with no errors; saved in the Story case (Levers E4 = 1); iterative calculation on, as in the CR-057 growth build. All amounts are MODEL.

**Why.** CR-057 was approved and its integration prepared on 6 November 2026 (PR #66), but that PR was never merged. The Civil War CRs' model (PR #72, merged 15 November) was built on the CR-051/054/055 workbook, without CR-056 and CR-057. Both changed the same workbook from different bases, so the chain is rebuilt with both, in one order.

## Rebuilding

```
python3 finance/build/cr057_rebuild_pair.py WORKDIR --recalc /mnt/skills/public/xlsx/scripts/recalc.py --passes 8
```

Each pass: energy export → CR-052 link (on the CR-050 workbook, commit `04155c7`) → CR-051/054/055 → **the Civil War CRs** (`cr059_068_civil_war.py`, then `cr059_068_levers.py` with `cr059_068_values.json`, package D final with every later decision) → CR-056 dynamic layer → CR-057 (`c_glide` 0) → the growth engine → LibreOffice → the energy workbook → LibreOffice → export. The last pass adds CR-056's Layers sheet. The pair converged in five passes (the energy outputs moved by at most 1.5e-6 on pass 4 and 5.7e-8 on pass 5, relative).

**Order.** The Civil War steps come before CR-056, because `cr059_068_levers.py` writes its levers from Levers row 408 and requires the sheet to end at row 406, and CR-056 and CR-057 append their levers at the end. Only three places are touched by both chains: the Levers rows, the Changes log and Gold & money column E (gold paid out). All three are appends. Column E keeps the Civil War's private lending (L13) and adds CR-057's run on partner balances (Money I).

## Results

| | `main` before (Civil War, no CR-057) | PR #66 (CR-057, no Civil War) | **This build** |
| --- | --- | --- | --- |
| Story: failed year-checks | 0 | 0 | **0** |
| Stress: failed year-checks | 15 | 52 | **51** |
| Output per person against US history, 1929 (real; money in brackets) | 2.49 (money only) | 2.30 (1.05) | **2.30 (1.03)** |
| Residents, end of 1932 | 38.68m | 36.49m | **36.77m** |
| Japanese- / Chinese-origin, 1932 (population model) | 6.16m / 5.04m | — | **5.77m / 4.84m** |
| Motor vehicles built, 1929 | — | 2.31m | **2.32m** |
| Atomic programme's peak share of output | — | 0.49% (1921) | **0.48% (1921)** |

**The Civil War years are unchanged or a little easier.** Private-saving margins in Stress: 1863 +$1.9m (was +$1.5m), 1864 +$2.9m (+$2.5m), 1867 +$7.0m (+$6.4m); Story margins rise by about $1m a year. No Civil War year fails in either case.

**Stress.** The 51 failures are CR-057's (PR #66 had 52 in the same pattern): nominal commitments fixed in historical dollars against a smaller nominal economy under falling prices. These are the debt ceiling from 1918, the bond markets in 1917–20 and 1931–32, and private saving. Against PR #66, 1916 improves (one failure instead of three) and **1902 is new**: private saving falls short by $0.4m of $793m. Treasury bond subscriptions in Stress are $41.9m that year, against $12.6m in PR #66, which is the Civil War package's debt (the Oregon customs share and the 1867 instalments) carried in a smaller nominal economy. The author's ceiling of 17 for the Civil War package was set on the workbook without CR-057. CR-057's own Stress result of 52 was reported when the author approved it on 6 November 2026 and was not given a ceiling.

**Population.** Re-run (`canon.py`, `flows.py`, `changes.py`, `neighbours.py`); all 18 tests pass. The cohort model and the sheet agree within 0.3% in 1932 (104,000), so Paths C was not re-iterated. The storyline's "about 39 million" (CR-059) goes back to **about 37 million**, the figure the author kept for CR-057. The origin counts become "about 5.8 against 4.8 million of some 37 million".

## Against the storyline

| The storyline says | This build | |
| --- | --- | --- |
| Output per person "about 2.3 times the Union's in 1929" | 2.30× | holds |
| "about 39 million" in 1932 (§-overview, §37) | 36.77m | **re-synced** to about 37 million |
| "about 6.2 against 5.0 million of some 39 million" | 5.77m / 4.84m | **re-synced** to about 5.8 against 4.8 of some 37 |
| "about 2.3 million vehicles a year" | 2.32m | holds |
| The atomic peak "about half a percent of national product, in 1921" | 0.48%, 1921 | holds |
| "about 1.2 million people by 1861" | unchanged by CR-057 | holds |
| Pacifica alone outproduces the Union at its prices from 1927 | 0.98× in 1927, 1.03× in 1928 (output per person × residents at US prices against the modelled Union) | **re-synced** to from 1928 (16 November 2026) |
| The order at about 1.16 and 1.74 times Union output in 1929 and 1932 | in money 1.0× and 1.67×; at the Union's prices 1.54× and 2.22× | **re-synced**, both bases stated (16 November 2026) |

## Open

- Whether the Stress case's 51 failures need a ceiling now that both packages sit in one workbook (the author's decision).
- The 1902 Stress shortfall ($0.4m) is a margin, not a structural failure. Raising the Stress `cw_idle_ratio` would not reach 1902, because L17 applies only to 1861–65.
- The open items of `CR-057-growth-workbook.md` (the unconfirmed loop through the 1927 Japan rescue; G8 simplified) and of `CR-059-068-workbook.md` stand.
