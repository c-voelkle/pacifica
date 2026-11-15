"""Phase 1-2 of the CR-059-068 model plan: the event register and the fixed/free split.

Reads the decision tables of the nine drafts at the pinned commit, maps every row to one
register row, and writes:
  register.csv   one row per event (owner, sources, model place, class, value or bound)
  crosswalk.csv  every decision-table row of the drafts -> one register row
Run from the repository root:  python3 outputs/sessions/20261113-model-register/build_register.py
"""
import csv, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
REV = ROOT / "book-agent" / "revision"
CRS = ["CR-059", "CR-060", "CR-061", "CR-062", "CR-063", "CR-064", "CR-065", "CR-067", "CR-068"]
SUBHEADERS = {"ID", "No.", "District", "Department", "Round", "Lincoln", "When", "Weight", "Stretch", ""}

# class values
FIX, FIXU, LEV, MEMO, DEF, NOTM, NONE, Q = ("Fixed", "Fixed (unchanged)", "Lever", "Memo", "Deferred by author",
                                           "Not the model's", "No model place", "Fixed? (author)")

R = []
def r(rid, title, years, owner, place, cls, value, status, note="", domain="Finance", cites=""):
    R.append(dict(rid=rid, title=title, years=years, owner=owner, cites=cites, domain=domain, place=place,
                  cls=cls, value=value, draft_status=status, note=note))

# ---------------------------------------------------------------- finance: fixed
r("F01", "London bonds repaid in full; London first; Reserve Fund untouched before the war", "1859", "CR-068 CT26",
  "E01; Debt & cash (repayment order)", FIX,
  "public debt $3.40m end-1858 -> $1.59m end-1859; Reserve Fund $3.29m", "APPROVED (CT26 decided)",
  "CT26 says the model already gets there with no lever changed; only the order of repayment moves", cites="CR-068 CT28")
r("F02", "End of the war footing: Pacifica's armistice; the Protectorship's dates", "1861-65", "CR-062 A1",
  "war-year switches; E07/E08 end; Labour (war unemployment)", FIX, "Protectorship 1 Jun 1861-31 May 1865; armistice mid-May 1865; Amity treaty last week of May; Enabling Law 1 Dec 1865",
  "PROPOSED (A1 order OPEN)", cites="CR-062 A6; CR-068 B16a, G9a, CT29")
r("F03", "Army of 1861 under the Defense Law", "1861", "CR-067 B1", "Labour (mobilised); garrison cost base", FIX,
  "about 20,000 regulars and 90,000 reservists", "canon; figures MODEL")
r("F04", "Western cession: $40m gold vendor credit", "1867-72", "CR-062 T4",
  "E11 (now 1866-72 in sevenths -> 1867-72); Levers union_vendor; Gold & money", FIX,
  "$40m in gold; first instalment deposited at the New York Subtreasury before the April 1867 vote, released at exchange (summer 1867)",
  "canon PROPOSED; schedule MODEL", "the split is lever L05; the set-offs are L06/L07", cites="CR-062 M1, S2, X1, O7, S4; CR-059 V1; CR-068 G11")
r("F05", "Alaska purchase", "Oct 1867", "CR-062 K3", "E12", FIX,
  "$7.2m in Pacifica's minted gold, paid at San Francisco against the commissioners' certificate", "PROPOSED",
  "amount and year as E12 already has them", cites="CR-062 K6, K10, M4, X5")
r("F06", "Confederate debt refinanced on customs security", "1871-72", "CR-068 CT28", "E19", FIX,
  "$25m of new lending", "APPROVED (CT28 adapted)",
  "question for phase 5: does the 1862-65 credit (L01) roll into this $25m or sit beside it?")
r("F07", "Abolition compensation bonds: Pacifica guarantor, takes $6m", "1888-89", "CR-068 CT28", "E41; E46 unchanged",
  FIX, "$6m taken (E41 3 x 2); guarantor, not lender", "APPROVED (CT28 adapted)")
r("F08", "Free Mississippi navigation as the condition of further credit", "1865 onward", "CR-068 K21",
  "E20 (Richmond's Mississippi tolls replaced, $1m a year 1871-88)", Q, "condition, no sum",
  "APPROVED (Two Houses decision 11 Nov)", "Q: if free navigation is the price of the credit, does Pacifica still pay E20 for the tolls?",
  cites="CR-068 PP8b")
r("F09", "Grant's war: Gulf squadron, turret ships, mines", "1870-71", "CR-068 K23", "E17", FIXU, "E17 as it stands",
  "canon", "the drafts name it but change nothing")
r("F10", "Peonage and captive compensation (E10 re-dated)", "1866", "CR-061 A2", "E10 (1865 -> 1866)", FIX,
  "quarter of registered face, cap $100 a peon; $50 a released captive; debts after 1 Jan 1863 not paid; total MODEL, under $0.5m",
  "APPROVED rule; amounts MODEL", "captives 2,000-3,000 (Benedict, Carleton) give $0.10-0.15m; the peon count is still needed",
  cites="CR-061 K4, N3, A1")
r("F11", "Oregon's customs held for Oregon", "1862-67", "CR-059 W6", "Budget (customs): not confederal revenue", FIX,
  "all Astoria and Portland customs to the Oregon account", "PROPOSED")
r("F12", "Idaho, Montana and Comstock gold on Pacifica's side", "1862 onward", "CR-059 I6", "Resources", FIX,
  "historical output: Boise Basin from Aug 1862; Montana camps 1862-64; Comstock through San Francisco, Washoe held from Apr 1864",
  "PROPOSED", "the plan names Comstock and Idaho; Montana's camps (CR-060 M2, CO2) are on Pacifica's side too",
  cites="CR-060 M1, M2, C1, C5, CO2")
r("F13", "Union public property taken at valuation", "1862; 1867", "CR-059 I3", "Events (new row) or a set-off inside E11", Q,
  "Fort Walla Walla's stores (1862); Port Townsend and Fort Union property 'removed or valued' (1867)", "PROPOSED",
  "Q: paid in cash when taken, or credited against the $40m?", cites="CR-062 T3, X2; CR-061 P2")
r("F14", "Keep of withdrawing Union garrisons", "1862; 1864; 1867", "CR-060 C5", "Events (new row) or a set-off inside E11", Q,
  "Fort Churchill's volunteers fed at the stations at Pacifica's charge (1864); Fort Union's march-out under escort (1867)",
  "PROPOSED; 'against the vendor credit, OPEN'", "small; same question as F13", cites="CR-061 P2; CR-060 models")
