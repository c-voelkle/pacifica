"""The provisioning account (CR-082): people against the food the domain can grow.

What it does
  * People: the Realm's residents from the canon run (outputs/canon_by_year.csv)
    and, from 1908, the Philippine crown (our timeline's censuses).
  * Home supply: our timeline's irrigated and dry crop land inside Pacifica's
    frontier, turned into acres of average Union crop land and then into mouths
    on the Realm's diet. Cases, each building on the last: history's acres;
    canon's farmers (history's acres a head for canon's larger population, up to
    the ceilings); concerted research (the central case: the Realm farms as our
    timeline farmed the same land a generation later); and the sea.
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
        return min(irr * k, top_irr), min(dry * k, top_dry)
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


def standard_acres(c: dict, base: dict, year: int, case: str, pop=None, nitrogen: str = "supplied") -> float:
    """Acres of average Union crop land the home soil is worth in a year, for a case."""
    irr, dry = base_standard(c, base, year, case, pop)
    if case in ("history", "farmers"):
        return irr + dry
    lifted = (irr if c["yield_components"]["applies_to_irrigated"] else 0.0) + dry
    share = 1.0
    if nitrogen == "canon":      # only as much of the nitrogen-bound gain as canon's own nitrogen buys
        n = c["nitrogen"]
        asked = lifted * (research(c, year) - research(c, year, nitrogen=0.0))
        bought = canon_farm_nitrogen(c, year) * n["grain_per_tonne_n"] / n["grain_per_standard_acre"]
        share = min(1.0, bought / asked) if asked > 0 else 1.0
    return irr + dry + lifted * (research(c, year, nitrogen=share) - 1)


def nitrogen_needed(c: dict, base: dict, year: int, pop) -> float:
    """Tonnes of nitrogen a year the nitrogen-bound components ask for."""
    n = c["nitrogen"]
    irr, dry = base_standard(c, base, year, "research", pop)
    lifted = (irr if c["yield_components"]["applies_to_irrigated"] else 0.0) + dry
    gain = lifted * (research(c, year) - research(c, year, nitrogen=0.0))
    return gain * n["grain_per_standard_acre"] / n["grain_per_tonne_n"]


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


def central(c: dict, base: dict, year: int, pop, nitrogen: str = "supplied") -> float:
    """The central case: canon's farmers, concerted research and the sea."""
    return mouths(c, base, year, "research", pop, nitrogen) + sea_mouths(c, year)


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
        fed = (irr * on_irr + dry * k) / lv["acres_per_head"] + sea_mouths(c, LAST)
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
    A("## 3. People against home supply")
    A("")
    A("| Year | Residents | History's acres | Canon's farmers | + concerted research | + the sea (central case) | Share fed |")
    A("|---|---|---|---|---|---|---|")
    for y in (1861, 1870, 1880, 1890, 1900, 1910, 1920, 1930, 1932):
        f = {k: mouths(c, base, y, k, pop) for k in CASES}
        cen = central(c, base, y, pop)
        A(f"| {y} | {m(pop[y])} | {m(f['history'])} | {m(f['farmers'])} | {m(f['research'])} | {m(cen)} | {cen / pop[y]:.0%} |")
    A("")
    A("Millions fed on the Realm's diet. *Canon's farmers* work as many acres a head as our timeline's residents did on "
      f"the same land, until the irrigated ceiling ({m(ceiling_area(c, base))} million acres) and the dry ceiling "
      f"({m(base['dry'] * lv['dry_ceiling_factor'])} million) stop them.")
    A("")
    x_f = crossing(pop, lambda y: mouths(c, base, y, "farmers", pop))
    x_c = crossing(pop, lambda y: central(c, base, y, pop))
    x_n = crossing(pop, lambda y: central(c, base, y, pop, "canon"))
    A(f"- **Without research** (canon's farmers at history's yields) the Realm outgrows its own soil in **{x_f}**.")
    if x_c:
        A(f"- **Central case:** the Realm outgrows its own soil and sea in **{x_c}**.")
    else:
        A(f"- **Central case:** the Realm still feeds itself in {LAST}, with {central(c, base, LAST, pop) / pop[LAST] - 1:.0%} to spare. "
          f"On the Office's course it outgrows soil and sea in **{crossing_ahead(c, base, pop, True)}** if yields stay at "
          f"1932's, and in **{crossing_ahead(c, base, pop, False)}** once the weedkiller, the last component, is in the fields.")
    A(f"- **With nitrogen as canon now has it** ({nn['canon_total_1929'] / 1000:.0f} thousand tonnes in 1929, half to farms) "
      f"the central case feeds {m(central(c, base, LAST, pop, 'canon'))} million in {LAST} and the Realm outgrows it in "
      f"**{x_n if x_n else 'no year before 1933'}**.")
    A("")
    A("## 4. What the central case asks for")
    A("")
    A("| Year | Irrigated acres | Dry acres | Nitrogen needed | All Chile's exports hold | Canon's farm nitrogen (CR-054) | The sea feeds |")
    A("|---|---|---|---|---|---|---|")
    for y in (1890, 1900, 1905, 1910, 1915, 1920, 1930):
        i, d = acres(c, base, y, "research", pop)
        A(f"| {y} | {m(i)} | {m(d)} | {nitrogen_needed(c, base, y, pop) / 1000:.0f} | {chile_nitrogen(c, y) / 1000:.0f} | "
          f"{canon_farm_nitrogen(c, y) / 1000:.0f} | {m(sea_mouths(c, y))} |")
    A("")
    A(f"Acres in millions, nitrogen in thousand tonnes a year, the sea in millions of mouths. Nitrogen is counted at canon's "
      f"own {nn['grain_per_tonne_n']} tonnes of grain per tonne, for the gain of the two components that need it (cheap "
      "nitrogen and the short-straw wheats). Our timeline irrigated "
      f"{m(acres(c, base, 1929, 'history')[0])} million acres on the same land in 1929.")
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
      "script's reading). The home ceiling is every irrigable and dry acre at the table year's yields, with the sea.")
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
    top70 = (last["ceiling_std"] - sea_mouths(c, 1930) * lv["acres_per_head"]) / research(c, 1930) * ladder(c, 1970)
    A(f"The table of 1930: {m(last['realm_100'])} million in the Realm a century on need "
      f"{last['need_100'] / 1e6:,.0f} million acres of average Union crop land, "
      f"{last['need_100'] / lv['union_cropland_1925_29']:.1f} times all the crop land the Union worked in 1925–29. "
      f"Even at our timeline's yields of 1966–75 the home ceiling gives about {top70 / 1e6:,.0f} million such acres, "
      f"one part in {last['need_100'] / top70:.0f}.")
    A("")
    A("## 8. What moves the result")
    A("")
    A("| Lever | Value | Central case feeds in 1932 | Share of residents | Table of 1930: need against ceiling |")
    A("|---|---|---|---|---|")
    def variant(name, value, section="levers", **kw):
        c2 = cfg()
        c2[section].update(kw)
        b2 = land_1929(c2)
        fed = central(c2, b2, LAST, pop)
        t = table(c2, b2, pop, 1930)
        A(f"| {name} | {value} | {m(fed)} | {fed / pop[LAST]:.0%} | {t['need_100'] / t['ceiling_std']:.0f} times |")
    variant("As built (central dates)", "—")
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
    A("## 9. Not sourced, or weakly")
    A("")
    for key, where in (("status", "yield_components"), ("irrigated_status", "yield_components"), ("status", "nitrogen"),
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
                    "irrigated_history", "irrigated_farmers", "dry_history", "dry_farmers", "crown_fed"])
        for y in range(FIRST, LAST + 1):
            w.writerow([y, round(pop[y]), round(crown_people(c, y))] +
                       [round(mouths(c, base, y, k, pop)) for k in CASES] +
                       [round(sea_mouths(c, y)), round(central(c, base, y, pop)), round(research(c, y), 3),
                        round(nitrogen_needed(c, base, y, pop))] +
                       [round(acres(c, base, y, "history")[0]), round(acres(c, base, y, "farmers", pop)[0]),
                        round(acres(c, base, y, "history")[1]), round(acres(c, base, y, "farmers", pop)[1]),
                        round(crown_fed(c, y))])
    print(f"wrote {OUT / 'provisioning.md'} and provisioning_by_year.csv")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
