"""The provisioning account (CR-082): people against the food the domain can grow.

What it does
  * People: the Realm's residents from the canon run (outputs/canon_by_year.csv)
    and, from 1908, the Philippine crown (our timeline's censuses).
  * Home supply: our timeline's irrigated and dry crop land inside Pacifica's
    frontier, turned into acres of average Union crop land and then into mouths
    on the Realm's diet. Three cases: history's acres; canon's farmers (history's
    acres a head for canon's larger population, up to the ceilings); the ceilings.
  * The Office's tables of 1890-1930: from each table year, the course of the
    population for a century at a slowing rate, set against the home ceiling.

It reads the canon run and data/provisioning.toml and feeds nothing back.
Every factor that turns acres into mouths is MODEL (see the data file).

Run:  python3 population/provisioning.py     (after population/canon.py)
"""
from __future__ import annotations

import csv
import math
import sys
from pathlib import Path

from cohort import interp, load

OUT = Path(__file__).resolve().parent / "outputs"
FIRST, LAST = 1861, 1932
TABLES = [1890, 1900, 1910, 1920, 1930]
CASES = {"history": "history's acres", "farmers": "canon's farmers", "ceiling": "the ceilings"}
ACRES_PER_HECTARE = 2.471


def cfg() -> dict:
    return load("provisioning")


# ---------------------------------------------------------------- people

def residents() -> dict[int, float]:
    path = OUT / "canon_by_year.csv"
    if not path.exists():
        sys.exit("Run population/canon.py first (outputs/canon_by_year.csv is missing).")
    with path.open(encoding="utf-8") as f:
        return {int(r["year"]): float(r["model_total"]) for r in csv.DictReader(f)}


def geometric(years: list[float], values: list[float], year: float) -> float:
    """Interpolate at a constant rate between anchors, and beyond them at the nearest rate."""
    i = max(0, min(len(years) - 2, sum(1 for y in years[1:-1] if year >= y)))
    r = math.log(values[i + 1] / values[i]) / (years[i + 1] - years[i])
    return values[i] * math.exp(r * (year - years[i]))


def crown_people(c: dict, year: int) -> float:
    if year < c["crown"]["from_year"]:
        return 0.0
    return geometric(c["crown"]["census_years"], c["crown"]["census"], year)


def crown_fed(c: dict, year: int) -> float:
    k = c["crown"]
    if year < k["from_year"]:
        return 0.0
    ha = interp(k["cultivated_years"], k["cultivated_hectares"], year)
    return ha * ACRES_PER_HECTARE * (1 - k["export_crop_share"]) / k["acres_per_head"]


# ---------------------------------------------------------------- land

def land_1929(c: dict) -> dict:
    """Irrigated area, irrigated harvest and dry crop land inside the frontier in 1929."""
    irr = {k: v for k, v in c["irrigation_1929"].items() if isinstance(v, (int, float))}
    crop, terr = c["cropland_1929"], c["territory"]
    area = harvest = dry = 0.0
    rows = []
    for state, a in irr.items():
        h = crop["irrigated_harvested"].get(state, a * crop["harvested_share_of_irrigated"])
        if state == "California":
            total = crop["california_cropland_harvested"]
        else:
            total = h / (crop["pct_irrigated"][state] / 100)
        si, sd = terr["irrigated"].get(state, 1.0), terr["dry"].get(state, 1.0)
        rows.append((state, a * si, h * si, (total - h) * sd))
        area, harvest, dry = area + a * si, harvest + h * si, dry + (total - h) * sd
    return {"area": area, "harvest": harvest, "dry": dry, "rows": rows,
            "share": area / c["irrigation_totals"]["acres"][-1]}


def ceiling_area(c: dict, base: dict) -> float:
    return c["irrigation_totals"][c["levers"]["ceiling_basis"]] * base["share"]


def history_people(c: dict, year: int) -> float:
    """Our timeline's census population inside the frontier (part states by share)."""
    st = load("census")["states"]
    share = c["territory"]["population"]
    return sum(geometric_census(st["years"], v, year) * share.get(k, 1.0)
               for k, v in st.items() if isinstance(v, list) and k not in ("years", "Alaska"))


