"""Build the full candidate storyline for CR-059 to CR-070 (15 November 2026).

    python3 outputs/sessions/20261115-integration/build_candidate.py

Takes canon (book-agent/revision/master_storyline.md), replaces §§8-13 with the candidate of
13 November (outputs/sessions/20261113-set-review/merged-storyline-8-13.md, the text of record),
then applies the storyline blocks written since: CR-059 (Columbia), CR-060 (the Legion at
Bannack; §19 Front Range; §25 critics), CR-062 (§14 Sitka), CR-068 (§4), CR-069 (§9, §10, §12, §19)
and CR-070 (§14, §25, §26), and the model's population figures. Writes candidate-full.md here.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
REV = ROOT / "book-agent" / "revision"
HERE = Path(__file__).resolve().parent
canon = (REV / "master_storyline.md").read_text().split("\n")
cand = (ROOT / "outputs/sessions/20261113-set-review/merged-storyline-8-13.md").read_text().rstrip("\n").split("\n")

i8 = canon.index("## 8. The constitutional test of public money and private force (1850–1861)")
i14 = canon.index("## 14. Alaska, Japan, China and the ocean road (1867–1880)")
assert cand[0] == canon[i8]
text = "\n".join(canon[:i8] + cand + [""] + canon[i14:])


def block(cr: str, heading_start: str) -> list[str]:
    """The quoted paragraphs ('> ...') under the storyline heading that starts with heading_start."""
    t = (REV / f"{cr}.md").read_text()
    i = t.index("## Storyline text")
    t = t[i:]
    h = t.index("\n### " + heading_start)
    j = t.find("\n### ", h + 5)
    k = t.find("\n## ", h + 5)
    end = min(x for x in (j, k) if x > 0)
    body = t[h:end].split("\n")[1:]
    paras, cur = [], []
    for line in body:
        if line.startswith("> "):
            cur.append(line[2:])
        elif line.strip() == ">":
            if cur:
                paras.append(" ".join(cur)); cur = []
        else:
            if cur:
                paras.append(" ".join(cur)); cur = []
    if cur:
        paras.append(" ".join(cur))
    assert paras, (cr, heading_start)
    return paras


def rep(old: str, new: str, count: int = 1) -> None:
    global text
    n = text.count(old)
    assert n == count, (old[:80], n)
    text = text.replace(old, new)


# ---------------------------------------------------------------- §4 (CR-068)
p = block("CR-068", "§4")[0]
m = re.search(r"\*\*\[PROPOSED — CR-028\]\*\* Trist, recalled but staying on[^\n]*", text)
assert m
text = text[:m.end()] + " " + p.strip() + text[m.end():]

# ---------------------------------------------------------------- §9 (CR-069)
b = block("CR-069", "§9, replacing")
rep("**[OPEN]** Alternate financial legislation, bullion and exchange flows, borrowing terms, price effects and the quantitative burden.",
    "\n\n".join(b))

# ---------------------------------------------------------------- §10 (CR-069; CR-060 Bannack)
b = block("CR-069", "§10, replacing")
rep("Finance and transport sustain the gains. Ralston's commercial relationships help bridge the gap between future public "
    "revenues and immediate payments to suppliers, workers and carriers.", b[0])
rep("**[OPEN]** Particular advances, security, interest, payment crises, routes, crossings and dates; Ralston's historical "
    "1864 Bank of California must not be silently placed in the early war.",
    "**[OPEN]** The amounts of particular advances, routes and crossings.")
b = block("CR-069", "§10, at the retaking of Washoe")
rep("No second convention meets, and there is no State of Nevada. **[OPEN]** Exact forces and routes; civilian and Native "
    "authority require their own agreements.",
    "No second convention meets, and there is no State of Nevada. **[OPEN]** Exact forces and routes; civilian and Native "
    "authority require their own agreements.\n\n" + b[0])
bannack = ("Lincoln's governors of Idaho and Montana keep their offices and little else. In the June rise of 1864 a steamer "
           "lands a company of the Union's regulars at Fort Benton")
src = (REV / "CR-060.md").read_text()
m = re.search(re.escape(bannack) + r".*?Fort Benton stays a Union landing,", src)
assert m
rep("Lincoln's governors of Idaho and Montana keep their offices and little else. Fort Benton stays a Union landing,", m.group(0))

# ---------------------------------------------------------------- §12 (CR-059 Columbia; CR-069)
src = (REV / "CR-059.md").read_text()
m = re.search(r"North of the river no vote is owed:.*?has died in June\. ", src)
assert m
rep("They have signed their own compacts, to take effect only if Oregon accedes.",
    "They have signed their own compacts, to take effect only if Oregon accedes. " + m.group(0).rstrip())
b = block("CR-069", "§12")
rep("Elias, once dispossessed by creditors, becomes creditor to the Union's bankers.",
    "Elias, once dispossessed by creditors, becomes creditor to the Union's bankers. " + b[0].strip())

# ---------------------------------------------------------------- §14 (CR-062, CR-070)
gold = ("Northern gold income belongs to the later Juneau and Klondike developments; the northern administration must "
        "initially pay for harbors and transport without a ready gold windfall.")
i = text.index(gold)
j = text.index("\n", i)
k62 = block("CR-062", "§14")
k70 = block("CR-070", "§14")
text = text[:i].rstrip() + text[i + len(gold):j] + "\n\n" + "\n\n".join(["<!-- CR-062 -->" + k62[0]] + k70) + text[j:]

# ---------------------------------------------------------------- §19 (CR-069; CR-060)
b = block("CR-069", "§19")
rep("so that Carquinez, built on the gold royalty, and Ralston College become Pacifica's colleges of gold and silver.",
    "so that Carquinez, built on the gold royalty, and Ralston College become Pacifica's colleges of gold and silver. "
    "<!-- CR-069 -->" + b[0].strip())
b = block("CR-060", "§19")
m = re.search(r"\n[^\n]*In 1881 Tom Talbert finds yellow uranium-vanadium ore[^\n]*", text)
assert m
text = text[:m.end()] + "\n\n<!-- CR-060 -->" + b[0] + text[m.end():]

# ---------------------------------------------------------------- §25 (CR-060 critics; CR-070 seals, copper and the road)
b = block("CR-060", "§25")
rep("Union critics answer with Bear River, the Chinese massacres, the Calamba evictions and the fugitive agreement.",
    b[0].replace("**[PROPOSED — CR-060]** ", "<!-- CR-060 -->**[PROPOSED — CR-060]** "))
b = block("CR-070", "§25, the seals")
new = b[0].strip().strip("… ").strip()
old_seal = ("Pacifica owns the Pribilofs and makes no claim that the Bering Sea is closed; **[PROPOSED — CR-058]** in the 1890s "
            "**[APPROVED — CR-058]** it proposes a conservation regime and seats Canadian delegates at the table, and the "
            "four-power convention bans pelagic sealing and gives Canada fifteen percent of the Pribilof catch, fifteen "
            "percent of the Commander Islands' and ten percent of Robben Island's.")
rep(old_seal, "<!-- CR-070: the seal convention of 1886 -->" + new)
kl = ("The approved Klondike policy holds the Alaska boundary firmly while offering Canada fair transit; a proposed "
      "Skagway–Whitehorse railway, assay and banking capture route income from Canadian gold.")
b = block("CR-070", "§25, after")
rep(kl, kl.replace("a proposed Skagway", "a Skagway") + " " + b[0].strip())
rep("the year of the first fur-seal convention; ", "")

# ---------------------------------------------------------------- §26 (CR-070)
b = block("CR-070", "§26")
rep("escorts, diversions and the hunt tie down half of Japan's cruisers. In May 1905, as the squadron returns from its "
    "spring cruise, Kuroda Kiyoshi gathers",
    "escorts, diversions and the hunt tie down half of Japan's cruisers. " + b[0].strip() + " In May 1905, as the squadron "
    "returns from its spring cruise, he gathers")

# ---------------------------------------------------------------- population (model of 15 November 2026)
rep("about 37 million by 1932 (MODEL; CR-052)", "about 39 million by 1932 (MODEL; CR-052, CR-059 to CR-070)")
rep("about 5.7 against 4.9 million of some 37 million **[MODEL — CR-052]**",
    "about 6.2 against 5.0 million of some 39 million **[MODEL — CR-052]**")
rep("counts about 37 million people **[MODEL — CR-052]**", "counts about 39 million people **[MODEL — CR-052]**")

# ---------------------------------------------------------------- fixes after the fresh-context review (review-1.md)
# B1 (author, 15 Nov: "Young acts; paid after")
rep("In the June rise of 1864 a steamer lands a company of the Union's regulars at Fort Benton with orders to garrison Montana's new capital at Bannack. At Monterey's request Young sends Lot Smith's cavalry north by the Montana Trail, beyond the roads the Compact binds the Legion to keep, and Pacifica pays it in gold for that summer, the only pay the Legion ever has from Pacifica. It is at Bannack first, and the regulars turn back at the Sun River without a fight; the gold of Alder Gulch stays inside Pacifica's freight and coin. Fort Benton stays a Union landing, and in the June rise the steamers from St Louis",
    "**[APPROVED — CR-060]** In the summer of 1864 a steamer lands a company of the Union's regulars at Fort Benton with orders to garrison Montana's new capital at Bannack. Elias orders nothing. Young, whose freighters live on the Montana Trail, sends Lot Smith's cavalry of the Legion north on Deseret's own decision, beyond the roads the Compact binds it to keep; it is at Bannack first, and the regulars turn back at the Sun River without a fight. The gold of Alder Gulch stays inside Pacifica's freight and coin. When the peace of 1865 leaves western Montana on Pacifica's side, the Republic pays the Legion in gold for that summer, the only pay it ever has from Pacifica. **[PROPOSED — CR-060]** Fort Benton stays a Union landing, and in the June rise the steamers from St Louis")
# S1, S11
rep("<!-- CR-069: the steamers return; Ralston lends -->**[PROPOSED — CR-069]** The Steamer Day Agreement ends with the treaty, the treasure steamers sail for New York again in 1866, and the gold the coast held back during the war goes east in 1866 and 1867. When the Senate will not take the Republic's loan, the money is lent privately through Ralston's bank as the Republic's agent, which leads the lending to the Union's bankers and the transit companies with a share of its own.",
    "<!-- CR-069: the steamers return -->**[PROPOSED — CR-069]** The Steamer Day Agreement ends with the treaty of December 1865, the treasure steamers sail for New York again in 1866, and the gold the coast held back during the war goes east in 1866 and 1867.")
m = re.search(r"The money is lent privately instead, to New York and Philadelphia houses and the transit companies\.", text)
assert m, "S1 anchor"
text = text.replace(m.group(0), "The money is lent privately instead, through Ralston's bank as the Republic's agent, which takes a share of its own, to New York and Philadelphia houses and the transit companies.")
# S2
rep("Larkin brings that number to Monterey in June with the ratified convention, and Elias reads it there.",
    "The number travels to Monterey with the convention, and Elias reads it there.")
# S3, S5 (P10, P11 decided)
rep("**[PROPOSED — CR-069]** William Ralston, Ohio-born, takes the Republic's oath in July 1861, with his family in Ohio and his partner Eugene Kelly in New York. When the news of New York's suspension reaches San Francisco by the Panama mail",
    "**[APPROVED — CR-069]** William Ralston, Ohio-born, takes the Republic's oath in July 1861, with his family in Ohio and his partner Eugene Kelly in New York. **[PROPOSED — CR-069]** No wire carries news to an enemy: the Union's line, finished in October 1861, carries nothing for Pacifica past Fort Churchill. When the news of New York's suspension reaches San Francisco by the Panama mail")
rep("Elias means to stop the export of coin by decree. Ralston asks him not to and brings him the houses' word instead, and on the steamer day of 1 March they sign",
    "**[APPROVED — CR-069]** Elias means to stop the export of coin by decree. Ralston asks him not to and brings him the houses' word instead, and on the steamer day of 1 March they sign")
rep("Most keep it, and the Republic owes them for a measure it never had to decree. When the Republic borrows",
    "Most keep it, and the Republic owes them for a measure it never had to decree. **[PROPOSED — CR-069]** When the Republic borrows")
# S4, S9 (P12 decided), nit on two "1864" openings
rep("**[PROPOSED — CR-069]** In the spring of 1864, with gold at its height in New York, Ralston gives the *Alta* a letter offering his house Union paper for its coin, without the sender's name, and says the house refused it. In 1864 Ralston and his partner Joseph A. Donohoe, who wants the firm's future in New York, quarrel in private",
    "**[APPROVED — CR-069]** In the spring of 1864, with gold climbing in New York, a letter from the firm's own partner there offers the house Union paper for its coin. Ralston gives the *Alta* the letter without the sender's name and says the house refused it. **[PROPOSED — CR-069]** That year he and his partner Joseph A. Donohoe, who wants the firm's future in New York, quarrel in private over it")
# S5: the memorial (U7, U8 approved); MODEL label
rep("<!-- CR-069: the bankers' memorial and the choice of paper -->**[PROPOSED — CR-069]**",
    "<!-- CR-069: the bankers' memorial and the choice of paper -->**[APPROVED — CR-069]**")
rep("**[OPEN]** The amounts of the Union's paper and the premium's figures, which are MODEL.",
    "**[MODEL]** The amounts of the Union's paper and the premium's figures.")
rep("about 6.2 against 5.0 million of some 39 million **[MODEL — CR-052]**", "about 6.2 against 5.0 million of some 39 million **[MODEL — CR-059]**")
rep("counts about 39 million people **[MODEL — CR-052]**", "counts about 39 million people **[MODEL — CR-059]**")
rep("(MODEL; CR-052, CR-059 to CR-070)", "(MODEL; CR-052, CR-059 to CR-068, CR-070)")
# S10 and the label's reach (l. 905)
rep("<!-- CR-060 -->**[PROPOSED — CR-060]** Union critics answer with the Owyhee hangings and the camp they came too late for, the Chinese massacres,",
    "Union critics answer with the Chinese massacres,")
rep("The depression, Coxey's Army and Pullman in 1893–1894 give the weekly further material.",
    "The depression, Coxey's Army and Pullman in 1893–1894 give the weekly further material. <!-- CR-060 -->**[PROPOSED — CR-060]** Among the critics' cases is the Paiute camp killed in the Owyhee in 1865–66, which Pacifica's courts could only avenge.")
# S7
rep("**[OPEN]** What becomes of the Union's Colorado, Denver and the plains; the author's preferred answer is that it is attached to Kansas in the 1880s, and that the page may say *Denver, Kansas*.",
    "**[OPEN]** What becomes of the Union's Colorado, Denver and the plains, perhaps attached to Kansas in the 1880s.")
# Front Range nits
rep("The Front Range comes over the way Deseret and Washoe came. Its gold fails in the refractory ores of 1864–67, its statehood is refused,",
    "The Front Range comes over the way Idaho and Deseret came, by its own vote. Its gold fails in the refractory ores of 1864–67, its statehood bills are vetoed in Washington,")
# S8: the White Pass
rep("and the railway, the assay office and the bank are building before the stampede of 1897.",
    "and the railway over the White Pass from Skagway is building before the stampede of 1897, on a compact with the Chilkoot, whose ground the pass is, that gives them a share of its freight for the packing it will end.")
# nits
rep("Ralston's credit and Crocker's construction teams, and Kelly's experiments,", "Ralston's credit and Crocker's construction teams, and William Kelly's experiments,")
rep("\nKelly's metallurgical experiments begin a slower undertaking", "\nWilliam Kelly's metallurgical experiments begin a slower undertaking")
rep("and the chambers vote him a station and no fortress;", "and the chambers vote the north a station and no fortress;")
rep("From 1870 the chambers tax every case of salmon packed,", "The Columbia's canners come north a decade early, and from 1870 the chambers tax every case of salmon packed,")
rep("<!-- CR-069 -->**[PROPOSED — CR-069]** The city names it for the banker who kept his doors open in the run of 1862 and published the offer he refused in 1864, and the silver his Gold Hill agency brought to San Francisco endows it.",
    "<!-- CR-069 -->**[PROPOSED — CR-069]** The houses chose his name because he kept his doors open in the run of 1862 and published the offer he refused in 1864, and the silver his Gold Hill agency brought to San Francisco endows the college.")
rep("North of the river no vote is owed: Washington Territory held no promise from the Union,", "North of the river no vote is owed: the Union made Washington Territory no offer of statehood,")

(HERE / "candidate-full.md").write_text(text)
print("candidate-full.md:", len(text.split("\n")), "lines")
