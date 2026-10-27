"""Where Pacifica's population comes from: a chain from 1846, and the migration flows.

Chain (all runs use the same engine and our-timeline vital rates, so each step is
exactly the contribution of what it adds; at 1846 every step is zero):

  1. The 1846 Californians and their descendants (no territory, no migration)
  2. + territories joined, with their descendants
  3. + migration streams, with descendants, one stream at a time
  4. + the sheet's natural-increase rate instead of age structure  (= the People sheet)

Against it: our timeline on the same territory (census), from each territory's
canon join year, growing at its real census growth.

Flows: the sheet's arrivals by decade against US immigration in the same decade
(DHS yearbook), and against our timeline's growth of the same territory.

Run:  python3 population/flows.py   -> population/outputs/flows.md, flows_by_year.csv
"""
from __future__ import annotations

import csv
import math
import sys
from pathlib import Path

import canon
import cohort
from cohort import load

OUT = Path(__file__).resolve().parent / "outputs"
KEY = [1850, 1856, 1862, 1870, 1880, 1890, 1900, 1910, 1920, 1932]

# The sheet's territory joins and the census states whose growth stands for them.
# Partial areas (Montana camps, Western Slope, SW Wyoming, Baja) grow at the
# whole state's or territory's census growth: an approximation.
JOINS = {
    1862: ("Northwest, Arizona and New Mexico", ["Oregon", "Washington", "Arizona", "New_Mexico"]),
    1863: ("Deseret, Idaho and Montana camps", ["Utah", "Idaho", "Montana"]),
    1864: ("Washoe (Nevada)", ["Nevada"]),
    1865: ("Western Slope and SW Wyoming", ["Colorado", "Wyoming"]),
    1867: ("Alaska and Baja", ["Alaska"]),
}


def loglin(years: list[int], values: list[float], y: float) -> float:
    pts = [(a, b) for a, b in zip(years, values) if b == b and b > 0]
    if y <= pts[0][0]:
        return pts[0][1]
    if y >= pts[-1][0]:
        return pts[-1][1]
    for (y0, v0), (y1, v1) in zip(pts, pts[1:]):
        if y0 <= y <= y1:
            return math.exp(math.log(v0) + (math.log(v1) - math.log(v0)) * (y - y0) / (y1 - y0))


# ---------------------------------------------------------------------------
# Our timeline on the same territory
# ---------------------------------------------------------------------------

def our_timeline(sheet: dict) -> dict[int, dict]:
    c = load("census")
    st, hi, ca = c["states"], c["hawaii"], c["california"]
    native = dict(zip(ca["native_estimate_years"], ca["native_estimate"]))
    # California: non-Native residents from the census (total minus enumerated Indians;
    # 1910-30 minus 16,000) plus the Native estimates. Before 1850 the non-Native
    # count runs log-linearly from the sheet's 1846 non-Native residents.
    non_native_years = [1846] + ca["years"] + [1910, 1920, 1930]
    non_native = ([sheet[1846]["start"] - ca["native_estimate"][0]]
                  + [t - i for t, i in zip(ca["total"], ca["indian_enumerated"])]
                  + [v - 16000 for v in st["California"][6:9]])
    hawaii_years = hi["years"] + [1910, 1920, 1930]
    hawaii_vals = hi["total"] + st["Hawaii"][6:9]
    out = {}
    for y in range(1846, 1933):
        nat = loglin([1846] + list(native), [native[1848]] + list(native.values()), y)
        row = {"California": loglin(non_native_years, non_native, y) + nat}
        if y >= canon.HAWAII_JOIN:
            row["Hawaii"] = loglin(hawaii_years, hawaii_vals, y)
        for jy, (label, states) in JOINS.items():
            if y >= jy:
                def total(t):
                    return sum(loglin(st["years"], st[s], t) for s in states)
                row[label] = sheet[jy]["join"] * total(y) / total(jy)
        out[y] = row
    return out


# ---------------------------------------------------------------------------
# Chain
# ---------------------------------------------------------------------------

