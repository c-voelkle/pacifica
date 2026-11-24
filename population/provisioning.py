"""The provisioning account (CR-082): people against the food the domain can grow.

What it does
  * People: the Realm's residents from the canon run (outputs/canon_by_year.csv)
    and, from 1908, the Philippine crown (our timeline's censuses).
  * Home supply: our timeline's irrigated and dry crop land inside Pacifica's
    frontier, turned into acres of average Union crop land and then into mouths
    on the Realm's diet. Cases, each building on the last: history's acres;
    canon's farmers (history's acres a head for canon's larger population, up to
    what the works can water); concerted research (the central case: the Realm
    farms as our timeline farmed the same land a generation later); and the sea.
  * Capacity against crop (22 November 2026): what the land could feed, and what
    is in fact grown, which is the Realm's own table and what it sells abroad.
    Nitrogen goes on the fields as the margin narrows and as there is nitrogen.
  * The Office's tables of 1890-1930: from each table year, the course of the
    population for a century at a slowing rate, set against the home ceiling.
  * The century: the provisioners' works against the table of 1930.

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
CASES = {"history": "history's acres", "farmers": "canon's farmers", "research": "concerted research",
         "ceiling": "the ceilings"}
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


def works_limit(c: dict, base: dict, year: float) -> float:
    """The most irrigated land canon's works can water in a year: the rivers' own flow until
    storage is built, then what the dams and pumps reach, at last every irrigable acre."""
    t, w = c["irrigation_totals"], c["works"]
    def level(key):
        return base["area"] if key == "history_1929" else t[key] * base["share"]
    return interp(w["years"], [level(k) for k in w["basis"]], year)


def draft_share(c: dict, year: float, who: str) -> float:
    """Share of crop land that feeds horses and mules and so feeds no people."""
    d = c["draft"]
    return interp(d[who + "_years"], d[who + "_share"], year)


def acres(c: dict, base: dict, year: int, case: str, pop: dict[int, float] | None = None) -> tuple[float, float]:
    """Irrigated area and dry crop land inside the frontier in a year, for a case."""
    t, d = c["irrigation_totals"], c["dry_cropland"]
    national = interp(t["early_years"] + t["years"], t["early_acres"] + t["acres"], year)
    irr = national * base["share"]
    dry = interp(d["years"], d["index"], year) * base["dry"]
    top_irr, top_dry = ceiling_area(c, base), base["dry"] * c["levers"]["dry_ceiling_factor"]
    if case == "ceiling":
        return top_irr, top_dry
    if case in ("farmers", "research"):
        k = pop[year] / history_people(c, year)
        return min(irr * k, top_irr, works_limit(c, base, year)), min(dry * k, top_dry)
    return irr, dry


def ladder(c: dict, year: float) -> float:
    """Our timeline's yield on the same land around a year, against its flat years (ten-year mean)."""
    y = c["yield_ladder"]
    series, first = y["bushels"], y["first_year"]
    lo, hi = y["base_years"]
    base = sum(series[lo - first:hi - first + 1]) / (hi - lo + 1)
    centre = int(round(min(year, first + len(series) - 5)))
    if centre - 5 < lo:
        return 1.0
    window = [series[i - first] for i in range(centre - 5, centre + 5)]
    return max(1.0, sum(window) / len(window) / base)


def span(years: list[float], year: float) -> float:
    return max(0.0, min(1.0, (year - years[0]) / (years[1] - years[0])))


def research(c: dict, year: float, when: str | None = None, nitrogen: float = 1.0) -> float:
    """The Realm's yields against history's: the product of the components in the field by a year.
    `when` is a column of dates (history, canon_central, canon_earliest); `nitrogen` is the share of
    the nitrogen the nitrogen-bound components ask for that is actually to hand."""
    yc = c["yield_components"]
    key = when or "canon_" + yc["mode"]
    k = 1.0
    for item in yc["items"]:
        share = span(item[key], year) * (nitrogen if item["needs_nitrogen"] else 1.0)
        k *= 1 + (item["gain"] - 1) * share
    return k


def canon_farm_nitrogen(c: dict, year: int) -> float:
    n = c["nitrogen"]
    ramp = max(0.0, min(1.0, (year - n["canon_from"]) / (1929 - n["canon_from"])))
    return n["canon_total_1929"] * n["canon_farm_share"] * ramp


def base_standard(c: dict, base: dict, year: int, case: str, pop=None) -> tuple[float, float]:
    """Standard acres from irrigated and from dry land at history's yields."""
    lv = c["levers"]
    irr, dry = acres(c, base, year, case, pop)
    return irr * base["harvest"] / base["area"] * lv["irrigated_factor"], dry * lv["dry_factor"]


def standard_acres(c: dict, base: dict, year: int, case: str, pop=None, nitrogen="supplied") -> float:
    """Acres of average Union crop land the home soil is worth to people in a year, for a case.
    `nitrogen` is the share of the nitrogen-bound gain in the fields: a number, "full", "supplied"
    (as much as Chile and the home plants can give) or "canon" (CR-054's nitrogen as it stands)."""
    irr, dry = base_standard(c, base, year, case, pop)
    if case in ("history", "farmers"):
        return (irr + dry) * (1 - draft_share(c, year, "history"))
    lifted = (irr if c["yield_components"]["applies_to_irrigated"] else 0.0) + dry
    if case == "ceiling" or nitrogen == "full":
        share = 1.0
    elif isinstance(nitrogen, (int, float)):
        share = float(nitrogen)
    else:
        n = c["nitrogen"]
        asked = lifted * (research(c, year) - research(c, year, nitrogen=0.0))
        tonnes = canon_farm_nitrogen(c, year) if nitrogen == "canon" else nitrogen_supply(c, year)
        bought = tonnes * n["grain_per_tonne_n"] / n["grain_per_standard_acre"]
        share = min(1.0, bought / asked) if asked > 0 else 1.0
    return (irr + dry + lifted * (research(c, year, nitrogen=share) - 1)) * (1 - draft_share(c, year, "canon"))


