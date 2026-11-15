"""Enter CR-059 to CR-070 into the commitments ledger (adoption of 15 November 2026).

Amends existing entries in place (stable IDs) and appends a new part with the new
parties and commitments. Every quote is the new master_storyline.md's text; the
status and section of each new entry are read from the storyline at its quote, as
ledger.py check requires. Run from the repository root:

  python3 outputs/sessions/20261115-integration/ledger_integration.py
  python3 commitments/ledger.py check
"""
from __future__ import annotations

import json
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
LEDGER = ROOT / "commitments" / "data" / "ledger.toml"
sys.path.insert(0, str(ROOT / "commitments"))
import ledger as L  # noqa: E402

ORDER = ["id", "name", "kind", "parties", "from", "from_approx", "until", "term_years", "renewals",
         "ended", "ended_by", "lapses_on_death", "holder", "owes", "secured_on", "can_end",
         "conditions", "status", "cr", "section", "quote", "more_quotes", "label_note", "open"]


def s(v: str) -> str:
    return json.dumps(v, ensure_ascii=False)


def val(v) -> str:
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, int):
        return str(v)
    if isinstance(v, str):
        return s(v)
    if isinstance(v, list):
        if not v:
            return "[]"
        if all(isinstance(x, int) for x in v):
            return "[" + ", ".join(str(x) for x in v) + "]"
        if all(isinstance(x, str) for x in v) and sum(len(x) for x in v) < 60:
            return "[" + ", ".join(s(x) for x in v) + "]"
        items = []
        for x in v:
            if isinstance(x, dict):
                items.append("  { " + ", ".join(f"{k} = {val(y)}" for k, y in x.items()) + " },")
            else:
                items.append("  " + val(x) + ",")
        return "[\n" + "\n".join(items) + "\n]"
    raise TypeError(v)


def dump(c: dict) -> str:
    keys = [k for k in ORDER if k in c] + [k for k in c if k not in ORDER]
    return "[[commitment]]\n" + "\n".join(f"{k} = {val(c[k])}" for k in keys) + "\n"


def dump_party(p: dict) -> str:
    return f"[[party]]\nid = {s(p['id'])}\nname = {s(p['name'])}\n"


# ---------------------------------------------------------------------------
# Block editing
# ---------------------------------------------------------------------------

def blocks(lines: list[str]) -> dict[str, tuple[int, int]]:
    """id -> (start, end) line indexes of each [[commitment]] block, trailing
    blank and comment lines excluded."""
    out = {}
    starts = [i for i, l in enumerate(lines) if l.startswith("[[")]
    for n, st in enumerate(starts):
        if lines[st].strip() != "[[commitment]]":
            continue
        end = starts[n + 1] if n + 1 < len(starts) else len(lines)
        while end > st and (not lines[end - 1].strip() or lines[end - 1].lstrip().startswith("#")):
            end -= 1
        text = "\n".join(lines[st:end])
        cid = tomllib.loads(text)["commitment"][0]["id"]
        out[cid] = (st, end)
    return out


# ---------------------------------------------------------------------------
# Amendments to existing entries
# ---------------------------------------------------------------------------

def amend(c: dict) -> dict:
    cid = c["id"]
    f = AMEND.get(cid)
    return f(dict(c)) if f else c


def a_london(c):
    c["more_quotes"] = [q for q in c["more_quotes"] if "credit was not extended" not in q] + [
        "In 1859 the Republic repays the London bondholders in full, and the pledge of its gold royalties and of San Francisco's customs ends.",
    ]
    c["ended"] = 1859
    c["ended_by"] = "repaid in full in 1859, ending the pledge of the gold royalties and San Francisco's customs (CR-068 CT26)"
    c["open"] = ("Valuation and interest not stated (left to financial modelling). Repaid in full in 1859 "
                 "(APPROVED — CR-068); no bondholders stand behind Britain in 1860.")
    return c


def a_deseret(c):
    return {
        "id": "C-1862-DESERET",
        "name": "Association of Deseret: the working articles of 1862 and the Compact of Association of 1863",
        "kind": "compact",
        "parties": ["PAC", "DESERET"],
        "from": 1862,
        "ended": 1867,
        "ended_by": "Deseret's accession on the exchange of ratifications in 1867 (C-1866-DESERET-CHARTER)",
        "owes": [
            {"by": "PAC", "to": "DESERET", "what": "the Protector's pledge that the Union's law will not be enforced in Deseret by arms"},
            {"by": "PAC", "to": "DESERET", "what": "published terms of passage; Deseret's courts and church property left alone; Deseret's wheat bought in gold"},
            {"by": "PAC", "to": "DESERET", "what": "the garrison's posts named at the old Camp Floyd, the Bear River crossing and Fort Bridger, none within a day's ride of the city"},
            {"by": "DESERET", "to": "PAC", "what": "supply of the road and passage to the interior campaigns; Lot Smith's cavalry and the Nauvoo Legion bound to the common defence of the roads and the valley"},
            {"by": "PAC", "to": "DESERET", "what": "a confederal travellers' court for crimes on the roads, extended by the Compact to crimes of any date"},
        ],
        "conditions": [
            "the working articles of December 1862 run to the end of 1863 at the latest and promise nothing against the Union's law; the Compact of 24 July 1863 replaces them",
            "an agreement about passage, supply and defence under the Protector's mandate, not an annexation; membership waits for the peace",
        ],
        "status": "PROPOSED",
        "section": 10,
        "cr": "CR-060",
        "quote": "In December 1862, while Elias is in New Mexico, his commissioners and Young's counsellors sign working articles for passage, supply, the garrison's posts and a confederal court for crimes against travellers on the roads.",
        "more_quotes": [
            "The articles run to the end of 1863 at the latest and promise nothing against the Union's law.",
            "On the 24th, the anniversary of the Saints' arrival in the valley, the Legion parades, and he and Young sign the Compact of Association, an agreement about passage, supply and defence under the Protector's mandate, not an annexation.",
            "Pacifica will not suffer the Union's law to be enforced in Deseret by arms.",
            "It publishes its terms of passage, leaves Deseret's courts and church property alone and buys Deseret's wheat in gold.",
            "Deseret supplies the road, gives passage to the interior campaigns, and binds Lot Smith's cavalry and the Nauvoo Legion to the common defence of the roads and the valley.",
            "At Elias's demand the Compact extends the travellers' court to crimes on the roads of any date.",
            "The garrison's posts are named, the old Camp Floyd, the Bear River crossing and Fort Bridger, none within a day's ride of the city.",
            "Membership waits for the peace.",
        ],
        "open": ("CR-060 CT1 (decided): association from December 1862, accession in 1867. The Legion's "
                 "ride to Bannack in 1864 is Young's own decision beyond the roads the Compact binds it to "
                 "keep, paid after the peace; it is no term of the Compact."),
    }


def a_matamoros(c):
    c["name"] = "Matamoros supply route"
    c["owes"] = [{"by": "PAC", "to": "CSA", "what": "credit, coin and specialist goods (rifles, machine tools, fuzes, primers and mine gear) and men, around Cape Horn to neutral Matamoros and overland into Texas; no bulk"}]
    c["conditions"] = ["arms and missions suspended by the 1865 armistice while the Union's armistice with Richmond holds; commerce and commercial credit continue (CR-062)"]
    c["more_quotes"] = [
        "Pacifican coin, rifles, machine tools, fuzes, primers, mine gear and men travel around Cape Horn to neutral Matamoros and overland into Texas and across Louisiana to the river.",
        "The armistice with Pacifica carries one public term on the South: while the Union's armistice with Richmond holds, Pacifica sends no military mission and no arms to the Confederacy.",
    ]
    c["open"] = ("The credit itself is C-1863-RICHMOND-CREDIT (CR-068). The flag of the ships (Pacifican or "
                 "neutral) is not stated. 'No bulk' is CR-063's reading of the goods named. Alliance terms with Richmond are **[OPEN]**.")
    return c


