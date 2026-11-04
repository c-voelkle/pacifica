# Note for the financial workbook's next build: the investment account, and the industrial series the energy workbook reads (CR-052 M2) — v2

**Status:** PROPOSED handoff, v2, 4 November 2026, after Sol's review of v1 (author: "Sure go ahead"). v1's hardship threshold and its 0.62–0.68 industrial-weight estimate are withdrawn as unsupported; the energy workbook's seventh build has made the changes on its side. Nothing in the financial workbook is changed yet. All figures MODEL.

**Read with:** `book-agent/revision/CR-052.md` (M2, F1, F12), `energy/CR-052-workbook.md` (seventh build: the calibration hook `ind_idx`, the Fund-credit cap, the revenue split, the `en_*` columns), `finance/CR-041-workbook.md` and `finance/CR-050-workbook.md` (the current financial workbook, SHA `22266bad…`), `energy/build/extract_finance.py`.

## What was decided and what was corrected

The author's direction (4 November) is that Pacifica reallocates from consumption to investment and that technological deflation is a visible fact of its 1920s. v1 turned that into a mechanism and a number. Sol's review (same day) accepted the test and corrected the number and two of the claims:

- **Proportional arithmetic.** Investment rising from 26% of GDP in 1913 to 28% in 1929 takes `ind_w` from 0.50 to about **0.54** if industry's share of GDP moves in proportion. v1's 0.62–0.68 requires industry's share to rise a quarter to a third above 1913, which is possible (domestic machinery, metals, manufactured exports) but has to be shown in amounts, not asserted. **`ind_w` is therefore a sensitivity, 0.54 the proportional baseline, until the amounts exist.**
- **The 2.35× figure is not purchasing power.** The financial workbook's "GDP per person about 2.3 times the US's" is a current-dollar comparison with the historical US; it says nothing about what households can buy, so v1's "35% investment would bring the Bread March back" was unsupported and is withdrawn. The consumption-per-person column proposed below is what answers that question.
- **There is no industrial deflator to correct.** Sol traced the formulas: the financial workbook divides nominal GDP by one general price index; core non-mining output starts in real terms; the champions mix physical quantities × dollar margins with dollar sales and value-added assumptions. v1's deflator question is answered: nothing to re-deflate. Physical quantities (steel, vehicles) are the right driver of energy demand; sector prices affect nominal sales and margins only. A higher real industrial estimate does not by itself mean more tonnes or more energy.
- **US anchor.** Kuznets puts US gross domestic capital formation at 20.6% of GNP in 1919–28 (Table I-3; NBER c1303). The other international anchors in v1 (Japan, the USSR, Germany) remain unverified and are not relied on.

## The build spec (Sol's four changes, as the financial workbook's next build)

### 1. A domestic investment and consumption account

