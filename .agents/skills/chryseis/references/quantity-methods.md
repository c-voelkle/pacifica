# Quantity estimation and calculation

Use these methods selectively. Follow the repository's established definitions and the actual draft. The aim is an auditable mechanism with useful uncertainty, not a point estimate selected to produce a preferred ending.

## Evidence and working estimates

Separate four roles: input quantities, calculated quantities, policy constraints, and desired outcomes. A desired GDP level, victory date, fleet parity, or political concession is not an input that can validate itself.

For each material new input:
- Prefer a directly applicable repository value or primary historical, engineering, demographic, or fiscal source. An inherited workbook amount remains an inherited model estimate.
- Seek comparable quantities in the relevant period, technology, geography, and institutions. For external research, retain the supporting source URL and page/table/section. Record an unavailable or weak analogue honestly.
- Show the raw observation, original unit/currency/year, conversion, and any explicit transferability adjustment. Keep an exchange rate distinct from a domestic price index or purchasing-power comparison.
- Triangulate high-impact estimates where possible. Use quantities and unit costs before aggregate ratios. Do not invent a citation or a precise historical value.
- Choose a central working assumption only when justified. Bounds should reflect identifiable uncertainty, not a universal +/- percentage. If a central estimate is unjustified, retain an interval or a missing dependency.
- Record independent source basis and narrative approval fields. Approving an event does not approve its cost, and a calculation does not approve the event.

Prioritize by likely materiality and sensitivity. Research to the precision useful for the decision; do not delay a supported provisional calculation for low-impact details.

## Mechanisms

| Requirement | Preferred build | Dependencies to preserve |
|---|---|---|
| Military campaign | Personnel x service time x pay/sustainment, equipment, ammunition, transport, medical care, losses, replacement, demobilization | Logistics throughput, mobilization, seasonality, existing readiness costs, coalition cost shares, continuing commitments |
| Railway or industrial project | Physical units x unit costs, construction schedule, maintenance, depreciation, commissioned capacity, utilization | Import content, local value added, labour and materials, lead times, land, counterpart demand and funding |
| Migration or training | Gross flows, retention/return, cohort survival and age, participation, training costs and delay | Housing, jobs, schooling, existing migration streams, additionality, people already included in resident or guest-worker totals |
| Lending or reconstruction | Borrower-specific drawdown schedule, funding, interest, maturity, amortization, restructuring and losses | Public/private/foreign ownership, collateral not pledged twice, cancellations, currency, income actually collectible |
| Banking and FX crisis | Bank capital, domestic liquidity, cash flows by currency, FX settlement dates, reserves and buffer requirement | Capital is not liquidity; domestic liquidity cannot automatically pay foreign-currency bills; commitments differ from drawings |
| Treaty or concession | Agreed rights, geography, duration, renewal, services, recurring cost, tax/royalty/dividend basis | Sovereignty, local ownership, consent, termination, enforcement cost, no automatic conversion of influence to fiscal receipts |

Costs released by a cancelled activity require an explicit use-of-resources policy: retain liquidity, repay debt, invest elsewhere, return funds, or leave resources idle. Preserve opportunity costs and transition costs. Do not assume every released worker, factory, or dollar moves immediately into productive civilian use.

An early armistice requires commitment and delivery schedules. Do not scale all war loans, industrial output, or costs by the fraction of war years avoided. Delivered goods, signed contracts, cancellation payments, inventories, existing capacity, and outstanding debt persist.

## Stocks, flows, and ownership

Maintain opening balances, movements, and closing balances with a declared sign convention. Amounts can be in period currency or constant prices, but they must carry their basis. Avoid mixing stocks and annual flows in aggregates.