def nitrogen_needed(c: dict, base: dict, year: int, pop) -> float:
    """Tonnes of nitrogen a year the nitrogen-bound components ask for when they are in every field."""
    n = c["nitrogen"]
    irr, dry = base_standard(c, base, year, "research", pop)
    lifted = (irr if c["yield_components"]["applies_to_irrigated"] else 0.0) + dry
    gain = lifted * (research(c, year) - research(c, year, nitrogen=0.0))
    return gain * n["grain_per_standard_acre"] / n["grain_per_tonne_n"]


def home_nitrogen(c: dict, year: float) -> float:
    """Tonnes of home-made nitrogen for the fields in a year (the Columbia's and the valley's ammonia)."""
    k = c["nitrogen_supply"]
    return interp(k["home_years"], k["home_farm_tonnes"], year)


def nitrogen_supply(c: dict, year: int) -> float:
    """Tonnes of nitrogen the Realm's fields can get in a year: its share of Chile's trade and its own."""
    return c["nitrogen_supply"]["chile_share_max"] * chile_nitrogen(c, year) + home_nitrogen(c, year)


def chile_nitrogen(c: dict, year: int) -> float:
    """Tonnes of nitrogen in all the nitrate Chile exported in a year (our timeline)."""
    n = c["nitrogen"]
    return geometric(n["chile_years"], n["chile_nitrate_tonnes"], min(year, n["chile_years"][-1])) * n["nitrogen_in_nitrate"]


def japanese_in_realm() -> dict[int, float]:
    with (OUT / "canon_by_year.csv").open(encoding="utf-8") as f:
        return {int(r["year"]): float(r["japanese"]) for r in csv.DictReader(f)}


def japan(c: dict, year: int, in_realm: dict[int, float]) -> dict:
    """Japan's rice in a year: our timeline, and canon with and without the stagnation of 1920-35."""
    j = c["japan"]
    people = geometric(j["people_years"], j["people"], year)
    away = max(0.0, in_realm[year] - j["our_timeline_japanese_in_territory_1930"] * in_realm[year] / in_realm[1930])
    canon_people = people - j["emigrant_share"] * away
    head = interp(j["kg_per_head_years"], j["kg_per_head"], year) / j["kg_per_koku"]
    to_1920 = j["crop_1890"] * math.exp(j["crop_growth_to_1920"] * (min(year, 1920) - 1890))
    crop = to_1920 * math.exp(j["crop_growth_after_1920"] * max(0, year - 1920))
    crop_on = j["crop_1890"] * math.exp(j["crop_growth_to_1920"] * (year - 1890))
    return {"people": people, "canon_people": canon_people, "head": head, "crop": crop, "crop_on": crop_on,
            "gap_history": people * head - crop, "gap_canon": canon_people * head - crop,
            "gap_canon_on": canon_people * head - crop_on}


def sea_mouths(c: dict, year: int) -> float:
    """Mouths the sea's catch frees from crop land, as animal food on the Realm's diet."""
    k = c["sea"]
    kg = (k["pacific_states_1936_lb"] + k["alaska_lb"]) * 0.4536 * k["edible_share"]
    return kg * interp(k["years"], k["index"], year) * k["meat_acres_per_kg"] / c["levers"]["acres_per_head"]


def mouths(c: dict, base: dict, year: int, case: str, pop=None, nitrogen: str = "supplied") -> float:
    return standard_acres(c, base, year, case, pop, nitrogen) / c["levers"]["acres_per_head"]


def central(c: dict, base: dict, year: int, pop, nitrogen="supplied") -> float:
    """The central case's capacity: canon's farmers, concerted research and the sea, with as much
    nitrogen as the Realm can get."""
    return mouths(c, base, year, "research", pop, nitrogen) + sea_mouths(c, year)


def tonnes_per_mouth(c: dict) -> float:
    """Grain or its equivalent behind one mouth on the Realm's diet for a year."""
    return c["levers"]["acres_per_head"] * c["nitrogen"]["grain_per_standard_acre"]


def export_mouths(c: dict, year: int) -> float:
    """What the Realm sells abroad in a year, in mouths on its own diet."""
    e = c["exports"]
    return interp(e["years"], e["grain_tonnes"], year) / tonnes_per_mouth(c)


def fields(c: dict, base: dict, year: int, pop) -> dict:
    """Capacity against crop in a year. The crop is the Realm's own table and its sales abroad, no more.
    The methods that cost nothing an acre are in every field as soon as they exist; nitrogen and the
    short wheats that need it go on as the margin narrows, never below what the paying crops take
    and never above what there is to buy."""
    k = c["nitrogen_supply"]
    demand = pop[year] + export_mouths(c, year)
    free = central(c, base, year, pop, 0.0)
    full = central(c, base, year, pop, "full")
    asked = nitrogen_needed(c, base, year, pop)
    supply = nitrogen_supply(c, year)
    can = min(1.0, supply / asked) if asked > 0 else 1.0
    need = max(0.0, min(1.0, (demand - free) / (full - free))) if full > free else 0.0
    floor = interp(k["paying_years"], k["paying_share"], year) if year >= k["paying_years"][0] else 0.0
    share = min(can, max(floor, need))
    capacity = central(c, base, year, pop, can)
    used = share * asked
    chile = min(used, max(0.0, used - home_nitrogen(c, year)))
    return {"demand": demand, "exports": export_mouths(c, year), "free": free, "full": full, "capacity": capacity,
            "share": share, "crop": min(demand, central(c, base, year, pop, share)), "asked": asked,
            "supply": supply, "used": used, "from_chile": chile, "from_home": used - chile}


def crossing(pop: dict[int, float], fed) -> int | None:
    """First year from which the Realm's residents stay above what a case feeds; None if fed in 1932."""
    last_fed = None
    for y in range(FIRST, LAST + 1):
        if pop[y] <= fed(y):
            last_fed = y
    if last_fed == LAST:
        return None
    return FIRST if last_fed is None else last_fed + 1


