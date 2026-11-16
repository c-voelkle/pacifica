"""Historical baseline for CR-071 Part I: the counties that existed on 1 August 1887
on the territory Pacifica holds, with census populations, and a regional split of the
model's 1887 residents.

    python3 population/counties_1887.py   -> outputs/counties_1887.csv, outputs/counties_1887.md

Our timeline's counties and boundaries: Atlas of Historical County Boundaries (Newberry
Library, CC0), extract in data/counties/newberry_1887.csv. County populations: decennial
census totals as given in each county's Wikipedia article (data/counties/census_by_county_raw.txt),
checked against the verified state totals in data/census.toml. The regional split of
Pacifica's residents (section 2 of the output) is MODEL and waits for the author's decision.
"""
from __future__ import annotations

import csv
import math
import tomllib
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).parent
DATA = HERE / "data" / "counties"
OUT = HERE / "outputs"

STATE = {"AZ": "Arizona", "CA": "California", "CO": "Colorado", "ID": "Idaho", "MT": "Montana",
         "NM": "New_Mexico", "NV": "Nevada", "OR": "Oregon", "UT": "Utah", "WA": "Washington",
         "WY": "Wyoming"}
# Canon's old units (CR-071 outline, section 0 and I2)
REGION = {"CA": "California", "OR": "Oregon", "WA": "Columbia", "ID": "Idaho",
          "MT": "Western Montana", "NV": "Washoe", "UT": "Deseret", "WY": "Deseret (southwest Wyoming)",
          "NM": "New Mexico", "AZ": "New Mexico (Arizona county)", "CO": "The Rockies (Colorado)"}
WHOLE = {"AZ", "CA", "ID", "NM", "NV", "OR", "UT", "WA"}
# 1 August 1887 lies this far between the censuses of 1 June 1880 and 1 June 1890
F1887 = (1887 + 7 / 12 - (1880 + 5 / 12)) / 10
MODEL_TOTAL_1887 = None  # read from outputs/canon_by_year.csv


def load():
    ov = tomllib.load(open(DATA / "overrides.toml", "rb"))
    pop = {}
    for line in open(DATA / "census_by_county_raw.txt", encoding="utf-8"):
        if line.startswith("#") or not line.strip():
            continue
        s, n, *v = line.strip().split(";")
        pop[f"{s};{n}"] = [int(x) if x else None for x in v]  # 1870, 1880, 1890, 1900
    atlas = [r for r in csv.DictReader(open(DATA / "newberry_1887.csv", encoding="utf-8"))
             if r["kind"] == "county"]
    return ov, pop, atlas


def build():
    ov, pop, atlas = load()
    rows = []
    for a in atlas:
        key = f"{a['state']};{a['county']}"
        p70, p80, p90, _ = pop.get(key, [None] * 4)
        note = []
        if key in ov["residual_1880"]:
            p80 = ov["residual_1880"][key]
            note.append("1880 by residual")
        if key in ov["unverified_1890"]:
            p90 = ov["unverified_1890"][key]
            note.append("1890 unverified")
        kids = [k for k, par in ov["parents"].items()
                if k.split(";")[0] == a["state"] and par == a["county"]]
        if kids:
            p90 = (p90 or 0) + sum(pop[k][2] for k in kids)
            note.append("1890 with " + ", ".join(k.split(";")[1] for k in kids))
        share = 1.0 if a["state"] in WHOLE else float(ov["pacifica_share"].get(key, 0))
        rows.append(dict(state=a["state"], county=a["county"], region=REGION[a["state"]],
                         area_sqmi=int(a["area_sqmi"]), created=a["created"],
                         pop1870=p70, pop1880=p80, pop1890=p90, share=share, note="; ".join(note)))
    # 1887: log-linear between the censuses where both exist, else the state's own ratio; then
    # every state is scaled to its log-linear total.
    states = tomllib.load(open(HERE / "data" / "census.toml", "rb"))["states"]
    by = defaultdict(list)
    for r in rows:
        by[r["state"]].append(r)
    check = {}
    for s, rs in by.items():
        t80, t90 = states[STATE[s]][3], states[STATE[s]][4]
        s80 = sum(r["pop1880"] or 0 for r in rs)
        s90 = sum(r["pop1890"] or 0 for r in rs)
        check[s] = (len(rs), s80, t80, s90, t90)
        ratio = (s80 / s90) ** (1 - F1887)  # the state's 1887 over 1890, on county sums
        for r in rs:
            if r["pop1880"] and r["pop1890"]:
                r["raw"] = math.exp((1 - F1887) * math.log(r["pop1880"]) + F1887 * math.log(r["pop1890"]))
            elif r["pop1890"]:
                r["raw"] = r["pop1890"] * ratio
            else:
                r["raw"] = 0.0
        target = math.exp((1 - F1887) * math.log(s80) + F1887 * math.log(s90))
        k = target / sum(r["raw"] for r in rs)
        for r in rs:
            r["est1887"] = round(r.pop("raw") * k)
            r["pacifica1887"] = round(r["est1887"] * r["share"])
    return ov, rows, check


