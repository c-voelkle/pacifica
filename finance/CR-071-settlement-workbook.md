# CR-071 C5: the interior settlement programme in the workbook (17 November 2026)

Built by `finance/build/cr071_settlement.py`, the last step of `cr057_rebuild_pair.py` (after Deseret). Master lever `sp_on`: at 0 the build reproduces the input workbook exactly (checked: 108,214 values, none differs). All amounts MODEL; their derivation is `population/settlement_1887.py` (`population/outputs/settlement_1887.md`).

**Authorization:** the author, 17 November 2026, 09:14 ("2, 3, 4, 5, 6, and 7 are approved as proposed"; item 7 was to build the programme's figures into the workbook).

## What was already there

| Programme item | Where the workbook already has it |
| --- | --- |
| The extra 1.17 million people of 1887 in the acceded units | The population model's total is fixed; the programme decides where people settle, not how many there are |
| Assisted passage and the recruiting offices | People T (about 1.07 million assisted arrivals in 1867–87) × `assist_cost`, in Budget T, about $109 million over 1867–87; more than the programme's own passage line, so nothing is added |
| The members' land | `Members' land` (L15) sells our timeline's census farm acreage from 1867: 10.7 million acres by 1887, 34 million by 1900 |

## What is added (Events rows)

| Row | Years | Category | Per year (Story) | What |
| --- | --- | --- | --- | --- |
| E243 | 1872–1887 | Investment | $0.70m | Irrigation districts' dams and canals, lent on Development Fund credit (`sp_irr_cap` $11.2m) |
| E244 | 1877–1906 | Receipt | $0.28m | The districts' repayments from water rates (`sp_irr_loss` 25% never repaid; Stress 40%) |
| E245 | 1870–1891 | Receipt | $0.93m | The interior's farms sold early: `sp_acres` 16.9m acres at `sp_price` $1.35, a tenth never paid |
| E246 | 1892–1911 | Receipt (negative) | −$1.87m | The same acres missing from L15's later sales at `sp_later_price` $2.46 |

## Results

| | Before | **With the programme** |
| --- | --- | --- |
| Story / Stress failed year-checks | 0 / 51 | **0 / 50** |
| Residents, end of 1932 | 37.06m | 37.06m |
| Domestic taxes, 1887 | $93.8m | **$87.1m** (the early land receipts let the surplus rule cut taxes) |
| Domestic taxes, 1895 / 1911 | $187.3m / $768.3m | $190.4m / $770.4m (the later sales missing) |
| Domestic taxes, 1867–1932, sum | | **+$17.9m** (the net cost of selling the interior cheap to fill it, and the irrigation loss) |

The programme moves tax burden from the 1880s to the 1890s–1900s and costs about $18 million in all, which is small beside a Budget of $100–200 million a year in those decades. The energy pair was not re-iterated: GDP is unchanged in every year, so the energy workbook's inputs do not move. Financial workbook SHA-256 `dea54361daf84fac11c7daaaf5644ab964c654632f2b0617c564a3f8174e2c5c`.

## Not modelled

- The railways' land grants (I-53): land, not cash; the Land Fund's acreage that the grants take is inside L15's census path.
- The anchors (smelters, coal, timber): private capital.
- Homeland leases (Santa Rita, Bisbee, Globe, Clifton, the Utes' districts): their royalties go to the nations, not the Treasury.
