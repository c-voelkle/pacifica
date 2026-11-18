# CR-074: the Pacific Companies in the workbook (18 November 2026)

Built by `finance/build/cr074_companies.py`, the last step of `cr057_rebuild_pair.py` (after the CR-071 settlement programme). Master lever `cp_on`: at 0 the build reproduces the input workbook exactly (checked after LibreOffice recalculation: 114,440 values outside Levers, Events and Changes, none differs). All amounts MODEL.

**Authorization:** the author, 18 November 2026, 12:02 ("You can proceed with the integration and then add the model rows"); revised on the author's word of 12:47 after the review of the integration (`book-agent/revision/CR-074-review-on-main.md`, items 11, 12 and 26): the warrant row starts in 1893 with more warrants a year, and the CR's Model section now matches what is built.

## What is added (Events rows)

| Row | Years | Category | Per year (Story) | What |
| --- | --- | --- | --- | --- |
| E247 | 1868 | Receipt (in gold) | $0.014m | Ward's bequest of ten thousand taels' worth in gold to the Republic's Treasury (value, not weight), paid out of the debts the consul recovers (`cp_ward_taels` × `cp_tael_usd` $1.39 to the Shanghai tael) |
| E248 | 1888–1932 | Programme | $0.18m | The companies' school at Sacramento and the Companies Office (`cp_cadets` 500 × `cp_cadet_cost` $360; Stress $480) |
| E249 | 1893–1932 | Receipt (negative) | −$0.079m | Land Fund receipts forgone on the warrants (`cp_warrants` 410 a year × `cp_warrant_acres` 55 × `cp_warrant_price` $3.50; Stress $5.00). The first warrants fall due in 1893, five years into the Act: service under the licence before 1888 earned none, and the wound and death rider is too rare to model |
| E250 | 1888–1932 | Programme | $0.011m | The home half: interest net of the Land Fund's earnings (`cp_abroad` 2,500 × `cp_pay` $360 × ½ × 2.5 years × `cp_spread` 1%; Stress 2%) |

The scale follows CR-074 F and E: about 2,000–3,000 men abroad at a time, about 9,000 warrants redeemed by 1914 (410 a year over the 22 years 1893–1914), half a farm for five years and a whole farm for ten.

The Events column "Story status" reads Approved for E247–E250 because the events themselves are approved canon (CR-074); the amounts are MODEL. CR-071's rows E240–E246 were left as built (Proposed). The column is not a canon label.

## Results

| | Before | **With the companies** |
| --- | --- | --- |
| Story / Stress failed year-checks | 0 / 50 | **0 / 50** |
| Residents, end of 1932 | 37.06m | 37.06m |
| Non-mining GDP, 1929 | $25,918m | $25,918m |
| Domestic taxes, 1887 / 1895 / 1911 / 1932 | $87.09m / $190.41m / $770.40m / $1,426.04m | $87.06m / $190.72m / $770.68m / $1,426.30m |
| Domestic taxes, 1846–1932, sum | | **+$12.2m** |

About $12 million over eighty-seven years (+$12.0m with the warrant row from 1888, before the revision), against budgets of $100–200 million a year in the 1880s and 1890s. GDP is unchanged in every year checked (the Economy and People sheets do not move), so the energy pair was not re-iterated (as for CR-071). `cp_on` 0 still reproduces the input exactly (114,440 values, none differs).

The small falls in 1880 and 1887–88, before any CR-074 row but the bequest, come through the Patrimony: the bequest of 1868 enlarges its income, so the share of domestic taxes it cuts (Patrimony column AA, used in Budget column C) is a little larger in those years.

Financial workbook SHA-256 `959008db7a796079513712dad1ec1ba832962b3047c1256ee164a87ecc1b0463`.

## Not modelled

- **The hosts' pay** (about $1m a year around 1900 at `cp_pay` × `cp_abroad`) and **the prize money of 1878 and 1914**: private income from abroad, not Treasury cash.
- **The Philippine companies' warrants:** the dependency's friar-estate land, outside the Realm's budget.
- **The men abroad:** 2,000–3,000 against about 37 million residents; the warrant men settle inside CR-071 C5's interior programme.
- **The first generation under the licence (1854–1887):** licence fees and bonds are not stated in canon.
