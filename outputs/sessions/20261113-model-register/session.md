---
session: 20261113-model-register
started: 2026-11-13
updated: 2026-11-14
mode: draft
status: phase-8-done
baseline:
  commit: bee7f76
  branch: models/cr059-068-civil-war (local, off revision/cr059-oregon)
independence: same-agent (no fresh-context review of the register yet)
---

# Phases 1 and 2 of the model plan: the event register and the fixed/free split

## Brief

- **Desired outcome:** every model-relevant item of CR-059 to CR-065, CR-067 and CR-068 in one register row, with an owner, a status and a place in a model; each row marked fixed or free; the split ready for the author's review (plan of 13 November 2026, phases 1 and 2).
- **Authorization (author, 13 November 2026):** "Phase 0 is done. Can you please do Phases 1 and 2 and then let me review the categorization?"
- **Out of scope:** any change to a workbook, the population model or a draft; phases 3 onward.

## Input

The register was first built from the drafts themselves at `bee7f76`, before the plan's workbook `Pacifica_CR059-068_model_events.xlsx` (584 items) reached this session:

- every row of the nine drafts' **Decisions** tables (646 rows, including CR-068's K1–K27 in `CR-068-lincoln-career.md`);
- every item listed in the drafts' **Financial and population models** sections and CR-068's "For integration" (32 items);
- nine items that live outside those places (CR-068 CT28, CR-060 Part V and similar), cited by section.

`build_register.py` reruns the whole thing. `crosswalk.csv` maps each of the 687 source items to exactly one register row; `register.csv` holds the register rows.

**The 584-item workbook (supplied 13 November 2026, 18:58).** `map_events.py` maps every item to exactly one register row: 291 through the decision IDs in its "CR ID / lines" column, 293 by reading the item (`events_mapped.csv`). The workbook is wider than the decision tables: it also lists pre-war baselines, Union-side items, logistics data points and items after 1872. That added 21 register rows (113 in all), which hold 85 of its items:

| Added | Rows |
|---|---|
| Finance | F17 Sausalito storehouse; F18 no treasure steamers to New York 1861–65; F19 Hawaii's agreed revenues (canon) |
| Memo | M11 confederal courts in the compact territories; M12 Oregon's softened slump; M13 grants to county boards; M14 defence organisation; M15 the Chancellor's six months; M16 guano islands and Midway |
| Population | P01i South Park and the upper Arkansas; P06 the Chinese floor; P07 entry controls (Texas line 1863; railway and ports 1871–72); P08 Assembly seats by population; P09 Hawaii's entry control from 1864; P10 displaced Unionists and the citizenship choice |
| Logistics | G12 the Columbia and the routes into Idaho; G14 wagon-road unit constants |
| Other | B01 pre-war baseline already in canon; C01 Colorado 1875–82 and Y01 after 1872 (class "Later round"); X05 Union-side items with no Pacifican entry |

**Where the workbook and the register read an item differently.**
- Items 391 and 400 read Lincoln's 1864 offer to admit Hawaiian sugar as "fixed-price sugar procurement from Hawaii 1864–65". The offer is refused (CR-068 G8, PP9); no procurement follows. Filed under no model place.
- Items 55 and 57 correct the register: the "some five hundred" Washoe volunteers of 1860 are canon (§8), restated in CR-067's "What canon says". The plan's E06 note stands; E06's $1m is unchanged.
- The workbook has no item for western Montana's head count (P01f), the Comstock's energy load (N01) or the Columbia's hydro sites (N05). They stay in the register from the drafts and the plan.
- 20 items say themselves that they change no model (the Gadsden split dropped, the Union's cabinet, the Council's size). They are filed under no model place and kept.

## Result

| Class | Register rows | Workbook items | Meaning |
|---|---|---|---|
| Fixed | 40 | 244 | value given by a draft or the record; entered as is |
| Fixed (unchanged) | 6 | 29 | named in the drafts, no change to the model |
| Lever | 18 | 151 | value left open; sized in phases 5–6 |
| Fixed? (author) | 11 | 34 | the classification itself needs the author (questions below) |
| Memo | 21 | 43 | small or pass-through; noted, not sized |
| Deferred by author | 1 | 1 | the Nauvoo Legion's pay |
| Not the model's | 5 | 41 | listed, not sized |
| No model place | 9 | 23 | one bucket per draft for narrative rows |
| Later round | 2 | 18 | after 1872 (Q15) |

