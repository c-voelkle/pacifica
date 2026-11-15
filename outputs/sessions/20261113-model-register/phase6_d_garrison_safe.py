"""Phase 6 follow-up: the largest share of the strengthened D maximum (phase6/d_plus.json) that still passes the
strict rule with garrisons above the head counts x 1.25. Paths are this session's working paths (/home/claude/p7).
"""
import json, sys
sys.path.insert(0, "/home/claude/c-voelkle/pacifica/outputs/sessions/20261113-model-register")
import phase6_packages as P, phase6_solver as S
from phase6_d_strong import FLOORS
dp = json.load(open("/home/claude/p7/d_plus.json"))
base = S.run({}); P.BASE_RUN.update(base)
res = {}
for tag in ("D + lease + refugees 20,000, growth first", "D + lease + refugees 33,000, growth first"):
    mx = dp[tag]["values"]
    def mk(f, garr):
        ov = dict(mx)
        for k, fl in FLOORS.items():
            ov[k] = round(fl + f * (mx[k] - fl), 3)
        if garr:
            ov.update(cw_war61=7.5, cw_occ6264=6.25, cw_occ6567=ov["cw_occ6567"] * 1.25)
        return ov
    lo, hi = 0.5, 0.75
    while hi - lo > 0.01:
        mid = (lo + hi) / 2
        if P.ok_rule(S.run(mk(mid, True))): lo = mid
        else: hi = mid
    r = S.run(mk(lo, False))
    res[tag] = {"garrison_safe_fraction": round(lo, 3), "values": mk(lo, False),
                "margin_1932": round(r["stress"]["series"]["private_margin"]["1932"], 2),
                "room": {str(y): round(S.room(r["stress"], y)["room"], 2) for y in range(1862, 1868)}}
    print(tag, res[tag], flush=True)
json.dump(res, open("/home/claude/p7/garr_frac.json", "w"), indent=1)
