"""Phase 6 follow-up (author, 14 Nov): package D made as strong as the model allows.

    PHASE6_BASE=levers2.xlsx PHASE6_CACHE=DIR python3 phase6_d_plus.py OUT.json

Starts from package D (phase6/packages.json) and adds the author's fix: the seal islands' lease (cw_alaska_rcpt,
$0.3175m a year, 1868-1900) and refugees at R a year in 1863-65 (R = 20,000 and 33,000). D's eight spending
levers were held at one shared fraction of their single ceilings (0.53), set by Stress 1863-64. The later ones do
not spend in those years, so each is then raised alone, in story order, as far as the strict rule allows:
Sitka (garrison and mail together), the Oregon works, the 1865-67 garrisons, the Juarez credit; and growth first
(the Oregon works, the Juarez credit, the garrisons, Sitka last). At 33,000 refugees 1863 is over by a little: the
1862-63 Richmond draw is trimmed by the smallest amount that passes. Each step keeps
what the steps before it took.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import phase6_packages as P
import phase6_solver as S

SEAL = 0.3175
PUSH_SITKA_FIRST = [("Sitka garrison and mail", ["cw_sitka_gar", "cw_sitka_mail"], 15.0),
                    ("Oregon works", ["cw_or_works"], 30.0),
                    ("Garrisons 1865-67", ["cw_occ6567"], 20.0),
                    ("Juarez credit", ["cw_juarez"], 30.0)]
# growth first: the Oregon works raise 1932 GDP (+$37m per $1m) and the Juarez credit pays interest back
PUSH_GROWTH_FIRST = [PUSH_SITKA_FIRST[i] for i in (1, 3, 2, 0)]


def summary(r: dict, base: dict) -> dict:
    return {"strict": P.ok_rule(r), "story": r["story"]["problems_total"], "stress": r["stress"]["problems_total"],
            "margin_1932_stress": round(r["stress"]["series"]["private_margin"]["1932"], 2),
            "room_stress": {str(y): round(S.room(r["stress"], y)["room"], 2) for y in range(1861, 1869)},
            "real_gdp_1932_story": round(r["story"]["series"]["real_gdp"]["1932"], 1),
            "residents_1932_story": round(r["story"]["series"]["residents"]["1932"]),
            "first_failure": S.first_failure(r, base) or "none"}


def push(ov: dict, names: list[str], cap: float, tol: float = 0.05) -> tuple[float, str]:
    lo = ov[names[0]]
    trial = lambda x: {**ov, **{n: x for n in names}}
    if P.ok_rule(S.run(trial(cap))):
        return cap, "cap"
    hi = cap
    while hi - lo > tol:
        mid = (lo + hi) / 2
        if P.ok_rule(S.run(trial(mid))):
            lo = mid
        else:
            hi = mid
    return lo, S.first_failure(S.run(trial(hi)), P.BASE_RUN)


def main() -> None:
    out = Path(sys.argv[1])
    res = json.loads(out.read_text()) if out.exists() else {}
    base = S.run({})
    P.BASE_RUN.update(base)
    d = json.loads((Path(__file__).parent / "phase6/packages.json").read_text())["D"]["values"]
    res["D as solved"] = summary(S.run(d), base)
    print("D", res["D as solved"], flush=True)
    runs = [(20000, PUSH_SITKA_FIRST, ""), (20000, PUSH_GROWTH_FIRST, ", growth first"),
            (33000, PUSH_GROWTH_FIRST, ", growth first")]
    for R, PUSH, suffix in runs:
        tag = f"D + lease + refugees {R:,}{suffix}"
        if tag in res and "final" in res[tag]:
            continue
        ov = {**d, "cw_alaska_rcpt": SEAL, "cw_refugees": R}
        entry = {"start": summary(S.run(ov), base), "steps": []}
        print(tag, entry["start"], flush=True)
        if not entry["start"]["strict"]:
            # make room in 1863 by trimming the 1862-63 Richmond draw, the smallest cut that passes
            lo, hi = 0.0, ov["cw_rich_early"]
            while hi - lo > 0.01:
                mid = (lo + hi) / 2
                if P.ok_rule(S.run({**ov, "cw_rich_early": mid})):
                    lo = mid
                else:
                    hi = mid
            entry["steps"].append({"lever": "Richmond draw 1862-63 (trimmed)", "from": ov["cw_rich_early"], "to": round(lo, 3)})
            ov["cw_rich_early"] = round(lo, 3)
            entry["start_trimmed"] = summary(S.run(ov), base)
            print("   ", entry["steps"][-1], flush=True)
        if not P.ok_rule(S.run(ov)):
            res[tag] = entry
            out.write_text(json.dumps(res, indent=1))
            continue
        for label, names, cap in PUSH:
            before = ov[names[0]]
            v, why = push(ov, names, cap)
            ov.update({n: round(v, 3) for n in names})
            entry["steps"].append({"lever": label, "from": before, "to": round(v, 3), "stopped_by": why})
            print("   ", entry["steps"][-1], flush=True)
        entry["values"] = ov
        entry["final"] = summary(S.run(ov), base)
        print("   final", entry["final"], flush=True)
        res[tag] = entry
        out.write_text(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