def a_navajo(c):
    c.pop("from_approx", None)
    c["name"] = "Navajo homeland treaty"
    c["from"] = 1865
    c["status"] = "APPROVED"
    c["cr"] = "CR-015"
    c["owes"] = [
        {"by": "PAC", "to": "NAVAJO", "what": "recognition of a homeland; no Long Walk"},
        {"by": "PAC", "to": "NAVAJO", "what": "the return of the Navajo held in New Mexican households: grown captives choose, a joint commission decides for the children, and Pacifica pays each household that releases one"},
    ]
    c["quote"] = "In Navajo country the government chooses a different course."
    c["more_quotes"] = [
        "In 1865 a treaty recognizes the Navajo homeland.",
        "Barboncito and Manuelito negotiate that settlement",
        "the Navajo homeland treaty of 1865 also returns the Navajo held in New Mexican households: grown captives choose whether to go home, a joint commission decides for the children, and Pacifica pays each household that releases one.",
    ]
    c["open"] = ("Boundaries not stated. Kit Carson sits as the Rio Grande compact's commissioner, not Pacifica's "
                 "(APPROVED — CR-061). The Cubero agreement of 1863 is C-1863-NAVAJO-PASSAGE.")
    return c


def a_apache(c):
    c["section"] = 12
    c["owes"] = c["owes"] + [{"by": "PAC", "to": "APACHE", "what": "passage money for the Chiricahua from the Sunset road's customs"}]
    c["more_quotes"] = [
        "At Santa Rita del Cobre, where he had met Kearny twenty years before, Mangas Coloradas brings his son-in-law Cochise to the table.",
        "The Chiricahua take passage money from the Sunset road's customs",
    ]
    c["open"] = ("Boundaries and term not stated; the Mescalero's joining and the Chihenne bounds (CR-061 N4, N7) "
                 "are not in the storyline. The copper lease is C-1865-SANTA-RITA.")
    return c


def a_scalp(c):
    c["section"] = 12
    c["more_quotes"] = ["The end of the bounties is the price Mangas asks."]
    c["open"] = ("Year not stated beyond following the 1865 Apache peace. CR-061 calls it the convention of Paso "
                 "del Norte, with a second article for the west-bank crossing; the crossing's customs post "
                 "'agreed with Mexico' is recorded under C-1867-JUAREZ-CREDIT.")
    return c


def a_hi_guar(c):
    c["status"] = "APPROVED"
    c["cr"] = "CR-068"
    c["owes"] = [{"by": "PAC", "to": "HI", "what": "protection of Hawaiian kingship, the Kuhina Nui, local institutions and agreed revenues, as protected provisions that cabinet legislation may not touch"}]
    c["quote"] = "The form of the law and the protection of Hawaiian kingship, the Kuhina Nui and local institutions were promised by the Council's resolution of November 1864."
    c["more_quotes"] = [
        "Hawaii now bargains for the agreed revenues and for the list of protected provisions that cabinet legislation may not touch, and wins both.",
        "The cabinet may legislate around specified provisions, but the Hawaiian crown, Kuhina Nui and local institutions are protected.",
        "The guarantees become protected provisions of the Enabling Law, whose later breach cannot be justified by the authority it grants.",
    ]
    c["open"] = ("Promised by the Council's resolution of 12 November 1864 (CR-068) and won at Monterey in the summer "
                 "of 1865. The amount of the agreed revenues and whether the guarantees survive the 1887 lapse of the "
                 "enabling delegation are not stated.")
    return c


def a_fugitive(c):
    c["name"] = "Fugitive agreement with Richmond"
    c.pop("from_approx", None)
    c["from"] = 1863
    c["owes"] = [
        {"by": "PAC", "to": "CSA", "what": "fugitives refused at the crossings of the Texas line, by travel-paper controls extended in 1871–1872 to the railway and the Gulf ports; Texas may police its own side"},
    ]
    c["conditions"] = [
        "no one who has reached Pacifican soil is returned; Richmond's requests for return are refused every year",
        "a slave whom a master brings onto Pacifican soil is free",
    ]
    c["quote"] = "Pacifica enforces a fugitive agreement with Richmond from 1863 until abolition in 1888–1889, preventing enslaved people from escaping to Pacifican territory; it closes the border and returns no one who has reached Pacifican soil."
    c["more_quotes"] = [
        "a fugitive is refused at the crossings of the Texas line, and Texas may police its own side; but one who reaches Pacifican soil is free and is not given up",
        "The association treaties of 1871–1872 extend the travel-paper controls that have closed the Texas line since 1863 to the railway and the Gulf ports.",
        "Richmond asks for the return of those who get through and is refused, as Texas has been every year since 1863.",
        "Confederate abolition in 1888–1889 ends the fugitive agreement",
    ]
    c["open"] = ("Made as an article of the Sunset articles at San Antonio in February 1863 (C-1863-ARIZONA; CR-061 "
                 "CT9) and extended in 1871–1872 (CR-068). The ID keeps its old year for stability. End given as "
                 "1888–1889; `ended` uses the later year.")
    return c


def a_seal(c):
    c["from"] = 1886
    c["cr"] = "CR-058"
    c["owes"] = [
        {"by": "PAC", "to": "CA", "what": "fifteen percent of the Pribilof catch"},
        {"by": "RU", "to": "CA", "what": "fifteen percent of the Commander Islands' catch, 1886–1921"},
        {"by": "PAC", "to": "CA", "what": "from 1921, with the Commander Islands, fifteen percent of their catch"},
        {"by": "JP", "to": "CA", "what": "ten percent of Robben Island's catch"},
    ]
    c["conditions"] = ["pelagic sealing banned"]
    c["quote"] = "the four-power convention, which bans pelagic sealing and gives Canada fifteen percent of the Pribilof catch, fifteen percent of the Commander Islands' and ten percent of Robben Island's."
    c["more_quotes"] = [
        "in 1884, when the sealing schooners first reach the Bering Sea,",
        "it proposes a conservation regime and seats Canadian delegates at the table.",
        "In 1886 Pacifica, Britain for Canada, Russia and Japan sign",
    ]
    c["open"] = ("Signed 1886 (APPROVED — CR-070); the ID keeps its old year for stability. Term and renewals not "
                 "stated. The Commander Islands pass to Pacifica in 1921 (CR-031).")
    return c


def a_protector(c):
    c["ended"] = 1865
    c["ended_by"] = "expires with its term on the last day of May 1865; the renewal of 1864 is the last (CR-068)"
    c["conditions"] = c["conditions"] + [
        "Hawaii's conditions for the third renewal (1864): no annexation, the Carson Convention's guarantees kept, and Hawaii's control of entry at its own ports",
    ]
    c["more_quotes"] = c["more_quotes"] + [
        "The Protectorship takes effect on 1 June 1861, and each yearly term ends on 31 May.",
        "Victoria writes Hawaii's conditions into its assent to the third renewal: no annexation, the Carson Convention's guarantees kept, and Hawaii's control of entry at its own ports.",
        "The renewal of 1864 is the last.",
        "On the last day of May 1865 the Protectorship expires with its term.",
    ]
    c["open"] = ("In force 1 June 1861 to 31 May 1865 (APPROVED — CR-068). Exact instruments **[OPEN]**. After the "
                 "lapse Elias governs for six months as Chancellor under the Articles of 1856 until the Enabling Law "
                 "is in force on 1 December 1865.")
    return c


def a_peace(c):
    c["conditions"] = c.get("conditions", []) + ["free navigation of the Mississippi is Pacifica's condition for its guarantee (CR-068 K21)"]
    c["more_quotes"] = c.get("more_quotes", []) + ["Free navigation of the Mississippi is Pacifica's condition for that guarantee."]
    return c