r("F15", "Baja purchase", "1867-71", "CR-062 M6", "E13", Q, "E13 as it stands ($1m a year)", "canon PROPOSED; 'test separately'",
  "Q: keep E13 on, or switch it off and test it as a separate case?")
r("F16", "Pyramid Lake and Washoe crisis", "1860", "canon", "E06", FIXU, "E06 as it stands ($1m)", "canon",
  "the 500 volunteers are canon (§8), restated in CR-067's 'What canon says'; E06's $1m already covers them", cites="CR-067 B6; CR-068 K11")

# ---------------------------------------------------------------- finance: levers
r("L01", "Richmond war credit: amount and rate", "1862-65", "CR-068 CT21",
  "E09 reclassified: Loans / War credit / Gulf", LEV,
  "floor: the $2.4m now in E09; widened Sept 1862; terms printed in Texas Feb 1863 (lent for independence, at interest, on security, due on reunion); no new advances after the armistice",
  "APPROVED (CT21, CT28, PP4c)", "Arizona's renunciation (CR-061 C8) is paid in this credit",
  cites="CR-068 G3, B8, B11, PP4c, CT28; CR-061 C8; CR-063 X4, CT5; CR-062 A3")
r("L01m", "Technical and military missions; Matamoros deliveries", "1861-65", "CR-063 L1",
  "E09 (cost part)", Q,
  "Logan's mission 1861-May 1865; Marcus's mission late 1862-late 1863; Matamoros cargo priced as coin, arms and specialist goods",
  "canon (mission); PROPOSED", "Q: are rifles and machine tools sold through Matamoros drawn on the credit (L01) or a separate cost? Recommended: on the credit; only the missions' pay is a cost",
  cites="CR-063 L2, X1, X2; CR-062 A4, A5; CR-067 missions row")
r("L02", "Honolulu package: batteries, two frigates, second turret ship and its slip", "1861-63", "CR-068 TL6",
  "Navy plan / Navy; Events (new row)", LEV, "the second turret ship lies at Honolulu from 1863, shipped in sections",
  "APPROVED (rev 37)", cites="CR-068 G2, B5, CT-KAIULANI; CR-067 C4")
r("L03", "War and garrison spending above the head counts", "1861-67", "CR-067 B7",
  "E07 (1861), E08 (1862-64 -> 1861/62-67); Budget (defence)", LEV,
  "head counts fixed (see the by-department rows G-*); cost per man, coin purchases and chartered steamers free",
  "MODEL", "E08's dates run to the exchange of 1867")
r("L03a", "Department of the Columbia: occupation of Oregon and Washington", "1861-67", "CR-059 W1",
  "E07, E08", LEV, "Walla Walla taken at valuation July 1862; the force staged on the Sound, winter 1864-65; Port Townsend held by the Union to 1867",
  "PROPOSED", "gold requisitions 'slightly above market' (W5) are part of this cost",
  cites="CR-059 W2, W5, W14, W15, I2, I3; CR-065 P2; CR-067 Columbia row")
r("L03b", "Department of the Great Basin: Salt Lake road and Washoe", "1862-67", "CR-060 D4",
  "E08", LEV, "Salt Lake road about 800 men and 400 animals from Oct 1862; Fort Bridger company from Dec 1862; Washoe about 1,500 from Apr 1864; Deseret's wheat bought in gold",
  "MODEL", "one or two summer trains a year from California (S2)", cites="CR-060 S1-S4, C5, R1, U3; CR-067 Great Basin row")
r("L03c", "Department of the Rio Grande: the column and the garrison", "1862-67", "CR-061 C3",
  "E08", LEV, "about 3,000 in autumn 1862; 2,300 regulars and about 670 animals in winter; Fort Garland 100-150 from May 1863; Fort Union watched to 1867",
  "MODEL (audit closed 9 Nov)", "bulk food bought locally in gold (L1, L4, C9); Pima wheat (N1); grain sold at cost in Santa Fe (L5); the 1866 revolt (A3)",
  cites="CR-061 C1-C14, L1-L5, F1-F9, N1, A3, P1-P2; CR-067 Rio Grande row")
r("L03d", "California and Hawaii departments; the fleet", "1861-67", "CR-067 C4",
  "Navy; Budget (defence)", LEV, "coast squadron and Puget Sound blockade; Columbia armoured battery (1862); Colorado River flotilla; Honolulu station; marines",
  "units canon; organization PROPOSED", "the Honolulu package itself is L02", cites="CR-067 B6, California and Hawaii rows, C1-C5")
r("L04", "Sitka garrison, Sitka squadron and the northern mail", "1867 onward", "CR-062 K10", "Events (new rows)", Q,
  "no figure in the drafts", "PROPOSED", "the plan books these at zero in phase 4 and does not list them as a lever. Recommended: a lever, or a small fixed estimate",
  cites="CR-062 models; CR-067 C4")
r("L05", "Instalment split of the $40m", "1867-72", "CR-062 M2", "E11", LEV,
  "(a) $8m + 5 x $6.4m; (b) six of $6.67m; (c) $10m + 5 x $6m; $8m is about 12 t fine", "OPEN")
r("L06", "Oregon war-scrip purchase and its set-off", "1861-66; set-off 1867", "CR-059 P11",
  "Events (new row: purchase); E11 (set-off)", LEV,
  "ceiling: the $6.0m claimed (less what the Union had paid: $2.8m appropriated, about $1.09m in bonds by 1866); purchase price free",
  "APPROVED in direction (7 Nov); amounts OPEN (open 20, 42)", "cash out 1861-66 at a discount; credited at face against the $40m in 1867",
  cites="CR-059 E2; CR-062 T4, M2")
r("L07", "Unratified-treaty deduction (N-C) and annuity credit (N-B) inside the $40m", "1867", "CR-059 N-C",
  "E11 (set-off); Land Fund (N-C paid in as purchase money)", Q,
  "N-C: the Union's debts under the unratified 1851 and 1855 treaties; N-B: annuities Pacifica paid from 1862",
  "PROPOSED; amounts OPEN (open 20; research 30)",
  "the plan makes these a lever that follows the scrip. Recommended: fixed by source (N-C from the treaties' own amounts, N-B from what L08 pays), not sized for headroom",
  cites="CR-059 N-B; CR-062 T12, T4")
r("L08", "Treaty annuities, passage money and scouts' pay", "1862 onward", "CR-061 N4", "Events (new rows); Budget", LEV,
  "no amounts in the drafts", "PROPOSED; amounts OPEN", "one lever, three regional rows (L08a-c)")