def chain() -> dict:
    base, meta = canon.run(joins=False, streams=())
    terr, _ = canon.run(joins=True, streams=())
    full, _ = canon.run(joins=True)
    without = {s: canon.run(joins=True, streams=tuple(x for x in canon.STREAMS if x != s))[0]
               for s in canon.STREAMS}
    return {"base": base, "terr": terr, "full": full, "without": without, "sheet": meta["sheet"]}


def decade_flows(sheet: dict) -> list[dict]:
    imm = load("us_immigration")
    t1, t2 = imm["table1"], imm["table2"]
    rows = []
    for i, label in enumerate(t1["decades"]):
        y0 = int(label[:4])
        years = range(y0, y0 + 10)
        s = {k: sum(sheet[y][k] for y in years if y in sheet)
             for k in ("am_eu", "chinese", "japanese", "filipino", "extra", "leave", "net")}
        s["gross"] = s["am_eu"] + s["chinese"] + s["japanese"] + s["filipino"] + s["extra"]
        rows.append({"decade": label, **s,
                     "us_total": sum(t1["annual"][i]),
                     "us_europe_canada": t2["europe"][i] + t2["canada"][i],
                     "us_china": t2["china"][i], "us_japan": t2["japan"][i]})
    return rows


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

def fmt(x: float) -> str:
    return f"{x:,.0f}"


def pct(a: float, b: float) -> str:
    if not b or b < 1000:
        return "—"           # US base too small to compare
    r = a / b
    return f"×{r:.1f}" if r >= 2 else f"{100 * r:.0f}%"


