"""Phase 5 of the CR-059-068 model plan: the Civil War levers, F18 and the idle-gold rule.

    python3 finance/build/cr059_068_levers.py IN.xlsx OUT.xlsx

IN is the phase 4 workbook (finance/build/cr059_068_civil_war.py's output, SHA-256 13a922c8...).
The script never recalculates; run LibreOffice (xlsx skill scripts/recalc.py) afterwards.

Every free item of the register gets a named lever on the Levers sheet (rows 408 on, names
cw_*), with the Story and Stress values equal at the story minimum: the value the drafts or
canon already fix, or zero where no figure exists. Phase 6 sets the packages.

  F18    No treasure steamers to New York 1861-65 (fixed): the New York-bound share of new gold
         (cw_ny_share, 0.85, the Custom House statement for the first quarter of 1860) is
         either kept at home (cw_ny_home) or sent direct to London. Resources R, 1861-65.
  F18b   The gold held back goes east when the steamers return: half in 1866, half in 1867
         (cw_ny_return, author 14 Nov), counted in Gold & money E.
  L17    War bonds subscribed in coin from the gold above note cover, 1861-65: a new private
         source on Sources & uses (column R) and in the bond-market check (Checks L). The share
         cw_idle_ratio (a share of notes and bank reserves, capped by the gold above cover)
         Story 0.12, Stress 0.06 (approved by the author, 14 Nov).
  L01    E09 becomes the Richmond credit, a Continental loan drawn in goods through Matamoros:
         $0.3m a year in 1862-63 and $0.9m in 1864-65 (the $2.4m floor, D5); the technical
         mission's pay is its own cost row (E199).
  L02    Honolulu: batteries 1861-62 (E203), frigates beyond the Navy plan (Navy plan C22),
         the second turret ship's sections and slip 1863-64 (E204). All 0.
  L03    E07 and E08 at their canon values through levers; 1865-67 garrisons above the head
         counts (E200) at 0.
  L04    E195-E196 Sitka through levers, 0.
  L05    E11 split into the 1867 instalment and 1868-72 (E197); option (b), D8.
  L06-07, F13-F14  Set-offs against the 1867 instalment (cw_setoffs, computed on Levers):
         scrip bought in 1865-66 (E205) at face, the Northwest annuities paid 1862-66 (N-B),
         the unratified-treaty debts (N-C, paid on to the nations, E206), the keep of the
         withdrawing garrisons (E201-E202); Union property at valuation is added to it (F13).
  L08    Annuities by region (E207-E209), and the regional receipts D4 earmarks to them
         (E210-E213, Washoe's net-proceeds tax is L11). All 0.
  L09    Juarez credit on the Sonora customs (E214, Continental loan), 0.
  L10    Oregon works on Development Fund credit from 1868 (E215, Investment), 0.
  L12    Refugees, deserters and draft evaders added to Paths E in 1863-65, 0.
  L13    E14 becomes private lending ($3m, D8): new category "Private lending", counted in
         gold paid out (Gold & money E) and in private uses (Sources & uses K), not in public cash.
  L16    The Nauvoo Legion paid in 1865 only for the Bannack deployment of 1864 (E216; author, 15 Nov).
Not done here: L15 (the Land Fund's intake of the ceded public domain), approved for a later step.
"""
from __future__ import annotations

import argparse
import copy
from pathlib import Path

import openpyxl
from openpyxl.comments import Comment
from openpyxl.workbook.defined_name import DefinedName

AUTH = "CR-059-068 phase 5, 13 Nov 2026"
FIRST, LAST = 1846, 1932
LEVER_ROW0 = 408
SU0 = 135          # Sources & uses private table: first year row
G0 = 6             # Gold & money, Checks, Resources, Paths, Navy plan: first year row