r("L08a", "Annuities: the Northwest", "1862 onward", "CR-059 N-B", "Events", LEV,
  "the Union's ratified treaties assumed from 1862 'at least in full'; Klamath compact 1864; Paiute peace 1865-66; Wasco scouts",
  "PROPOSED", cites="CR-059 N-A, N-D-N-I, I1, I5; CR-060 N5")
r("L08b", "Annuities: the Great Basin and the Rockies", "1863 onward", "CR-060 N1", "Events", LEV,
  "Box Elder and Soda Springs 1863; Washakie; Spanish Fork 1865 (cattle and flour, part from the road's fees); Owyhee and Bannock 1866; the Ute agreement 1866",
  "PROPOSED; terms OPEN", "the road's fees are a receipt that nets against this", cites="CR-060 D8, D9, M8-M10, R2-R4, N2-N8; CR-061 N6")
r("L08c", "Annuities: the Southwest", "1862 onward", "CR-061 N4", "Events", LEV,
  "Pima-Maricopa compact 1862 (a purchase, not an annuity); Navajo 1863 and 1865; Apache peace 1865 (passage money from the Sunset road's customs; scouts in coin); Moache, Capote, Jicarilla",
  "APPROVED (N3, N4); PROPOSED", "the Santa Rita lease's royalty goes the other way (energy row N04)", cites="CR-061 N1-N7, C6; CR-067 B6")
r("L09", "Juárez credit on the Sonora customs", "1865 onward", "CR-061 M1", "Loans (new row)", LEV,
  "amount not stated anywhere; rifles delivered at Paso del Norte from Aug 1865", "APPROVED backing (CR-058); date PROPOSED (CT4)",
  cites="CR-062 M5; CR-058 NA-1")
r("L10", "Promised Oregon works and the railway north", "1863-66; after 1867", "CR-059 V9", "Works; Development Fund", LEV,
  "Willamette Falls and Cascades locks, the Columbia bar, the Oregon-Sacramento railway, on Development Fund credit; the Sacramento line reaches the Siskiyous 1863-66 (W9)",
  "PROPOSED; open 23", "W9's date is fixed; its cost is free", cites="CR-059 W9, open 23")
r("L11", "Washoe net-proceeds mining tax", "1864 onward", "CR-060 C8", "Budget (receipt)", LEV,
  "rate OPEN; must be lighter than the rejected 1863 constitution's", "PROPOSED",
  "the ceiling is narrative (lighter than 1863), not financial. Recommended: research the 1863 rate and set it below")
r("L12", "Refugees, deserters and draft evaders", "1863-65", "CR-059 W7", "population: flows.py / pools.toml", LEV,
  "MODEL 'tens of thousands'; larger than historical (author's story assumption, 10 Nov)", "PROPOSED",
  "ceiling from pools.toml, us_immigration.toml and the Union's draft numbers", domain="Population",
  cites="CR-060 R2; CR-068 G5, B10, TL1, PP5, PP6")
r("L13", "Private lending to Eastern houses and the transit companies (replaces the Treasury loan)", "1867", "CR-062 M3",
  "E14 ($10m 'Treasury loan to the Union')", LEV,
  "Senate declines the Treasury loan (decided 13 Nov); placed privately with New York and Philadelphia houses and the transit companies; amount deferred: 'requires modeling'",
  "outcome decided; amount OPEN (open 19)", "not in the plan's lever list. E14's party and loan group change with it",
  cites="CR-062 S10, L1, CT9; CR-068 G11, O5")
r("L14", "Hudson's Bay Company and Puget Sound Agricultural Company rights bought", "1861-62", "CR-059 P10",
  "Events (new row: purchase)", Q, "no amount; historically the 1869 award was $650,000 ($450,000 and $200,000)",
  "APPROVED in direction (7 Nov)", "not in the plan. Recommended: fixed at the historical award")
r("L15", "Ceded public domain to the Land Fund; Oregon's customs and school shares", "1867 onward", "CR-059 V9",
  "Land Fund; Budget (member shares)", Q,
  "Land Fund receives the ceded public domain; a fixed share of its margin for Oregon's schools; a defined customs share; no confederal direct tax",
  "PROPOSED; open 19, 21, 44", "not in the plan. Recommended: the existing member-state rules, with the new members' land in the Land Fund from 1867",
  cites="CR-059 N2, CT13; CR-061 K3; CR-060 A5")
r("L16", "The Nauvoo Legion's pay", "1863-67", "CR-060 D7", "Budget (defence)", DEF, "recommended: confederal pay in gold for road duty only",
  "OPEN; 'not to be integrated' (CT7 deferred)", "carry at zero with a switch")

# ---------------------------------------------------------------- finance: memo
r("M01", "Assay offices at Idaho City and Virginia City; coin at cost", "1862 onward", "CR-059 I6", "Gold & money", MEMO, "", "PROPOSED", cites="CR-060 M1")
r("M02", "Mail: Mullan's contract; the Salt Lake road mail", "1862 onward", "CR-059 I4", "Budget", MEMO, "", "PROPOSED", cites="CR-060 D4")
r("M03", "Claims commission, boundary survey, archives", "1867 onward", "CR-062 X3", "Budget", MEMO, "", "PROPOSED", cites="CR-062 T9, T14")
r("M04", "The Hawaiian sailor's compensation", "1861; claim to 1867", "CR-062 T9", "Budget", MEMO, "", "PROPOSED", cites="CR-068 B5")
r("M05", "Homeland leases (Lewiston townsite; mining ground); rent passes to the nations", "1861 onward", "CR-059 I1",
  "Land Fund (pass-through)", MEMO, "", "PROPOSED; rent OPEN (open 25)", cites="CR-060 N7")
r("M06", "Coin leaving by the Santa Fe Trail permit trade", "1863-67", "CR-061 F6", "Gold & money", MEMO, "", "PROPOSED")
r("M07", "Union access to the Columbia and the Sound; named routes; bonded transit", "1867 onward", "CR-062 T5",
  "Budget (port charges)", MEMO, "", "PROPOSED", cites="CR-062 T6; CR-061 P3")
r("M08", "Paso del Norte customs post", "1865 onward", "CR-061 M2", "Budget", MEMO, "", "PROPOSED")
r("M09", "Mutual waiver of war claims", "1867", "CR-062 T9", "none (no payment)", MEMO, "", "PROPOSED")
r("M10", "Pre-1859 Oregon policy: market, coin, 1855 credit, assisted passage, scholarships", "1848-58", "CR-059 P1",
  "already in the workbook where canon", FIXU, "", "canon / PROPOSED", "P3 extends CR-034; P8 and P9 are private money", cites="CR-059 P2-P9")

