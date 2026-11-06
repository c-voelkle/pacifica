# Workbook note, 6 November 2026: the growth engine (CR-057 follow-up)

SHA-256 `de93b28370be0c67d783304b7983034c3445c316ea56f2e624263be7ee873a8a`. Status: PROPOSED, for the author's decision before integration. No canon text, register, facts file, character file or ledger is changed. All amounts are MODEL.

**Chain.** The CR-056 dynamic layer (PR #65, merged into this draft branch, `a579fee5…`) → [`build/cr057_economic_order.py`](build/cr057_economic_order.py) → [`build/cr057_growth_engine.py`](build/cr057_growth_engine.py). The CR-057 script now accepts CR-056's Economy D formula and wraps it unchanged. LibreOffice recalculation gives 79,261 formulas and no errors. The comparison was run by [`build/cr057_growth_variants.py`](build/cr057_growth_variants.py).

**Identity checks** (numeric cells, tolerance 1e-9; Levers, Changes and Start excluded):
- With `c57_on` 0 and `g_on` 0, the workbook reproduces CR-056's saved values: 90,899 cells, none differ.
- With `c57_on` 1 and `g_on` 0, it reproduces the CR-057 build on CR-056: 99,971 cells, none differ.
- The `--off` build reproduces it as well.

**Authorization.** Author, 6 November 2026, on [CR-057-growth-design-note.md](CR-057-growth-design-note.md):
- "Yes that sounds much more accurate";
- the answers of 09:18, 09:48 ("aim high … research directed at industrial goals and close to industry") and 10:06 (steel 24%, the research path to 2%).

## What is built

One master lever, `g_on` (Story 1, Stress 1; 0 reproduces the input), and a new `Growth` sheet:

| Channel | Mechanism | Main levers (Story · Stress) |
| --- | --- | --- |
| G2/G3 research and diffusion | Research stocks per unit of output for Pacifica, the Union and the rest of the world, depreciating at `g_dep`. Each enters after an adoption lag: 3 years under open licensing, 6 under exclusive licences. The usable share of the patented part is `g_open` against `g_excl`. Absorption of the world's stock rises with own research. A quarter of Pacifica's stock leaks to the Union. TFP lead = MAX(1, Pacifica's effective stock / the Union's)^`g_gamma` | `g_gamma` 0.12 · 0.08; `g_dep` 0.15 · 0.20; `g_pat` 0.3; `g_open` 0.9 · 0.8; `g_excl` 0.6; `g_leak` 0.25 · 0.30. Research paths: Pacifica 0.6% (1880), 1.2% (1900), 1.8% (1913), 2% (1929); the Union 0.05%, 0.1%, 0.15%, 0.25% |
| G4 learning by doing | Seven sectors. Experience = the leader's world share + 0.3 × the rest (Irwin and Klenow), Pacifica's leader against the Union's. The cost advantage b × ln(E_P / E_U) is weighted by gross output / GDP | Steel 24% → 15%, cars 15%, chemicals 15%, electrical 10%, power 10%, aluminium 15%, aircraft 15% → 10% |
| G6 capital | Stock of gross domestic investment (Energy link AA, public and private alike), depreciating at `k_dep`. Level ((K/Y) / (K/Y)_Union)^(α/(1−α)) against the Union's s / (g + δ) | `k_alpha` 0.3, `k_dep` 0.04, `g_su` 0.21 |
| G6b network premium | `g_prem` × (1 − coverage) on core network investment. Power is the energy workbook's power investment, with homes wired as coverage. Rail, ports and the canal are `g_core` × GDP, with a coverage path. Enters as a growth increment in Economy D | `g_prem` 0.08 · 0.04; `g_core` 0.01 |

**The hooks:**
- Economy D becomes the network premium alone. The Development Fund's 30% return and CR-057's re-based Patrimony term both go; all capital earns the ordinary return through G6.
- Economy J is multiplied by (1 + the level factor).

**Unchanged:** G1 (`Paths!L`), G5 (talent), G7 (mining, the Gulf) and the champions' block. The research level multiplies non-mining, non-champion output only (Economy J). The champions' laboratories are inside the research path, so their output is not counted twice. This is G8 in simplified form: the champions' world shares are not yet driven by G2 and G4.

**Iterative calculation is enabled** (200 iterations, delta 1e-7). CR-057's money block and the 1927 Japan rescue close a loop:
- Money N reads the rescue's callable balances from 1928;
- the rescue's private share reads 1927 investment abroad, which reads 1927 output.

LibreOffice reported this loop as Err:522 once the engine changed the path. With iteration on it resolves, and no value moves at `g_on` 0 (identity above).

## Results, Story case

GDP per person against US history, in money (Economy R) and at US prices (Economy T). Real GDP is in 1913 $m. Residents are the year's average.

| Variant | 1900 | 1913 | 1920 | 1929 | 1932 |
| --- | --- | --- | --- | --- | --- |
| **Old design, accounting** (the current model) | 2.17 | 2.29 | 2.42 | **2.38** | 2.83 |
| Old design, engine | 2.24 | 2.27 | 2.34 | 2.22 | 2.75 |
| CR-057, accounting (5 November) | 1.96 | 1.93 | 1.98 | 1.86 | 2.21 |
| **CR-057, engine** (saved) | 2.24 | 2.27 | 2.34 | **2.23** | 2.76 |
| CR-057, engine, the 1913 cover held (falling prices) | 2.24 | 2.27 | 2.34 | **2.24** | 2.78 |
| CR-057, engine, research to 3% | | | | 2.28 | |
| CR-057, engine, cautious (γ 0.07, no premium) | | | | 1.98 | |

**1929 in detail:**

| Variant | Money (R) | Real GDP | Real per resident ($) | Residents (m) | Price level | Residents end 1932 (m) |
| --- | --- | --- | --- | --- | --- | --- |
| Old design, accounting | 2.38 | 44,487 | 1,332 | 33.4 | 1.60 | 36.8 |
| Old design, engine | 2.22 | 40,740 | 1,245 | 32.7 | 1.60 | 35.9 |
| CR-057, accounting | 1.56 | 31,422 | 1,054 | 29.8 | 1.32 | 32.4 |
| CR-057, engine | 1.68 | 41,558 | 1,257 | 33.1 | 1.18 | 36.1 |
| CR-057, engine, 1913 cover held | 1.11 | 42,721 | 1,273 | 33.5 | 0.74 | 36.7 |

**What it shows:**
- **The engine reaches the storyline's figure.** The storyline's MODEL sentence is "about 2.24 times the Union's in 1929". At US prices the engine gives 2.23× (saved) and 2.24× (falling prices). It does not give the old 2.38×. The research path at 3% gives 2.28×. The cautious case gives 1.98×, just outside the storyline's 10% band (2.02–2.46×).
- **The two designs come out equal.** Once public and private capital earn the same ordinary return, CR-057 costs no output:
  - before 1914 the two are identical, because the money rule starts in 1914 and the research path is the same for both;
  - by 1929 CR-057 is slightly ahead (real output per resident 1,257 against 1,245), because the migration pull reads the lead at US prices.
  
  The 21% gap of 5 November came entirely from the Development Fund's 30% return.
- **Falling prices (MR-01) work.** Holding the 1913 cover, the price level falls from 1.00 in 1913 to 0.74 in 1929. Real output per resident rises (1,273) and residents in 1932 are 36.7 million, close to canon's "about 37 million". Money income per person is then 1.11 times US history, while real income is 2.24 times.

**The engine's channels, CR-057 saved case:**

| Channel | 1900 | 1913 | 1929 |
| --- | --- | --- | --- |
| G2/G3 research lead (of which open licensing) | +30.6% (1.1%) | +27.8% (1.0%) | +22.6% (1.0%) |
| Pacifica's effective research stock / the Union's | 9.2 | 7.7 | 5.5 |
| G4 learning | −0.5% | −0.3% | −0.0% |
| G6 capital (Pacifica's K/Y against the Union's 2.6) | −9.2% (2.10) | −3.4% (2.42) | +4.1% (2.89) |
| G6b network premium, cumulative from 1847 | | | +4.0% |

**What the channels show:**
- **The research lead is largest early.** Pacifica's research starts from almost nothing in the Union's time. Then the Union's intensity rises from 0.1% to 0.25% while Pacifica's rises from 1.2% to 2%, so the ratio narrows. That puts more of the lead into 1900–1913 than the old model had.
- **Learning by doing gives Pacifica no lead.** By sector in 1929:

| Sector | 1929 |
| --- | --- |
| Steel | −0.17% |
| Cars | −0.19% |
| Chemicals | +0.09% |
| Electrical | +0.07% |
| Power | +0.13% |
| Aluminium | +0.02% |
| Aircraft | +0.01% |

  Spillovers are international (Irwin and Klenow), and the Union's leaders, US Steel and Ford, are bigger than Pacifica's. Pacifica's own leads in aluminium, chemicals and power are worth little at their weight in GDP. The first draft's ×1.02–1.04 was too high.
- **Capital dilutes before 1913.** Arrivals at 4–5% a year outrun the investment share. That is CR-056 mode 2's finding again. Capital deepens in the 1920s.

**Who pays for research.** In 1929 research costs $1.0bn, 2% of output. The state's half is $0.50bn, about 1% of GDP. The Patrimony's transfer to the Budget is $0.43bn. With the 1913 cover held, the figures are $0.34bn against $0.30bn. So the Patrimony's 3% rule pays for most of the state's research, and an ordinary budget line covers the rest. The research spending is a memo; it is not yet charged to the Budget.

## Stress

Stress takes `g_gamma` 0.08, `g_dep` 0.20, `g_open` 0.8, `g_leak` 0.30, `g_prem` 0.04 and lower learning rates.

| Variant (1929) | × US at US prices | Real per resident ($) | Residents end 1932 (m) | Year-checks failing |
| --- | --- | --- | --- | --- |
| Old design, accounting | 1.53 | 842 | 21.6 | 17 |
| Old design, engine | 1.60 | 881 | 20.3 | 25 |
| CR-057, accounting | 1.43 | 793 | 20.7 | 52 |
| CR-057, engine | 1.61 | 889 | 20.4 | 55 |

The engine lifts Stress, because its research channel survives the low end of every range while the Fund's return did not. The failing checks are CR-057's nominal commitments under a money rule (5 November note, Stress), plus a few more.

## Against the storyline

| The storyline says | CR-057 engine (saved) | Falling prices (1913 cover) |
| --- | --- | --- |
| Output per person "about 2.24 times the Union's in 1929" (MODEL) | 2.23× · holds | 2.24× · holds |
| "about 37 million" in 1932 (MODEL; flag a move above 0.3m) | 36.1m · re-sync | 36.7m · holds |
| "The prosperity comes from champions, talent, oil and partner growth" | Research becomes the largest single source; this sentence would need the laboratories added | as left |

The CR-056 tests on §34 (the Union "remains larger in real output") are not re-run here.

## Known limits

- **The energy workbook was not re-iterated.** The energy outputs are those of the fifteenth build. Residents move by up to −0.7m, which changes kilowatt-hours a head and the power memos slightly. Iterate after adoption.
- **The Layers sheet** holds CR-056's values as of 5 November. The population model and Paths C were not re-run.
- **G8 is simplified.** The champions' world shares are not yet driven by G2 and G4.
- **Research is a memo,** not charged to the Budget or the Patrimony.
- **The G4 inputs** (the leaders' world shares and gross-output weights) are MODEL estimates. US Steel's and Ford's shares are to verify.
- **Current shares stand in for cumulative experience.**
- **The Union's capital ratio** is a steady state at `g_su` 0.21 (Kuznets; to verify).
- **The research ratio counts only a lead.** MAX(1, R) gives no penalty in the 1850s, when Pacifica's stock is below the Union's.
- **Iterative calculation is on** (see above). Excel users need it enabled; the file carries the setting.

## Decisions for the author

1. **Adopt the engine** as the Story case (saved at `g_on` 1), in place of the Fund's 30% return?
2. **Prices.** Hold the 1913 cover (`c_glide` 0)? It gives MR-01's falling prices, 2.24× and about 36.7 million in 1932. The alternative is the default glide, which gives a gently rising price level, 2.23× and 36.1 million.
3. **Charge research to the accounts.** The state's half would go to the Patrimony's transfer plus a budget line.
4. **Then:** iterate the energy workbook, re-run the population model, re-sync the storyline's MODEL figures, and add the laboratories to the storyline's sentence on where the prosperity comes from.
