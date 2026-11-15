"""Phase 6 solver: run the levers workbook with lever values changed, in both cases, and test the "allows" rule.

    import phase6_solver as S
    res = S.run({"cw_occ6567": 2.0})          # both cases; cached
    S.allows(res)                              # Story 0 failed year-checks and Stress <= 17

The base is the phase 5 workbook as built (finance/build/cr059_068_levers.py, not recalculated), path in
BASE. A run patches the Levers sheet's XML directly (Levers C = Story value, D = Stress value; E4 = case),
recalculates the two copies in parallel with LibreOffice (xlsx skill scripts/recalc.py), and reads:
the problem count (Start!C5), the failing year-checks by year (Checks), and the series used for pricing.
Results are cached by their overrides in CACHE (one JSON per run), so a rerun with the same values is free.

An override value is a number (Story = Stress) or a pair (Story, Stress). Values for computed levers are
refused. The rule "allows" is the author's of 13 November 2026: every Story check passes, and Stress has no
more than 17 failed year-checks (D14 of 14 November: 17 stays the ceiling).
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import openpyxl

RECALC = "/mnt/skills/public/xlsx/scripts/recalc.py"
BASE = Path(os.environ.get("PHASE6_BASE", "/home/claude/p5/levers1.xlsx"))
CACHE = Path(os.environ.get("PHASE6_CACHE", "/home/claude/p6/cache"))
STRESS_CEILING = 17
FIRST = 1846
LEVERS_XML = "xl/worksheets/sheet3.xml"  # the Levers sheet (checked in lever_rows)

# label: sheet, column (year rows 6..92 = 1846..1932)
SERIES = {
    "reserve_fund": ("Debt & cash", "S"), "public_debt": ("Debt & cash", "R"), "borrowed": ("Debt & cash", "G"),
    "dev_stock": ("Debt & cash", "O"), "net_lending": ("Debt & cash", "B"), "real_gdp": ("Economy", "S"),
    "gdp": ("Economy", "O"), "receipts": ("Budget", "M"), "spending": ("Budget", "Y"),
    "gold": ("Gold & money", "F"), "gold_paid_out": ("Gold & money", "E"), "residents": ("People", "L"),
    "interest_received": ("Budget", "H"), "continental_out": ("Loans", "E"),
    "bonds_placed": ("Debt & cash", "Y"), "rf_drawn": ("Debt & cash", "F"),
}
SU_SERIES = {"private_margin": ("Sources & uses", "L"), "idle_source": ("Sources & uses", "R")}  # rows 135..221


def _lever_map() -> dict[str, int]:
    wb = openpyxl.load_workbook(BASE, read_only=True)
    out = {}
    for n, d in wb.defined_names.items():
        if n.startswith("cw_") and d.attr_text.startswith("Levers!$E$"):
            out[n] = int(d.attr_text.split("$")[-1])
    return out


LEVER_ROWS: dict[str, int] = {}
COMPUTED = {"cw_setoffs", "cw_ny_held"}


def lever_rows() -> dict[str, int]:
    if not LEVER_ROWS:
        LEVER_ROWS.update(_lever_map())
        with zipfile.ZipFile(BASE) as z:
            wbx = z.read("xl/workbook.xml").decode()
            rels = z.read("xl/_rels/workbook.xml.rels").decode()
        rid = re.search(r'<sheet [^>]*name="Levers"[^>]*r:id="([^"]+)"', wbx).group(1)
        m = re.search(r'Id="%s"[^>]*Target="([^"]+)"' % rid, rels) or re.search(r'Target="([^"]+)"[^>]*Id="%s"' % rid, rels)
        assert m.group(1).endswith("sheet3.xml"), m.group(1)
    return LEVER_ROWS


def _set_cell(xml: str, ref: str, value: float) -> str:
    pat = re.compile(r'(<c r="%s"[^>]*?)(/>|>(.*?)</c>)' % ref, re.S)
    m = pat.search(xml)
    assert m, ref
    head = re.sub(r'\st="[^"]*"', "", m.group(1)) + ' t="n"'
    return xml[:m.start()] + f"{head}><v>{value!r}</v></c>" + xml[m.end():]


def _write_copy(dst: Path, cells: dict[str, float]) -> None:
    with zipfile.ZipFile(BASE) as zin, zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == LEVERS_XML:
                x = data.decode()
                for ref, v in cells.items():
                    x = _set_cell(x, ref, v)
                data = x.encode()
            zout.writestr(item, data)


def _read(path: Path) -> dict:
    wb = openpyxl.load_workbook(path, data_only=True, read_only=True)
    ck = wb["Checks"]
    rows = list(ck.iter_rows(min_row=5, max_row=92, values_only=True))
    head = rows[0]
    fails, problems = {}, {}
    for r in rows[1:]:
        if not isinstance(r[0], (int, float)):
            continue
        y = int(r[0])
        problems[y] = r[18] or 0
        bad = [str(head[i]) for i, v in enumerate(r) if v == "Check" and i < len(head) and head[i]]
        if bad or (r[18] or 0):
            fails[str(y)] = bad
    series = {}
    for k, (sh, col) in SERIES.items():
        ci = openpyxl.utils.column_index_from_string(col) - 1
        series[k] = {str(int(r[0])): r[ci] for r in wb[sh].iter_rows(min_row=6, max_row=92, values_only=True)
                     if r and isinstance(r[0], (int, float))}
    for k, (sh, col) in SU_SERIES.items():
        ci = openpyxl.utils.column_index_from_string(col) - 1
        series[k] = {str(int(r[0])): r[ci] for r in wb[sh].iter_rows(min_row=135, max_row=221, values_only=True)
                     if r and isinstance(r[0], (int, float))}
    lv = wb["Levers"]
    consts = {"mkt_capacity": lv["E38"].value, "foreign_capacity": lv["E39"].value, "issue_price": lv["E35"].value}
    return {"problems_total": wb["Start"]["C5"].value, "failing": fails, "series": series, "consts": consts}


def _key(overrides: dict) -> str:
    norm = {k: (list(v) if isinstance(v, (tuple, list)) else [v, v]) for k, v in sorted(overrides.items())}
    return hashlib.sha1(json.dumps(norm, sort_keys=True).encode()).hexdigest()[:16], norm


def run(overrides: dict) -> dict:
    """Run both cases with the given lever values; cached."""
    rows = lever_rows()
    key, norm = _key(overrides)
    CACHE.mkdir(parents=True, exist_ok=True)
    cf = CACHE / f"{key}.json"
    if cf.exists():
        return json.loads(cf.read_text())
    cells = {}
    for name, (story, stress) in norm.items():
        if name in COMPUTED or name not in rows:
            raise KeyError(name)
        cells[f"C{rows[name]}"] = float(story)
        cells[f"D{rows[name]}"] = float(stress)
    tmp = Path(tempfile.mkdtemp(prefix="p6-"))

    def one(case: int) -> dict:
        dst = tmp / f"case{case}.xlsx"
        _write_copy(dst, {**cells, "E4": case})
        out = subprocess.run([sys.executable, RECALC, str(dst), "600"], capture_output=True, text=True)
        rc = json.loads(out.stdout[out.stdout.index("{"):])
        d = _read(dst)
        d["formula_errors"] = rc.get("total_errors")
        return d

    with ThreadPoolExecutor(2) as ex:
        story, stress = ex.map(one, (1, 2))
    shutil.rmtree(tmp, ignore_errors=True)
    res = {"overrides": norm, "story": story, "stress": stress}
    cf.write_text(json.dumps(res, default=str))
    return res


def allows(res: dict) -> bool:
    return (res["story"]["problems_total"] == 0 and res["stress"]["problems_total"] <= STRESS_CEILING
            and not res["story"]["formula_errors"] and not res["stress"]["formula_errors"])


def first_failure(res: dict, base: dict) -> str:
    """Name the year-checks that fail in this run and not in the base run."""
    out = []
    for case in ("story", "stress"):
        for y, cols in sorted(res[case]["failing"].items()):
            old = set(base[case]["failing"].get(y, []))
            new = [c for c in cols if c not in old]
            if new:
                out.append(f"{case} {y}: {', '.join(new)}")
    return "; ".join(out)


def room(case_res: dict, year: int) -> dict:
    """The phase 5 headroom for one year of one case: Reserve Fund left plus the smaller margin."""
    sr, c, y = case_res["series"], case_res["consts"], str(year)
    bond = (c["mkt_capacity"] * sr["gdp"][y] + c["foreign_capacity"] + (sr["idle_source"][y] or 0)
            - (sr["bonds_placed"][y] or 0) * c["issue_price"])
    priv = sr["private_margin"][y]
    rf_left = sr["reserve_fund"][str(year - 1)] - (sr["rf_drawn"][y] or 0)
    return {"bond_margin": bond, "private_margin": priv, "rf_left": rf_left, "room": rf_left + min(bond, priv),
            "binding": "bond market" if bond < priv else "private saving"}


def allows_war(res: dict, base: dict, last_year: int = 1900) -> bool:
    """Variant rule for long-lived levers: Story passes everywhere; Stress gains no failed year-check up to last_year
    (new failures after it, such as the knife-edge private-saving check of 1932, are set aside and reported)."""
    if res["story"]["problems_total"] != 0 or res["story"]["formula_errors"] or res["stress"]["formula_errors"]:
        return False
    for y, cols in res["stress"]["failing"].items():
        if int(y) <= last_year and set(cols) - set(base["stress"]["failing"].get(y, [])):
            return False
    return True
