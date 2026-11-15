# Phase 6: what the model allows

14 November 2026. Model plan for CR-059–065, 067 and 068, phase 6.

**Base.** The phase 5 workbook with the author's answers of 14 November, so the idle-gold rule (L17) is on and the held gold goes east in 1866–67. Its checks: Story 0 failed year-checks, Stress 17.

**Scripts** (all in this folder):
- `phase6_solver.py` patches the lever cells and recalculates Story and Stress in parallel. It reproduces phase 5 exactly.
- `phase6_ceilings.py`, `phase6_price.py`, `phase6_packages.py`, `phase6_sensitivity.py`, `phase6_robust.py`, `phase6_rebuild.py` do the searches.
- Results are in `phase6/`.

**Clean rebuilds.** Each package was rebuilt from the phase 4 workbook with `finance/build/cr059_068_levers.py --values phase6/package_K.json` and recalculated. All four match the solver, with no formula errors. Their Story workbooks are `phase6/Pacifica_financial_model_cr059-068_package_{A,B,C,D}.xlsx`.

## Result

1. **The war years are limited by one check in one case:** Stress private saving in 1862–64. Every lever spent in those years hits it.
   - The Richmond credit can reach about $26m in all.
   - The batteries can reach $8.75m a year.
   - The 1865–67 garrisons can reach $11.5m a year, limited by 1867.
   - Story never binds in the war years. Its tightest year has $16m of room left in every package.
2. **The four packages all pass**, under a rule stricter than the count alone (next section):

   | Package | What it buys |
   |---|---|
   | A | the Richmond credit at $26.3m |
   | B | the Honolulu batteries and slip, the 1865–67 garrisons and Sitka, at about 79% of their single ceilings, with the credit at its $2.4m floor |
   | C | every lever at 22% of its range |
   | D | the self-financing measures, which let the other levers reach 53% of their ranges |

3. **The packages sit on the edge.** Stress room in 1863 or 1864 is close to zero in each.
   - If the garrisons cost 25% more, about three-quarters of each package's extra spending survives.
   - If interior gold is 25% lower, packages A, C and D keep 94–97% of theirs. Package B keeps only 36%, because Sitka runs to 1900.
4. **Two findings outside the war years matter more than any lever:**
   - **The Stress private-saving check of 1932 is on a knife edge.** A cost that runs for decades, such as Sitka or the annuities, is capped by 1932 rather than by the war. Sitka's ceiling is $0.9m a year counting 1932, and $15m a year without it.
   - **The head counts are binding by themselves.** If the 1867 joins are 4% smaller than estimated (about 14,000 people), Stress reaches 18 with nothing added. The extra failure is the private-saving check of 1932 (corrected 14 November: the private-saving failures of 1914–24 already belong to the baseline 17).
5. **Some levers pay for themselves:**
   - **The credits.** Each $1m lent to Richmond or to Juárez brings back about $0.95m in interest by 1900, plus the repayments, and raises real GDP in 1932 by about $7m.
   - **The Oregon works.** On Development Fund credit, each $1m raises real GDP in 1932 by about $37m. Their ceiling, $14m a year in 1868–75, is set by Story in 1920: a larger economy needs more gold behind its notes.
   - **The scrip.** Buying it at 0.6 of face and crediting it at face in 1867 saves money. It also cures two Stress year-checks in 1932, debt and gold cover.

## The rule

The author's rule (13 November) is that every Story check passes and Stress has no more than 17 failed year-checks; 17 stays the ceiling (author, 14 November).

**Why the packages needed a stricter rule.** The first package runs showed the risk the plan names: Stress is a count, not a location. With the scrip at $3.2m, two Stress year-checks of 1932 stop failing. Every package then spent that saving on a new failure in 1863 or 1864, keeping the count at 17 while moving a failure into the war years (`phase6/packages_countrule.json`).

