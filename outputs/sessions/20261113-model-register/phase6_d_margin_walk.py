"""Why D strong has a smaller Stress margin of private saving in 1932 than D as solved (author's challenge, 14 Nov).

    PHASE6_BASE=levers2.xlsx PHASE6_CACHE=NEW_DIR python3 phase6_d_margin_walk.py OUT.json

Walks from D as solved to D strong (20,000 refugees, 73.4%) one change at a time and reads the 1932 Stress row of
the private sources and uses table: domestic saving, foreign income, principal returned (sources) against the home
capital allowance, market Treasury bond subscriptions, portfolio outflow and champions' investment (uses). Needs its
own cache folder, because it reads more columns than the other phase 6 scripts.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import phase6_solver as S

S.SU_SERIES.update({"dom_saving": ("Sources & uses", "B"), "foreign_income": ("Sources & uses", "C"),
                    "principal_back": ("Sources & uses", "D"), "sources": ("Sources & uses", "E"),
                    "home_capital": ("Sources & uses", "F"), "treasury_bonds": ("Sources & uses", "G"),
                    "portfolio_out": ("Sources & uses", "H"), "champions": ("Sources & uses", "J"),
                    "uses": ("Sources & uses", "K")})
FIELDS = ["private_margin", "sources", "dom_saving", "foreign_income", "principal_back", "uses", "home_capital",
          "treasury_bonds", "portfolio_out", "champions", "gdp", "real_gdp", "public_debt", "dev_stock", "receipts",
          "spending", "residents"]
HERE = Path(__file__).resolve().parent
WAR = ["cw_rich_early", "cw_rich_late", "cw_hon_batt", "cw_hon_turret", "cw_occ6567", "cw_juarez"]


def main() -> None:
    d = json.loads((HERE / "phase6/packages.json").read_text())["D"]["values"]
    strong = json.loads((HERE / "phase6/d_strong_garrison_safe.json").read_text())[
        "D + lease + refugees 20,000, growth first"]["values"]
    steps = [("D as solved", dict(d))]
    ov = {**d, "cw_alaska_rcpt": strong["cw_alaska_rcpt"]}
    steps.append(("+ seal lease", dict(ov)))
    ov.update({k: strong[k] for k in WAR})
    steps.append(("+ war-year items cut to D strong", dict(ov)))
    ov["cw_or_works"] = strong["cw_or_works"]
    steps.append(("+ Oregon works 7.50 -> 10.87 a year", dict(ov)))
    ov.update(cw_sitka_gar=strong["cw_sitka_gar"], cw_sitka_mail=strong["cw_sitka_mail"])
    steps.append(("+ Sitka 0.95 -> 5.70 a year (= D strong)", dict(ov)))
    steps.append(("D as solved + Sitka alone", {**d, "cw_sitka_gar": strong["cw_sitka_gar"],
                                                 "cw_sitka_mail": strong["cw_sitka_mail"]}))
    res = {}
    for name, o in steps:
        r = S.run(o)
        res[name] = {"stress_1932": {f: r["stress"]["series"][f]["1932"] for f in FIELDS},
                     "stress_1900": {f: r["stress"]["series"][f]["1900"] for f in FIELDS},
                     "story_1932": {f: r["story"]["series"][f]["1932"] for f in FIELDS}}
        print(name, {f: round(v, 1) for f, v in res[name]["stress_1932"].items()}, flush=True)
    Path(sys.argv[1]).write_text(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