def geometric_census(years: list[float], values: list[float], year: float) -> float:
    pts = [(y, v) for y, v in zip(years, values) if v == v]
    if year <= pts[0][0]:
        return pts[0][1]
    return geometric([y for y, _ in pts], [v for _, v in pts], year)


def acres(c: dict, base: dict, year: int, case: str, pop: dict[int, float] | None = None) -> tuple[float, float]:
    """Irrigated area and dry crop land inside the frontier in a year, for a case."""
    t, d = c["irrigation_totals"], c["dry_cropland"]
    national = interp(t["early_years"] + t["years"], t["early_acres"] + t["acres"], year)
    irr = national * base["share"]
    dry = interp(d["years"], d["index"], year) * base["dry"]
    top_irr, top_dry = ceiling_area(c, base), base["dry"] * c["levers"]["dry_ceiling_factor"]
    if case == "ceiling":
        return top_irr, top_dry
    if case == "farmers":
        k = pop[year] / history_people(c, year)
        return min(irr * k, top_irr), min(dry * k, top_dry)
    return irr, dry


def standard_acres(c: dict, base: dict, year: int, case: str, pop=None, yields: float | None = None) -> float:
    lv = c["levers"]
    irr, dry = acres(c, base, year, case, pop)
    y = interp(lv["yield_years"], lv["yield_index"], year) if yields is None else yields
    harvest = irr * base["harvest"] / base["area"]
    return (harvest * lv["irrigated_factor"] + dry * lv["dry_factor"]) * y


def mouths(c: dict, base: dict, year: int, case: str, pop=None) -> float:
    return standard_acres(c, base, year, case, pop) / c["levers"]["acres_per_head"]


def crossing(c: dict, base: dict, pop: dict[int, float], case: str) -> int | None:
    """First year from which the Realm's residents stay above what its own soil feeds."""
    last_fed = None
    for y in range(FIRST, LAST + 1):
        if pop[y] <= mouths(c, base, y, case, pop):
            last_fed = y
    if last_fed == LAST:
        return None
    return FIRST if last_fed is None else last_fed + 1


# ---------------------------------------------------------------- the Office's tables

def rate(series, year: int, span: int = 10) -> float:
    return math.log(series(year) / series(year - span)) / span


def project(p0: float, r0: float, g_end: float, n: float, horizon: float) -> float:
    """The rate falls in a straight line from r0 to g_end over the horizon, then holds."""
    m = min(n, horizon)
    grown = r0 * m - (r0 - g_end) * m * m / (2 * horizon) + g_end * max(0.0, n - horizon)
    return p0 * math.exp(grown)


def table(c: dict, base: dict, pop: dict[int, float], year: int, g_end: float | None = None) -> dict:
    lv = c["levers"]
    g = lv["g_end"] if g_end is None else g_end
    r_realm = rate(lambda y: pop[y], year)
    counted = year >= c["crown"]["from_year"]
    r_crown = rate(lambda y: geometric(c["crown"]["census_years"], c["crown"]["census"], y), year) if counted else 0.0
    out = {"year": year, "realm": pop[year], "crown": crown_people(c, year), "rate": r_realm, "rate_crown": r_crown}
    for n in (25, 50, 100):
        realm = project(pop[year], r_realm, g, n, lv["horizon"])
        crown = project(out["crown"], r_crown, min(g, r_crown), n, lv["horizon"]) if counted else 0.0
        out[f"realm_{n}"], out[f"crown_{n}"] = realm, crown
    # What the century's Realm needs, in acres of average Union crop land, at the table year's yields.
    out["need_100"] = out["realm_100"] * lv["acres_per_head"]
    top = standard_acres(c, base, year, "ceiling")
    out["ceiling_std"] = top
    out["ceiling_mouths"] = top / lv["acres_per_head"]
    # The year the projected Realm passes the ceiling (0 if it already has).
    n = 0
    while project(pop[year], r_realm, g, n, lv["horizon"]) <= out["ceiling_mouths"] and n < 300:
        n += 1
    out["passes_ceiling"] = year + n
    return out


# ---------------------------------------------------------------- report

def m(x: float) -> str:
    return f"{x / 1e6:.1f}"


