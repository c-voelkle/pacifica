# Workbook note, 3 November 2026: the energy workbook (CR-052)

SHA-256 of the energy workbook: `f474cb9fc65f0d9f3fc19c3de17183dc2c7d6e99f38a25f9802672356262fc22`. Built from the financial workbook with SHA-256 `22266bad58ee60da888c9b8de9bcd2c964498a5427d6b453b1f6a5a46f6120b2` (the CR-050 workbook) by [`build/extract_finance.py`](build/extract_finance.py) and [`build/build_energy_workbook.py`](build/build_energy_workbook.py), then recalculated in LibreOffice: 22,633 formulas, no errors, in both cases. The financial workbook is not changed. All amounts are MODEL estimates; every input is a blue cell with its basis beside it.

The model follows the handoff (`claude/energy-workbook-handoff.md`) and the storyline as integrated on `main`, plus CR-051 (approved, not yet integrated) for the halls, the feed plant, the Columbia station and the Works' dams. A fresh-context review ([`outputs/CR-052/review.md`](../outputs/CR-052/review.md)) found that the first build drove factory motors from total GDP at a US-calibrated intensity while the fuel side treated Pacifica's dollar as much less industrial. This version applies one industrial weight (`ind_w` = 0.5) to both; all results below are after that fix.

## The answer

**Pacifica uses about twice the United States' electricity per person, and it cannot fuel itself from the Realm.** Built from sources and uses, its electricity per person is 1.9–2.3 times the US's in 1920–1932 (all producers). Its fuel base is the West's: with California's oilfields, western coal and canon's 33–37 million people, about a fifth to a quarter of its primary energy must be imported, and in the war years the Story case needs more coal than any supplier in reach can ship.

| Story case | 1900 | 1913 | 1920 | 1922 | 1924 | 1927 | 1929 | 1932 |
|---|---|---|---|---|---|---|---|---|
| Everyone present (m) | 10.6 | 19.9 | 25.5 | 27.3 | 29.4 | 32.6 | 34.8 | 37.2 |
| Generation (TWh) | 2.0 | 13.8 | 28.6 | 35.0 | 44.9 | 58.2 | 64.3 | 60.1 |
| Capacity (GW) | 1.1 | 5.9 | 10.8 | 12.8 | 15.9 | 20.1 | 22.4 | 22.7 |
| Hydro share of generation | 81% | 77% | 69% | 68% | 65% | 63% | 64% | 76% |
| Electricity per person (kWh) | 191 | 691 | 1,123 | 1,280 | 1,526 | 1,785 | 1,848 | 1,615 |
| **× US electricity per person (all producers)** | — | 2.35 | 2.11 | 2.30 | 2.26 | 2.10 | 1.93 | 2.03 |
| × US utility capacity per person | — | 4.82 | 3.54 | 3.63 | 3.23 | 2.87 | 2.63 | 2.21 |
| Halls' draw (MW) | — | — | 175 | 350 | 575 | 700 | 525 | 525 |
| **Halls / capacity** | — | — | 1.6% | 2.7% | 3.6% | 3.5% | 2.3% | 2.3% |
| **Halls / electricity used** | — | — | 5.8% | 9.3% | 11.8% | 11.0% | 7.4% | 7.9% |
| Halls from the common grid (MW avg) | — | — | 0 | 33 | 106 | 109 | 0 | 0 |
| Primary energy (PJ) | 1,133 | 2,714 | 3,737 | 4,014 | 4,540 | 5,100 | 5,433 | 4,780 |
| Primary energy per person (GJ) | 106 | 136 | 146 | 147 | 154 | 156 | 156 | 128 |
| Energy per real $ vs US | 0.38 | 0.32 | 0.30 | 0.30 | 0.32 | 0.33 | 0.33 | 0.22 |
| Home oil (m bbl, from finance) | 25 | 100 | 115 | 150 | 230 | 253 | 300 | 153 |
| Oil imported (m bbl) | 6 | 31 | 83 | 104 | 123 | 171 | 228 | 169 |
| Oil for railways, industry and power: share of what they want | 14% | 34% | 34% | 45% | 67% | 76% | 99% | 50% |
| Coal mined in the Realm (Mt) | 19.8 | 41.4 | 52.2 | 52.3 | 52.3 | 52.4 | 52.4 | 52.5 |
| Coal imported (Mt) | 4.6 | 12.5 | 20.7 | 15.7 | 7.8 | 9.0 | 0 | 18.6 |
| **Coal beyond reach (Mt)** | 0.1 | 4.5 | 11.7 | 6.1 | 0 | 0 | 0 | 6.6 |
| Primary energy that would have to be imported | 13% | 18% | 28% | 26% | 21% | 25% | 26% | 31% |
| … that can actually be imported | 13% | 14% | 20% | 22% | 21% | 25% | 26% | 28% |
| Motor vehicles on the road (m) | 0.00 | 0.35 | 1.66 | 2.02 | 2.84 | 4.23 | 5.28 | 5.53 |
| Power investment ($m) | 34 | 138 | 325 | 555 | 592 | 564 | 537 | 230 |
| Power investment / GDP | 0.6% | 0.8% | 0.6% | 1.3% | 1.1% | 0.9% | 0.8% | 0.4% |
| Electricity revenue ($m) | 72 | 342 | 960 | 831 | 1,005 | 1,146 | 1,210 | 966 |
| Checks failing | 7 | 7 | 7 | 7 | — | — | — | 4, 7 |

