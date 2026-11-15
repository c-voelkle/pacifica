"""Phase 6, steps 5 and 6: the refugee stream through the workbook, and the packages' sensitivity.

    python3 phase6_sensitivity.py refugees OUT.json
    PHASE6_BASE=VARIANT.xlsx PHASE6_CACHE=DIR python3 phase6_sensitivity.py packages PACKAGES.json TAG OUT.json [--garrisons 1.25]

refugees: cw_refugees at 10,000, 20,000, 33,000 and 50,000 a year in 1863-65, all else at the story minimum: does the
model allow it, and what does it add to receipts, spending, residents and real GDP?

packages: rerun each package's values (from phase6_packages.py) on a variant base, the adverse case of one
uncertain fixed input:
  heads   every 1867 join's residents x 0.75 (base built from population/data/joins_cr059_068.toml scaled);
  gold    interior gold and silver output (Resources C) x 0.75 in 1863-72;
  garrisons (--garrisons F on the normal base) E07, E08 and the 1865-67 garrisons above the head counts x F.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import phase6_solver as S


def refugees(out: Path) -> None:
    base = S.run({})
    res = {}
    for n in (10000, 20000, 33000, 50000):
        r = S.run({"cw_refugees": n})
        a, b = r["story"]["series"], base["story"]["series"]
        res[str(n)] = {
            "allows": S.allows(r), "story_problems": r["story"]["problems_total"],
            "stress_problems": r["stress"]["problems_total"],
            "receipts_1863_1885": sum(a["receipts"][str(y)] - b["receipts"][str(y)] for y in range(1863, 1886)),
            "spending_1863_1885": sum(a["spending"][str(y)] - b["spending"][str(y)] for y in range(1863, 1886)),
            "residents_1866": a["residents"]["1866"] - b["residents"]["1866"],
            "residents_1900": a["residents"]["1900"] - b["residents"]["1900"],
            "real_gdp_1900_pct": 100 * (a["real_gdp"]["1900"] / b["real_gdp"]["1900"] - 1),
            "stress_room_1863": S.room(r["stress"], 1863)["room"], "stress_room_1864": S.room(r["stress"], 1864)["room"],
        }
        print(n, res[str(n)], flush=True)
    out.write_text(json.dumps(res, indent=1))


def packages(pk: Path, tag: str, out: Path, garrisons: float | None) -> None:
    pkgs = json.loads(pk.read_text())
    res = json.loads(out.read_text()) if out.exists() else {}
    base = S.run({})
    for k, p in pkgs.items():
        ov = dict(p["values"])
        if garrisons:
            ov["cw_war61"] = 6.0 * garrisons
            ov["cw_occ6264"] = 5.0 * garrisons
            ov["cw_occ6567"] = ov.get("cw_occ6567", 0.0) * garrisons
        r = S.run(ov)
        res.setdefault(tag, {})[k] = {
            "allows": S.allows(r), "strict": S.allows(r) and S.allows_war(r, base),
            "story_problems": r["story"]["problems_total"],
            "stress_problems": r["stress"]["problems_total"],
            "new_failures_vs_variant_base": S.first_failure(r, base) or "none",
            "stress_room_1863": round(S.room(r["stress"], 1863)["room"], 2),
            "stress_room_1867": round(S.room(r["stress"], 1867)["room"], 2),
        }
        print(tag, k, res[tag][k], flush=True)
        out.write_text(json.dumps(res, indent=1))
    res.setdefault(tag, {})["variant_base"] = {"story_problems": base["story"]["problems_total"],
                                               "stress_problems": base["stress"]["problems_total"]}
    out.write_text(json.dumps(res, indent=1))


if __name__ == "__main__":
    if sys.argv[1] == "refugees":
        refugees(Path(sys.argv[2]))
    else:
        g = float(sys.argv[sys.argv.index("--garrisons") + 1]) if "--garrisons" in sys.argv else None
        packages(Path(sys.argv[2]), sys.argv[3], Path(sys.argv[4]), g)
