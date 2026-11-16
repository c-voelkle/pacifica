"""The counties of 1887 as far as CR-071 Part I has drawn them: people, counts and checks.

    python3 population/map_1887.py   -> outputs/map_1887.md

Reads data/counties/map_1887.toml, the historical baseline and the regional multiples. MODEL.
"""
from __future__ import annotations

import tomllib
from collections import defaultdict
from pathlib import Path

import counties_1887 as base

HERE = Path(__file__).parent
ALLOC = {"California": 43, "Oregon": 14, "Columbia": 14, "Deseret": 10, "New Mexico": 9, "Idaho": 6,  # I-10
         "Arizona": 6, "Washoe": 5, "The Rockies": 5, "Hawaii": 5, "Western Montana": 4, "Baja": 2, "Thalassia": 1}
STATE_UNIT = {"CA": "California", "OR": "Oregon", "WA": "Columbia", "ID": "Idaho", "MT": "Western Montana",
              "NV": "Washoe", "UT": "Deseret", "WY": "Deseret", "NM": "New Mexico", "AZ": "Arizona", "CO": "The Rockies"}


def main():
    cfg = tomllib.load(open(HERE / "data" / "counties" / "regions_1887.toml", "rb"))
    m = tomllib.load(open(HERE / "data" / "counties" / "map_1887.toml", "rb"))["county"]
    _, rows, _ = base.build()
    hist = {f"{r['state']};{r['county']}": r for r in rows}
    total = base.model_1887()["model_total"]
    mult = dict(cfg["multiple"])
    by_unit = defaultdict(float)
    for r in rows:
        by_unit[STATE_UNIT[r["state"]]] += r["pacifica1887"]
    rest = total - sum(cfg["fixed"].values()) - sum(by_unit[u] * k for u, k in mult.items())
    mult["California"] = rest / by_unit["California"]

    used = defaultdict(float)
    out, problems = [], []
    for c in m:
        people = 0.0
        for key, frac in c["parts"].items():
            if key not in hist:
                problems.append(f"{c['name']}: unknown part {key}")
                continue
            h = hist[key]
            people += h["pacifica1887"] * frac * mult[STATE_UNIT[h["state"]]]
            used[key] += frac
        people += 1000 * (c.get("adjust", 0) + c.get("people", 0))
        out.append((c, people))
    for key, f in used.items():
        if f > 1.0001:
            problems.append(f"{key} assigned {f:.2f} times")
    names = [c["name"] for c, _ in out]
    for n in set(names):
        if names.count(n) > 1:
            problems.append(f"name used twice: {n}")

    L = ["# The counties of 1887 as drawn so far (MODEL)\n",
         "Built by `population/map_1887.py` from `data/counties/map_1887.toml`. People in thousands.\n"]
    drawn = defaultdict(list)
    for c, p in out:
        drawn[c["unit"]].append((c, p))
    L.append("| Allocation unit | Allotted (I-10, I-15) | Drawn | People in the drawn counties |")
    L.append("|---|---|---|---|")
    for u, n in ALLOC.items():
        d = drawn.get(u, [])
        L.append(f"| {u} | {n} | {len(d)} | {sum(p for _, p in d) / 1000:,.0f} |")
    L.append(f"| **Total** | {sum(ALLOC.values())} | {len(out)} | {sum(p for _, p in out) / 1000:,.0f} |")
    L.append("")
    L.append("The allocation by old unit is accounting: counties cross the old lines, and counties a unit does not need go to a pool (Deseret one, to New Mexico; Columbia one and Idaho one, western Montana none after Three Forks; Arizona takes the two that were left).\n")
    for u in ALLOC:
        if u not in drawn:
            continue
        L.append(f"## {u}\n")
        L.append("| County | Seat | Made of | People | Status |")
        L.append("|---|---|---|---|---|")
        for c, p in sorted(drawn[u], key=lambda t: -t[1]):
            parts = c.get("note", "") if not c["parts"] else ", ".join((k.split(";")[1] if k.startswith(next(iter(c["parts"])).split(";")[0]) and f == 1 else
                               f"{k.split(';')[1]} ({k.split(';')[0]})" + ("" if f == 1 else f" {f:.0%}"))
                              for k, f in c["parts"].items())
            L.append(f"| {c['name']} | {c['seat']} | {parts} | {p / 1000:,.0f} | {c.get('status', 'proposed')} |")
        L.append("")
    todo = [k for k, r in hist.items() if r["share"] > 0 and used.get(k, 0) < 0.999
            ]
    L.append("## Checks\n")
    L.append("- Problems: " + ("; ".join(problems) if problems else "none") + ".")
    L.append("- Our timeline's counties not fully assigned: " + (", ".join(
        f"{k.split(';')[1]} ({k.split(';')[0]}, {used.get(k, 0):.0%})" for k in sorted(todo)) or "none") + ".")
    (HERE / "outputs" / "map_1887.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L))


if __name__ == "__main__":
    main()
