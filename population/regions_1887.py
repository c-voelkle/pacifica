"""Regional layer for 1887 and the allocation of the 124 counties (CR-071 Part I, steps 2 and 4).

    python3 population/regions_1887.py   -> outputs/regions_1887.md, outputs/regions_1887.csv

Reads the historical baseline (counties_1887.py), the population model's 1887 row and
data/counties/regions_1887.toml. Everything it writes is MODEL.
"""
from __future__ import annotations

import csv
import math
import tomllib
from collections import defaultdict
from pathlib import Path

import counties_1887 as base

HERE = Path(__file__).parent
OUT = HERE / "outputs"
UNIT = {"California": "California", "Oregon": "Oregon", "Columbia": "Columbia", "Idaho": "Idaho",
        "Western Montana": "Western Montana", "Washoe": "Washoe", "Deseret": "Deseret",
        "Deseret (southwest Wyoming)": "Deseret", "New Mexico": "New Mexico",
        "New Mexico (Arizona county)": "Arizona", "The Rockies (Colorado)": "The Rockies"}
ORDER = ["California", "Oregon", "Columbia", "Idaho", "Western Montana", "Washoe", "Deseret",
         "New Mexico", "Arizona", "The Rockies", "Hawaii", "Alaska", "Baja"]
STRAWMAN = {"California": 41, "Oregon": 14, "Columbia": 14, "Idaho": 5, "Western Montana": 4, "Washoe": 5,
            "Deseret": 9, "New Mexico": 9, "Arizona": 6, "The Rockies": 6, "Hawaii": 5, "Alaska": 5, "Baja": 0}


def webster(weights: dict[str, float], seats: int, floor: dict[str, int]) -> dict[str, int]:
    """Sainte-Lague / Webster with a floor per unit."""
    got = dict(floor)
    for _ in range(seats - sum(got.values())):
        k = max(weights, key=lambda u: weights[u] / (2 * got[u] + 1))
        got[k] += 1
    return got