## Changes against the plan's first lists

**Fixed list.**
1. Added: Oregon's customs held for Oregon 1862–67 (F11) and the Idaho, Montana and Comstock gold (F12), which the plan applies in phase 4 but did not list. Montana's camps are new: CR-060 M2 and CO2 put them on Pacifica's side.
2. Added: Washington Territory (P01b; 11,594 in 1860), absent from every list in the plan.
3. Questioned: "the Rio Grande valley and Arizona from 1862" (Q1) and "the San Luis Valley's 7,000 from 1863" (Q2).
4. E06 is unchanged: the 500 volunteers are canon, and its $1m stands.
5. E11 must move from 1866–72 in sevenths (current workbook) to 1867–72.

**Lever list.**
1. Added: private lending of 1867 (L13). The Senate declines the Treasury loan and the money is placed privately (CR-062 M3, decided 13 November); its amount is deferred as "requires modeling". The workbook still carries E14, a $10m Treasury loan to the Union.
2. Proposed for fixed instead of free: the head counts (Q3) and the set-offs N-B and N-C (Q4).
3. Added as questions: the Hudson's Bay Company purchase (Q6), the Land Fund and member shares (Q7), Sitka (Q8).

## Questions for the author

| No. | Question | Recommendation |
|---|---|---|
| Q1 | When do New Mexico and Arizona enter the confederal count? The plan and the current workbook (joins of 177,000 in 1862 and 85,000 in 1863) have them from 1862; CR-061's model section says from 1867. | 1867 for every acceding territory, as for Oregon and Deseret: they are held under compact, not members, until the exchange. |
| Q2 | The San Luis Valley's 7,000 from 1863 | Drop the separate line. Its settlements were in Taos County in 1860, so New Mexico's 93,516 already counts them. |
| Q3 | Head counts for Deseret, Washoe, Idaho, western Montana and Alaska: the plan makes them levers. | Fixed inputs with a stated assumption each, tested in phase 6's sensitivity run. "The largest value the model allows" is meaningless for a head count, since more people bring more revenue. The refugee stream (L12) stays a lever, bounded by its sources. |
| Q4 | Set-offs inside the $40m (N-B annuity credit, N-C unratified treaties): the plan makes them a lever that follows the scrip. | Fixed by source: N-C from the 1851 and 1855 treaties' own sums (CR-059 research 30), N-B from what L08 pays. Only the scrip purchase (L06) is free. |
| Q5 | Add the private lending of 1867 (L13) as a lever, replacing E14? | Yes. Its party becomes the Eastern houses and the transit companies. |
| Q6 | The Hudson's Bay and Puget Sound Agricultural companies' rights, bought by the Confederal Treasury in 1861–62 (CR-059 P10): no amount is given. | Fixed at the historical award of 1869, $650,000 ($450,000 and $200,000; to verify). |
| Q7 | The ceded public domain going to the Land Fund, Oregon's customs share and its schools' share (CR-059 V9): none of these is in the plan. | Fixed rule: the new members' public land enters the Land Fund from 1867 under the existing member-state rules. Only the schools' share needs a number. |
| Q8 | The Sitka garrison, squadron and northern mail from 1867 (CR-062): at zero in phase 4, and not in the lever list. | A lever, so the 1867 test sees it. |
| Q9 | Do the rifles and machine tools sold through Matamoros count against the Richmond credit (L01) or as a separate cost? | Against the credit. Only the missions' pay is a cost. CR-068's ledger note already merges C-1863-MATAMOROS into one credit entry. |
| Q10 | Union property taken at valuation (Walla Walla 1862; Port Townsend and Fort Union 1867) and the keep of withdrawing garrisons (Fort Churchill 1864): pay cash or credit against the $40m? | Credit against the $40m, as CR-060's model note suggests for Fort Churchill. |
| Q11 | E20, $1m a year 1871–88 for Richmond's Mississippi tolls: does it stand now that free navigation is the condition of the credit (CR-068 K21)? | Drop E20. If free navigation is a condition of the loan, Pacifica need not also buy the tolls off. This is only a recommendation, since the draft does not say. |
| Q12 | Baja (E13; CR-062 M6, "test separately") | Switch it off in the build and test it as a separate case. |
| Q13 | Washoe's net-proceeds tax (L11): its ceiling is a narrative one, "lighter than the rejected constitution's". | Keep it as a lever with the 1863 rate as its ceiling (research needed). |
| Q14 | The Nauvoo Legion's pay (deferred by you, CR-060 CT7) | Carry it at zero behind a switch. |
| Q15 | The workbook's 18 items after 1872 (the Colorado transfers of 1875–82; canon after 1872): in this round? | No: "Later round". They do not touch the 1859–1872 checks. |

