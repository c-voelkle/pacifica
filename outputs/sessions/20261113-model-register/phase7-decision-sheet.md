# Phase 7: the decision sheet

**Author's decision (14 November 2026): Q1–Q8 all approved as recommended.**

*CR-059–068 model plan, 14 November 2026. Every lever's value for the package to be written into the workbook in phase 8, what the author has decided, and the questions still open. All amounts are MODEL; all workbook statuses stay "Proposed" until the CRs are integrated.*

## 1. What the author has decided (13–14 November 2026)

| Item | Decision |
|---|---|
| The rule | Every Story check passes. Stress has no more than 17 failing year-checks (D14). Packages also add no new Stress failure up to 1900 (the strict rule; open point 3). |
| F18, L17 | No treasure steamers to New York 1861–65; the held gold goes east in 1866–67. The idle-gold bound for war bonds is 0.12 of notes and bank reserves in Story and 0.06 in Stress (D10–D13). |
| L01 mission | $0.1m a year (D16). |
| L02 frigates | None beyond the Navy plan: Victoria's frigates are its two 1861 cruisers, handed over after the war (D15). |
| E14 | Private lending, $3m in 1867 (D17). |
| L05 | Instalment option (b), six of $6.67m (D8). |
| L15 | Approved: the new members' public land enters the Land Fund from 1867 under the existing rules (Q7). Not yet built. |
| Package | D (self-financing), made strong: 73.4% of its strengthened maximum, the later levers raised growth first. The trade is accepted. |
| L12 refugees | 20,000 a year, 1863–65. |
| Alaska (CR-070) | All ideas in. The finder's share is negotiated on top of the state's 5%. The taper runs from 1873 at 40%. §14 is amended. The Bering telegraph is OPEN pending research. |

## 2. The package to write in (D final)

The values are the same in Story and Stress; each case keeps its own assumptions (F18's home share, L17's bound and the rest of the Levers sheet). "Solver" means the value phase 6 found under the strict rule.

| Lever | Value | Source | Meaning |
|---|---|---|---|
| **Credits and war** | | | |
| cw_rich_early / cw_rich_late | 1.458 / 4.375 $m a year | Solver (D strong) | The Richmond credit, $11.7m over 1862–65 |
| cw_mission | 0.1 | Author | Eastern technical mission |
| cw_war61 / cw_occ6264 | 6 / 5 | Canon (E07, E08) | The campaign and occupation above the head counts |
| cw_occ6567 | 4.785 | Solver | Garrisons of the held territories, 1865–67 |
| cw_hon_batt / cw_hon_turret / cw_hon_frig | 3.414 / 2.353 / 0 | Solver; frigates author | Honolulu batteries 1861–62, the second turret ship's slip 1863–64 |
| cw_legion_on | 0 | Deferred (author) | The Nauvoo Legion's pay |
| **Alaska (CR-070)** | | | |
| cw_sitka_gar | 2.848 | Solver | The garrison and squadron, 1867–72 |
| cw_sitka_taper | 0.4 | Author | The garrison at 40% from 1873 (settler soldiers) |
| **cw_sitka_mail** | **0.3** (was 2.848) | **Recommended here (Q1)** | The northern mail |
| cw_alaska_rcpt | 0.3175 | Hist. | The first seal lease, 1868–79 |
| cw_seal_1880s / 1890s / after | 0.5 / 0.85 / 0.85 | Author (CR-070 D1–D2) | The tendered lease and the herd saved |
| cw_ak_salmon | 1 | Author (D4) | The case tax path |
| cw_ak_gold_lead / cw_ak_seward | 8 years / 1.0 | Author (B2, B3) | Juneau from 1872; the Seward Peninsula from 1876 |
| cw_ak_commission | 0.15 | Author (A1) | The Northern Commission, 1867–85 |
| cw_ak_telegraph | 1 (provisional) | OPEN (Q5) | The Bering telegraph's cost |
| cw_ak_route | 1 | Author (F) | The Chilkoot compact and the early Yukon route |
| **The price and its set-offs** | | | |
| cw_inst_opt | 2 | Author (D8) | Six instalments of $6.67m |
| cw_scrip_face / cw_scrip_price | 3.2 / 0.6 | Source ceiling | Oregon scrip, credited at face |
| cw_nb_credit / cw_setoff_nc | 1 / 0 | Canon / default | N-B annuities credited; the N-C deduction not set |
| cw_union_prop / cw_keep64 / cw_keep67 | 0 / 0 / 0 | Default (Q6) | Union property; the withdrawing garrisons' keep |
| **Annuities and receipts** | | | |
| cw_ann_nw / cw_ann_gb / cw_ann_sw | 0.45 / 0.20 / 0.30 | D4–D10 (self-financing) | Equal to each region's receipts |
| cw_rc_or / cw_washoe / cw_rc_sw / cw_rc_gb | 0.45 / 0.15 / 0.30 / 0.05 | MODEL (Q4) | Oregon's customs, the Washoe tax, the Sunset road, the Snake and Bridger roads |
| **Peace and growth** | | | |
| cw_juarez | 8.436 | Solver | The Juárez credit, 1865–66 |
| cw_or_works | 10.867 | Solver | The Oregon works, 1868–75 |
| cw_priv1867 | 3.0 | Author | Private lending, 1867 |
| **People and gold** | | | |
| cw_refugees | 20,000 a year | Author | 1863–65 |
| cw_ny_share / cw_ny_home / cw_ny_return | 0.85 / 0.5 (Stress 0.25) / 1 | Author (F18) | |
| cw_idle_ratio | 0.12 (Stress 0.06) | Author (L17) | |

