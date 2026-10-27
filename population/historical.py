"""Our-timeline validation of the cohort engine.

1. Native Hawaiians 1853-1896, a population without migration: calibrate
   (e0, TFR) to the census decline, then test the calibration against an
   independent measure (share under 15 in 1866 and 1872) and against Honolulu's
   life expectancy in 1884.
2. California 1850-1900 by census group: project each group between censuses
   and solve for the constant annual net migration that reproduces the next
   census. This yields historical net migration by group and decade.
3. Native Californians 1848-1900: loss beyond the worst life-table mortality.

Run:  python3 population/historical.py   (writes population/outputs/historical.md
and population/outputs/native_hawaiian_calibration.csv)
"""
from __future__ import annotations

import csv
import math
import sys
from pathlib import Path

import cohort
from cohort import Group, Rates, load

OUT = Path(__file__).resolve().parent / "outputs"


# ---------------------------------------------------------------------------
# 1. Native Hawaiians
# ---------------------------------------------------------------------------

def run_closed(start_total: float, rates: Rates, start_year: int, end_year: int,
               keep: tuple[int, ...] = ()) -> dict[int, Group]:
    g = cohort.stable_structure(rates, start_total)
    out = {start_year: _copy(g)}
    for y in range(start_year, end_year):
        cohort.step(g, rates)
        if y + 1 in keep or y + 1 == end_year:
            out[y + 1] = _copy(g)
    return out


def _copy(g: Group) -> Group:
    c = Group(g.name)
    c.F, c.M = list(g.F), list(g.M)
    return c


def under15(g: Group) -> float:
    return (sum(g.F[:15]) + sum(g.M[:15])) / g.total()


def calibrate_native_hawaiian() -> dict:
    h = load("census")["hawaii"]
    years, obs = h["native_hawaiian_years"], h["native_hawaiian"]
    rng = load("assumptions")["native_hawaiian_calibration"]
    targets = dict(zip(years, obs))
    end = years[-1]

    def sse(e0: float, tfr: float):
        res = run_closed(obs[0], Rates(e0, tfr), years[0], end, keep=tuple(years))
        err = sum(math.log(res[y].total() / targets[y]) ** 2 for y in years[1:])
        return err, res

    # For each TFR, the e0 that best reproduces the decline (golden-section search).
    family = []
    tfr = rng["tfr_range"][0]
    while tfr <= rng["tfr_range"][1] + 1e-9:
        lo, hi = rng["e0_range"]
        gr = (math.sqrt(5) - 1) / 2
        a, b = lo, hi
        c, d = b - gr * (b - a), a + gr * (b - a)
        fc, fd = sse(c, tfr)[0], sse(d, tfr)[0]
        for _ in range(18):
            if fc < fd:
                b, d, fd = d, c, fc
                c = b - gr * (b - a)
                fc = sse(c, tfr)[0]
            else:
                a, c, fc = c, d, fd
                d = a + gr * (b - a)
                fd = sse(d, tfr)[0]
        e0 = (a + b) / 2
        err, res = sse(e0, tfr)
        family.append({"tfr": round(tfr, 2), "e0": round(e0, 2), "rmse_log": math.sqrt(err / (len(years) - 1)),
                       "u15_1866": under15(res[1866]), "u15_1872": under15(res[1872]),
                       "fit": {y: res[y].total() for y in years}})
        tfr += 0.25

    # Independent test: Native Hawaiian under-15 share must lie between the whole-population
    # share (non-Hawaiians with as many children) and that share divided by the Hawaiian
    # fraction (non-Hawaiians with none).
    ch = dict(zip(h["characteristics_years"], h["pct_under_15"]))
    nh = dict(zip(h["native_hawaiian_years"], h["native_hawaiian"]))
    tot = dict(zip(h["years"], h["total"]))
    bounds = {y: (ch[y] / 100, ch[y] / 100 / (nh[y] / tot[y])) for y in (1866, 1872)}
    for f in family:
        f["passes_u15"] = all(bounds[y][0] <= f[f"u15_{y}"] <= bounds[y][1] for y in (1866, 1872))
        f["below_honolulu_e0"] = f["e0"] <= h["honolulu_e0_1884"]
    ok = [f for f in family if f["passes_u15"] and f["below_honolulu_e0"]]
    chosen = min(ok, key=lambda f: f["rmse_log"]) if ok else min(family, key=lambda f: f["rmse_log"])
    return {"family": family, "bounds": bounds, "chosen": chosen, "any_pass": bool(ok), "obs": targets}


