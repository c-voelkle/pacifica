# Workbook note, 3 November 2026: the energy workbook (CR-052)

SHA-256 of the energy workbook: `5aca0d32346d38ad76c3fc0d19344c14f16a07fe2d7ceb1f0aa7e929c1979f1f`. Built from the financial workbook with SHA-256 `22266bad58ee60da888c9b8de9bcd2c964498a5427d6b453b1f6a5a46f6120b2` (the CR-050 workbook) by [`build/extract_finance.py`](build/extract_finance.py) and [`build/build_energy_workbook.py`](build/build_energy_workbook.py), then recalculated in LibreOffice: 22,535 formulas, no errors, in both cases. The financial workbook is not changed. All amounts are MODEL estimates; every input is a blue cell with its basis beside it.

The model follows the handoff (`claude/energy-workbook-handoff.md`) and the storyline as integrated on `main`, plus CR-051 (approved, not yet integrated) for the halls, the feed plant, the Columbia station and the Works' dams.

## The answer

**Pacifica is an electricity-rich, fuel-poor country.** Built from sources and uses, its electricity per person is about three times the United States'. Its fuel is not: with California's oilfields, the West's coal and canon's 33–37 million people, about a quarter to a third of its primary energy must be imported, and in 1905–1928 the Story case needs more coal than any supplier in reach can ship.

| Story case | 1900 | 1913 | 1920 | 1922 | 1924 | 1927 | 1929 | 1932 |
|---|---|---|---|---|---|---|---|---|
| Everyone present (m) | 10.6 | 19.9 | 25.5 | 27.3 | 29.4 | 32.6 | 34.8 | 37.2 |
| Generation (TWh) | 2.5 | 18.5 | 38.8 | 47.1 | 60.4 | 78.5 | 88.1 | 83.0 |
| Capacity (GW) | 1.3 | 7.6 | 14.1 | 16.7 | 20.9 | 26.9 | 30.3 | 31.1 |
| Hydro share of generation | 67% | 58% | 51% | 51% | 51% | 55% | 57% | 69% |
| Electricity per person (kWh) | 231 | 926 | 1,520 | 1,726 | 2,051 | 2,409 | 2,532 | 2,231 |
| **× US electricity per person** | — | 3.15 | 2.86 | 3.10 | 3.04 | 2.83 | 2.64 | 2.80 |
| × US utility capacity per person | — | 6.21 | 4.63 | 4.74 | 4.24 | 3.84 | 3.56 | 3.03 |
| Halls' draw (MW) | — | — | 175 | 350 | 575 | 700 | 525 | 525 |
| **Halls / capacity** | — | — | 1.2% | 2.1% | 2.8% | 2.6% | 1.7% | 1.7% |
| **Halls / electricity used** | — | — | 4.3% | 6.9% | 8.8% | 8.2% | 5.4% | 5.8% |
| Halls from the common grid (MW avg) | — | — | 0 | 33 | 106 | 109 | 0 | 0 |
| Primary energy (PJ) | 1,147 | 2,827 | 3,940 | 4,243 | 4,812 | 5,425 | 5,790 | 5,112 |
| Primary energy per person (GJ) | 108 | 142 | 154 | 155 | 163 | 166 | 166 | 137 |
| Energy per real $ vs US | 0.39 | 0.34 | 0.31 | 0.32 | 0.34 | 0.35 | 0.35 | 0.24 |
| Home oil (m bbl, from finance) | 25 | 100 | 115 | 150 | 230 | 253 | 300 | 153 |
| Oil imported (m bbl) | 5 | 31 | 83 | 104 | 123 | 171 | 228 | 169 |
| Oil for railways, industry and power: share of what they want | 13% | 32% | 31% | 41% | 61% | 70% | 92% | 47% |
| Coal mined in the Realm (Mt) | 19.8 | 41.4 | 52.2 | 52.3 | 52.3 | 52.4 | 52.4 | 52.5 |
| Coal imported (Mt) | 5.3 | 17.0 | 28.9 | 24.9 | 17.6 | 18.0 | 2.7 | 24.9 |
| **Coal beyond reach (Mt)** | 0.8 | 9.0 | 19.9 | 15.2 | 7.3 | 6.7 | 0 | 12.9 |
| Primary energy imported | 14% | 22% | 31% | 30% | 25% | 28% | 25% | 32% |
| Motor vehicles on the road (m) | 0.00 | 0.35 | 1.66 | 2.02 | 2.84 | 4.23 | 5.28 | 5.53 |
| Power investment ($m) | 38 | 179 | 442 | 715 | 819 | 810 | 792 | 379 |
| Power investment / GDP | 0.7% | 1.0% | 0.9% | 1.6% | 1.6% | 1.3% | 1.1% | 0.7% |
| Electricity revenue ($m) | 87 | 459 | 1,314 | 1,138 | 1,380 | 1,576 | 1,679 | 1,353 |
| Checks failing | 7 | 7 | 7 | 7 | 7 | 7 | — | 4, 6, 7 |

