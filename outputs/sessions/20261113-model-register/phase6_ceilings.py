"""Phase 6, step 1: each spending lever's ceiling on its own, by bisection.

    python3 phase6_ceilings.py OUT.json

For each lever in SPEC, starting from its story minimum (the phase 5 value), find the largest value at which
the model still "allows" it (phase6_solver.allows: Story 0 failed year-checks, Stress at most 17), all other
levers at their story minimum. The search doubles a step until the rule fails, then bisects to TOL. The
check that fails just above the ceiling, and its year, is recorded as the binding check.

Receipts (cw_rc_or, cw_washoe, cw_rc_sw, cw_rc_gb) have no finance ceiling: more always helps. Their bound is
their source. Switches and parameters the author has fixed (cw_inst_opt, cw_nb_credit, cw_ny_share, cw_ny_home,
cw_idle_ratio, cw_scrip_price, cw_hon_frig: 0 by the author's decision of 14 Nov) are not searched here.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import phase6_solver as S

# id: (label, unit, floor, first step, cap, overrides(x))
SPEC = {
    "richmond": ("L01 Richmond credit, total drawn 1862-65 (a quarter in 1862-63, three quarters in 1864-65; D5)",
                 "$m total", 2.4, 8.0, 400.0,
                 lambda x: {"cw_rich_early": x * 0.25 / 2, "cw_rich_late": x * 0.75 / 2}),
    "cw_mission": ("L01 technical mission's pay, per year 1862-65", "$m/yr", 0.1, 2.0, 100.0, None),
    "cw_war61": ("L03 Northwestern campaign above head counts, 1861", "$m", 6.0, 8.0, 400.0, None),
    "cw_occ6264": ("L03 occupation and garrisons above head counts, per year 1862-64", "$m/yr", 5.0, 4.0, 200.0, None),
    "cw_occ6567": ("L03 held-territory garrisons above head counts, per year 1865-67", "$m/yr", 0.0, 4.0, 200.0, None),
    "cw_hon_batt": ("L02 Honolulu batteries, per year 1861-62", "$m/yr", 0.0, 4.0, 200.0, None),
    "cw_hon_turret": ("L02 second turret ship's sections and slip, per year 1863-64", "$m/yr", 0.0, 4.0, 200.0, None),
    "cw_sitka_gar": ("L04 Sitka garrison and squadron, per year from 1867", "$m/yr", 0.0, 1.0, 100.0, None),
    "cw_sitka_mail": ("L04 northern mail, per year from 1867", "$m/yr", 0.0, 1.0, 100.0, None),
    "cw_scrip_face": ("L06 Oregon scrip bought 1865-66, face (price 0.6 of face)", "$m face", 0.0, 3.2, 200.0, None),
    "cw_union_prop": ("F13 Union property at valuation, paid in 1867", "$m", 0.0, 4.0, 200.0, None),
    "cw_keep64": ("F14 keep of the withdrawing garrison, 1864 (set off in 1867)", "$m", 0.0, 4.0, 200.0, None),
    "cw_ann_nw": ("L08a annuities, the Northwest, per year 1862-81", "$m/yr", 0.0, 1.0, 100.0, None),
    "cw_ann_gb": ("L08b annuities, the Great Basin and Rockies, per year 1863-82", "$m/yr", 0.0, 1.0, 100.0, None),
    "cw_ann_sw": ("L08c annuities, the Southwest, per year 1862-81", "$m/yr", 0.0, 1.0, 100.0, None),
    "cw_juarez": ("L09 Juarez credit, per year 1865-66", "$m/yr", 0.0, 4.0, 200.0, None),
    "cw_or_works": ("L10 Oregon works on Development Fund credit, per year 1868-75", "$m/yr", 0.0, 4.0, 200.0, None),
    "cw_priv1867": ("L13 private lending to the Union's bankers, 1867", "$m", 3.0, 4.0, 200.0, None),
    "cw_legion_pay": ("L16 Nauvoo Legion's pay (switched on), per year 1863-67", "$m/yr", 0.15, 2.0, 100.0,
                      lambda x: {"cw_legion_on": 1, "cw_legion_pay": x}),
}


def ov(lid: str, x: float) -> dict:
    f = SPEC[lid][5]
    return f(x) if f else {lid: x}


def tol(x: float) -> float:
    return max(0.02, 0.01 * abs(x))


RULE = "allows"  # or "war" (phase6_solver.allows_war), set by --war


def ceiling(lid: str, base: dict, log) -> dict:
    label, unit, floor, step, cap, _ = SPEC[lid]
    probes = []

    def test(x):
        r = S.run(ov(lid, x))
        ok = S.allows(r) if RULE == "allows" else S.allows_war(r, base)
        probes.append((round(x, 4), ok))
        log(f"  {lid} {x:.4f}: {'ok' if ok else 'FAILS'}  (story {r['story']['problems_total']}, stress {r['stress']['problems_total']})")
        return ok, r

    assert test(floor)[0], f"{lid}: the story minimum fails"
    lo, hi, rhi = floor, None, None
    x = floor + step
    while x <= cap:
        ok, r = test(x)
        if ok:
            lo, step = x, step * 2
            x = floor + step
        else:
            hi, rhi = x, r
            break
    if hi is None:
        return {"label": label, "unit": unit, "floor": floor, "ceiling": None, "note": f"no ceiling below {cap}",
                "probes": probes}
    while hi - lo > tol(lo):
        mid = (lo + hi) / 2
        ok, r = test(mid)
        if ok:
            lo = mid
        else:
            hi, rhi = mid, r
    return {"label": label, "unit": unit, "floor": floor, "ceiling": round(lo, 3), "fails_at": round(hi, 3),
            "binding": S.first_failure(rhi, base), "probes": probes}


def main() -> None:
    global RULE
    args = sys.argv[1:]
    if "--war" in args:
        RULE = "war"
        args.remove("--war")
    out = Path(args[0])
    only = args[1:] or list(SPEC)
    done = json.loads(out.read_text()) if out.exists() else {}
    base = S.run({})
    t0 = time.time()
    for lid in only:
        if lid in done:
            continue
        print(f"{lid}: {SPEC[lid][0]}", flush=True)
        done[lid] = ceiling(lid, base, lambda m: print(m, flush=True))
        d = done[lid]
        print(f"=> {lid} ceiling {d.get('ceiling')} {d['unit']} (floor {d['floor']}); binding: {d.get('binding', d.get('note'))}"
              f"  [{time.time() - t0:.0f}s]", flush=True)
        out.write_text(json.dumps(done, indent=1))


if __name__ == "__main__":
    main()
