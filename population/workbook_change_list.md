# Workbook change list (population step 3)

**Status:** proposed changes for the next version of `finance/Pacifica_financial_model_1846-1932.xlsx`, 27 October 2026. The workbook is not changed. Chryseis makes the edits in a separate financial task, then reruns the Checks sheet and both cases.

**Basis:** the author's decisions of 27 October 2026 (`README.md`, decisions 1–6) and draft CR-033. The figures come from `python3 population/changes.py`: the summary is in `outputs/workbook_changes.md`, and year-by-year values for pasting are in `outputs/workbook_changes.csv`. Residents are counted at the end of each year, as in People column L.

## Changes to inputs

| ID | Where | Change | Why | Effect by 1932 |
|---|---|---|---|---|
| P1 | Paths C, 1846–1932 | Replace the flat natural-increase path with the model's implied rate (`paths_C_model`). Valid only together with P2, because the rate depends on the age structure the arrivals bring. | Decisions 1, 5 and 6: Native Californians fall then recover; Native Hawaiians turn about 1895 (§20, §23); canon health and fertility reach the best real levels (`data/rates.toml`). The sheet now grows both Native populations with everyone. | Residents 27.3m → 30.9m (+13%) |
| P2 | Paths E and F, 1848–1860 | Multiply arrivals by 2.10 (`[dem01]`): Americas & Europe 475,000 → 997,500; Chinese 77,300 → 162,330. | Decision 3 (DEM-01): about 1.2m people in 1861, 1.7m in 1865. | 1861 residents 0.73m → 1.27m |
| P3 | Levers; Labour AL; People N–R | Split "Extra arrivals drawn by Pacifica's lead" (Labour AL) by origin with four Levers shares: Americas & Europe, Japan, China, Philippines. They are 0.70 / 0.20 / 0.10 / 0.00 from 1846 and 0.50 / 0.32 / 0.13 / 0.05 from 1914. Add each Asian share of AL into People N, O and P. R (Asian talent) then stops counting Asian talent separately, to avoid double counting. Q (settled guest workers) stays. | Decision 4 (Japanese predominance) and the talent-stream split. | Japanese-origin 4.37m, Chinese-origin 4.20m. Asian-origin share 20.0% → 30.5% |
| P4 | People, two new memo columns | Native Hawaiians and Native Californians, pasted from the CSV. These are for checks only and don't feed the totals. | Canon makes dated claims about both (§20, §23; CR-033 A10). | Hawaiians: low 41,800 in 1895, 68,400 in 1932. Californians: low 99,400 in 1895–96, 131,400 in 1932 |
| P5 | Checks | Two new rows. (a) The Native Hawaiian memo series reaches its low between 1893 and 1897. (b) 1861 residents are within 10% of DEM-01's 1.2m. | Keeps the canon claims from drifting in later workbook versions. | none |
| P6 | Levers `pop_1846`, comment | Note that the 170,000 Californians in 1846 include about 150,000 Native Californians. | Decision 2. | none |

## Knock-on effects to check (no input change proposed)

| ID | Where | What to check |
|---|---|---|
| D1 | Economy J | Non-mining GDP is residents × output per resident, so P2 raises 1850s non-mining output by up to 74%. Decide whether the DEM-01 settlers earn the sheet's full output per resident, or start lower while they find land and work. Mining output (Resources) doesn't change. |
| D2 | Budget T | Assisted arrivals are a share of all arrivals (Paths J). P2 roughly doubles the cost of settlement and immigration in 1848–1860. CR-033 A18 pays for it from the land margin (see L1). |
| D3 | Sources & uses, row 38; Checks | The story case's private-saving test was already tight in 1862 (home capital allowance 12.3%, margin $0.08m). A larger economy changes both saving and borrowing, so rerun before judging. |
| D4 | Labour B | The labour force is residents × `lf_rate`, so it rises with P1–P2. The implied participation stays at 59–64% of ages 15–64 (`outputs/reconciliation.md`). |
| D5 | CR-015 range | The model's 1895 total, about 7.1m at year end, is above CR-015's 4–6.5m. This is an author choice, already listed in CR-033's open choices. |

## Land Fund rows (only if CR-033 is adopted)

| ID | Where | Change |
|---|---|---|
| L1 | Events, or new Budget lines | **Costs:** annuities paid in goods; survey, the register and its assurance fund; licence commissioners and mounted police. **Receipts:** settlers' land instalments, fees on homeland leases, and land taken in payment for grant patents (CR-033 A17–A23). Keep the Land Fund apart from the revenues pledged to London. Add a check that the margin covers Budget T in 1852–1870 (A18). Prices, annuity terms and acreages are OPEN (CR-033 A9). The our-timeline anchors to source before use are the acreage reserved by the eighteen 1851–52 treaties and the acreage of confirmed Mexican grants. |

## Order of work

1. P6, P4 and P5 change nothing in the results, so make them first.
2. P2 with P1.
3. P3.
4. Recalculate, compare Story and Stress against `finance/CR-031-review.md`, and settle D1–D3.
5. L1 after CR-033 is adopted.

Then rerun `population/canon.py`. With P1–P3 in place, the reconciliation gap should be close to zero; any remaining gap shows what the sheet still does differently.