## Contradictions between drafts

| No. | Where | What | Model effect | Recommended reading |
|---|---|---|---|---|
| C1 | CR-068, ledger paragraph and historical-background list | still adds C-1871-RANSOM-ARTICLE and lists "Lincoln's opinion of 1871", both withdrawn with G12 | none | remove both (plan phase 10, step 3) |
| C2 | Workbook E14 against CR-062 M3, S10 and CR-068 G11, O5 | the drafts agree that the loan is declined and lent privately; the workbook has a $10m Treasury loan to the Union; CR-062 open decision 19 still asks "whether it is made" | E14's party and amount | the drafts; Q5 |
| C3 | CR-068 K18 against B4 and PP2 | Astoria falls "early July" (K18); on 4 July it "has not yet fallen" (PP2); the columns land in the third week of July (B4) | none (1861 either way) | B4, which revision 37 follows |
| C4 | CR-063 Part III against CR-063's review note and CR-064 | about 12,500 escape, 16,500 hold and 15,000 surrender about 4 July (Part III); "15,000 out, 8,000 rear garrison" (the review note in CR-063, repeated in CR-064's); CR-064 Part V holds the city "until the turn of June and July" | neighbours.py casualties | Part III's numbers. You deferred this choice on 12 November; it is needed by phase 3 |
| C5 | CR-061 against the plan | New Mexico's count year | population and revenue | Q1 |
| C6 | Workbook E11 against CR-062 | 1866–72 in sevenths against 1867–72 | gold in 1866 and 1867 | the drafts |

## Author's decisions (13 November 2026, 19:46)

"I approve all the recommendations, please make a reasonable assumption for Vicksburg."

| ID | Decision |
|---|---|
| D1 | Q1–Q15 approved as recommended (written into `build_register.py`, DECISIONS; the register has no row left for the author to classify). |
| D2 | Contradictions C1–C3, C5, C6: the recommended readings. |
| D3 | C4, Vicksburg (drafter's assumption at the author's request): CR-063 Part III's numbers, which CR-064 Part V already uses: about 30,000 inside the lines, 12,500 escape on 17–18 May, about 1,500 lost in the assaults and the siege, about 15,000 surrender about 4 July. The "15,000 out, 8,000 rear garrison" note in CR-063 and CR-064 is the one to correct in phase 10. |

After the decisions the register stands at 50 Fixed, 6 Fixed (unchanged), 19 Lever, 21 Memo, 1 Deferred, 5 Not the model's, 9 No model place and 2 Later round.

## Author's decisions (13 November 2026, 22:56): getting through the war years

"I think these suggestions all makes sense, including the one about letting war bonds draw on the idle gold. You can add it as a fourth package in phase 6."

