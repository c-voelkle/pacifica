"""Phase 6 follow-up: package D at 75% of its strengthened maximum, and how it stands up.

    PHASE6_BASE=levers2.xlsx PHASE6_CACHE=DIR python3 phase6_d_strong.py D_PLUS.json OUT.json

For each growth-first maximum in D_PLUS.json (phase6_d_plus.py), the spending levers are set at their story
minimum plus 0.75 of the way to the maximum; the self-financing parts (receipts, annuities, refugees, the lease,
instalment option, private lending, scrip) are kept. Tests: the strict rule and its margins; garrisons above the
head counts x 1.25 (as in phase6_sensitivity.py). The head-count tolerance is run separately with
phase6_robust.py heads (HEADS_OVERRIDES = the values written here).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import phase6_d_plus as DP
import phase6_packages as P
import phase6_solver as S

FLOORS = {"cw_rich_early": 0.3, "cw_rich_late": 0.9, "cw_hon_batt": 0.0, "cw_hon_turret": 0.0, "cw_occ6567": 0.0,
          "cw_sitka_gar": 0.0, "cw_sitka_mail": 0.0, "cw_juarez": 0.0, "cw_or_works": 0.0}


def main() -> None:
    dp = json.loads(Path(sys.argv[1]).read_text())
    out = Path(sys.argv[2])
    res = {}
    base = S.run({})
    P.BASE_RUN.update(base)
    for tag, e in dp.items():
        if "growth first" not in tag or "values" not in e:
            continue
        mx = e["values"]
        ov = dict(mx)
        for k, f in FLOORS.items():
            ov[k] = round(f + 0.75 * (mx[k] - f), 3)
        r = S.run(ov)
        g = dict(ov, cw_war61=6.0 * 1.25, cw_occ6264=5.0 * 1.25, cw_occ6567=ov["cw_occ6567"] * 1.25)
        rg = S.run(g)
        name = tag.replace("growth first", "75% of maximum")
        res[name] = {"values": ov, "result": DP.summary(r, base),
                     "garrisons_x1.25": {"strict": P.ok_rule(rg), "stress": rg["stress"]["problems_total"],
                                         "first_failure": S.first_failure(rg, base) or "none"}}
        print(name, res[name], flush=True)
        out.write_text(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
