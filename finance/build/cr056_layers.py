"""Run the CR-056 workbook in Story and Stress at dyn_mode 0, 1 and 2; write the Layers sheet; test against the story.

    python3 finance/build/cr056_layers.py BUILT.xlsx OUT.xlsx RESULTS.json --recalc PATH_TO_recalc.py

BUILT is cr056_dynamics.py's output (formulas). Each of the six cases is a copy with Levers E4 (case) and
the dyn_mode row set, recalculated in LibreOffice. The indicators and the story tests are written as values
on a new Layers sheet of OUT (saved at Story, dyn_mode 0, then recalculated) and to RESULTS.json for the
workbook note. The story tests compare each case with what the master storyline says, not with US history.
"""
from __future__ import annotations

import argparse
import copy
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import openpyxl

YEARS = (1900, 1913, 1920, 1924, 1929, 1932)
CASES = [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
NAMES = {0: "accounting", 1: "on top", 2: "derived"}


def r(y):
    return y - 1840


def set_case(src, dst, case, mode):
    wb = openpyxl.load_workbook(src)
    L = wb["Levers"]
    rr = next(i for i in range(1, L.max_row + 1) if str(L.cell(i, 2).value).startswith("Dynamic layer: 0 ="))
    L.cell(rr, 3).value = mode
    L.cell(rr, 4).value = mode
    L["E4"].value = case
    wb.save(dst)


def col(ws, header, row_=5):
    for c in range(1, ws.max_column + 1):
        if ws.cell(row_, c).value == header:
            return c
    raise SystemExit(f"{ws.title}: no column {header!r}")


def read(path):
    wv = openpyxl.load_workbook(path, data_only=True)
    E, P, La, D, Pr, K, EL, A, Ch, DC, B = (wv[n] for n in ("Economy", "People", "Labour", "Dynamics", "Prices", "Checks",
                                                          "Energy link", "Atomic", "Champions", "Debt & cash", "Budget"))
    g = lambda ws, c, y: ws.cell(r(y), c).value  # noqa: E731
    dc = {k: col(D, k) for k in ("Average earnings per worker ($)", "Union average earnings ($)", "Hours a week, Pacifica",
                                 "Hours a week, Union", "Electricity per person (kWh)", "Extra farm value added (1913 $m)",
                                 "Extra women in paid work (share of women)", "Points of the gap closed by that demand",
                                 "Points left to prices, money and banks", "C1: output per resident raised by unit drive",
                                 "C4: output per resident raised on the farms", "C5: output per resident raised by women's work",
                                 "Electrical world share raised by (into Champions AF)", "Agriculture's share of output",
                                 "Trend growth per resident, derived (into Economy C)",
                                 "Women in paid work above the Union (share of women)",
                                 "Pacifica's real output below its 1920s trend")}
    pc = {k: col(Pr, k) for k in ("Consumer prices against the Union", "… at Union prices", "Power to homes, Pacifica (cents/kWh)",
                                  "Food against the Union", "Services and rent against the Union", "Power to homes", "A car",
                                  "GDP prices against the Union", "GDP per person against the Union")}
    out = {}
    for y in range(1900, 1933):
        o = {}
        o["core_gdp"] = g(E, 15, y)
        o["real_gdp"] = g(E, 19, y)
        o["gdp_pp_x_us"] = g(E, 18, y)
        union_pp = g(La, 63, y) * 1e6 / (g(La, 50, y) * 1e6)
        o["gdp_pp_x_union"] = g(E, 16, y) / union_pp
        o["union_gdp"] = g(La, 63, y)
        o["residents"] = g(P, 12, y)
        o["jp_origin"] = g(P, 15, y)
        o["cn_origin"] = g(P, 14, y)
        o["cons_pp"] = g(EL, 35, y)
        o["cons_x_us"] = g(EL, 37, y)
        o["cons_x_us_real"] = g(Pr, pc["… at Union prices"], y)
        o["cpi_rel"] = g(Pr, pc["Consumer prices against the Union"], y)
        o["gdp_rel"] = g(Pr, pc["GDP prices against the Union"], y)
        o["pp_union_m"] = g(Pr, pc["GDP per person against the Union"], y)
        o["real_pp"] = g(E, 19, y) / g(E, 2, y)
        o["women_lead"] = g(D, dc["Women in paid work above the Union (share of women)"], y)
        o["gap_trend"] = g(D, dc["Pacifica's real output below its 1920s trend"], y)
        o["earn"] = g(D, dc["Average earnings per worker ($)"], y)
        o["earn_u"] = g(D, dc["Union average earnings ($)"], y)
        o["hours"] = g(D, dc["Hours a week, Pacifica"], y)
        o["hours_u"] = g(D, dc["Hours a week, Union"], y)
        o["power_home"] = g(Pr, pc["Power to homes, Pacifica (cents/kWh)"], y)
        o["food_rel"] = g(Pr, pc["Food against the Union"], y)
        o["serv_rel"] = g(Pr, pc["Services and rent against the Union"], y)
        o["td_power"] = g(Pr, pc["Power to homes"], y)
        o["td_car"] = g(Pr, pc["A car"], y)
        o["farm_extra"] = g(D, dc["Extra farm value added (1913 $m)"], y)
        o["farm_output"] = g(D, dc["Agriculture's share of output"], y) * g(E, 10, y) / g(E, 8, y)
        o["women_pts"] = g(D, dc["Extra women in paid work (share of women)"], y)
        o["c1"] = g(D, dc["C1: output per resident raised by unit drive"], y)
        o["c4"] = g(D, dc["C4: output per resident raised on the farms"], y)
        o["c5"] = g(D, dc["C5: output per resident raised by women's work"], y)
        o["c3_el"] = g(D, dc["Electrical world share raised by (into Champions AF)"], y)
        o["growth"] = g(E, 5, y)
        o["fund_growth"] = g(E, 4, y)
        o["slump_demand"] = g(D, dc["Points of the gap closed by that demand"], y)
        o["slump_money"] = g(D, dc["Points left to prices, money and banks"], y)
        o["kwh_pp"] = g(D, dc["Electricity per person (kWh)"], y)
        o["debt"] = g(DC, 18, y)
        o["debt_gdp"] = g(DC, 22, y)
        o["budget"] = g(B, 26, y)
        o["dev_stock"] = g(DC, 15, y)
        o["champions"] = g(Ch, 42, y)
        o["atomic_share"] = g(A, 28, y)
        o["checks"] = g(K, 19, y)
        o["output_gap"] = 1 - g(E, 7, y)
        out[y] = o
    for y in range(1901, 1933):
        out[y]["real_pp_growth"] = out[y]["real_pp"] / out[y - 1]["real_pp"] - 1
    out[1900]["real_pp_growth"] = None
    out["checks_total"] = sum(out[y]["checks"] or 0 for y in range(1900, 1933)) + sum(
        (K.cell(rr, 19).value or 0) for rr in range(6, r(1900)))
    fails = []
    for rr in range(6, 93):
        if K.cell(rr, 19).value:
            for c in range(2, K.max_column + 1):
                if K.cell(rr, c).value == "Check":
                    fails.append((K.cell(rr, 1).value, K.cell(5, c).value))
    out["fails"] = fails
    return out


def _money_first(o):
    return next((y for y in range(1900, 1933) if o[y]["core_gdp"] >= o[y]["union_gdp"]), None)


# Verdicts: "holds"; "fails" (a sentence of the story no longer fits); "re-sync" (a MODEL figure in the storyline to update).
STORY = [
    # (key, the storyline's words, test(o, base) -> (value_text, verdict))
    ("residents", "\"about 37 million\" in 1932 (§33, MODEL); flag a move above 0.3m",
     lambda o, b: (f"{o[1932]['residents']/1e6:.2f}m ({(o[1932]['residents']-b[1932]['residents'])/1e6:+.2f}m)",
                   "holds" if abs(o[1932]['residents'] - b[1932]['residents']) <= 0.3e6 and 36.5e6 <= o[1932]['residents'] <= 37.5e6 else "re-sync")),
    ("pp_union", "output per person \"about 2.24 times\" in 1929 (§33; Economy R, against US history, as in CR-031); within 10%",
     lambda o, b: (f"{o[1929]['gdp_pp_x_us']:.2f}× (against the modelled Union {o[1929]['pp_union_m']:.2f}× money, "
                   f"{o[1929]['pp_union_m']/o[1929]['gdp_rel']:.2f}× at Union prices)",
                   "holds" if abs(o[1929]['gdp_pp_x_us'] / 2.24 - 1) <= 0.1 else "re-sync")),
    ("union_real", "\"the Union remains larger in real output\" in 1932 (§34; real output at Union GDP prices)",
     lambda o, b: (f"1929 {o[1929]['core_gdp']/o[1929]['union_gdp']/o[1929]['gdp_rel']:.2f}×, "
                   f"1932 {o[1932]['core_gdp']/o[1932]['union_gdp']/o[1932]['gdp_rel']:.2f}×",
                   "holds" if o[1932]['core_gdp'] / o[1932]['union_gdp'] / o[1932]['gdp_rel'] < 1 else "fails")),
    ("money_first", "\"in 1932 money income briefly puts Pacifica alone ahead\" (§34; first year money output ≥ the Union's)",
     lambda o, b: (f"first ahead {_money_first(o)}; 1932 {o[1932]['core_gdp']/o[1932]['union_gdp']:.2f}×",
                   "holds" if _money_first(o) == 1932 else "fails")),
    ("crash", "\"a milder crash than the Union, without escaping collapsing trade\" (Union real GDP 1932/1929 about 0.75)",
     lambda o, b: (f"real GDP 1932/1929 {o[1932]['real_gdp']/o[1929]['real_gdp']:.3f}; per resident {o[1932]['real_pp']/o[1929]['real_pp']:.3f}",
                   "holds" if 0.75 < o[1932]['real_gdp'] / o[1929]['real_gdp'] < 0.99 else "fails")),
    ("champions", "\"a champion has a bad year; the Realm does not\" (champions fall more than money GDP)",
     lambda o, b: (f"champions 1931/1929 {o[1931]['champions']/o[1929]['champions']:.2f}, GDP {o[1931]['core_gdp']/o[1929]['core_gdp']:.2f}, "
                   f"real per resident {o[1931]['real_pp']/o[1929]['real_pp']:.2f}",
                   "holds" if o[1931]['champions'] / o[1929]['champions'] < o[1931]['core_gdp'] / o[1929]['core_gdp'] else "fails")),
    ("better_off", "Pacificans \"visibly better off\" than the Union's citizens (consumption per person × US at Union consumer prices, 1929)",
     lambda o, b: (f"{o[1929]['cons_x_us_real']:.2f}× (money {o[1929]['cons_x_us']:.2f}×)", "holds" if o[1929]['cons_x_us_real'] >= 1.3 else "fails")),
    ("atomic", "the atomic programme at its peak \"0.45 percent of national product, in 1921\" (§33, MODEL)",
     lambda o, b: (f"{o[1921]['atomic_share']*100:.2f}%", "holds" if round(o[1921]['atomic_share'] * 100, 2) == 0.45 else "re-sync")),
    ("kwh", "\"about 2,600 kilowatt-hours a head in 1929\" (the energy workbook reads the accounting case)",
     lambda o, b: (f"{o[1929]['kwh_pp']*b[1929]['residents']/o[1929]['residents']:,.0f} kWh at these residents",
                   "holds" if abs(o[1929]['kwh_pp'] * b[1929]['residents'] / o[1929]['residents'] - 2600) <= 100 else "re-sync")),
    ("budget", "\"Pacifica raises neither tariffs nor taxes; reserves and borrowing fund the response\"",
     lambda o, b: (f"Budget 1932 {o[1932]['budget']:,.0f}, debt/GDP {o[1932]['debt_gdp']*100:.0f}%",
                   "holds" if o[1932]['debt_gdp'] < 0.3 else "strained")),
    ("checks", "the workbook's checks (Story none; Stress 17 accepted)",
     lambda o, b: (f"{o['checks_total']} year-checks fail", "holds" if o["checks_total"] <= b["checks_total"] else "new failures")),
]

ROWS = [
    ("Core GDP ($m)", "core_gdp", "{:,.0f}"), ("Real GDP (1913 $m)", "real_gdp", "{:,.0f}"),
    ("GDP per person × US (current $)", "gdp_pp_x_us", "{:.2f}"), ("GDP per person × the Union, money", "pp_union_m", "{:.2f}"),
    ("GDP prices × the Union", "gdp_rel", "{:.2f}"),
    ("Trend growth per resident (before the slump and talent)", "growth", "{:.2%}"),
    ("Growth of real GDP per resident, actual", "real_pp_growth", "{:.2%}"),
    ("… unit drive (C1, level)", "c1", "{:.1%}"), ("… farms (C4, level)", "c4", "{:.1%}"), ("… women's work (C5, level)", "c5", "{:.1%}"),
    ("… electrical share raised (C3)", "c3_el", "{:.1%}"),
    ("Household consumption per person × US, money", "cons_x_us", "{:.2f}"), ("… at Union prices", "cons_x_us_real", "{:.2f}"),
    ("Consumer prices × the Union", "cpi_rel", "{:.2f}"),
    ("Average earnings ($)", "earn", "{:,.0f}"), ("Union average earnings ($)", "earn_u", "{:,.0f}"),
    ("Hours a week", "hours", "{:.1f}"), ("Hours a week, Union", "hours_u", "{:.1f}"),
    ("Power to homes (cents/kWh)", "power_home", "{:.1f}"), ("… relative to Pacifica's prices (1913 = 1)", "td_power", "{:.2f}"),
    ("A car, relative to Pacifica's prices (1913 = 1)", "td_car", "{:.2f}"), ("Food × the Union", "food_rel", "{:.2f}"),
    ("Services and rent × the Union", "serv_rel", "{:.2f}"),
    ("Farm output (1913 $m)", "farm_output", "{:,.0f}"), ("… extra from pumping and nitrogen", "farm_extra", "{:,.0f}"),
    ("Extra women in paid work, driver (points)", "women_pts", "{:.1%}"),
    ("Women in paid work above the Union (points)", "women_lead", "{:.1%}"),
    ("Residents (m)", "residents", "{:,.0f}"), ("Public debt ($m)", "debt", "{:,.0f}"), ("Budget balance ($m)", "budget", "{:,.0f}"),
    ("Development stock ($m)", "dev_stock", "{:,.0f}"), ("Output below trend (the model's, flat 1930-32)", "output_gap", "{:.1%}"),
    ("Real output below its 1920s trend", "gap_trend", "{:.1%}"),
    ("Slump: points closed by demand", "slump_demand", "{:.1%}"), ("Slump: points left to money and banks", "slump_money", "{:.1%}"),
    ("Checks failing", "checks", "{:.0f}"),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("built")
    ap.add_argument("out")
    ap.add_argument("json")
    ap.add_argument("--recalc", required=True)
    a = ap.parse_args()
    res = {}
    with tempfile.TemporaryDirectory() as td:
        for case, mode in CASES:
            p = Path(td) / f"c{case}m{mode}.xlsx"
            set_case(a.built, p, case, mode)
            subprocess.run([sys.executable, a.recalc, str(p), "300"], check=True, capture_output=True)
            res[(case, mode)] = read(p)
            print(f"case {case} mode {mode}: done")
    tests = {}
    for case in (1, 2):
        b = res[(case, 0)]
        for mode in (0, 1, 2):
            tests[(case, mode)] = [(k, words, *fn(res[(case, mode)], b)) for k, words, fn in STORY]

    wb = openpyxl.load_workbook(a.built)
    if "Layers" in wb.sheetnames:
        del wb["Layers"]
    ws = wb.create_sheet("Layers", index=wb.sheetnames.index("Life") + 1)
    Bg = wb["Budget"]
    ws["A1"].value = "Layers: the accounting model and the two dynamic modes side by side (CR-056; values)"
    ws["A2"].value = ("Written by finance/build/cr056_layers.py from six LibreOffice recalculations of this workbook (Story and Stress × "
                      "dyn_mode 0, 1, 2). Values, not formulas: rebuild to refresh. Mode 0 = the accounting model; 1 = channels on top of "
                      "Paths!L (only Pacifica's lead over the Union's electrification, dyn_vs_us 1); 2 = growth derived from capital and base "
                      "progress from 1900. All MODEL.")
    ws["A3"].value = ("The story tests compare each case with what the master storyline says (not with US history). \"fails\": a sentence "
                      "of the story no longer fits; \"re-sync\": a MODEL figure in the storyline to update.")
    for c, s in (("A1", Bg["A1"]), ("A2", Bg["A2"]), ("A3", Bg["A3"])):
        ws[c]._style = copy.copy(s._style)
    hdr, body, grp = Bg["B5"]._style, Bg["B6"]._style, Bg["B4"]._style
    rr = 5
    for case in (1, 2):
        ws.cell(rr, 1).value = "Story case" if case == 1 else "Stress case"
        ws.cell(rr, 1)._style = copy.copy(grp)
        rr += 1
        ws.cell(rr, 1).value = "Indicator"
        ws.cell(rr, 1)._style = copy.copy(hdr)
        c0 = 2
        for y in YEARS:
            for mode in (0, 1, 2):
                cell = ws.cell(rr, c0)
                cell.value = f"{y} · {NAMES[mode]}"
                cell._style = copy.copy(hdr)
                c0 += 1
        rr += 1
        for lab, key, fmt in ROWS:
            ws.cell(rr, 1).value = lab
            ws.cell(rr, 1)._style = copy.copy(body)
            c0 = 2
            for y in YEARS:
                for mode in (0, 1, 2):
                    v = res[(case, mode)][y].get(key)
                    cell = ws.cell(rr, c0)
                    cell.value = (v / 1e6 if key == "residents" else v) if isinstance(v, (int, float)) else v
                    cell._style = copy.copy(body)
                    cell.number_format = {"{:,.0f}": "#,##0", "{:.2f}": "0.00", "{:.2%}": "0.00%", "{:.1%}": "0.0%",
                                          "{:.1f}": "0.0", "{:.0f}": "0"}[fmt] if key != "residents" else "0.00"
                    c0 += 1
            rr += 1
        rr += 1
        ws.cell(rr, 1).value = "Story tests" + ("" if case == 1 else " (Stress is a stress test; it is not meant to match the story)")
        ws.cell(rr, 1)._style = copy.copy(grp)
        rr += 1
        for c, h in enumerate(["The storyline says", "Accounting (0)", "", "On top (1)", "", "Derived (2)", ""], start=1):
            ws.cell(rr, c).value = h
            ws.cell(rr, c)._style = copy.copy(hdr)
        rr += 1
        for i, (k, words, *_rest) in enumerate(tests[(case, 0)]):
            ws.cell(rr, 1).value = words
            ws.cell(rr, 1)._style = copy.copy(body)
            for mode in (0, 1, 2):
                _, _, val, verdict = tests[(case, mode)][i]
                ws.cell(rr, 2 + 2 * mode).value = val
                ws.cell(rr, 3 + 2 * mode).value = verdict
                for c in (2 + 2 * mode, 3 + 2 * mode):
                    ws.cell(rr, c)._style = copy.copy(body)
            rr += 1
        rr += 2
    ws.column_dimensions["A"].width = 60
    for c in range(2, 2 + 3 * len(YEARS)):
        ws.column_dimensions[openpyxl.utils.get_column_letter(c)].width = 12
    ws.freeze_panes = "B5"
    wb.save(a.out)
    subprocess.run([sys.executable, a.recalc, a.out, "300"], check=True, capture_output=True)
    js = {f"{c}_{m}": {"years": {y: res[(c, m)][y] for y in range(1900, 1933)}, "checks_total": res[(c, m)]["checks_total"],
                       "fails": res[(c, m)]["fails"], "tests": tests[(c, m)]} for c, m in CASES}
    Path(a.json).write_text(json.dumps(js, indent=1, default=str))
    print(f"saved {a.out} and {a.json}")


if __name__ == "__main__":
    main()