## 3. What it does (MODEL; phase 6 and 7 runs)

| | D as solved | D strong | D strong + Alaska | **D final (mail 0.3)** |
|---|---|---|---|---|
| Stress failing year-checks (ceiling 17) | 16 | 16 | 16 | **15** |
| Stress margin of private saving, 1932 | +57.2 | +32.1 | +48.7 | **+79.5** |
| Stress room 1863 / 1864 / 1865 ($m) | 0.0 / 0.1 / 1.0 | 1.5 / 2.5 / 6.5 | 1.5 / 2.5 / 6.5 | 1.5 / 2.5 / 6.5 |
| Story real GDP, 1932 ($m, 1913 dollars) | 43,358 | 43,469 | 43,863 | **44,295** |
| Story residents, 1932 | 37.92m | 38.05m | 38.18m | **38.32m** |
| Garrisons above the head counts × 1.25 | fails (strict) | passes | passes (+39.9) | **passes (+70.8)** |
| Clean rebuild | passes | passes | passes | **passes** (Story 0, Stress 15, no formula errors; `phase7/d_final/`) |

The Stress failures that remain are the baseline's own: 1887, 1914–24 and 1927 (`phase7/d_final/package_D_final_stress.json`). **1932 now passes every check in Stress.** The knife edge is gone, because the cut in the mail removes a cost of about $2.5m a year from 1867 to 1900.

## 4. Questions for the author

**Q1. The northern mail (new; recommended: $0.3m a year).**
- The solver raised the garrison and the mail together, so the mail sits at $2.85m a year for 34 years.
- For scale: the Union's Congress paid Pacific Mail $500,000 a year for the whole San Francisco–Hong Kong mail from 1867 (Hist.). A coastal mail to Sitka at nearly six times that has no story reason.
- At $0.3m a year the 1932 Stress margin rises from +$48.7m to +$79.5m, Stress falls to 15 and real GDP in 1932 rises by about 1%; at $0.5m the margin is +$77.1m (`phase6/mail_test.json`).
- **Recommended:** $0.3m, and use part of the room if a scene needs a bigger Sitka.

**Q2. Does the 1932 Stress check govern long-lived costs?**
- With D final, 1932 passes with $79m to spare, so the question no longer binds.
- **Recommended:** yes, keep it governing, as the rule has run all along.

**Q3. Firm up the uncensused head counts?**
- The margin was 4% at the story minimum. D strong still passes the author's rule with every 1867 join at 0.75 of its estimate; D final has more margin.
- **Recommended:** no firming needed before integration. Deseret's growth, Washoe, Idaho and western Montana stay MODEL, with the research list of phase 3.

**Q4. The regional receipts (D4).** Oregon's customs $0.45m a year 1861–66, the Washoe net-proceeds tax $0.15m 1864–72, the Sunset road and Paso del Norte customs $0.30m 1862–72, the Snake and Fort Bridger road fees $0.05m 1863–72; derivations in the phase 6 note. **Recommended:** approve as MODEL working figures.

**Q5. The Bering telegraph's cost (CR-070 E1–E3, OPEN).** **Recommended:** keep it in the model at 1 until the research decides. It is the conservative choice: dropping it adds about $3m to the 1932 margin.

**Q6. The levers at zero.** Union property at valuation (F13), the withdrawing garrisons' keep (F14), the N-C deduction (L07) and the Legion (deferred). **Recommended:** confirm 0. Each is a story decision the drafts leave open; none is needed for the money to work.

**Q7. L15, Oregon's schools.** The ceded public domain enters the Land Fund from 1867 (decided). The schools' share of its margin needs a number (CR-059 CT13, open 44).
- For scale: the Union's admission act for Oregon (1859) gave the state sections 16 and 36 of every township for schools, two in 36 (Hist.; to verify).
- **Recommended:** a schools' share of one-eighteenth of the margin on Oregon's public land, the same proportion.

**Q8. One package for both cases.** The levers take the same values in Story and Stress, as in phase 6. **Recommended:** confirm.

## 5. Phase 8, once the author answers

1. Write D final into the canonical workbook, `finance/Pacifica_financial_model_1846-1932.xlsx`:
   - the phase 4 builder (`cr059_068_civil_war.py`), then the levers builder (`cr059_068_levers.py --values`);
   - L15 built in the Land Fund and Budget sheets;
   - recalculate both cases and check against this sheet.
2. Write the workbook note, `finance/CR-059-068-workbook.md`: the levers, the values, the results, Stress's remaining failures and what the checks show.
3. Re-run the population model with the joins, refugees and Alaska's residents (MODEL).
4. Check the storyline's MODEL figures against the new workbook and list any that need updating at integration.
5. Commit the model work on `models/cr059-068-civil-war` when the author asks.

## Sources

- [Hong Kong in texts: the Pacific Mail's subsidy](https://hkintexts.histsyn.com/page/1875374): $500,000 a year for the San Francisco–Hong Kong mail.
- Phase 6 note (`phase6-ranges-packages.md`), CR-070, and the runs in `phase6/` and `phase7/`.