# ---------------------------------------------------------------------------
# 2. California by census group
# ---------------------------------------------------------------------------

def male_share(stream: str, year: int, table: str = "migration_otl") -> float:
    pairs = load("assumptions")[table][stream]
    return [v for y, v in pairs if y <= year][-1]


def implied_migration(group: Group, rates_fn, stream: str, y0: int, y1: int, target: float):
    """Constant annual net migration over [y0, y1) that brings `group` to `target`."""
    a = load("assumptions")["migration"]

    def run(m: float, tally: dict | None = None) -> Group:
        g = _copy(group)
        for y in range(y0, y1):
            kids = a["child_share_unassisted"] if m > 0 else 0.0  # departures are adults
            prof = cohort.migrant_profile(m, male_share(stream, y), kids)
            res = cohort.step(g, rates_fn(y), prof)
            if tally is not None:
                tally["births"] += res["births"]
                tally["deaths"] += res["deaths"]
        return g

    m0, m1 = 0.0, (target - group.total()) / (y1 - y0)
    f0, f1 = run(m0).total() - target, run(m1).total() - target
    for _ in range(30):
        if abs(f1) < 0.5 or f1 == f0:
            break
        m0, f0, m1 = m1, f1, m1 - f1 * (m1 - m0) / (f1 - f0)
        f1 = run(m1).total() - target
    tally = {"births": 0.0, "deaths": 0.0}
    g = run(m1, tally)
    return m1, g, tally


def california() -> list[dict]:
    ca = load("census")["california"]
    years = ca["years"]
    a = load("assumptions")["migration"]
    plan = [("white", "white", "americas_europe"), ("black", "black", "americas_europe"),
            ("chinese", "white", "chinese"), ("japanese", "white", "japanese")]
    rows = []
    for col, series, stream in plan:
        counts = ca[col]
        g = None
        for i in range(len(years) - 1):
            y0, y1 = years[i], years[i + 1]
            if g is None:
                if counts[i] <= 0:
                    continue
                g = Group(col)
                g.add(*cohort.migrant_profile(counts[i], male_share(stream, y0), a["child_share_unassisted"]))
            m, g, tally = implied_migration(g, lambda y, s=series: cohort.series_rates(s, y), stream, y0, y1, counts[i + 1])
            natural = tally["births"] - tally["deaths"]
            rows.append({"group": col, "decade": f"{y0}-{y1}", "start": counts[i], "end": counts[i + 1],
                         "net_migration_per_year": m, "natural_increase_total": natural,
                         "male_share_end": sum(g.M) / g.total()})
    return rows


# ---------------------------------------------------------------------------
# 3. Native Californians
# ---------------------------------------------------------------------------

def native_californians() -> list[dict]:
    ca = load("census")["california"]
    r = load("rates")["native_californian"]
    rates = Rates(r["floor_e0"], r["tfr"])
    yrs, est = ca["native_estimate_years"], ca["native_estimate"]
    rows = []
    g = cohort.stable_structure(rates, est[0])
    for i in range(len(yrs) - 1):
        y0, y1 = yrs[i], yrs[i + 1]
        g.scale(est[i] / g.total())
        for _ in range(y0, y1):
            cohort.step(g, rates)
        expected = g.total()
        rows.append({"period": f"{y0}-{y1}", "start": est[i], "end_estimate": est[i + 1],
                     "end_at_worst_lifetable": expected, "excess_loss": expected - est[i + 1]})
    return rows


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

def fmt(x: float) -> str:
    return f"{x:,.0f}"