def a_western(c):
    c["name"] = "Western treaty (the Western line of the 1865 peace)"
    c["owes"] = [
        {"by": "US", "to": "PAC", "what": "cession of the Northwest, Great Basin, Arizona, Utah, Nevada, Idaho, western Montana, southwest Wyoming, Colorado's Western Slope, North and Middle Park, the San Luis Valley and New Mexico to 103°W; Oregon as Oregon's voters choose"},
        {"by": "US", "to": "PAC", "what": "evacuation of Port Townsend and Fort Union after the exchange; the surviving Puget Sound enclave evacuated"},
        {"by": "PAC", "to": "US", "what": "a $40 million gold vendor credit in six instalments from the exchange (see C-1867-VENDOR-CREDIT)"},
        {"by": "PAC", "to": "US", "what": "the Union's merchants keep the Columbia and Puget Sound on published terms; its warships may come in for refuge or repair; no storehouse is granted"},
        {"by": "PAC", "to": "US", "what": "named roads open from Fort Benton to Helena, from Denver to Salt Lake and from Denver over Raton Pass to Santa Fe; the Santa Fe Trail open to the Union's freighters under published duties"},
        {"by": "PAC", "to": "US", "what": "the Colorado article: any mountain mining district may vote itself over, and Pacifica supplies and coins it either way"},
        {"by": "US", "to": "PAC", "what": "the Colorado article: transit through Denver"},
        {"by": "PAC", "to": "US", "what": "every resident of a ceded district may choose either citizenship and keeps property, courts and civil protection without distinction of colour"},
    ]
    c["conditions"] = [
        "federal cession does not settle Native title or consent",
        "both governments waive their war claims; private claims go to a mixed commission (C-1867-WESTERN-CLAIMS)",
        "the treaty says nothing about fugitives, names no government south of its line and touches no claim of the Union to the South; it cedes territories, not states",
        "the Oregon protocol signed with the treaty: a Union Oregon would be disarmed and Pacifica would pay less; spent by Oregon's choice of October 1866 (C-1866-OR-CERTIFICATION)",
        "separated from executive recognition of Richmond, which the Senate never ratifies",
        "north of the Columbia no vote is owed; Washington Territory accedes by its convention's charter as the member Columbia (C-1866-WA-CHARTER)",
    ]
    c["quote"] = "The Western line is agreed in the 1865 peace and ratified by the Union Senate in 1867, alongside Pacifica's Alaska purchase."
    c["more_quotes"] = [
        "The Western treaty is signed at Washington in the third week of December 1865, under the full powers of the office the Enabling Law created on the first of the month.",
        "The Union is to evacuate Port Townsend and Fort Union after the exchange, and Pacifica is to pay a vendor credit of $40 million in gold in six instalments from the exchange.",
        "Its merchants keep the Columbia and Puget Sound on published terms; its warships may come in for refuge or repair, and no storehouse is granted anywhere.",
        "Named roads stay open from Fort Benton to Helena, from Denver to Salt Lake and from Denver over Raton Pass to Santa Fe.",
        "Every resident of a ceded district may choose either citizenship and keeps property, courts and civil protection without distinction of colour.",
        "The treaty says nothing about fugitives.",
        "The treaty cedes territories, not states.",
        "The Colorado article lets any mountain mining district vote itself over, binds Pacifica to supply and coin it either way and binds the Union to transit through Denver.",
        "Oregon it cedes as Oregon's voters shall choose, and the terms of the choice stand in a protocol signed with the treaty by Vallejo and Sherman: a Union Oregon would be disarmed, and Pacifica would pay less.",
        "North of the river no vote is owed: the Union made Washington Territory no offer of statehood",
        "The Senate consents on 9 April and, taking that advice, declines the separate Treasury loan by resolution.",
        "The ratifications are exchanged at Washington that summer, and the first payment is released.",
        "The Santa Fe Trail stays open to the Union's freighters under published duties.",
        "The surviving Puget Sound enclave is evacuated under the treaty, leaving the Union without a Pacific port.",
        "Senate ratification of the paid Western cession is separated from executive recognition of Richmond, which the Senate never ratifies.",
        "Its Senate recognizes the Confederacy and Gulf Republic and renounces the surviving claims under the 1865 and 1871 lines; the paid Western cession had already been ratified in 1867.",
    ]
    c["open"] = ("Signed December 1865 at Washington (PROPOSED — CR-062); the Senate consents on 9 April 1867 and the "
                 "ratifications are exchanged that summer (from = the exchange). Detailed boundary surveys are "
                 "**[PROPOSED]**; the Colorado districts' votes of 1878–1880 and the survey of 1880–82 are in §19. "
                 "The Union's Secretary of State is **[OPEN]**. CR-059's succession article (N-B) and the deduction "
                 "for the unratified treaties (N-C) are not stated in the storyline.")
    return c


def a_armistice(c):
    c["owes"] = [
        {"by": "PAC", "to": "US", "what": "no military mission and no arms to the Confederacy while the Union's armistice with Richmond holds"},
    ]
    c["conditions"] = c["conditions"] + [
        "Pacifica's war advances to Richmond end with the armistice; Washington's request to ban commercial credit as well is refused",
        "the armistice line at Glorieta holds until the exchange, and the Union keeps Las Vegas, Mora and Fort Union",
    ]
    c["more_quotes"] = c["more_quotes"] + [
        "The armistice with Pacifica carries one public term on the South: while the Union's armistice with Richmond holds, Pacifica sends no military mission and no arms to the Confederacy.",
        "It is signed in mid-May 1865, some weeks after Richmond's, by Elias as Protector.",
        "Washington asks for a ban on commercial credit as well, and Elias refuses",
        "Until the exchange the armistice line at Glorieta holds, and the Union keeps Las Vegas, Mora and Fort Union.",
    ]
    c["open"] = ("Pacifica's convention is signed in mid-May 1865 (PROPOSED — CR-062) and gives way to the Western "
                 "treaty on the exchange of 1867 (the line at Glorieta holds 'until the exchange'). The Oregon "
                 "protocol is signed with the Western treaty (C-1867-WESTERN-LINE). The Union–Richmond armistice's end "
                 "is not stated.")
    return c


def a_vendor(c):
    c["owes"] = [{"by": "PAC", "to": "US", "what": "$40 million in gold in six instalments from the exchange of 1867, through 1872"}]
    c["more_quotes"] = [
        "Pacifica is to pay a vendor credit of $40 million in gold in six instalments from the exchange.",
        "Before the vote the first instalment lies counted in gold in the New York Subtreasury, to be released on the exchange.",
        "The ratifications are exchanged at Washington that summer, and the first payment is released.",
        "The Senate consents on 9 April and, taking that advice, declines the separate Treasury loan by resolution.",
    ]
    c["open"] = ("First instalment 1867, at the exchange; the split between instalments is **[OPEN]**; set-offs "
                 "(CR-059, CR-062) are not stated in the storyline. The separate Treasury loan is declined by the "
                 "Senate; the money is lent privately through Ralston's bank (C-1862-COIN-BONDS).")
    return c


def a_alaska(c):
    c["owes"] = [
        {"by": "RU", "to": "PAC", "what": "Russia's claim to Russian America (Alaska)"},
        {"by": "PAC", "to": "RU", "what": "$7.2 million in Pacifica's own gold, paid at handover"},
        {"by": "PAC", "to": "RU", "what": "the Russian subjects may leave or stay; the Orthodox Church keeps its property; the Creoles of Sitka and Kodiak become Pacifican citizens"},
    ]
    c["conditions"] = ["the lands and rights of the Aleut, the Alutiiq, the Tlingit and the other nations are left to their own arrangements"]
    c["more_quotes"] = [
        "Pacifica's envoy offers $7.2 million in Pacifica's own gold, paid at handover rather than when a legislature agrees.",
        "The treaty is signed at St Petersburg early in March 1867, and the cable has the news in Washington within the day.",
        "The treaty transfers Russia's claim and leaves the lands and rights of the Aleut, the Alutiiq, the Tlingit and the other nations to their own arrangements; Victoria will not have it otherwise.",
        "The flag changes at Sitka in October 1867.",
        "The Russian subjects may leave or stay, the Orthodox Church keeps its property, and the Creoles of Sitka and Kodiak become Pacifican citizens.",
    ]
    c["open"] = ("Signed at St Petersburg in March 1867; handover at Sitka in October 1867 (PROPOSED — CR-062). The "
                 "price is the envoy's offer; CR-062's non-alienation pledge (K4) is not stated in the storyline.")
    return c


def a_juarez(c):
    c["from"] = 1865
    c["owes"] = c["owes"] + [{"by": "MX", "to": "PAC", "what": "a customs post at the boundary at the Pass that passes the rifles overland into Chihuahua"}]
    c["more_quotes"] = [
        "From the autumn of 1865 until June 1866 Juárez's government sits at Paso del Norte itself, and the crossing outlives his stay.",
        "The rifles go down the Rio Grande's west bank from Mesilla to the boundary at the Pass, where a customs post agreed with Mexico passes them overland into Chihuahua",
    ]
    c["open"] = "From the autumn of 1865 (CR-061 CT4; CR-058 'Juárez backed in 1865–67'). The credit's amount and term are not stated."
    return c


