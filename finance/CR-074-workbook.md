# CR-074: the Pacific Companies in the workbook (18 November 2026)

Built by `finance/build/cr074_companies.py`, the last step of `cr057_rebuild_pair.py` (after the CR-071 settlement programme). Master lever `cp_on`: at 0 the build reproduces the input workbook exactly (checked after LibreOffice recalculation: 114,440 values outside Levers, Events and Changes, none differs). All amounts MODEL.

**Authorization:** the author, 18 November 2026, 12:02 ("You can proceed with the integration and then add the model rows").

## What is added (Events rows)

| Row | Years | Category | Per year (Story) | What |
| --- | --- | --- | --- | --- |
| E247 | 1868 | Receipt (in gold) | $0.014m | Ward's bequest of ten thousand taels in gold to the Republic's Treasury, paid out of the debts the consul recovers (`cp_ward_taels` × `cp_tael_usd` $1.39) |
| E248 | 1888–1932 | Programme | $0.18m | The companies' school at Sacramento and the Companies Office (`cp_cadets` 500 × `cp_cadet_cost` $360; Stress $480) |
| E249 | 1888–1932 | Receipt (negative) | −$0.067m | Land Fund receipts forgone on the warrants (`cp_warrants` 350 a year × `cp_warrant_acres` 55 × `cp_warrant_price` $3.50; Stress $5.00) |
| E250 | 1888–1932 | Programme | $0.011m | The home half: interest net of the Land Fund's earnings (`cp_abroad` 2,500 × `cp_pay` $360 × ½ × 2.5 years × `cp_spread` 1%; Stress 2%) |

The scale follows CR-074 F and E: about 2,000–3,000 men abroad at a time, about 9,000 warrants redeemed by 1914, half a farm for five years and a whole farm for ten.

## Results

| | Before | **With the companies** |
| --- | --- | --- |
| Story / Stress failed year-checks | 0 / 50 | **0 / 50** |
| Residents, end of 1932 | 37.06m | 37.06m |
| Non-mining GDP, 1929 | $25,918m | $25,918m |
| Domestic taxes, 1887 / 1895 / 1911 / 1932 | $87.09m / $190.41m / $770.40m / $1,426.04m | $87.07m / $190.71m / $770.67m / $1,426.29m |
| Domestic taxes, 1846–1932, sum | | **+$12.0m** |

About $12 million over eighty-seven years, against budgets of $100–200 million a year in the 1880s and 1890s. GDP is unchanged in every year checked, so the energy pair was not re-iterated (as for CR-071). Financial workbook SHA-256 `b527c12a37bce74e21f1d1c0497592925a50c4cee375ebbf789f72ed7a94674e`.

## Not modelled

- **The hosts' pay** (about $1m a year around 1900 at `cp_pay` × `cp_abroad`) and **the prize money of 1878 and 1914**: private income from abroad, not Treasury cash.
- **The Philippine companies' warrants:** the dependency's friar-estate land, outside the Realm's budget.
- **The men abroad:** 2,000–3,000 against about 37 million residents; the warrant men settle inside CR-071 C5's interior programme.
- **The first generation under the licence (1854–1887):** licence fees and bonds are not stated in canon.