def main() -> int:
    OUT.mkdir(exist_ok=True)
    cal = calibrate_native_hawaiian()
    ch = cal["chosen"]
    with open(OUT / "native_hawaiian_calibration.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["tfr", "e0", "rmse_log", "under15_1866", "under15_1872", "passes_under15", "e0_below_honolulu"])
        for r in cal["family"]:
            w.writerow([r["tfr"], r["e0"], f"{r['rmse_log']:.4f}", f"{r['u15_1866']:.3f}", f"{r['u15_1872']:.3f}",
                        r["passes_u15"], r["below_honolulu_e0"]])
    ca_rows = california()
    nc = native_californians()

    L = ["# Population model: validation against our timeline", "",
         "Generated by `population/historical.py`. Inputs and sources: `population/data/`.", "",
         "## 1. Native Hawaiians, 1853–1896 (no migration)", "",
         f"Calibrated rates: **e0 {ch['e0']:.1f} years, TFR {ch['tfr']:.2f}** "
         f"(root-mean-square error {100 * ch['rmse_log']:.1f}% across six censuses). "
         + ("This pair also passes the independent tests below." if cal["any_pass"] else
            "**No pair passed the independent tests; the best-fitting pair is shown.**"), "",
         "| Census | Observed | Model |", "|---|---|---|"]
    for y, v in cal["obs"].items():
        L.append(f"| {y} | {fmt(v)} | {fmt(ch['fit'][y])} |")
    b = cal["bounds"]
    L += ["", "Independent tests of the calibrated pair:",
          f"- Share under 15 in 1866: model {100 * ch['u15_1866']:.1f}%, census bounds {100 * b[1866][0]:.1f}–{100 * b[1866][1]:.1f}%.",
          f"- Share under 15 in 1872: model {100 * ch['u15_1872']:.1f}%, census bounds {100 * b[1872][0]:.1f}–{100 * b[1872][1]:.1f}%.",
          f"- e0 {ch['e0']:.1f} is {'below' if ch['below_honolulu_e0'] else 'ABOVE'} Honolulu's whole-population 36.5 years (1884), as Hawaiian mortality should be.",
          "",
          "The census decline fixes a family of (e0, TFR) pairs (TFR 2.5 with e0 37 fits it as well as TFR 5.25 with e0 19); "
          "the age structure picks among them. It picks the corner: e0 at the floor of the West tables. Either Hawaiian "
          "mortality really was that severe on average, or the stable-population starting assumption is wrong (the 1848–49 "
          "measles and 1853 smallpox epidemics distorted the age structure). Treat this pair as the best available, weakly "
          "identified. Full family: `outputs/native_hawaiian_calibration.csv`.",
          "",
          "## 2. California by census group: implied net migration", "",
          "Each group is projected from one census to the next with its vital rates; the constant annual net "
          "migration that reproduces the next census is solved for. The engine closes exactly by construction; "
          "the result is historical net migration, which the canon run compares with the People sheet.", "",
          "| Group | Decade | Start | End | Net migration / year | Natural increase (decade) | Male share at end |",
          "|---|---|---|---|---|---|---|"]
    for r in ca_rows:
        L.append(f"| {r['group']} | {r['decade']} | {fmt(r['start'])} | {fmt(r['end'])} | {fmt(r['net_migration_per_year'])} "
                 f"| {fmt(r['natural_increase_total'])} | {100 * r['male_share_end']:.0f}% |")
    L += ["", "Natural increase counts births minus deaths in the run; departures are adults. Migrant sex shares for our timeline are MODEL "
          "(`[migration_otl]` in assumptions.toml). Chinese, Japanese and Black residents use the white or Black national series (no group-specific rates in this version). "
          "Indians enumerated by the census are not projected: coverage changed between censuses (only Indians \"taxed\" before 1890).", "",
          "## 3. Native Californians, 1848–1900", "",
          "Estimated population against what the worst West life table (e0 about 19, TFR 4.0) would leave. "
          "The difference is loss that no ordinary mortality explains: killing, enslavement, starvation and displacement "
          "(Madley 2016). Estimates, not counts; 1853 uses the midpoint of Beale's 75,000–100,000.", "",
          "| Period | Start | At worst life table | Estimate at end | Excess loss |", "|---|---|---|---|---|"]
    for r in nc:
        L.append(f"| {r['period']} | {fmt(r['start'])} | {fmt(r['end_at_worst_lifetable'])} | {fmt(r['end_estimate'])} | {fmt(r['excess_loss'])} |")
    L += ["", "Canon leaves Indigenous claims and obligations OPEN (master storyline, unresolved items 4, 6 and 7); "
          "the canon run therefore shows Native Californians under two labelled bounds, not one answer.", ""]
    (OUT / "historical.md").write_text("\n".join(L), encoding="utf-8")
    print("\n".join(L))
    return 0


if __name__ == "__main__":
    sys.exit(main())
