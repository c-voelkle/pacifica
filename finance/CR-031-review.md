# CR-031 financial reference review — 23 October 2026

## Current source and scope

The author-supplied `Pacifica_financial_model_1846-1932_cr-031.xlsx` is published byte-for-byte at [the stable current-workbook path](Pacifica_financial_model_1846-1932.xlsx). SHA-256: `29aaeaafeeef712ff6c276c71495c461a122f111726abdafacd558f9bab30091`. It supersedes the earlier workbook. The older [Pacifica Ledger](Pacifica-Ledger.md) is retained unchanged as a CR-021 revision-8 snapshot; it is not a dashboard for CR-031.

This documentation review extracted all thirty sheets, their saved values and formulas, and checked the ZIP archive. It found 48,940 formulas, 0 stored Excel error cells and 0 formulas without a saved value. The saved case is `Story case` and `Start!C5` reports 0 flags. These are saved results supplied by the author. No native Excel recalculation, Stress-case trial or independent engineering/bank certification was performed, and the workbook was not edited.

## Saved Story-case reference values

| Measure | 1929 | 1932 | Source cells |
|---|---:|---:|---|
| Pacifica core GDP, period $bn | 50.781 | 39.495 | Start!K12:L12 |
| Residents, millions | 25.516 | 27.318 | Start!K9:L9 |
| Public debt / core GDP | 5.00% | 5.49% | Start!K32:L32 |
| Pacific order / Union money output | 1.167 | 1.756 | Start!D55:D56; E55:E56, independently divided |
| Core output per resident / Union comparator | 2.248 | 2.977 | Start!K13:L13 |

The order includes allied economies, not only Pacifican sovereign territory. These are period-money comparisons, not proof that the order surpasses the Union in real output. Foreign concession gold is purchased into reserves and remains outside domestic GDP.

Japan’s rescue requires $496.861m of drawing within $600m committed: $165.620m public and $331.241m private, retaining a $375m import buffer (`Japan rescue!D9:D19`). Domestic bank capital is $400m and BOJ liquidity $295m. Their sum is not another foreign drawing. Matching on-loans, lender claims and 1929–1933 repayment remain MODEL mechanisms.

Foreign Entente subscriptions total $3950m, independently matching named sources: Union investors $1950m, collateral loans $800m, Japan $600m, neutrals $250m, Gulf/Latin America $350m (`Entente subscribers!B11:I11`). Foreign subscribers retain their own claims and risk. The narrative’s $8.5bn total advance also contains Treasury and Pacifican private subscriptions.

## Narrative commitments and accounting boundaries

| Revision | Current financial treatment | Trace / qualification |
|---|---|---|
| CR-028 | £3m Mexican obligations booked at $14.6m in 1848; October-only royalty adjustment; claims and whaler/customs adjustments | Events!6 and 153:156. Proposed recognition machinery and first-service timing are not proved by the model |
| CR-029 | $20m Philippine purchase paid by guaranteed Philippine Redemption Loan, including repayment of the prior advance | Events!31, 120:121. Zero core purchase cash does not mean free territory or no guarantee exposure |
| CR-029 | Approximately $9.5m residual Philippine bonds assumed in 1914 | Events!146. Keep principal assumption, continuing service, incremental-revenue covenant and Philippine population separate |
| CR-029 | Tobacco/abaca charter receipts, dividends and peso reserve income | Events!147:152. MODEL amounts; neither receipts nor Crown shares turn the islands into core GDP |
| CR-030 | Five railway sections, quarterly campaign and annual standing-front schedule feeding Events | Siberia; Events!157:169. 1919 $348.95m; 1920 $288.68m. Capacity, troop numbers, depots and costs remain assumptions |
| CR-031 | Relief $1.5m and trader-debt write-down $0.5m; Commander Islands price $0.1m and seal receipts $0.2m a year from 1922 | Events!170:173. MODEL estimates, not recovered historical accounts |
| CR-031 | $3m Company stake over 1927–1929, conservatively booked as Treasury cash; no dividends counted | Events!174. Stake, foreign company operations, forced labour and Kolyma reserve purchases are distinct |

## Source discrepancies retained for the author

The following are observations, not additional canon decisions. Supplied bytes are unchanged.

- `Start!B2` still describes an 18 October rebuild, although Events includes CR-031 entries and the workbook contains later schedules.
- `Siberia!A2` says four railway sections; the actual header lists five (`AM5:AQ5`), as does CR-030’s synopsis.
- `Entente subscribers!A1` says foreign $4.25bn; the named total and required foreign subscriptions at `G11:H11` are $3.95bn.
- `Events!M174` describes approximately 30% Pacifican Company capital; the master proposes one-third. The $3m cash schedule does not settle that ownership fraction.
- Events labels some CR-031 mechanics Approved, and CR-028’s assumed debt Canon, while the matching detailed master passages remain PROPOSED. Financial metadata does not promote those passages to approval.
- The master’s approximate output ratios (1.16, 1.74 and 2.24) are earlier rounded references. The supplied saved workbook gives 1.167, 1.756 and 2.248. The master is preserved verbatim, and the documentation identifies the current source rather than silently changing its numbers.
- No named Puʻuloa Crown-rent line was found in the extracted Events descriptions. General harbour spending is not evidence of rent. The earlier [handoff](CR-027-handoff.md) still leaves the amount and estate classification unquantified.
- The master’s CR-021 overview dates Rey de Filipinas from 1914, while the detailed CR-029 passage marks the combined style PROPOSED and places the Manila oath in 1915. The character documents distinguish the settlement, accession rite and proposed full style; no missing instrument is invented.

Historical and engineering follow-up remains in [the feasibility audit](../book-agent/revision/war_base_assumptions.md). None of these discrepancies authorizes rewriting source proposals or committing ledger-style claims as actual history.