def model_1887():
    for r in csv.DictReader(open(OUT / "canon_by_year.csv")):
        if r["year"] == "1887":
            return {k: int(float(v)) for k, v in r.items() if k != "year"}
    raise SystemExit("run population/canon.py first")


# Regional variants (MODEL, for the author's decision). The interior joined in 1867 at its
# historical size (joins_cr059_068.toml). `interior` is how many times its historical 1887
# population each acceded region holds in 1887; California takes the remainder of the model total.
VARIANTS = [
    ("V1 interior as in history", 1.0),
    ("V2 interior one and a half times history", 1.5),
    ("V3 interior twice history", 2.0),
    ("V4 every region in proportion", None),
]
STRAWMAN = {"California": 40 + 1, "Oregon": 14, "Columbia": 14, "Deseret": 9, "Washoe": 5,
            "Idaho and western Montana": 9, "Arizona": 6, "New Mexico": 9, "The Rockies": 6,
            "Hawaii": 5, "Alaska": 5}
GROUP = {"California": "California", "Oregon": "Oregon", "Columbia": "Columbia", "Idaho": "Idaho and western Montana",
         "Western Montana": "Idaho and western Montana", "Washoe": "Washoe", "Deseret": "Deseret",
         "Deseret (southwest Wyoming)": "The Rockies", "New Mexico": "New Mexico",
         "New Mexico (Arizona county)": "Arizona", "The Rockies (Colorado)": "The Rockies"}


