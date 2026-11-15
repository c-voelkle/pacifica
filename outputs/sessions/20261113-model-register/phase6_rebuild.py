"""Phase 6: rebuild each package cleanly from the phase 4 workbook and evaluate it.

    python3 phase6_rebuild.py PACKAGES.json OUTDIR

For each package: write its lever values to OUTDIR/package_<K>.json, run finance/build/cr059_068_levers.py with
--values on the phase 4 workbook, recalculate both cases with evaluate.py, and confirm the "allows" rule
(Story 0, Stress <= 17) and that the results equal the solver's.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
P4 = HERE / "phase4" / "Pacifica_financial_model_cr059-068_fixed-only.xlsx"


def main() -> None:
    pk = json.loads(Path(sys.argv[1]).read_text())
    out = Path(sys.argv[2])
    out.mkdir(parents=True, exist_ok=True)
    summary = {}
    for k, p in pk.items():
        vals = {n: v for n, v in p["values"].items()}
        vf = out / f"package_{k}.json"
        vf.write_text(json.dumps(vals, indent=1))
        wb = out / f"package_{k}.xlsx"
        subprocess.run([sys.executable, str(ROOT / "finance/build/cr059_068_levers.py"), str(P4), str(wb), "--values", str(vf)],
                       check=True, capture_output=True)
        subprocess.run([sys.executable, str(HERE / "evaluate.py"), str(wb), str(out), "--tag", f"package_{k}"],
                       check=True, capture_output=True)
        st = json.loads((out / f"package_{k}_story.json").read_text())
        ss = json.loads((out / f"package_{k}_stress.json").read_text())
        ok = st["problems_total"] == 0 and ss["problems_total"] <= 17 and not st["recalc"]["total_errors"] and not ss["recalc"]["total_errors"]
        same = (st["problems_total"] == p["story_problems"] and ss["problems_total"] == p["stress_problems"])
        summary[k] = {"story": st["problems_total"], "stress": ss["problems_total"], "allows": ok,
                      "matches_solver": same, "formula_errors": [st["recalc"]["total_errors"], ss["recalc"]["total_errors"]]}
        print(k, summary[k], flush=True)
    (out / "rebuild_summary.json").write_text(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