# ---------------------------------------------------------------- population
r("P01", "Accessions on exchange: the confederal count", "1867", "CR-062 X1", "Paths!D (territory joins); census.toml", Q,
  "the workbook now joins 177,000 (1862), 85,000 (1863), 25,000 (1864), 10,000 (1865), 50,000 (1867), with no recorded split",
  "PROPOSED", "the join years must be rebuilt territory by territory (P01a-h)", domain="Population")
r("P01a", "Oregon", "1867", "CR-059 V15", "census.toml [states] Oregon", FIX, "52,465 in 1860 (verified); about 10,000 emigrants in autumn 1862 (Alvord)",
  "PROPOSED", domain="Population", cites="CR-059 W7, research 25")
r("P01b", "Washington Territory", "1867", "CR-059 V17", "census.toml Washington", FIX, "11,594 in 1860 (verified)", "PROPOSED",
  "not in the plan's lists", domain="Population")
r("P01c", "Idaho", "1867", "CR-059 I10", "census.toml Idaho (no 1860 value)", FIX, "no census before 1870 (14,999); the rush from Aug 1862", "PROPOSED",
  "head count needs a stated assumption", domain="Population")
r("P01d", "Washoe", "held from Apr 1864; counted 1867", "CR-060 C11", "census.toml Nevada", FIX, "6,857 in 1860; 42,941 in 1870", "PROPOSED",
  "head count needs a stated assumption for 1864-67", domain="Population", cites="CR-060 C5, A2")
r("P01e", "Deseret, with southwest Wyoming", "1867", "CR-060 D12", "census.toml Utah (+ Wyoming share)", FIX,
  "40,273 in 1860; associate from Dec 1862, member only on exchange", "PROPOSED (CT1 decided)",
  "plan: anything booked for 1862-66 comes out", domain="Population", cites="CR-060 D5, A1, A4")
r("P01f", "Western Montana", "1867", "CR-060 M7", "census.toml Montana (west of the line)", FIX, "no census before 1870 (20,595)", "PROPOSED",
  "head count needs a stated assumption", domain="Population", cites="CR-060 A3, CO2")
r("P01g", "New Mexico with Arizona and the San Luis Valley", "1867 (CR-061) or 1862 (plan)", "CR-061 A4",
  "census.toml New_Mexico", Q, "93,516 in 1860 (verified), which already includes Arizona and the valley's settlements",
  "APPROVED (A4)", "Q1: CR-061 enters New Mexico in the count from 1867; the plan has the Rio Grande and Arizona from 1862. Q2: the plan's '7,000 from 1863' for the San Luis Valley would count the valley twice",
  domain="Population", cites="CR-061 K1, F8, P5; CR-060 CO3")
r("P01h", "Alaska", "1867", "CR-062 K7", "census.toml Alaska (no value before 1880)", FIX, "small; source to find", "PROPOSED",
  domain="Population", cites="CR-062 models")
r("P02", "Native nations, Hispano and Pueblo populations in the model's groups", "1862 onward", "CR-061 K6", "canon.py groups", MEMO,
  "treaty-nation members may hold citizenship (CR-059 open 27)", "APPROVED / PROPOSED", "follow the existing groups; note what cannot be expressed",
  domain="Population", cites="CR-059 open 27; CR-061 N3")
r("P03", "War deaths and mobilisation on Pacifica's side", "1862-66", "CR-061 C10", "memo items", MEMO,
  "second Valverde; Apache Pass; Bear River (a limited action, about 300 men); Black Hawk; the Owyhee killings; the 1866 revolt", "MODEL",
  domain="Population", cites="CR-060 D8, M8, N6; CR-061 C6, A3")
r("P04", "Neighbours: the Union's and the Confederacy's war", "1861-66", "CR-064 S8", "neighbours.py / neighbours.toml", FIX,
  "Confederacy keeps Louisiana and its ports; Shiloh (Union ~11,500, Confederate ~8,000); Vicksburg's army escapes (~15,000 out, ~8,000 stay); Overland > 60,000; Atlanta untaken; Kentucky and Delaware slave in 1866",
  "PROPOSED / MODEL", domain="Population", cites="CR-063 N1-N4, V1-V6; CR-064 A1-A13; CR-065 W4; CR-059 open 38")
r("P05", "Exclusion article, residence and franchise rules", "1866", "CR-059 X2", "none", MEMO, "touches 128 protected people (X8)", "PROPOSED",
  domain="Population", cites="CR-059 X1-X8")

# ---------------------------------------------------------------- energy
r("N01", "Comstock mining load", "1864 onward", "CR-060 C5", "energy workbook", FIX, "", "PROPOSED", domain="Energy")
r("N02", "Puget Sound coal for the fleet and the coast steamers", "1861 onward", "CR-059 P1", "energy workbook", FIX, "", "PROPOSED",
  domain="Energy", cites="CR-068 G2 (reason 6)")
r("N03", "Celilo fishing guarantee: no dam at The Dalles", "1866", "CR-059 S6", "energy workbook, Hydro", FIX, "", "PROPOSED", domain="Energy", cites="CR-055")
r("N04", "Santa Rita copper lease with the Chihenne royalty", "1865", "CR-061 N4", "energy workbook; CR-052 link", FIX, "", "APPROVED", domain="Energy")
r("N05", "Columbia hydro sites inside the confederation", "1867 onward", "CR-059 V15", "energy workbook, Hydro", FIX, "", "PROPOSED", domain="Energy")

# ---------------------------------------------------------------- logistics
for rid, t, o, c in [
    ("G01", "San Francisco-Honolulu by navy steamer; the mails and news timing", "CR-068 TL5", "CR-068 B4, B15, CT17, CT24"),
    ("G02", "Monterey-Salt Lake by Honey Lake and the Humboldt", "CR-060 S2", "CR-060 Part V, S1, S3"),
    ("G03", "The Mullan Road, Walla Walla-Fort Benton", "CR-059 I3", "CR-059 I4, I5; CR-060 M2"),
    ("G04", "The Santa Fe Trail and the plains roads", "CR-061 F1", "CR-061 F4, F6, F9, P3; CR-060 CO4"),
    ("G05", "Leavenworth-Salt Lake: the Union's ceiling", "CR-060 U4", "CR-060 S4, U1-U3"),
    ("G06", "The staged road: Colorado mouth-Fort Yuma-Tucson-Mesilla-Santa Fe", "CR-061 L2", "CR-061 C1, C4, C5, L1-L5"),
    ("G07", "The Matamoros corridor", "CR-063 X2", "CR-063 T4, X1"),
    ("G08", "Panama-Puget Sound: the Union's sealift", "CR-059 W13", "CR-064 S3"),
    ("G09", "The telegraph", "CR-060 D4a", "CR-060 C5"),
    ("G10", "Fort Benton and the Missouri's June rise; the Montana Trail", "CR-060 M6", "CR-060 M2, CO2"),
    ("G11", "Union and Confederate war logistics: rail, river, sealift, march rates (claim checks only)", "CR-064 A4", "CR-064 A6, A13")]:
    r(rid, t, "1861-67", o, "logistics/data/routes.toml", FIX, "", "Hist. / MODEL", domain="Logistics", cites=c)