**What the packages use.** On 14 November the author agreed that the war years do not spend a check cured elsewhere (phase 5, open point 3). So the packages are solved under a stricter rule: the author's rule, and no Stress year-check up to 1900 that did not fail before. Under it, packages A, C and D end with Stress at 16, keeping the scrip's gain. Package B ends at 17: its Sitka spending adds one failure in 1932, which the rule allows.

**The single ceilings** use the author's rule. For a lever on its own, any new failure makes 18, so the two rules agree. For the long-lived levers, the table also gives the ceiling with failures after 1900 set aside.

## The levers: floor, ceiling alone, value in each package, price

The floor is the story minimum of phase 5. The ceiling is the largest value the model allows with every other lever at its floor. "Binds" is the check that fails just above the ceiling. The two price columns are the effect, in the Story case, of $1m more in all, spread over the lever's years.

| Lever | Floor | Ceiling alone | Binds | Without the 1932 effect | A | B | C | D | Real GDP 1932 per $1m | Interest back by 1900 per $1m |
|---|---|---|---|---|---|---|---|---|---|---|
| Richmond credit, total 1862–65 ($m) | 2.4 | 26.15 | Stress 1864: private saving | — | 26.34 | 2.4 | 7.69 | 15.02 | +6.6 | 0.96 |
| Technical mission, $m/yr 1862–65 | 0.1 | 5.631 | Stress 1863: private saving | — | 0.1 | 0.1 | 0.1 | 0.1 | -0.8 | 0.00 |
| Northwestern campaign 1861 ($m) | 6 | 23.5 | Stress 1861: private saving | — | 6 | 6 | 6 | 6 | -1.0 | 0.00 |
| Occupation 1862–64, $m/yr | 5 | 10.5 | Stress 1863: private saving | — | 5 | 5 | 5 | 5 | -0.9 | 0.00 |
| Held-territory garrisons 1865–67, $m/yr | 0 | 11.5 | Stress 1867: private saving | — | 0 | 9.12 | 2.56 | 6.11 | -0.7 | 0.00 |
| Honolulu batteries 1861–62, $m/yr | 0 | 8.75 | Stress 1862: private saving | — | 0 | 6.94 | 1.95 | 4.65 | -0.9 | 0.00 |
| Turret ship slip 1863–64, $m/yr | 0 | 6.031 | Stress 1863: private saving | — | 0 | 4.78 | 1.34 | 3.2 | -0.8 | 0.00 |
| Sitka garrison from 1867, $m/yr | 0 | 0.891 | Stress 1932: private saving | 15.25 | 0 | 0.71 | 0.2 | 0.47 | -5.3 | 0.00 |
| Northern mail from 1867, $m/yr | 0 | 0.891 | Stress 1932: private saving | 15.25 | 0 | 0.71 | 0.2 | 0.47 | -5.3 | 0.00 |
| Oregon scrip, face ($m) | 0 | 81.6 | Stress 1865: private saving | — | 3.2 | 3.2 | 3.2 | 3.2 | +0.2 | 0.00 |
| Union property 1867 ($m) | 0 | 15.25 | Stress 1867: private saving | — | 0 | 0 | 0 | 0 | -0.6 | 0.00 |
| Garrisons' keep 1864 ($m) | 0 | 21.75 | Stress 1864: private saving | — | 0 | 0 | 0 | 0 | -0.2 | 0.00 |
| Annuities, Northwest, $m/yr 1862–81 | 0 | 5.844 | Stress 1863: private saving | 5.531 | 0 | 0 | 1.3 | 0.45 | -1.5 | 0.00 |
| Annuities, Great Basin, $m/yr 1863–82 | 0 | 3.906 | Stress 1932: private saving | 6.031 | 0 | 0 | 0.87 | 0.2 | -2.4 | 0.00 |
| Annuities, Southwest, $m/yr 1862–81 | 0 | 5.531 | Stress 1863: private saving | 5.531 | 0 | 0 | 1.23 | 0.3 | -1.7 | 0.00 |
| Juárez credit 1865–66, $m/yr | 0 | 20.5 | Stress 1866: private saving | — | 0 | 0 | 4.56 | 10.89 | +7.1 | 0.94 |
| Oregon works 1868–75, $m/yr | 0 | 14.125 | Story 1920: gold cover | — | 0 | 0 | 3.15 | 7.5 | +37.1 | 0.00 |
| Private lending 1867 ($m) | 3 | 15.5 | Stress 1867: private saving | — | 3 | 3 | 3.45 | 3 | +0.0 | 0.00 |
| Legion pay 1863–67, $m/yr (deferred) | 0.15 | 6.025 | Stress 1863: private saving | — | 0.15 | 0.15 | 0.15 | 0.15 | -1.3 | 0.00 |