- Treasury cash closes from opening cash plus cash receipts, principal repayments received, borrowing proceeds and asset disposals, less expenditure, new loan advances, asset purchases and debt principal repaid. Define categories so no flow appears twice.
- Loan claims close from opening claims plus advances and permitted capitalized amounts, less principal received, write-offs and disposals, with valuation/FX changes separately identified. Cash interest is income; loan principal is not profit.
- Public debt closes from opening face value plus issues, assumed debt and other noncash movements, less redemptions and write-offs. Issue proceeds can differ from face value. Interest belongs to the relevant dated borrowing schedule.
- Equity acquisition creates an asset and a cash use; dividends, operating profits, ownership value, and GDP are separate measures.
- An undrawn facility is a commitment. A guarantee is contingent exposure; model fees, collateral and actual calls separately. An expected-loss diagnostic is not automatically a realized cash loss.
- Track public, private, company/Crown and foreign holders separately. The entire syndicated issue cannot become a Treasury asset. A liability assumed without cash is not cash income.
- Domestic Treasury accounts, sovereign reserve investments and monetary gold have separate owners, liquidity, restrictions and currencies. Transfers among them are not new national resources.
- Match borrower liabilities to lender assets and lender receipts to borrower payments, with explicit fees, scope differences, losses and FX valuation where appropriate. Consolidate internal transfers once.

Budget balance excludes financing transactions under the chosen convention. Present loan advances, asset acquisitions and principal repayments alongside the operating/capital budget as needed to reconcile cash.

## GDP and national-income transmission

Begin by reproducing the baseline's actual equations and output perimeter. Identify historical calibration, exogenous future assumptions, and responses already present in those equations.

For an extension, choose a supported method:
- A region/sector production build based on labour, capital, productivity, commissioned capacity and utilization; or
- A documented modification of the baseline model using incremental domestic value added and explicit changes to its drivers.

Respect the national-accounting identity used by the model. Do not add the full revenue of intermediate suppliers to final production, or add exports again to production already recorded. Net out imported content where appropriate. Avoid double-counting technology, migration or industrial activity already present in the baseline.

Domestic investment spending is not an equal immediate permanent increase in GDP or productive capacity. Model construction, domestic value added, commissioning lags, depreciation, utilization and later productivity separately. A small illustrative capital build is opening productive capital less depreciation plus completed additions, with capacity entering production on the commissioning date.

Keep resident production, overseas production, foreign income and allied/network GDP separate. Foreign ownership, a common crown, transit rights, or a treaty does not annex the partner's output. Use an explicit changing territory/membership map.

Carry through tax bases, tariff/import shares, effective collections, royalties, company distributions, and public spending responses. Explain residual or imposed growth assumptions. Do not call a model fully endogenous when an important future path is held fixed.

Report nominal GDP for fiscal reconciliation and real GDP at a common base for prosperity comparisons. Compare per-person measures using the appropriate population. Sum cumulative real flows only after conversion to the declared common price base; keep nominal cash totals labelled as nominal.

## Uncertainty and fairness

Separate:
- Parameter uncertainty: costs, productivity, utilization, losses, repayment and timing.
- Political branches: a treaty accepted, reforms failing, intervention chosen.
- Structural uncertainty: missing transmission channels or competing economic mechanisms.
- External shocks: physical disasters or specified international disturbances.

Use central and adverse parameter sets or sensitivity sweeps with explicit bounds and dependencies. Account for correlated assumptions; avoid making every uncertain input simultaneously favourable. A range of selected cases is not a probability distribution.

If stochastic trials are requested and justified, document distributions, correlations and seeds. Match exogenous realizations across alternatives by stable entity/event keys so adding an event does not scramble all common shocks. Keep narrative success assumptions separate from modelled stochastic outcomes.

A no-general-war reference remains a no-general-war scenario when testing a severe recession or failed reform. A renewed general war is a separately named structural branch.

Report useful break-even thresholds when possible: the maximum recurring security cost, minimum civilian demand, or recovery rate at which a preferred economic outcome reverses. Distinguish those thresholds from predictions.

## Meaningful checks

Choose checks appropriate to the calculation:
- Zero-change replay matches the baseline; sibling scenarios cannot mutate each other's inputs.
- No change appears before its earliest causal date unless the scenario explicitly models anticipation.
- Currency, price base, scale, period, geography, and stock/flow definitions agree.
- Cash, debt, claims, capital and population roll forward correctly.
- Financing is allocated once and capacity is not exceeded without a reported gap or response.
- Removed commitments lose only the appropriate future flows; existing liabilities remain.
- A moved assumption of debt uses the balance at the new date, not the old nominal amount.
- Common controls and shock sets permit the intended comparison.
- Missing inputs and failed calculations remain visible rather than producing a plausible zero.

State the checks executed and their results. Financial consistency is distinct from whether the political or military premise is plausible.
