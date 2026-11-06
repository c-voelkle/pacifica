# Workbook note, 6 November 2026: the growth engine (CR-057 follow-up)

SHA-256 `cf18730e132c3192f042b1965ff2010e1d8e538970315a4e040ddd0e5b4d842b` (energy workbook `b59af946…`). Status: PROPOSED; the author's decisions of 10:45 are applied, and the workbook awaits integration with CR-057. No canon text, register, facts file, character file or ledger is changed. All amounts are MODEL.

**Authorization.** The author, 6 November 2026:
- on the design note: "Yes that sounds much more accurate";
- the answers of 09:18, 09:48 and 10:06;
- at 10:45: "1. yes 2. falling prices 3. ok 4. agreed. Please proceed with the three suggested steps. Bear in mind that US Steel does not exist in this timeline (or is much smaller) because Carnegie Steel was bought by a SF syndicate and became Pacifica Steel, the world's first billion dollar company, in 1901."

## The chain

Each pass of [`build/cr057_rebuild_pair.py`](build/cr057_rebuild_pair.py) runs:
1. the CR-050 workbook (commit `04155c7`);
2. the CR-052 link;
3. CR-051/054/055;
4. the CR-056 dynamic layer;
5. CR-057, with `c_glide` 0 (the 1913 cover held);
6. the growth engine;
7. LibreOffice;
8. extract, the energy workbook, LibreOffice, export.