# ---------------------------------------------------------------- not the model's / no model place
r("X01", "Not the model's to decide", "", "plan phase 7", "none", NOTM,
  "flag of the Matamoros ships; the 1855-56 naval agreement; when Kentucky and Delaware end slavery; a later war ministry (CR-067 A4)", "")
r("X02", "The Union's war finance on the page", "1864-65", "CR-065 F1", "none", NOTM, "canon §9: named, not modelled", "OPEN in canon", cites="CR-065 F2-F5")
r("X03", "The Union's armoured fleet and Gulf garrison", "1862-65", "CR-063 F1", "MIL-01 audit, not these models", NOTM, "", "MODEL",
  cites="CR-063 F2, F3, S1-S6, M1-M7")
r("X04", "Richmond's own London debt", "1863 onward", "CR-068 CT28", "Gulf sheet note only", NOTM, "no Pacifican cash", "APPROVED (new fact)")
r("Z59", "CR-059: votes, conventions, offers and politics", "", "CR-059", "none", NONE, "", "", domain="None")
r("Z60", "CR-060: politics, compacts, persons, the Colorado line", "", "CR-060", "none", NONE, "", "", domain="None",
  note="the Colorado votes of 1875-82 (CO7) lie outside this round")
r("Z61", "CR-061: politics, compacts, persons", "", "CR-061", "none", NONE, "", "", domain="None")
r("Z62", "CR-062: treaty texts, the Senate, residents' rights", "", "CR-062", "none", NONE, "", "", domain="None")
r("Z63", "CR-063: the Gulf campaign", "", "CR-063", "none", NONE, "", "", domain="None")
r("Z64", "CR-064: the Union's western command and campaigns", "", "CR-064", "none", NONE, "", "", domain="None")
r("Z65", "CR-065: the election and the lame-duck winter", "", "CR-065", "none", NONE, "", "", domain="None")
r("Z67", "CR-067: command structure and offices", "", "CR-067", "none", NONE, "", "", domain="None")
r("Z68", "CR-068: the agon (terms, Chronicler, papers, rounds, telling)", "", "CR-068", "none", NONE, "", "", domain="None")


# ---------------------------------------------------------------- added after mapping the 584-item workbook
r("F17", "The US naval storehouse at Sausalito sealed", "1861", "CR-068 K15", "Navy (asset taken over)", MEMO,
  "value not given", "APPROVED", "the workbook item reads it as an asset gain")
r("F18", "No treasure steamers to New York; Pacific gold retained", "1861-65", "CR-068 G8", "Gold & money; Abroad", FIX,
  "gold exports to New York nil 1861-65; applied in phase 5 (Resources R: 85% New York share; Story half, Stress a quarter kept at home; goes east 1866-67, author 14 Nov)", "APPROVED", cites="CR-068 W2, G6b; CR-064 causal chain; CR-065 F1")
r("F19", "Hawaii's agreed revenues under the Enabling Law", "from 1 Dec 1865", "CR-068 CT29", "Budget; Partners", FIXU,
  "canon's agreed revenues; no new sum", "canon", cites="CR-068 G9a")
r("M11", "Confederal courts and civil administration in the compact territories", "1862-67", "CR-060 M4", "Budget", MEMO,
  "circuit courts in Montana and Idaho; the Salt Lake court; no Union revenue collected there", "PROPOSED", cites="CR-059 I8; CR-060 D5, U5")
r("M12", "Oregon's softened slump", "1865-66", "CR-059 Part V", "dynamic layer (Economy)", MEMO, "", "PROPOSED",
  "the draft flags it for the dynamic model layer")
r("M13", "Confederal grants to county boards", "1867 onward", "CR-059 S3", "Budget", MEMO, "no amounts", "PROPOSED", cites="CR-068 G10")
r("M14", "Defence organisation: annual estimates, General Staff, Navy Board, ranks", "1855 onward", "CR-067 A1", "Budget (structure)", MEMO,
  "no new sum; defence and navy are confederal items", "canon / PROPOSED", cites="CR-067 B2, B5, C2, C3; CR-064 H4")
r("M15", "The Chancellor's six months: no law in the interior", "Jun-Nov 1865", "CR-068 G9a", "Budget timing", MEMO,
  "pay and works delayed (no figure)", "APPROVED", cites="CR-068 B16a")
r("M16", "Guano islands and Midway added in the peace", "1865-67", "canon §12", "Resources", FIXU, "", "canon", cites="CR-062 X4, T7; CR-068 G6")
r("P01i", "South Park and the upper Arkansas (the 1865 Colorado line)", "1867", "CR-060 CO4", "census.toml Colorado (west of the line)", FIX,
  "small, 'almost empty'; the 25,000 of Union Colorado stay Union", "PROPOSED", domain="Population", cites="CR-062 T2")
r("P06", "The Chinese floor and Chinese migration into Oregon and Idaho", "1867 onward", "CR-059 S4", "flows.py", MEMO,
  "13 counted in 1860 (an undercount); 3,330 in 1870 (Hist.)", "PROPOSED", domain="Population", cites="CR-059 X5")
r("P07", "Entry controls: the Texas line closed to fugitives; extended to the railway and the Gulf ports", "1863; 1871-72", "CR-061 S4",
  "flows.py", FIX, "inflow across the line near zero from 1863", "APPROVED (CT9)", domain="Population",
  cites="CR-061 CT9; CR-062 T11; CR-059 S2; CR-068 CT18, CT25")
r("P08", "Assembly seats by population for the new members", "1867 onward", "CR-060 A5", "output use", MEMO, "", "PROPOSED",
  domain="Population", cites="CR-059 CT8, open 18")