| Stress case | 1913 | 1920 | 1922 | 1924 | 1927 | 1929 | 1932 |
|---|---|---|---|---|---|---|---|
| Everyone present (m) | 13.4 | 16.4 | 17.3 | 18.3 | 19.9 | 20.9 | 22.0 |
| Generation (TWh) | 11.3 | 21.9 | 26.1 | 33.1 | 41.4 | 43.4 | 35.9 |
| × US electricity per person | 2.87 | 2.52 | 2.72 | 2.69 | 2.45 | 2.16 | 2.05 |
| × US utility capacity per person | 5.63 | 4.05 | 4.09 | 3.66 | 3.22 | 2.92 | 2.32 |
| Halls' draw (MW, top of CR-051's range) | — | 200 | 400 | 650 | 800 | 600 | 600 |
| Halls / capacity | — | 2.5% | 4.4% | 5.8% | 5.8% | 4.0% | 4.3% |
| Halls / electricity used | — | 8.6% | 14.2% | 18.0% | 17.5% | 12.5% | 15.1% |
| Halls from the common grid (MW avg) | — | 0 | 81 | 261 | 210 | 0 | 0 |
| Primary energy imported | 8% | 16% | 18% | 19% | 15% | 7% | 24% |
| Coal beyond reach (Mt) | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Checks failing | 6 | — | 2 | 6, 9 | 6, 9 | 6 | — |

Notes on reading the tables:
- **The multiplier.** Against all US electricity (utilities and industrial plants), Pacifica uses 2.6–3.1 times as much per person in the Story case, 2.0–2.9 in Stress. Against US *utility* capacity, the comparison the power check used, it is 3.0–4.7 times (Story): higher, because US industrial plants are missing from that denominator and Pacifica's figure includes everything. The author's view that 2.0–2.75 was too low holds.
- **Why the multiplier falls after 1913.** The United States electrified fast in the 1920s; Pacifica started a decade earlier and was already near Norway's level by 1929.
- **The halls.** Story: 1–3% of capacity and 4–10% of electricity (peak 9.6% in 1925). In 1923–27 the arc plants' freed power (about 250 MW) and the Works' dams (about 300 MW on average) fall short of the full plant's steady draw, so 60–150 MW comes from the common grid, most in 1925. Stress: 2.5–6.6% and 9–20%. CR-051's corrected 3–9% and 7–16% sits between the two cases.
- **Energy per dollar.** Pacifica's primary energy per person is about 0.85 of the US's, while its real GDP per person is about 2.3 times (finance). Its physical industry (steel, vehicles, refining) is 15–30% of the US's while its GDP is about two-thirds, and hydro replaces fuel. Hence 0.3–0.4 of US energy per dollar.

## The checks

| Test | Story | Stress |
|---|---|---|
| 1. Supply = use (oil, electricity, primary) | passes every year | passes |
| 2. Basins within potential; strategic dams after their lead time | passes | fails 1922: with Stress's three-year lead time, the Works' first 100 MW in 1922 comes a year early |
| 3. Oilfields within plausible output and known reserves; gasoline yield | passes | passes |
| 4. Electricity per person and energy per dollar within bands | fails 1932 (the US slump makes the ratio 0.24) | passes |
| 5. Capacity factor 20–60%, reserve ≥ 10%, dry year keeps the strategic loads | passes | passes, including the 1924 drought |
| 6. Power investment within 4% of GDP and the Development Fund's share | fails 1916 and 1932: power would need more than 60% of what the Fund invests | fails in 13 years: the Stress Fund invests little |
| 7. Oil and coal imports within reach | **fails 1882–88, 1900–27 and 1932**: coal beyond reach, up to 24.5 Mt in 1918 | passes from 1889 |
| 8. Navy oil = finance; vehicles per person ≤ 0.5 | passes | passes |
| 9. Strategic loads powered (halls ≤ 25% from the grid; Rock Island; Hilo) | passes | fails 1923–27: 210–260 MW of the halls from the grid |