| ID | Decision |
|---|---|
| D4 | Each theatre pays for itself: Oregon's customs account, Washoe's net-proceeds tax, the Sunset road and Paso del Norte customs, the Snake and Fort Bridger road fees, and the Sonora customs (for the Juárez credit) are earmarked to the garrisons, annuities and credits of the same region. The held territories pay the 5% royalty on their gold from 1863, as a fee for assay and coinage (F12; Phase 4 open point 2 closed). |
| D5 | The Richmond credit is drawn in Pacifican goods through Matamoros (as Q9), with small draws in 1862–63 and most in 1864–65. |
| D6 | The Honolulu package is spread: batteries and frigates 1861–62, the second turret ship's cost across 1863–64. |
| D7 | The refugee stream (L12) is used to fill the 1863–65 gap, screened by Victoria's skilled-immigration policy. |
| D8 | 1867 is kept light: option (b) for the $40m (six equal instalments); the 1867 private lending smaller and shorter ($3–5m suggested); set-offs (scrip bought in 1865–66 and credited at face, Union property at valuation, the keep of the garrisons) cover part of the first instalment. |
| D9 | No new gold-heavy works in 1862–66; the Oregon works on Development Fund credit after 1867; the Polytechnic at full pace from 1868. |
| D10 | New model rule (L17): war bonds subscribed in coin may draw on a bounded share of the gold above note cover. The bound is to be sized from the Union's and Britain's war finance. |
| D11 | Phase 6 gets a fourth package, "self-financing" (D4–D10), alongside the plan's three. |

Drafter's correction: F18 (no treasure steamers to New York, 1861–65) is a fixed item that phase 4 did not apply; it goes in at the start of phase 5.

## Author's decisions, 14 Nov 2026 (06:48), on the phase 5 open points

| ID | Point | Decision |
|---|---|---|
| D12 | L17's bound | Approved: 0.12 of notes and bank reserves (Story), 0.06 (Stress), capped by the gold above cover |
| D13 | F18's held gold | Goes east when the steamers return: half in 1866, half in 1867 |
| D14 | Stress ceiling | Stays 17 for the war-years packages |
| D15 | Victoria's frigates | The Navy plan's two steam cruisers of 1861, built for the war; she gets them after the war (no extra ships) |
| D16 | Technical mission pay | $0.1m a year stands |
| D17 | E14 | Private money, as built |

## Checks

| ID | Check | Result |
|---|---|---|
| X1 | every draft item maps to exactly one register row | 687 of 687 |
| X1b | every workbook item maps to exactly one register row | 584 of 584 |
| X2 | every register row has at least one source item (draft or workbook) | 113 of 113 |
| X3 | every lever names its lever and every row its owner | yes |
| X4 | fresh-context review | not run |

## Resume here

