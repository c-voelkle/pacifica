"""Rebuild the financial workbook's chain and iterate it with the energy workbook to a fixed point.

    python3 finance/build/cr057_rebuild_pair.py WORKDIR --recalc PATH_TO_recalc.py [--passes 6] [--tol 1e-6]

Chain (each pass): energy export -> CR-052 link (on the CR-050 workbook, commit 04155c7) -> CR-051/054/055 ->
CR-056 dynamic layer -> CR-057 (c_glide 0: the 1913 cover held, author's decision 2 of 6 Nov 2026) -> the growth
engine -> LibreOffice -> extract -> energy workbook -> LibreOffice -> export. Stops when the energy outputs move by
less than --tol (relative). The last pass also runs cr056_layers.py (the Layers sheet) on the CR-056 build and
carries its sheet into the final workbook. Writes the two workbooks in place in the repository.
"""
from __future__ import annotations

import argparse
import csv
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
FIN = REPO / "finance"
EN = REPO / "energy"
B = FIN / "build"
EB = EN / "build"


def run(*args: str) -> str:
    res = subprocess.run([sys.executable, *args], capture_output=True, text=True, cwd=REPO)
    if res.returncode != 0:
        raise SystemExit(f"failed: {' '.join(args)}\n{res.stdout[-2000:]}\n{res.stderr[-2000:]}")
    return res.stdout


def recalc(rc: str, f: Path) -> None:
    out = subprocess.run([sys.executable, rc, str(f), "300"], capture_output=True, text=True).stdout
    if '"total_errors": 0' not in out:
        raise SystemExit(f"recalc errors in {f}: {out[:600]}")


def read_csv(p: Path) -> dict:
    rows = list(csv.reader(l for l in p.read_text().splitlines() if not l.startswith("#")))
    head, body = rows[0], rows[1:]
    return {h: [float(r[i]) if r[i] not in ("",) else 0.0 for r in body] for i, h in enumerate(head) if h != "year"}


def max_rel(a: dict, b: dict) -> float:
    m = 0.0
    for k in a:
        for x, y in zip(a[k], b.get(k, a[k])):
            m = max(m, abs(x - y) / max(1.0, abs(y)))
    return m


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("workdir")
    ap.add_argument("--recalc", required=True)
    ap.add_argument("--passes", type=int, default=6)
    ap.add_argument("--tol", type=float, default=1e-6)
    a = ap.parse_args()
    W = Path(a.workdir)
    W.mkdir(parents=True, exist_ok=True)
    cr050 = W / "CR-050.xlsx"
    with open(cr050, "wb") as fh:
        fh.write(subprocess.run(["git", "show", "04155c7:finance/Pacifica_financial_model_1846-1932.xlsx"], cwd=REPO,
                                capture_output=True, check=True).stdout)
    eo = EB / "energy_outputs.csv"
    for p in range(1, a.passes + 1):
        before = read_csv(eo)
        run(str(B / "cr052_energy_link.py"), str(cr050), str(eo), str(W / "CR-052.xlsx"))
        run(str(B / "cr051_054_055_champions.py"), str(W / "CR-052.xlsx"), str(eo), str(W / "CR-051.xlsx"))
        run(str(B / "cr056_dynamics.py"), str(W / "CR-051.xlsx"), str(eo), str(W / "CR-056.xlsx"))
        run(str(B / "cr057_economic_order.py"), str(W / "CR-056.xlsx"), str(W / "CR-057.xlsx"), "--set", "c_glide=0,0")
        final = W / "final.xlsx"
        run(str(B / "cr057_growth_engine.py"), str(W / "CR-057.xlsx"), str(final))
        recalc(a.recalc, final)
        run(str(EB / "extract_finance.py"), str(final), str(EB / "finance_inputs.csv"), "--recalc", a.recalc)
        run(str(EB / "build_energy_workbook.py"), str(EB / "finance_inputs.csv"), str(EN / "Pacifica_energy_model_1846-1932.xlsx"))
        recalc(a.recalc, EN / "Pacifica_energy_model_1846-1932.xlsx")
        run(str(EB / "export_energy.py"), str(EN / "Pacifica_energy_model_1846-1932.xlsx"), str(eo), "--recalc", a.recalc)
        d = max_rel(read_csv(eo), before)
        print(f"pass {p}: energy outputs moved by at most {d:.2e} (relative)", flush=True)
        if d < a.tol:
            break
    # the Layers sheet (CR-056's six cases) on the converged CR-056 build, then CR-057 and the engine on top of it
    run(str(B / "cr056_layers.py"), str(W / "CR-056.xlsx"), str(W / "CR-056L.xlsx"), str(W / "cr056_layers.json"), "--recalc", a.recalc)
    run(str(B / "cr057_economic_order.py"), str(W / "CR-056L.xlsx"), str(W / "CR-057L.xlsx"), "--set", "c_glide=0,0")
    run(str(B / "cr057_growth_engine.py"), str(W / "CR-057L.xlsx"), str(final))
    recalc(a.recalc, final)
    shutil.copy(final, FIN / "Pacifica_financial_model_1846-1932.xlsx")
    print("final workbook copied; energy outputs:", eo)


if __name__ == "__main__":
    main()