# name, label, story, stress, unit, status, note
LEVERS = [
    ("cw_ny_share", "F18: share of Pacific treasure sent to New York before the war", 0.85, 0.85, "share",
     "Fixed (CR-068 G8)", "Custom House statement, first quarter of 1860: $8.66m of about $10.2m of treasure "
     "exported went to New York. In 1861-65 none goes there (F18)."),
    ("cw_ny_home", "F18: share of the New York-bound gold kept at home, 1861-65", 0.5, 0.25, "share",
     "Model estimate", "The rest goes direct to London on the British steamers, as more of it did historically "
     "from 1863. Raises monetary gold (Gold & money), not the Treasury's cash."),
    ("cw_ny_return", "F18: share of the gold held back in 1861-65 that goes east when the steamers return, 1866-67",
     1, 1, "share", "Author (14 Nov)", "Half in 1866, half in 1867 (Gold & money E). Two Houses (CR-068 G6b): at "
     "peace 'the coast's gold goes to New York again'."),
    ("cw_idle_ratio", "L17: coin war bonds may draw each year 1861-65, / notes and bank reserves", 0.12, 0.06, "share",
     "Author (14 Nov)",
     "Bound approved by the author, 14 Nov 2026. In Aug-Sept 1861 the New York "
     "banks' specie fell from $48m to $37m (23%) in six weeks of coin loans to the Treasury, most of it paid back "
     "out at home; their specie was 50% of deposits and notes, so the net drain was about 12% of them. A run of "
     "one-third in three weeks (Dec 1861) then forced suspension: Stress keeps half. Never more than the gold "
     "above cover (Gold & money K)."),
    ("cw_rich_early", "L01: Richmond credit drawn per year, 1862-63", 0.3, 0.3, "$m/yr", "Lever (floor)",
     "Drawn in Pacifican goods through Matamoros (D5). Floor: the $2.4m once in E09, $0.6m in 1862-63 and "
     "$1.8m in 1864-65. Continental terms: 5% coupon, 4% repaid a year."),
    ("cw_rich_late", "L01: Richmond credit drawn per year, 1864-65", 0.9, 0.9, "$m/yr", "Lever (floor)",
     "Most of the credit in the last two years (D5). No new advances after the armistice."),
    ("cw_mission", "L01: eastern technical mission, pay and passage per year, 1862-65", 0.1, 0.1, "$m/yr",
     "Model estimate (author, 14 Nov)", "Was inside E09 with the credit; stays a cost. A few dozen engineers and officers."),
    ("cw_war61", "L03: Northwestern campaign above the head counts, 1861", 6, 6, "$m", "Canon (§10)",
     "E07: sea transport and occupation. Head counts are in Budget N (Paths W)."),
    ("cw_occ6264", "L03: occupation, columns and garrisons above the head counts, per year 1862-64", 5, 5,
     "$m/yr", "Canon (§10-11)", "E08: coin purchases, chartered steamers, cost per man above the head counts."),
    ("cw_occ6567", "L03: garrisons of the held territories above the head counts, per year 1865-67", 0, 0,
     "$m/yr", "Lever (start 0)", "E200: the departments (CR-067 B7) until the exchange of 1867."),
    ("cw_hon_batt", "L02: Honolulu batteries, per year 1861-62", 0, 0, "$m/yr", "Lever (start 0)",
     "Victoria's price of July 1861 (CR-068 TL6), spread 1861-62 (D6)."),
    ("cw_hon_frig", "L02: frigates for Honolulu beyond the Navy plan (ships completed 1862)", 0, 0, "ships",
     "Author (14 Nov): 0", "Victoria's frigates are the Navy plan's two steam cruisers of 1861, built for the war; "
     "she gets them after the war. Their running costs stay in the Navy sheet."),
    ("cw_hon_turret", "L02: second turret ship, sections shipped and slip at Honolulu, per year 1863-64", 0, 0,
     "$m/yr", "Lever (start 0)", "The ship itself is the Navy plan's 1863 turret ship (D6)."),
    ("cw_sitka_gar", "L04: Sitka garrison and squadron, per year from 1867", 0, 0, "$m/yr", "Lever (start 0)",
     "E195. No figure in the drafts."),
    ("cw_sitka_taper", "L04: share of the Sitka garrison and squadron kept 1873-1900 (1 = no taper)", 1, 1, "share",
     "Lever (no taper)", "E218 (author, 14 Nov: taper from 1873, 40%). The garrison runs at cw_sitka_gar in 1867-72 "
     "(E195) and at this share of it in 1873-1900: settler soldiers on the Hokkaido model take land, fishing and claims. Historically the Union's army left Sitka on 15 June 1877 and the navy "
     "kept a station there."),
    ("cw_sitka_mail", "L04: northern mail to Sitka, per year from 1867", 0, 0, "$m/yr", "Lever (start 0)",
     "E196. No figure in the drafts."),
    ("cw_alaska_rcpt", "L04: the seal islands' lease and Alaska's customs, per year 1868-79", 0, 0, "$m/yr",
     "Lever (start 0)", "E217. Historically the Alaska Commercial Company of San Francisco paid $55,000 rent and "
     "$2.625 a skin on 100,000 skins, $317,500 a year, from 1870 (House Report 623, 1876). Here the Republic leases "
     "the islands in 1868 (author, 14 Nov: Sitka pays for itself early)."),
    ("cw_seal_1880s", "L04: Pribilof receipts per year 1880-89 (tendered lease, herd saved)", 0, 0, "$m/yr",
     "Lever (start 0)", "E219. Alaskamaxx E (author, 14 Nov). MODEL 0.5: re-tendered per skin on 100,000 skins, net of "
     "Canada's 15% from the convention of 1886 (CR-070 D2): 1880-85 at this value / 0.85 (E219), 1886-89 at it (E239)."),
    ("cw_seal_1890s", "L04: Pribilof receipts per year 1890-1900", 0, 0, "$m/yr", "Lever (start 0)",
     "E220. MODEL 0.85: the 1890 bid ($60,000 rent and $9.625 a skin, Hist.) on a herd still giving 100,000 skins, "
     "less Canada's 15%."),
    ("cw_seal_after", "L04: Pribilof receipts per year 1901-32", 0, 0, "$m/yr", "Lever (start 0)",
     "E221. MODEL 0.85, flat in nominal dollars (conservative: pelts rose from under $5 to about $40 by 1900, Hist.)."),
    ("cw_ak_salmon", "L04: Alaska salmon case tax, scale of the MODEL path (0 = none)", 0, 0, "scale",
     "Lever (start 0)", "E222-E225. Path at 1: $0.05m/yr 1870-79, 0.15 1880-89, 0.3 1890-1900, 0.6 1901-32 (about 4% "
     "of the pack's value, canneries a decade early; Alaskamaxx F)."),
    ("cw_ak_gold_lead", "L04: years by which the Juneau belt comes early (finder's compact)", 0, 0, "years",
     "Lever (start 0)", "Resources E, 1867-98: the Alaska gold path of years y+lead (capped at 1898's value); the "
     "historical path is kept in Resources T. Alaskamaxx C (author: 8 years). The finder's share is negotiated on top "
     "of the state's 5% and paid by the mine, so the royalty is unchanged."),
    ("cw_ak_seward", "L04: Seward Peninsula placers from the telegraph survey's notes, $m/yr 1876-98", 0, 0, "$m/yr",
     "Lever (start 0)", "Added to Resources E 1876-98 (from 1899 the historical path holds Nome). Alaskamaxx D, MODEL 1.0."),
    ("cw_ak_telegraph", "L04: the Alaska line through British Columbia (1 = built)", 0, 0, "switch", "Lever (off)",
     "CR-070 E2-E3, E7 (author, 15 Nov: the Bering telegraph is a road not taken). E226: Western Union's British "
     "Columbia line bought, the gap built to the Stikine and the Wrangell-Sitka cable, $0.4m/yr 1868-70; E227: an "
     "operating loss of $0.05m/yr 1871-97; E232-E233: the Sitka-Juneau cable ($0.15m/yr 1872-73) and the Lynn Canal "
     "line ($0.2m, 1884). MODEL."),
    ("cw_ak_commission", "L04: Northern Commission and survey, $m/yr 1867-1932", 0, 0, "$m/yr", "Lever (start 0)",
     "E228. Alaskamaxx A-B, MODEL 0.15: the assay office, claims courts, land office and survey. CR-070 G2: the "
     "Commission continues after 1885; carried to 1932 until the counties' CR settles Alaska's standing."),
    ("cw_ak_route", "L04: the Chilkoot compact and an early Yukon route (1 = on)", 0, 0, "switch", "Lever (off)",
     "E229-E231: road and tramway with the clans $0.1m/yr 1884-86; E61's railway, assay and bank moved to 1897-99 "
     "(CR-070 F3, after the news); the public share of route, assay and bank income $0.3m/yr 1897-1910. MODEL."),
    ("cw_l15_on", "L15: the new members' public land in the Land Fund from 1867 (1 = on)", 1, 1, "switch",
     "Approved (author, 13 Nov: Q7)", "Sheet Members' land; its net to the Treasury goes into Budget G beside the Land "
     "Fund's. Sold on the Land Fund's instalments, default and survey cost, at the Land Fund's price (cw_l15_value_rel). The nations are paid "
     "by the regional annuities (L08), so no purchase cost is counted here."),
    ("cw_l15_mt_share", "L15: western Montana's share of Montana's farm land", 0.25, 0.25, "share", "Model estimate",
     "The 1867 population was nearly all west of the line; the later ranch land was mostly on the plains (MODEL)."),
    ("cw_col_school", "CR-059 Part IX: Columbia's schools' share of the margin on Columbia's land", 1 / 18, 1 / 18,
     "share", "Approved (author, 15 Nov)", "On Oregon's terms (Members' land). Columbia is Washington Territory "
     "from the exchange of 1867."),
    ("cw_col_nontreaty", "CR-059 Part IX: share of Columbia's farm land in the country of nations without a treaty",
     0.15, 0.15, "share", "Story assumption (author, 15 Nov)", "The Chehalis, Cowlitz, Lower Chinook and their "
     "neighbours, whose council of 1855 made no treaty: their land enters the Land Fund only by purchase, at "
     "lfund_price an acre paid as annuities over lfund_term years (Members' land). A story assumption: the lower "
     "Columbia and the Chehalis and Cowlitz valleys hold about a seventh of Columbia's farm land by the census."),
    ("cw_l15_or_school", "L15: Oregon's schools' share of the margin on Oregon's land", 1 / 18, 1 / 18, "share",
     "Approved (author, 14 Nov: Q7)", "One-eighteenth, the proportion of the Union's grant of sections 16 and 36 of "
     "every township to Oregon's schools (1859; Hist.; to verify). CR-059 CT13, open 44."),
    ("cw_inst_opt", "L05: split of the $40m (1 = $8m + 5 x $6.4m; 2 = six of $6.67m; 3 = $10m + 5 x $6m)", 2, 2,
     "option", "Author (D8)", "Option (b) keeps 1867 light."),
    ("cw_scrip_face", "L06: Oregon war scrip bought in 1865-66, face value", 0, 0, "$m", "Lever (start 0)",
     "Ceiling about $3.2m: the $6.0m claimed less the $2.8m the Union appropriated. Credited at face against "
     "the 1867 instalment."),
    ("cw_scrip_price", "L06: price paid for the scrip / face", 0.6, 0.6, "share", "Model estimate",
     "The scrip traded well below face while the Union's payment was in doubt."),
    ("cw_setoff_nc", "L07 (N-C): the Union's debts under the unratified treaties, deducted in 1867", 0, 0, "$m",
     "Fixed, amount unknown", "Paid on to the nations as purchase money (E206), so it saves gold, not cash."),
    ("cw_nb_credit", "L07 (N-B): Northwest annuities paid 1862-66 credited against the price (1 = in full)", 1, 1,
     "switch", "Fixed", "Uses L08a's yearly amount for the five years 1862-66."),
    ("cw_union_prop", "F13: Union public property taken at valuation, paid with the 1867 instalment", 0, 0, "$m",
     "Fixed, amount unknown", "Fort Walla Walla's stores (1862); Port Townsend and Fort Union property (1867)."),
    ("cw_keep64", "F14: keep of the withdrawing Union garrisons, 1864 (Fort Churchill)", 0, 0, "$m",
     "Fixed, amount unknown", "Paid by Pacifica (E201), claimed back against the 1867 instalment (D8)."),
    ("cw_keep67", "F14: keep of the withdrawing Union garrisons, 1867 (Fort Union)", 0, 0, "$m",
     "Fixed, amount unknown", "Paid by Pacifica (E202), claimed back against the 1867 instalment (D8)."),
    ("cw_ann_nw", "L08a: annuities, the Northwest, per year 1862-81", 0, 0, "$m/yr", "Lever (start 0)",
     "The Union's ratified treaties assumed 'at least in full', Klamath 1864, Paiute 1865-66. Earmarked: Oregon's "
     "customs account (D4)."),
    ("cw_ann_gb", "L08b: annuities, the Great Basin and the Rockies, per year 1863-82", 0, 0, "$m/yr",
     "Lever (start 0)", "Box Elder, Soda Springs, Washakie, Spanish Fork, Owyhee, the Ute agreement. Earmarked: "
     "Washoe's tax and the Snake and Fort Bridger road fees (D4)."),
    ("cw_ann_sw", "L08c: annuities, the Southwest, per year 1862-81", 0, 0, "$m/yr", "Lever (start 0)",
     "Navajo, Apache, Moache, Capote, Jicarilla; scouts in coin. Earmarked: the Sunset road and Paso del Norte "
     "customs (D4)."),
    ("cw_rc_or", "D4: Oregon's customs account while held, per year 1861-66", 0, 0, "$m/yr", "Lever (start 0)",
     "From 1867 Oregon's people are residents and its customs are in Budget B."),
    ("cw_washoe", "L11: Washoe net-proceeds tax, per year 1864-72", 0, 0, "$m/yr", "Lever (start 0)",
     "Rate OPEN; must be lighter than the rejected 1863 constitution's."),
    ("cw_rc_sw", "D4: Sunset road and Paso del Norte customs, per year 1862-72", 0, 0, "$m/yr", "Lever (start 0)",
     ""),
    ("cw_rc_gb", "D4: Snake and Fort Bridger road fees, per year 1863-72", 0, 0, "$m/yr", "Lever (start 0)", ""),
    ("cw_juarez", "L09: Juarez credit on the Sonora customs, per year 1865-66", 0, 0, "$m/yr", "Lever (start 0)",
     "Rifles delivered at Paso del Norte from Aug 1865 (goods, not gold). Continental terms."),
    ("cw_or_works", "L10: Oregon works on Development Fund credit, per year 1868-75", 0, 0, "$m/yr",
     "Lever (start 0)", "Willamette Falls and Cascades locks, the Columbia bar, the railway north (D9)."),
    ("cw_refugees", "L12: refugees, deserters and draft evaders arriving per year, 1863-65", 0, 0, "persons/yr",
     "Lever (start 0)", "Added to Paths E (D7). The population model (pools.toml) is not changed here."),
    ("cw_priv1867", "L13: private lending to the Union's bankers and the transit companies, 1867", 3, 3, "$m",
     "Author (D8: $3-5m; private, 14 Nov)", "Private, not the Treasury's: it uses private saving and gold, not public cash."),
    ("cw_legion_on", "L16: the Nauvoo Legion paid by the Confederation for a decisive deployment (1 = yes)", 0, 0,
     "switch", "Author (15 Nov): paid only for a decisive deployment",
     "CR-060 D7, CT7: Pacifica pays the Legion only where its deployment, at a decisive moment, wins something Pacifica "
     "would not otherwise have had. The deployment is CR-060 M11 (PROPOSED): Lot Smith's cavalry at Bannack, summer 1864."),
    ("cw_legion_pay", "L16: the Legion's pay for the Bannack deployment of 1864, paid in 1865", 0.1, 0.1, "$m", "Model estimate",
     "About 300 mounted men for a season, in gold, with horses and forage (MODEL). Road duty is the Compact's common "
     "defence and is not paid."),
    ("cw_ak_cable88", "CR-070 E4: the Puget Sound-Sitka sea cable, total cost 1887-88", 0, 0, "$m", "Lever (start 0)",
     "E234, half in each year. MODEL 1.5 (the Army's 1903 appropriation for Sitka-Seattle and Juneau-Sitka was "
     "$485,000 with cheap rubber cable, Hist.; conservative). Ordered by Elias's cabinet in 1886 after Port Hamilton."),
    ("cw_ak_bc_sale", "CR-070 E5: the British Columbia line sold to Canada, 1897", 0, 0, "$m", "Lever (start 0)",
     "E235, a receipt. MODEL 0.25: Ottawa's own estimates of 1897-98 were $150,000-340,000 to build (Hist.)."),
    ("cw_ak_aleutian", "CR-070 E4: the Aleutian cable, Sitka to Hakodate, total cost 1900-03", 0, 0, "$m",
     "Lever (start 0)", "E236, a quarter in each year. MODEL 4.5 (range 4-5), about 3,300 nautical miles at the rate of "
     "the British Pacific cable of 1902 (to verify). Its stations' upkeep is not costed."),
    ("cw_ak_copper", "CR-070 B4, G5: the Chitina's copper under Nicolai's compact, scale of the MODEL path", 0, 0,
     "scale", "Lever (start 0)", "Added to Resources F in 1900-28. Path at 1: $2m in 1900, $5m a year in 1901-02, $9m "
     "a year in 1903-20, $3m a year in 1921-28, about $198m in all: Kennecott's output of 1909-38 (about $200m, to "
     "verify by year) read about ten years early at a flat value. Not in the baseline's column F. The state takes its "
     "5%; the finder's share and the lease are paid by the mine."),
    ("cw_ak_copper_rail", "CR-070 B4, G5: the Copper River railway on Development Fund credit, total 1897-1900", 0, 0,
     "$m", "Lever (start 0)", "E238, a quarter in each year. MODEL 25 (historically $23-25m, built 1907-11, Hist.)."),
    ("cw_l15_value_rel", "L15: the new members' farm value per acre / California's (Land Fund T)", 0.5, 0.5, "share",
     "Story assumption (author, 15 Nov)", "Members' land prices its land as the Land Fund does: "
     "MAX(lfund_floor, lfund_share x value per acre), with the value per acre at this share of California's. MODEL 0.5: "
     "a story assumption (author, 15 Nov 2026): the new members' land is worth about half California's."),
    ("cw_peon_comp", "F10: peonage and captive compensation, 1866 (E10)", 0.5, 0.5, "$m", "Author (15 Nov)",
     "CR-061 A2: a quarter of registered face, cap $100 a peon; $50 a released captive; under $0.5m. The Navajo and "
     "Apache treaties' costs are in the Southwest's annuities (E209) from 1862, so E10 carries the compensation only."),
    ("cw_or_rail_south", "CR-059 W9: the Sacramento line to the Siskiyous, total 1863-66", 8, 8, "$m",
     "Model estimate (author, 15 Nov: built from 1865)", "E240-E242, Development Fund credit: 25%, 37.5% and 37.5% in 1865-67; the line reaches the Siskiyous in 1867 (author, 15 Nov: started later, so that the war years keep their room). MODEL 8: about "
     "200 miles up the Sacramento valley and into the Shasta country at about $40,000 a mile (to verify against the "
     "California and Oregon Railroad's costs of 1870-72)."),
    ("cw_or_cust_share", "CR-059 V9: Oregon's customs share from 1867, / the customs its residents pay", 0.25, 0.25,
     "share", "Story assumption (author, 15 Nov)", "The Charter's 'defined customs share': a quarter of "
     "the confederal customs attributable to Oregon's residents, paid to the State (Budget V, subsidies). CR-059 "
     "open decision 21, settled as a story assumption."),
    ("cw_or_cust_base", "CR-059 V9: Oregon's residents / the confederation's, held at the exchange of 1867", 0.0346,
     0.0346, "share", "Model estimate", "77,096 of about 2.23m residents at the end of 1867 (joins_cr059_068.toml; "
     "People L). Held flat: Oregon grows more slowly than California and Hawaii."),
]

