# CR-049 in the workbook: the atomic programme (MODEL)

**2 November 2026.** The author accepted the [atomic estimate](CR-049-atomic-estimate.md) and asked for it to be integrated "with the proposed figures and add them to the workbook as a new atomic program". The [workbook](Pacifica_financial_model_1846-1932.xlsx) is built from the CR-045–047 workbook by [`build/cr049_atomic_programme.py`](build/cr049_atomic_programme.py) and recalculated in LibreOffice (no formula errors; no check fails). Paths C was not re-iterated. All amounts are MODEL.

The author's direction is that Pacifica treats the years before 1927 as an opportunity that comes once and mines as much uranium as it can get. How it gets more than the four sources below is the next CR; the quantities here are the estimate's central case and will rise with it.

## What changed

- **New sheet `Atomic`** (after Champions), one row a year 1846–1932, totals in row 94:
  - uranium mined by source (radium-era by-product, Western Slope, Joachimsthal, Shinkolobwe, Fergana), in tonnes of uranium;
  - its use for research installations, weapons (a coarse separation-feed bucket, never per device) and energy, and the reserve at each year end;
  - costs in 1913 dollars (mining by the unit-cost levers; contracts and concessions; laboratories and installations; separation halls, weapons and tests; power stations), converted to current dollars through the Paths price level;
  - direct returns (radium and the source trade, vanadium from Western Slope ore, electricity from the atomic stations) in 1913 and current dollars;
  - the net cost to the Treasury, the navy's saving after 1927 as a memo, the cost as a share of real GDP and a reserve check.
- **Levers** (`atom_*`, Levers under "CR-049"): unit costs by source, vanadium yield and price, the stations' capacity factor and power price, and `atom_scale`, a multiplier on the non-mining costs (Story 1.0; Stress 1.5, the estimate's high case).
- **Budget:** the programme's cost is added to *Technical programmes* (S) and its direct returns to *State enterprises* (F). The navy's saving is not entered in the Budget or the Navy sheet.
- **Checks:** a new column, *Uranium reserve not negative (CR-049)*, counted in *Problems this year*.
- Not entered, because canon states no amounts: the reconstruction credit to Belgium and Bohemia at The Hague; the Bosnian compensation loan of 1909, which Pacifican banks lend rather than the Treasury.

## Results (Story case)

| | 1864–1932 |
|---|---:|
| Uranium mined | 5,804 t (Western Slope 2,760; Shinkolobwe 2,270; Joachimsthal 390; radium era 300; Fergana 84) |
| Used for energy / weapons / research | 1,025 / 550 / 150 t |
| Reserve in 1932 | 4,079 t (70%) |
| Cost, 1913 $ | $692m |
| Cost, current $ | $1,014m |
| Direct returns, current $ (radium, vanadium, electricity) | $262m |
| Net cost to the Treasury, current $ | $751m |
| Navy's saving after 1927, memo (1913 $) | $150m |

| Year | Mined (t) | Reserve (t) | Cost (1913 $m) | Cost ($m) | Returns ($m) | Net ($m) |
|---|---:|---:|---:|---:|---:|---:|
| 1913 | 190 | 786 | 23.9 | 23.9 | 5.8 | 18.2 |
| 1919 | 130 | 1,428 | 34.3 | 62.7 | 7.5 | 55.2 |
| 1927 | 427 | 3,269 | 34.5 | 54.5 | 7.3 | 47.2 |
| 1932 | 207 | 4,079 | 23.6 | 28.8 | 30.8 | −2.0 |

The peak cost is 0.17% of real GDP (1914). Against the CR-045–047 workbook, the budget surplus is about $18m lower in 1913, $58m in 1919 and $53m in 1927; because the Development Fund invests most of each surplus, its investment is about 5% lower in 1919 and 3% in 1927, and real GDP in 1932 is about 0.45% lower ($39.8bn against $40.0bn, 1913 $). The model does not credit the programme with spillovers (valves, electrical industry, the strategic settlement of 1927), so this is the cost side only. Public debt, debt/GDP and the population are practically unchanged; no canon ceiling is breached.

SHA-256 of the workbook: `02dff02958cf6956268d1101263cffa9136127d055aef4c990d1a102ceafc9a9`.