def a_arizona(c):
    c["name"] = "Confederate renunciation of Arizona and the Sunset articles"
    c["owes"] = [
        {"by": "CSA", "to": "PAC", "what": "renunciation of the Confederate Arizona claim; no Confederate soldier enters New Mexico in arms"},
        {"by": "CSA", "to": "PAC", "what": "Texas gives up its old claim to New Mexico east of the river, by a resolution of its legislature at Austin"},
        {"by": "PAC", "to": "CSA", "what": "credit and the future railway connection"},
        {"by": "PAC", "to": "CSA", "what": "use of the Sunset road, but no right to march on it; Texan freight changes to New Mexican carts at El Paso"},
    ]
    c["conditions"] = [
        "a slave whom a master brings onto Pacifican soil is free; a fugitive is refused at the Texas line and one who reaches Pacifican soil is not given up (C-1871-FUGITIVE)",
    ]
    c["more_quotes"] = [
        "At San Antonio in February 1863, where Elias has come from Santa Fe, the Sunset articles give the Confederacy the use of the southern road, the Sunset road, but no right to march on it.",
        "Colonel James Reily, who carried Sibley's letters to the governors of Chihuahua and Sonora the year before, signs for Richmond, and General Magruder for the military district.",
        "No Confederate soldier enters New Mexico in arms; Texan freight changes to New Mexican carts at El Paso; a slave whom a master brings onto Pacifican soil is free;",
        "Texas gives up its old claim to New Mexico east of the river by a resolution of its legislature at Austin.",
        "Early in 1863 Elias goes to Texas in person to settle the Arizona renunciation and the Matamoros supply terms.",
    ]
    c["open"] = ("Settled at San Antonio in February 1863 (APPROVED — CR-061). The credit's amount is not stated "
                 "(C-1863-RICHMOND-CREDIT); the railway connection's terms are not stated. Munitions under the 1865 "
                 "armistice: C-1865-ARMISTICE.")
    return c


def a_carson(c):
    c["more_quotes"] = c["more_quotes"] + [
        "American owners in Nevada keep the property guarantees Carson gave them.",
    ]
    c["open"] = ("Washoe is retaken in 1864; its guarantees are kept as Hawaii's condition for the third renewal "
                 "(C-1861-PROTECTOR) and restated in the civil compact (C-1864-WASHOE-COMPACT), and the 1865 peace "
                 "keeps the property guarantees while ending the convention (CR-039).")
    return c


def a_amity(c):
    c["conditions"] = ["no military clause"]
    c["more_quotes"] = ["The treaty carries no military clause; its exact drafting remains"]
    return c


AMEND = {
    "C-1847-LONDON-DEBT": a_london,
    "C-1862-DESERET": a_deseret,
    "C-1863-MATAMOROS": a_matamoros,
    "C-1863-NAVAJO": a_navajo,
    "C-1865-APACHE": a_apache,
    "C-1865-MX-SCALP": a_scalp,
    "C-1865-HI-GUARANTEES": a_hi_guar,
    "C-1871-FUGITIVE": a_fugitive,
    "C-1911-FUR-SEAL": a_seal,
    "C-1861-PROTECTOR": a_protector,
    "C-1871-PEACE": a_peace,
    "C-1871-CSA-GUARANTEE": a_peace,
    "C-1867-WESTERN-LINE": a_western,
    "C-1865-ARMISTICE": a_armistice,
    "C-1867-VENDOR-CREDIT": a_vendor,
    "C-1867-ALASKA": a_alaska,
    "C-1867-JUAREZ-CREDIT": a_juarez,
    "C-1863-ARIZONA": a_arizona,
    "C-1860-CARSON": a_carson,
    "C-1865-CSA-AMITY": a_amity,
}

# ---------------------------------------------------------------------------
# New parties and commitments
# ---------------------------------------------------------------------------

PARTIES = [
    ("OR", "Oregon (the territory's compact with the occupation command from 1861; the member state from 1867)"),
    ("COLUMBIA", "Washington Territory and its counties (the parallel compact of 1861); the member Columbia from 1867"),
    ("IDAHO", "Idaho (the member state from 1867)"),
    ("WASHOE", "Washoe (Nevada Territory's legislature and counties; the member state from 1867)"),
    ("MONTANA", "Western Montana's counties (the member state from 1867)"),
    ("NM", "New Mexico: the Rio Grande compact's signatories and assembly (1863); the member state from 1867"),
    ("MTCAMPS", "The mining camps of western Montana (Bannack and Alder Gulch)"),
    ("NEZPERCE", "The Nez Perce (Lewiston townsite)"),
    ("ORNATIONS", "The nations of Oregon whose compacts take effect only if Oregon accedes"),
    ("SOUNDNATIONS", "The treaty nations of the Sound, the coast and the Yakama"),
    ("NWSHOSHONE", "The Northwestern Shoshone bands (Box Elder compact)"),
    ("ESHOSHONE", "Washakie's Eastern Shoshone"),
    ("BHUTES", "Black Hawk's Utes (Deseret's southern settlements, 1865)"),
    ("OWYPAIUTE", "The Paiute of the Owyhee"),
    ("PUEBLOS", "The Pueblos of New Mexico"),
    ("TLINGIT", "The Tlingit of Sitka"),
    ("ALUTIIQ", "The nations of the Kodiak compact (Alutiiq)"),
    ("UNANGAN", "The Unangan of St Paul and St George"),
    ("SEALLESSEES", "The seal-islands lessees (not named in canon)"),
    ("AUK", "The Auk Tlingit under Kowee"),
    ("AHTNA", "The Ahtna under Nicolai"),
    ("CHILKOOT", "The Chilkoot of Dyea"),
    ("WHITEPASS", "The builders of the White Pass railway from Skagway (not named in canon)"),
    ("BCCO", "The company of the colony of British Columbia that holds the Confederation's line"),
    ("EASTHOUSES", "The New York and Philadelphia houses and the transit companies (the private loan of 1867)"),
]


def N(**kw):
    return kw