def main() -> int:
    c, pop = cfg(), residents()
    base = land_1929(c)
    lv = c["levers"]
    L: list[str] = []
    A = L.append
    A("# The provisioning account (CR-082)")
    A("")
    A("Built by `population/provisioning.py` from the canon run and `data/provisioning.toml`. Acreages are our "
      "timeline's census figures inside Pacifica's frontier; every factor that turns acres into mouths is MODEL. "
      "The author's decisions of 21 November 2026 are built in: the Realm's present diet held constant, a slowing "
      "rate of growth, and the Philippine crown counted from 1908.")
    A("")
    A("## 1. The land in 1929 (our timeline, inside the frontier)")
    A("")
    A("| State | Area irrigated | Irrigated land harvested | Dry crop land |")
    A("|---|---|---|---|")
    for state, a, h, d in base["rows"]:
        A(f"| {state.replace('_', ' ')} | {m(a)} | {m(h)} | {m(d)} |")
    A(f"| **Total** | **{m(base['area'])}** | **{m(base['harvest'])}** | **{m(base['dry'])}** |")
    A("")
    A(f"Millions of acres. The territory holds {base['share']:.0%} of the 19 states' irrigated area. "
      f"The ceiling used is the 1940 census's irrigable area in enterprises times that share: "
      f"{m(ceiling_area(c, base))} million acres. Part states and the dry land are estimates.")
    A("")
    A("## 2. People against home supply")
    A("")
    A(f"One head needs {lv['acres_per_head']} acres of average Union crop land on the Realm's diet. An irrigated acre "
      f"counts as {lv['irrigated_factor']} such acres and a dry western acre as {lv['dry_factor']}; canon's nitrogen "
      f"raises yields to {lv['yield_index'][-1]:.2f} times history's by 1929.")
    A("")
    A("| Year | Residents | Our timeline, same land | Fed at home: history's acres | canon's farmers | the ceilings | "
      "Share fed (canon's farmers) |")
    A("|---|---|---|---|---|---|---|")
    for y in (1861, 1870, 1880, 1890, 1900, 1910, 1920, 1930, 1932):
        f = {k: mouths(c, base, y, k, pop) for k in CASES}
        A(f"| {y} | {m(pop[y])} | {m(history_people(c, y))} | {m(f['history'])} | {m(f['farmers'])} | "
          f"{m(f['ceiling'])} | {f['farmers'] / pop[y]:.0%} |")
    A("")
    A("*Canon's farmers* is the central case: canon's residents work as many acres a head as our timeline's did on "
      f"the same land, until the irrigated ceiling ({m(ceiling_area(c, base))} million acres) and the dry ceiling "
      f"({m(base['dry'] * lv['dry_ceiling_factor'])} million) stop them.")
    A("")
    x = crossing(c, base, pop, "farmers")
    first = next(y for y in range(FIRST, LAST + 1) if pop[y] <= mouths(c, base, y, "farmers", pop))
    if x:
        A(f"- Canon's farmers feed the Realm, with a surplus to sell, from **{first}** to **{x - 1}**. "
          f"From **{x}** the Realm eats more than its own soil grows, even at the ceilings.")
    else:
        A(f"- Canon's farmers feed the Realm from {first} to 1932.")
    A(f"- In {LAST} about {m(pop[LAST] - mouths(c, base, LAST, 'farmers', pop))} million residents, "
      f"{1 - mouths(c, base, LAST, 'farmers', pop) / pop[LAST]:.0%}, eat from other people's land. "
      f"On history's acres alone it would be {m(pop[LAST] - mouths(c, base, LAST, 'history'))} million.")
    A("")
    A("## 3. The Philippine crown, from 1908 (its own ledger)")
    A("")
    A("| Year | People | Fed from its own land | Balance |")
    A("|---|---|---|---|")
    for y in (1910, 1920, 1930, 1932):
        p, f = crown_people(c, y), crown_fed(c, y)
        A(f"| {y} | {m(p)} | {m(f)} | {m(f - p)} |")
    A("")
    A("Our timeline's censuses and cultivated area, on the crown's own rice diet (MODEL). It roughly feeds itself "
      "and brings no surplus to the Realm.")
    A("")
    A("## 4. The Office's tables")
    A("")
    A(f"From each table year the yearly rate falls in a straight line from the last decade's rate to "
      f"{lv['g_end']:.1%} over a century. Need is at the table year's yields.")
    A("")
    A("| Table | Residents | Crown | Rate | In 25 years | In 50 | In 100 (Realm + crown) | Home ceiling feeds | "
      "Realm passes it | A century's need against the ceiling |")
    A("|---|---|---|---|---|---|---|---|---|---|")
    rows = []
    for y in TABLES:
        t = table(c, base, pop, y)
        rows.append(t)
        when = "already past" if t["passes_ceiling"] <= y else str(t["passes_ceiling"])
        A(f"| {y} | {m(t['realm'])} | {m(t['crown']) if t['crown'] else '—'} | {t['rate']:.1%} | "
          f"{m(t['realm_25'] + t['crown_25'])} | {m(t['realm_50'] + t['crown_50'])} | "
          f"{m(t['realm_100'])} + {m(t['crown_100'])} = {m(t['realm_100'] + t['crown_100'])} | "
          f"{m(t['ceiling_mouths'])} | {when} | {t['need_100'] / t['ceiling_std']:.0f} times |")
    A("")
    last = rows[-1]
    A(f"The table of 1930: {m(last['realm_100'])} million in the Realm a century on need "
      f"{last['need_100'] / 1e6:,.0f} million acres of average Union crop land at the yields of 1930, "
      f"{last['need_100'] / lv['union_cropland_1925_29']:.1f} times all the crop land the Union worked in 1925–29.")
    A("")
    A("## 5. What moves the result")
    A("")
    A("| Lever | Value | The ceilings feed in 1932 | Deficit begins | Table of 1930, Realm a century on |")
    A("|---|---|---|---|---|")
    def variant(name, value, **kw):
        c2 = cfg()
        g = None
        for key, val in kw.items():
            if key == "g_end":
                g = val
            else:
                c2["levers"][key] = val
        t = table(c2, land_1929(c2), pop, 1930, g)
        b2 = land_1929(c2)
        x2 = crossing(c2, b2, pop, "farmers")
        A(f"| {name} | {value} | {m(mouths(c2, b2, LAST, 'ceiling'))} | {x2 if x2 else 'not before 1933'} | {m(t['realm_100'])} |")
    variant("As built", "—")
    variant("A leaner diet", "1.5 acres a head", acres_per_head=1.5)
    variant("A rice diet", "0.7 acres a head", acres_per_head=0.7)
    variant("Irrigated acre", "counts 3.0", irrigated_factor=3.0)
    variant("Yields", "1.6 times history's by 1929", yield_index=[1.0, 1.0, 1.2, 1.6, 1.6])
    variant("Dry-farm ceiling", "twice the 1929 land", dry_ceiling_factor=2.0)
    variant("Growth ends at", "1.0% a year", g_end=0.010)
    variant("Growth ends at", "2.0% a year", g_end=0.020)
    A("")
    A("## 6. Not sourced, or weakly")
    A("")
    for key, where in (("status", "territory"), ("status", "dry_cropland"), ("pct_status", "cropland_1929"),
                       ("harvested_status", "cropland_1929"), ("california_status", "cropland_1929"),
                       ("factor_status", "levers"), ("yield_status", "levers"), ("status", "crown")):
        A(f"- `[{where}]`: {c[where][key]}")
    A("- Range and pasture are left out on both sides of the account; so are the sea, Hawaii's cane and the Japan series.")
    (OUT / "provisioning.md").write_text("\n".join(L) + "\n", encoding="utf-8")

    with (OUT / "provisioning_by_year.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["year", "residents", "crown_people", "fed_history", "fed_farmers", "fed_ceiling",
                    "irrigated_history", "irrigated_farmers", "dry_history", "dry_farmers", "crown_fed"])
        for y in range(FIRST, LAST + 1):
            w.writerow([y, round(pop[y]), round(crown_people(c, y))] +
                       [round(mouths(c, base, y, k, pop)) for k in CASES] +
                       [round(acres(c, base, y, "history")[0]), round(acres(c, base, y, "farmers", pop)[0]),
                        round(acres(c, base, y, "history")[1]), round(acres(c, base, y, "farmers", pop)[1]),
                        round(crown_fed(c, y))])
    print(f"wrote {OUT / 'provisioning.md'} and provisioning_by_year.csv")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