1. Done: the author approved Q1–Q15 (D1–D3 above); the sheet "Pacifica — model register, CR-059 to CR-068" records the answers.
2. Done: the 584-item workbook is mapped (`map_events.py`, `events_mapped.csv`).
3. Done: answers written into `build_register.py` and rerun.
4. Done: phase 3 (`phase3-population-change-list.md`, `phase3_by_year.csv`, `phase3-run/`). Paths D's joins move to 1867 (350,036); residents at the end of 1865 fall from 1.90m to 1.60m; from 1867 the difference is under 0.4%.
5. For the author before phase 4: D1 (read DEM-01's 1.9m at the end of 1865 as the people under the Republic's government, members plus held territories, and keep 1.60m as the members' count) and D4 (whether the treaty nations of the new territories count as residents from 1867).
6. Done: phase 4 (`phase4-fixed-only.md`; `finance/build/cr059_068_civil_war.py`). The fixed items alone hold: Story 0 failing checks, Stress the same 17. The war years borrow more (debt peaks at $31.6m in 1864), 1867 borrows $4.7m, and the binding check is the Stress private-saving margin: $4.1m in 1863, $8.2m in 1867. D1 and D4 taken as recommended. E20 kept (Q11 withdrawn: canon §13 has Pacifica replace the toll revenue).
7. Done: phase 5 (`phase5-levers-headroom.md`; `finance/build/cr059_068_levers.py`; `phase5_lever_test.py`; `phase5_headroom.py`; `phase5/`). F18 applied, with the held gold going east in 1866-67; 36 named levers (`cw_*`, Levers rows 408-446) at the story minimum, all of which move the model; E09 the Richmond credit as a loan; E11 split with set-offs; E14 private lending ($3m); L17 on at 0.12 / 0.06 of notes and bank reserves. Story 0, Stress 17 (the same 17 as phase 4). Room in Stress: $11.2m (1862), $6.0m (1863), $9.0m (1864), $14.4m (1867); private saving binds.
8. Done: the author's answers of 14 Nov (D12-D17): L17 bound approved; the held gold goes east in 1866-67; Stress ceiling 17; Victoria's frigates are the Navy plan's two 1861 steam cruisers, handed over after the war; mission pay $0.1m/yr; E14 private. L15 approved, not built.
9. Done: phase 6 (`phase6-ranges-packages.md`; `phase6_*.py`; `phase6/`). Single ceilings for 19 spending levers (all bound by Stress private saving in their own war year, except long-lived ones bound by Stress 1932 and the Oregon works by Story 1920); prices per $1m; instalment split (all three pass, (b) leaves most room); refugees (no finance ceiling to 50,000/yr; route ceiling about 33,000/yr); four packages under a strict rule (no new Stress year-check up to 1900, since the scrip's 1932 cure was otherwise spent on war-year failures), all passing in clean rebuilds; sensitivity (packages keep 73-81% with dearer garrisons; B only 36% with less interior gold; the 1867 joins have a 4% margin before Stress breaks in 1932; corrected: 1914-24 were already among the 17).
10. Done: the author's fix (14 Nov): lever cw_alaska_rcpt (E217, seal lease $0.3175m/yr, 1868-1900) added to `finance/build/cr059_068_levers.py`; `phase6_sitka_fix.py`; `phase6_robust.py heads` takes HEADS_OVERRIDES. Lease + 20,000 refugees/yr: 1932 Stress margin +3.9 -> +18.0, Sitka ceiling 0.89 -> 4.20, joins tolerance 4% -> 21%. Not yet adopted into the packages.
11. Done: D strengthened (author takes D, 14 Nov): `phase6_d_plus.py` (lease, refugees, later levers raised growth first), `phase6_d_strong.py`, `phase6_d_garrison_safe.py`; D strong at 73.4% (20k) or 72.7% (33k) of the new maximum passes clean rebuilds (Story 0, Stress 16), survives garrisons x1.25 and joins x0.75; Sitka $5.7-6.3m/yr, Oregon works $87m, war-year items about a quarter below D. Results `phase6/d_plus.json`, `d_strong_*.json`, `d_strong/`.
12. Author (14 Nov): D strong, 20,000 refugees a year, trade accepted. Challenge answered with `phase6_d_margin_walk.py`: the $25m lower 1932 margin is Sitka (-$43m; about -$9m per $1m a year, 1867-1900), offset by the Oregon works (+$18m); the war-year cuts do nothing for 1932. Open: the model gives Alaska no return beyond the seal lease.
13. Alaskamaxx (author, 14 Nov: taper and Alaska receipts approved; investigate how Pacifica makes Alaska pay sooner): taper built (cw_sitka_taper, E218 1880-1900; E195 now 1867-79; `levers3.xlsx`): 50% -> 1932 margin +38.2 (from +32.1), 30% -> +40.6. Investigation `alaska-maxx.md` (ideas A-J, MODEL receipts, workbook plan, canon tensions §14 and CR-058). Awaiting the author's choices before the receipts levers.
14. Author's answers (14 Nov): A-J all in incl. the Bering telegraph; finder's share negotiated on top of the state's 5%; taper 1873 at 40%; §14 amended. Built (levers rows 408-457, events to E231; `levers4.xlsx`); `phase6_alaska_walk.py`: D strong + Alaska, 1932 Stress margin +48.7 (D strong +32.1; taper +12.8, seals +4.0, salmon +3.1, gold +0.9, commission and telegraph -4.3, route +0.1); Stress 16, strict rule, garrisons x1.25 pass; clean rebuild `phase6/d_strong_alaska/`. CR-070 (Alaska) to draft.
15. CR-070 drafted (`book-agent/revision/CR-070.md`, project `claude/CR-070.md`): decisions A-F, storyline text for §14 and §25, model table and walk, CT1-CT4, four fact changes (preview clean, lint clean). Self-review only; fresh-context review pending. Not committed.
16. CR-070 revised (telegraph OPEN pending research; its fact change withdrawn) and pushed to revision/cr069-gold (dff087e, author's request).
17. Phase 7: `phase7-decision-sheet.md` (project `claude/phase7-decision-sheet.md`). New finding: the northern mail at the solver's $2.85m/yr; at $0.3m (recommended, Q1) D final has 1932 Stress margin +79.5, Stress 15, 1932 passing every check, garrisons x1.25 pass (+70.8), clean rebuild `phase7/d_final/`. Questions Q1-Q8 for the author.
18. Author (14 Nov, evening): Q1-Q8 all approved.
19. Phase 8 done:
    - L15 built: sheet Members' land; levers cw_l15_on, cw_l15_mt_share 0.25, cw_l15_or_school 1/18; census farm land from the 1945 Census of Agriculture, Table 18; Budget G. $105m net to the Treasury 1867-1932, Oregon's schools $1.25m.
    - D final written into finance/Pacifica_financial_model_1846-1932.xlsx (SHA c5ebb7bb...; values finance/build/cr059_068_values.json; rates finance/build/paths_c_rates_cr059_068_final.csv, two rounds to the fixed point).
    - Results: Story 0 failed checks, Stress 15; 1932 Stress margin +92.4 (garrisons x1.25 +85.9); residents at the end of 1932 38.44m.
    - Population outputs regenerated, tests pass.
    - finance/CR-059-068-workbook.md, finance/README.md and AGENTS.md entries written.
    - Storyline MODEL figures to update at integration: 37m -> 38m (x3), 5.7/4.9m -> 6.1/5.0m.
    - Not committed.
20. Next: commit on models/cr059-068-civil-war when the author asks; phases 9-10 per the plan; fresh-context reviews of CR-069 and CR-070 still pending., the decision sheet. For the author: which package or values (recommended 70-75% of a package's maximum), whether the 1932 Stress check should govern long-lived costs, firming up the uncensused head counts, the refugee level, the regional receipts.

21. Done (15 Nov, author: "Please rebuild the model next", after CR-070's three reviews): `cr059_068_levers.py` and `cr059_068_values.json` changed for CR-070 as decided (Alaska line in place of the Bering entry, E232-E238, the Commission to 1932, the Sitka rent, the railway in 1897-99, the copper path in Resources F and its railway). Rebuilt from the base (cba70b31) through step 4; the unchanged builders first reproduced the 14 Nov results exactly. Story 0, Stress 15 (same years), 1932 Stress margin +91.68 (from +92.43); residents 38.443m. Workbook SHA 9ac9d556...; population outputs regenerated, tests pass; Paths C not re-iterated; garrisons x1.25 not rerun. Addendum in finance/CR-059-068-workbook.md.

22. Done (15 Nov): phases 9 and 10. Phase 9: fresh-context review of the model work (`/home/claude/reviews/phase9-brief.md`; report summarized in `finance/CR-059-068-workbook.md`, "Fresh-context review"): rebuild reproduces the workbook exactly; no blocker; the binding 1932 Stress check is the gold cover, not private saving. Phase 10: the drafts' model sections (CR-059 to CR-064), CR-062 M2/M3/M5, CR-068's withdrawn ledger items and stale workbook notes, the Vicksburg notes (CR-063, CR-064), CR-069 P2/P6, CR-070's model section, the integration checklist (on revision/cr069-gold).
23. Done (15 Nov, author: "I approve all 6 suggestions"): second rebuild (note, second addendum): L15 at the Land Fund's price (cw_l15_value_rel 0.5); E10 $0.5m; E19 beside the war credit; the Sacramento line $8m in 1863-66, back-loaded (E240-E243); Canada's seal share from 1886 (E219, E239); Oregon's customs share from 1867 (Budget V). Paths C re-iterated (two rounds). Story 0, Stress 15 (same years); 1932 Stress gold cover +$10.0m, private saving +$110.0m; residents 38.71m. Garrisons x1.25: Stress 17, new failures 1863-64 (the line uses the war years' room). SHA eb642aa7....