def main():
    ov, rows, check = build()
    m = model_1887()
    fields = ["state", "county", "region", "area_sqmi", "created", "pop1870", "pop1880", "pop1890",
              "est1887", "share", "pacifica1887", "note"]
    with open(OUT / "counties_1887.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    isl = ov["islands"]
    hawaii87 = [round(math.exp((1 - 0.5) * math.log(a) + 0.5 * math.log(b))) for a, b in zip(isl["y1884"], isl["y1890"])]
    alaska80 = sum(ov["alaska"]["y1880"])

    L = []
    A = L.append
    A("# The counties of 1 August 1887 on Pacifica's territory: historical baseline and a regional split\n")
    A("Built by `population/counties_1887.py`. Sections 1 and 3 are our timeline (sources below). "
      "Section 2 is MODEL and waits for the author's decision. Nothing here is canon.\n")
    A("## 1. Our timeline: counties, area and people by old unit\n")
    A("Counties whose people would be Pacifican in 1887. \"Whole\" counts a county if any of it lies on "
      "Pacifica's side; \"split\" lists those the line cuts. Population is the census's, which before 1890 "
      "leaves out Indians not taxed.\n")
    A("| Old unit | Counties, 1 Aug 1887 | Area, sq mi | 1880 | 1890 (1887 lines) | 1887 est. | People per county | Median county |")
    A("|---|---|---|---|---|---|---|---|")
    reg = defaultdict(list)
    for r in rows:
        if r["share"] > 0:
            reg[r["region"]].append(r)
    order = ["California", "Oregon", "Columbia", "Idaho", "Western Montana", "Washoe", "Deseret",
             "Deseret (southwest Wyoming)", "New Mexico", "New Mexico (Arizona county)", "The Rockies (Colorado)"]
    hist = {}
    tot = [0, 0, 0, 0, 0]
    for g in order:
        rs = reg[g]
        p80 = round(sum((r["pop1880"] or 0) * r["share"] for r in rs))
        p90 = round(sum((r["pop1890"] or 0) * r["share"] for r in rs))
        p87 = sum(r["pacifica1887"] for r in rs)
        hist[g] = p87
        full = [r for r in rs if r["share"] == 1]
        med = sorted(r["est1887"] for r in rs)[len(rs) // 2]
        area = sum(r["area_sqmi"] for r in full)
        split = len(rs) - len(full)
        A(f"| {g} | {len(rs)}{f' ({split} split)' if split else ''} | {area:,} | {p80:,} | {p90:,} | {p87:,} | {p87 // len(rs):,} | {med:,} |")
        for i, v in enumerate([len(rs), area, p80, p90, p87]):
            tot[i] += v
    A(f"| **Mainland** | **{tot[0]}** | **{tot[1]:,}** | **{tot[2]:,}** | **{tot[3]:,}** | **{tot[4]:,}** | {tot[4] // tot[0]:,} | |")
    h87 = sum(hawaii87)
    A(f"| Hawaii | no counties before 1905; 5 island groups | {sum(isl['area_sqmi']):,} | (1884) {sum(isl['y1884']):,} | {sum(isl['y1890']):,} | {h87:,} | | |")
    A(f"| Alaska | none; 6 census divisions in 1880 | about 586,000 | {alaska80:,} | | | | |")
    A("")
    A("Hawaii by island, 1884 / 1890: " + "; ".join(f"{n} {a:,} / {b:,}" for n, a, b in zip(isl["names"], isl["y1884"], isl["y1890"])) + ".")
    A("Alaska in 1880 by division (Petroff): " + "; ".join(f"{n} {v:,}" for n, v in zip(ov["alaska"]["names"], ov["alaska"]["y1880"])) + "; 430 white and 1,756 Creole residents.\n")
    A("Baja California (the purchase of 1867, PROPOSED in the storyline; switched off in the workbook) is not in this table or in the outline's strawman.\n")

    A("## 2. Where Pacifica's people of 1887 live (MODEL; for decision)\n")
    mt = m["model_total"]
    A(f"The population model has {mt:,} residents at the end of 1887 and no regions. Its only regional memory is "
      f"`joined_territories`, {m['joined_territories']:,}: the head counts of 1867 with their natural increase and no "
      f"migrant after 1867. Read literally, the interior and the Northwest hold {m['joined_territories'] / mt:.0%} of the people.\n")
    A("The variants below fix Hawaii at one and a half times its historical population (Japanese settlement; MODEL) "
      "and Alaska at 40,000 (Petroff's count plus the garrison of settlers; MODEL), set each acceded unit at a multiple "
      "of its historical 1887 population, and give California the rest.\n")
    hist_total = tot[4]
    groups = ["California", "Oregon", "Columbia", "Idaho and western Montana", "Washoe", "Deseret",
              "New Mexico", "Arizona", "The Rockies", "Hawaii", "Alaska"]
    hg = defaultdict(int)
    for g, v in hist.items():
        hg[GROUP[g]] += v
    hawaii_p, alaska_p = round(h87 * 1.5), 40000
    table = {}
    for name, mult in VARIANTS:
        if mult is None:
            k = (mt - hawaii_p - alaska_p) / hist_total
            v = {g: hg[g] * k for g in hg}
        else:
            v = {g: hg[g] * mult for g in hg if g != "California"}
            v["California"] = mt - hawaii_p - alaska_p - sum(v.values())
        v["Hawaii"], v["Alaska"] = hawaii_p, alaska_p
        table[name] = v
    A("| Old unit | History 1887 | " + " | ".join(n for n, _ in VARIANTS) + " | Strawman counties (I2) |")
    A("|---|---|" + "---|" * (len(VARIANTS) + 1))
    for g in groups:
        h = hg.get(g, h87 if g == "Hawaii" else alaska80)
        A(f"| {g} | {h:,} | " + " | ".join(f"{table[n][g] / 1000:,.0f}k ({table[n][g] / mt:.0%})" for n, _ in VARIANTS) + f" | {STRAWMAN[g]} |")
    A("")
    A("**What each variant does to the Senate of 1888** (123 county senators; the strawman's counts; "
      "California's 41 include San Francisco):\n")
    A("| | " + " | ".join(n.split()[0] for n, _ in VARIANTS) + " |")
    A("|---|" + "---|" * len(VARIANTS))
    A("| California's share of the people | " + " | ".join(f"{table[n]['California'] / mt:.0%}" for n, _ in VARIANTS) + " |")
    A("| California's share of county senators | " + " | ".join(["33%"] * len(VARIANTS)) + " |")
    A("| People per Californian county | " + " | ".join(f"{table[n]['California'] / 41 / 1000:,.0f}k" for n, _ in VARIANTS) + " |")
    A("| People per county elsewhere on the mainland | " + " | ".join(
        f"{sum(v for g, v in table[n].items() if g not in ('California', 'Hawaii', 'Alaska')) / 72 / 1000:,.0f}k" for n, _ in VARIANTS) + " |")
    A("| Counties California would have by population alone (of 124) | " + " | ".join(f"{124 * table[n]['California'] / mt:.0f}" for n, _ in VARIANTS) + " |")
    A("")

    A("## 3. Sources and checks\n")
    A("- **Counties, dates and areas:** Atlas of Historical County Boundaries (Newberry Library; CC0), every county "
      "whose boundary version covers 1 August 1887 (`data/counties/newberry_1887.csv`).")
    A("- **County populations:** census totals as given in each county's English Wikipedia article, read on "
      "16 November 2026 (`data/counties/census_by_county_raw.txt`). Status: identity-checked for 1880 where the state sums close.")
    A("- **1887:** log-linear between the censuses of 1880 and 1890, each state scaled to its own interpolated total; "
      "counties created between August 1887 and 1890 are folded into their parents (`overrides.toml`). An estimate.")
    A("- **The line in Montana, Wyoming and Colorado:** `[pacifica_share]` in `overrides.toml`; the split counties' fractions are guesses.\n")
    A("| State | Counties | Sum of counties 1880 | Census 1880 | Difference | Sum 1890 | Census 1890 | Difference |")
    A("|---|---|---|---|---|---|---|---|")
    for s in sorted(check):
        n, s80, t80, s90, t90 = check[s]
        A(f"| {s} | {n} | {s80:,} | {t80:,} | {t80 - s80:,} | {s90:,} | {t90:,} | {t90 - s90:,} |")
    A("")
    A("1880: Colorado (444), Montana (170) and Oregon (100) do not close and are to be traced. "
      "1890: the census totals include Indians on reservations, whom the county figures leave out, so the differences are expected; "
      "San Francisco, Ormsby and Alturas for 1890 are unverified (`overrides.toml`).")
    (OUT / "counties_1887.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L))


if __name__ == "__main__":
    main()
