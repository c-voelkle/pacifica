# CR-076: drink, the duty schedule and coffee in the workbook (19 November 2026)

Built by `finance/build/cr076_drink_coffee.py`, the last step of `cr057_rebuild_pair.py` (after the Pacific Companies). It adds 36 levers (`dc_*`) and a memo sheet, **Drink & coffee**, which reads People, Prices, Budget and Economy and feeds nothing. Domestic taxes stay the existing share of non-mining GDP: the drink duty is shown as a part of them, not added to them. The mortality lever is not built. All amounts MODEL.

**Authorization:** the author, 19 November 2026: the duty schedule (20:11), option 1 with the mortality lever off (20:34: "Option 1 mortality lever off is approved").

## What the sheet shows (1846–1932)

- Pure alcohol drunk per resident by period (`dc_pa_1` to `dc_pa_4`: 2.2, 1.4, 0.9 and 0.75 US gallons; Stress 2.6, 1.6, 1.1 and 0.9) and its split between spirits, wine and beer (spirits 70%, 50%, 35% and 30%).
- The spirits duty per gallon of pure alcohol (CR-076 R1-1): $1.875 in 1852–66, $3.50 in 1867–87, and from 1888 $6.375 in 1888 prices, reset every five years with Pacifica's price level (Prices!C). Beer and wine pay 0.13 and 0.26 of the spirits rate per unit of alcohol. Collection is 60%, 80% and 95% by period (Stress 50%, 70% and 90%).
- The Spirit Stores' surplus (the county option at 30% of spirits in 1867–87, all take-away spirits from 1888), the share kept by the nations' own stores (1.5% of the duty), and the duty against domestic taxes, checked against a 35% ceiling.
- Coffee: pounds per resident (8 before 1888, 12 in 1888–1914, 14 in 1915 rising 0.2 lb a year), the Realm's consumption, Hawaii's and the Philippines' crops reaching the Realm, the share grown under the Pacific crowns and the import bill (green coffee at $0.15 a pound, halved in 1931–32).

## Results (Story case)

| Year | Residents | Spirits duty per gal of pure alcohol | Drink duty | Stores' surplus | Domestic taxes | Duty / domestic taxes |
| --- | --- | --- | --- | --- | --- | --- |
| 1852 | 0.53m | $1.88 | $1.0m | — | $6m | 17% |
| 1866 | 1.77m | $1.88 | $3.3m | — | $46m | 7% |
| 1887 | 6.10m | $3.50 | $14.0m | $0.8m | $87m | 16% |
| 1888 | 6.34m | $6.38 | $15.9m | $1.2m | $80m | 20% |
| 1900 | 10.45m | $6.25 | $25.7m | $2.1m | $327m | 8% |
| 1913 | 19.23m | $8.69 | $65.8m | $5.2m | $933m | 7% |
| 1929 | 34.40m | $5.96 | $61.9m | $4.4m | $1,650m | 4% |
| 1932 | 37.06m | $5.96 | $66.7m | $5.0m | $1,426m | 5% |

The largest share is 23% in the 1880s (Stress 25%), so no year breaks the 35% ceiling. The duty's weight falls as drinking falls and the income tax arrives in 1915. The duty per gallon rises to 1913 and falls after it, because the five-year reset follows Pacifica's price level.

| Coffee | 1888 | 1913 | 1929 | 1932 |
| --- | --- | --- | --- | --- |
| Pounds per resident | 12 | 12 | 16.8 | 17.4 |
| Drunk in the Realm | 35,000 t | 105,000 t | 262,000 t | 293,000 t |
| Hawaii's crop to the Realm | 300 t | 13,500 t | 22,300 t | 24,000 t |
| Philippine crop to the Realm | 8,000 t | 23,800 t | 36,000 t | 36,000 t |
| Grown under the Pacific crowns | 24% | 36% | 22% | 20% |
| Import bill | $8.7m | $22.3m | $67.4m | $38.5m |

In 1929 the share grown under the crowns is 22% (Stress 25%) and consumption is 16.8 lb a head (Stress 15.1). Both are inside CR-076's ranges (15–30%; 15–18 lb), and the sheet's own check reads "ok" in both cases.

## Checks

- **Switch-off check:** the workbook built with the sheet on and the one built with `dc_on` at 0 both match the input workbook in every value outside Levers, Changes and the new sheet (117,393 values; none differs).
- **Failed year-checks:** Story 0, Stress 50 (unchanged). Residents, GDP and the Budget are unchanged in every year.
- **Recalculation:** LibreOffice (the spreadsheet skill's `recalc.py`), 83,712 formulas, no errors in either case.
- **Financial workbook SHA-256:** `9198e4eb82f20d35974d66c827d5c8728ca9ef9c393326dff6374088f0a2660d`.

The energy pair was not re-iterated, because nothing it reads changes (as for CR-071 and CR-074).

## Not modelled

- The mortality lever (author's decision, 20:34; confirmed 20:44). The population model already converges Pacifica's mortality on New Zealand's, the world's best of the period, from 1888 to 1910 (`population/data/rates.toml`). New Zealand's own strong temperance movement is part of that benchmark, so a separate drink effect would double-count and pass the model's ceiling. Before 1888 the effect would be about half a year to a year of adult male life expectancy, or about 0.1–0.2% more residents by 1932, which is smaller than the model's other uncertainties. The drink rules are recorded as one reason the convergence is plausible.
- The county earmark as county spending: there are no county budgets in the workbook, so the duty and surplus that go to surgeries and halls are a memo.
- The duty collected by members in 1867–87 is shown on the same sheet as the confederal figures. Whether it is member or confederal money is CR-076 D5's split, which the Budget does not separate.
- Revenue from the Union's visitors in 1920–32: no national Prohibition, so no reverse traffic of any size.
