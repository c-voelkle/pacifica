"""The continental neighbours: the rump Confederacy, the Gulf Republic and the Union.

What it does
  * The rump (South Carolina, Georgia, Alabama, Mississippi, Florida; CR-048):
    two groups, Black and white-and-other, from the 1870 census.
      - Our timeline: each group is projected between censuses with Haines's
        national rates, solving for the constant net migration that reproduces
        the next census (as historical.py does for California).
      - Canon: the same rates and the same historical migration, plus the extra
        departures of `data/neighbours.toml` [rump_flight]: escapes under the
        Freedom Act, departures after abolition and the long emergency.
  * The people who leave, and their descendants, are followed to the Union or
    the Gulf Republic.
  * The Union and the Gulf: the workbook's own paths (values only; the file is
    never written), plus the rump's extra emigrants and their descendants.

What it reports (`population/outputs/`)
  * neighbours_by_year.csv: every year 1870-1932.
  * neighbours.md: the estimate, the historical closure and the workbook comparison.

Run:  python3 population/neighbours.py
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

import openpyxl

import canon
import cohort
import historical
from cohort import Group, load

OUT = Path(__file__).resolve().parent / "outputs"
STATES = ["SC", "GA", "AL", "MS", "FL"]
FIRST, LAST = 1870, 1932
GROUPS = ("black", "white")
STREAM = "americas_europe"  # historical.py's age-sex profile for net migration


def census() -> dict[str, dict[int, float]]:
    c = load("neighbours")["rump_census"]
    years = c["years"]
    out = {"total": {}, "black": {}, "white": {}}
    for i, y in enumerate(years):
        tot = sum(c[f"{s}_total"][i] for s in STATES)
        blk = sum(c[f"{s}_black"][i] for s in STATES)
        out["total"][y], out["black"][y], out["white"][y] = tot, blk, tot - blk
    return out


def step_value(pairs: list, year: int) -> float:
    return [v for y, v in pairs if y <= year][-1]


def rates(group: str, year: int) -> cohort.Rates:
    r = load("neighbours")["rump_rates"]
    return cohort.series_rates(r[f"series_{group}"], year)


def flight(year: int, scale: float = 1.0) -> dict:
    f = load("neighbours")["rump_flight"]
    row = [p for p in f["periods"] if p[0] <= year]
    black, white = (row[-1][1] * scale, row[-1][2] * scale) if row else (0.0, 0.0)
    return {"black": black, "white": white,
            "child": step_value(f["child_share"], year),
            "male_black": step_value(f["black_male_share"], year),
            "male_white": f["white_male_share"],
            "to_union_black": step_value(f["black_to_union"], year),
            "to_union_white": step_value(f["white_to_union"], year)}


def copy(g: Group) -> Group:
    c = Group(g.name)
    c.F, c.M = list(g.F), list(g.M)
    return c


# ---------------------------------------------------------------------------
# Our timeline: closure between censuses
# ---------------------------------------------------------------------------

def closure(cen: dict) -> tuple[dict, dict]:
    """Net migration a year by group and decade, and the start structure in 1870."""
    years = sorted(cen["total"])
    mig: dict[str, dict[int, float]] = {g: {} for g in GROUPS}
    start: dict[str, Group] = {}
    for grp in GROUPS:
        g = cohort.stable_structure(rates(grp, FIRST), cen[grp][FIRST])
        g.name = grp
        start[grp] = copy(g)
        for y0, y1 in zip(years, years[1:]):
            m, g, _ = historical.implied_migration(g, lambda y, s=grp: rates(s, y), STREAM, y0, y1, cen[grp][y1])
            mig[grp][y0] = m
    return mig, start


def hist_migration(mig: dict, grp: str, year: int) -> tuple[list[float], list[float]]:
    decade = max(d for d in mig[grp] if d <= year)  # 1930-1932 keep the 1920s rate
    m = mig[grp][decade]
    kids = load("assumptions")["migration"]["child_share_unassisted"] if m > 0 else 0.0
    return cohort.migrant_profile(m, historical.male_share(STREAM, year), kids)


# ---------------------------------------------------------------------------
# Runs
# ---------------------------------------------------------------------------

def run(mig: dict, start: dict, with_flight: bool, scale: float = 1.0) -> list[dict]:
    rump = {g: copy(start[g]) for g in GROUPS}
    away = {(g, d): Group(f"{g}-{d}") for g in GROUPS for d in ("union", "gulf")}
    rows = []
    cum = {g: 0.0 for g in GROUPS}
    for y in range(FIRST, LAST + 1):
        f = flight(y, scale) if with_flight else {"black": 0.0, "white": 0.0}
        rows.append(snapshot(y, rump, away, cum))
        if y == LAST:
            break
        for g in GROUPS:
            prof = hist_migration(mig, g, y)
            n = f[g]
            if n:
                male = f["male_black"] if g == "black" else f["male_white"]
                out = cohort.migrant_profile(n, male, f["child"])
                prof = cohort.merge(prof, cohort.migrant_profile(-n, male, f["child"]))
                share_u = f[f"to_union_{g}"]
                for dest, share in (("union", share_u), ("gulf", 1 - share_u)):
                    if share > 0:
                        cohort.step(away[(g, dest)], rates(g, y),
                                    ([x * share for x in out[0]], [x * share for x in out[1]]))
                    else:
                        cohort.step(away[(g, dest)], rates(g, y))
                cum[g] += n
            else:
                for dest in ("union", "gulf"):
                    cohort.step(away[(g, dest)], rates(g, y))
            cohort.step(rump[g], rates(g, y), prof)
    return rows


def snapshot(y: int, rump: dict, away: dict, cum: dict) -> dict:
    b, w = rump["black"].total(), rump["white"].total()
    return {"year": y, "black": b, "white": w, "total": b + w, "black_share": b / (b + w),
            "left_black": cum["black"], "left_white": cum["white"],
            "union_black": away[("black", "union")].total(), "union_white": away[("white", "union")].total(),
            "gulf_black": away[("black", "gulf")].total(), "gulf_white": away[("white", "gulf")].total()}


# ---------------------------------------------------------------------------
# Workbook
# ---------------------------------------------------------------------------

def workbook() -> dict[int, dict]:
    wb = openpyxl.load_workbook(canon.WORKBOOK, read_only=True, data_only=True)
    want = {"Labour": {"Union population (m)": "union",
                       "Union population without Pacifica's pull (m)": "union_no_pull"},
            "Gulf": {"Residents": "gulf"}}
    data: dict[int, dict] = {}
    for sheet, cols in want.items():
        ws = wb[sheet]
        rows = list(ws.iter_rows(values_only=True))
        header = next(r for r in rows if r and r[0] == "Year")
        idx = {header.index(h): k for h, k in cols.items()}
        for r in rows:
            if r and isinstance(r[0], (int, float)) and FIRST <= r[0] <= LAST:
                for i, k in idx.items():
                    v = r[i] or 0.0
                    data.setdefault(int(r[0]), {})[k] = v * 1e6 if k.startswith("union") else v
    return data


def world_rump(wbk_union_hist: dict) -> dict[int, float]:
    """The rump population the workbook's World sheet implies: its census share of the US."""
    return {1870: 0.101 * 38.6e6, 1900: 0.098 * 76.2e6, 1913: 0.087 * 97.2e6, 1929: 0.088 * 121.8e6,
            1932: 0.088 * 124.8e6}


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