NEW = [
    # --- CR-059: Oregon, the Sound and Columbia
    N(id="C-1861-OR-ENABLING", name="The Union's Oregon Enabling Act", kind="law", parties=["US", "OR"], **{"from": 1861},
      ended=1866, ended_by="Oregon's choice of Pacifica in October 1866; it 'stood for five years'",
      owes=[{"by": "US", "to": "OR", "what": "statehood under a new constitution without slavery or exclusion"}],
      cr="CR-059",
      quote="The Oregon Enabling Act of 2 March 1861 offers statehood under a new constitution without slavery or exclusion, and Oregon is to elect its delegates in June.",
      more_quotes=["The convention the Enabling Act called never meets at Salem.",
                   "The Union's Enabling Act still offers statehood, and the Senate's Republicans refuse to drop its ban on excluding free Black people.",
                   "the Union's own Enabling Act, which demanded the clause's removal, stood for five years and never got it removed"],
      open="CR-059 has it amended in 1864 with the restoration programme; the amendment is not in the storyline."),
    N(id="C-1861-OR-COMPACT", name="Oregon's civil compact with the occupation command", kind="compact", parties=["PAC", "OR"],
      **{"from": 1861}, from_approx=True,
      owes=[{"by": "PAC", "to": "OR", "what": "courts and county governments continue; requisitions are paid and disputed in civilian courts; no one swears allegiance; Oregon's men, ports and revenues serve no military purpose outside Oregon"},
            {"by": "PAC", "to": "OR", "what": "from 1862 the customs collected at Astoria and Portland go into a published Oregon account that pays Oregon's courts and county officers"}],
      conditions=["Whiteaker negotiates civil protections without conceding a governor's right to transfer Oregon's allegiance",
                  "the legislature's acts take effect without the absent federal governor, subject to the compact's court"],
      cr="CR-059",
      quote="Its territorial legislature and county commissioners negotiate a civil compact with the occupation command.",
      more_quotes=["Courts and county governments continue, requisitions are paid and disputed in civilian courts, no one swears allegiance, and Oregon's men, ports and revenues serve no military purpose outside Oregon.",
                   "The legislature's acts take effect without the absent federal governor, subject to the compact's court.",
                   "From 1862 the customs collected at Astoria and Portland go into a published Oregon account that pays Oregon's courts and county officers."],
      open="Year not stated; from = the fall of Portland in 1861 (the compact precedes the flood of December 1861). The customs account (CR-059 W6) is folded in. Its end at accession is not stated."),
    N(id="C-1861-PUGET-COMPACT", name="The Puget Sound counties' parallel compact", kind="compact", parties=["PAC", "COLUMBIA"],
      **{"from": 1861}, from_approx=True, cr="CR-059",
      quote="The Puget Sound counties sign a parallel compact, and Matthew Deady, a territorial justice, becomes the compact's court.",
      open="Terms as Oregon's (C-1861-OR-COMPACT); year not stated beyond 1861."),
    N(id="C-1862-WALLA-WALLA", name="Walla Walla convention", kind="convention", parties=["US", "PAC"], **{"from": 1862}, until=1862,
      owes=[{"by": "PAC", "to": "US", "what": "the regulars march east with the honours of war by the Mullan Road"}], cr="CR-059",
      quote="After the attempt on the lower Columbia fails, the Walla Walla convention of July 1862 lets the regulars carry out their own government's order: they march east with the honours of war, guided by John Mullan on the road he built.",
      open="Other terms not stated."),
    N(id="C-1862-LEWISTON-LEASE", name="Lewiston townsite lease", kind="lease", parties=["NEZPERCE", "PAC"], **{"from": 1862}, from_approx=True,
      owes=[{"by": "NEZPERCE", "to": "PAC", "what": "the Lewiston townsite, leased through the Confederation"}], cr="CR-059",
      quote="Lewiston stands on a townsite the Nez Perce lease through the Confederation.",
      open="Year, rent and term not stated; from = the Boise Basin rush of 1862 in the same paragraph."),
    N(id="C-1866-OR-CHARTER", name="Oregon's charter of accession", kind="charter", parties=["PAC", "OR"], **{"from": 1866},
      owes=[{"by": "PAC", "to": "OR", "what": "the charter entrenched by the Confederal chambers and California and ratified by Hawaii's legislature: 'a charter no cabinet can touch'"}],
      conditions=["the Native article sends killings and land disputes to confederal courts and admits Native testimony, against Oregon's own law",
                  "the charter's floor for Chinese residents: one licence and one court for all",
                  "the exclusion article takes effect only under Pacifica and is limited to people who are not citizens of a member state"],
      cr="CR-059",
      quote="The Confederal chambers and California entrench Oregon's charter, and Hawaii's legislature ratifies on her message;",
      more_quotes=["James Nesmith, the Douglas Democrats' leader in Oregon, calls it a charter no cabinet can touch.",
                   "The charter's Native article sends killings and land disputes to confederal courts and admits Native testimony, against Oregon's own law.",
                   "The Native article and the charter's floor for Chinese residents, one licence and one court for all, which Elias insisted on, nearly cost him the south.",
                   "That summer Victoria, in San Francisco, has the article limited to people who are not citizens of a member state.",
                   "In October 1866 Oregon chooses Pacifica narrowly."],
      open="Approved 1866 with Oregon's choice of October; membership on the exchange of 1867 (CR-059). Amendment only with Oregon's consent (CR-059) is not stated beyond 'entrench'."),
    N(id="C-1866-OR-NATIONS", name="The Oregon nations' conditional compacts", kind="compact", parties=["PAC", "ORNATIONS"], **{"from": 1866},
      conditions=["take effect only if Oregon accedes"], cr="CR-059",
      quote="They have signed their own compacts, to take effect only if Oregon accedes.",
      more_quotes=["The nations whose land it is have no ballot."],
      open="The nations and terms are not stated (CR-059's Klamath compact and Paiute peace are not in the storyline)."),
    N(id="C-1866-ID-CHARTER", name="Idaho's charter of accession", kind="charter", parties=["PAC", "IDAHO"], **{"from": 1866}, cr="CR-059",
      quote="In June 1866 Idaho's voters approve its charter of accession.",
      more_quotes=["The peace transfers Idaho outright."],
      open="Terms not stated; membership on the exchange of 1867."),
    N(id="C-1866-WA-CHARTER", name="Columbia's charter of accession (Washington Territory)", kind="charter", parties=["PAC", "COLUMBIA"], **{"from": 1866},
      conditions=["no exclusion clause"], cr="CR-059",
      quote="North of the river no vote is owed: the Union made Washington Territory no offer of statehood, and in the autumn of 1866 its elected convention meets at Olympia.",
      more_quotes=["It writes no exclusion clause;",
                   "It names the new member Columbia, the name its settlers asked for at Monticello in 1852 and Congress gave away."],
      open="Approved by the Olympia convention in the autumn of 1866; member as Columbia on the exchange of 1867 (CR-059 Part IX, approved). Further terms not stated."),
    N(id="C-1866-SOUND-NATIONS", name="Compacts of the treaty nations of the Sound, the coast and the Yakama", kind="compact", parties=["PAC", "SOUNDNATIONS"], **{"from": 1866},
      owes=[{"by": "PAC", "to": "SOUNDNATIONS", "what": "the fishing places their treaties kept, as a right no licence can narrow"}], cr="CR-059",
      quote="The treaty nations of the Sound, the coast and the Yakama sign compacts of their own, and the fishing places their treaties kept become a right no licence can narrow;",
      open="Signatories and other terms not stated."),
    N(id="C-1866-OR-CERTIFICATION", name="Protocol of certification of Oregon's returns", kind="convention", parties=["US", "PAC"], **{"from": 1866},
      cr="CR-062",
      quote="In the winter after Oregon's vote both governments sign a protocol recording the certified returns and striking the terms the protocol of 1865 set for a Union Oregon.",
      open="Signed in the winter of 1866–67; from = 1866."),
    # --- CR-060: Deseret, the Basin and the Rockies
    N(id="C-1863-SHOSHONE-BOXELDER", name="Box Elder compact", kind="compact", parties=["PAC", "NWSHOSHONE"], **{"from": 1863},
      owes=[{"by": "PAC", "to": "NWSHOSHONE", "what": "annuities paid from the road's own fees; Cache Valley's grazing paid for through Deseret"},
            {"by": "NWSHOSHONE", "to": "PAC", "what": "Shoshone scouts on the Snake road; the killers given up to the travellers' court by their own people, those of 1862 among them"}],
      cr="CR-060",
      quote="In the summer, with Elias present on his way from Salt Lake, the bands sign the Box Elder compact: annuities paid from the road's own fees, Cache Valley's grazing paid for through Deseret, Shoshone scouts on the Snake road, and the killers given up to the travellers' court by their own people, those of 1862 among them now that the Compact reaches crimes of any date.",
      open="Amounts, term and the scouts' pay not stated; the Soda Springs agreement (CR-060 N2) is not in the storyline."),
    N(id="C-1863-SHOSHONE-BRIDGER", name="Washakie's terms for passage at Fort Bridger", kind="pact", parties=["PAC", "ESHOSHONE"], **{"from": 1863},
      cr="CR-060",
      quote="Washakie's Eastern Shoshone make their own terms for passage at Fort Bridger and keep their distance from both armies.",
      more_quotes=["The Ute leaders and terms, and Washakie's agreement."],
      open="Terms **[OPEN]** (§12)."),
    N(id="C-1863-MINING-COMPACTS", name="Supply compacts of the Montana camps", kind="compact", parties=["PAC", "MTCAMPS"], **{"from": 1863}, from_approx=True,
      owes=[{"by": "PAC", "to": "MTCAMPS", "what": "freight at published rates, Pacifican coin, assay and licensed courts"}], cr="CR-060",
      quote="Deseret's freighters work the Montana Trail on the Compact's terms, and the camps at Bannack and Alder Gulch sign supply compacts for freight at published rates, Pacifican coin, assay and licensed courts.",
      more_quotes=["The courts come too late for the winter of 1863–64."],
      open="Year given only as 1863–1864 for the camps' turn; the Idaho districts' compacts (CR-060 M1) are not stated."),
    N(id="C-1864-FORT-CHURCHILL", name="Withdrawal terms of the Fort Churchill garrison", kind="settlement", parties=["PAC", "US"], **{"from": 1864}, until=1864,
      owes=[{"by": "PAC", "to": "US", "what": "the garrison leaves with its arms; volunteers who will not stay march east by Deseret's road, fed at Pacifica's charge"}],
      cr="CR-060",
      quote="Those of Fort Churchill's volunteers who will not stay march east by Deseret's road, fed at Pacifica's charge, and Nye goes with them.",
      more_quotes=["Sherman insists that the garrison leave with its arms"],
      open="No parole is stated either way (CR-060 C5–C6)."),
    N(id="C-1864-WASHOE-COMPACT", name="Washoe's civil compact", kind="compact", parties=["PAC", "WASHOE"], **{"from": 1864},
      owes=[{"by": "PAC", "to": "WASHOE", "what": "a published tax on the mines' net proceeds lighter than the one Washoe refused"},
            {"by": "PAC", "to": "WASHOE", "what": "the Carson Convention's guarantees kept"}],
      conditions=["on Oregon's terms (C-1861-OR-COMPACT)"], cr="CR-060",
      quote="Washoe's legislature and county officials sign a civil compact on Oregon's terms, and Pacifica publishes a tax on the mines' net proceeds lighter than the one Washoe has just refused.",
      more_quotes=["no annexation, the Carson Convention's guarantees kept, and Hawaii's control of entry at its own ports."],
      open="The tax schedule (CR-060 C8) is not stated. Victoria's request that Washoe choose for itself after the peace is not written in."),
    N(id="C-1865-UTE-BLACKHAWK", name="Spanish Fork agreement with Black Hawk's Utes", kind="pact", parties=["PAC", "BHUTES", "DESERET"], **{"from": 1865},
      owes=[{"by": "PAC", "to": "BHUTES", "what": "cattle and flour each year for the grazing the settlements took; homelands they will not be moved from"},
            {"by": "PAC", "to": "BHUTES", "what": "what was done that spring is forgiven on both sides; killings from that day go to the confederal court"}],
      conditions=["the stock already driven off is set against the first year's issue"], cr="CR-060",
      quote="The Utes are promised cattle and flour each year for the grazing the settlements took, and homelands they will not be moved from; the stock already driven off is set against the first year's issue; what was done that spring is forgiven on both sides, and killings from that day go to the confederal court.",
      more_quotes=["That summer the Republic's commissioner calls a council at Spanish Fork."],
      open="Who bears the yearly issue (Pacifica or Deseret) and the homelands' bounds are not stated."),
    N(id="C-1866-OWYHEE-PAIUTE", name="Owyhee Paiute agreement", kind="pact", parties=["PAC", "OWYPAIUTE"], **{"from": 1866}, cr="CR-060",
      quote="Silver City calls it murder; the Paiute of the Owyhee sign their agreement that year because of it.",
      open="Terms not stated (CR-060 N8)."),
    N(id="C-1866-UTE", name="Ute homeland agreement of 1866", kind="pact", parties=["PAC", "UTE"], **{"from": 1866},
      owes=[{"by": "PAC", "to": "UTE", "what": "the Slope and the Parks reserved as a Ute homeland that can never be sold, whose ground the Republic may lease only for the Utes"}],
      conditions=["conditional on the treaty"], cr="CR-060",
      quote="Pacifica's commissioners meet the Utes in the summer of 1866, and the agreement they make, conditional on the treaty, reserves the Slope and the Parks as a Ute homeland that can never be sold and whose ground the Republic may lease only for the Utes.",
      more_quotes=["The Ute leaders and terms, and Washakie's agreement."],
      open="Bands and leaders **[OPEN]**; the party is entered as UTE because the Uncompahgre lease of 1881 (C-1881-UTE-LEASE) rests on this homeland."),
    N(id="C-1866-WASHOE-CHARTER", name="Washoe's charter of accession", kind="charter", parties=["PAC", "WASHOE"], **{"from": 1866}, cr="CR-060",
      quote="Washoe elects a convention in 1866 that approves its charter of accession, and western Montana's counties do the same.",
      open="Terms not stated; membership on the exchange of 1867. Amendment only with the member's consent (CR-060 A5) is not stated."),
    N(id="C-1866-MT-CHARTER", name="Western Montana's charter of accession", kind="charter", parties=["PAC", "MONTANA"], **{"from": 1866}, cr="CR-060",
      quote="Washoe elects a convention in 1866 that approves its charter of accession, and western Montana's counties do the same.",
      open="Terms not stated; membership on the exchange of 1867."),
    N(id="C-1866-DESERET-CHARTER", name="Deseret's charter of accession", kind="charter", parties=["PAC", "DESERET"], **{"from": 1866},
      owes=[{"by": "PAC", "to": "DESERET", "what": "Deseret's marriage and church-property law protected under the confederal floor"},
            {"by": "DESERET", "to": "PAC", "what": "the Nauvoo Legion placed within the Defense Law"}],
      conditions=["confederal law forbids member states from banning marriage on grounds of race or origin; it does not impose one marriage system"],
      cr="CR-060",
      quote="In December 1866, after Oregon has voted, Utah's territorial legislature adjourns and meets again the same day as the General Assembly of Deseret, and approves the charter that Elias had held back until Oregon was safe.",
      more_quotes=["Deseret becomes a member state on the exchange of ratifications in 1867, with its marriage and church-property law protected under the confederal floor and the Nauvoo Legion placed within the Defense Law.",
                   "Confederal law forbids member states from banning marriage on grounds of race or origin; it does not impose one marriage system on every state."],
      open="Approved December 1866; member state on the exchange of 1867. Representation is not stated."),
    # --- CR-061: New Mexico
    N(id="C-1863-RIO-GRANDE", name="Rio Grande compact", kind="compact", parties=["PAC", "NM"], **{"from": 1863},
      owes=[{"by": "PAC", "to": "NM", "what": "elected town government; courts in Spanish and English; the territory's own institutions of 1850; the old grants confirmed, with each community's commons confirmed to the community"},
            {"by": "PAC", "to": "NM", "what": "any congregation keeps its chapel and calls its own priest"},
            {"by": "PAC", "to": "NM", "what": "Arizona county organized for Tucson and the Gila"},
            {"by": "PAC", "to": "NM", "what": "the Taos article: no one tried for 1847, on either side; the Taos and Rio Arriba companies come home as the compact's home guard, sworn to its laws and never ordered against the Union"},
            {"by": "NM", "to": "PAC", "what": "when the peace comes, debt peonage and the captive trade end, with compensation"}],
      cr="CR-061",
      quote="its members open the Rio Grande compact of 1863 with Elias at the turn of the year and carry it on with his commissioner, Pablo de la Guerra, after he leaves for Texas.",
      more_quotes=["In the spring it is signed at Santa Fe by the members from the counties Pacifica holds, the probate judges and the town councils",
                   "the compact lets any congregation keep its chapel and call its own priest.",
                   "It gives the towns elected government, courts that sit in Spanish and English, the territory's own institutions of 1850, and confirmation of the old grants, with each community's commons confirmed to the community, and it organizes Arizona county for Tucson and the Gila.",
                   "The signatories accept one clause unwillingly: when the peace comes, debt peonage and the captive trade will end, with compensation.",
                   "The amnesty becomes an article of the Rio Grande compact, and Carson the compact's broker in the Hispano towns.",
                   "The captive article brings the compact's unwilling clause forward."],
      open="Signed at Santa Fe in the spring of 1863. Its abolition clause is carried out by the ordinance of 1865–66 (C-1866-NM-ABOLITION)."),
    N(id="C-1863-PUEBLOS", name="The Pueblos' agreement", kind="pact", parties=["PAC", "PUEBLOS"], **{"from": 1863}, from_approx=True,
      owes=[{"by": "PAC", "to": "PUEBLOS", "what": "their grants entered in the register as homelands"}], cr="CR-061",
      quote="The Pueblos make their own agreement, and their grants enter the register as homelands.",
      open="Year not stated; from = the Rio Grande compact's year in the same paragraph."),
    N(id="C-1863-NAVAJO-PASSAGE", name="Cubero agreement with the Navajo", kind="pact", parties=["PAC", "NAVAJO"], **{"from": 1863},
      owes=[{"by": "PAC", "to": "NAVAJO", "what": "the towns' slaving expeditions forbidden"},
            {"by": "NAVAJO", "to": "PAC", "what": "the raids stop"}],
      cr="CR-061",
      quote="The towns' slaving expeditions are forbidden, the Navajo raids stop, and at the beginning of May the agreement is signed at Cubero with de la Guerra.",
      open="Signed May 1863; replaced by the homeland treaty of 1865 (C-1863-NAVAJO) is not stated."),
    N(id="C-1865-SANTA-RITA", name="Santa Rita del Cobre copper lease", kind="lease", parties=["APACHE", "PAC"], **{"from": 1865},
      owes=[{"by": "APACHE", "to": "PAC", "what": "the old copper mine at Santa Rita del Cobre"},
            {"by": "PAC", "to": "APACHE", "what": "a royalty to the Chihenne"}], cr="CR-061",
      quote="Pacifica takes the old copper mine on a lease that pays the Chihenne a royalty.",
      open="Royalty and term not stated."),
    N(id="C-1866-NM-ABOLITION", name="New Mexico's abolition ordinance", kind="law", parties=["PAC", "NM"], **{"from": 1866},
      owes=[{"by": "PAC", "to": "NM", "what": "compensation for the peons and captives freed, forfeited by every patrón who rose in 1866"}],
      cr="CR-061",
      quote="In December 1865 the compact's assembly votes the abolition ordinance, in the House by one vote, the speaker's, cast by José Manuel Gallegos, the priest Bishop Lamy suspended, for the abolition Lamy has preached since the captive article; the cabinet promulgates it as voted in January 1866.",
      more_quotes=["Pacifica abolishes New Mexico's debt peonage and Native captive trade gradually with compensation by 1866, facing a short Hispano revolt.",
                   "every patrón who rose loses the compensation for the peons and captives he must free anyway."],
      open="Voted December 1865, promulgated January 1866. Rates of compensation are not stated."),
    N(id="C-1866-NM-CHARTER", name="New Mexico's charter of accession", kind="charter", parties=["PAC", "NM"], **{"from": 1866},
      conditions=["abolition written into the charter"], cr="CR-061",
      quote="That summer New Mexico's convention approves its charter of accession with abolition written into it.",
      open="Membership on the exchange of 1867. San Miguel's and Mora's members sign against the Union governor's order; Las Vegas protests to Washington."),
    # --- CR-062: the claims commission
    N(id="C-1867-WESTERN-CLAIMS", name="Mutual waiver and the mixed claims commission", kind="settlement", parties=["US", "PAC", "HI"], **{"from": 1867},
      owes=[{"by": "US", "to": "PAC", "what": "the Union's claims from the war waived"},
            {"by": "PAC", "to": "US", "what": "Pacifica's claims from the war waived"},
            {"by": "PAC", "to": "HI", "what": "the family of the Hawaiian sailor killed in 1861 keeps its own claim before the commission"}],
      cr="CR-062",
      quote="Both governments waive their claims from the war, so Farragut's death is charged to no one in the treaty, and a mixed commission hears private claims.",
      more_quotes=["At Victoria's insistence, the family of the Hawaiian sailor killed in 1861 keeps its own claim before the commission."],
      open="An article of the Western treaty; from = the exchange of 1867. The commission's sittings and awards are not stated."),
    # --- CR-068: the Richmond credit
    N(id="C-1863-RICHMOND-CREDIT", name="The Republic's credit to Richmond", kind="loan", parties=["PAC", "CSA"], **{"from": 1863},
      owes=[{"by": "PAC", "to": "CSA", "what": "credit lent at interest for independence, spent in Europe"}],
      conditions=["it falls due if Richmond treats for reunion",
                  "the war advances end when both governments accept an armistice (published in the spring of 1862); they end with the armistice of 1865"],
      cr="CR-068",
      quote="At San Antonio in February, where the Sunset articles are signed, he also has the terms of the Richmond credit printed: it is lent for independence and falls due if Richmond treats for reunion.",
      more_quotes=["He then widens the Republic's credit at Richmond and publishes its condition, that its war advances end when both governments accept an armistice.",
                   "Pacifica's credit to Richmond, lent on terms it prints the next year, buys in Europe;",
                   "the credit is lent at interest so that the South is not conquered and the Pacific taken next",
                   "Pacifica's war advances to Richmond end with the armistice, as it published in 1862."],
      open="The credit runs from 1861–62; from = the printed terms of February 1863. Amount and interest are MODEL (CR-068). The offer to lend or stand surety on the customs for compensated emancipation when Richmond asks is an offer, not a term. The supply route is C-1863-MATAMOROS."),
    # --- CR-069: the coin bonds and the agency of 1867
    N(id="C-1862-COIN-BONDS", name="War bonds in coin and the agency of 1867", kind="loan", parties=["SANFRANCISCO", "PAC", "EASTHOUSES"], **{"from": 1862},
      owes=[{"by": "SANFRANCISCO", "to": "PAC", "what": "the Republic's war bonds taken in coin from the houses' reserves, brought by Ralston"},
            {"by": "PAC", "to": "SANFRANCISCO", "what": "interest on the coin bonds (amount OPEN)"},
            {"by": "PAC", "to": "EASTHOUSES", "what": "from 1867, the loan the Senate declined, lent privately through Ralston's bank as the Republic's agent, which takes a share of its own"}],
      cr="CR-069",
      quote="When the Republic borrows for the war that year, Ralston brings the houses to take its bonds in coin from their reserves; the Republic spends the coin on its own foundries, yards and carriers, and it comes back to the banks.",
      more_quotes=["The interest on the coin bonds and their amounts beyond the model's.",
                   "The money is lent privately instead, through Ralston's bank as the Republic's agent, which takes a share of its own, to New York and Philadelphia houses and the transit companies."],
      open="Bonds of 1862–1864 (CR-069 P2; about one-fifth of the war's cost, MODEL); interest, amounts and redemption **[OPEN]**. The Steamer Day Agreement is private and not a commitment of the Republic; the Bank of California holds no public charter."),
    # --- CR-070: Alaska and the north
    N(id="C-1867-NORTHERN-COMMISSION", name="Charter of the Northern Commission", kind="charter", parties=["PAC"], **{"from": 1867},
      conditions=["a bill of the confederal chambers, not a cabinet ordinance, so that the compacts have a ratifier that will outlive Elias; the north a station and no fortress",
                  "the Mining Law of 1849 extended north; the land office grants nothing and the claims courts register nothing on a nation's country without that nation's compact",
                  "a mine on a nation's land holds it by the nation's lease; the Confederation takes its five per cent; the finder's share is agreed on top of both and paid by the mine"],
      cr="CR-070",
      quote="Alaska is a territory of the Confederation from the day the flag changes, and the confederal chambers charter a Northern Commission under Pablo de la Guerra to govern it;",
      more_quotes=["he brings it to the chambers as a bill, because the compacts need a ratifier that will outlive him, and the chambers vote the north a station and no fortress;",
                   "but the land office grants nothing and the claims courts register nothing on a nation's country without that nation's compact,",
                   "A mine on a nation's land holds it by the nation's lease; the Confederation takes its five per cent; and the nation that showed the ore takes a finder's share agreed on top of both and paid by the mine."],
      open="George Davidson succeeds de la Guerra in 1873. The compacts for the Commission's stations and wire (Wrangell, Juneau, Unalaska) and for the Seward Peninsula placers: parties, years and terms OPEN."),
    N(id="C-1869-SITKA", name="Sitka compact with the Tlingit", kind="compact", parties=["PAC", "TLINGIT"], **{"from": 1869},
      owes=[{"by": "PAC", "to": "TLINGIT", "what": "their village and its fisheries stay theirs; the Commission holds the Russian town's ground by a yearly rent; clan property is recognised in its courts"},
            {"by": "PAC", "to": "TLINGIT", "what": "a killing by the garrison is paid to the dead man's clan under Tlingit law"},
            {"by": "TLINGIT", "to": "PAC", "what": "disputes go to a joint hearing"}],
      cr="CR-070",
      quote="the first is opened with the Tlingit at Sitka in the autumn of 1867 and concluded in 1869: their village and its fisheries stay theirs, the Commission holds the Russian town's ground by a yearly rent, clan property is recognised in its courts, and disputes go to a joint hearing.",
      more_quotes=["the rule becomes a term of the Sitka compact, concluded that year, and the town stays quiet."],
      open="Opened 1867, concluded 1869. The rent's amount and review (CR-070: $5,000 a year in gold, reviewed every ten years) are not in the storyline."),
    N(id="C-1868-KODIAK", name="Kodiak compact", kind="compact", parties=["PAC", "ALUTIIQ"], **{"from": 1868},
      owes=[{"by": "PAC", "to": "ALUTIIQ", "what": "only the nations' hunters take the sea otter"}],
      conditions=["a yearly quota"], cr="CR-070",
      quote="By the Kodiak compact of 1868 only the nations' hunters take the sea otter, under a yearly quota, and the otter is not hunted out.",
      open="The quota and the nations' names are not stated."),
    N(id="C-1868-SEAL-LEASES", name="Seal-islands leases", kind="lease", parties=["PAC", "SEALLESSEES", "UNANGAN"], **{"from": 1868}, from_approx=True,
      renewals=[1880, 1890, 1900, 1910, 1920, 1930],
      owes=[{"by": "SEALLESSEES", "to": "PAC", "what": "a price per skin"},
            {"by": "SEALLESSEES", "to": "UNANGAN", "what": "the Unangan sealers' terms, paid by the skin, carried in every lease"}],
      cr="CR-070",
      quote="The seal islands are leased at a price per skin and put out to tender again every ten years from 1880, and every lease carries the terms of the Unangan of St Paul and St George, who are paid by the skin and hold their islands by their own compact.",
      open="First lease year not stated (1868 in CR-070). Lessees and prices not stated."),
    N(id="C-1868-PRIBILOF-COMPACT", name="The Pribilof islands' compact with the Unangan", kind="compact", parties=["PAC", "UNANGAN"], **{"from": 1868}, from_approx=True,
      owes=[{"by": "PAC", "to": "UNANGAN", "what": "their islands held by their own compact; their terms carried in every seal lease"}], cr="CR-070",
      quote="who are paid by the skin and hold their islands by their own compact.",
      open="Year and further terms not stated."),
    N(id="C-1872-AUK-FINDER", name="The Auk finder's compact (Gastineau Channel)", kind="compact", parties=["PAC", "AUK"], **{"from": 1872},
      owes=[{"by": "PAC", "to": "AUK", "what": "a finder's share in the gold belt, agreed before the source is shown and paid by the mine"}], cr="CR-070",
      quote="In 1872 the Auk leader Kowee brings ore from Gastineau Channel to the assay office at Sitka and will not show its source until the Commission has agreed his people's share.",
      open="The share is not stated."),
    N(id="C-1880-CHILKOOT", name="Chilkoot compact", kind="compact", parties=["PAC", "CHILKOOT"], **{"from": 1880},
      owes=[{"by": "PAC", "to": "CHILKOOT", "what": "their packers carry; their trade goes on"},
            {"by": "CHILKOOT", "to": "PAC", "what": "prospectors cross their pass for a toll"},
            {"by": "CHILKOOT", "to": "PAC", "what": "from 1884, with the Commission, a wagon road to Sheep Camp and an aerial tramway over the summit"}],
      cr="CR-070",
      quote="In 1880 the Chilkoot of Dyea make a compact with the Northern Commission: their packers carry, their trade goes on, and prospectors cross their pass for a toll.",
      more_quotes=["From 1884, for the Yukon bar miners, the Chilkoot and the Commission build a wagon road to Sheep Camp and an aerial tramway over the summit, and the Fortymile strike of 1886 pays for it."],
      open="The toll is not stated. The Chilkat of Klukwan refuse a compact and their pass stays closed."),
    N(id="C-1885-AHTNA-FINDER", name="The Ahtna finder's compact (Chitina copper)", kind="compact", parties=["PAC", "AHTNA"], **{"from": 1885},
      owes=[{"by": "PAC", "to": "AHTNA", "what": "a finder's share in the copper of the Chitina"}], cr="CR-070",
      quote="In 1885 the Ahtna leader Nicolai shows the Commission's party the copper of the Chitina and makes a finder's compact for it, so that he never has to trade its whereabouts for food, and the mine opened under it ships its ore from about 1900.",
      open="The share and the mine's lease are not stated."),
    N(id="C-1897-WHITE-PASS", name="White Pass railway compact with the Chilkoot", kind="compact", parties=["WHITEPASS", "CHILKOOT"], **{"from": 1897},
      owes=[{"by": "WHITEPASS", "to": "CHILKOOT", "what": "a share of the railway's freight for the packing it will end"}], cr="CR-070",
      quote="the railway over the White Pass from Skagway is building before the stampede of 1897, on a compact with the Chilkoot, whose ground the pass is, that gives them a share of its freight for the packing it will end.",
      open="The builders and the share are not stated."),
    N(id="C-1868-BC-TELEGRAPH", name="The Confederation's line through British Columbia", kind="concession", parties=["PAC", "BCCO", "CA"], **{"from": 1868}, from_approx=True,
      ended=1897, ended_by="sold to Canada in the spring of 1897 (C-1897-BC-LINE-SALE)",
      owes=[{"by": "BCCO", "to": "PAC", "what": "Western Union's line in British Columbia, held for the Confederation by a company of the colony"}],
      cr="CR-070",
      quote="The Confederation buys the company's line in British Columbia through a company of the colony, and its engineers build north from Fort Stager to the Stikine and down the river to Wrangell, and a cable through the straits puts Sitka on the wire in 1870.",
      more_quotes=["For eighteen years Alaska's wire crosses British, then Canadian, soil;",
                   "for a month in 1885 the Dominion's offices refuse Pacifica's cipher, and Sitka is reached only by steamer."],
      open="Year of purchase not stated (1868 in CR-070). The franchise's terms (CR-070: Collins's grant; free government messages and the Cariboo service owed to the colony and the Dominion) are not in the storyline."),
    N(id="C-1897-BC-LINE-SALE", name="Sale of the British Columbia line to Canada", kind="settlement", parties=["PAC", "CA"], **{"from": 1897},
      owes=[{"by": "PAC", "to": "CA", "what": "the old line through British Columbia, as the first half of Canada's own wire to the Yukon"}], cr="CR-070",
      quote="in the spring of 1897, when the strike is public, it sells Canada the old line through British Columbia as the first half of Canada's own wire to the Yukon.",
      open="Price and the through-traffic rights to Alaska (CR-070) are not stated."),
    N(id="C-1903-KURIL-CABLE", name="Cable landings by the Kurils at Hakodate", kind="concession", parties=["JP", "PAC"], **{"from": 1903},
      owes=[{"by": "JP", "to": "PAC", "what": "landing of the Sitka cable by Attu and the Kurils at Hakodate, on Japanese soil"}], cr="CR-070",
      quote="Between 1900 and 1903 Pacifica carries the Sitka cable on, to Kodiak and Unalaska in 1900 and by Attu and the Kurils to Hakodate in 1903: the second route to Japan is open, landing only on Pacifican and Japanese soil.",
      open="The grants are not described; CR-070 calls them Japanese grants. Kiyoshi keeps the cable from being cut in 1904."),
]


