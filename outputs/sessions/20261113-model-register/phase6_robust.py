"""Phase 6, step 6 (continued): how much of each package survives the adverse cases, and the head-count tolerance.

    python3 phase6_robust.py scale PACKAGES.json VARIANT OUT.json        # VARIANT: garrisons | gold (env PHASE6_BASE)
    python3 phase6_robust.py heads OUT.json

scale: for each package, the largest s in [0, 1] such that the package's spending levers at
floor + s x (package value - floor) pass the packages' strict rule on the adverse case. The self-financing
parts (receipts, the annuities matched to them, the refugees, the scrip, the 1867 lending and the instalment
option) stay as they are. garrisons: E07, E08 and the 1865-67 garrisons x 1.25 on the normal base; gold: the
interior-gold base (PHASE6_BASE, interior gold and silver x 0.75 in 1863-72).

heads: (env HEADS_OVERRIDES = lever values as JSON, HEADS_WORK = work folder) the largest shortfall in every 1867 join's residents (joins x k) at which the story-minimum workbook,
rebuilt from the phase 4 build, still passes the author's rule; bisected on k in [0.75, 1.0].
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]

FLOORS = {"cw_rich_early": 0.3, "cw_rich_late": 0.9, "cw_priv1867": 3.0}
FIXED = {"cw_scrip_face", "cw_rc_or", "cw_washoe", "cw_rc_sw", "cw_rc_gb", "cw_refugees", "cw_inst_opt"}
SELF_FIXED = {"cw_ann_nw", "cw_ann_gb", "cw_ann_sw", "cw_priv1867"}  # matched to receipts in D


def scaled(values: dict, s: float, key: str) -> dict:
    out = {}
    for n, v in values.items():
        if n in FIXED or (key == "D" and n in SELF_FIXED):
            out[n] = v
        else:
            f = FLOORS.get(n, 0.0)
            out[n] = f + s * (v - f)
    return out


def scale(pk: Path, variant: str, out: Path) -> None:
    import phase6_solver as S
    pkgs = json.loads(pk.read_text())
    res = json.loads(out.read_text()) if out.exists() else {}
    base = S.run({})
    ok = lambda r: S.allows(r) and S.allows_war(r, base)

    def make(k, s):
        ov = scaled(pkgs[k]["values"], s, k)
        if variant == "garrisons":
            ov["cw_war61"], ov["cw_occ6264"] = 6.0 * 1.25, 5.0 * 1.25
            ov["cw_occ6567"] = ov.get("cw_occ6567", 0.0) * 1.25
        return ov

    for k in pkgs:
        tag = f"{variant}:{k}"
        if tag in res:
            continue
        lo, hi = 0.0, 1.0
        r0 = S.run(make(k, 0.0))
        if not ok(r0):
            res[tag] = {"survives": None, "note": "fails even at the story minimum", "stress": r0["stress"]["problems_total"]}
        elif ok(S.run(make(k, 1.0))):
            res[tag] = {"survives": 1.0}
        else:
            while hi - lo > 0.02:
                mid = (lo + hi) / 2
                if ok(S.run(make(k, mid))):
                    lo = mid
                else:
                    hi = mid
            res[tag] = {"survives": round(lo, 3), "values": {n: round(v, 3) for n, v in make(k, lo).items()}}
        print(tag, res[tag], flush=True)
        out.write_text(json.dumps(res, indent=1))


def heads(out: Path) -> None:
    src = (ROOT / "population/data/joins_cr059_068.toml").read_text()
    ov = json.loads(os.environ.get("HEADS_OVERRIDES", "{}"))
    work = Path(os.environ.get("HEADS_WORK", "/home/claude/p6/heads"))
    work.mkdir(parents=True, exist_ok=True)
    res = {}

    def test(k: float) -> bool:
        tag = f"{k:.4f}"
        jf = work / f"joins_{tag}.toml"
        jf.write_text(re.sub(r"residents = (\d+)", lambda m: f"residents = {round(int(m.group(1)) * k)}", src))
        p4, p5 = work / f"p4_{tag}.xlsx", work / f"p5_{tag}.xlsx"
        subprocess.run([sys.executable, str(ROOT / "finance/build/cr059_068_civil_war.py"),
                        str(ROOT / "finance/Pacifica_financial_model_1846-1932.xlsx"), str(p4), "--joins", str(jf)],
                       check=True, capture_output=True)
        subprocess.run([sys.executable, str(ROOT / "finance/build/cr059_068_levers.py"), str(p4), str(p5)],
                       check=True, capture_output=True)
        env = {**os.environ, "PHASE6_BASE": str(p5), "PHASE6_CACHE": str(work / f"cache_{tag}")}
        txt = subprocess.run([sys.executable, "-c",
                              "import json, os, phase6_solver as S; r = S.run(json.loads(os.environ.get('HEADS_OVERRIDES', '{}'))); "
                              "print(json.dumps([r['story']['problems_total'], r['stress']['problems_total'], S.allows(r)]))"],
                             check=True, capture_output=True, text=True, env=env, cwd=HERE).stdout
        story, stress, ok = json.loads(txt.strip().splitlines()[-1])
        res[tag] = {"story": story, "stress": stress, "allows": ok}
        print(tag, res[tag], flush=True)
        out.write_text(json.dumps(res, indent=1))
        return ok

    lo, hi = 0.75, 1.0
    assert test(hi)
    if test(lo):
        return
    while hi - lo > 0.01:
        mid = round((lo + hi) / 2, 4)
        if test(mid):
            hi = mid
        else:
            lo = mid
    res["tolerance"] = {"passes_at": hi, "fails_at": lo}
    out.write_text(json.dumps(res, indent=1))


if __name__ == "__main__":
    if sys.argv[1] == "scale":
        scale(Path(sys.argv[2]), sys.argv[3], Path(sys.argv[4]))
    else:
        heads(Path(sys.argv[2]))