def main():
    cfg = tomllib.load(open(HERE / "data" / "counties" / "regions_1887.toml", "rb"))
    _, rows, _ = base.build()
    m = base.model_1887()
    hist, n_hist = defaultdict(int), defaultdict(int)
    for r in rows:
        if r["share"] > 0:
            hist[UNIT[r["region"]]] += r["pacifica1887"]
            n_hist[UNIT[r["region"]]] += 1
    pop = {u: hist[u] * k for u, k in cfg["multiple"].items()}
    pop.update(cfg["fixed"])
    total = m["model_total"]
    pop["California"] = total - sum(pop.values())
    hist["Hawaii"], hist["Alaska"], hist["Baja"] = 85108, 33426, cfg["baja"]["historical_1887"]
    asian_total = m["chinese"] + m["japanese"] + m["filipino"]
    asian = {u: pop[u] * s for u, s in cfg["asian_share"].items()}
    asian["California"] = asian_total - sum(asian.values())
    area = cfg["area_sqmi"]

    L = []
    A = L.append
    A("# Pacifica in 1887 by old unit, and the 124 counties (MODEL)\n")
    A("Built by `population/regions_1887.py` from `data/counties/regions_1887.toml`. The multiples and Asian shares "
      "are proposals for the author; the allocation in section 2 is for decision.\n")
    A("## 1. Residents at the end of 1887\n")
    A(f"Model total {total:,}; of Chinese, Japanese or Filipino origin {asian_total:,} ({asian_total / total:.0%}).\n")
    A("| Old unit | Our timeline 1887 | Multiple | Pacifica 1887 | Share | Per sq mi | Of Asian origin | Share of unit |")
    A("|---|---|---|---|---|---|---|---|")
    for u in ORDER:
        mult = pop[u] / hist[u]
        A(f"| {u} | {hist[u]:,} | {mult:.2f} | {pop[u]:,.0f} | {pop[u] / total:.1%} | {pop[u] / area[u]:.1f} | {asian[u]:,.0f} | {asian[u] / pop[u]:.0%} |")
    interior = sum(pop[u] for u in ORDER if u not in ("California", "Hawaii", "Alaska", "Baja"))
    hint = sum(hist[u] for u in ORDER if u not in ("California", "Hawaii", "Alaska", "Baja"))
    A("")
    A(f"The acceded mainland units hold {interior:,.0f}, {interior / hint:.2f} times our timeline's {hint:,} "
      f"(V3 was 2.00). California holds {pop['California'] / total:.0%}.\n")

    A("## 2. Allocating the 124\n")
    A("Thalassia, on Kāneʻohe Bay, is one of the 124 and has no senator (K-7); it is counted apart from Hawaii's counties. "
      "San Francisco is one of California's. Three rules for the other 123, "
      "each by Webster's method with at least one county a unit (Hawaii at least four, one for each island group):\n")
    cal_rest = pop["California"]  # includes San Francisco and Thalassia's residents
    w = {u: pop[u] for u in ORDER}
    floor = {u: 1 for u in ORDER}
    floor["Hawaii"] = 4
    rules = {
        "A by people": webster(w, 123, floor),
        "B by the square root of people": webster({u: math.sqrt(v) for u, v in w.items()}, 123, floor),
        "C by the square root of people times area": webster({u: math.sqrt(v * min(area[u], 160000)) for u, v in w.items()}, 123, floor),
    }
    A("| Old unit | Our timeline's counties | Strawman (I2) | " + " | ".join(rules) + " |")
    A("|---|---|---|" + "---|" * len(rules))
    for u in ORDER:
        A(f"| {u} | {n_hist.get(u, '-')} | {STRAWMAN[u]} | " + " | ".join(str(r[u]) for r in rules.values()) + " |")
    A("| Thalassia | - | 1 | " + " | ".join("1" for _ in rules) + " |")
    A("| **Total** | | 124 | " + " | ".join(str(sum(r.values()) + 1) for r in rules.values()) + " |")
    A("")
    A("California's rows include San Francisco. Alaska and the homelands are in these rules only for comparison: "
      "the author decided on 16 November 2026 that neither forms counties in 1887 (CR-071-I-map.md).\n")
    A("| | Strawman | " + " | ".join(n.split()[0] for n in rules) + " |")
    A("|---|---|" + "---|" * len(rules))
    allr = {"Strawman": STRAWMAN, **rules}
    def line(label, f):
        A(f"| {label} | " + " | ".join(f(r) for r in allr.values()) + " |")
    line("California's county senators of 123", lambda r: f"{r['California']} ({r['California'] / 123:.0%})")
    line("People per Californian county", lambda r: f"{pop['California'] / r['California'] / 1000:.0f}k")
    line("People per county, acceded mainland", lambda r: f"{interior / sum(r[u] for u in ORDER if u not in ('California', 'Hawaii', 'Alaska', 'Baja')) / 1000:.0f}k")
    line("Smallest unit's people per county", lambda r: min((f"{pop[u] / r[u] / 1000:.0f}k {u}" for u in ORDER if r[u]), key=lambda s: int(s.split('k')[0])))
    line("Largest county area, sq mi (average in unit)", lambda r: max((f"{area[u] / r[u] / 1000:.0f}k {u}" for u in ORDER if r[u] and u != 'Alaska'), key=lambda s: int(s.split('k')[0])))
    A("")
    (OUT / "regions_1887.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    with open(OUT / "regions_1887.csv", "w", newline="", encoding="utf-8") as f:
        o = csv.writer(f)
        o.writerow(["unit", "history_1887", "pacifica_1887", "asian_origin", "area_sqmi", "strawman"] + list(rules))
        for u in ORDER:
            o.writerow([u, hist[u], round(pop[u]), round(asian[u]), area[u], STRAWMAN[u]] + [r[u] for r in rules.values()])
    print("\n".join(L))


if __name__ == "__main__":
    main()