The pair converged in six passes. The energy outputs moved by at most 8.8e-6 on pass 4, 1.3e-6 on pass 5 and 7.1e-8 on pass 6 (relative). On the last pass, the Layers sheet (CR-056's six cases) is rebuilt on the converged CR-056 build, and CR-057 and the engine go on top of it. LibreOffice then recalculates the workbook with no errors.

**Identity checks** (6 November, on the same chain; numeric cells, tolerance 1e-9; Levers, Changes and Start excluded):
- `c57_on` 0 and `g_on` 0 reproduce CR-056's saved values: 90,899 cells, none differ.
- `g_on` 0 reproduces the CR-057 build on CR-056: 99,971 cells, none differ.
- The `--off` build reproduces it too.

The comparison is run by [`build/cr057_growth_variants.py`](build/cr057_growth_variants.py).

## What is built

[`build/cr057_growth_engine.py`](build/cr057_growth_engine.py), with one master lever `g_on` (saved at 1; 0 reproduces the input) and a `Growth` sheet:

| Channel | Mechanism | Main levers (Story · Stress) |
| --- | --- | --- |
| G2/G3 research and diffusion | Research stocks per unit of output for Pacifica, the Union and the world, depreciating at `g_dep`. They enter after an adoption lag: 3 years under open licensing, 6 under exclusive licences. The usable share of the patented part is `g_open` against `g_excl`. Absorption of the world's stock rises with own research, and a quarter of Pacifica's stock leaks to the Union. TFP lead = MAX(1, Pacifica's effective stock / the Union's)^`g_gamma` | `g_gamma` 0.12 · 0.08; `g_dep` 0.15 · 0.20; `g_pat` 0.3; `g_open` 0.9 · 0.8; `g_excl` 0.6; `g_leak` 0.25 · 0.30. Research path: Pacifica 0.6% (1880), 1.2% (1900), 1.8% (1913), 2% (1929); the Union 0.05%, 0.1%, 0.15%, 0.25% |
| G4 learning by doing | Seven sectors. Experience = the leader's world share + 0.3 × the rest (Irwin and Klenow), Pacifica's leader against the Union's. The cost advantage b × ln(E_P / E_U) is weighted by gross output / GDP. **Steel follows canon:** from 1901 Pacifica's leader is Pacifica Steel (Carnegie's plants plus the Pacifican mills, about 0.16–0.17 of world output). The Union's leader is the trust formed without Carnegie (0.12–0.14). Before 1901 the Union's leader is Carnegie. Experience is the firm's wherever its plants are; only the Pacifican mills are in Pacifica's GDP | Steel 24% → 15%, cars 15%, chemicals 15%, electrical 10%, power 10%, aluminium 15%, aircraft 15% → 10% |
| G6 capital | Stock of gross domestic investment (Energy link AA, public and private alike), depreciating at `k_dep`. Level ((K/Y) / (K/Y)_Union)^(α/(1−α)) against the Union's s / (g + δ) | `k_alpha` 0.3, `k_dep` 0.04, `g_su` 0.21 |
| G6b network premium | `g_prem` × (1 − coverage) on core network investment. Power uses the energy workbook's power investment, with homes wired as coverage. Rail, ports and the canal are `g_core` × GDP, with a coverage path. It enters as a growth increment in Economy D | `g_prem` 0.08 · 0.04; `g_core` 0.01 |
| Research in the accounts (decision 3) | The state's half (`g_pub`) of the research path, beyond the research already in Technical programmes (`g_tp_res` 0.75 of GDP × Paths V), goes to a new Budget line AF and into government consumption (Energy link AE) | `g_pub` 0.5, `g_tp_res` 0.75, `g_charge` 1 |

**The hooks:**
- Economy D becomes the network premium alone. The Development Fund's 30% return and CR-057's Patrimony term both go.
- Economy J is multiplied by (1 + the level factor).

**Unchanged:** G1 (`Paths!L`), G5 (talent), G7 (mining, the Gulf) and the champions' block. The research level multiplies non-mining, non-champion output only. This is G8 simplified: the champions' world shares are not yet driven by G2 and G4.

**Iterative calculation is enabled** (200 iterations, delta 1e-7). CR-057's money block and the 1927 Japan rescue close a loop:
- Money N reads the rescue's callable balances from 1928;
- the rescue's private share reads 1927 investment abroad, which reads 1927 output.

LibreOffice reported the loop (Err:522) once the engine changed the path. With iteration on it resolves, and no value moves at `g_on` 0.

## Results, Story case (saved: CR-057 with the engine, falling prices)

GDP per person against US history, at US prices (Economy T). Economy R, money, is in brackets where it differs.

| Variant | 1900 | 1913 | 1920 | 1929 | 1932 |
| --- | --- | --- | --- | --- | --- |
| Old design, accounting (the model before CR-057) | 2.17 | 2.29 | 2.42 | **2.38** | 2.83 (3.17) |
| Old design, engine | 2.24 | 2.28 | 2.35 | 2.22 | 2.76 (3.08) |
| CR-057, accounting, falling prices | 1.96 | 1.93 | 1.98 (0.83) | 1.87 (0.87) | 2.21 (1.35) |
| **CR-057, engine, falling prices (saved)** | **2.24** | **2.28** | **2.35 (1.01)** | **2.24 (1.11)** | **2.78 (1.84)** |
| … research to 3% | | | | 2.29 | |
| … cautious (γ 0.07, no premium) | | | | 2.00 | |

**1929 in detail:**

| Variant | Real GDP (1913 $m) | Real per resident ($) | Residents (m) | Price level (1913 = 1) | Residents, end 1932 (m) |
| --- | --- | --- | --- | --- | --- |
| Old design, accounting | 44,524 | 1,333 | 33.4 | 1.60 | 36.8 |
| Old design, engine | 40,899 | 1,247 | 32.8 | 1.60 | 36.0 |
| CR-057, accounting | 32,824 | 1,074 | 30.6 | 0.68 | 33.3 |
| **CR-057, engine (saved)** | **42,844** | **1,275** | **33.6** | **0.75** | **36.8** |

**What the results show:**
- **The storyline's 2.24× holds exactly.** Its 1932 "about 37 million" holds too, at 36.8m against 36.75m before. The storyline's kilowatt-hours ("about 2,600 a head in 1929") hold at 2,635.
- **Prices fall as MR-01 asks.** The price level goes from 1.00 in 1913 to 0.83 in 1920 and 0.75 in 1929. Money income per person is then 1.11 times US history, and real income 2.24 times.
- **CR-057 costs no output once capital earns the ordinary return.** With the engine, the old design and CR-057 are identical to 1913. By 1929 CR-057 is slightly ahead: $1,275 against $1,247 per resident, because the migration pull reads the lead at US prices and the lower price level helps.

**The engine's channels (saved case):**

| Channel | 1900 | 1913 | 1929 |
| --- | --- | --- | --- |
| G2/G3 research lead | +30.5% | +27.8% | +22.5% |
| … of which open licensing | 1.1% | 1.0% | 1.0% |
| G4 learning (all seven sectors) | −0.1% | −0.0% | +0.2% |
| G6 capital | −9.2% | −3.4% | +4.6% |
| G6b network premium, cumulative from 1847 | | | +3.9% |

**What the channels show:**
- **Learning by doing, by sector in 1929:**

| Sector | 1929 |
| --- | --- |
| Steel | +0.04% |
| Cars | −0.19% |
| Chemicals | +0.09% |
| Electrical | +0.07% |
| Power | +0.13% |
| Aluminium | +0.02% |
| Aircraft | +0.01% |

  With Pacifica Steel in canon, steel turns from −0.17% to a small plus. Learning still adds little, because spillovers are international and the sectors' weight in GDP is small.
- **The research lead is largest about 1900 and narrows as the Union's intensity rises.**
- **Capital dilutes before 1913,** because arrivals outrun the investment share, and deepens in the 1920s.

**Research in the accounts (decision 3):**

| | 1913 | 1929 |
| --- | --- | --- |
| The state's half of research | $161m | $340m |
| … already in Technical programmes | $108m | $204m |
| New Budget line AF | $54m | $136m |
| The Patrimony's transfer to the Budget | $97m | $302m |

The Story checks still pass in every year. The 1932 deficit is −$890m, from CR-057's rule of no tax rise in 1930–32.

## Stress

| Variant (1929) | × US at US prices | Real per resident ($) | Residents, end 1932 (m) | Year-checks failing |
| --- | --- | --- | --- | --- |
| CR-057, engine | 1.61 | 900 | 20.6 | 59 |
| … research to 3% | 1.63 | 911 | 20.8 | 62 |
| … cautious | 1.56 | 868 | 20.1 | 65 |

Before this round, the 5 November accounting case failed 52 year-checks and the model before CR-057 failed 17. The extra failures are CR-057's nominal commitments under a money rule with falling prices, as in the 5 November note. Holding the 1913 cover lowers the Stress price level further.

## The population model (re-run)

The population model's scripts (`population/canon.py`, `flows.py`, `changes.py`, `neighbours.py`) were re-run on the new workbook. All 15 tests pass. The sheet and the cohort model now differ by:

| | 1880 | 1900 | 1932 |
| --- | --- | --- | --- |
| Gap (sheet − model) | +17,000 (+0.4%) | −12,000 (−0.1%) | −244,000 (−0.7%) |
| Before this round | | | −55,000 |

Paths C (the natural-increase rate) was last re-iterated with CR-041 and was not re-iterated here. Iterating it would lower the 1932 sheet total by up to about 0.2m.

The engine's early capital dilution makes Pacifica's lead a little smaller in the 1860s–80s, so the early populations are lower:

| Year | Before | Now |
| --- | --- | --- |
| 1861 | 1.24m | 1.21m |
| 1880 | 4.16m | 3.93m |

The storyline's "about 1.2 million" in 1861 holds.

## Against the storyline (MODEL figures to re-sync at integration)

| The storyline says | Now | |
| --- | --- | --- |
| Output per person "about 2.24 times the Union's in 1929" | 2.24× | holds |
| "about 37 million" in 1932 | 36.8m | holds |
| "about 1.2 million people by 1861" | 1.21m | holds |
| "about 2,600 kilowatt-hours a head in 1929" | 2,635 | holds |
| "about 96 per cent of homes are wired" (1929) | 8.52m of 8.88m homes, 96% | holds |
| "Pacifica builds about 2.2 million vehicles a year" | 2.31m | re-sync ("about 2.3 million") |
| "The prosperity comes from champions, talent, oil and partner growth" | research is the largest single source | **add the laboratories** (decision 4) |

The §34 tests of CR-056 are not re-run here: the order against Union output ("about 1.16 times … in 1929 and 1.74 times in 1932") and the Union "the larger power in real output". At integration, also check the investment programme figures quoted in money terms: power investment is lower in money because prices fall.

## Known limits

- **G8 is simplified:** the champions' world shares are not yet driven by G2 and G4.
- **The G4 inputs** (the leaders' world shares and gross-output weights) are MODEL estimates. The Union's steel trust without Carnegie and Ford's shares are author-adjustable. Current shares stand in for cumulative experience, so Pacifica Steel's experience jumps in 1901.
- **The Union's capital ratio** is a steady state at `g_su` 0.21 (Kuznets; to verify).
- **The research ratio counts only a lead** (MAX(1, R)).
- **`g_tp_res` 0.75** is a judgement on how much of Technical programmes is research.
- **Iterative calculation is on.** Excel users need it enabled; the file carries the setting.
- **Paths C was not re-iterated** (see the population model above).
