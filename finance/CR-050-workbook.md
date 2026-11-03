# CR-050 in the workbook: the atomic programme re-timed (MODEL)

**3 November 2026.** After approving CR-050 and CR-050-R1, the author asked to "update the workbook". The [workbook](Pacifica_financial_model_1846-1932.xlsx) is built from the CR-049 workbook by [`build/cr050_atomic_retiming.py`](build/cr050_atomic_retiming.py) and recalculated in LibreOffice (52,578 formulas, no errors; no check fails). Only the `Atomic` sheet's yearly inputs and notes change: every formula, lever, Budget link and check stays as CR-049 built it. Paths C was not re-iterated. All amounts are MODEL.

## What moved

| Item | CR-049 | CR-050 |
|---|---|---|
| Separation halls | built 1912–1919 ($120m) | decided 1917, first hall 1919, rebuilt, built to 1923 ($130m) |
| Halls' operation | from 1914 | from 1919 |
| Weapons feed (coarse bucket) | 1911–1927 | 1920–1927 (250 t by 1927, unchanged) |
| Desert test | about 1920 | May 1924 |
| Sea demonstration | 1927 | 1927, with a closed zone and the target ships scuttled (+$1m) |
| The walled college at Hetch Hetchy | — | spur, tunnel, buildings, tram, 1909–1911 ($6m) |
| Ralston College's share (Compact of the Tuolumne) | — | $0.5m a year from 1910, $1m from 1920 |
| Me-Wuk and Kootzaduka'a leases | — | $0.05m a year from 1910 |
| Tokyo station | built 1925–1927, first load 1926–27 | built 1928–1931, first power 1931 |
| Pacifican stations | 1928–1931, loaded 1929–1931 | built 1929–1932, two loaded in 1932, two after |
| Margin on the barium-borne salt | $2.0m a year from 1909 | $2.4m from 1908 (whole ores, Austrian marketing), $2.1m from 1910 and $1.7m from 1919 (gifts of state) |

## Results (Story case)

| | CR-049 | CR-050 |
|---|---:|---:|
| Uranium mined, 1864–1932 | 5,804 t | 5,804 t |
| Used for energy / weapons / research | 1,025 / 550 / 150 t | 485 / 550 / 150 t |
| Reserve in 1932 | 4,079 t (70%) | 4,619 t (80%) |
| Cost, 1913 $ | $692m | $678m |
| Cost, current $ | $1,014m | $1,048m |
| Direct returns, current $ | $262m | $167m |
| Net cost to the Treasury, current $ | $751m | $881m |
| Peak cost / real GDP | 0.17% (1914) | 0.18% (1921) |
| Real GDP in 1932 (1913 $) | $39,806m | $39,840m |

| Year | Cost (1913 $m) | Cost ($m) | Returns ($m) | Net ($m) | Reserve (t) |
|---|---:|---:|---:|---:|---:|
| 1913 | 8.5 | 8.5 | 5.9 | 2.6 | 830 |
| 1919 | 42.8 | 78.4 | 7.0 | 71.4 | 1,560 |
| 1924 | 22.0 | 35.6 | 5.7 | 29.9 | 2,616 |
| 1927 | 26.6 | 42.0 | 7.2 | 34.8 | 3,489 |
| 1931 | 47.6 | 65.2 | 11.3 | 53.9 | 4,737 |
| 1932 | 44.7 | 54.5 | 12.7 | 41.8 | 4,619 |

**Reading the results:**
- **Timing.** The programme now costs least before the war and most in 1919–1923, when the halls are built in inflated dollars. That is why its cost in current dollars rises while its cost in 1913 dollars falls.
- **Electricity.** It comes almost entirely after 1931, so the direct returns are about $95m lower and the net cost to the Treasury about $130m higher.
- **Real GDP.** The 1932 figure is slightly higher than in the CR-049 workbook, because less was spent in the years when the Development Fund's investment compounds longest.
- **Unchanged:** public debt, debt/GDP and the population. No canon ceiling is breached, and no check fails.

**Not entered**, because canon states no amounts:
- San Francisco's purchase of the Spring Valley Water Company and the Eleanor–Cherry waterworks (municipal, not Treasury);
- the Tokyo station's financing (OPEN; it is entered as Pacifica's);
- the Bosnian loan and the Hague reconstruction credits, as before.

SHA-256 of the workbook: `22266bad58ee60da888c9b8de9bcd2c964498a5427d6b453b1f6a5a46f6120b2`.
