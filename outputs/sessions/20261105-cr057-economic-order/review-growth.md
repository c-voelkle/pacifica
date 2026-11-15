# The growth engine: fresh-context review (6 November 2026)

A separate agent reviewed the first adopted build of the growth engine (workbook `cf18730e…`). It was given:
- AGENTS.md;
- the design note;
- the build, rebuild and variant scripts;
- the workbook and the results note;
- the affected storyline passages and CR-057.

It was not given the drafting notes. It recalculated its own variants in LibreOffice. Its spot-checks of the note's figures all matched the workbook. Nothing in canon was touched.

All findings are applied in the rebuilt workbook (see `finance/CR-057-growth-workbook.md`) unless noted.

## MUST FIX

| ID | Finding | Applied |
| --- | --- | --- |
| M1 | The research leak used a hand-typed Pacifica/Union output ratio of 0.10–0.30. The model's own ratio is 0.39 (1900), 0.65 (1913), 1.04 (1929) and 1.48 (1932). This overstated the research lead: 2.24× fell to 2.11× when corrected | Growth "ratio" now reads last year's model ratio: Pacifica's GDP at US prices over the Union's GDP (Labour BK) |
| M2 | γ 0.12 is not the author's 35%. On the built stocks it implies a gross return of about 220% in 1900, about 600% in 1880, and about 80% net at the 1929 margin. The stock-ratio form also blows up early, because the Union's stocks are tiny (R about 8 in 1880, a +30% lead in 1900) | G2 is rebuilt in Jones and Williams's flow form. Extra TFP growth = g_r × (Pacifica's usable research less the leak − the Union's usable research), lagged, with g_r = the author's 35% (Stress 0.25). That is their measured return at about 2% of GDP, Pacifica's 1929 intensity. The stock, absorption and γ levers are removed |

## SHOULD FIX

| ID | Finding | Applied |
| --- | --- | --- |
| S1 | Capital was deflated by Economy H, but GDP mixes two price levels (inflating real investment by 6% in 1929) | Investment × Economy S / O |
| S2 | The capital channel measured against the Union's steady state from 1846. That double-counts the base path, which holds the historical West's capital, and gives −29% in 1861 and −9% in 1900 | G6 counts deepening from `g_kstart` (1900, CR-056's dyn_start) against Pacifica's own 1899 ratio. Capital is now measured against trend output (Economy S / G), so a slump does not read as deepening |
| S3 | The documented circular reference is not confirmed. Results are the same at 5, 200 and 1,000 iterations, but a global iteration setting would mask a future accidental loop | Not resolved. Iteration stays on with the evidence recorded (identical at 5, 200 and 1,000). An open item for the next workbook pass: find the loop and break it with a lag, then switch iteration off |
| S4 | The stock's lag ignored growth | Moot: the flow form uses lagged intensity, as Jones and Williams's regression does |
| S5 | Nothing stopped CR-056's mode 2 and C3 running with the engine | While `g_on` = 1, Economy C ignores mode 2 and Champions Z/AF ignore C3. C1 and C5 stay with dyn_mode |
| S6 | The car inputs conflicted with canon: hand-typed shares put Pacifica's leader at 0.08–0.11 of world output against the Union's at 0.33–0.45 | Pacifica's leader = `g_car_lp` (0.5) × Pacifica's vehicles (Champions U) / world. The Union's leader = `g_car_lu` (0.4) × the Union's historical production / world |
| S7 | A storyline test that already failed got worse and was not disclosed: "the Union remains the larger power in real output" | Reported in the note's table as a fail, with the figures |

## NOTE

- Population years: the note now says which year-end or start-of-year figures it uses.
- The note now reports Stress's price level in 1932.
- Learning's small total (+0.2%) was already disclosed.
- The energy figures were not checked by the reviewer.