| Stress case | 1913 | 1920 | 1922 | 1924 | 1927 | 1929 | 1932 |
|---|---|---|---|---|---|---|---|
| Everyone present (m) | 13.4 | 16.4 | 17.3 | 18.3 | 19.9 | 20.9 | 22.0 |
| Generation (TWh) | 9.3 | 17.9 | 21.5 | 27.5 | 34.4 | 35.5 | 29.2 |
| × US electricity per person | 2.35 | 2.06 | 2.24 | 2.23 | 2.03 | 1.77 | 1.67 |
| × US utility capacity per person | 4.78 | 3.42 | 3.46 | 3.10 | 2.74 | 2.42 | 1.88 |
| Halls' draw (MW, top of CR-051's range) | — | 200 | 400 | 650 | 800 | 600 | 600 |
| Halls / capacity | — | 3.0% | 5.2% | 6.9% | 6.8% | 4.8% | 5.3% |
| Halls / electricity used | — | 10.4% | 17.2% | 21.5% | 21.0% | 15.3% | 18.5% |
| Halls from the common grid (MW avg) | — | 0 | 81 | 261 | 210 | 0 | 0 |
| Primary energy imported | 8% | 16% | 19% | 17% | 13% | 6% | 24% |
| Coal beyond reach (Mt) | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Checks failing | 6 | — | 2 | 6, 9 | 9 | — | — |