SETOFFS = "cw_scrip_face+cw_nb_credit*cw_ann_nw*5+cw_setoff_nc+cw_keep64+cw_keep67"
FIRST_SHARE = "CHOOSE(cw_inst_opt,0.2,1/6,0.25)"

# id, start, end, description, category, loan group, party, H, gold, status, canon, note
NEW_EVENTS = [
    ("E197", 1868, 1872, "Western cession: instalments 1868-72", "Purchase", None, "Union",
     f"=union_vendor*(1-{FIRST_SHARE})/5", "Yes", "Proposed", "§12", "L05, the rest of the $40m (CR-062 M2)."),
    ("E198", 1864, 1865, "Richmond war credit, drawn in goods through Matamoros (1864-65)", "Loan", "Continental",
     "Confederacy", "=cw_rich_late", "No", "Canon", "§11", "L01; most of the credit in 1864-65 (D5)."),
    ("E199", 1862, 1865, "Eastern technical mission: pay and passage", "Subsidy & guarantee", None, "Confederacy",
     "=cw_mission", "No", "Canon", "§11", "L01; the part of the old E09 that is a cost."),
    ("E200", 1865, 1867, "Garrisons of the held territories above the head counts", "War & operations", None, None,
     "=cw_occ6567", "No", "Proposed", "§10-12", "L03 (CR-067 B7)."),
    ("E201", 1864, 1864, "Keep of the withdrawing Union garrison of Fort Churchill", "War & operations", None,
     "Union", "=cw_keep64", "No", "Proposed", "CR-060 C5", "F14; set off against the 1867 instalment."),
    ("E202", 1867, 1867, "Keep of the withdrawing Union garrison of Fort Union", "War & operations", None, "Union",
     "=cw_keep67", "No", "Proposed", "CR-061 P2", "F14; set off against the 1867 instalment."),
    ("E203", 1861, 1862, "Honolulu batteries (Victoria's price of 1861)", "War & operations", None, "Hawaii",
     "=cw_hon_batt", "No", "Proposed", "CR-068 TL6", "L02 (D6)."),
    ("E204", 1863, 1864, "Second turret ship: sections shipped and slip at Honolulu", "War & operations", None,
     "Hawaii", "=cw_hon_turret", "No", "Proposed", "CR-068 TL6", "L02 (D6)."),
    ("E205", 1865, 1866, "Oregon war scrip bought from its holders", "Purchase", None, "Oregon holders",
     "=cw_scrip_face*cw_scrip_price/2", "No", "Proposed", "CR-059 P11", "L06; credited at face in 1867."),
    ("E206", 1867, 1867, "Unratified-treaty debts paid to the nations as purchase money (N-C)", "Purchase", None,
     None, "=cw_setoff_nc", "No", "Proposed", "CR-059 N-C", "L07; the same sum is deducted from the 1867 instalment."),
    ("E207", 1862, 1881, "Annuities: the Northwest", "Subsidy & guarantee", None, None, "=cw_ann_nw", "No",
     "Proposed", "CR-059 N-B", "L08a."),
    ("E208", 1863, 1882, "Annuities: the Great Basin and the Rockies", "Subsidy & guarantee", None, None,
     "=cw_ann_gb", "No", "Proposed", "CR-060 N1", "L08b."),
    ("E209", 1862, 1881, "Annuities: the Southwest", "Subsidy & guarantee", None, None, "=cw_ann_sw", "No",
     "Proposed", "CR-061 N4", "L08c."),
    ("E210", 1861, 1866, "Oregon customs account while held", "Receipt", None, None, "=cw_rc_or", "No", "Proposed",
     "CR-059 V9", "D4."),
    ("E211", 1864, 1872, "Washoe net-proceeds mining tax", "Receipt", None, None, "=cw_washoe", "No", "Proposed",
     "CR-060 C8", "L11."),
    ("E212", 1862, 1872, "Sunset road and Paso del Norte customs", "Receipt", None, None, "=cw_rc_sw", "No",
     "Proposed", "CR-061", "D4."),
    ("E213", 1863, 1872, "Snake and Fort Bridger road fees", "Receipt", None, None, "=cw_rc_gb", "No", "Proposed",
     "CR-060", "D4."),
    ("E214", 1865, 1866, "Juarez credit on the Sonora customs", "Loan", "Continental", "Mexico", "=cw_juarez",
     "No", "Proposed", "CR-061 M1", "L09; rifles delivered at Paso del Norte."),
    ("E215", 1868, 1875, "Oregon works and the railway north (Development Fund credit)", "Investment", None, None,
     "=cw_or_works", "No", "Proposed", "CR-059 V9", "L10 (D9)."),
    ("E216", 1865, 1865, "The Nauvoo Legion's cavalry at Bannack in 1864, paid after the peace", "War & operations", None,
     "Deseret", "=cw_legion_on*cw_legion_pay", "No", "Proposed", "CR-060 D7, M11", "L16 (author, 15 Nov): Young's own decision in 1864; paid in 1865."),
    ("E217", 1868, 1879, "Seal islands lease and Alaska customs", "Receipt", None, "Alaska Commercial Company",
     "=cw_alaska_rcpt", "No", "Proposed", "CR-062", "L04; Sitka pays for itself (author, 14 Nov)."),
    ("E218", 1873, 1900, "Sitka garrison and squadron (1873-1900, tapered)", "War & operations", None, None,
     "=cw_sitka_gar*cw_sitka_taper", "No", "Proposed", "CR-062", "L04; the taper (author, 14 Nov)."),
    ("E219", 1880, 1885, "Pribilof receipts, tendered lease", "Receipt", None, None, "=cw_seal_1880s/0.85", "No",
     "Proposed", "Alaskamaxx E", "L04 (author, 14 Nov); before Canada's share (CR-070 D2)."),
    ("E220", 1890, 1900, "Pribilof receipts, tendered lease", "Receipt", None, None, "=cw_seal_1890s", "No",
     "Proposed", "Alaskamaxx E", "L04."),
    ("E221", 1901, 1932, "Pribilof receipts, the herd saved", "Receipt", None, None, "=cw_seal_after", "No",
     "Proposed", "Alaskamaxx E", "L04."),
    ("E222", 1870, 1879, "Alaska salmon case tax", "Receipt", None, None, "=0.05*cw_ak_salmon", "No",
     "Proposed", "Alaskamaxx F", "L04."),
    ("E223", 1880, 1889, "Alaska salmon case tax", "Receipt", None, None, "=0.15*cw_ak_salmon", "No",
     "Proposed", "Alaskamaxx F", "L04."),
    ("E224", 1890, 1900, "Alaska salmon case tax", "Receipt", None, None, "=0.3*cw_ak_salmon", "No",
     "Proposed", "Alaskamaxx F", "L04."),
    ("E225", 1901, 1932, "Alaska salmon case tax", "Receipt", None, None, "=0.6*cw_ak_salmon", "No",
     "Proposed", "Alaskamaxx F", "L04."),
    ("E226", 1868, 1870, "Alaska line: the British Columbia line bought, built to the Stikine, cable to Sitka",
     "Programme", None, None, "=0.4*cw_ak_telegraph", "No", "Proposed", "CR-070 E2", "L04; E7, MODEL $1.2m."),
    ("E227", 1871, 1897, "Alaska line: operating loss", "Subsidy & guarantee", None, None,
     "=0.05*cw_ak_telegraph", "No", "Proposed", "CR-070 E2", "L04; sold to Canada in 1897 (E235)."),
    ("E228", 1867, 1932, "Northern Commission, assay office and survey", "Programme", None, None,
     "=cw_ak_commission", "No", "Proposed", "CR-070 A1, G2", "L04; to 1932 pending the counties' CR."),
    ("E229", 1884, 1886, "Chilkoot road and tramway with the clans", "Programme", None, None,
     "=0.1*cw_ak_route", "No", "Proposed", "Alaskamaxx G", "L04."),
    ("E230", 1897, 1899, "Skagway-Whitehorse railway, assay and banking (public share), early", "Programme", None,
     "Canada", "=1*cw_ak_route", "No", "Proposed", "Alaskamaxx G", "L04; replaces E61 when cw_ak_route = 1."),
    ("E231", 1897, 1910, "Yukon route, assay and bank income (public share)", "Receipt", None, None,
     "=0.3*cw_ak_route", "No", "Proposed", "Alaskamaxx G", "L04."),
    ("E232", 1872, 1873, "Sitka-Juneau cable", "Programme", None, None, "=0.15*cw_ak_telegraph", "No", "Proposed",
     "CR-070 E3", "E7, MODEL."),
    ("E233", 1884, 1884, "Lynn Canal line to Dyea", "Programme", None, None, "=0.2*cw_ak_telegraph", "No",
     "Proposed", "CR-070 E3", "E7, MODEL; with the Chilkoot road."),
    ("E234", 1887, 1888, "Puget Sound-Sitka sea cable", "Investment", None, None, "=cw_ak_cable88/2", "No",
     "Proposed", "CR-070 E4", "Ordered 1886; Alaska's wire off British soil."),
    ("E235", 1897, 1897, "British Columbia telegraph line sold to Canada", "Receipt", None, "Canada",
     "=cw_ak_bc_sale", "No", "Proposed", "CR-070 E5", "Once the Klondike news is public."),
    ("E236", 1900, 1903, "Aleutian cable: Sitka, Kodiak, Unalaska, Attu, the Kurils, Hakodate", "Investment", None,
     None, "=cw_ak_aleutian/4", "No", "Proposed", "CR-070 E4, G9", "The second route to Japan (CR-021 I3)."),
    ("E237", 1869, 1932, "Sitka ground rent to the Tlingit clans", "Programme", None, None,
     "=IF(cw_ak_commission>0,0.005,0)", "No", "Proposed", "CR-070 G4", "$5,000 a year in gold; reviewed every ten years."),
    ("E238", 1897, 1900, "Copper River railway (Development Fund credit)", "Investment", None, None,
     "=cw_ak_copper_rail/4", "No", "Proposed", "CR-070 B4, G5", "Ore shipped from about 1900."),
    ("E239", 1886, 1889, "Pribilof receipts, tendered lease, net of Canada's 15% (convention of 1886)", "Receipt",
     None, None, "=cw_seal_1880s", "No", "Proposed", "CR-070 D2", "L04 (author, 15 Nov)."),
    ("E240", 1865, 1865, "Sacramento line to the Siskiyous, 1865 (Development Fund credit)", "Investment", None, None,
     "=cw_or_rail_south*0.25", "No", "Proposed", "CR-059 W9", "Author, 15 Nov: built from 1865 (MODEL); 25% of the line in 1865."),
    ("E241", 1866, 1866, "Sacramento line to the Siskiyous, 1866 (Development Fund credit)", "Investment", None, None,
     "=cw_or_rail_south*0.375", "No", "Proposed", "CR-059 W9", "Author, 15 Nov: built from 1865 (MODEL); 37.5% of the line in 1866."),
    ("E242", 1867, 1867, "Sacramento line to the Siskiyous, 1867 (Development Fund credit)", "Investment", None, None,
     "=cw_or_rail_south*0.375", "No", "Proposed", "CR-059 W9", "Author, 15 Nov: built from 1865 (MODEL); 37.5% of the line in 1867."),
]

