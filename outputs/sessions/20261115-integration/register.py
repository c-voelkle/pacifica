"""Add the register entries of CR-059 to CR-065 and CR-067 to CR-070 (approved 15 November 2026)."""
import json, re
from pathlib import Path
REV = Path(__file__).resolve().parents[3] / "book-agent" / "revision"
AUTH = ('Author, 15 November 2026: "I approve the crs" (the set CR-059 to CR-065 and CR-067 to CR-070, after the '
        'integration candidate and its fresh-context review), following the author\'s decisions recorded in each '
        'decision record (7-15 November 2026) and the decision sheet of 12 November 2026.')
REQ = {
 "CR-059": "Oregon and the Northwest: the House's rejection of 1859, the Enabling Act of 1861, the occupation and civil compacts, the Walla Walla convention and the interior gate, the Oregon article and the vote of October 1866, the exclusion bargain limited to non-citizens, the Native article; Washington Territory accedes as Columbia (Part IX).",
 "CR-060": "The interior: Deseret's articles (December 1862), the Compact of 24 July 1863 and accession in 1867; Bear River as a limited action; Washoe retaken in 1864 with no State of Nevada; Idaho and western Montana; the Legion paid only for Bannack (1864, on Young's decision, paid after the peace); the Colorado line; the Owyhee prosecution.",
 "CR-061": "The Southwest: the Rio Grande column of 1862, Fort Craig and Fort Garland, the Navajo homeland and the Apache peace, the end of peonage, the Texas line closed to fugitives from 1863 and no one returned, New Mexico's accession in 1867.",
 "CR-062": "The peace: the armistices of 1865, the Western treaty of December 1865 and its ratification in 1867, the $40m in six instalments, the Senate's refusal of the Treasury loan and the private lending, Alaska and the handover at Sitka, the residents' and nations' articles.",
 "CR-063": "The Gulf without New Orleans: the Confederacy keeps Louisiana and its ports; Vicksburg's army marches out on 17-18 May 1863; the Matamoros credit; no Fort Fisher; the February 1865 expedition.",
 "CR-064": "The Union's war without Sherman: Shiloh, the western command and the campaigns of 1862-64, Thomas against Polk's flank in 1864.",
 "CR-065": "The election of 1864 and the lame-duck winter: McClellan's victory, Pacifica's silence before the vote, the Gold Room's fall on the result.",
 "CR-067": "Pacifica's command structure, 1855-1867: political control, the army and its departments, the navy and its board.",
 "CR-068": "The agon of Elias Thorne and Abraham Lincoln, 1838-1867, and how the Chronicler writes Lincoln; Lincoln dies at Springfield in November 1872.",
 "CR-069": "The coast's gold in the war: the steamers stop in July 1861, the banks' terms and the run on the Sub-Treasury, the choice of paper, Ralston's run, the Steamer Day Agreement of 1 March 1862, the coin bonds, the Bank of California of 4 July 1864, the agency of 1867.",
 "CR-070": "Alaska pays early: the Northern Commission chartered by bill under de la Guerra and Davidson, the finder's compacts and Kowee, the settler garrison, the seals, salmon and sea otter, the Alaska line and the cables to 1903, the Chilkoot compact and the Yukon road, the Chitina's copper.",
}
LINCOLN = {"add_person": {"id": "CT-ABRAHAM-LINCOLN", "aliases": ["Abraham Lincoln"], "born": 1809, "died": 1872}}

def facts(cr):
    t = (REV / f"{cr}.md").read_text()
    i = t.find("## Fact changes"); j = t.find("\n## ", i + 5)
    m = re.search(r"```json\n(.*?)```", t[i:j], re.S)
    out = json.loads(m.group(1)) if m else []
    ct = t.find("## Canon tensions"); cte = t.find("\n## ", ct + 5)
    for mm in re.finditer(r"### (CT\d+)(.*?)(?=\n### CT|\Z)", t[ct:cte], re.S):
        body = mm.group(2)
        blocks = [b for b in re.findall(r"```json\n(.*?)```", body, re.S) if b.strip() not in ("[]", "")]
        if not blocks:
            continue
        dec = " ".join(l for l in body.split("\n") if "Decision" in l or "Decided" in l)
        if re.search(r"\bamend", dec, re.I):
            for f in json.loads(blocks[0]):
                if f not in out:
                    out.append(f)
    if cr == "CR-068":
        out.append(LINCOLN)
    return out

d = json.loads((REV / "change_requests.json").read_text())
have = {r["id"] for r in d["requests"]}
for cr in ["CR-059", "CR-060", "CR-061", "CR-062", "CR-063", "CR-064", "CR-065", "CR-067", "CR-068", "CR-069", "CR-070"]:
    assert cr not in have, cr
    title = (REV / f"{cr}.md").read_text().split("\n", 1)[0].lstrip("# ").split(" — ", 1)[1]
    d["requests"].append({
        "id": cr, "title": title, "status": "approved_integrated_local_labels_retained", "approved_on": "2026-11-15",
        "decision_record": f"{cr}.md", "authorization": AUTH, "requirements": [REQ[cr]],
        "open": [f"The items still marked OPEN in {cr}.md (Open decisions) and in the storyline; amounts MODEL (finance/CR-059-068-workbook.md)."],
        "facts": facts(cr)})
    print(cr, len(d["requests"][-1]["facts"]), "facts")
(REV / "change_requests.json").write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n")