r("P09", "Hawaii controls entry at its own ports", "1864 onward", "CR-068 CT8", "population: Hawaii arrivals", FIX,
  "kingdom-controlled entry and quarantine", "APPROVED", domain="Population", cites="CR-068 G8, TL6")
r("P10", "Displaced Unionists; residents' citizenship choice", "1863-68", "CR-062 T10", "population: small out-migration", MEMO,
  "Port Townsend's displaced Unionists (no number); one-year choice of citizenship", "PROPOSED", domain="Population",
  cites="CR-059 W11a; CR-068 G7")
r("G12", "The Columbia, the Snake and the routes into Idaho", "1861-67", "CR-059 Part V", "logistics/data/routes.toml", FIX,
  "OSN traffic 6,290 t (1861) to 21,834 t; three-fourths of Idaho's trains from California by Oct 1865", "Hist. / MODEL", domain="Logistics",
  cites="CR-059 I11")
r("G14", "Unit constants for wagon roads: payloads, rations, forage, prices", "1862-65", "CR-061 Part II", "logistics constants", FIX,
  "six-mule wagon 1,500-2,500 lb; 3 lb a man, 26 lb an animal a day", "Hist. / MODEL", domain="Logistics")
r("B01", "Pre-war baseline already in canon", "1846-58", "canon", "baseline check only", FIXU,
  "no US Army in California after 1846; coast survey 1849; Benicia, Mare Island, Carquinez foundries; regular army 1852; land warrants 1851; Hawaii's defence confederal from 1856; the pre-war fleet; Colorado River steamers",
  "canon", "check the workbook already carries these; the drafts change none", cites="CR-067 candidates; CR-064 H1, O3")
r("C01", "Colorado: the Colorado article and the transfers of 1875-82", "1865; 1875-82", "CR-060 CO5",
  "later round (after 1872)", "Later round",
  "supply and coin pledge to Union-side districts; Leadville; the Front Range votes; the narrow gauge; a smelter; the survey's compensation",
  "PROPOSED", cites="CR-060 CO6-CO9; CR-062 T10a")
r("Y01", "After 1872: the Freedom Act, Hawaii 1874-76, the Realm 1887, immigration 1888", "1873 onward", "canon", "later rounds", "Later round",
  "canon; the drafts only refer to it", "canon", cites="CR-068 K24, M15, TL6; CR-061 Part VII; CR-067 Dominis, Soberanes")
r("L17", "War bonds subscribed in coin from idle gold", "1861-65", "author 13 Nov 2026",
  "Sources & uses (new source); Gold & money", LEV,
  "a bounded share of notes and bank reserves (Gold & money I), never more than the gold above cover, may fund war bonds in coin 1861-65; 0.12 / 0.06 from the Union's 1861 bank loan (approved by the author, 14 Nov)",
  "APPROVED as a model rule (author, 13 Nov 2026, 22:56)", "changes the private-saving test: today it counts only current saving")
r("X05", "Union-side items with no Pacifican entry", "1846-72", "", "neighbours or none", NOTM,
  "pre-war Union harbour works and the Sausalito supply; the restoration programme; Union Colorado; the Pacific Railway and Homestead Acts",
  "", cites="CR-059 H7, W12, Part I; CR-060 CO4, CO6; CR-068 K7, CT20")

# ---------------------------------------------------------------- author's decisions, 13 November 2026
# "I approve all the recommendations, please make a reasonable assumption for Vicksburg."
D = "Decided (author, 13 Nov 2026): "
DECISIONS = {
    "P01":  (FIX, "Q1: every acceding territory enters the confederal count at the exchange of 1867"),
    "P01g": (FIX, "Q1, Q2: New Mexico with Arizona from 1867; no separate San Luis Valley line"),
    "P01c": (FIX, "Q3: a fixed estimate between the 1860 and 1870 censuses, stated; tested in phase 6"),
    "P01d": (FIX, "Q3: a fixed estimate between the 1860 and 1870 censuses, stated; tested in phase 6"),
    "P01e": (FIX, "Q3: a fixed estimate between the 1860 and 1870 censuses, stated; tested in phase 6"),
    "P01f": (FIX, "Q3: a fixed estimate between the 1860 and 1870 censuses, stated; tested in phase 6"),
    "P01h": (FIX, "Q3: a fixed estimate, stated; tested in phase 6"),
    "L07":  (FIX, "Q4: fixed by source: N-C from the 1851 and 1855 treaties' sums, N-B from what L08 pays"),
    "L13":  (LEV, "Q5: a lever replacing E14; party the Eastern houses and the transit companies"),
    "L14":  (FIX, "Q6: fixed at the historical award of 1869, $650,000 (to verify)"),
    "L15":  (FIX, "Q7: the new members' public land enters the Land Fund from 1867 under the existing member-state rules; the schools' share needs a number"),
    "L04":  (LEV, "Q8: a lever"),
    "L01m": (FIX, "Q9: Matamoros cargo is drawn on the Richmond credit (L01); only the missions' pay is a cost"),
    "F13":  (FIX, "Q10: credited against the $40m"),
    "F14":  (FIX, "Q10: credited against the $40m"),
    "F08":  (FIXU, "Q11 approved as 'drop E20', withdrawn by the drafter in phase 4: canon §13 (CR-039) says 'Pacifica replaces the surrendered toll revenue', so E20 stays; dropping it needs a canon tension"),
    "F15":  (FIX, "Q12: E13 switched off in the build; Baja tested as a separate case"),
    "L11":  (LEV, "Q13: a lever with the rejected 1863 constitution's rate as its ceiling (research needed)"),
    "L16":  (DEF, "Q14: carried at zero behind a switch"),
    "C01":  ("Later round", "Q15: not in this round"),
    "Y01":  ("Later round", "Q15: not in this round"),
    "F12":  (FIX, "the held territories pay the 5% royalty on their gold from 1863, as a fee for assay and coinage (author, 13 Nov 2026, 22:56)"),
    "P04":  (FIX, "Vicksburg (drafter's assumption at the author's request): CR-063 Part III's numbers: about 30,000 inside, 12,500 escape on 17-18 May, about 1,500 lost in the siege, about 15,000 surrender about 4 July"),
}
for x in R:
    if x["rid"] in DECISIONS:
        x["cls"], why = DECISIONS[x["rid"]]
        x["note"] = (x["note"] + " | " if x["note"] else "") + D + why

# ---------------------------------------------------------------- crosswalk: (CR, ID) -> register row
M = {}
def m(cr, ids, rid):
    for i in ids.split():
        M[(cr, i)] = rid