# CR-070 G5: the Chitina's copper, MODEL path at cw_ak_copper = 1 ($m a year), added to Resources F.
AK_COPPER = {1900: 2, **{y: 5 for y in (1901, 1902)}, **{y: 9 for y in range(1903, 1921)},
             **{y: 3 for y in range(1921, 1929)}}

PRIV = ('SUMPRODUCT((Events!$B$6:$B$400<=$A{r})*(Events!$C$6:$C$400>=$A{r})*'
        '(Events!$E$6:$E$400="Private lending")*(Events!$J$6:$J$400="{gold}")*Events!$H$6:$H$400)')
PRIV_ANY = ('SUMPRODUCT((Events!$B$6:$B$400<=$A{r})*(Events!$C$6:$C$400>=$A{r})*'
            '(Events!$E$6:$E$400="Private lending")*Events!$H$6:$H$400)')


def yrow(year: int, base: int = G0) -> int:
    return year - FIRST + base


def event_row(ws, eid: str) -> int:
    for r in range(6, 401):
        if ws.cell(r, 1).value == eid:
            return r
    raise KeyError(eid)


def note(cell, text: str) -> None:
    cell.comment = Comment(text, AUTH)


def style_row(ws, src: int, dst: int, cols: range) -> None:
    for c in cols:
        ws.cell(dst, c)._style = copy.copy(ws.cell(src, c)._style)


