"""Run the growth engine's comparison: the old design and CR-057, with and without the engine.

    python3 finance/build/cr057_growth_variants.py BUILT.xlsx OUTDIR --recalc PATH_TO_recalc.py [--case story|stress]

BUILT is the workbook from cr057_growth_engine.py. Each variant sets Story (or Stress) lever values
on the Levers sheet, is recalculated in LibreOffice and read back. Writes OUTDIR/variants.csv and
prints a table. MODEL.
"""
from __future__ import annotations

import argparse
import csv
import shutil
import subprocess
from pathlib import Path

import openpyxl

ROW0, FIRST = 6, 1846
L6 = "G6: level from capital per output against the Union's"
YEARS = (1900, 1913, 1920, 1929, 1932)

VARIANTS = [
    ("old, accounting", {"c57_on": 0, "g_on": 0}),
    ("old, engine", {"c57_on": 0, "g_on": 1}),
    ("CR-057, accounting", {"c57_on": 1, "g_on": 0}),
    ("CR-057, engine", {"c57_on": 1, "g_on": 1}),
    ("CR-057, engine, 1913 cover held", {"c57_on": 1, "g_on": 1, "c_glide": 0}),
    ("CR-057, engine, research to 3%", {"c57_on": 1, "g_on": 1}),  # rd path edited below
    ("CR-057, engine, cautious (γ 0.07, no premium)", {"c57_on": 1, "g_on": 1, "g_gamma": 0.07, "g_prem": 0}),
]


def row(y: int) -> int:
    return ROW0 + y - FIRST


def set_levers(wb, vals: dict, col: int) -> None:
    L = wb["Levers"]
    for k, v in vals.items():
        r = int(wb.defined_names[k].attr_text.split("$")[-1])
        L.cell(r, col).value = v


def find_col(ws, header: str) -> str | None:
    for c in range(1, ws.max_column + 1):
        if ws.cell(5, c).value == header:
            return openpyxl.utils.get_column_letter(c)
    return None


def read(path: Path) -> dict:
    wb = openpyxl.load_workbook(path, data_only=True)
    E, G, K, P = wb["Economy"], wb["Growth"], wb["Checks"], wb["People"]
    gc = {h: find_col(G, h) for h in ("G2/G3: TFP lead from research", "… of which open licensing (G3, memo)", "G4: TFP lead from learning",
                                      L6, "Level factor into Economy J",
                                      "Research spending ($m)", "… paid by the state ($m)")}
    out = {}
    for y in YEARS:
        r = row(y)
        s, b = E[f"S{r}"].value, E[f"B{r}"].value
        out[y] = dict(R=E[f"R{r}"].value, T=E[f"T{r}"].value if E["T5"].value else None, S=s, B=b / 1e6, real_pr=s * 1e6 / b,
                      H=E[f"H{r}"].value, D=E[f"D{r}"].value,
                      l2=G[f"{gc['G2/G3: TFP lead from research']}{r}"].value, l3=G[f"{gc['… of which open licensing (G3, memo)']}{r}"].value,
                      l4=G[f"{gc['G4: TFP lead from learning']}{r}"].value,
                      l6=G[f"{gc[L6]}{r}"].value,
                      lvl=G[f"{gc['Level factor into Economy J']}{r}"].value,
                      rd=G[f"{gc['Research spending ($m)']}{r}"].value, rd_pub=G[f"{gc['… paid by the state ($m)']}{r}"].value)
    out["res1932"] = P[f"L{row(1932)}"].value / 1e6 if isinstance(P[f"L{row(1932)}"].value, (int, float)) else None
    out["checks"] = sum((K[f"S{row(y)}"].value or 0) for y in range(1846, 1933) if isinstance(K[f"S{row(y)}"].value, (int, float)))
    # cumulative network premium: product of (1 + D) over years
    cum = 1.0
    for y in range(1847, 1930):
        d = E[f"D{row(y)}"].value
        cum *= 1 + (d if isinstance(d, (int, float)) else 0)
    out["D_cum1929"] = cum - 1
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("built")
    ap.add_argument("outdir")
    ap.add_argument("--recalc", required=True)
    ap.add_argument("--case", default="story")
    ap.add_argument("--only", default="")
    a = ap.parse_args()
    od = Path(a.outdir)
    od.mkdir(parents=True, exist_ok=True)
    col = 3 if a.case == "story" else 4
    rows = []
    for name, vals in VARIANTS:
        if a.only and a.only not in name:
            continue
        wb = openpyxl.load_workbook(a.built)
        set_levers(wb, vals, col)
        if a.case != "story":
            wb["Levers"]["E4"].value = 2
        if "research to 3%" in name:
            G = wb["Growth"]
            from cr057_growth_engine import interp, RD_P  # noqa
            rp = interp({**RD_P, 1900: 0.015, 1913: 0.025, 1929: 0.03})
            for y in range(FIRST, 1933):
                G[f"B{row(y)}"].value = round(rp[y], 5)
        f = od / (name.replace(",", "").replace(" ", "_").replace("(", "").replace(")", "").replace("γ", "g") + ".xlsx")
        wb.save(f)
        res = subprocess.run(["python3", a.recalc, str(f), "300"], capture_output=True, text=True)
        if '"total_errors": 0' not in res.stdout:
            print(name, "RECALC ERRORS", res.stdout[:300])
        v = read(f)
        rows.append((name, v))
        y = 1929
        print(f"{name:48s} R29 {v[y]['R']:.2f} T29 {v[y]['T'] or 0:.2f} realGDP29 {v[y]['S']:,.0f} res29 {v[y]['B']:.1f}m "
              f"real/res {v[y]['real_pr']:,.0f} H {v[y]['H']:.2f} l2 {v[y]['l2']:.3f} l4 {v[y]['l4']:.3f} l6 {v[y]['l6']:.3f} "
              f"Dcum {v['D_cum1929']:.3f} res32 {v['res1932'] or 0:.1f} checks {v['checks']}")
    with open(od / "variants.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["variant", "year", "R", "T", "real_gdp", "residents_m", "real_per_resident", "price", "D", "l2", "l3", "l4", "l6",
                    "lvl", "rd", "rd_pub", "res1932", "checks", "D_cum1929"])
        for name, v in rows:
            for y in YEARS:
                d = v[y]
                w.writerow([name, y, d["R"], d["T"], d["S"], d["B"], d["real_pr"], d["H"], d["D"], d["l2"], d["l3"], d["l4"], d["l6"],
                            d["lvl"], d["rd"], d["rd_pub"], v["res1932"], v["checks"], v["D_cum1929"]])


if __name__ == "__main__":
    main()