def main() -> int:
    story = L.Story.load()
    text = LEDGER.read_text(encoding="utf-8")
    data = tomllib.loads(text)
    have_ids = {c["id"] for c in data["commitment"]}
    have_parties = {p["id"] for p in data["party"]}
    lines = text.splitlines()
    idx = blocks(lines)
    missing = [k for k in AMEND if k not in idx]
    if missing:
        print("not found:", missing)
        return 1
    by_id = {c["id"]: c for c in data["commitment"]}
    # replace from the bottom up so earlier indexes stay valid
    for cid, (st, en) in sorted(((k, idx[k]) for k in AMEND), key=lambda kv: -kv[1][0]):
        new = amend(by_id[cid])
        new.setdefault("status", by_id[cid]["status"])
        new.setdefault("section", by_id[cid]["section"])
        lines[st:en] = dump(new).rstrip("\n").split("\n")

    out = ["", "# ---------------------------------------------------------------------------",
           "# Part 4: CR-059 to CR-070, adopted 15 November 2026 (storyline §§8–14, §25)",
           "# ---------------------------------------------------------------------------", ""]
    for pid, name in PARTIES:
        if pid not in have_parties:
            out.append(dump_party({"id": pid, "name": name}))
    problems = []
    for c in NEW:
        if c["id"] in have_ids:
            problems.append(f"{c['id']}: id exists")
            continue
        hits = story.find(c["quote"])
        if not hits:
            problems.append(f"{c['id']}: quote not found")
            c["status"], c["section"] = "PROPOSED", 0
        else:
            c["status"] = story.label_at(hits[0], c["quote"])
            c["section"] = story.section(hits[0])
        out.append(dump(c))
    LEDGER.write_text("\n".join(lines).rstrip("\n") + "\n" + "\n".join(out), encoding="utf-8")
    tomllib.loads(LEDGER.read_text(encoding="utf-8"))
    for p in problems:
        print(p)
    print(f"amended {len(AMEND)}, added {len(NEW)} commitments and {len(PARTIES)} parties")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
