"""Phase 6 follow-up (author, 14 Nov): more people, and Sitka paying for itself early.

    PHASE6_BASE=levers2.xlsx PHASE6_CACHE=DIR python3 phase6_sitka_fix.py OUT.json

levers2.xlsx is the phase 5 build with the new lever cw_alaska_rcpt (E217: the seal islands' lease and Alaska's
customs, 1868-1900). For each scenario: the Stress margin of private saving in 1932 and the Stress count with
Sitka at 0, and the Sitka garrison's ceiling (northern mail at 0) under the packages' strict rule.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import phase6_solver as S

SEAL = 0.3175  # $317,500 a year, the Alaska Commercial Company's lease (Hist., from 1870)
SCENARIOS = {
    "none": {},
    "refugees 20,000": {"cw_refugees": 20000},
    "seal lease": {"cw_alaska_rcpt": SEAL},
    "seal lease + refugees 20,000": {"cw_alaska_rcpt": SEAL, "cw_refugees": 20000},
    "seal lease + refugees 33,000": {"cw_alaska_rcpt": SEAL, "cw_refugees": 33000},
}


def main() -> None:
    out = Path(sys.argv[1])
    res = json.loads(out.read_text()) if out.exists() else {}
    base = S.run({})
    ok = lambda r: S.allows(r) and S.allows_war(r, base)
    for name, ov in SCENARIOS.items():
        if name in res:
            continue
        r0 = S.run(ov)
        info = {"stress_problems": r0["stress"]["problems_total"], "story_problems": r0["story"]["problems_total"],
                "margin_1932_stress": r0["stress"]["series"]["private_margin"]["1932"],
                "residents_1932": r0["story"]["series"]["residents"]["1932"]}
        lo, hi, x = 0.0, None, 1.0
        while x <= 64:
            if ok(S.run({**ov, "cw_sitka_gar": x})):
                lo, x = x, x * 2
            else:
                hi = x
                break
        if hi is not None:
            while hi - lo > 0.02:
                mid = (lo + hi) / 2
                if ok(S.run({**ov, "cw_sitka_gar": mid})):
                    lo = mid
                else:
                    hi = mid
            info["binding"] = S.first_failure(S.run({**ov, "cw_sitka_gar": hi}), base)
        info["sitka_ceiling"] = round(lo, 3)
        res[name] = info
        print(name, info, flush=True)
        out.write_text(json.dumps(res, indent=1, default=str))


if __name__ == "__main__":
    main()
