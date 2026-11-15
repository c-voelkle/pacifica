"""Phase 6, steps 3 and 4: the price of each lever per $1m, and the instalment split against 1867.

    python3 phase6_price.py OUT.json

Price: each spending lever is raised from its story minimum by $1m in all (spread evenly over its years;
for a lever that is already a total, by $1m), and the run is compared with the story-minimum run, in the
Story case:
  - the Reserve Fund: its lowest difference over 1861-67, and the difference at the end of 1867;
  - the public debt: the largest difference in 1861-1900;
  - the development stock and real GDP (1913 $m) at the end of 1900 and of 1932;
  - interest received on loans abroad, summed 1862-1900 (what a credit brings back).
Instalment split: cw_inst_opt 1, 2 and 3 (CR-062 M2), with the room in 1867 in both cases.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import phase6_ceilings as C
import phase6_solver as S

YEARS = {  # number of years each per-year lever runs (Events B..C)
    "cw_mission": 4, "cw_occ6264": 3, "cw_occ6567": 3, "cw_hon_batt": 2, "cw_hon_turret": 2,
    "cw_sitka_gar": 34, "cw_sitka_mail": 34, "cw_ann_nw": 20, "cw_ann_gb": 20, "cw_ann_sw": 20,
    "cw_juarez": 2, "cw_or_works": 8, "cw_legion_pay": 5,
}
TOTALS = {"richmond", "cw_war61", "cw_scrip_face", "cw_union_prop", "cw_keep64", "cw_priv1867"}


def diff(a: dict, b: dict, k: str, y: int) -> float:
    return (a["series"][k][str(y)] or 0) - (b["series"][k][str(y)] or 0)


def price(lid: str, base: dict) -> dict:
    floor = C.SPEC[lid][2]
    step = 1.0 if lid in TOTALS else 1.0 / YEARS[lid]
    r = S.run(C.ov(lid, floor + step))
    a, b = r["story"], base["story"]
    rf = [diff(a, b, "reserve_fund", y) for y in range(1861, 1868)]
    debt = [diff(a, b, "public_debt", y) for y in range(1861, 1901)]
    out = {
        "step": step, "allows": S.allows(r),
        "reserve_fund_lowest_1861_67": min(rf), "reserve_fund_1867": rf[-1],
        "public_debt_largest_1861_1900": max(debt, key=abs),
        "dev_stock_1900": diff(a, b, "dev_stock", 1900), "dev_stock_1932": diff(a, b, "dev_stock", 1932),
        "real_gdp_1900": diff(a, b, "real_gdp", 1900), "real_gdp_1932": diff(a, b, "real_gdp", 1932),
        "real_gdp_1900_pct": 100 * diff(a, b, "real_gdp", 1900) / b["series"]["real_gdp"]["1900"],
        "real_gdp_1932_pct": 100 * diff(a, b, "real_gdp", 1932) / b["series"]["real_gdp"]["1932"],
        "interest_received_1862_1900": sum(diff(a, b, "interest_received", y) for y in range(1862, 1901)),
    }
    return {k: (round(v, 4) if isinstance(v, float) else v) for k, v in out.items()}


def main() -> None:
    out = Path(sys.argv[1])
    res = json.loads(out.read_text()) if out.exists() else {"price": {}, "instalments": {}}
    base = S.run({})
    for lid in C.SPEC:
        if lid not in res["price"]:
            res["price"][lid] = price(lid, base)
            print(lid, res["price"][lid], flush=True)
            out.write_text(json.dumps(res, indent=1))
    for opt in (1, 2, 3):
        if str(opt) in res["instalments"]:
            continue
        r = S.run({"cw_inst_opt": opt})
        res["instalments"][str(opt)] = {
            "allows": S.allows(r),
            "story_problems": r["story"]["problems_total"], "stress_problems": r["stress"]["problems_total"],
            "story_1867": S.room(r["story"], 1867), "stress_1867": S.room(r["stress"], 1867),
            "stress_1868": S.room(r["stress"], 1868),
            "gold_paid_out_1867": r["story"]["series"]["gold_paid_out"]["1867"],
            "borrowed_1867_story": r["story"]["series"]["borrowed"]["1867"],
            "borrowed_1867_stress": r["stress"]["series"]["borrowed"]["1867"],
        }
        print("instalment option", opt, res["instalments"][str(opt)], flush=True)
        out.write_text(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