# L15: land in farms, our timeline (acres), census years (1945 Census of Agriculture, Farms and Farm Property,
# Table 18; several entries OCR-flagged there; Montana's whole state, scaled by cw_l15_mt_share in the sheet).
# Read as 3 where the scan prints 5 and the neighbouring censuses rule out the printed figure: Utah 1910
# (5,397,699), Idaho 1900 (5,204,903), Montana 1910 (15,545,603) and 1925 (52,735,725), New Mexico 1935
# (54,397,205). Other flagged entries are kept as printed; all are to verify against the scans.
L15_CENSUS = {
    "Oregon": {1860: 2160539, 1870: 2369252, 1880: 4214712, 1890: 6909888, 1900: 10071328, 1910: 11685110,
               1920: 13542318, 1925: 14130847, 1930: 16548678, 1935: 17357549},
    "Washington": {1860: 366156, 1870: 649139, 1880: 1409421, 1890: 4179190, 1900: 8499297, 1910: 11712235,
                   1920: 13244720, 1925: 12610310, 1930: 13533778, 1935: 14680097},
    "Idaho": {1860: 0, 1870: 77139, 1880: 327798, 1890: 1302256, 1900: 3204903, 1910: 5283604, 1920: 8375875,
              1925: 8116147, 1930: 9346908, 1935: 9951661},
    "Nevada": {1860: 56118, 1870: 208510, 1880: 530862, 1890: 1661416, 1900: 2565647, 1910: 2714747,
               1920: 2357165, 1925: 4090586, 1930: 4080906, 1935: 3621769},
    "Utah": {1860: 89911, 1870: 148361, 1880: 655524, 1890: 1323705, 1900: 4116951, 1910: 3397699, 1920: 5050410,
             1925: 5000724, 1930: 5613101, 1935: 6259518},
    "Montana": {1860: 0, 1870: 159537, 1880: 405883, 1890: 1964197, 1900: 11844454, 1910: 13545603,
                1920: 35070656, 1925: 32735725, 1930: 44659152, 1935: 47511868},
    "New Mexico": {1860: 1414909, 1870: 835549, 1880: 651131, 1890: 787882, 1900: 5130878, 1910: 11270021,
                   1920: 24409633, 1925: 27850325, 1930: 30822054, 1935: 34397205},
    "Arizona": {1860: 0, 1870: 21807, 1880: 135573, 1890: 1297033, 1900: 1935327, 1910: 1246613, 1920: 5602126,
                1925: 11065291, 1930: 10526627, 1935: 14018540},
}