def crossing_ahead(c: dict, base: dict, pop: dict[int, float], frozen: bool) -> int:
    """After 1932: the year the Office's course passes the central case. Land stays at the ceilings;
    yields either stay at 1932's or go on up our timeline's ladder."""
    lv = c["levers"]
    r = rate(lambda y: pop[y], LAST)
    irr, dry = base_standard(c, base, LAST, "ceiling")
    for n in range(1, 200):
        k = research(c, LAST) if frozen else research(c, LAST + n)
        on_irr = k if c["yield_components"]["applies_to_irrigated"] else 1.0
        people = 1 - draft_share(c, LAST if frozen else LAST + n, "canon")
        fed = (irr * on_irr + dry * k) * people / lv["acres_per_head"] + sea_mouths(c, LAST)
        if project(pop[LAST], r, slowing(c, LAST), n, lv["horizon"]) > fed:
            return LAST + n
    return LAST + 200


# ---------------------------------------------------------------- the Office's tables

def rate(series, year: int, span: int = 10) -> float:
    return math.log(series(year) / series(year - span)) / span


def project(p0: float, r0: float, g_end: float, n: float, horizon: float) -> float:
    """The rate falls in a straight line from r0 to g_end over the horizon, then holds."""
    m = min(n, horizon)
    grown = r0 * m - (r0 - g_end) * m * m / (2 * horizon) + g_end * max(0.0, n - horizon)
    return p0 * math.exp(grown)


def slowing(c: dict, year: int) -> float:
    """The rate the Office lets growth fall to over a century, by the reign the table is made in."""
    lv = c["levers"]
    return lv["g_end_julian"] if year >= lv["julian_from"] else lv["g_end"]


def table(c: dict, base: dict, pop: dict[int, float], year: int, g_end: float | None = None) -> dict:
    lv = c["levers"]
    g = slowing(c, year) if g_end is None else g_end
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
    top = standard_acres(c, base, year, "ceiling") + sea_mouths(c, year) * lv["acres_per_head"]
    out["ceiling_std"] = top
    out["ceiling_mouths"] = top / lv["acres_per_head"]
    # The year the projected Realm passes the ceiling (0 if it already has).
    n = 0
    while project(pop[year], r_realm, g, n, lv["horizon"]) <= out["ceiling_mouths"] and n < 300:
        n += 1
    out["passes_ceiling"] = year + n
    return out


# ---------------------------------------------------------------- the century (CR-082 Part F, P-5)

def year_passed(c: dict, pop: dict[int, float], fed: float, year: int = 1930, g_end: float | None = None) -> int:
    """The year the Office's course from a table year passes a number of mouths."""
    lv = c["levers"]
    g = slowing(c, year) if g_end is None else g_end
    r = rate(lambda y: pop[y], year)
    n = 0
    while project(pop[year], r, g, n, lv["horizon"]) <= fed and n < 400:
        n += 1
    return year + n


def slowing_that_fits(c: dict, pop: dict[int, float], fed: float, year: int = 1930) -> float:
    """The rate the Office's course must fall to over the century for the Realm of a century on to be fed."""
    lv = c["levers"]
    r = rate(lambda y: pop[y], year)
    lo, hi = -0.10, r
    for _ in range(60):
        mid = (lo + hi) / 2
        if project(pop[year], r, mid, lv["horizon"], lv["horizon"]) > fed:
            hi = mid
        else:
            lo = mid
    return lo


def farmed_sea(c: dict, case: str = "central") -> float:
    """Work 5: mouths from farmed kelp and shellfish at a scale of farm."""
    k = c["century"]["mariculture"]
    ha = k["area_km2"][case] * 100
    return ha * k["dry_tonnes_per_ha"] * k["grain_equivalent"] / tonnes_per_mouth(c)


def century(c: dict, base: dict, pop: dict[int, float]) -> dict:
    """The provisioners' works a century after the table of 1930, in mouths on the Realm's diet."""
    lv, k = c["levers"], c["century"]
    t = table(c, base, pop, 1930)
    irr, dry = base_standard(c, base, LAST, "ceiling")
    home = (irr + dry) * k["yield_multiple"] / lv["acres_per_head"] + sea_mouths(c, LAST)
    # Work 2, the northern water, was withdrawn with CR-083 (author, 23 November 2026: the diversion is
    # dropped and appears nowhere; item 83-1). The works keep their numbers 1, 3, 4 and 5.
    sea = {case: farmed_sea(c, case) for case in k["mariculture"]["area_km2"]}
    sellers = [{"name": s["name"], "listed": s["listed"], "union": s.get("union", False),
                "now": s["about_1930"] * 1e6 / tonnes_per_mouth(c), "then": s["today"] * 1e6 / tonnes_per_mouth(c),
                "tonnes": s["today"] * 1e6} for s in k["sellers"]]
    every = sum(s["then"] for s in sellers)
    union = sum(s["then"] for s in sellers if s["union"])
    first = sum(s["then"] for s in sellers if s["listed"] == "2026-11-21" and not s["union"])
    tonnes = sum(s["tonnes"] for s in sellers)
    diet = 1 / (1 - k["diet_saving"])
    own = home + sea["central"]
    cases = [("Home yields alone (work 1)", home),
             ("And the farmed sea, central case (work 5)", own),
             ("And all that the first list sells, the Union apart (work 3)", own + first),
             ("And half of what every seller sells, the Union with them", own + every / 2),
             ("And all that every seller but the Union sells", own + every - union),
             ("And all of it, the Union with them", own + every)]
    rows = [{"name": n, "fed": f, "share": f / t["realm_100"], "passed": year_passed(c, pop, f),
             "slowing": slowing_that_fits(c, pop, f)} for n, f in cases]
    need = t["realm_100"]
    bought = max(0.0, min(1.0, (need - own) / every))
    bought_diet = max(0.0, min(1.0, (need / diet - own) / every))
    return {"need": need, "crown": t["crown_100"], "home": home, "home_1932": central(c, base, LAST, pop),
            "sea": sea, "own": own, "sellers": sellers, "every": every, "union": union,
            "first": first, "tonnes": tonnes, "diet": diet, "rows": rows, "plan": rows[-1],
            "gap": need - rows[-1]["fed"], "with_diet": own * diet + every * diet,
            "bought": bought, "bought_diet": bought_diet,
            "world_share": bought * tonnes / k["world_trade_today_tonnes"],
            "world_share_diet": bought_diet * tonnes / k["world_trade_today_tonnes"],
            "sellers_of_world": tonnes / k["world_trade_today_tonnes"]}