Reading the tables (annual figures, not only the benchmark years):
- **The multiplier.** Story, electricity per person against all US producers: 1.86–2.30 in 1920–1932, up to 2.71 in the war boom of 1916. Against US *utility* capacity, the power check's own yardstick: 2.21–3.63 in 1920–1932 (4.5–5.2 in 1913–18). The utility comparison runs high because US industrial plants are missing from its denominator while Pacifica's figure includes everything. Stress: 1.63–2.24 and 1.88–3.46 in 1920–1932.
- **The halls, 1920–27.** Story: 1.6–4.0% of capacity, 5.8–12.9% of electricity (peak 1925). Stress: 3.0–7.7% and 10.4–23.6%. CR-051's 3–9% of capacity and 7–16% of electricity fits the Story case for electricity; its capacity share is a little high.
- **The halls' power.** The arc plants' freed power is 168 MW in 1919 (below R1's 200–300 MW) and 219–236 MW in 1920–27; the Works' dams average 62–300 MW as they come in. At the full plant in 1922–27, 33–153 MW comes from the common grid (Story), most in 1925.
- **Energy per dollar.** Pacifica's primary energy per person is about 0.8 of the US's while its real GDP per person is about 2.3 times (finance). The same industrial weight scales its factory motors and its industrial fuel.
- **Oil.** The trust sells 24–45m bbl of home crude a year in Asia (finance) while the Realm's railways and industry get only 27–45% of the oil they want in 1913–1922 (Fuels!H).

## The checks

| Test | Story | Stress |
|---|---|---|
| 1. Supply = use (oil, electricity, primary) | passes. Largely an accounting identity: it catches formula errors | passes |
| 2. Basins within potential; strategic dams after their lead time | passes | fails 1922: with Stress's three-year lead time, the Works' first 100 MW in 1922 is a year early (the dams' path does not shift with the lever) |
| 3. Oilfields within plausible output and known reserves; gasoline yield | passes | passes |
| 4. Electricity per person and energy per dollar within bands | fails 1932 (the US slump makes the ratio 0.22). The lower band (0.25) sits just below the model's own range, so this check can fail only in an outlier year | passes |
| 5. Capacity factor 20–60%, reserve ≥ 10%, dry year keeps the strategic loads | passes | passes, including the 1924 drought |
| 6. Power investment within 4% of GDP and the Development Fund's share | fails 1916 | fails in 9 years before 1927: the Stress Fund invests little |
| 7. Oil and coal imports within reach | **fails 1900–1923, 1925–26 and 1932** on coal: up to 17.7 Mt beyond reach (1917) | passes |
| 8. Navy oil = finance; vehicles per person ≤ 0.5 | passes. The navy half is an identity | passes |
| 9. Strategic loads powered (halls ≤ 25% from the grid; Rock Island; Hilo) | passes | fails 1923–27: 124–261 MW of the halls from the grid |

## Sensitivity runs (Story; one change at a time)

| Change | × US electricity per person, 1920–32 | Halls / electricity, 1920–27 | Hydro share 1929 | Coal beyond reach, all years (Mt) | Worst year (Mt) | Halls from grid, 1925 (MW) |
|---|---|---|---|---|---|---|
| As built | 1.86–2.30 | 6–13% | 64% | 130 | 17.7 (1917) | 153 |
| Mid-Columbia chain on (option) | 1.86–2.30 | 6–13% | 79% | 120 | 17.7 (1917) | 153 |
| No main-line electrification | 1.73–2.20 | 6–14% | 69% | 148 | 17.9 (1917) | 153 |
| All Pacifican-controlled Gulf crude shipped home | 1.86–2.30 | 6–13% | 64% | 75 | 14.7 (1917) | 153 |
| Realm coal at 4× history instead of 3× | 1.86–2.30 | 6–13% | 64% | 3 | 1.8 (1917) | 153 |
| No home oil sold in Asia | 1.86–2.30 | 6–13% | 64% | 101 | 16.2 (1917) | 153 |
| Works' dams 30% larger (about 650 MW) | 1.86–2.30 | 6–13% | 65% | 129 | 17.7 (1917) | 73 |
| Industrial weight 0.7 | 2.14–2.62 | 5–11% | 56% | 190 | 20.3 (1917) | 153 |
| Industrial weight 1.0 (US-type dollar, the first build) | 2.56–3.10 | 4–10% | 47% | 295 | 24.5 (1918) | 153 |

The coal gap is mostly the size of the `coal_mult` lever, not a ceiling the model derives: at four times historical western output it nearly vanishes. The multiplier depends mainly on the industrial weight.

## What is in the workbook

| Sheet | Contents |
|---|---|
| Start | Purpose, conventions, case, the financial workbook's SHA, key results for the benchmark years, the §8 questions and how each is carried. |
| Levers | 78 levers, Story and Stress, each with a named range, status and basis; `case_sel` in E4. |
| Anchors | US series used by formula (population, utility capacity, total generation, primary energy from EIA Table E1) and 61 anchor facts with source and status. |
| Paths | 72 benchmark-year paths: intensities, shares, tonnages, capacity by basin, the halls' range. |
| People & output | 27 finance series, Story and Stress side by side (red), the active one picked by the case. |
| Hydro | Eight basins, the Works' dams, Rock Island, Boulder Canyon and the optional mid-Columbia chain; output in a normal or dry year; potential used; lead times. |
| Strategic loads | The halls (with the arc power freed and the Works' dams), the feed plant, the Columbia station and Rock Island's balance, the walled college, Hilo and Hawaii's island grid, the navy, the canal; register of sources. |
| Uses | Electricity in 14 sectors (eight of them electrochemical); fuel in 13; conversion; the use-side primary total. |
| Electricity | Demand, losses, Hawaii's grid, hydro, steam and atomic supply, peak, capacity, reserve, capacity factors, fuel, per person, the multipliers, the halls' shares, the dry-year test. |
| Fuels | Oil allocated where it is available (motor fuel, lamps, the navy, bunkers and the feed plant first), then Realm coal, extra wood and imported coal for the rest; gas from the oilfields; the supply-side primary total; import shares; intensity against the US. |
| Finance link | Investment, the Development Fund's credit, revenue, royalties and fuel trade in money; named columns `en_*`. |
| Events | 28 dated canon commitments. |
| Checks | The nine tests of handoff §7, year by year, and the failing tests. |
| Changes | Revision history. |

## Limits of the model

- **One mainland grid.** All mainland hydro can serve all mainland demand. No 1920s line could carry Columbia power to California, so the Northwest's hydro is counted where it could not go. This flatters the hydro share and the value of Columbia dams.
- The financial workbook does not yet read the `en_*` columns and was not re-run. Its Story and Stress results are unchanged by this note.
- Partners' own energy, and production abroad (Emba, Baku, Grozny–Maikop) except as oil the trust can ship home; no trade block yet for partners' equipment purchases.
- Industrial self-generation is not separated from utility supply; revenue prices all of it at the average utility price, which overstates revenue.
- The atomic stations' cost stays in the financial workbook's Atomic sheet.

## Anchors

The building session could not reach census.gov or the USGS PDFs. Verified in the session: US primary energy by source 1850–1935 (EIA Annual Energy Review Table E1, from Schurr and Netschert); US electricity in 1930 (114 TWh, which matches all producers although the article calls it utility-provided; coal 56%, hydro 34%; 68% of homes electrified; Construction Physics); California oil in 1895 and 1900. Carried from the CR-051 power check: California hydro output in 1922, PG&E in 1911, Oak Ridge in 1945. Everything else on the Anchors sheet is marked TO VERIFY; [README.md](README.md) lists the downloads that would settle it.