## What the sensitivity runs show (Story)

| Change | Hydro share 1929 | Coal beyond reach, all years to 1932 | Peak halls from grid (1925) |
|---|---|---|---|
| As built | 57% | 271 Mt | 153 MW |
| No mid-Columbia chain | 47% | 295 Mt | 153 MW |
| No main-line electrification | 60% (less demand) | 297 Mt | 153 MW |
| Works' dams 30% larger (about 650 MW) | 58% | 269 Mt | 73 MW |
| All Pacifican-controlled Gulf crude shipped home | 57% | 182 Mt (none after 1926) | 153 MW |
| Hilo on windward hydro | — | — | Check 9 fails 1925–32 |

## What is in the workbook

| Sheet | Contents |
|---|---|
| Start | Purpose, conventions, case, the financial workbook's SHA, key results for the benchmark years, the §8 questions and how each is carried. |
| Levers | 77 levers, Story and Stress, each with a named range, status and basis; `case_sel` in E4. |
| Anchors | US series used by formula (population, utility capacity, total generation, primary energy from EIA Table E1) and 61 anchor facts with source and status. |
| Paths | 72 benchmark-year paths: intensities, shares, tonnages, capacity by basin, the halls' range. |
| People & output | 27 finance series, Story and Stress side by side (red), the active one picked by the case. |
| Hydro | Eight basins, the Works' dams, Rock Island, Boulder Canyon and the mid-Columbia chain; output in a normal or dry year; potential used; lead times. |
| Strategic loads | The halls (with the arc power freed and the Works' dams), the feed plant, the Columbia station and Rock Island's balance, the walled college, Hilo and Hawaii's island grid, the navy, the canal; register of sources. |
| Uses | Electricity in 14 sectors (eight of them electrochemical); fuel in 13; conversion; the use-side primary total. |
| Electricity | Demand, losses, Hawaii's grid, hydro, steam and atomic supply, peak, capacity, reserve, capacity factors, fuel, per person, the multipliers, the halls' shares, the dry-year test. |
| Fuels | Oil allocated where it is available (motor fuel, lamps, the navy, bunkers and the feed plant first), coal, wood and imported coal for the rest; gas from the oilfields; the supply-side primary total; intensity against the US. |
| Finance link | Investment, the Development Fund's credit, revenue, royalties and fuel trade in money; named columns `en_*`. |
| Events | 28 dated canon commitments. |
| Checks | The nine tests of handoff §7, year by year, and the failing tests. |
| Changes | Revision history. |

## Not in the model

- The financial workbook does not yet read the `en_*` columns. Adding power investment, fuel imports and royalties to it is the next build, after approval. Its Story and Stress results are unchanged by this note.
- Partners' own energy (Japan, the Philippine crown, the Gulf, Siberia) and production abroad (Emba, Baku, Grozny–Maikop) except as oil the trust can ship home.
- The cost of the atomic stations (already in the financial workbook's Atomic sheet).
- Industrial self-generation is not separated from utility supply: the workbook models the whole system.

## Anchors

The building session could not reach census.gov or the USGS PDFs. Verified in the session: US primary energy by source 1850–1935 (EIA Annual Energy Review Table E1, from Schurr and Netschert), US electricity in 1930 (114 TWh; coal 56%, hydro 34%; 68% of homes electrified; Construction Physics), California oil in 1895 and 1900. Carried from the CR-051 power check: California hydro output in 1922, PG&E in 1911, Oak Ridge in 1945. Everything else on the Anchors sheet is marked TO VERIFY; [README.md](README.md) lists the downloads that would settle it.