def interp(points: dict[int, float], y: int) -> float:
    ys = sorted(points)
    if y <= ys[0]:
        return points[ys[0]]
    for a, b in zip(ys, ys[1:]):
        if a <= y <= b:
            return points[a] + (points[b] - points[a]) * (y - a) / (b - a)
    return points[ys[-1]]


def build_members_land(wb) -> None:
    ws = wb.create_sheet("Members' land")
    ws["A1"] = "Members' land (L15)"
    ws["A2"] = ("CR-059 N2, CT13 and the author's Q7 (13-14 Nov 2026): the new members' ceded public domain enters "
                "the Land Fund from 1867 under its rules. Farm land is our timeline's census (1945 Census of "
                "Agriculture, Farms and Farm Property, Table 18), linear between censuses. Sold on the Land Fund's "
                "instalments at the Land Fund's price (the floor, or a share of the value per acre if higher); the nations are paid by the regional annuities (L08). MODEL.")
    ws["A3"] = "Blue = census input; black = formula. Acres; $m in period money. Net to the Treasury feeds Budget G."
    names = list(L15_CENSUS)
    heads = ["Year"] + [f"{n}, land in farms (acres)" for n in names] + [
        "Total, western Montana at its share (acres)", "Sold to date from 1867 (acres)", "Sold this year (acres)",
        "Price ($ an acre)", "Value sold, to date ($m)", "Instalments received ($m)", "Survey and register ($m)",
        "Net ($m)", "Oregon, sold to date (acres)", "Oregon's schools ($m)", "Columbia, sold to date (acres)",
        "Columbia's schools ($m)", "Bought from Columbia's nations without a treaty, to date (acres)",
        "Annuities for that land ($m)", "Net to the Treasury ($m)"]
    for c, h in enumerate(heads, 1):
        ws.cell(5, c).value = h
    col = {h: i + 1 for i, h in enumerate(heads)}
    L = lambda name: openpyxl.utils.get_column_letter(col[name])
    TOT, SOLD, NEW, PRICE, VAL, INST, SURV, NET, ORS, SCH, WAS, SCHW, BUYW, ANNW, OUT = (L(h) for h in heads[9:])
    WA = L("Washington, land in farms (acres)")
    MT = L("Montana, land in farms (acres)")
    OR = L("Oregon, land in farms (acres)")
    first_c, last_c = L(heads[1]), L(heads[8])
    r67 = yrow(1867)
    for y in range(FIRST, LAST + 1):
        r = yrow(y)
        ws.cell(r, 1).value = y
        for i, n in enumerate(names):
            ws.cell(r, 2 + i).value = round(interp(L15_CENSUS[n], y))
        ws[f"{TOT}{r}"] = f"=SUM({first_c}{r}:{last_c}{r})-(1-cw_l15_mt_share)*{MT}{r}"
        prev = r - 1
        if y < 1867:
            for c in (SOLD, NEW, VAL, ORS, WAS, BUYW):
                ws[f"{c}{r}"] = 0
        else:
            ws[f"{SOLD}{r}"] = f"=IF(cw_l15_on=1,MAX({SOLD}{prev},{TOT}{r}-{TOT}${r67}),0)"
            ws[f"{NEW}{r}"] = f"={SOLD}{r}-{SOLD}{prev}"
            ws[f"{VAL}{r}"] = f"={VAL}{prev}+{NEW}{r}*{PRICE}{r}/1000000"
            ws[f"{ORS}{r}"] = f"=IF(cw_l15_on=1,MAX({ORS}{prev},{OR}{r}-{OR}${r67}),0)"
            ws[f"{WAS}{r}"] = f"=IF(cw_l15_on=1,MAX({WAS}{prev},{WA}{r}-{WA}${r67}),0)"
            ws[f"{BUYW}{r}"] = f"={WAS}{r}*cw_col_nontreaty"
        ws[f"{PRICE}{r}"] = f"=MAX(lfund_floor,lfund_share*'Land Fund'!T{r}*cw_l15_value_rel)"
        ws[f"{INST}{r}"] = (f"=({VAL}{r}-IF({r}-lfund_inst<{yrow(FIRST)},0,INDEX(${VAL}${yrow(FIRST)}:${VAL}${yrow(LAST)},"
                             f"{r}-{yrow(FIRST) - 1}-lfund_inst)))/lfund_inst*(1-lfund_default)")
        ws[f"{SURV}{r}"] = f"={NEW}{r}*lfund_survey/1000000"
        ws[f"{NET}{r}"] = f"={INST}{r}-{SURV}{r}"
        ws[f"{SCH}{r}"] = f"=IF({SOLD}{r}>0,cw_l15_or_school*{NET}{r}*{ORS}{r}/{SOLD}{r},0)"
        ws[f"{SCHW}{r}"] = f"=IF({SOLD}{r}>0,cw_col_school*{NET}{r}*{WAS}{r}/{SOLD}{r},0)"
        ws[f"{ANNW}{r}"] = (f"=lfund_price/lfund_term*({BUYW}{r}-IF({r}-lfund_term<{yrow(FIRST)},0,"
                            f"INDEX(${BUYW}${yrow(FIRST)}:${BUYW}${yrow(LAST)},{r}-{yrow(FIRST) - 1}-lfund_term)))/1000000")
        ws[f"{OUT}{r}"] = f"={NET}{r}-{SCH}{r}-{SCHW}{r}-{ANNW}{r}"
    ws.column_dimensions["A"].width = 8
    for c in range(2, len(heads) + 1):
        ws.column_dimensions[openpyxl.utils.get_column_letter(c)].width = 16
    b = wb["Budget"]
    for y in range(FIRST, LAST + 1):
        r = yrow(y)
        v = b.cell(r, 7).value
        assert isinstance(v, str) and v.endswith(f"'Land Fund'!O{r}"), (y, v)
        b.cell(r, 7).value = v + f"+'Members'' land'!{OUT}{r}"
    note(b.cell(5, 7), "L15 (author, 13-14 Nov 2026): plus the new members' land, sheet Members' land.")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("dst")
    ap.add_argument("--values", help="JSON file {lever: value or [story, stress]} to set instead of the story minimum "
                                     "(phase 6 packages); the Changes log row names the file")
    a = ap.parse_args()
    chosen = {}
    if a.values:
        import json
        chosen = json.loads(Path(a.values).read_text())
        known = {n for n, *_ in LEVERS}
        bad = sorted(set(chosen) - known)
        assert not bad, f"unknown levers: {bad}"
    wb = openpyxl.load_workbook(a.src)
    L, E, C = wb["Levers"], wb["Events"], wb["Changes"]

    # --- Levers
    assert L.max_row == 406 and L.cell(LEVER_ROW0, 2).value is None
    taken = set(wb.defined_names.keys())
    hdr = LEVER_ROW0
    style_row(L, 66, hdr, range(1, 9))
    L.cell(hdr, 2).value = ("— CR-059-068 and CR-070: the Civil War years and Alaska ("
                            + (f"values from {Path(a.values).name}" if a.values else "the story minimum")
                            + "; Story = Stress unless both are given) —")
    r = hdr
    for name, label, story, stress, unit, status, text in LEVERS:
        r += 1
        if name in chosen:
            v = chosen[name]
            story, stress = (v if isinstance(v, (list, tuple)) else (v, v))
            if status.startswith("Lever"):
                status = "Package D final (author, 14 Nov)"
        assert name not in taken, name
        style_row(L, 406, r, range(1, 9))
        L.cell(r, 2).value = label
        L.cell(r, 3).value = story
        L.cell(r, 4).value = stress
        L.cell(r, 5).value = f"=IF(case_sel=1,C{r},D{r})"
        L.cell(r, 6).value = unit
        L.cell(r, 7).value = status
        L.cell(r, 8).value = text or None
        wb.defined_names[name] = DefinedName(name, attr_text=f"Levers!$E${r}")
    r += 1
    style_row(L, 406, r, range(1, 9))
    L.cell(r, 2).value = "Set-offs against the 1867 instalment (computed: L06, L07, F14)"
    L.cell(r, 5).value = f"={SETOFFS}"
    L.cell(r, 6).value = "$m"
    L.cell(r, 7).value = "Computed"
    L.cell(r, 8).value = "Scrip at face + N-B annuities 1862-66 + N-C + the garrisons' keep. F13 is added to the instalment."
    wb.defined_names["cw_setoffs"] = DefinedName("cw_setoffs", attr_text=f"Levers!$E${r}")
    r += 1
    style_row(L, 406, r, range(1, 9))
    L.cell(r, 2).value = "F18: gold held back from New York in 1861-65 (computed)"
    L.cell(r, 5).value = (f"=SUM(Resources!B{yrow(1861)}:E{yrow(1865)})*(1-gold_retained)*cw_ny_share*cw_ny_home")
    L.cell(r, 6).value = "$m"
    L.cell(r, 7).value = "Computed"
    L.cell(r, 8).value = "Goes east in 1866-67 by cw_ny_return (Gold & money E)."
    wb.defined_names["cw_ny_held"] = DefinedName("cw_ny_held", attr_text=f"Levers!$E${r}")
    lever_last = r

    # --- Events: existing rows rewired
    def setrow(eid, **kw):
        rr = event_row(E, eid)
        cols = dict(start=2, end=3, desc=4, cat=5, group=6, party=7, h=8, gold=10, status=11, canon=12, note=13)
        for k, v in kw.items():
            E.cell(rr, cols[k]).value = v
        return rr

    rr = setrow("E07", h="=cw_war61")
    rr = setrow("E08", h="=cw_occ6264")
    rr = setrow("E09", start=1862, end=1863, desc="Richmond war credit, drawn in goods through Matamoros (1862-63)",
                cat="Loan", group="Continental", party="Confederacy", h="=cw_rich_early", gold="No")
    note(E.cell(rr, 4), "CR-068 CT21, D5: the old E09 ($0.8m a year 1862-64, a subsidy) split into the credit "
         "(E09, E198: a loan at continental terms) and the technical mission's pay (E199). Lever L01.")
    rr = setrow("E11", end=1867, desc="Western cession: first instalment at the exchange, less set-offs",
                h=f"=MAX(0,union_vendor*{FIRST_SHARE}+cw_union_prop-cw_setoffs)")
    note(E.cell(rr, 8), "L05 option (cw_inst_opt), plus F13 (Union property at valuation), less the set-offs "
         "(cw_setoffs: scrip at face, N-B annuities, N-C, the keep of the withdrawing garrisons). 1868-72 in E197.")
    rr = setrow("E14", cat="Private lending", group=None, h="=cw_priv1867")
    note(E.cell(rr, 5), "Phase 5: the money is private (the Senate declined the Treasury loan), so the new category "
         "'Private lending' keeps it out of the Treasury's cash and counts it in private uses (Sources & uses K) and in "
         "gold paid out (Gold & money E). Lever L13 (D8: $3-5m, shorter).")
    setrow("E195", end=1872, desc="Sitka garrison and squadron (1867-72)", h="=cw_sitka_gar",
           note="L04; 1873-1900 at the taper in E218. Stops after 1900.")
    setrow("E196", h="=cw_sitka_mail", note="L04; the northern mail. Stops after 1900.")
    setrow("E09", note="Pacifican goods through Matamoros, drawn on the credit (L01); the mission's pay is E199.")
    rr = setrow("E10", desc="Peonage and captive compensation (CR-061 A2)", h="=cw_peon_comp",
                note="Author, 15 Nov: the compensation only; the treaties' costs are in E209.")
    rr = setrow("E19", note="Old model L03 + L04. Stands beside the war credit of 1862-65 (E09, E198), which is not "
                            "rolled into it (author, 15 Nov; register F06).")
    bg = wb["Budget"]
    for y in range(1867, LAST + 1):
        rb = yrow(y)
        v = bg.cell(rb, 22).value
        assert isinstance(v, str) and v.startswith("=SUMPRODUCT(") and "cw_or_cust" not in v, (y, v)
        bg.cell(rb, 22).value = v + f"+cw_or_cust_share*cw_or_cust_base*B{rb}"
    note(bg.cell(5, 22), "CR-059 V9 (author, 15 Nov): from 1867 plus Oregon's customs share (cw_or_cust_share x "
                         "cw_or_cust_base x customs).")
    rr = setrow("E61", h="=1*(1-cw_ak_route)")
    note(E.cell(rr, 8), "Alaskamaxx G (author, 14 Nov; CR-070 F3): moved to 1897-99 (E230) when cw_ak_route = 1.")

    last = max(x for x in range(6, 401) if E.cell(x, 1).value)
    assert E.cell(last, 1).value == "E196", E.cell(last, 1).value
    for k, ev in enumerate(NEW_EVENTS, start=1):
        rr = last + k
        style_row(E, last, rr, range(1, 14))
        for c, v in zip((1, 2, 3, 4, 5, 6, 7, 8), ev[:8]):
            E.cell(rr, c).value = v
        E.cell(rr, 9).value = f'=IF(H{rr}="","",H{rr}*(C{rr}-B{rr}+1))'
        E.cell(rr, 10).value, E.cell(rr, 11).value, E.cell(rr, 12).value, E.cell(rr, 13).value = ev[8:]
    assert last + len(NEW_EVENTS) <= 400

    # --- Navy plan: Honolulu frigates beyond the plan (L02)
    nv = wb["Navy plan"]
    assert nv.cell(yrow(1862), 3).value in (0, "0")
    nv.cell(yrow(1862), 3).value = "=0+cw_hon_frig"

    # --- F18: Resources R 1861-65
    rs = wb["Resources"]
    for y in range(1861, 1866):
        rr = yrow(y)
        assert rs.cell(rr, 18).value == f"=SUM(B{rr}:E{rr})*gold_retained+(G{rr}+H{rr})*conc_gold"
        rs.cell(rr, 18).value = (f"=SUM(B{rr}:E{rr})*(gold_retained+(1-gold_retained)*cw_ny_share*cw_ny_home)"
                                 f"+(G{rr}+H{rr})*conc_gold")
    note(rs.cell(yrow(1861), 18), "F18 (CR-068 G8): no treasure steamers to New York in 1861-65. The New York-bound "
         "share of exported gold (cw_ny_share) is kept at home (cw_ny_home) or goes direct to London.")

    build_members_land(wb)

    # --- Alaskamaxx C-D: Resources E (Alaska gold) shifted early and the Seward Peninsula placers
    rs.cell(5, 20).value = "Alaska gold, historical path ($m)"
    rs.cell(5, 20)._style = copy.copy(rs.cell(5, 5)._style)
    for y in range(FIRST, LAST + 1):
        rr = yrow(y)
        v = rs.cell(rr, 5).value
        assert isinstance(v, (int, float)), (y, v)
        rs.cell(rr, 20).value = v
        rs.cell(rr, 20)._style = copy.copy(rs.cell(rr, 5)._style)
        if 1867 <= y <= 1898:
            rs.cell(rr, 5).value = (f"=INDEX($T${yrow(FIRST)}:$T${yrow(LAST)},MIN({y - FIRST + 1}+cw_ak_gold_lead,"
                                    f"{1898 - FIRST + 1}))" + ("+cw_ak_seward" if y >= 1876 else ""))
        else:
            rs.cell(rr, 5).value = f"=T{rr}"
    note(rs.cell(5, 20), "Alaskamaxx (author, 14 Nov): the historical path. Column E reads it shifted by "
         "cw_ak_gold_lead years in 1867-98 (finder's compact) plus cw_ak_seward in 1876-98.")

    # --- CR-070 G5: Resources F (copper & other metals) gains the Chitina's copper, 1900-28
    for y, amt in AK_COPPER.items():
        c = rs.cell(yrow(y), 6)
        assert isinstance(c.value, (int, float)), (y, c.value)
        c.value = f"={c.value}+{amt}*cw_ak_copper"
    note(rs.cell(yrow(1900), 6), "CR-070 B4, G5 (author, 15 Nov): the Chitina's copper under Nicolai's finder's "
         "compact, 1900-28, MODEL path scaled by cw_ak_copper.")

    # --- L12: Paths E, 1863-65
    ps = wb["Paths"]
    for y in (1863, 1864, 1865):
        c = ps.cell(yrow(y), 5)
        assert isinstance(c.value, (int, float)), (y, c.value)
        c.value = f"={c.value}+cw_refugees"

    # --- L13: Gold & money E and Sources & uses K; L17: Sources & uses R, E and Checks L
    gm, su, ck = wb["Gold & money"], wb["Sources & uses"], wb["Checks"]
    su.cell(SU0 - 1, 18).value = "War bonds in coin from idle gold (L17)"
    su.cell(SU0 - 1, 18)._style = copy.copy(su.cell(SU0 - 1, 11)._style)
    note(su.cell(SU0 - 1, 18), "L17 (author, 13 Nov 2026, D10): in 1861-65 war bonds may be subscribed in coin from "
         "a bounded share (cw_idle_ratio) of notes and bank reserves (Gold & money I), never more than the gold above cover (K). Counted as a private "
         "source here and as home-market capacity in Checks L.")
    for y in range(FIRST, LAST + 1):
        g, s = yrow(y), yrow(y, SU0)
        f = gm.cell(g, 5).value
        assert f.startswith("=SUMPRODUCT(") and "Private lending" not in f
        gm.cell(g, 5).value = f + "+" + PRIV.format(r=g, gold="Yes") + ("+cw_ny_return*cw_ny_held/2" if y in (1866, 1867) else "")
        k = su.cell(s, 11).value
        assert k == f"=SUM(F{s}:J{s})+'Energy link'!BF{g}", (y, k)
        su.cell(s, 11).value = k + "+" + PRIV_ANY.format(r=s)
        assert su.cell(s, 5).value == f"=SUM(B{s}:D{s})"
        su.cell(s, 5).value = f"=SUM(B{s}:D{s})+R{s}"
        su.cell(s, 18).value = f"=IF(AND($A{s}>=1861,$A{s}<=1865),MIN(MAX(0,'Gold & money'!K{g}),cw_idle_ratio*'Gold & money'!I{g}),0)"
        su.cell(s, 18)._style = copy.copy(su.cell(s, 12)._style)
        lc = ck.cell(g, 12).value
        old = (f"=IF('Debt & cash'!Y{g}*issue_price<=mkt_capacity*Economy!O{g}+foreign_capacity,\"OK\",\"Check\")")
        assert lc == old, (y, lc)
        ck.cell(g, 12).value = (f"=IF('Debt & cash'!Y{g}*issue_price<=mkt_capacity*Economy!O{g}+foreign_capacity"
                                f"+'Sources & uses'!R{s},\"OK\",\"Check\")")

    # --- Changes log
    n = C.max_row + 1
    C.cell(n, 1).value = "13-15 Nov: CR-059-068, CR-070"
    C.cell(n, 2).value = "Civil War CRs, levers"
    C.cell(n, 3).value = (f"Model plan phase 5 (build/cr059_068_levers.py): levers cw_* on Levers rows {LEVER_ROW0}-"
                          f"{lever_last} at the story minimum; F18 (no gold to New York 1861-65) in Resources R; "
                          "L17 idle-gold source (Sources & uses R, Checks L), 0.12 / 0.06; F18 gold goes east 1866-67; E09 the Richmond "
                          "credit as a loan (with E198-E199); E11 split (E197) with set-offs; E14 private lending; "
                          "new rows E197-E242; the Members' land sheet (L15); CR-070's Alaska (E195-E196, E217-E239, "
                          "Resources E/F/T); E10 the compensation only; Oregon's customs share in Budget V from 1867 "
                          "(rebuilt 13-15 Nov 2026)."
                          + (f" Lever values from {Path(a.values).name}." if a.values else ""))
    style_row(C, n - 1, n, range(1, 4))
    wb.save(a.dst)
    print(f"saved {a.dst}; levers rows {LEVER_ROW0}-{lever_last}; events to {last + len(NEW_EVENTS)}")


if __name__ == "__main__":
    main()