The full prices are in `phase6/price.json`: the Reserve Fund's lowest difference in 1861–67, the largest public-debt difference to 1900, and the development stock and real GDP in 1900 and 1932.

**Notes on the table:**
- The ceilings of the canon items (the 1861 campaign, the 1862–64 occupation) and of the fixed items whose amount is unknown (Union property, the garrisons' keep) show how much room canon leaves. They are not proposals to spend it.
- The Northwest annuities' ceiling is a little lower without the 1932 effect (5.53 against 5.84). The stricter rule refuses a new failure in 1863 that the count rule let through in exchange for a cure elsewhere.
- The scrip's ceiling of $81.6m is meaningless. Its bound is the source's $3.2m: the $6.0m claimed less the $2.8m appropriated.
- The private lending of 1867 has no public price, because it is private. Its $15.5m ceiling is set by Stress private saving in 1867; D8 asks for $3–5m.
- **Not searched:**
  - receipts, which always help, so their bound is their source (below);
  - the parameters the author fixed: the instalment option, the N-B credit, the New York share, the share kept at home, the idle-gold bound, the scrip price;
  - Victoria's frigates, which are 0 by the author's decision of 14 November.

## The packages

| | A Creditor first | B Fleet and garrisons first | C Balanced | D Self-financing |
|---|---|---|---|---|
| Rule | the credit as large as allowed | batteries, slip, 1865–67 garrisons and Sitka at the same fraction of their ceilings, then the credit | every lever at the same fraction of its range | D4–D10, then the rest at the same fraction |
| Fraction reached | 100% of the credit's range | fleet and garrisons 79%; credit 0% | 22% | 53% |
| Richmond credit, total | $26.3m | $2.4m (floor) | $7.7m | $15.0m |
| Honolulu batteries and slip | 0 | $13.9m and $9.6m | $3.9m and $2.7m | $9.3m and $6.4m |
| Garrisons 1865–67 | 0 | $27.4m | $7.7m | $18.3m |
| Sitka, garrison and mail | 0 | $0.71m + $0.71m a year | $0.20m + $0.20m a year | $0.47m + $0.47m a year |
| Annuities, NW / GB / SW, a year | 0 | 0 | $1.30m / $0.87m / $1.23m | $0.45m / $0.20m / $0.30m (matched to receipts) |
| Juárez credit, total | 0 | 0 | $9.1m | $21.8m |
| Oregon works 1868–75, total | 0 | 0 | $25.2m | $60.0m |
| Regional receipts, refugees | 0 | 0 | 0 | $0.95m a year; 20,000 a year in 1863–65 |
| Stress failed year-checks | 16 | 17 | 16 | 16 |
| Stress room, 1863 / 1864 | $3.0m / $0.0m | $0.0m / $2.5m | $0.1m / $1.3m | $0.0m / $0.1m |
| Public debt peak 1861–72, Story / Stress | $52.5m / $56.7m | $76.9m / $84.8m | $66.9m / $73.0m | $87.0m / $94.1m |
| Reserve Fund, end of 1872 (Story) | $43.4m | $8.6m | $4.5m | $2.8m |
| Real GDP 1932 (Story, 1913 $m) | 41,153 | 40,702 | 41,812 | 43,358 |

The story minimum, for comparison:
- Stress room is $6.0m in 1863 and $9.0m in 1864;
- the public debt peaks at $30.8m (Story) and $33.7m (Stress);
- the Reserve Fund is $62.0m at the end of 1872;
- real GDP in 1932 is 40,994 (1913 $m).

All four packages buy the scrip at $3.2m face. The canon items and the mission's pay stay at their values, and the Legion stays off.

**What the packages show:**
- **The credit and the fleet compete for 1862–64.** A takes all of that room for the credit, and B takes it for the ships and garrisons. B pays for it with the largest debt for what it buys and the lowest real GDP in 1932, because Sitka runs to 1900.
- **Packages C and D are not alike.** D spends far less on annuities, matching them to the regional receipts, and annuities are the levers that eat 1863's room. Its refugees and receipts add a little more. So the gap between D's 53% and C's 22% comes mostly from the annuities, not from self-financing as such.
- **D buys the most and ends the richest**, through the Oregon works ($60m) and the Juárez credit. It also carries the highest debt peak ($87m in Story) and leaves the Reserve Fund almost empty in 1872.

## The instalment split (CR-062 M2), against 1867

| Option | Stress room 1867 | Stress room 1868 | Story room 1867 | Gold paid out 1867 (Story) | Stress borrows in 1867 |
|---|---|---|---|---|---|
| (a) $8m + 5 × $6.4m | $13.9m | $19.3m | $39.1m | $58.0m | 0 |
| (b) six of $6.67m (chosen, D8) | **$14.4m** | $20.0m | $39.1m | $56.6m | 0 |
| (c) $10m + 5 × $6m | $11.9m | $18.0m | $38.8m | $60.0m | $0.7m |

All three options pass, and (b) leaves the most room. The gold paid out in 1867 includes the $39.8m of held gold going east (F18).

## The refugee stream (L12)

**The pool.** Of the men chosen in the Union's four drafts, about 161,000 of 776,000 failed to report and fled to the West, to Canada or to the woods (Hist.). The Provost-Marshal-General counted 230,148 deserters still at large at the end, non-reporting drafted men included (Hist.).

**The route.** The overland trails carried 10,000 people in 1863, 20,000 in 1864 and 25,000 in 1865 (Hist.). Their heaviest year, 1850, carried about 55,000.

**The ceiling.** An extra 33,000 a year in 1863–65 brings the trails back to about the 1850 peak, a third of the pool in three years. Above that the route, not the pool, is the limit.

**The finance.** The model sets no ceiling: 50,000 a year still passes, with Stress improving to 16. Refugees pay more than they cost, with these effects over 1863–85 (Story):

| Refugees a year, 1863–65 | Receipts | Spending | Residents 1900 | Real GDP 1900 | Stress room 1863 |
|---|---|---|---|---|---|
| 10,000 | +$22.7m | +$9.6m | +40,500 | +0.4% | $5.9m |
| 20,000 (in D, MODEL) | +$45.3m | +$19.0m | +80,300 | +0.8% | $5.8m |
| 33,000 (route ceiling) | +$74.2m | +$31.0m | +130,300 | +1.2% | $5.6m |
| 50,000 | +$112.0m | +$46.7m | +195,800 | +1.9% | $5.4m |

They cost a little room in 1863 before they pay: arrivals come before their taxes.

**Recommended:** 20,000 a year (D7), screened, with 33,000 as the ceiling. The population model's pools are unchanged. The refugees enter the workbook through Paths E only.

## The regional receipts (D4), MODEL

| Receipt | Estimate | Basis |
|---|---|---|
| Oregon's customs account, 1861–66 | $0.45m a year | the model's customs per resident (about $7) × the held Northwest, including Portland's Idaho trade (about 65,000–110,000 people), × 0.75 for occupation and smuggling |
| Washoe net-proceeds tax, 1864–72 | $0.15m a year | about 3% of the Comstock's net proceeds. The 1863 constitution taxed mines like other property and was rejected; the 1864 constitution capped the tax at 5% of net proceeds (Hist.) |
| Sunset road and Paso del Norte customs, 1862–72 | $0.30m a year | New Mexico's roughly 100,000 people at half the customs per resident |
| Snake and Fort Bridger road fees, 1863–72 | $0.05m a year | the trail traffic above at a few dollars a wagon |

The four together are under $1m a year, small against the war's costs. Self-financing works mainly by keeping the annuities to what the regions pay, not by raising money.

## Sensitivity

Each package was rerun with one uncertain fixed input moved against it. The table gives the share of the package's extra spending above the floor that still passes the strict rule. The self-financing parts of D stay as they are.

| Adverse case | A | B | C | D |
|---|---|---|---|---|
| Garrisons above the head counts × 1.25 (E07, E08, 1865–67) | 81% | 75% | 75% | 73% |
| Interior gold and silver × 0.75, 1863–72 | 94% | 36% | 97% | 95% |
| Every 1867 join × 0.75 | fails even at the story minimum (Stress 19) | | | |

**The head counts.** The tolerance search rebuilt the workbook from the phase 4 build with the joins scaled. Stress passes at 0.961 of the estimated joins and fails at 0.953. The joins total 350,036, so about 14,000 fewer residents in 1867 push Stress to 18. The only new failure is 1932's private-saving check; at three-quarters of the joins, 1932's interest check fails as well (corrected 14 November: the private-saving failures of 1914–24 already belong to the baseline 17). None is in the war years. War-year choices cannot fix this, but they can use up the margin it needs.

**Reading:** a package chosen at about 70–75% of its maximum survives dearer garrisons. Package B also needs far less Sitka to survive lower gold. Phase 7 should offer values at those fractions, not the maxima.

## The author's fix (14 November): more people, and Sitka paying early

The author proposed two fixes for the 1932 knife edge: more people, and making Sitka pay for itself early. A new lever, cw_alaska_rcpt (event E217, 1868–1900), carries the seal islands' lease and Alaska's customs. It is set at the historical lease of $317,500 a year: a $262,500 tax on 100,000 skins plus $55,000 rent. Historically the lease ran from 1870; here the Republic leases from 1868. The refugee lever L12 adds its value to arrivals in each of 1863, 1864 and 1865, so 20,000 a year means 60,000 people. Rule: strict (author's rule, no new Stress failure to 1900). Sitka ceiling = garrison, mail at 0 (`phase6_sitka_fix.py`; `phase6/sitka_fix.json`).

| Scenario | Stress margin, 1932 ($m) | Residents 1932 (Story) | Sitka ceiling ($m/yr) | Binding check |
|---|---|---|---|---|
| Neither | +3.9 | 36.75m | 0.89 | Stress 1932 private saving |
| Seal lease | +5.4 | 36.77m | 1.22 | the same |
| Refugees 20,000/yr | +16.6 | 36.92m | 3.89 | the same |
| Lease + refugees 20,000/yr | +18.0 | 36.94m | 4.20 | the same |
| Lease + refugees 33,000/yr | +26.2 | 37.04m | 7.98 | 1932 private saving and interest within 15% |

Stress stays at 17 in every scenario: the fixes widen the margin and cure no baseline failure.

**Head counts.** With the lease and 20,000 refugees a year, Stress passes at 0.789 of the estimated 1867 joins and fails at 0.781 (`phase6/heads_tolerance_refugees20k_lease.json`). That is about 74,000 fewer residents, against about 14,000 without the fix. The uncensused head counts stop being a knife edge.

**Reading:**
- The lease is worth about its face. It lifts Sitka's ceiling by $0.33m a year, roughly a third of a $1m garrison. It is a receipt and does not compound.
- People compound: each arrival saves, pays customs and raises children until 1932.
- Beyond about $15m a year, Sitka meets the war-year checks (the war-rule ceiling), whatever happens in 1932.
- Package D already contains 20,000 refugees a year; packages A–C do not. Adopting refugees would let A–C be re-solved with more room.

## Package D strengthened (author's choice, 14 November)

The author will take package D and asked how to make it as strong as possible. D's eight spending levers were held at one shared 53% of their single ceilings. That share was set by Stress 1863–64, where D has almost no room left ($0.02m and $0.07m). Four steps:

1. **The fix.** Add the seal lease and keep 20,000 refugees a year. Within D the lease adds little to 1932 (+$57m → +$59m), because D's own receipts and refugees already carry that year. At 33,000 refugees a year D fails 1863 by $0.14m, since refugees cost a little on arrival. A trim of $0.14m a year to the 1862–63 Richmond draw pays for it.
2. **The later levers raised alone** (`phase6_d_plus.py`). Growth first works better than Sitka first:

   | Order | Real GDP 1932 (Story) | Stress margin 1932 |
   |---|---|---|
   | Growth first: Oregon works, Juárez, garrisons, then Sitka | $43,668m | +$4.6m |
   | Sitka first | $43,469m | +$0.7m |

   Growth first raises the Oregon works from $7.5m to $14.8m a year (bound by Story 1920 gold cover) and Sitka from $0.47m to $3.9m. Every war year from 1863 to 1865 is then left with nothing.
3. **Strength means margin.** At 75% of that maximum, garrisons 25% dearer than the head counts add a war-year failure in 1863. The largest share that survives them is 73.4% at 20,000 refugees and 72.7% at 33,000 (`phase6_d_garrison_safe.py`).
4. **The head counts.** At 75% (20,000), Stress still passes the author's rule with every 1867 join at three-quarters of its estimate (Stress 17; `phase6/heads_tolerance_d_strong.json`).

Both strengthened packages pass clean rebuilds: Story 0, Stress 16, no formula errors (`phase6/d_strong/`).

| | D as solved | D strong (20,000 refugees, 73.4%) | D strong (33,000 refugees, 72.7%) |
|---|---|---|---|
| Richmond credit, total 1862–65 | $15.0m | $11.7m | $11.4m |
| Honolulu batteries, 1861–62 | $9.3m | $6.8m | $6.8m |
| Second turret ship, 1863–64 | $6.4m | $4.7m | $4.7m |
| Garrisons above the head counts, 1865–67 | $18.3m | $14.4m | $16.2m |
| Juárez credit, 1865–66 | $21.8m | $16.9m | $16.1m |
| Sitka garrison + mail, a year | $0.95m | $5.7m | $6.3m |
| Oregon works, 1868–75 | $60.0m | $86.9m | $84.2m |
| Seal lease, a year from 1868 | — | $0.32m | $0.32m |
| Stress room 1863 / 1864 / 1865 | $0.02m / $0.07m / $1.0m | $1.5m / $2.5m / $6.5m | $1.5m / $2.7m / $6.8m |
| Stress margin 1932 | +$57m | +$32m | +$36m |
| Survives garrisons × 1.25 | no (keeps 73%) | yes | yes |

**Reading.** The strong D gives up about a quarter of each war-year item. In return it gets six times the Sitka presence, half as much again for the Oregon works, and room in every war year to absorb dearer garrisons and short head counts. The extra 13,000 refugees a year buy more garrisons, more Sitka and $4m more margin in 1932, for a little less credit and works. The two strong versions are otherwise close. MODEL.

**Author's decision (14 November):** D strong, 20,000 refugees a year, trade accepted.

**Why D strong's 1932 margin is $25m lower** (author's challenge; `phase6_d_margin_walk.py`, `phase6/d_margin_walk.json`). The walk from D as solved to D strong, Stress 1932, one change at a time:

| Step | Margin | Change |
|---|---|---|
| D as solved | +57.2 | |
| + seal lease | +58.6 | +1.4 |
| + war-year items cut to D strong | +57.2 | −1.4 |
| + Oregon works $7.5m → $10.9m a year | +75.1 | +17.9 |
| + Sitka $0.95m → $5.7m a year (= D strong) | +32.1 | −43.0 |

**What the walk shows:**
- **The war-year cuts.** They are one-off and mostly loans repaid with interest, so they barely reach 1932. The small loss is interest no longer received.
- **The Oregon works** pay back in growth.
- **Sitka is the whole difference.** It is a cost every year from 1867 to 1900, about $160m more in all. Each $1m a year of Sitka costs about $9m of the 1932 margin. The chain: smaller surpluses, then a smaller Development Fund (its 1932 stock $1,240m → $1,085m in Stress), then less growth and fewer arrivals.
- **The model earns nothing from Alaska except the seal lease.** That is an assumption to challenge.
- **The Story case is better off in 1932 than under D as solved.**

## For the author (phase 7)

1. **Which package**, or which values within the ranges. For robustness, I recommend 70–75% of a package's maximum.
2. **The 1932 knife edge.** Should long-lived costs (Sitka, the annuities) be judged with the 1932 Stress check or without it? With it, Sitka can have $0.9m a year; without it, $15m. With the author's fix (lease + 20,000 refugees a year), $4.2m with the check.
3. **The head counts.** The 1867 joins are MODEL estimates with 4% of margin (21% with the author's fix). Phase 7 could firm up the uncensused ones (Deseret's growth, Washoe, Idaho, western Montana) before the author chooses.
4. **Refugees.** 20,000 a year as in D7, or more, up to the route's 33,000.
5. **The regional receipts** above are MODEL estimates.

## Sources (refugees, the Washoe tax, the seal lease)

- [McPherson, *Battle Cry of Freedom*, reader's note](https://www.goodreads.com/notes/8147859-battle-cry-of-freedom/20815803-paul-sorrells/86017c2e-5d3e-459b-b43a-79768147eccb): 161,000 of 776,000 drafted men failed to report, fleeing to the West, to Canada or to the woods.
- [Official Records, ser. III, vol. 5, p. 109 (Fry)](https://civilwar.com/official-record/990-union-letters-orders-reports/273181-109-series-iii-volume-v-serial-126-union-letters-orders-reports.html): 230,148 deserters still at large, non-reporting drafted men included.
- [Oregon Trail chronology (Historic Oregon City)](https://historicoregoncity.org/2019/04/03/oregon-trail-chronology/): 55,000 in 1850; 5,000 in 1861 and 1862, 10,000 in 1863; [the same chronology](https://historicoregoncity.org/?p=426): 20,000 in 1864, 25,000 in 1865 and 1866.
- [Mining taxes and the Nevada constitution (Mesquite Local News)](https://mesquitelocalnews.com/?p=4320): the 1863 constitution, which taxed mining like other businesses, rejected by four to one; the 1864 net-proceeds tax capped at 5%.
- [House Report 623 (1876), pp. 11–13 (Alaska Jewish Museum)](https://www.alaskajewishmuseum.com/media/t2jnkekl/housereport623-acc-fulfills-its-contract_pp11-13.pdf): $262,500 tax and $55,000 rent, $317,500 a year; [p. 8](https://www.alaskajewishmuseum.com/media/0m5h4ynt/housereport623-protection-us-interests_p8.pdf): the lease fixes $2.62½ a skin and $55,000 rent, above the law's $2 and $50,000.
- [Alaska Jewish Museum, mercantile trade](https://alaskajewishmuseum.com/exhibits/from-purchase-to-prosperity/mercantile-trade-and-transportation): the 1870 lease allowed 100,000 pelts a season.