def m(x: float) -> str:
    return f"{x / 1e6:.2f}"


def main() -> int:
    OUT.mkdir(exist_ok=True)
    cen = census()
    mig, start = closure(cen)
    otl = {r["year"]: r for r in run(mig, start, with_flight=False)}
    alt = {r["year"]: r for r in run(mig, start, with_flight=True)}
    wbk = workbook()

    rows = []
    for y in range(FIRST, LAST + 1):
        a, o, w = alt[y], otl[y], wbk.get(y, {})
        union_wb, gulf_wb = w.get("union", 0.0), w.get("gulf", 0.0)
        rows.append({
            "year": y,
            "rump_otl_total": o["total"], "rump_otl_black": o["black"], "rump_otl_black_share": o["black_share"],
            "rump_total": a["total"], "rump_black": a["black"], "rump_white": a["white"],
            "rump_black_share": a["black_share"],
            "extra_left_black_cumulative": a["left_black"], "extra_left_white_cumulative": a["left_white"],
            "rump_born_in_union": a["union_black"] + a["union_white"],
            "rump_born_in_union_black": a["union_black"],
            "rump_born_in_gulf": a["gulf_black"] + a["gulf_white"],
            "union_workbook": union_wb, "union_with_rump_emigrants": union_wb + a["union_black"] + a["union_white"],
            "gulf_workbook": gulf_wb,
            "gulf_with_rump_emigrants": (gulf_wb + a["gulf_black"] + a["gulf_white"]) if gulf_wb else 0.0,
        })
    with open(OUT / "neighbours_by_year.csv", "w", newline="", encoding="utf-8") as fh:
        wr = csv.DictWriter(fh, fieldnames=list(rows[0]))
        wr.writeheader()
        for r in rows:
            wr.writerow({k: (round(v, 4) if isinstance(v, float) and abs(v) < 2 else round(v) if isinstance(v, float) else v)
                         for k, v in r.items()})

    by = {r["year"]: r for r in rows}
    marks = [1870, 1880, 1890, 1900, 1906, 1910, 1913, 1920, 1927, 1929, 1932]
    cyears = sorted(cen["total"])
    L = []
    L.append("# The continental neighbours: the rump, the Gulf and the Union\n")
    L.append("Generated by `population/neighbours.py` from `data/neighbours.toml` and the workbook (values only). "
             "Rump census anchors are our timeline; the extra departures are MODEL readings of canon (CR-048, proposed). "
             "Populations at the start of the year (census years: the census count).\n")

    L.append("## The estimate\n")
    L.append("| Year | Rump (m) | Black (m) | Black share | Our timeline (m) | Our timeline Black share | "
             "Extra departures to date, Black / white (k) | Rump-born and descendants in the Union (m) | Union, workbook → with them (m) | Gulf, workbook → with them (m) |")
    L.append("|---|---|---|---|---|---|---|---|---|---|")
    for y in marks:
        r = by[y]
        gulf = f"{m(r['gulf_workbook'])} → {m(r['gulf_with_rump_emigrants'])}" if r["gulf_workbook"] else "Confederate"
        L.append(f"| {y} | {m(r['rump_total'])} | {m(r['rump_black'])} | {r['rump_black_share']:.1%} | "
                 f"{m(r['rump_otl_total'])} | {r['rump_otl_black_share']:.1%} | "
                 f"{r['extra_left_black_cumulative'] / 1e3:,.0f} / {r['extra_left_white_cumulative'] / 1e3:,.0f} | "
                 f"{m(r['rump_born_in_union'])} | {m(r['union_workbook'])} → {m(r['union_with_rump_emigrants'])} | {gulf} |")
    L.append("")
    flip = next((y for y in range(FIRST, LAST + 1) if by[y]["rump_black_share"] < 0.5), None)
    flip_otl = next((y for y in range(FIRST, LAST + 1) if by[y]["rump_otl_black_share"] < 0.5), None)
    r32, r00 = by[1932], by[1900]
    L.append("**Reading it.**")
    L.append(f"- In 1900 the rump has {m(r00['rump_total'])}m people against {m(r00['rump_otl_total'])}m on the historical census; "
             f"{r00['rump_black_share']:.0%} are Black against {r00['rump_otl_black_share']:.0%}. "
             f"The difference is a generation of escapes under the Freedom Act and departures after abolition, and their unborn children.")
    L.append(f"- The rump's Black majority ends in {flip or 'no year before 1933'} "
             f"(our timeline: {flip_otl or 'not before 1933'}). In 1932 the rump has {m(r32['rump_total'])}m people, "
             f"{r32['rump_black_share']:.0%} Black, against {m(r32['rump_otl_total'])}m and {r32['rump_otl_black_share']:.0%} in our timeline.")
    L.append(f"- By 1932, {m(r32['rump_born_in_union'])}m rump emigrants and their descendants beyond our timeline's live in the Union, "
             f"{m(r32['rump_born_in_union_black'])}m of them Black: the assertive minority of CR-048 A4, on top of the Union's historical Black population. "
             f"The Gulf gains {m(r32['rump_born_in_gulf'])}m.")
    L.append("- The Union's workbook path is the historical population of the states it holds, less what Pacifica draws away. "
             "Our timeline's southern migrants are already in it; only the extra departures are added here.\n")

    L.append("## Low and high cases\n")
    L.append("The departures scaled up and down together (`[rump_flight] scenarios`).\n")
    L.append("| Case | Scale | Rump 1900 (m) | Black share 1900 | Rump 1932 (m) | Black share 1932 | Black majority ends | Extra rump-born in the Union 1932 (m) |")
    L.append("|---|---|---|---|---|---|---|---|")
    for name, k in [("low", load("neighbours")["rump_flight"]["scenarios"]["low"]), ("central", 1.0),
                    ("high", load("neighbours")["rump_flight"]["scenarios"]["high"])]:
        sc = {r["year"]: r for r in run(mig, start, with_flight=True, scale=k)}
        fl = next((y for y in range(FIRST, LAST + 1) if sc[y]["black_share"] < 0.5), "after 1932")
        L.append(f"| {name} | {k:g} | {m(sc[1900]['total'])} | {sc[1900]['black_share']:.0%} | {m(sc[1932]['total'])} | "
                 f"{sc[1932]['black_share']:.0%} | {fl} | {m(sc[1932]['union_black'] + sc[1932]['union_white'])} |")
    L.append("")

    L.append("## Our timeline: the census closure\n")
    L.append("Net migration a year that carries each group from one census to the next under Haines's national rates. "
             "Negative = net departures. This is the historical baseline the canon run keeps.\n")
    L.append("| Decade | Black, census start → end | Net migration a year | White and other, start → end | Net migration a year |")
    L.append("|---|---|---|---|---|")
    for y0, y1 in zip(cyears, cyears[1:]):
        L.append(f"| {y0}–{y1} | {cen['black'][y0]:,.0f} → {cen['black'][y1]:,.0f} | {mig['black'][y0]:,.0f} | "
                 f"{cen['white'][y0]:,.0f} → {cen['white'][y1]:,.0f} | {mig['white'][y0]:,.0f} |")
    L.append("\nThe 1870s figure absorbs the 1870 census's undercount of the South. The national white rates are kinder "
             "than Southern white mortality (hookworm, malaria, pellagra), so white net migration reads a little lower than it was.\n")

    L.append("## The canon departures (MODEL)\n")
    L.append("| From | Black a year | White a year | Children among them | Black to the Union | White to the Union | Canon anchor |")
    L.append("|---|---|---|---|---|---|---|")
    anchors = {1870: "Black regulars and escape networks along Tennessee (§13)",
               1873: "Freedom Act: free on arrival, citizen after a year (§13)",
               1889: "Final abolition; emigrant-agent laws and passes (§25)",
               1900: "The rump alone; the debt stays (CR-048 R1-R3)",
               1906: "Atlanta, the weevil, the long emergency (CR-048 R8, R14)",
               1916: "On top of our timeline's Great Migration",
               1930: "Depression"}
    for p in load("neighbours")["rump_flight"]["periods"]:
        f = flight(p[0])
        L.append(f"| {p[0]} | {p[1]:,} | {p[2]:,} | {f['child']:.0%} | {f['to_union_black']:.0%} | {f['to_union_white']:.0%} | {anchors.get(p[0], '')} |")
    L.append("")

    L.append("## Against the workbook\n")
    L.append("The World sheet treats the rump as its historical census share of the United States. The estimate here is lower:\n")
    L.append("| Year | World sheet (m) | This model (m) | Difference |")
    L.append("|---|---|---|---|")
    for y, v in world_rump({}).items():
        L.append(f"| {y} | {m(v)} | {m(by[y]['rump_total'])} | {by[y]['rump_total'] / v - 1:+.0%} |")
    L.append("\nSuggested workbook changes (not applied): the World sheet's rump population share from this model; "
             "the Union's population plus the rump emigrants; the Gulf's residents plus its share. "
             "The rump's output follows its population unless output per person is changed with it.\n")

    L.append("## What is not modelled\n")
    L.append("- State by state: the five states are one population. Florida, which gained from the Union's money in the 1920s, is folded into the rest.")
    L.append("- Group rates in the destinations: emigrants keep the national Black or white rates wherever they go.")
    L.append("- The Union's own Black population before the rump's extra emigrants, and Virginia's and North Carolina's (CR-048 R9).")
    L.append("- 1930–1932 keep the 1920s historical migration rate.")

    (OUT / "neighbours.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    for y in (1900, 1910, 1920, 1932):
        r = by[y]
        print(y, m(r["rump_total"]), f"{r['rump_black_share']:.1%}", "OTL", m(r["rump_otl_total"]),
              "Union", m(r["union_with_rump_emigrants"]), "Gulf", m(r["gulf_with_rump_emigrants"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