m("CR-059", "P1", "N02"); m("CR-059", "P2 P3 P4 P5 P6 P7 P8 P9", "M10"); m("CR-059", "P10", "L14"); m("CR-059", "P11 E2", "L06")
m("CR-059", "W1 W2 W3 W4 W5 W14", "L03a"); m("CR-059", "W15", "L03a"); m("CR-059", "W6", "F11"); m("CR-059", "W7", "L12")
m("CR-059", "W8", "G01"); m("CR-059", "W9", "L10"); m("CR-059", "W13", "G08")
m("CR-059", "I1", "M05"); m("CR-059", "I2", "L03a"); m("CR-059", "I3", "F13"); m("CR-059", "I4", "M02"); m("CR-059", "I5", "G03")
m("CR-059", "I6", "F12"); m("CR-059", "I7", "L08b"); m("CR-059", "I9 I10", "P01c"); m("CR-059", "V9", "L15"); m("CR-059", "V10 V16", "L15")
m("CR-059", "V15", "P01a"); m("CR-059", "V17", "P01b"); m("CR-059", "V1", "F04"); m("CR-059", "X1 X2 X3 X4 X5 X6 X7 X8", "P05")
m("CR-059", "N-A N-D N-E N-F N-G N-H N-I", "L08a"); m("CR-059", "N-B", "L07"); m("CR-059", "N-C", "L07"); m("CR-059", "S5", "L08a"); m("CR-059", "S6", "N03")
m("CR-060", "U1 U2 U3 U4", "G05"); m("CR-060", "D4", "L03b"); m("CR-060", "D4a", "G09"); m("CR-060", "D7", "L16")
m("CR-060", "D8 D9", "L08b"); m("CR-060", "D12 A1 A4", "P01e"); m("CR-060", "C1", "F12"); m("CR-060", "C5", "L03b"); m("CR-060", "C6 C7", "L03b")
m("CR-060", "C8", "L11"); m("CR-060", "C11 A2", "P01d"); m("CR-060", "M1", "M01"); m("CR-060", "M2", "F12"); m("CR-060", "M6", "G10")
m("CR-060", "M7 A3", "P01f"); m("CR-060", "M8 M9 M10", "L08b"); m("CR-060", "R1", "L03b"); m("CR-060", "R2", "L12"); m("CR-060", "R3 R4", "L08b")
m("CR-060", "CO2", "F12"); m("CR-060", "CO3", "L03c"); m("CR-060", "N1 N2 N3 N4 N5 N6 N7 N8", "L08b"); m("CR-060", "S1 S2 S3", "L03b"); m("CR-060", "S4", "G05")
m("CR-061", "C1 C3 C9 C10 C13 C2", "L03c"); m("CR-061", "C4 C5", "G06"); m("CR-061", "C6", "L08c"); m("CR-061", "C8", "L01")
m("CR-061", "L1 L3 L4 L5", "L03c"); m("CR-061", "L2", "G06"); m("CR-061", "F1", "G04"); m("CR-061", "F3 F4 F5 F7 F8 F9", "L03c")
m("CR-061", "F6", "M06"); m("CR-061", "K3", "L15"); m("CR-061", "K4 A1 A2", "F10"); m("CR-061", "K6", "P02"); m("CR-061", "A3", "L03c")
m("CR-061", "A4 K1 P5", "P01g"); m("CR-061", "N1 N2 N3 N5 N6 N7", "L08c"); m("CR-061", "N4", "N04"); m("CR-061", "P1 P2", "L03c")
m("CR-061", "P3", "M07"); m("CR-061", "M1", "L09"); m("CR-061", "M2", "M08")
m("CR-062", "A1 A6", "F02"); m("CR-062", "A2 A3 A4", "L01"); m("CR-062", "A5", "L01m"); m("CR-062", "T3", "F13"); m("CR-062", "T4 S2 S4 X1 O7 M1", "F04")
m("CR-062", "T5 T6", "M07"); m("CR-062", "T9", "M04"); m("CR-062", "T12", "L07"); m("CR-062", "T14 X3", "M03"); m("CR-062", "K3 K10 M4 X5", "F05")
m("CR-062", "K7 K8", "P01h"); m("CR-062", "S10 L1 M3", "L13"); m("CR-062", "X2", "F14"); m("CR-062", "M2", "L05"); m("CR-062", "M5", "L09"); m("CR-062", "M6", "F15")
m("CR-062", "Washington_Ter", "P01b"); m("CR-062", "Idaho", "P01c"); m("CR-062", "Washoe", "P01d"); m("CR-062", "Deseret", "P01e")
m("CR-062", "Western_Montan", "P01f"); m("CR-062", "New_Mexico The_San_Luis_V Arizona", "P01g")
m("CR-063", "N1 N2 N3 V1 V2 V3 V4 V5 V6 T6", "P04"); m("CR-063", "S1 S2 S3 S4 S5 S6 T1 T2 T3 T5 F1 F2 F3 M1 M2 M3 M4 M5 M6 M7", "X03")
m("CR-063", "T4 X2", "G07"); m("CR-063", "X1 L1 L2", "L01m"); m("CR-063", "X3 X4", "L01")
m("CR-064", "S8 S3", "P04"); m("CR-064", "S5 S7 A1 A7 A10 A12", "P04"); m("CR-064", "A4 A6 A13", "G11")
m("CR-065", "W4", "P04"); m("CR-065", "F1 F2 F3 F4 F5", "X02"); m("CR-065", "P2", "L03a")
m("CR-067", "B1", "F03"); m("CR-067", "A4", "X01"); m("CR-067", "B6 C4 California_(th The_Hawaiian_I", "L03d"); m("CR-067", "B7", "L03")
m("CR-067", "The_Columbia_(", "L03a"); m("CR-067", "The_Great_Basi", "L03b"); m("CR-067", "The_Rio_Grande", "L03c"); m("CR-067", "Missions_abroa", "L01m")
m("CR-068", "G3_The_river's PP4c B8 B11", "L01"); m("CR-068", "G5_The_refuge B10 PP5", "L12"); m("CR-068", "July_1861", "L02")
m("CR-068", "G11_The_credit PP13", "L13"); m("CR-068", "TL5 B4 B15", "G01"); m("CR-068", "K11", "F16"); m("CR-068", "K21", "F08"); m("CR-068", "K23", "F09")
m("CR-060", "R5", "P01g"); m("CR-064", "C5", "P04")