Add to the financial workbook, at baseline GDP first so the reallocation is visible:
- gross domestic fixed investment by year, with imported equipment identified separately from domestic;
- foreign loans and stake purchases (the Entente and Japanese credits, the Russian reconstruction credit, the CR-053 stakes) kept apart from domestic investment;
- household consumption per person, after government consumption and net exports (BEA expenditure accounts as the template);
- an `inv_share` path: **Story 27–29% of GDP in the 1920s** as the test value (about 15% at settlement, 18–20% in the 1860s–70s, 22–25% under the regency, 25–27% in 1900–13, 22–24% in 1914–19 when the war's capital went abroad, 24–26% in 1930–32); Stress five points lower.
- The consumption-per-person column is the author's trade-off view: a higher investment share is a lower consumption share, and whether Pacificans in the 1920s still live visibly better than the Union's citizens is read from this column, not from the 2.35× figure.

### 2. Derive the energy input from domestic production

- From the investment mix, domestic sourcing and manufactured exports, estimate the change in energy-relevant industrial output (metals, machinery, chemicals, building materials) relative to 1913; check it against the physical series the workbook already has (steel, vehicles) and the champions' tonnages.
- Export it as a Story and Stress series through `energy/build/extract_finance.py` (one new row in `FIN_KEYS`), indexed to 1913 = 1.
- The energy workbook reads it as Paths `ind_idx` (seventh build; 1 until exported) and scales **both** `ind_w` (factory motors) and `ind_mj` (industrial fuel) by it, so the two intensities are calibrated to the same series rather than set independently. Sol's proportional estimate implies about 1.08 by 1929.
- The Max case's electrified process heat is now its own switch in the energy workbook (`heat_el`; Paths `indw_x` applies only with it), so a higher finance series is never multiplied by the Max factor.

### 3. Model cheaper industrial goods separately

- For steel, vehicles and the other sectors with quantities, keep the quantities as the driver of energy demand and test sector-specific prices for nominal sales and margins (falling faster than the general index where Pacifica's productivity lead is real).
- This changes nominal GDP, debt ratios and the gold-standard story (CR-020's ten-cent oil, the 1931 sterling undercut), not the physical weight of industry. It is also the storyline's sentence: cheaper cars, power, aluminium and film every year, a Reserve Bank managing falling prices, savers who hold gold coupons because everything else gets cheaper.

### 4. Reconcile the energy handoff before rerunning F1

What the energy workbook's Story case now asks of the financial workbook, and how each item maps:

| Item | Energy (Story, seventh build) | Finance now | Mapping (payer → recipient) |
| --- | --- | --- | --- |
| Home oil | CR-052 C with M8: 228m bbl 1913, 304m 1924, 255m 1929, 229m 1932 (Paths `oil_c52`); the 1932 compact a separate switch (`compact_on`, Story 0) | 100, 230, 300, 153 | a **replacement path** for `oil_out`; the compact's price floor a separate decision |
| Vehicles | about 2.15m built a year by 1929 (CT5, `veh_build`) | 1.15m | `Champions!U` rises to match |
| Power capex | `en_power_capex`: $0.76–0.92bn a year 1922–29 (1.3–1.7% of GDP) | no power line | counted **once**, as domestic fixed investment |
| Fund credit | `en_dev_power_credit`: capped at `df_max` × the Fund's investment (about $0.29–0.32bn a year 1924–29) | Fund invests in `Debt & cash!I` | **financing** of part of the capex, not additional investment; the Fund → utilities |
| Private financing | `en_power_capex_private`: the remainder (about two thirds in the 1920s) | — | utilities' bonds and shares, champions' retained earnings, the Reserve Bank in the slump |
| Electricity revenue | `en_elec_revenue` gross ($1.59bn 1929); `en_elec_revenue_utility` ($1.27bn) and `en_elec_revenue_selfgen` ($0.32bn) | — | only utility receipts are sales; self-generation is a cost inside the champions |
| Royalties | `en_royalties` (about $3m a year by 1927) | — | utilities → the compact peoples (CR-051 S8) |
| Fuel trade | `en_oil_import_value`, `en_coal_import_value`, `en_fuel_trade_net` | the trust's Gulf and Asian sales | the trust's purchases of Gulf crude; the CR-053 entitlements priced separately |
| CR-053 | stake costs (1920–28), dividends, entitlement crude (8m bbl 1926, 20m 1929, 24m 1932) | — | kept apart from domestic investment and from the Gulf trade |
| Asian exports | the sixth build defers 8–21m bbl a year of home-refined Asian exports from 1915 (the import ceiling binds) | `asia_oil` with `asia_home` = 0.5 from home crude | the Asian contracts served from Gulf crude in those years: `asia_home` effectively 0.25–0.3 after 1915 (OPEN) |

Then rerun Story and Stress and report, against the seventh-build baseline: consumption per person; the Fund's capacity against the power credit (check 6 is now a real test); fuel security (unmet demand, motor-fuel rationing, stocks); and the electricity multiplier against **2.29–2.85× in 1920–32** (Story) — the F1 figure CR-052 will carry.

## What the energy workbook has already done (seventh build, 4 November)

- `heat_el`: the Max case's process heat as its own switch (Story 0, Max 1).
- Paths `ind_idx` on `ind_w` and `ind_mj` together, 1 until finance exports the series.
- Fund credit capped at `df_max` × Fund investment; `en_power_capex_private`; check 6 tests the 4%-of-GDP ceiling and the cap, with no waiver when the Fund invests nothing. It passes in every case.
- Revenue split by `self_gen` (Story 0.2): `en_elec_revenue_utility`, `en_elec_revenue_selfgen`.

## Open

- The `inv_share` path and the industrial-output derivation (Sol, with the author).
- Whether 0.54 (proportional) or a higher calibrated value is adopted once the amounts exist; Max keeps `heat_el` as a sensitivity.
- `asia_home` after 1915.
- `self_gen` share (to verify against the US industrial-plant share).
- The anchors marked *to verify*: Kuznets is cited; the rest are not.