def endgame(c: dict) -> dict:
    """The contracts of 1931-32 (CR-083 A11, A12; CR-086 D3, D6): what they move, in mouths on the Realm's diet.

    None of it feeds anyone in the Realm before the margin closes: the wheat is resold abroad. The figures
    are the cabinet's second figure for the wheat contract and Giannini's case against it."""
    e = c["endgame"]
    per = tonnes_per_mouth(c)
    realm_sales = interp(c["exports"]["years"], c["exports"]["grain_tonnes"], LAST)
    out = {"prairie_tonnes": e["prairie_tonnes"], "prairie_mouths": e["prairie_tonnes"] / per,
           "prairie_share_of_canada": e["prairie_tonnes"] / e["canada_exports_1931_tonnes"],
           "prairie_against_realm_sales": e["prairie_tonnes"] / realm_sales,
           "prairie_cost": e["prairie_tonnes"] * e["prairie_price"], "realm_sales": realm_sales,
           "harvests": e["prairie_harvests"]}
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
    A("**Reworked on 22 November 2026** after the fresh-context review (B5, S1, S2, S10, M2, M3): irrigated land waits for "
      "its works; land that feeds horses and mules is taken out; nitrogen is what Chile and the home plants can give; "
      "capacity is told apart from crop (section 4); and the century's works are computed (section 8). The first "
      "draft's central case is kept as a row of section 9.")
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
    w = c["works"]
    A("**Works (review S2).** Irrigated land needs works. Canon's farmers can water "
      + ", ".join(f"{m(works_limit(c, base, y))} million acres by {y}" for y in w["years"])
      + f": first what our timeline's rivers watered before the great dams, then what the 1940 census calls works capable "
      f"of supplying, at last every irrigable acre. {w['named']} The dates are MODEL.")
    A("")
    yc, nn = c["yield_components"], c["nitrogen"]
    A("## 2. The rule for yields")
    A("")
    A(f"One head needs {lv['acres_per_head']} acres of average Union crop land on the Realm's diet (author: the same diet). "
      f"At history's yields an irrigated acre counts as {lv['irrigated_factor']} such acres and a dry western acre as "
      f"{lv['dry_factor']}.")
    A("")
    A("**The measure.** Washington's wheat is dry-farmed. Its yield in our timeline, as ten-year means against 1900–1929, "
      "beside what the six components below give when dated as they happened:")
    A("")
    marks = (1915, 1935, 1945, 1950, 1955, 1960, 1965, 1970)
    A("| Ten years centred on | " + " | ".join(str(y) for y in marks) + " |")
    A("|---" * (len(marks) + 1) + "|")
    A("| Our timeline (verified) | " + " | ".join(f"{ladder(c, y):.2f}" for y in marks) + " |")
    A("| The components, at history's dates | " + " | ".join(f"{research(c, y, 'history'):.2f}" for y in marks) + " |")
    A("")
    A("**The components.** Each is worth its gain once it is in the fields; the dates are when it gets there.")
    A("")
    A("| Component | Gain | Our timeline | Canon, earliest | Canon, central | Years gained (central) |")
    A("|---|---|---|---|---|---|")
    for it in yc["items"]:
        A(f"| {it['name']}{' (needs nitrogen)' if it['needs_nitrogen'] else ''} | {it['gain'] - 1:+.0%} | "
          f"{it['history'][0]}–{it['history'][1]} | {it['canon_earliest'][0]}–{it['canon_earliest'][1]} | "
          f"{it['canon_central'][0]}–{it['canon_central'][1]} | {it['history'][1] - it['canon_central'][1]} |")
    total = 1.0
    for it in yc["items"]:
        total *= it["gain"]
    A(f"| **All six** | **{total - 1:+.0%}** | | | | |")
    A("")
    decades = (1890, 1900, 1910, 1920, 1930, 1932, 1940)
    A("| The Realm's yields against history's | " + " | ".join(str(y) for y in decades) + " |")
    A("|---" * (len(decades) + 1) + "|")
    A("| Central dates | " + " | ".join(f"{research(c, y, 'canon_central'):.2f}" for y in decades) + " |")
    A("| Earliest dates | " + " | ".join(f"{research(c, y, 'canon_earliest'):.2f}" for y in decades) + " |")
    def our_year(k):
        return next((y for y in range(1930, 1971) if ladder(c, y) >= k), 1970)
    A("| Central: our timeline reached this in | " + " | ".join(
        (str(our_year(research(c, y, 'canon_central'))) if research(c, y, 'canon_central') > 1.05 else "—") for y in decades) + " |")
    A("")
    for it in yc["items"]:
        A(f"- **{it['name']}.** {it['basis']}")
    A("")
    A("## 3. People against what the home soil and sea could feed")
    A("")
    A("| Year | Residents | History's acres | Canon's farmers | + concerted research, no nitrogen | + nitrogen as it can be got | "
      "+ the sea (capacity) | Capacity against residents |")
    A("|---|---|---|---|---|---|---|---|")
    for y in (1880, 1890, 1900, 1910, 1920, 1930, 1932):
        f = {k: mouths(c, base, y, k, pop) for k in ("history", "farmers")}
        cen = central(c, base, y, pop)
        A(f"| {y} | {m(pop[y])} | {m(f['history'])} | {m(f['farmers'])} | {m(mouths(c, base, y, 'research', pop, 0.0))} | "
          f"{m(mouths(c, base, y, 'research', pop))} | {m(cen)} | {cen / pop[y]:.0%} |")
    A("")
    A("Millions fed on the Realm's diet. *Canon's farmers* work as many acres a head as our timeline's residents did on "
      f"the same land, until the works (section 1), the irrigated ceiling ({m(ceiling_area(c, base))} million acres) and "
      f"the dry ceiling ({m(base['dry'] * lv['dry_ceiling_factor'])} million) stop them. Land that feeds horses and mules "
      f"is taken out: {draft_share(c, 1910, 'history'):.0%} of crop land in 1910 in our timeline, "
      f"{draft_share(c, 1930, 'history'):.0%} in 1930; canon's tractors bring it to {draft_share(c, 1925, 'canon'):.0%} by 1925. "
      "The years before 1880 are left out: the early acreages are guesses.")
    A("")
    A("**The measure checked on our timeline.** History's acres against history's own people inside the frontier: "
      + ", ".join(f"{mouths(c, base, y, 'history') / history_people(c, y):.0%} in {y}" for y in (1900, 1910, 1920, 1930))
      + ". Our timeline's West fed itself with a shrinking margin and sold wheat and fruit abroad, which is about what the "
      "measure says.")
    A("")
    x_f = crossing(pop, lambda y: mouths(c, base, y, "farmers", pop))
    x_c = crossing(pop, lambda y: central(c, base, y, pop))
    x_0 = crossing(pop, lambda y: central(c, base, y, pop, 0.0))
    x_n = crossing(pop, lambda y: central(c, base, y, pop, "canon"))
    A(f"- **Without research** (canon's farmers at history's yields) the Realm outgrows its own soil in **{x_f}**.")
    A(f"- **With research but no bought nitrogen** it outgrows soil and sea in **{x_0 if x_0 else 'no year to 1932'}**.")
    if x_c:
        A(f"- **Central case:** the Realm outgrows its own soil and sea in **{x_c}**.")
    else:
        A(f"- **Central case:** the Realm could still feed itself in {LAST}, with {central(c, base, LAST, pop) / pop[LAST] - 1:.0%} "
          f"to spare. On the Office's course it outgrows soil and sea in **{crossing_ahead(c, base, pop, True)}** if yields stay "
          f"at 1932's, and in **{crossing_ahead(c, base, pop, False)}** once the weedkiller, the last component, is in the fields.")
    fed_n = central(c, base, LAST, pop, "canon")
    A(f"- **With nitrogen as canon now has it** ({nn['canon_total_1929'] / 1000:.0f} thousand tonnes in 1929, half to farms) "
      f"the capacity of {LAST} is {m(fed_n)} million, {fed_n / pop[LAST]:.0%} of residents"
      + (f"; the Realm outgrows it in **{x_n}**." if x_n else "."))
    A("")
    A("## 4. Capacity against crop (review B5)")
    A("")
    A("What could be grown is not what is grown. The crop is the Realm's own table and what it sells abroad. The methods "
      "that cost nothing an acre (seed, drill, fallow, tractor) are in every field as soon as they exist. Nitrogen and the "
      "short wheats that need it go on as the margin narrows: never less than the paying crops take, never more than "
      "there is to buy.")
    A("")
    A("| Year | Residents | Sold abroad | Crop grown | Capacity | Idle capacity | Nitrogen-bound gain in the fields | "
      "Nitrogen used | from Chile | from home plants | Chile's share taken | The full ask |")
    A("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for y in (1890, 1900, 1905, 1910, 1915, 1917, 1920, 1925, 1930, 1932):
        f = fields(c, base, y, pop)
        sold = max(0.0, f["crop"] - pop[y])
        A(f"| {y} | {m(pop[y])} | {m(sold)} | {m(f['crop'])} | {m(f['capacity'])} | {m(f['capacity'] - f['crop'])} | "
          f"{f['share']:.0%} | {f['used'] / 1000:.0f} | {f['from_chile'] / 1000:.0f} | {f['from_home'] / 1000:.0f} | "
          f"{f['from_chile'] / chile_nitrogen(c, y):.0%} | {f['asked'] / 1000:.0f} |")
    A("")
    ex = c["exports"]
    lo_w, hi_w = ex["world_wheat_trade_1920s_tonnes"]
    A(f"People and mouths in millions; nitrogen in thousand tonnes a year. A mouth is {tonnes_per_mouth(c):.2f} tonnes of grain "
      f"or its equivalent. *Sold abroad* (MODEL): {ex['buyers']} At {interp(ex['years'], ex['grain_tonnes'], 1929) / 1e6:.0f} "
      f"million tonnes in 1929 it is about a sixth of the world's wheat trade ({lo_w / 1e6:.0f}–{hi_w / 1e6:.1f} million tonnes "
      "a year in the late 1920s). *The full ask* is the nitrogen the two nitrogen-bound components would take in every field "
      f"(canon's own {nn['grain_per_tonne_n']} tonnes of grain per tonne). The Realm takes at most "
      f"{c['nitrogen_supply']['chile_share_max']:.0%} of Chile's trade; the home plants give "
      + ", ".join(f"{home_nitrogen(c, y) / 1000:.0f} thousand tonnes in {y}" for y in (1920, 1925, 1930))
      + " to the fields (MODEL; review S1).")
    f17 = fields(c, base, 1917, pop)
    sold17 = max(0.0, f17["crop"] - pop[1917])
    A("")
    A(f"In 1917 the Entente asks {interp(ex['years'], ex['grain_tonnes'], 1917) / 1e6:.0f} million tonnes. Capacity binds "
      f"that year, so the Realm ships {m(sold17)} million mouths, about {sold17 * tonnes_per_mouth(c) / 1e6:.1f} million tonnes "
      "(CR-082 review 2, S1).")
    A("")
    f10, f29, f32 =fields(c, base, 1910, pop), fields(c, base, 1929, pop), fields(c, base, 1932, pop)
    margins = {y: central(c, base, y, pop) / pop[y] for y in range(1890, LAST + 1)}
    best = max(margins, key=margins.get)
    late = [v for y, v in margins.items() if y >= 1905]
    A(f"- **The margin is thin.** Capacity is at most {margins[best] - 1:.0%} above residents (in {best}, before the rivers' "
      f"own flow is all in use) and between {min(late) - 1:.0%} and {max(late) - 1:.0%} above them from 1905. "
      "No table shows a country twice fed.")
    A(f"- **Chile is needed early.** By 1910 the fields take {f10['used'] / 1000:.0f} thousand tonnes of nitrogen, "
      f"{f10['from_chile'] / chile_nitrogen(c, 1910):.0%} of all Chile exports. Without it the Realm could sell "
      f"{m(max(0.0, f10['free'] - pop[1910]))} million mouths' worth abroad in 1910 instead of {m(f10['crop'] - pop[1910])}, "
      f"and from {crossing(pop, lambda y: central(c, base, y, pop, 0.0))} it could not feed itself.")
    A(f"- **The home plants take over in the 1920s.** In 1929 the fields use {f29['used'] / 1000:.0f} thousand tonnes "
      f"and in 1932 {f32['used'] / 1000:.0f}, against CR-054's {nn['canon_total_1929'] * nn['canon_farm_share'] / 1000:.0f} "
      f"for farms in 1929 and the first draft's {nitrogen_needed(c, base, 1930, pop) / 1000:.0f}.")
    A("")
    A("## 5. Japan's rice (the Concord's side)")
    A("")
    jr = japanese_in_realm()
    A("| Year | People, our timeline | People, canon | Rice a head (koku) | Own crop | Gap, our timeline | Gap, canon | "
      "Gap if the crop keeps growing | Yields needed for no gap | The Realm's surplus |")
    A("|---|---|---|---|---|---|---|---|---|---|")
    for y in (1890, 1900, 1910, 1920, 1930, 1932):
        j = japan(c, y, jr)
        spare = central(c, base, y, pop) - pop[y]
        A(f"| {y} | {m(j['people'])} | {m(j['canon_people'])} | {j['head']:.2f} | {m(j['crop'])} | "
          f"{m(j['gap_history'])} ({j['gap_history'] / (j['people'] * j['head']):.0%}) | "
          f"{m(j['gap_canon'])} ({j['gap_canon'] / (j['canon_people'] * j['head']):.0%}) | "
          f"{m(j['gap_canon_on'])} | {j['canon_people'] * j['head'] / j['crop']:.2f} | {m(spare)} mouths |")
    A("")
    j = japan(c, LAST, jr)
    A("People in millions; crop and gaps in millions of koku of brown rice (a koku is about 150 kg and feeds one person a "
      "year, near enough). *Gap, our timeline* is what Japan bought, mostly from its colonies; in 1929–33 Korea alone sent "
      f"{c['japan']['korea_koku']['1931'] / 1e6:.2f} million koku a year. Canon's Japan has no colonies to buy from, but "
      f"about {m(j['people'] - j['canon_people'])} million fewer mouths, because they are in the Realm. *If the crop keeps growing* "
      "drops our timeline's stagnation of 1920–35, which Hayami and Ruttan put down to the colonial rice itself. "
      "*Yields needed for no gap* is what canon's Japan must grow, against our timeline's crop of the same year, for its "
      "rice never to fall short (the author's wish of 18:52; a requirement for the partners' CR).")
    per = lv["acres_per_head"] * c["nitrogen"]["grain_per_standard_acre"] * 1000 / c["japan"]["kg_per_koku"]
    A("")
    A(f"The land behind one mouth on the Realm's diet grows about {per:.0f} koku of grain or its equivalent, so the Realm's "
      f"surplus of {LAST} is some {(central(c, base, LAST, pop) - pop[LAST]) * per / 1e6:.0f} million koku-equivalents against a "
      f"Japanese gap of {m(j['gap_canon'])} million koku. It is mostly wheat and feed, not rice.")
    A("")
    A("## 6. The Philippine crown, from 1908 (its own ledger)")
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
    A("## 7. The Office's tables")
    A("")
    A(f"From each table year the yearly rate falls in a straight line from the last decade's rate, over a century, to "
      f"{lv['g_end']:.1%} in the tables before {lv['julian_from']} and to {lv['g_end_julian']:.1%} in the tables of Julian's reign "
      "(author: Julian is a provisioner, so the Office assumes less slowing for the time being; the figure itself is the "
      "script's reading). The home ceiling is every irrigable and dry acre at the table year's yields, with the sea, "
      "less the land that feeds work stock in that year. *Realm passes it* is the table's own forecast; it is a different "
      "measure from section 3's crossing, which follows the yields as they in fact rise.")
    A("")
    A("| Table | Residents | Crown | Rate | In 25 years (Realm + crown) | In 50 (Realm + crown) | In 100 (Realm + crown) | "
      "Home ceiling feeds | Realm passes it | A century's need against the ceiling |")
    A("|---|---|---|---|---|---|---|---|---|---|")
    rows = []
    for y in TABLES:
        t = table(c, base, pop, y)
        rows.append(t)
        when = "already past" if t["passes_ceiling"] <= y else str(t["passes_ceiling"])
        A(f"| {y} | {m(t['realm'])} | {m(t['crown']) if t['crown'] else '—'} | {t['rate']:.1%} | "
          f"{m(t['realm_25'])} + {m(t['crown_25'])} | {m(t['realm_50'])} + {m(t['crown_50'])} | "
          f"{m(t['realm_100'])} + {m(t['crown_100'])} = {m(t['realm_100'] + t['crown_100'])} | "
          f"{m(t['ceiling_mouths'])} | {when} | {t['need_100'] / t['ceiling_std']:.0f} times |")
    A("")
    last = rows[-1]
    top70 = (last["ceiling_std"] - sea_mouths(c, 1930) * lv["acres_per_head"]) / research(c, 1930) * ladder(c, 1970)
    A(f"The table of 1930: {m(last['realm_100'])} million in the Realm a century on need "
      f"{last['need_100'] / 1e6:,.0f} million acres of average Union crop land, "
      f"{last['need_100'] / lv['union_cropland_1925_29']:.1f} times all the crop land the Union worked in 1925–29. "
      f"Even at our timeline's yields of 1966–75 the home ceiling gives about {top70 / 1e6:,.0f} million such acres, "
      f"one part in {last['need_100'] / top70:.0f}.")
    A("")
    A("## 8. The century: the provisioners' works (CR-082 Part F, P-5)")
    A("")
    cy, kc = century(c, base, pop), c["century"]
    A(f"Julian's table of 1930 has **{m(cy['need'])} million** in the Realm a century on (and {m(cy['crown'])} million under "
      "the Philippine crown, on its own ledger). Everything below is in mouths on the Realm's diet of today. "
      f"{kc['grain_trade_aim']}")
    A("")
    A(f"**Work 1, home yields.** Every irrigable and dry acre at {kc['yield_multiple']} times the yields of 1900–29 "
      f"(what Washington's dry wheat gives in our timeline today), no horses, and the wild sea as in 1930: **{m(cy['home'])} "
      f"million**, against a capacity of {m(cy['home_1932'])} million in {LAST}.")
    A("")
    A("**Work 2, the northern water, is withdrawn** (CR-083; author, 23 November 2026). Nothing is counted for it.")
    A("")
    mc = kc["mariculture"]
    A("**Work 5, the farmed sea** (author, 22 November 2026: a Pacific kelp aquaculture industry as a century project).")
    A("")
    A("| Case | Farms | Mouths |")
    A("|---|---|---|")
    for case, v in cy["sea"].items():
        A(f"| {case.capitalize()} | {mc['area_km2'][case]:,} km² | {m(v)} million |")
    A("")
    A(f"{mc['basis']} It is a useful work but not a large one: the central case is a fifth of what home yields give.")
    A("")
    A("**Work 3, the sellers, as trading partners.** What each sells abroad, about 1930 and a century on. The century's "
      "figure is what the same lands sell in our timeline today. None is taken; every one is bought from.")
    A("")
    A("| Seller | Listed | About 1930 (million tonnes) | In mouths | A century on (million tonnes) | In mouths |")
    A("|---|---|---|---|---|---|")
    for sv, src in zip(cy["sellers"], kc["sellers"]):
        when = "first list" if sv["listed"] == "2026-11-21" else "added 22 Nov."
        A(f"| {sv['name']} | {when} | {src['about_1930']} | {m(sv['now'])} | {src['today']} | {m(sv['then'])} |")
    A(f"| **Every seller** | | | **{m(sum(s['now'] for s in cy['sellers']))}** | **{cy['tonnes'] / 1e6:.0f}** | **{m(cy['every'])}** |")
    A("")
    A(f"Together these sellers are {cy['sellers_of_world']:.0%} of the world's trade in grain and soybeans today "
      f"({kc['world_trade_today_tonnes'] / 1e6:.0f} million tonnes a year; {kc['world_trade_status']}).")
    A("")
    A(f"**Work 4, the thriftier table: pending the culinary CR.** At {kc['diet_saving']:.0%} less land a head every acre and "
      f"every bought tonne would feed {cy['diet'] - 1:.0%} more people. It is shown apart and kept out of the totals.")
    A("")
    A("**Whether it closes.**")
    A("")
    A("| Works | Mouths fed | Share of the table's Realm | The Office's course passes it in | Slowing that would fit |")
    A("|---|---|---|---|---|")
    for r in cy["rows"]:
        fit = f"{r['slowing']:.2%} a year" if r["slowing"] > 0 else "growth must end within the century"
        if r["slowing"] >= lv["g_end_julian"]:
            fit += " (Julian's table fits)"
        A(f"| {r['name']} | {m(r['fed'])} | {r['share']:.0%} | {r['passed']} | {fit} |")
    A("")
    pl = cy["plan"]
    A(f"- **The Realm's own works feed {m(cy['own'])} million** (home and the farmed sea), "
      f"{cy['own'] / cy['need']:.0%} of the need. Everything else is bought.")
    A(f"- **The plan closes only by buying.** To feed {m(cy['need'])} million the Realm must buy **{cy['bought']:.0%}** of "
      f"everything these sellers sell abroad, which is about **{cy['world_share']:.0%} of the world's grain and soybean "
      f"trade** of today. With every tonne of it, the works feed {m(pl['fed'])} million, {pl['share']:.0%}.")
    A(f"- **With the thriftier table** (work 4, pending) it must buy {cy['bought_diet']:.0%} of what they sell, about "
      f"{cy['world_share_diet']:.0%} of the world's trade.")
    A(f"- **Without the Union** the plan needs every tonne that every other seller sells, and then reaches "
      f"{cy['rows'][4]['share']:.0%}: with the Union in the list it has room to share the trade with other buyers.")
    A("- **This is the strategic ambition the author named:** not land but the grain trade. Japan, China and every other "
      "importer buy from the same pool, so the Realm's share is contested, and the share is only as safe as the sea lanes, "
      "the inputs and the means to pay.")
    A("- **What is not counted:** other buyers' demand, the sellers' meat, butter and wool, Caledonia's own land and people, "
      "the Philippine crown's own frontier, and a bad year.")
    A("")
    A(f"`[century]`: {kc['status']}")
    A("")
    eg = endgame(c)
    A("### The contracts of 1931-32 (CR-083, CR-086)")
    A("")
    A(f"- **The prairie wheat contract** (the Patrimony's board, December 1931; CR-083 A11): {eg['prairie_tonnes'] / 1e6:.1f} "
      f"million tonnes a harvest for {eg['harvests']} harvests, {eg['prairie_share_of_canada']:.0%} of what Canada sold abroad "
      f"in 1931-32. At the slump's price it costs the board ${eg['prairie_cost'] / 1e6:.0f} million a year.")
    A(f"- **Mouths fed in the Realm: 0.** The wheat is resold in Asia. Abroad it is bread for {m(eg['prairie_mouths'])} million "
      "on the Realm's diet, which is the cabinet's second figure for the contract (CR-083 A12).")
    A(f"- **Giannini's case.** The Realm itself sells {eg['realm_sales'] / 1e6:.1f} million tonnes abroad in {LAST}. The board's "
      f"wheat is {eg['prairie_against_realm_sales']:.0%} of that, sold to the same buyers.")
    A("- **Article II** (CR-086 D6) feeds no one in the Realm. Its schedule is this contract, New Zealand's crop guarantee and "
      "the private houses' Pampas contracts; the Pampas volumes are not modelled.")
    A("")
    A(f"`[endgame]`: {c['endgame']['status']}")
    A("")
    A("## 9. What moves the result")
    A("")
    A("| Lever | Value | Capacity in 1910 | Share of residents | Capacity in 1932 | Share of residents | "
      "Table of 1930: need against ceiling |")
    A("|---|---|---|---|---|---|---|")
    def variant(name, value, section="levers", **kw):
        c2 = cfg()
        if section == "first_draft":
            c2["works"]["basis"] = ["irrigable_in_enterprises_1940"] * 3
            c2["draft"].update(history_share=[0.0] * 5, canon_share=[0.0] * 4)
            c2["nitrogen_supply"].update(chile_share_max=10.0)
        else:
            c2[section].update(kw)
        b2 = land_1929(c2)
        fed, early = central(c2, b2, LAST, pop), central(c2, b2, 1910, pop)
        t = table(c2, b2, pop, 1930)
        A(f"| {name} | {value} | {m(early)} | {early / pop[1910]:.0%} | {m(fed)} | {fed / pop[LAST]:.0%} | "
          f"{t['need_100'] / t['ceiling_std']:.0f} times |")
    variant("As built (central dates)", "—")
    variant("The works as in the first draft", "22 million irrigated acres as soon as there are farmers", "works",
            basis=["irrigable_in_enterprises_1940"] * 3)
    variant("No land for work stock", "as in the first draft", "draft", history_share=[0.0] * 5, canon_share=[0.0] * 4)
    variant("Both, and all the nitrogen asked for", "the first draft's central case", "first_draft")
    variant("The Realm takes more of Chile's trade", "60%", "nitrogen_supply", chile_share_max=0.60)
    variant("No home ammonia for the fields", "Chile only", "nitrogen_supply", home_farm_tonnes=[0] * 6)
    variant("Earliest dates for the other four", "—", "yield_components", mode="earliest")
    variant("Research on dry land only", "irrigated yields as history's", "yield_components", applies_to_irrigated=False)
    variant("Irrigated acre", "counts 2.5", irrigated_factor=2.5)
    variant("Dry-farm ceiling", "the 1929 land and no more", dry_ceiling_factor=1.0)
    variant("The sea", "twice our timeline's peak", "sea", index=[0.02, 0.10, 2.00])
    variant("No sea", "—", "sea", index=[0.0, 0.0, 0.0])
    variant("A leaner diet", "1.5 acres a head", acres_per_head=1.5)
    variant("Julian's tables slow to", "1.5% a year", g_end_julian=0.015)
    variant("Julian's tables slow to", "2.5% a year", g_end_julian=0.025)
    A("")
    A("## 10. Not sourced, or weakly")
    A("")
    for key, where in (("status", "yield_components"), ("irrigated_status", "yield_components"), ("status", "nitrogen"),
                       ("chile_status", "nitrogen"), ("status", "nitrogen_supply"), ("paying_status", "nitrogen_supply"),
                       ("status", "works"), ("status", "draft"), ("status", "exports"), ("yield_status", "century"),
                       ("diet_status", "century"), ("world_trade_status", "century"),
                       ("status", "sea"), ("alaska_status", "sea"), ("status", "japan"), ("people_status", "japan"),
                       ("kg_status", "japan"), ("factor_status", "levers"),
                       ("status", "territory"), ("status", "dry_cropland"), ("pct_status", "cropland_1929"),
                       ("harvested_status", "cropland_1929"), ("california_status", "cropland_1929"), ("status", "crown")):
        A(f"- `[{where}]`: {c[where][key]}")
    A("- Range and pasture are left out on both sides of the account; so are Hawaii's cane, fishponds and hatcheries, and the Japan series.")
    (OUT / "provisioning.md").write_text("\n".join(L) + "\n", encoding="utf-8")

    with (OUT / "provisioning_by_year.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["year", "residents", "crown_people", "fed_history", "fed_farmers", "fed_research", "fed_ceiling",
                    "fed_sea", "fed_central", "yields_against_history", "nitrogen_needed_t",
                    "irrigated_history", "irrigated_farmers", "dry_history", "dry_farmers", "crown_fed",
                    "crop_grown", "sold_abroad", "nitrogen_share", "nitrogen_used_t", "nitrogen_from_chile_t",
                    "nitrogen_supply_t", "works_limit_acres"])
        for y in range(FIRST, LAST + 1):
            w.writerow([y, round(pop[y]), round(crown_people(c, y))] +
                       [round(mouths(c, base, y, k, pop)) for k in CASES] +
                       [round(sea_mouths(c, y)), round(central(c, base, y, pop)), round(research(c, y), 3),
                        round(nitrogen_needed(c, base, y, pop))] +
                       [round(acres(c, base, y, "history")[0]), round(acres(c, base, y, "farmers", pop)[0]),
                        round(acres(c, base, y, "history")[1]), round(acres(c, base, y, "farmers", pop)[1]),
                        round(crown_fed(c, y))] +
                       (lambda f: [round(f["crop"]), round(max(0.0, f["crop"] - pop[y])), round(f["share"], 3),
                                   round(f["used"]), round(f["from_chile"]), round(f["supply"]),
                                   round(works_limit(c, base, y))])(fields(c, base, y, pop)))
    print(f"wrote {OUT / 'provisioning.md'} and provisioning_by_year.csv")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
