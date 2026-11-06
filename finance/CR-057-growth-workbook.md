# Workbook note, 6 November 2026: the growth engine (CR-057 follow-up)

SHA-256 `05a84022a5de5a991d89f114268b63304b3b36eb6ee133e7dd0b1445dae8353a` (energy workbook `de27b3ea…`). Status: PROPOSED. The author's decisions of 10:45 are applied, and the build is revised after a fresh-context review (`outputs/sessions/20261105-cr057-economic-order/review-growth.md`). It awaits integration with CR-057. No canon text, register, facts file, character file or ledger is changed. All amounts are MODEL.

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
5. CR-057, with `c_glide` 0 (the 1913 cover held: falling prices);
6. the growth engine;
7. LibreOffice;
8. extract, the energy workbook, LibreOffice, export.

The pair converged in five passes. The energy outputs moved by at most 5.8e-6 on pass 4 and 6.3e-7 on pass 5 (relative). On the last pass, the Layers sheet (CR-056's six cases) is rebuilt on the converged CR-056 build. LibreOffice recalculation gives no errors, and no Story check fails in any year.

**Identity:** with `g_on` 0 the engine reproduces its input exactly. This was checked cell by cell on the first build: 99,971 numeric cells, and 90,899 with `c57_on` 0 too. The variants below reproduce the earlier figures: the old design, accounting, 2.38×; CR-057, accounting, 1.87×.

The comparison is run by [`build/cr057_growth_variants.py`](build/cr057_growth_variants.py).

## What is built

[`build/cr057_growth_engine.py`](build/cr057_growth_engine.py): one master lever `g_on` (saved at 1) and a `Growth` sheet.

**The hooks:**
- **Economy D** becomes the network premium alone. The Development Fund's 30% return and CR-057's Patrimony term both go.
- **Economy J** is multiplied by (1 + research) × (1 + learning) × (1 + capital).
- **CR-056.** While `g_on` is 1, CR-056's mode 2 (Economy C) and C3 (Champions Z, AF) are switched off, because G6 and G2 supersede them. C1 and C5 stay with `dyn_mode` (saved 0).

| Channel | Mechanism | Main levers (Story · Stress) |
| --- | --- | --- |
| G2/G3 research and diffusion | Jones and Williams's flow form: extra TFP growth = `g_r` × (Pacifica's research / GDP lagged `g_lag_p` × its usable share under open licensing × (1 − `g_leak` × Pacifica's output / the Union's) − the Union's research / GDP lagged `g_lag_u` × its usable share under exclusive licences), when positive. The lead is the exponential of the running sum. The output ratio is the model's own, last year: Pacifica's GDP at US prices over the Union's (Labour BK) | `g_r` 0.35 · 0.25 (the author's 35%; Jones and Williams measured 0.30–0.37 at about 2% of GDP, Pacifica's 1929 intensity). `g_lag_p` 3 · 4, `g_lag_u` 6, `g_pat` 0.3, `g_open` 0.9 · 0.8, `g_excl` 0.6, `g_leak` 0.25 · 0.30. Research path: Pacifica 0.6% (1880), 1.2% (1900), 1.8% (1913), 2% (1929); the Union 0.05%, 0.1%, 0.15%, 0.25% |
| G4 learning by doing | Seven sectors. Experience = the leader's world share + 0.3 × the rest (Irwin and Klenow), Pacifica's leader against the Union's. The cost advantage b × ln(E_P / E_U) is weighted by gross output / GDP. **Steel follows canon:** from 1901 Pacifica's leader is Pacifica Steel (Carnegie's plants plus the Pacifican mills, about 0.16–0.17 of the world); the Union's is the trust formed without Carnegie (0.12–0.14). Only the Pacifican mills are in Pacifica's GDP. **Cars:** the leading maker's share × each country's vehicles built (Pacifica's from the energy workbook) over the world's | Steel 24% → 15%, cars 15%, chemicals 15%, electrical 10%, power 10%, aluminium 15%, aircraft 15% → 10%. `g_car_lp` 0.5, `g_car_lu` 0.4 |
| G6 capital | Stock of gross domestic investment (Energy link AA, public and private alike, deflated as GDP is), depreciating at `k_dep`. Level ((K / trend output) / its 1900 value)^(α/(1−α)), from `g_kstart`. The base path holds the West's own capital before 1900 | `k_alpha` 0.3, `k_dep` 0.04, `g_kstart` 1900 |
| G6b network premium | `g_prem` × (1 − coverage) on core network investment: power from the energy workbook, with homes wired as coverage; rail, ports and the canal at `g_core` × GDP | `g_prem` 0.08 · 0.04; `g_core` 0.01 |
| Research in the accounts | The state's half (`g_pub`) of research beyond the research already in Technical programmes (`g_tp_res` 0.75 of GDP × Paths V) goes to Budget line AF and government consumption (Energy link AE) | `g_pub` 0.5, `g_tp_res` 0.75, `g_charge` 1 |

**Iterative calculation is enabled** (200 iterations, delta 1e-7). It was turned on because LibreOffice reported a circular reference (Err:522) from 1927 once the engine was on. The reviewer could not confirm the loop. Results are the same at 5, 200 and 1,000 iterations. Finding the loop and switching iteration off is an open item for the next workbook pass.

## Results, Story case (saved: CR-057 with the engine, falling prices)

GDP per person against US history, at US prices (Economy T). Economy R, money, is in brackets where it differs.

| Variant | 1900 | 1913 | 1920 | 1929 | 1932 |
| --- | --- | --- | --- | --- | --- |
| Old design, accounting (before CR-057) | 2.17 | 2.29 | 2.42 | **2.38** | 2.83 (3.17) |
| Old design, engine | 2.04 | 2.17 | 2.31 | 2.31 | 2.80 (3.13) |
| CR-057, accounting, falling prices | 1.96 | 1.93 | 1.98 (0.83) | 1.87 (0.87) | 2.21 (1.35) |
| **CR-057, engine, falling prices (saved)** | **2.04** | **2.17** | **2.30 (0.96)** | **2.30 (1.05)** | **2.78 (1.69)** |
| … rising prices (the default glide) | | | 2.31 (1.30) | 2.31 (1.66) | 2.79 (2.90) |
| … research to 3% | | | | 2.42 | |
| … cautious (r 0.25, no premium) | | | | 2.10 | |

**1929 in detail:**

| Variant | Real GDP (1913 $m) | Real per resident ($) | Residents (m) | Price level | Residents, end 1932 (m) |
| --- | --- | --- | --- | --- | --- |
| Old design, accounting | 44,516 | 1,333 | 33.4 | 1.60 | 36.8 |
| Old design, engine | 41,937 | 1,296 | 32.4 | 1.60 | 35.6 |
| CR-057, accounting | 32,814 | 1,074 | 30.5 | 0.68 | 33.3 |
| **CR-057, engine (saved)** | **43,560** | **1,310** | **33.2** | **0.68** | **36.5** |

**What the results show:**
- **The engine carries Pacifica to 2.30× in 1929 with your 35%, applied as measured.** The storyline's "about 2.24 times" is within its 10% band. The old 2.38× is reached only with research at 3% of GDP (2.42×).
- **CR-057 costs no output once capital earns the ordinary return.** With the engine, the old design and CR-057 are identical to 1913. By 1929 CR-057 is slightly ahead: $1,310 against $1,296 per resident.
- **Falling prices (MR-01).** The price level goes from 1.00 in 1913 to 0.80 in 1920 and 0.68 in 1929. Money income per person is then about US history's (1.05×), while real income is 2.30 times.
- **The early decades are lower than in the old model** (2.04× in 1900 against 2.17×). The research lead builds up slowly, as the flow form says it should.

**The engine's channels (saved case):**

| Channel | 1900 | 1913 | 1920 | 1929 | 1932 |
| --- | --- | --- | --- | --- | --- |
| G2/G3 research lead | +6.7% | +12.1% | +15.8% | +20.4% | +21.9% |
| … of which open licensing | 0.7% | 1.2% | 1.5% | 1.9% | 2.1% |
| G4 learning (seven sectors) | −0.1% | +0.1% | +0.2% | +0.2% | +0.4% |
| G6 capital deepening since 1900 | 0 | +4.3% | +5.3% | +9.5% | +11.3% |
| G6b network premium, cumulative from 1847 | | | | +4.0% | |

**Learning by doing, by sector in 1929:**

| Sector | 1929 |
| --- | --- |
| Steel (Pacifica Steel's experience) | +0.04% |
| Cars | −0.17% |
| Chemicals | +0.09% |
| Electrical | +0.07% |
| Power | +0.13% |
| Aluminium | +0.02% |
| Aircraft | +0.01% |

Learning adds little: spillovers are international and the sectors' weight in GDP is small.

**Research in the accounts:**

| | 1913 | 1929 | 1932 |
| --- | --- | --- | --- |
| New Budget line AF | $51m | $127m | $120m |
| The Patrimony's transfer to the Budget | $93m | $280m | $301m |

The 1932 deficit is −$828m, from CR-057's rule of no tax rise in 1930–32.

## Stress

| Variant (1929) | × US at US prices | Real per resident ($) | Residents, end 1932 (m) | Price level, 1929 | Year-checks failing |
| --- | --- | --- | --- | --- | --- |
| CR-057, engine (falling prices) | 1.78 | 991 | 22.3 | 0.74 | 52 |
| … rising prices | 1.78 | 987 | 22.2 | 1.30 | 45 |
| … cautious | 1.74 | 970 | 22.0 | 0.74 | 52 |

Earlier figures for comparison:
- **Year-checks failing:** 52 for CR-057 without the engine (5 November), and 17 for the model before CR-057.
- **1929 output:** the model before CR-057 gave 1.53× in Stress, so the engine raises Stress.

The failures are CR-057's nominal commitments under a money rule (5 November note).

## The population model (re-run)

The population model was re-run on the new workbook (`canon.py`, `flows.py`, `changes.py`, `neighbours.py`), and all 15 tests pass. The sheet and the cohort model now agree within 0.2% in every benchmark year (−18,000, or −0.1%, in 1932), so Paths C needs no re-iteration.

Start-of-year residents (People B):

| 1861 | 1880 | 1900 | 1913 | 1929 | 1932 |
| --- | --- | --- | --- | --- | --- |
| 1.24m | 4.19m | 9.84m | 18.11m | 32.62m | 35.70m |

End of 1932 (People L): 36.49m.

## Against the storyline (MODEL figures to re-sync at integration)

| The storyline says | Now | |
| --- | --- | --- |
| Output per person "about 2.24 times the Union's in 1929" | 2.30× | holds within 10%. Re-sync to "about 2.3 times" |
| "about 37 million" in 1932 | 36.5m (end of year) | holds. Re-sync to "about 36½ million" at the author's choice |
| "about 1.2 million people by 1861" | 1.24m | holds |
| "about 2,600 kilowatt-hours a head in 1929" | 2,675 | holds |
| "about 96 per cent of homes are wired" (1929) | 96% | holds |
| "Pacifica builds about 2.2 million vehicles a year" | 2.31m | re-sync to "about 2.3 million" |
| "The prosperity comes from champions, talent, oil and partner growth" | research is the largest single source | add the laboratories (decision 4) |
| "The Union remains the larger power in real output" | Pacifica's output at US prices is 1.08 times the Union's in 1929 and 1.49 times in 1932 | **fails.** It already failed under CR-056 (0.97, 1.35) and fails more now. A canon decision for integration (CR-056 decision 3) |

## Known limits

- **G8 is simplified:** the champions' world shares are not yet driven by G2 and G4.
- **The flow form holds the return constant at 35%.** That is defensible at Pacifica's intensities, which do not exceed about 2% of GDP, the level where it was measured. Jones and Williams's caution about diminishing returns applies above that.
- **The G4 inputs** are MODEL estimates. Current shares stand in for cumulative experience, so Pacifica Steel's experience jumps in 1901.
- **G6 counts deepening only from 1900.**
- **`g_tp_res` 0.75** is a judgement.
- **Iterative calculation is on,** and the loop is unconfirmed (see above).
