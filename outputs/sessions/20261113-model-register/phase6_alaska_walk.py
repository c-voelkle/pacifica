"""Alaskamaxx (author, 14 Nov): what the adopted ideas do to package D strong, one change at a time.

    PHASE6_BASE=levers4.xlsx PHASE6_CACHE=DIR python3 phase6_alaska_walk.py OUT.json

levers4.xlsx is the phase 5 build with the Alaskamaxx levers (finance/build/cr059_068_levers.py). The walk starts
from D strong (20,000 refugees, 73.4%) with the old seal lease of $0.3175m a year to 1900, which reproduces it.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import phase6_packages as P
import phase6_solver as S

HERE = Path(__file__).resolve().parent
OLD_SEAL = 0.3175


def summary(r: dict) -> dict:
    st, ss = r["story"]["series"], r["stress"]["series"]
    return {"strict": P.ok_rule(r), "story_problems": r["story"]["problems_total"],
            "stress_problems": r["stress"]["problems_total"],
            "margin_1932_stress": round(ss["private_margin"]["1932"], 2),
            "margin_1900_stress": round(ss["private_margin"]["1900"], 2),
            "room_stress": {str(y): round(S.room(r["stress"], y)["room"], 2) for y in (1863, 1864, 1865, 1867, 1872)},
            "real_gdp_1900_story": round(st["real_gdp"]["1900"], 1), "real_gdp_1932_story": round(st["real_gdp"]["1932"], 1),
            "residents_1900_story": round(st["residents"]["1900"]), "residents_1932_story": round(st["residents"]["1932"]),
            "receipts_1868_1900_story": round(sum(st["receipts"][str(y)] for y in range(1868, 1901)), 1),
            "spending_1868_1900_story": round(sum(st["spending"][str(y)] for y in range(1868, 1901)), 1),
            "public_debt_1900_story": round(st["public_debt"]["1900"], 1)}


def main() -> None:
    d = json.loads((HERE / "phase6/d_strong_garrison_safe.json").read_text())[
        "D + lease + refugees 20,000, growth first"]["values"]
    ov = {**d, "cw_alaska_rcpt": OLD_SEAL, "cw_seal_1880s": OLD_SEAL, "cw_seal_1890s": OLD_SEAL}
    steps = [("D strong", dict(ov))]
    ov["cw_sitka_taper"] = 0.4
    steps.append(("+ taper from 1873 at 40%", dict(ov)))
    ov.update(cw_seal_1880s=0.5, cw_seal_1890s=0.85, cw_seal_after=0.85)
    steps.append(("+ seals: tendered, herd saved", dict(ov)))
    ov["cw_ak_salmon"] = 1.0
    steps.append(("+ salmon case tax", dict(ov)))
    ov.update(cw_ak_gold_lead=8, cw_ak_seward=1.0)
    steps.append(("+ Juneau 8 years early, Seward Peninsula placers", dict(ov)))
    ov.update(cw_ak_commission=0.15, cw_ak_telegraph=1)
    steps.append(("+ Northern Commission and Bering telegraph (costs)", dict(ov)))
    ov["cw_ak_route"] = 1
    steps.append(("+ Chilkoot compact and early Yukon route (= D strong + Alaska)", dict(ov)))
    base = S.run({})
    P.BASE_RUN.update(base)
    res = {}
    for name, o in steps:
        r = S.run(o)
        res[name] = {"values": o, "result": summary(r), "new_failures": S.first_failure(r, base) or "none"}
        print(name, res[name]["result"], res[name]["new_failures"], flush=True)
    Path(sys.argv[1]).write_text(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