def main() -> int:
    OUT.mkdir(exist_ok=True)
    ch = chain()
    sheet = ch["sheet"]
    otl = our_timeline(sheet)
    by = {k: {r["year"]: r["model_total"] for r in ch[k]} for k in ("base", "terr", "full")}
    wo = {s: {r["year"]: r["model_total"] for r in rows} for s, rows in ch["without"].items()}
    sheet_tot = {y + 1: sheet[y]["end"] for y in range(canon.FIRST, canon.LAST + 1)}
    sheet_tot[1846] = sheet[1846]["start"]
    for k in by:
        by[k][1846] = sheet[1846]["start"]
    for s in wo:
        wo[s][1846] = sheet[1846]["start"]

    def stream_effect(s: str, y: int) -> float:
        return by["full"][y] - wo[s][y]

    labels = {"americas_europe": "Americas & Europe", "chinese": "Chinese", "japanese": "Japanese",
              "filipino": "Filipino", "extra": "Drawn by Pacifica's lead (skilled + families)"}

    with open(OUT / "flows_by_year.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["year", "our_timeline_same_territory", "closed_1846_california", "territory", "migration"]
                   + [f"migration_{s}" for s in canon.STREAMS] + ["sheet_rate_effect", "sheet"])
        for y in range(1846, 1933):
            o = sum(otl[min(y, 1932)].values())
            w.writerow([y, round(o), round(by["base"][y]), round(by["terr"][y] - by["base"][y]),
                        round(by["full"][y] - by["terr"][y])]
                       + [round(stream_effect(s, y)) for s in canon.STREAMS]
                       + [round(sheet_tot[y] - by["full"][y]), round(sheet_tot[y])])

    sw = canon.native_ca_switch()
    L = ["# Where Pacifica's population comes from", "",
         "Generated by `population/flows.py`. Each step below is a full cohort run with the same engine and our-timeline "
         "vital rates, so each step is exactly the people it adds, with their descendants. At 1846 every step is zero. "
         f"Native Californians: switch `{sw}` (data/assumptions.toml).", "",
         "## The chain", "",
         "| Year | 1846 Californians and descendants | + Territories | + Migration | + Sheet's growth rate | = Sheet | Our timeline, same territory | Sheet ÷ our timeline |",
         "|---|---|---|---|---|---|---|---|"]
    for y in KEY:
        o = sum(otl[y].values())
        L.append(f"| {y} | {fmt(by['base'][y])} | {fmt(by['terr'][y] - by['base'][y])} | {fmt(by['full'][y] - by['terr'][y])} "
                 f"| {fmt(sheet_tot[y] - by['full'][y])} | {fmt(sheet_tot[y])} | {fmt(o)} | {sheet_tot[y] / o:.2f} |")
    y = 1932
    mig = by["full"][y] - by["terr"][y]
    L += ["",
          f"By 1932, migrants arriving after 1846 and their descendants are **{fmt(mig)}** of the sheet's "
          f"{fmt(sheet_tot[y])} people ({pct(mig, sheet_tot[y])}). Territories joined in 1856–1867 and their descendants "
          f"are {fmt(by['terr'][y] - by['base'][y])}; the 1846 Californians and theirs are {fmt(by['base'][y])}.", "",
          "Our timeline on the same territory: each territory from its canon join year, growing at its real census growth "
          "(partial areas — Montana camps, Western Slope, SW Wyoming, Baja — at the whole state's growth). Censuses before 1890 "
          "missed most Native people. It counts our timeline's own migration, so the ratio compares the sheet with what really "
          "happened, not with a closed population.", "",
          "## Migration by stream", "",
          "People present in each year because of each stream (arrivals, minus those who left, plus descendants):", "",
          "| Stream | 1870 | 1890 | 1910 | 1932 |", "|---|---|---|---|---|"]
    for s in canon.STREAMS:
        L.append(f"| {labels[s]} | " + " | ".join(fmt(stream_effect(s, yy)) for yy in (1870, 1890, 1910, 1932)) + " |")
    resid = [by["full"][yy] - by["terr"][yy] - sum(stream_effect(s, yy) for s in canon.STREAMS) for yy in (1870, 1890, 1910, 1932)]
    L.append("| (interaction, rounding) | " + " | ".join(fmt(v) for v in resid) + " |")

    rows = decade_flows(sheet)
    L += ["", "## Arrivals against real US immigration", "",
          "The sheet's gross arrivals per decade, and the same decade's immigration to the whole United States "
          "(DHS yearbook; US figures by country use calendar decades, one year earlier). A share near or above 100% "
          "means Pacifica would need about as many immigrants as the entire United States received; ×N means N times the "
          "US intake from that origin. US Table 1 counts fiscal years; \"—\" where the US base is under 1,000.", "",
          "| Decade | Sheet gross arrivals | US immigration (all) | Share | Americas & Europe | US from Europe + Canada | Share | Chinese | US from China | Share | Japanese | US from Japan | Share |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        L.append(f"| {r['decade']} | {fmt(r['gross'])} | {fmt(r['us_total'])} | {pct(r['gross'], r['us_total'])} "
                 f"| {fmt(r['am_eu'])} | {fmt(r['us_europe_canada'])} | {pct(r['am_eu'], r['us_europe_canada'])} "
                 f"| {fmt(r['chinese'])} | {fmt(r['us_china'])} | {pct(r['chinese'], r['us_china'])} "
                 f"| {fmt(r['japanese'])} | {fmt(r['us_japan'])} | {pct(r['japanese'], r['us_japan'])} |")
    tot = {k: sum(r[k] for r in rows) for k in ("gross", "us_total", "am_eu", "us_europe_canada", "chinese", "us_china",
                                                 "japanese", "us_japan", "filipino", "extra", "leave", "net")}
    L.append(f"| **1841–1930** | {fmt(tot['gross'])} | {fmt(tot['us_total'])} | {pct(tot['gross'], tot['us_total'])} "
             f"| {fmt(tot['am_eu'])} | {fmt(tot['us_europe_canada'])} | {pct(tot['am_eu'], tot['us_europe_canada'])} "
             f"| {fmt(tot['chinese'])} | {fmt(tot['us_china'])} | {pct(tot['chinese'], tot['us_china'])} "
             f"| {fmt(tot['japanese'])} | {fmt(tot['us_japan'])} | {pct(tot['japanese'], tot['us_japan'])} |")
    # by origin: named streams plus the talent stream's origin shares
    eo = load("assumptions")["extra_origin"]
    pools = load("pools")
    origin = {"americas_europe": 0.0, "japanese": 0.0, "chinese": 0.0, "filipino": 0.0}
    for yy in range(canon.FIRST, canon.LAST + 1):
        d = sheet[yy]
        origin["americas_europe"] += d["am_eu"]
        origin["japanese"] += d["japanese"]
        origin["chinese"] += d["chinese"]
        origin["filipino"] += d["filipino"]
        if eo["mode"] == "shares":
            sh = [row for row in eo["periods"] if row[0] <= yy][-1][1:]
            for k, s in zip(("americas_europe", "japanese", "chinese", "filipino"), sh):
                origin[k] += d["extra"] * s
    full_last = ch["full"][-1]
    jp_pool = pools["japan_overseas"]["total"] + sum(v for k, v in pools["japan_colonies_c1940"].items()
                                                     if isinstance(v, int))
    L += ["", "## All arrivals by origin, 1846–1932", "",
          f"Named streams plus the talent stream split by origin (`[extra_origin]`, mode `{eo['mode']}`). "
          "Gross arrivals; the population column counts each group in 1932 with descendants, after departures.", "",
          "| Origin | Gross arrivals | Group population 1932 | US intake 1841–1930 | Our timeline's pool |",
          "|---|---|---|---|---|",
          f"| Americas & Europe | {fmt(origin['americas_europe'])} | {fmt(full_last['white'])} (all white, incl. 1846 and territory residents) "
          f"| {fmt(tot['us_europe_canada'])} | {fmt(pools['europe_to_americas']['low'])}–{fmt(pools['europe_to_americas']['high'])} Europeans to the Americas, 1846–1940 |",
          f"| Japan | {fmt(origin['japanese'])} | {fmt(full_last['japanese'])} | {fmt(tot['us_japan'])} "
          f"| {fmt(pools['japan_overseas']['total'])} overseas 1868–1941, plus about {fmt(jp_pool - pools['japan_overseas']['total'])} in colonies and China c.1940: {fmt(jp_pool)} |",
          f"| China | {fmt(origin['chinese'])} | {fmt(full_last['chinese'])} | {fmt(tot['us_china'])} "
          f"| part of {fmt(pools['india_south_china_to_southeast_asia']['low'])}–{fmt(pools['india_south_china_to_southeast_asia']['high'])} Indians and Chinese to Southeast Asia, 1846–1940 |",
          f"| Philippines | {fmt(origin['filipino'])} | {fmt(full_last['filipino'])} | — | not yet sourced |",
          "", f"Japanese arrivals as a share of Japan's redirected pool: {pct(origin['japanese'], jp_pool)}. "
          "Pools are our timeline's totals; the canon can redirect them (Japan without Korea and Manchuria) but not "
          "multiply them without a stated reason.", ""]
    L += ["",
          f"Also in the sheet over 1846–1932: {fmt(tot['filipino'])} Filipino arrivals (no US yardstick: Filipinos were US "
          f"nationals from 1898 and are largely absent from these counts) and {fmt(tot['extra'])} drawn by Pacifica's lead "
          f"(skilled workers and families; split by origin above). {fmt(tot['leave'])} leave again; net "
          f"{fmt(tot['net'])}.", "",
          "## Reading this", "",
          "- The chain separates the sheet's growth into its sources; each column is the people that source accounts for.",
          "- The US comparison shows the scale of the claim, not its impossibility: the canon diverts part of the US flow "
          "(the Labour sheet's diverted immigration), and some streams, such as Chinese family migration, have no "
          "US counterpart because the US restricted them. Whether each stream's size fits its canon cause is the author's call.",
          "- Natural increase in every run uses our-timeline rates; canon health and family policies are not yet modelled."]
    (OUT / "flows.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L))
    return 0


if __name__ == "__main__":
    sys.exit(main())