# the items each draft lists under "Financial and population models" (and CR-068's "For integration")
MODEL_ITEMS = [
    ("CR-059", "the Oregon customs account (W6)", "F11"), ("CR-059", "gold requisitions (W5)", "L03a"),
    ("CR-059", "the Lewiston lease rent", "M05"), ("CR-059", "the 1862-66 annuities and their credit (N-B)", "L08a"),
    ("CR-059", "the deduction for the unratified treaties (N-C)", "L07"), ("CR-059", "the scrip purchase and set-off (P11)", "L06"),
    ("CR-059", "Oregon's customs share", "L15"), ("CR-059", "the promised works (V9)", "L10"),
    ("CR-059", "the Sacramento line to the Siskiyous (W9)", "L10"), ("CR-059", "the 1863-65 refugees (W7)", "L12"),
    ("CR-059", "Oregon and Idaho joining the confederal population from 1867", "P01a"),
    ("CR-060", "Deseret's wheat bought in gold, 1862-67", "L03b"), ("CR-060", "the Legion's pay (held pending CT7)", "L16"),
    ("CR-060", "the road garrison's California freight", "L03b"), ("CR-060", "the Fort Churchill withdrawal's keep (against the vendor credit, OPEN)", "F14"),
    ("CR-060", "Washoe's net-proceeds tax", "L11"), ("CR-060", "the Idaho and Montana assay offices", "M01"),
    ("CR-060", "Washoe, Deseret and western Montana join the confederal population on exchange in 1867", "P01"),
    ("CR-061", "the garrison's cost (pay, coin for local purchase, the road)", "L03c"), ("CR-061", "the Pima compact", "L08c"),
    ("CR-061", "compensation for peon debts and released captives (A2)", "F10"),
    ("CR-061", "the Navajo and Apache annuities and scouts' pay", "L08c"), ("CR-061", "the Juárez credit's New Mexican deliveries", "L09"),
    ("CR-061", "New Mexico's population entering the confederal count from 1867", "P01g"),
    ("CR-062", "the $40m schedule (M2)", "L05"), ("CR-062", "the 1867 deposit", "F04"), ("CR-062", "the set-offs as credits", "L06"),
    ("CR-062", "the Treasury loan as a separate line", "L13"), ("CR-062", "Alaska's $7.2m in 1867", "F05"),
    ("CR-062", "the Sitka garrison and the northern mail", "L04"), ("CR-062", "Baja kept separate and optional", "F15"),
    ("CR-062", "the Juárez credit's amount is not stated", "L09"), ("CR-062", "Alaska's residents from 1867", "P01h"),
    ("CR-063", "the Pensacola brigade's size and supply (MIL-01)", "X03"), ("CR-063", "the armour programme's allocation", "X03"),
    ("CR-063", "the February 1865 shipping, coal and troop numbers", "X03"), ("CR-063", "Pacifica's Matamoros cargo by value", "L01m"),
    ("CR-064", "nothing touches Pacifica's workbook", "Z64"), ("CR-065", "the Union's war finance: named, not modelled", "X02"),
    ("CR-068", "CT26: the workbook's order of repayment (London first)", "F01"),
    ("CR-068", "CT28: the war credit of 1862-65 as a loan event (E09; E19)", "L01"),
    # sources outside the decision tables
    ("CR-068", "[text] CT28: refinancing of 1871-72 on customs security", "F06"),
    ("CR-068", "[text] CT28: guarantor of the 1888-89 bonds; takes $6m", "F07"),
    ("CR-068", "[text] CT28: Richmond's own London debt", "X04"),
    ("CR-062", "[text] Part II: mutual waiver of war claims", "M09"),
    ("CR-061", "[text] Part I: the second Valverde and the campaign's losses", "P03"),
    ("CR-060", "[text] C5: Washoe retaken April 1864 (the Comstock's load)", "N01"),
    ("CR-059", "[text] Part V: the Columbia inside the confederation from 1867", "N05"),
    ("CR-060", "[text] Part V: the Salt Lake road's arithmetic", "G02"),
    ("CR-061", "[text] models: the Navajo and Apache annuities (parent lever)", "L08"),
]

DEFAULT = {"CR-059": "Z59", "CR-060": "Z60", "CR-061": "Z61", "CR-062": "Z62", "CR-063": "Z63", "CR-064": "Z64",
           "CR-065": "Z65", "CR-067": "Z67", "CR-068": "Z68"}

def rows():
    files = [(cr, REV / f"{cr}.md") for cr in CRS] + [("CR-068", REV / "CR-068-lincoln-career.md")]
    for cr, f in files:
        sec = None
        for n, line in enumerate(f.read_text().split("\n"), 1):
            if line.startswith("## "):
                sec = line[3:].strip()
            if f.name.startswith("CR-068-lincoln") or sec == "Decisions":
                if line.startswith("|") and not re.match(r"^\|\s*-", line):
                    cells = [c.strip() for c in line.strip().strip("|").split("|")]
                    rid = re.sub(r"\*\*", "", cells[0])[:14].replace(" ", "_")
                    if rid in SUBHEADERS:
                        continue
                    if f.name.startswith("CR-068-lincoln") and not re.match(r"K\d", rid):
                        continue
                    text = re.sub(r"\*\*", "", " | ".join(cells[1:]))
                    yield cr, f.name, n, rid, text

def main():
    ids = {x["rid"] for x in R}
    bad = [v for v in M.values() if v not in ids]
    assert not bad, bad
    xw = []
    used = set()
    for cr, fname, n, rid, text in rows():
        key = (cr, rid)
        dest = M.get(key, DEFAULT[cr])
        used.add(key)
        xw.append(dict(cr=cr, file=fname, line=n, row_id=rid, register=dest, text=text[:160]))
    for k, (cr, text, dest) in enumerate(MODEL_ITEMS, 1):
        xw.append(dict(cr=cr, file=f"{cr}.md", line="", row_id=f"models:{k}", register=dest, text=text))
    missing = [k for k in M if k not in used]
    if missing:
        sys.exit(f"mapped ids not found in the drafts: {missing}")
    with open(OUT / "crosswalk.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(xw[0]))
        w.writeheader(); w.writerows(xw)
    count = {}
    for x in xw:
        count[x["register"]] = count.get(x["register"], 0) + 1
    for x in R:
        x["rows"] = count.get(x["rid"], 0)
    with open(OUT / "register.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(R[0]))
        w.writeheader(); w.writerows(R)
    print(f"{len(xw)} decision rows -> {len({x['register'] for x in xw})} register rows used of {len(R)}")
    by = {}
    for x in R:
        by[x["cls"]] = by.get(x["cls"], 0) + 1
    print(by)

if __name__ == "__main__":
    main()
