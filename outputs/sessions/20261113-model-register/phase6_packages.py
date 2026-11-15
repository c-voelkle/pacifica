"""Phase 6, step 2: the four packages.

    python3 phase6_packages.py CEILINGS.json OUT.json

The levers compete for the same gold in the same years, so the single ceilings (phase6_ceilings.py) cannot
all be taken at once. Each package fixes a rule and solves for the largest values that the model allows
(phase6_solver.allows). Every package starts from the story minimum and, in all four:
  - cw_scrip_face at 3.2 (the source's ceiling; bought at 0.6 of face and credited at face, it pays for itself);
  - the canon values of E07 and E08, the mission's pay ($0.1m, author), Union property and the garrisons' keep at 0,
    and the Legion off (deferred by the author).

A  Creditor first: the Richmond credit as large as the model allows; the rest at story minimum.
B  Fleet and garrisons first: the Honolulu batteries and slip, the 1865-67 garrisons and Sitka at the same
   fraction of their single ceilings, as large as allowed; then the Richmond credit sized to what is left.
C  Balanced: every package lever at the same fraction of the way from its story minimum to its ceiling.
D  Self-financing (author's D4-D10): the regional receipts at MODEL estimates (D4) with each region's annuities
   equal to its receipts; the refugees at 20,000 a year in 1863-65 (D7); option (b), $3m lending, scrip set off (D8);
   then the other levers at the same fraction of their ceilings, as large as allowed (the Oregon works after 1867,
   D9; L17 already on, D10).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import phase6_ceilings as C
import phase6_solver as S

COMMON = {"cw_scrip_face": 3.2}
CAPS = {"cw_priv1867": 5.0, "cw_scrip_face": 3.2}  # D8 range; the source's ceiling
GROUP_FLEET = ["cw_hon_batt", "cw_hon_turret", "cw_occ6567", "cw_sitka_gar", "cw_sitka_mail"]
BALANCED = ["richmond", "cw_hon_batt", "cw_hon_turret", "cw_occ6567", "cw_sitka_gar", "cw_sitka_mail",
            "cw_ann_nw", "cw_ann_gb", "cw_ann_sw", "cw_juarez", "cw_or_works", "cw_priv1867"]
# D4 regional receipts, MODEL ($m a year; see the phase 6 note for the derivation)
RECEIPTS = {"cw_rc_or": 0.45, "cw_washoe": 0.15, "cw_rc_sw": 0.30, "cw_rc_gb": 0.05}
SELF_FIN = {**RECEIPTS, "cw_ann_nw": 0.45, "cw_ann_gb": 0.20, "cw_ann_sw": 0.30, "cw_refugees": 20000,
            "cw_inst_opt": 2, "cw_priv1867": 3.0}
SELF_REST = ["richmond", "cw_hon_batt", "cw_hon_turret", "cw_occ6567", "cw_sitka_gar", "cw_sitka_mail",
             "cw_juarez", "cw_or_works"]


def top(lid: str, ceil: dict) -> float:
    c = ceil[lid]["ceiling"]
    if c is None:
        c = C.SPEC[lid][4]
    return min(c, CAPS.get(lid, c))


def values(levers: list[str], f: float, ceil: dict) -> dict:
    out = {}
    for lid in levers:
        floor = C.SPEC[lid][2]
        out.update(C.ov(lid, floor + f * (top(lid, ceil) - floor)))
    return out


BASE_RUN: dict = {}


def ok_rule(r: dict) -> bool:
    """The packages' rule: the author's (Story 0, Stress <= 17) and no Stress year-check up to 1900 that failed
    nowhere before (the war years may not spend a check cured elsewhere, author 14 Nov, open point 3)."""
    return S.allows(r) and S.allows_war(r, BASE_RUN)


def solve(make, lo: float = 0.0, hi: float = 1.0, tol: float = 0.005, log=print):
    """Largest f in [lo, hi] for which make(f) is allowed (make(lo) must be)."""
    r = S.run(make(lo))
    assert ok_rule(r), "the package's starting point fails"
    best, rbest = lo, r
    r = S.run(make(hi))
    if ok_rule(r):
        return hi, r
    while hi - lo > tol:
        mid = (lo + hi) / 2
        r = S.run(make(mid))
        ok = ok_rule(r)
        log(f"    f={mid:.4f}: {'ok' if ok else 'fails'}")
        if ok:
            lo, best, rbest = mid, mid, r
        else:
            hi = mid
    return best, rbest


def describe(name: str, ov: dict, f, r: dict, base: dict) -> dict:
    rooms = {str(y): {c: round(S.room(r[c], y)["room"], 2) for c in ("story", "stress")} for y in range(1861, 1873)}
    return {"package": name, "fraction": f, "values": {k: round(v, 4) for k, v in ov.items()},
            "story_problems": r["story"]["problems_total"], "stress_problems": r["stress"]["problems_total"],
            "rule_strict": ok_rule(r), "stress_failing": r["stress"]["failing"], "new_failures_vs_base": S.first_failure(r, base) or "none",
            "room_after": rooms,
            "debt_peak_story": max(r["story"]["series"]["public_debt"][str(y)] for y in range(1861, 1873)),
            "debt_peak_stress": max(r["stress"]["series"]["public_debt"][str(y)] for y in range(1861, 1873)),
            "rf_1872_story": r["story"]["series"]["reserve_fund"]["1872"],
            "real_gdp_1932_story": r["story"]["series"]["real_gdp"]["1932"]}


def main() -> None:
    ceil = json.loads(Path(sys.argv[1]).read_text())
    out = Path(sys.argv[2])
    res = json.loads(out.read_text()) if out.exists() else {}
    base = S.run({})
    BASE_RUN.update(base)

    if "A" not in res:
        mk = lambda f: {**COMMON, **values(["richmond"], f, ceil)}
        f, r = solve(lambda f: mk(f), 0.0, 1.5)
        res["A"] = describe("Creditor first", mk(f), f, r, base)
        out.write_text(json.dumps(res, indent=1)); print("A", res["A"]["values"], flush=True)

    if "B" not in res:
        mk1 = lambda f: {**COMMON, **values(GROUP_FLEET, f, ceil)}
        f1, _ = solve(mk1, 0.0, 1.0)
        fleet = mk1(f1)
        mk2 = lambda g: {**fleet, **values(["richmond"], g, ceil)}
        f2, r = solve(mk2, 0.0, 1.0)
        res["B"] = describe("Fleet and garrisons first", mk2(f2), {"fleet": f1, "credit": f2}, r, base)
        out.write_text(json.dumps(res, indent=1)); print("B", res["B"]["values"], flush=True)

    if "C" not in res:
        mk = lambda f: {**COMMON, **values(BALANCED, f, ceil)}
        f, r = solve(mk, 0.0, 1.0)
        res["C"] = describe("Balanced", mk(f), f, r, base)
        out.write_text(json.dumps(res, indent=1)); print("C", res["C"]["values"], flush=True)

    if "D" not in res:
        mk = lambda f: {**COMMON, **SELF_FIN, **values(SELF_REST, f, ceil)}
        f, r = solve(mk, 0.0, 1.0)
        res["D"] = describe("Self-financing", mk(f), f, r, base)
        out.write_text(json.dumps(res, indent=1)); print("D", res["D"]["values"], flush=True)


if __name__ == "__main__":
    main()
