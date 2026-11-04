"""Build Pacifica's energy workbook: power generation and use, 1846-1932.

    python3 energy/build/build_energy_workbook.py FINANCE_INPUTS.csv OUT.xlsx

FINANCE_INPUTS.csv comes from extract_finance.py (Story and Stress results of the
financial workbook). The script writes formulas only; recalculate in LibreOffice
afterwards (the xlsx skill's scripts/recalc.py) and check that no formula errors remain.

Conventions follow the financial workbook: years run down the page (row 6 = 1846,
row 92 = 1932), blue = input, black = formula, green = link to another sheet,
red = value imported from the financial workbook. Every lever has a Story and a
Stress value and a named range; Levers!E4 picks the case and also picks which of the
two imported finance cases feeds the model, so one switch moves the whole system.
All results are MODEL estimates.
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

import openpyxl
from openpyxl.comments import Comment
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.workbook.defined_name import DefinedName
from openpyxl.formatting.rule import CellIsRule

sys.path.insert(0, str(Path(__file__).resolve().parent))
import energy_inputs as I  # noqa: E402

Y0, Y1 = 1846, 1932
FIRST = 6
LAST = FIRST + (Y1 - Y0)  # 92
YEARS = list(range(Y0, Y1 + 1))


def row(y: int) -> int:
    return y - Y0 + FIRST


FONT = "Arial"
F_IN = Font(name=FONT, color="0000FF")
F_IN_FILL = Font(name=FONT, color="6F8FCF", italic=True)
F_CALC = Font(name=FONT, color="000000")
F_LINK = Font(name=FONT, color="008000")
F_EXT = Font(name=FONT, color="C00000")
F_HEAD = Font(name=FONT, bold=True)
F_TITLE = Font(name=FONT, bold=True, size=14)
F_NOTE = Font(name=FONT, italic=True, color="555555")
FILL_HEAD = PatternFill("solid", fgColor="E8EEF6")
FILL_KEY = PatternFill("solid", fgColor="FFF2CC")
FILL_FAIL = PatternFill("solid", fgColor="F4CCCC")
FILL_PASS = PatternFill("solid", fgColor="D9EAD3")
WRAP = Alignment(wrap_text=True, vertical="top")
THIN = Border(bottom=Side(style="thin", color="999999"))

# ------------------------------------------------------------------ hydro basins
BASINS = [  # key, path, label, capacity factor, physical potential (MW, 1920s technique)
    ("sierra", "h_sierra", "Sierra west slope", 0.50, 3500),
    ("pit", "h_pit", "Pit and Feather", 0.55, 2500),
    ("sj", "h_sj", "San Joaquin, Big Creek and Kern", 0.45, 2200),
    ("col", "h_col", "Columbia and Snake", 0.60, 12000),
    ("wil", "h_wil", "Willamette, Cascades and Puget Sound", 0.55, 5000),
    ("colo", "h_colo", "Colorado", 0.50, 3000),
    ("int", "h_int", "Interior (Salt, Wasatch, Bear, upper Snake, Clark Fork)", 0.50, 2000),
    ("haw", "h_haw", "Hawaii (windward streams)", 0.45, 250),
]
LEVERS = list(I.LEVERS) + [("— Hydro basins: capacity factor and physical potential —",)]
for k, p, lab, cf, pot in BASINS:
    LEVERS.append((f"cf_{k}", f"Capacity factor, {lab}", cf, cf, "share", "Model estimate", "Normal year."))
for k, p, lab, cf, pot in BASINS:
    LEVERS.append((f"pot_{k}", f"Physical potential, {lab}", pot, pot, "MW", "Model estimate",
                   "What 1920s dams and lines could develop; strategic dams in the same basin count against it."))

# ------------------------------------------------------------------ finance import
FIN_KEYS = ["pop_res", "pop_all", "guest", "labour", "gdp", "gdp_real", "price", "gdp_pc", "us_gdp_pc", "oil_out",
            "oil_price", "metals", "gold_ca", "gold_int", "steel", "cars", "chem", "elec_eq", "alum_air", "gulf_crude",
            "gulf_share", "asia_oil", "navy_oil", "navy_ships", "atom_mwe", "dev_inv", "public_works"]


def load_finance(path: Path):
    lines = path.read_text().splitlines()
    sha = lines[0].split()[-1]
    rdr = list(csv.reader(lines[1:]))
    hdr = rdr[0]
    data, meta = {}, {}
    for r in rdr[1:]:
        key, case, label, unit = r[:4]
        data[(key, case)] = [float(x) for x in r[4:]]
        meta[key] = (label, unit)
    assert hdr[4] == "1846" and hdr[-1] == "1932"
    return sha, data, meta


# ------------------------------------------------------------------ column model
class Col:
    def __init__(self, key, header, tpl, fmt="#,##0", kind="calc", note="", group=None, first=None, width=12):
        self.key, self.header, self.tpl, self.fmt, self.kind = key, header, tpl, fmt, kind
        self.note, self.group, self.first, self.width = note, group, first, width
        self.letter = None


SHEETS: dict[str, dict] = {}  # name -> {"cols": [...], "title":..., "desc":...}
LETTER: dict[tuple[str, str], str] = {}
PATH_ROW: dict[str, int] = {}
PATH_COLS: tuple[str, str] = ("", "")
US_ROW: dict[str, int] = {}
US_COLS: tuple[str, str] = ("", "")


def sheet(name, title, desc, cols, start_col=2):
    for i, c in enumerate(cols):
        c.letter = get_column_letter(start_col + i)
        LETTER[(name, c.key)] = c.letter
    SHEETS[name] = {"cols": cols, "title": title, "desc": desc}


def q(name: str) -> str:
    return f"'{name}'" if re.search(r"[^A-Za-z0-9_]", name) else name


def interp_path(key: str, r: int) -> str:
    if key + "__max" in PATH_ROW:
        return f"IF(case_sel=3,{_interp_row(key + '__max', r)},{_interp_row(key, r)})"
    return _interp_row(key, r)


def _interp_row(key: str, r: int) -> str:
    p = PATH_ROW[key]
    a, b = PATH_COLS
    yrs = f"Paths!${a}$5:${b}$5"
    vals = f"Paths!${a}${p}:${b}${p}"
    m = f"MATCH($A{r},{yrs},1)"
    return (f"IF($A{r}>=Paths!${b}$5,Paths!${b}${p},INDEX({vals},{m})+($A{r}-INDEX({yrs},{m}))*"
            f"(INDEX({vals},{m}+1)-INDEX({vals},{m}))/(INDEX({yrs},{m}+1)-INDEX({yrs},{m})))")


def interp_us(key: str, r: int) -> str:
    p = US_ROW[key]
    a, b = US_COLS
    yrs = f"Anchors!${a}$6:${b}$6"
    vals = f"Anchors!${a}${p}:${b}${p}"
    m = f"MATCH($A{r},{yrs},1)"
    return (f"IF($A{r}<Anchors!${a}$6,0,IF($A{r}>=Anchors!${b}$6,Anchors!${b}${p},INDEX({vals},{m})+($A{r}-INDEX({yrs},{m}))*"
            f"(INDEX({vals},{m}+1)-INDEX({vals},{m}))/(INDEX({yrs},{m}+1)-INDEX({yrs},{m}))))")


TOKEN = re.compile(r"\{([^{}]+)\}")


def render(tpl: str, this: str, r: int) -> str:
    def sub(m):
        t = m.group(1)
        if t == "A":
            return f"$A{r}"
        if t.startswith("P:"):
            return "(" + interp_path(t[2:], r) + ")"
        if t.startswith("US:"):
            return "(" + interp_us(t[3:], r) + ")"
        rr = r
        if t.endswith("@p"):
            t, rr = t[:-2], r - 1
        if ":" in t:
            sh, k = t.split(":", 1)
            return f"{q(sh)}!{LETTER[(sh, k)]}{rr}"
        return f"{LETTER[(this, t)]}{rr}"
    out = TOKEN.sub(sub, tpl)
    return out if out.startswith("=") else "=" + out


# ------------------------------------------------------------------ sheet specs
PO = "People & output"


def spec_people():
    cols = []
    for k in FIN_KEYS:
        cols.append(Col(k, None, f"IF(case_sel=2,{{{k}_t}},{{{k}_s}})", kind="calc"))
    cols += [
        Col("gold", "Gold and silver ($m)", "{gold_ca}+{gold_int}", "#,##0.0"),
        Col("homes", "Homes (thousand)", "{pop_all}/{P:hh_size}/1000", "#,##0"),
        Col("gdp_pp", "Real GDP per person present (1913 $)", "IF({pop_all}>0,{gdp_real}*1000000/{pop_all},0)", "#,##0"),
        Col("us_pop", "US population (m), anchor", "{US:us_pop}", "#,##0.0", kind="link"),
        Col("us_cap", "US utility generating capacity (GW), anchor", "{US:us_cap}", "#,##0.00", kind="link"),
        Col("us_gen", "US electricity produced (TWh), anchor", "{US:us_gen}", "#,##0.0", kind="link"),
        Col("us_pj", "US primary energy (PJ), anchor", "{US:us_energy}*1055.06", "#,##0", kind="link"),
        Col("us_real", "US real GDP (1913 $m)", "IF({price}>0,{us_gdp_pc}*{us_pop}/{price},0)", "#,##0",
            note="US GDP per person (finance Economy!Q) × US population ÷ the finance workbook's price level, used as the deflator for both."),
    ]
    for k in FIN_KEYS:
        cols.append(Col(k + "_s", None, None, kind="ext"))
    for k in FIN_KEYS:
        cols.append(Col(k + "_t", None, None, kind="ext"))
    sheet(PO, "People and output", "Population, output and industry from the financial workbook (Story and Stress), "
          "with the case picked by Levers!E4 (the Max case uses the Story values). No independent population: the energy model only multiplies these.", cols)


def spec_hydro():
    cols = []
    for k, p, lab, cf, pot in BASINS:
        cols.append(Col(f"cap_{k}", f"{lab} (MW)", f"{{P:{p}}}*hydro_pace*(1+({{P:hyd_x}}-1)*hydx_on)", group="Nameplate capacity, ordinary plants"))
    cols += [
        Col("cap_works", "The Works' dams, Pit and upper Feather (MW)", "{P:h_works}", group="Strategic dams",
            note="CR-051 R2. Not scaled by hydro_pace. Native consent OPEN."),
        Col("cap_rock", "Rock Island (MW)", "{P:h_rock}", note="CR-051 S7; the Rock Island compact (S8 C)."),
        Col("cap_hilo", "Hawaiian hydro board, Big Island (MW)", "IF(hilo_src=2,{P:h_hilo},0)", note="CR-052 CT6. Not scaled by hydro_pace."),
        Col("cap_bonn", "Bonneville (MW)", "{P:h_bonn}", note="CR-055: decided 1908, first power 1913; laddered; Celilo untouched."),
        Col("cap_rreach", "Rocky Reach (MW)", "{P:h_rreach}", note="CR-055: decided 1914, first power 1919."),
        Col("cap_wells", "Wells (MW)", "{P:h_wells}", note="CR-055: decided 1921, first power 1926."),
        Col("cap_boulder", "Boulder Canyon (MW)", "IF({A}>=boulder_dec+boulder_lead,MIN(1345,({A}-boulder_dec-boulder_lead+1)*330),0)",
            note="Built up at 330 MW a year to 1,345 MW from the decision plus lead time (Levers). OPEN."),
        Col("cap_colms", "Mid-Columbia chain (MW)", "IF(AND(colms_on=1,{A}>=colms_dec+dam_lead+1),MIN(colms_max,({A}-colms_dec-dam_lead)*colms_rate),0)",
            note="PROPOSED (CR-052): low main-stem dams with ladders above Rock Island; first power in the year after decision + lead time."),
        Col("cap_total", "All hydro (MW)", "+".join(f"{{cap_{k}}}" for k, *_ in BASINS) + "+{cap_works}+{cap_rock}+{cap_hilo}+{cap_bonn}+{cap_rreach}+{cap_wells}+{cap_boulder}+{cap_colms}",
            group="Totals"),
        Col("rain", "Rainfall (× normal)", "IF({A}=dry_year,dry_factor,1)", "0.00"),
    ]
    for k, p, lab, cf, pot in BASINS:
        cols.append(Col(f"av_{k}", f"{lab} (GWh)", f"{{cap_{k}}}*cf_{k}*8.76*{{rain}}", group="Output available (GWh)"))
    cols += [
        Col("av_works", "The Works' dams (GWh)", "{cap_works}*works_cf*8.76*{rain}"),
        Col("av_rock", "Rock Island (GWh)", "{cap_rock}*cf_col*8.76*{rain}"),
        Col("av_hilo", "Hawaiian hydro board (GWh)", "{cap_hilo}*cf_haw*8.76*{rain}"),
        Col("av_bonn", "Bonneville (GWh)", "{cap_bonn}*cf_col*8.76*{rain}"),
        Col("av_rreach", "Rocky Reach (GWh)", "{cap_rreach}*cf_col*8.76*{rain}"),
        Col("av_wells", "Wells (GWh)", "{cap_wells}*cf_col*8.76*{rain}"),
        Col("av_boulder", "Boulder Canyon (GWh)", "{cap_boulder}*cf_colo*8.76*{rain}"),
        Col("av_colms", "Mid-Columbia chain (GWh)", "{cap_colms}*cf_col*8.76*{rain}"),
        Col("av_main", "Mainland hydro available (GWh)", "+".join(f"{{av_{k}}}" for k, *_ in BASINS if k != "haw") +
            "+{av_works}+{av_rock}+{av_bonn}+{av_rreach}+{av_wells}+{av_boulder}+{av_colms}", group="Totals"),
        Col("av_haw", "Hawaii hydro available (GWh)", "{av_haw}" if False else f"{{av_haw}}"),
    ]
    # av_haw total duplicates the basin column name; rename the basin one
    cols[-1] = Col("av_haw_t", "Hawaii hydro available (GWh)", "{av_haw}+{av_hilo}")
    cols += [
        Col("u_pit", "Pit and Feather incl. the Works", "({cap_pit}+{cap_works})/pot_pit", "0%", group="Share of physical potential used"),
        Col("u_col", "Columbia and Snake incl. Rock Island, the CR-055 dams and the chain", "({cap_col}+{cap_rock}+{cap_bonn}+{cap_rreach}+{cap_wells}+{cap_colms})/pot_col", "0%"),
        Col("u_colo", "Colorado incl. Boulder", "({cap_colo}+{cap_boulder})/pot_colo", "0%"),
        Col("u_haw", "Hawaii incl. the hydro board", "({cap_haw}+{cap_hilo})/pot_haw", "0%"),
        Col("u_max", "Highest basin", "MAX({u_pit},{u_col},{u_colo},{u_haw}," + ",".join(f"{{cap_{k}}}/pot_{k}" for k, *_ in BASINS
                                                                              if k not in ("pit", "col", "colo", "haw")) + ")", "0%"),
        Col("lead_ok", "Strategic dams after their lead time (1 = yes)",
            "IF(AND({A}<works_dec+dam_lead,{cap_works}>0),0,1)*IF(AND({A}<rock_dec+dam_lead,{cap_rock}>0),0,1)*IF(AND({A}<colms_dec+dam_lead+1,{cap_colms}>0),0,1)*IF(AND({A}<boulder_dec+boulder_lead,{cap_boulder}>0),0,1)", "0",
            group="Lead time"),
    ]
    sheet("Hydro", "Hydro by river basin", "Nameplate capacity by basin (Story path × hydro pace), the strategic dams, output in "
          "a normal year and the use of each basin's physical potential.", cols)


def spec_strategic():
    cols = [
        Col("halls_mw", "Halls' draw (MW)", "IF({A}<=1927,{P:halls_lo}+halls_pos*({P:halls_hi}-{P:halls_lo}),"
            "halls_after*(600+halls_pos*200))", group="Separation halls (CR-051 M2)",
            note="CR-051 M2 range, positioned by halls_pos; after 1927 × halls_after (OPEN)."),
        Col("halls_gwh", "Halls' use (GWh)", "{halls_mw}*8.76*strat_lf"),
        Col("arc_mw", "Arc nitrogen plants' load (MW)", "{Uses:e_arc}/8.76/0.95", "#,##0", group="Their power (R1, R2)"),
        Col("arc_peak", "Arc plants' wartime peak (MW)", f"MAX(${{arc_mw}}$6:${{arc_mw}}${row(1918)})".replace("${arc_mw}$6", "X"), "#,##0"),
        Col("freed", "Arc power freed for the halls (MW)", "IF({A}>=1919,MAX(0,{arc_peak}-{arc_mw}),0)", "#,##0"),
        Col("works_avg", "Works' dams, average output (MW)", "{Hydro:av_works}/8.76", "#,##0"),
        Col("halls_ded", "Halls met from dedicated power (MW avg)", "MIN({halls_mw}*strat_lf,{freed}+{works_avg})", "#,##0"),
        Col("halls_grid", "Halls met from the common grid (MW avg)", "{halls_mw}*strat_lf-{halls_ded}", "#,##0"),
        Col("halls_gs", "Share of the halls' power from the grid", "IF({halls_mw}>0,{halls_grid}/({halls_mw}*strat_lf),0)", "0%"),
        Col("feed_mt", "Feed plant oil (Mt)", "IF(AND({A}>=1921,{A}<=1927),0.4+feed_pos*0.35,IF({A}>1927,halls_after*(0.4+feed_pos*0.35),0))",
            "0.00", group="Feed plant (CR-051 M1, M2)", note="Steam for the thermal-diffusion columns, from 1921."),
        Col("feed_pj", "Feed plant oil (PJ)", "{feed_mt}*41.9", "#,##0.0"),
        Col("st_mw", "Columbia station's draw (MW)", "{P:station}", group="Columbia station (CR-051 S7)"),
        Col("st_gwh", "Columbia station's use (GWh)", "{st_mw}*8.76*strat_lf"),
        Col("rock_avg", "Rock Island, average output (MW)", "{Hydro:av_rock}/8.76"),
        Col("wen_mw", "Wenatchee smelter (MW avg)", "{P:alu_wen}*{P:alu_mwh}/8.76", note="Part of aluminium on Uses."),
        Col("rock_spare", "Rock Island left for orchards and pumps (MW avg)", "{rock_avg}-{st_mw}*strat_lf-{wen_mw}"),
        Col("roslyn_mw", "Roslyn coal steam plant on standby (MW)", "{st_mw}", note="Second supply for the pumps; standby, fuel not counted."),
        Col("hh_mw", "Walled college and Tuolumne Station (MW)", "{P:hetch}", "#,##0.0", group="Hetch Hetchy (CR-050, CR-051)",
            note="From the Eleanor–Cherry system O'Shaughnessy builds."),
        Col("hh_gwh", "Walled college's use (GWh)", "{hh_mw}*8.76*strat_lf", "#,##0.0"),
        Col("hilo_mw", "Hilo smelter (MW avg)", "{P:alu_hilo}*{P:alu_mwh}/8.76", "#,##0", group="Hilo aluminium (I13, L14)"),
        Col("haw_hyd", "Hawaii hydro, average (MW)", "{Hydro:av_haw_t}/8.76", "#,##0"),
        Col("haw_ord", "Hawaii's ordinary load (MW avg)", "{Electricity:haw_gen_ord}/8.76", "#,##0"),
        Col("hilo_board", "Hawaiian hydro board, average output (MW)", "{Hydro:av_hilo}/8.76", "#,##0"),
        Col("hilo_ok", "Hilo's source can carry it (1 = yes)", "IF(hilo_src=2,IF({hilo_mw}<={hilo_board}+0.001,1,0),1)", "0",
            note="CT6: the board's own plants carry the smelter; Honolulu's grid stays as it is."),
        Col("hilo_oil", "Hilo smelter's oil (PJ)", "IF(hilo_src=1,{hilo_mw}*8.76*{P:heat_rate}/1000,0)", "#,##0.0",
            note="Counted inside the Hawaii thermal generation on Electricity."),
        Col("navy", "Navy oil (m bbl)", "{People & output:navy_oil}", "#,##0.0", kind="link", group="Memo"),
        Col("canal", "Canal locks and zone (MW, outside the Realm)", "{P:canal_mw}", "#,##0"),
        Col("strat_gwh", "Strategic loads on dedicated lines (GWh)", "{halls_gwh}+{st_gwh}+{hh_gwh}", group="Total"),
    ]
    sheet("Strategic loads", "Strategic loads", "Each named canon load with its source of power (register at right). "
          "The halls, the feed plant, the Columbia station and the walled college are MODEL figures from CR-050 and CR-051.", cols)


ECHEM = ["e_alu", "e_arc", "e_haber", "e_eln", "e_carb", "e_chlor", "e_esteel", "e_falloy", "e_abras", "e_zinc", "e_mg", "e_phos", "e_cu"]


def spec_uses():
    cols = [
        Col("homes_el", "Homes with electricity (thousand)", "{People & output:homes}*MIN(1,{P:elec_home}*elec_pace)", group="Electricity (GWh)"),
        Col("e_home", "Households", "{homes_el}*{P:kwh_home}*home_kwh_x/1000"),
        Col("e_comm", "Commerce and public lighting", "{People & output:pop_all}*{P:kwh_comm}*elec_pace/1000000"),
        Col("fact", "Factory horsepower electric", "MIN(1,{P:fact_elec}*elec_pace)", "0%"),
        Col("e_motor", "Industry, motors (and process heat if heat_el = 1)", "{People & output:gdp_real}*ind_w*{P:ind_idx}*(1+({P:indw_x}-1)*heat_el)*{fact}*motor_full",
            note="Real GDP × industrial weight (ind_w × the finance calibration Paths ind_idx) × factory horsepower electric × kWh per 1913 $ of US-type output (motor_full); "
                 "the Max case's electrified process heat (Paths indw_x) applies only when heat_el = 1, so it never stacks on a higher finance weight."),
        Col("e_alu", "Aluminium", "{P:alu_kt}*{P:alu_mwh}", group="Electrochemistry and electrometallurgy (GWh)"),
        Col("e_arc", "Arc nitrogen", "{P:arc_kt}*arc_mwh"),
        Col("e_haber", "Haber–Bosch nitrogen", "{P:haber_kt}*haber_mwh"),
        Col("e_eln", "Electrolytic nitrogen (the Columbia's cells)", "{P:eln_kt}*eln_mwh"),
        Col("e_carb", "Calcium carbide", "{P:carb_kt}*carbide_mwh"),
        Col("e_chlor", "Chlor-alkali", "{P:chlor_kt}*chlor_mwh"),
        Col("e_esteel", "Electric steel", "{People & output:steel}*1000*{P:esteel}*esteel_mwh"),
        Col("e_falloy", "Ferro-alloys", "IF({A}>=1900,{People & output:steel}*1000*falloy_share*falloy_mwh,0)"),
        Col("e_abras", "Carborundum and graphite", "{P:abras_kt}*abras_mwh"),
        Col("e_zinc", "Electrolytic zinc (CR-055)", "{P:zinc_kt}*zinc_mwh"),
        Col("e_mg", "Magnesium (CR-055)", "{P:mg_kt}*mg_mwh"),
        Col("e_phos", "Furnace phosphorus (CR-055)", "{P:phos_kt}*phos_mwh"),
        Col("e_cu", "Electrolytic copper refining (CR-055)", "{P:cu_kt}*cu_mwh"),
        Col("e_echem", "All electrochemistry", "+".join("{%s}" % k for k in ECHEM)),
        Col("e_mine", "Mining and smelting", "({People & output:metals}+{People & output:gold})/{People & output:price}*{P:mine_int}",
            group="Electricity (GWh), continued"),
        Col("e_rail", "Streetcars, interurbans (and main lines if electrified)",
            "{People & output:pop_all}*{P:rail_kwh}/1000000+IF(mainline_on=1,{People & output:pop_all}*{P:rail_gj}/1000000*{P:rail_el}*rail_kwh_gj,0)"),
        Col("e_pump", "Pumping and irrigation", "{P:pump_acres}*pump_kwh"),
        Col("alu_grid", "Aluminium for the grid's conductor (kt, memo)", "{P:alu_grid}", "#,##0.0", group="Aluminium's uses (kt, memo; CR-054 A1)"),
        Col("alu_air", "… the Concord fleet's aircraft", "{P:alu_air}", "#,##0.0"),
        Col("alu_pool", "… the Concord pool, to Japan", "{P:alu_pool}", "#,##0.0"),
        Col("alu_civil", "… civil uses at home", "{P:alu_civil}", "#,##0.0"),
        Col("alu_exp", "… exported beyond the Concord", "MAX(0,{P:alu_kt}-{alu_grid}-{alu_air}-{alu_pool}-{alu_civil})", "#,##0.0", kind="key",
            note="The part exposed to sterling and the European cartel in 1931 (CR-054 A4)."),
        Col("e_nwboil", "Electric boilers in Northwest mills", "{P:nwboil}*nwboil_x"),
        Col("e_ord", "Ordinary uses", "{e_home}+{e_comm}+{e_motor}+{e_echem}+{e_mine}+{e_rail}+{e_pump}+{e_nwboil}"),
        Col("e_strat", "Strategic loads (halls, station, valley)", "{Strategic loads:strat_gwh}", kind="link"),
        Col("e_total", "All electricity used", "{e_ord}+{e_strat}"),
        Col("veh", "Motor vehicles on the road (thousand)",
            "IF(veh_src=2,{P:veh_pp}*{People & output:pop_all}/1000,{veh@p}*(1-car_scrap)+{People & output:cars}*car_home)",
            first="IF(veh_src=2,{P:veh_pp}*{People & output:pop_all}/1000,{People & output:cars}*car_home)", group="Fuel (PJ)",
            note="veh_src = 2: vehicles per person (Paths veh_pp, CR-052 CT5); 1: the financial workbook's build × share kept."),
        Col("veh_pp", "Vehicles per person", "IF({People & output:pop_all}>0,{veh}*1000/{People & output:pop_all},0)", "0.00", kind="key"),
        Col("veh_cal", "California's vehicles per person (memo)", "{veh_pp}*cal_mult", "0.00"),
        Col("veh_build", "Vehicles the finance workbook must build (thousand)", "MAX(0,{veh}-{veh@p}*(1-car_scrap))/car_home",
            first="{veh}/car_home", note="New vehicles for the road, plus exports at the same share as now."),
        Col("gasoline", "Motor fuel (m bbl)", "{veh}/1000*{P:gal_veh}", "#,##0.0"),
        Col("f_motor", "Motor fuel", "{gasoline}*5.54", "#,##0.0"),
        Col("f_lamp", "Lamp oil", "{People & output:homes}*{P:lamp_bbl}/1000*5.98", "#,##0.0"),
        Col("f_navy_oil", "Navy oil", "{People & output:navy_oil}*6.63", "#,##0.0"),
        Col("f_navy_coal", "Navy coal", "{P:navy_coal}*coal_gj", "#,##0.0"),
        Col("f_bunker", "Merchant bunkers", "{P:bunker}*6.63", "#,##0.0"),
        Col("f_rail", "Steam railways", "{People & output:pop_all}*{P:rail_gj}/1000000*(1-IF(mainline_on=1,{P:rail_el},0))", "#,##0.0"),
        Col("f_ind", "Industry: fuel and steam", "MAX(0,{People & output:gdp_real}*{P:ind_mj}*{P:ind_idx}/1000-{Uses:e_nwboil}*5.1/1000)", "#,##0.0",
            note="ind_mj already reflects Pacifica's lighter industry (about 0.35–0.4 of US intensity), consistent with ind_w; both are scaled by the same finance calibration (Paths ind_idx). Electric mill boilers replace 5.1 MJ of fuel per kWh."),
        Col("f_steel", "Steel: coke and coal", "{People & output:steel}*{P:steel_gj}", "#,##0.0"),
        Col("f_haber", "Haber–Bosch: gas", "{P:haber_kt}*haber_gj/1000", "#,##0.0"),
        Col("f_bld", "Heating and cooking", "({People & output:homes}*{P:gj_home}+{People & output:pop_all}/1000*{P:gj_comm})/1000", "#,##0.0"),
        Col("f_feed", "The Works' feed plant (oil)", "{Strategic loads:feed_pj}", "#,##0.0", kind="link"),
        Col("f_sugar", "Sugar mills (bagasse)", "{P:sugar_kt}*24/1000", "#,##0.0"),
        Col("f_power", "Power stations' fuel", "{Electricity:pj_power}", "#,##0.0", kind="link", group="Conversion (PJ)"),
        Col("f_refine", "Refineries' own use", "{Fuels:own_pj}", "#,##0.0", kind="link"),
        Col("f_hydro", "Hydro (fossil-fuel equivalent)", "{Electricity:pj_hydro}", "#,##0.0", kind="link"),
        Col("f_atom", "Atomic (fossil-fuel equivalent)", "{Electricity:pj_atom}", "#,##0.0", kind="link"),
        Col("use_pj", "Primary energy, use side (PJ)", "+".join("{%s}" % k for k in
            ["f_motor", "f_lamp", "f_navy_oil", "f_navy_coal", "f_bunker", "f_rail", "f_ind", "f_steel", "f_haber", "f_bld",
             "f_feed", "f_sugar", "f_power", "f_refine", "f_hydro", "f_atom"]), group="Total"),
    ]
    sheet("Uses", "Uses of electricity and fuel", "Electricity by sector (GWh) and fuel by sector (PJ), each built from a "
          "driver in the financial workbook times an intensity path (Paths) or a lever.", cols)


def spec_electricity():
    cols = [
        Col("ord", "Ordinary sales (GWh)", "{Uses:e_ord}", kind="link", group="Demand"),
        Col("strat", "Strategic sales (GWh)", "{Uses:e_strat}", kind="link"),
        Col("loss", "Losses, ordinary", "{P:loss}", "0%"),
        Col("gen_ord", "Generation for ordinary uses (GWh)", "{ord}/(1-{loss})"),
        Col("gen_strat", "Generation for strategic loads (GWh)", "{strat}/(1-strat_loss)"),
        Col("gen", "Generation (GWh)", "{gen_ord}+{gen_strat}"),
        Col("hilo_gwh", "Hilo smelter (GWh)", "{P:alu_hilo}*{P:alu_mwh}", group="Hawaii's island grid"),
        Col("haw_gen_ord", "Hawaii ordinary generation (GWh)", "({ord}-{hilo_gwh})*{P:hawaii}/(1-{loss})"),
        Col("haw_gen", "Hawaii generation incl. Hilo (GWh)", "{haw_gen_ord}+{hilo_gwh}/(1-{loss})"),
        Col("main_gen", "Mainland generation (GWh)", "{gen}-{haw_gen}"),
        Col("atom", "Atomic stations (GWh)", "{People & output:atom_mwe}*atom_cf*8.76", group="Supply (GWh)"),
        Col("hyd_main", "Hydro used, mainland", "MIN({Hydro:av_main}-{stranded},MAX(0,{main_gen}-{atom}))",
            note="Northwest water power beyond the Northwest's own load cannot reach California unless a line carries it (Paths tie_mw)."),
        Col("hyd_haw", "Hydro used, Hawaii", "MIN({Hydro:av_haw_t},{haw_gen})"),
        Col("hyd", "Hydro used", "{hyd_main}+{hyd_haw}"),
        Col("spill", "Hydro spilled", "{Hydro:av_main}+{Hydro:av_haw_t}-{hyd}"),
        Col("th_main", "Steam, mainland", "{main_gen}-{atom}-{hyd_main}"),
        Col("th_haw", "Steam, Hawaii (oil)", "{haw_gen}-{hyd_haw}"),
        Col("th", "Steam generation", "{th_main}+{th_haw}"),
        Col("hydro_share", "Hydro share of generation", "IF({gen}>0,{hyd}/{gen},0)", "0%"),
        Col("peak", "Peak demand (MW)", "{gen_ord}/(8.76*{P:sys_lf})+{gen_strat}/(8.76*strat_lf)", group="Capacity (MW)"),
        Col("hyd_cap", "Hydro", "{Hydro:cap_total}", kind="link"),
        Col("th_cap", "Steam", "MAX(0,{peak}*(1+reserve)-{hyd_cap}*hydro_firm-{People & output:atom_mwe},{th}/(8.76*th_cf_max))"),
        Col("at_cap", "Atomic", "{People & output:atom_mwe}", kind="link"),
        Col("cap", "All generating capacity", "{hyd_cap}+{th_cap}+{at_cap}"),
        Col("sys_cf", "System capacity factor", "IF({cap}>0,{gen}/(8.76*{cap}),0)", "0%"),
        Col("th_cf", "Steam capacity factor", "IF({th_cap}>0,{th}/(8.76*{th_cap}),0)", "0%"),
        Col("res", "Reserve margin at the peak", "IF({peak}>0,({hyd_cap}*hydro_firm+{th_cap}+{at_cap})/{peak}-1,0)", "0%"),
        Col("hr", "Heat rate (MJ/kWh)", "{P:heat_rate}", "0.0", group="Fuel (PJ)"),
        Col("pj_oil", "Oil wanted", "({th_main}*{P:th_oil}+{th_haw})*{hr}/1000", "#,##0.0"),
        Col("pj_gas", "Gas", "{th_main}*{P:th_gas}*{hr}/1000", "#,##0.0"),
        Col("pj_coal", "Coal (more if oil is short: Fuels)", "{th_main}*(1-{P:th_oil}-{P:th_gas})*{hr}/1000", "#,##0.0"),
        Col("pj_power", "All power-station fuel", "{pj_oil}+{pj_gas}+{pj_coal}", "#,##0.0"),
        Col("pj_hydro", "Hydro, fossil-fuel equivalent", "{hyd}*{hr}/1000", "#,##0.0"),
        Col("pj_atom", "Atomic, fossil-fuel equivalent", "{atom}*{hr}/1000", "#,##0.0"),
        Col("kwh_pp", "Electricity per person (kWh)", "IF({People & output:pop_all}>0,{gen}*1000000/{People & output:pop_all},0)",
            group="Per person and against the US"),
        Col("kw_pp", "Capacity per person (kW)", "IF({People & output:pop_all}>0,{cap}*1000/{People & output:pop_all},0)", "0.000"),
        Col("us_kw_pp", "US utility capacity per person (kW)", "IF({People & output:us_pop}>0,{People & output:us_cap}/{People & output:us_pop},0)", "0.000"),
        Col("mult_cap", "Multiplier: capacity per person vs US utilities", "IF({us_kw_pp}>0,{kw_pp}/{us_kw_pp},\"\")", "0.00", kind="key",
            note="The power check's input (2.0–3.0), now an output. US utilities only: industrial plants add about a third."),
        Col("us_kwh_pp", "US electricity per person, all producers (kWh)", "IF({People & output:us_pop}>0,{People & output:us_gen}*1000/{People & output:us_pop},0)"),
        Col("mult_gen", "Multiplier: electricity per person vs US", "IF({us_kwh_pp}>0,{kwh_pp}/{us_kwh_pp},\"\")", "0.00", kind="key"),
        Col("halls_cap", "Halls / capacity", "IF({cap}>0,{Strategic loads:halls_mw}/{cap},0)", "0.0%", kind="key", group="The halls (CR-051)"),
        Col("halls_el", "Halls / electricity used", "IF({ord}+{strat}>0,{Strategic loads:halls_gwh}/({ord}+{strat}),0)", "0.0%", kind="key"),
        Col("nw_gen", "Northwest generation needed (GWh)",
            "(({ord}-{Uses:e_echem}-{Uses:e_nwboil})*{P:nw_share}+{Uses:e_nwboil}+{P:alu_col}*{P:alu_mwh}+{Uses:e_eln}*eln_col+({Uses:e_zinc}+{Uses:e_phos})*{P:nw_new}+0.3*({Uses:e_echem}-{Uses:e_alu}-{Uses:e_eln}-{Uses:e_zinc}-{Uses:e_phos}-{Uses:e_mg}-{Uses:e_cu}))/(1-{loss})"
            "+{Strategic loads:st_gwh}/(1-strat_loss)", group="The Northwest's own balance",
            note="Ordinary load at the Northwest's share, Columbia aluminium, electrolytic nitrogen on the Columbia, a third of the rest of electrochemistry, the Columbia station."),
        Col("nw_hyd", "Northwest hydro available (GWh)", "{Hydro:av_col}+{Hydro:av_wil}+{Hydro:av_rock}+{Hydro:av_bonn}+{Hydro:av_rreach}+{Hydro:av_wells}+{Hydro:av_colms}+0.5*{Hydro:av_int}"),
        Col("nw_spare", "Northwest hydro beyond its own load (GWh)", "MAX(0,{nw_hyd}-{nw_gen})", kind="key",
            note="No 1920s line could carry it to California: it needs more Northwest industry or a tie line."),
        Col("stranded", "… of which no line can carry south (GWh, spilled)", "MAX(0,{nw_spare}-{P:tie_mw}*8.76)"),
        Col("hyd_dry", "Hydro in a dry year (GWh)", "({Hydro:av_main}+{Hydro:av_haw_t})/{Hydro:rain}*dry_factor", group="Dry-year test"),
        Col("av_dry", "Supply possible in a dry year (GWh)", "{hyd_dry}+{th_cap}*8.76*0.85+{atom}"),
        Col("short_dry", "Shortfall in a dry year (GWh)", "MAX(0,{gen}-{av_dry})"),
        Col("interr", "Interruptible electrochemistry (GWh)", "({Uses:e_arc}+{Uses:e_carb}+{Uses:e_abras}+{Uses:e_falloy}+{Uses:e_phos}+{Uses:e_zinc})/(1-{loss})"),
        Col("dry_ok", "Strategic loads kept in a dry year (1 = yes)", "IF({short_dry}<={interr},1,0)", "0"),
    ]
    sheet("Electricity", "Electricity", "Generation, capacity by source, capacity factors, losses, reserve, the dry-year test "
          "and the multiplier against the United States, which the power check assumed and this sheet computes.", cols)


def spec_fuels():
    O = "Uses"
    cols = [
        Col("fixed_pj", "Oil for uses that must have it (PJ)", "+".join(f"{{{O}:{k}}}" for k in ["f_motor", "f_lamp", "f_navy_oil", "f_bunker", "f_feed"]),
            "#,##0.0", group="Oil (crude equivalent at 6.12 GJ/bbl)",
            note="Motor fuel, lamp oil, the navy, bunkers and the feed plant."),
        Col("flex_pj", "Oil wanted where coal could serve (PJ)", f"{{{O}:f_rail}}*{{P:rail_oil}}+{{{O}:f_ind}}*{{P:ind_oil}}+{{{O}:f_bld}}*{{P:bld_oil}}"
            "+{Electricity:pj_oil}+{gas_short}", "#,##0.0", note="Railways, industry, buildings and power stations at their wanted oil shares, plus gas that is not there."),
        Col("E0", "Exports to Asia from home refineries, wanted (m bbl)", "{People & output:asia_oil}*asia_home", "#,##0.0"),
        Col("home", "Home oilfields (m bbl)", "IF(oil_src=2,{P:oil_c52}*IF({A}=1932,1-0.15*compact_on,1),{People & output:oil_out})", "#,##0.0", kind="key",
            note="oil_src = 2: CR-052's discovery path (Paths oil_c52), with the 1932 compact's cut only if compact_on = 1; 1: the financial workbook."),
        Col("gulf_av", "Gulf crude that can come home (m bbl)", "IF({A}>=1901,MAX(0,{People & output:gulf_crude}*{People & output:gulf_share}"
            "-{People & output:asia_oil}*(1-asia_home))*gulf_home,0)", "#,##0.0"),
        Col("conc", "CR-053 concessions: entitlement crude (m bbl)", "+".join("{P:%s}" % k for k in I.CONC_KEYS), "#,##0.0",
            note="Maracaibo, De Mares, Peru, Bahrain, Kuwait, Mesopotamia (Paths conc_*; PROPOSED, MODEL)."),
        Col("imp_max", "Most oil that can be imported (m bbl)", "{gulf_av}+{P:other_imp}+{conc}", "#,##0.0"),
        Col("avail", "Products available before any measure (PJ)", "(({home}+{imp_max})*(1-ref_own)-{E0})*6.12", "#,##0.0",
            group="A short year: stocks, exports, rationing, the switch to coal, unmet demand",
            note="Crude in reach less exports wanted, refined."),
        Col("deficit", "Shortfall against everything wanted (PJ)", "MAX(0,{fixed_pj}+{flex_pj}-{avail})", "#,##0.0"),
        Col("stk_tgt", "Stocks target (PJ)", "stock_days/365*{oil_pj@p}", "#,##0.0", first="0"),
        Col("stk_use", "Drawn from stocks (PJ)", "MIN({stk@p},{deficit})", "#,##0.0", first="0"),
        Col("exp_cutp", "Asian exports deferred (PJ)", "IF(prio=1,MIN({E0}*6.12*exp_cut,{deficit}-{stk_use}),0)", "#,##0.0"),
        Col("E", "Exports to Asia from home refineries (m bbl)", "{E0}-{exp_cutp}/6.12", "#,##0.0"),
        Col("stk_fill", "Put into stocks (PJ)", "MIN(MAX(0,{stk_tgt}-({stk@p}-{stk_use})),MAX(0,{avail}+{exp_cutp}-{fixed_pj}-{flex_pj}))", "#,##0.0", first="0",
            note="Refilled only from surplus: while the import ceiling binds, stocks cannot be rebuilt by buying more."),
        Col("k0", "Share of the wanted oil the flexible uses get before the switch", "IF({flex_pj}>0,MAX(0,MIN(1,({avail}+{stk_use}+{exp_cutp}-{stk_fill}-{fixed_pj})/{flex_pj})),1)", "0%"),
        Col("switch", "Flexible demand that can switch to coal (PJ)", "{P:dual_share}*dual_x*{flex_pj}", "#,##0.0"),
        Col("to_coal", "Moved from oil to coal (PJ)", "MIN((1-{k0})*{flex_pj},{switch})", "#,##0.0"),
        Col("mf_cutp", "Motor fuel rationed (PJ)", "IF(prio=1,MIN({Uses:f_motor}*mf_cut,(1-{k0})*{flex_pj}-{to_coal}),0)", "#,##0.0", kind="key",
            note="Only after the coal-capable plant has switched."),
        Col("fixed_adj", "Oil for uses that must have it, after rationing (PJ)", "{fixed_pj}-{mf_cutp}", "#,##0.0"),
        Col("k", "Share of the wanted oil the flexible uses get", "IF({flex_pj}>0,MIN(1,{k0}+{mf_cutp}/{flex_pj}),1)", "0%", kind="key"),
        Col("unmet", "Oil demand left unmet: real curtailment (PJ)", "MAX(0,(1-{k})*{flex_pj}-{to_coal})", "#,##0.0", kind="key",
            note="Flexible demand that neither oil nor coal-capable plant can serve: the load-shedding figure. Check 10 holds it under unmet_max."),
        Col("unmet_sh", "… as a share of the flexible demand", "IF({flex_pj}>0,{unmet}/{flex_pj},0)", "0.0%"),
        Col("oil_pj", "Oil products used (PJ)", "{fixed_adj}+{k}*{flex_pj}", "#,##0.0"),
        Col("stk", "Stocks at year end (PJ)", "{stk@p}-{stk_use}+{stk_fill}", "#,##0.0", first="0"),
        Col("stk_days", "Stocks (days of use)", "IF({oil_pj}>0,{stk}/{oil_pj}*365,0)", "0", kind="key"),
        Col("bal_adj", "Balance adjustment: curtailment + stocks drawn − stocks filled (PJ)", "{unmet}+{mf_cutp}+{stk_use}-{stk_fill}", "#,##0.0"),
        Col("D", "Oil products used (m bbl)", "{oil_pj}/6.12", "#,##0.0", group="Oil balance"),
        Col("T", "Refinery throughput (m bbl)", "({D}-{stk_use}/6.12+{stk_fill}/6.12+{E})/(1-ref_own)", "#,##0.0"),
        Col("own_pj", "Refineries' own use (PJ)", "ref_own*{T}*6.12", "#,##0.0"),
        Col("imp", "Oil imported (m bbl): the Gulf from 1901, the Union, Peru and Russia before", "MAX(0,{T}-{home})", "#,##0.0", kind="key"),
        Col("oexp", "Other crude exports (m bbl)", "MAX(0,{home}-{T})", "#,##0.0"),
        Col("resid", "Balance residual (m bbl)", "{home}+{imp}-{oexp}-{T}", "0.000"),
        Col("gas_yield", "Motor fuel / throughput", "IF({T}>0,{Uses:gasoline}/{T},0)", "0%"),
        Col("cap_oil", "Plausible field output (m bbl)", "IF(oil_src=2,{P:oil_cap},{P:oil_caph})", "#,##0.0"),
        Col("cum", "Home output to date (bn bbl)", "{cum@p}+{home}/1000", "0.00", first="{home}/1000"),
        Col("known", "Known recoverable (bn bbl)", "IF(oil_src=2,{P:oil_known},{P:oil_knownh})", "0.00"),
        Col("gas_sup", "Marketed gas: oilfields and dry fields (PJ)", "{home}*{P:gor}*1.087*{P:gas_mkt}+{P:dry_gas}", "#,##0.0", group="Gas (PJ)"),
        Col("gas_dem", "Gas wanted", f"{{{O}:f_ind}}*{{P:ind_gas}}+{{{O}:f_bld}}*{{P:bld_gas}}+{{{O}:f_haber}}+{{Electricity:pj_gas}}", "#,##0.0"),
        Col("gas_used", "Gas used", "MIN({gas_sup},{gas_dem})", "#,##0.0"),
        Col("gas_short", "Shortfall made up with oil", "{gas_dem}-{gas_used}", "#,##0.0"),
        Col("flared", "Gas flared, vented or left in the ground", "{home}*{P:gor}*1.087+{P:dry_gas}-{gas_used}", "#,##0.0"),
        Col("coal_pj", "Solid fuel needed beyond the wood shares (PJ)", f"{{{O}:f_navy_coal}}+{{{O}:f_rail}}*(1-{{P:rail_oil}}-{{P:rail_wood}})+"
            f"{{{O}:f_ind}}*(1-{{P:ind_oil}}-{{P:ind_gas}}-{{P:ind_wood}})+{{{O}:f_steel}}+{{{O}:f_bld}}*(1-{{P:bld_wood}}-{{P:bld_gas}}-{{P:bld_oil}})+"
            "{Electricity:pj_coal}+{to_coal}", "#,##0.0", group="Coal"),
        Col("coal_cap", "Western coal the Realm can raise (Mt)", "({P:c_wa}+{P:c_ut}+{P:c_nm}+{P:c_wy})*coal_mult", "#,##0.0"),
        Col("coal_dom", "Coal mined at home (Mt)", "MIN({coal_pj}/coal_gj,{coal_cap},{coal_dom@p}*(1+coal_ramp)+1)", "#,##0.0",
            first="MIN({coal_pj}/coal_gj,{coal_cap})", note="Within the ceiling and the yearly ramp (coal_ramp, plus 1 Mt of slack)."),
        Col("wood_base", "Wood at the wanted shares (PJ)", f"{{{O}:f_rail}}*{{P:rail_wood}}+{{{O}:f_ind}}*{{P:ind_wood}}+{{{O}:f_bld}}*{{P:bld_wood}}", "#,##0.0",
            group="Wood and bagasse"),
        Col("wood_x", "Extra wood and mill waste in place of imported coal (PJ)", "MIN({coal_pj}-{coal_dom}*coal_gj,MAX(0,{P:wood_cap}-{wood_base}))", "#,##0.0"),
        Col("wood_pj", "Wood (PJ)", "{wood_base}+{wood_x}", "#,##0.0"),
        Col("coal_imp", "Coal imported (Mt)", "({coal_pj}-{wood_x})/coal_gj-{coal_dom}", "#,##0.0", kind="key", group="Coal imports"),
        Col("coal_imp_cap", "Coal the Realm can import (Mt)", "{P:coal_imp_cap}", "#,##0.0"),
        Col("coal_gap", "Coal beyond reach (Mt)", "MAX(0,{coal_imp}-{coal_imp_cap})", "#,##0.0", kind="key",
            note="Demand no supplier in reach can fill: the size of the canon tension (CR-052)."),
        Col("bag_pj", "Bagasse (PJ)", f"{{{O}:f_sugar}}", "#,##0.0"),
        Col("s_oil", "Oil", "({T}-{E})*6.12", "#,##0", group="Primary energy, supply side (PJ)"),
        Col("s_coal", "Coal", "{coal_pj}-{wood_x}", "#,##0"),
        Col("s_gas", "Gas", "{gas_used}", "#,##0"),
        Col("s_wood", "Wood and bagasse", "{wood_pj}+{bag_pj}", "#,##0"),
        Col("s_hydro", "Hydro", "{Electricity:pj_hydro}", "#,##0"),
        Col("s_atom", "Atomic", "{Electricity:pj_atom}", "#,##0"),
        Col("prim", "All primary energy", "{s_oil}+{s_coal}+{s_gas}+{s_wood}+{s_hydro}+{s_atom}", "#,##0", kind="key"),
        Col("mtoe", "All primary energy (Mtoe)", "{prim}/41.868", "#,##0.0"),
        Col("imp_sh", "Share of primary energy that would have to be imported", "IF({prim}>0,({imp}*6.12+{coal_imp}*coal_gj)/{prim},0)", "0%", kind="key"),
        Col("imp_sh2", "Share that can actually be imported", "IF({prim}>0,({imp}*6.12+MIN({coal_imp},{coal_imp_cap})*coal_gj)/{prim},0)", "0%", kind="key"),
        Col("gj_pp", "Per person (GJ)", "IF({People & output:pop_all}>0,{prim}*1000000/{People & output:pop_all},0)", "#,##0",
            group="Intensity"),
        Col("mj_d", "Per 1913 $ of real GDP (MJ)", "IF({People & output:gdp_real}>0,{prim}/{People & output:gdp_real}*1000,0)", "#,##0"),
        Col("us_mj_d", "US per 1913 $ (MJ)", "IF({People & output:us_real}>0,{People & output:us_pj}/{People & output:us_real}*1000,0)", "#,##0"),
        Col("int_ratio", "Energy per real $ vs US", "IF({us_mj_d}>0,{mj_d}/{us_mj_d},\"\")", "0.00", kind="key"),
    ]
    sheet("Fuels", "Fuels and the primary balance", "Oil, gas, coal, wood and bagasse: production, imports, exports and use; "
          "the primary-energy balance on the supply side; intensity against the US.", cols)


def spec_finance():
    cols = [
        Col("new_h", "New hydro (MW)", "MAX(0,{Electricity:hyd_cap}-{Electricity:hyd_cap@p})", first="{Electricity:hyd_cap}",
            group="Investment"),
        Col("new_t", "New steam (MW)", "MAX(0,{Electricity:th_cap}-{Electricity:th_cap@p})", first="{Electricity:th_cap}"),
        Col("stock", "Power plant stock (1913 $m)", "{stock@p}*(1-renewal)+{capex_r}", "#,##0",
            first="{capex_r}"),
        Col("capex_r", "Power investment (1913 $m)", "({new_h}*(cost_hydro+cost_td)+{new_t}*(cost_steam+cost_td))/1000+renewal*{stock@p}",
            "#,##0.0", first="({new_h}*(cost_hydro+cost_td)+{new_t}*(cost_steam+cost_td))/1000"),
        Col("capex", "Power investment ($m)", "{capex_r}*{People & output:price}", "#,##0.0", kind="key"),
        Col("capex_gdp", "Power investment / GDP", "IF({People & output:gdp}>0,{capex}/{People & output:gdp},0)", "0.0%"),
        Col("dev_want", "Development Fund's power credit wanted ($m)", "{capex}*dev_share", "#,##0.0"),
        Col("dev_credit", "Development Fund's power credit ($m)", "MIN({dev_want},df_max*MAX(0,{People & output:dev_inv}))", "#,##0.0",
            note="Capped at df_max of what the Fund invests that year (finance Debt & cash); the Fund never lends what it has not got."),
        Col("priv_fin", "Power investment financed outside the Fund ($m)", "{capex}-{dev_credit}", "#,##0.0",
            note="Utilities' bonds and shares, the champions' retained earnings, the Reserve Bank's lending in the slump."),
        Col("dev_sh", "… Fund credit as a share of the Fund's investment", "IF({People & output:dev_inv}>0,{dev_credit}/{People & output:dev_inv},\"\")", "0%"),
        Col("rev", "Electricity revenue, gross ($m)", "({Electricity:ord}*{P:el_price}+{Electricity:strat}*price_strat)/100*{People & output:price}",
            "#,##0.0", group="Revenue and royalties", note="All electricity valued at the average utility price, self-generation included."),
        Col("rev_self", "… of it self-generation valued at utility rates ($m)", "{rev}*self_gen", "#,##0.0",
            note="Industrial and electrochemical self-generation is not a utility sale; the financial workbook should count only rev_util as utility receipts."),
        Col("rev_util", "Utility receipts ($m)", "{rev}-{rev_self}", "#,##0.0", kind="key"),
        Col("rev_gdp", "Electricity revenue / GDP", "IF({People & output:gdp}>0,{rev}/{People & output:gdp},0)", "0.0%"),
        Col("roy", "Royalties to the compact peoples ($m)", "({Hydro:av_rock}+{Hydro:av_works})*roy_mill/1000*{People & output:price}", "#,##0.00",
            note="Rock Island (CR-051 S8 C2) and the Works' dams (R2, OPEN), on every kWh sold."),
        Col("v_imp", "Oil imported from the Gulf ($m)", "{Fuels:imp}*{People & output:oil_price}", "#,##0.0", group="Fuel trade"),
        Col("v_oexp", "Other crude exported ($m)", "{Fuels:oexp}*{People & output:oil_price}", "#,##0.0"),
        Col("v_asia", "Home oil sold in Asia ($m, memo: in finance)", "{Fuels:E}*{People & output:oil_price}", "#,##0.0"),
        Col("v_coal", "Coal imported ($m)", "{Fuels:coal_imp}*coal_price*{People & output:price}", "#,##0.0"),
        Col("x_oil", "Home oil above the finance workbook's path (m bbl)", "{Fuels:home}-{People & output:oil_out}", "#,##0.0",
            group="What the financial workbook would need", note="For its next build (CR-052 CT3 C)."),
        Col("x_oil_v", "… its value at the finance price ($m)", "{x_oil}*{People & output:oil_price}", "#,##0.0"),
        Col("x_veh", "Vehicles to build above the finance workbook's path (thousand)", "{Uses:veh_build}-{People & output:cars}", "#,##0"),
        Col("v_net", "Net fuel trade outside the finance workbook ($m)", "{v_oexp}-{v_imp}-{v_coal}", "#,##0.0", kind="key"),
    ]
    sheet("Finance link", "Link to the financial workbook", "What power costs and earns, and the fuel trade, in money. "
          "Named columns (en_*) are for the financial workbook's next build to read; nothing here is pasted into it.", cols)


CHECKS = [
    ("c1", "1. Supply = use", "IF(AND(ABS({Fuels:resid})<0.001,ABS({Uses:e_total}-{Electricity:ord}-{Electricity:strat})<0.01,"
     "ABS({Electricity:gen}-{Electricity:hyd}-{Electricity:th}-{Electricity:atom})<0.01,"
     "ABS({Fuels:prim}+{Fuels:bal_adj}-{Uses:use_pj})<=0.001*MAX(1,{Uses:use_pj})),1,0)"),
    ("c2", "2. Basins and lead times", "IF(AND({Hydro:u_max}<=1,{Hydro:lead_ok}=1),1,0)"),
    ("c3", "3. Oilfields", "IF(AND({Fuels:home}<={Fuels:cap_oil}+0.001,{Fuels:cum}<={Fuels:known},{Fuels:gas_yield}<={P:gas_yield}),1,0)"),
    ("c4", "4. Intensity bands", "IF(AND({Electricity:kwh_pp}<=kwh_max,OR({A}<1880,AND({Fuels:int_ratio}>=int_lo,{Fuels:int_ratio}<=int_hi))),1,0)"),
    ("c5", "5. Capacity factor, reserve, dry year", "IF(OR({Electricity:gen}=0,{A}<1900),1,IF(AND({Electricity:sys_cf}>=cf_lo,"
     "{Electricity:sys_cf}<=cf_hi,{Electricity:res}>=0.1,{Electricity:dry_ok}=1),1,0))"),
    ("c6", "6. Money", "IF(AND({Finance link:capex_gdp}<=capex_hi,{Finance link:dev_credit}<=df_max*MAX(0,{People & output:dev_inv})+0.001),1,0)"),
    ("c7", "7. Fuel imports within reach", "IF(AND({Fuels:imp}<={Fuels:imp_max}+0.001,{Fuels:coal_imp}<={Fuels:coal_imp_cap}+0.001),1,0)"),
    ("c8", "8. Navy and motor fuel", "IF(AND(ABS({Uses:f_navy_oil}-{People & output:navy_oil}*6.63)<0.0001,"
     "{Uses:veh}*1000<=veh_max*{People & output:pop_all}),1,0)"),
    ("c9", "9. Strategic loads powered", "IF(AND({Strategic loads:halls_gs}<=halls_grid_max,{Strategic loads:rock_spare}>=0,"
     "{Strategic loads:hilo_ok}=1),1,0)"),
    ("c10", "10. Fuel security", "IF(AND({Fuels:unmet_sh}<=unmet_max,{Fuels:coal_gap}<=0.001),1,0)"),
]


def spec_checks():
    cols = [Col(k, lab, tpl, "0", kind="check", width=10) for k, lab, tpl in CHECKS]
    cols.append(Col("all", "All pass", "*".join("{%s}" % k for k, *_ in CHECKS), "0", kind="check", width=9))
    parts = ",".join(f'IF({{{k}}}=0,"{lab.split(".")[0]}","")' for k, lab, _ in CHECKS)
    cols.append(Col("prob", "Problems this year (test numbers)", f'_xlfn.TEXTJOIN(", ",TRUE,{parts})', "@", width=28))
    sheet("Checks", "Checks", "One column per test in the handoff's §7 (1 = pass, 0 = fail), and the failing tests by year.", cols)


# ------------------------------------------------------------------ writers
def style_head(ws, r, c, text, comment=None, width=None):
    cell = ws.cell(r, c, text)
    cell.font = F_HEAD
    cell.fill = FILL_HEAD
    cell.alignment = WRAP
    if comment:
        cell.comment = Comment(comment, "energy build")
    if width:
        ws.column_dimensions[get_column_letter(c)].width = width


def write_years(ws):
    ws.cell(5, 1, "Year").font = F_HEAD
    ws.cell(5, 1).fill = FILL_HEAD
    for y in YEARS:
        ws.cell(row(y), 1, y).font = F_HEAD
    ws.column_dimensions["A"].width = 7
    ws.freeze_panes = "B6"


def write_title(ws, title, desc):
    ws["A1"] = title
    ws["A1"].font = F_TITLE
    ws["A2"] = desc
    ws["A2"].font = F_NOTE
    ws["A3"] = ("Years run down the page. Blue = input · black = formula · green = link to another sheet · "
                "red = value imported from the financial workbook. Hover a column heading for its basis. All results MODEL.")
    ws["A3"].font = F_NOTE


def write_yearly(wb, name, fin=None, fin_meta=None):
    spec = SHEETS[name]
    ws = wb.create_sheet(name)
    write_title(ws, spec["title"], spec["desc"])
    write_years(ws)
    for c in spec["cols"]:
        ci = openpyxl.utils.column_index_from_string(c.letter)
        header = c.header
        if header is None and fin_meta is not None:
            base = c.key[:-2] if c.key.endswith(("_s", "_t")) else c.key
            label, unit = fin_meta[base]
            suffix = " · Story" if c.key.endswith("_s") else " · Stress" if c.key.endswith("_t") else ""
            header = f"{label.split(' (')[0]} ({unit}){suffix}"
            c.note = c.note or f"From the financial workbook, {label.split('(')[-1].rstrip(')')}."
        style_head(ws, 5, ci, header, c.note or None, width=c.width if c.kind != "check" else 10)
        if c.group:
            g = ws.cell(4, ci, c.group)
            g.font = F_HEAD
        for y in YEARS:
            r = row(y)
            cell = ws.cell(r, ci)
            if c.kind == "ext":
                base, case = c.key[:-2], ("story" if c.key.endswith("_s") else "stress")
                cell.value = round(fin[(base, case)][y - Y0], 6)
                cell.font = F_EXT
            else:
                tpl = c.first if (y == Y0 and c.first) else c.tpl
                cell.value = render(tpl, name, r)
                cell.font = F_LINK if c.kind == "link" else F_CALC
                if c.kind == "key":
                    cell.fill = FILL_KEY
            cell.number_format = c.fmt
        if c.kind == "check":
            rng = f"{c.letter}{FIRST}:{c.letter}{LAST}"
            if c.key != "prob":
                ws.conditional_formatting.add(rng, CellIsRule(operator="equal", formula=["0"], fill=FILL_FAIL))
                ws.conditional_formatting.add(rng, CellIsRule(operator="equal", formula=["1"], fill=FILL_PASS))
    ws.row_dimensions[5].height = 60
    return ws


def write_levers(wb):
    ws = wb.create_sheet("Levers")
    ws["A1"] = "Energy levers"
    ws["A1"].font = F_TITLE
    ws["A2"] = ("Every scalar assumption in one place. Pick the case in E4: it switches every lever and also which of the "
                "financial workbook's two cases feeds People & output (the Max case uses the Story values).")
    ws["A2"].font = F_NOTE
    ws["A3"] = "Blue = input · the Active column feeds the model through the named range in column J."
    ws["A3"].font = F_NOTE
    ws["B4"] = "Case in use (1 = Story, 2 = Stress, 3 = Max)"
    ws["B4"].font = F_HEAD
    ws["E4"] = 1
    ws["E4"].font = F_IN
    ws["E4"].fill = FILL_KEY
    ws["F4"] = '=CHOOSE(E4,"Story case","Stress case","Max case")'
    wb.defined_names["case_sel"] = DefinedName("case_sel", attr_text="Levers!$E$4")
    for i, h in enumerate(["Lever", "Story case", "Stress case", "Max case", "Active", "Unit", "Status", "Basis and notes", "Name"], start=2):
        style_head(ws, 6, i, h)
    r = 7
    for lv in LEVERS:
        if len(lv) == 1:
            ws.cell(r, 2, lv[0]).font = F_HEAD
            r += 1
            continue
        name, label, st, sx, unit, status, basis = lv
        mx = I.MAX.get(name, st)
        if name in I.MAX_NOTES:
            basis = (basis + " " + I.MAX_NOTES[name]).strip()
        ws.cell(r, 2, label).font = F_CALC
        ws.cell(r, 3, st).font = F_IN
        ws.cell(r, 4, sx).font = F_IN
        ws.cell(r, 5, mx).font = F_IN
        if mx != st:
            ws.cell(r, 5).fill = FILL_KEY
        ws.cell(r, 6, f"=CHOOSE(case_sel,C{r},D{r},E{r})").font = F_CALC
        ws.cell(r, 7, unit)
        ws.cell(r, 8, status)
        ws.cell(r, 9, basis).alignment = WRAP
        ws.cell(r, 10, name).font = F_NOTE
        if "OPEN" in status:
            ws.cell(r, 8).fill = FILL_KEY
        wb.defined_names[name] = DefinedName(name, attr_text=f"Levers!$F${r}")
        r += 1
    for col, w in zip("ABCDEFGHIJ", [3, 58, 10, 10, 10, 10, 20, 22, 80, 14]):
        ws.column_dimensions[col].width = w
    ws.freeze_panes = "C7"


def fill_points(points: dict, years: list[int]) -> dict:
    ks = sorted(points)
    out = {}
    for y in years:
        if y in points:
            out[y] = (points[y], True)
        elif y < ks[0]:
            out[y] = (points[ks[0]], False)
        elif y > ks[-1]:
            out[y] = (points[ks[-1]], False)
        else:
            lo = max(k for k in ks if k < y)
            hi = min(k for k in ks if k > y)
            out[y] = (points[lo] + (y - lo) * (points[hi] - points[lo]) / (hi - lo), False)
    return out


def write_paths(wb):
    global PATH_COLS
    ws = wb.create_sheet("Paths")
    ws["A1"] = "Paths"
    ws["A1"].font = F_TITLE
    ws["A2"] = ("Story-case inputs at benchmark years; the yearly sheets interpolate linearly between them by formula. "
                "Bold blue = value set by the author or the builder; pale italic = filled in between, edit freely.")
    ws["A2"].font = F_NOTE
    years = sorted(set(I.PATH_YEARS) | {y for v in I.PATHS.values() for y in v[2] if Y0 <= y <= Y1}
                   | {y for v in I.PATHS_MAX.values() for y in v if Y0 <= y <= Y1})
    for i, h in enumerate(["Key", "Series", "Unit"], start=1):
        style_head(ws, 5, i, h)
    c0 = 4
    for j, y in enumerate(years):
        style_head(ws, 5, c0 + j, y)
    a, b = get_column_letter(c0), get_column_letter(c0 + len(years) - 1)
    PATH_COLS = (a, b)
    cb, cs = c0 + len(years), c0 + len(years) + 1
    style_head(ws, 5, cb, "Basis")
    style_head(ws, 5, cs, "Status")
    r = 6
    for key, (label, unit, points, basis, status) in I.PATHS.items():
        PATH_ROW[key] = r
        ws.cell(r, 1, key).font = F_NOTE
        ws.cell(r, 2, label)
        ws.cell(r, 3, unit)
        # beyond-1932 points still shape the 1932 value
        filled = fill_points(points, years)
        for j, y in enumerate(years):
            v, given = filled[y]
            cell = ws.cell(r, c0 + j, round(v, 6))
            cell.font = Font(name=FONT, color="0000FF", bold=True) if given else F_IN_FILL
            cell.number_format = "General"
        ws.cell(r, cb, basis).alignment = Alignment(vertical="top")
        ws.cell(r, cs, status)
        r += 1
    r += 1
    ws.cell(r, 2, "Max case (used when Levers!E4 = 3; other series take their Story path)").font = F_HEAD
    r += 1
    for key, points in I.PATHS_MAX.items():
        label, unit = I.PATHS[key][0], I.PATHS[key][1]
        PATH_ROW[key + "__max"] = r
        ws.cell(r, 1, key + "__max").font = F_NOTE
        ws.cell(r, 2, label + " (Max)")
        ws.cell(r, 3, unit)
        filled = fill_points(points, years)
        for j, y in enumerate(years):
            v, given = filled[y]
            cell = ws.cell(r, c0 + j, round(v, 6))
            cell.font = Font(name=FONT, color="0000FF", bold=True) if given else F_IN_FILL
        ws.cell(r, cb, I.MAX_BASIS).alignment = Alignment(vertical="top")
        ws.cell(r, cs, "Max case")
        r += 1
    ws.column_dimensions["A"].width = 11
    ws.column_dimensions["B"].width = 52
    ws.column_dimensions["C"].width = 14
    for j in range(len(years)):
        ws.column_dimensions[get_column_letter(c0 + j)].width = 8
    ws.column_dimensions[get_column_letter(cb)].width = 90
    ws.freeze_panes = "D6"


def write_anchors(wb):
    global US_COLS
    ws = wb.create_sheet("Anchors")
    ws["A1"] = "Historical anchors (outside the texts)"
    ws["A1"].font = F_TITLE
    ws["A2"] = ("Real historical data with a source and status for every value. VERIFIED = read from the source in the building "
                "session; CARRIED = verified earlier and cited in a project document; TO VERIFY = recalled from the standard "
                "series because the primary table could not be reached. The first table feeds the US comparison by formula.")
    ws["A2"].font = F_NOTE
    ws["A4"] = "A. United States series used by formula (interpolated between the years shown)"
    ws["A4"].font = F_HEAD
    for i, h in enumerate(["Key", "Series", "Unit"], start=1):
        style_head(ws, 6, i, h)
    c0 = 4
    for j, y in enumerate(I.US_YEARS):
        style_head(ws, 6, c0 + j, y)
    a, b = get_column_letter(c0), get_column_letter(c0 + len(I.US_YEARS) - 1)
    US_COLS = (a, b)
    cs = c0 + len(I.US_YEARS)
    style_head(ws, 6, cs, "Source")
    style_head(ws, 6, cs + 1, "Status")
    r = 7
    for key, label, unit, vals, src, status in I.US_SERIES:
        US_ROW[key] = r
        ws.cell(r, 1, key).font = F_NOTE
        ws.cell(r, 2, label)
        ws.cell(r, 3, unit)
        for j, v in enumerate(vals):
            ws.cell(r, c0 + j, v).font = F_IN
        ws.cell(r, cs, src)
        ws.cell(r, cs + 1, status)
        r += 1
    r += 2
    ws.cell(r, 1, "B. All anchors").font = F_HEAD
    r += 1
    for i, h in enumerate(["Region", "Series", "Unit", "Year", "Value", "Source", "Status"], start=1):
        style_head(ws, r, i, h)
    r += 1
    for reg, ser, unit, y, v, src, st in I.ANCHOR_FACTS:
        for i, val in enumerate([reg, ser, unit, y, v, src, st], start=1):
            cell = ws.cell(r, i, val)
            if i == 5:
                cell.font = F_IN
        r += 1
    ws.column_dimensions["A"].width = 12
    ws.column_dimensions["B"].width = 46
    ws.column_dimensions["C"].width = 16
    for j in range(len(I.US_YEARS)):
        ws.column_dimensions[get_column_letter(c0 + j)].width = 9
    ws.column_dimensions["F"].width = 14
    ws.column_dimensions[get_column_letter(cs)].width = 60


def write_events(wb):
    ws = wb.create_sheet("Events")
    ws["A1"] = "Events"
    ws["A1"].font = F_TITLE
    ws["A2"] = "Dated canon commitments the energy model serves, with where they show and their status."
    ws["A2"].font = F_NOTE
    for i, h in enumerate(["Year", "Event", "Where in this workbook", "Section or CR", "Status"], start=1):
        style_head(ws, 5, i, h)
    for r, ev in enumerate(I.EVENTS, start=6):
        for i, v in enumerate(ev, start=1):
            ws.cell(r, i, v)
    for col, w in zip("ABCDE", [7, 70, 42, 26, 24]):
        ws.column_dimensions[col].width = w


def write_register(wb):
    ws = wb["Strategic loads"]
    c0 = openpyxl.utils.column_index_from_string(SHEETS["Strategic loads"]["cols"][-1].letter) + 2
    style_head(ws, 4, c0, "Register of strategic loads")
    heads = ["Load", "Years", "Source of power", "CR", "Status"]
    for i, h in enumerate(heads):
        style_head(ws, 5, c0 + i, h)
    reg = [
        ("Separation halls", "1919–1932", "Arc plants' freed power (1919–21), then the Works' dams on the Pit and upper Feather; remainder from the grid", "CR-051 M2, R1, R2", "APPROVED; figures MODEL"),
        ("Feed plant (thermal diffusion)", "1921–1932", "Its own oil-fired steam plant", "CR-051 M1, M2", "APPROVED; MODEL"),
        ("Columbia station", "1923–1932", "Rock Island dam; Roslyn-coal steam plant as second supply", "CR-051 S7, S8", "APPROVED"),
        ("Walled college and Tuolumne Station", "1911–1932", "Eleanor–Cherry system", "CR-050, CR-051 C2", "CANON; MODEL"),
        ("Arc nitrogen plants", "1908–1929", "Sierra hydro (Pit and Feather, Sierra west slope)", "Ledger K11; CR-051 R1", "CANON; end date OPEN"),
        ("Aluminium: Sierra", "1895–1932", "Sierra hydro", "Ledger K9", "CANON"),
        ("Aluminium: Columbia and Wenatchee", "1907–1932", "Columbia hydro; Rock Island for Wenatchee", "Ledger K9; CR-051 S7", "CANON"),
        ("Aluminium: Hilo", "1925–1932", "The Hawaiian hydro board's Big Island plants (Paths h_hilo; hilo_src = 2)", "Ledger I13, L14; CR-052 CT6", "APPROVED (CT6, 4 Nov 2026)"),
        ("The navy", "1882–1932", "Oil from the home fields and the Gulf", "CR-020 B1", "CANON"),
        ("The canal (memo)", "1900–1932", "Gatun hydro, outside the Realm", "Canon", "CANON"),
    ]
    for j, rg in enumerate(reg, start=6):
        for i, v in enumerate(rg):
            ws.cell(j, c0 + i, v).alignment = WRAP
    for i, w in enumerate([30, 11, 48, 20, 20]):
        ws.column_dimensions[get_column_letter(c0 + i)].width = w


def write_start(wb, sha):
    ws = wb["Start"]
    ws["A1"] = "Pacifica energy workbook, 1846–1932"
    ws["A1"].font = F_TITLE
    lines = [
        "Purpose: track every source of power in the Realm and Hawaii and what it is used for, and tie both to the financial workbook. "
        "Its main job is to make the multiplier of Pacifica's electricity per person against the United States an output, built from sources and uses.",
        "Territory: the Realm's counties and Hawaii. Partners and assets abroad count only through trade (oil from the Gulf, oil sold in Asia).",
        "Two layers: primary energy (PJ, with Mtoe) and electricity (MW, GWh). Hydro and atomic power count at their fossil-fuel equivalent, as in the US historical series.",
        "Case: Levers!E4 (1 = Story, 2 = Stress, 3 = Max) switches every lever and picks which of the financial workbook's cases feeds People & output. Max = every source Pacifica can reach and every use that can absorb it, on the Story finance drivers (CR-052, exploration).",
        f"Financial workbook imported: SHA-256 {sha}. Rebuild with energy/build/ when that workbook changes (see energy/README.md).",
        "Conventions: years down the page (row 6 = 1846, row 92 = 1932); blue input, black formula, green link, red imported from finance; yellow = key result. All results MODEL.",
    ]
    for i, t in enumerate(lines, start=2):
        ws.cell(i, 1, t).font = F_NOTE
    ws["A9"] = "Case in use:"
    ws["A9"].font = F_HEAD
    ws["C9"] = "=Levers!F4"
    ws["C9"].font = F_LINK
    ws["A10"] = "Years failing at least one check:"
    ws["A10"].font = F_HEAD
    ws["C10"] = f"=COUNTIF(Checks!{LETTER[('Checks', 'all')]}{FIRST}:{LETTER[('Checks', 'all')]}{LAST},0)"
    ws["C10"].fill = FILL_KEY
    # key results
    bench = [1860, 1880, 1900, 1913, 1920, 1922, 1924, 1927, 1929, 1932]
    r0 = 12
    style_head(ws, r0, 1, "Key results")
    style_head(ws, r0, 2, "Unit")
    for j, y in enumerate(bench):
        style_head(ws, r0, 3 + j, y)
    E = "Electricity"
    items = [
        ("Everyone present", "m", "{%s:pop_all}/1000000" % PO, "0.0"),
        ("Real GDP", "1913 $bn", "{%s:gdp_real}/1000" % PO, "0.0"),
        ("Generating capacity", "GW", "{%s:cap}/1000" % E, "0.00"),
        ("… hydro", "GW", "{%s:hyd_cap}/1000" % E, "0.00"),
        ("Generation", "TWh", "{%s:gen}/1000" % E, "0.0"),
        ("Hydro share of generation", "share", "{%s:hydro_share}" % E, "0%"),
        ("Electricity per person", "kWh", "{%s:kwh_pp}" % E, "#,##0"),
        ("Multiplier: capacity per person vs US utilities", "×", "{%s:mult_cap}" % E, "0.00"),
        ("Multiplier: electricity per person vs US", "×", "{%s:mult_gen}" % E, "0.00"),
        ("Halls' draw", "MW", "{Strategic loads:halls_mw}", "#,##0"),
        ("Halls / capacity", "share", "{%s:halls_cap}" % E, "0.0%"),
        ("Halls / electricity used", "share", "{%s:halls_el}" % E, "0.0%"),
        ("Halls from the common grid", "MW avg", "{Strategic loads:halls_grid}", "#,##0"),
        ("Primary energy", "PJ", "{Fuels:prim}", "#,##0"),
        ("Primary energy", "Mtoe", "{Fuels:mtoe}", "#,##0.0"),
        ("Primary energy per person", "GJ", "{Fuels:gj_pp}", "#,##0"),
        ("Energy per real $ vs US", "×", "{Fuels:int_ratio}", "0.00"),
        ("Home oil output", "m bbl", "{Fuels:home}", "#,##0"),
        ("Oil imported from the Gulf", "m bbl", "{Fuels:imp}", "#,##0"),
        ("Coal imported", "Mt", "{Fuels:coal_imp}", "#,##0.0"),
        ("Coal beyond reach", "Mt", "{Fuels:coal_gap}", "#,##0.0"),
        ("Oil for railways, industry and power: share of wanted", "share", "{Fuels:k}", "0%"),
        ("Share of primary energy that would have to be imported", "share", "{Fuels:imp_sh}", "0%"),
        ("Oil demand left unmet (real curtailment)", "PJ", "{Fuels:unmet}", "#,##0.0"),
        ("Motor fuel rationed", "PJ", "{Fuels:mf_cutp}", "#,##0.0"),
        ("Asian exports deferred", "m bbl", "{Fuels:exp_cutp}/6.12", "#,##0.0"),
        ("Oil stocks at year end", "days", "{Fuels:stk_days}", "0"),
        ("… that can actually be imported", "share", "{Fuels:imp_sh2}", "0%"),
        ("Motor vehicles per person", "per person", "{Uses:veh_pp}", "0.00"),
        ("… California (memo)", "per person", "{Uses:veh_cal}", "0.00"),
        ("Vehicles to build a year", "thousand", "{Uses:veh_build}", "#,##0"),
        ("Home oil above the finance workbook's path", "m bbl", "{Finance link:x_oil}", "#,##0"),
        ("Northwest hydro beyond its own load (spilled)", "TWh", "{Electricity:stranded}/1000", "#,##0.0"),
        ("Power investment", "$m", "{Finance link:capex}", "#,##0"),
        ("Power investment / GDP", "share", "{Finance link:capex_gdp}", "0.0%"),
        ("Checks failing this year", "tests", "{Checks:prob}", "@"),
    ]
    for i, (lab, unit, tpl, fmt) in enumerate(items, start=r0 + 1):
        ws.cell(i, 1, lab)
        ws.cell(i, 2, unit)
        for j, y in enumerate(bench):
            cell = ws.cell(i, 3 + j, render(tpl, "Start", row(y)))
            cell.font = F_LINK
            cell.number_format = fmt
    r = r0 + len(items) + 3
    ws.cell(r, 1, "Sheets").font = F_HEAD
    guide = [
        ("Levers", "Scalar assumptions, Story and Stress, with named ranges; the case switch."),
        ("Paths", "Benchmark-year inputs (intensities, shares, capacities by basin), interpolated by formula."),
        ("Anchors", "Historical data with source and status."),
        ("People & output", "Population, GDP and industry from the financial workbook, both cases."),
        ("Hydro", "Capacity and output by river basin; strategic dams; potential and lead times."),
        ("Strategic loads", "The halls, the feed plant, the Columbia station, the valley, Hilo; register of sources."),
        ("Uses", "Electricity and fuel by sector."),
        ("Electricity", "Generation, capacity, losses, reserve, the dry-year test, the multiplier against the US."),
        ("Fuels", "Oil, gas, coal, wood and bagasse balances; primary energy; intensity."),
        ("Finance link", "Investment, revenue, royalties and fuel trade in money; named columns en_*."),
        ("Events", "Dated canon commitments."),
        ("Checks", "The nine tests of the handoff's §7 and the fuel-security test, year by year."),
        ("Changes", "Revision history."),
    ]
    for i, (s, d) in enumerate(guide, start=r + 1):
        ws.cell(i, 1, s).font = F_HEAD
        ws.cell(i, 2, d)
    r = r + len(guide) + 2
    ws.cell(r, 1, "Open questions carried as switches (handoff §8)").font = F_HEAD
    opens = [
        "Hetch Hetchy: the valley is the college; San Francisco's water and the valley's power come from the Eleanor–Cherry system (CR-051 C2). No switch needed.",
        "Big dams earlier (4 Nov 2026): Boulder Canyon decided 1920, first power 1926 (Story and Max; Stress keeps 1928); Rock Island as canon (1920–23); the mid-Columbia chain is off in every case (CR-051 S7). No early Grand Coulee.",
        "Main-line railway electrification: mainline_on (Story 1 with half the traffic by 1929 since 4 Nov 2026; Stress 0; Max 1).",
        "Oil abroad (CR-053, PROPOSED): entitlement crude from the Maracaibo, De Mares and Peruvian positions and the Gulf-coast options is added to the import ceiling (Paths conc_*, Fuels conc).",
        "Oil (approved CT3 A–C): Realm coal at 4×, all Gulf crude home, home oil on the discovery path oil_c52 (oil_src = 2). Motor vehicles per person (veh_src = 2) so that California is the most motorized place on earth.",
        "Hawaii (CT6, approved 4 Nov 2026): hilo_src = 2, the Hawaiian hydro board's Big Island plants (Paths h_hilo) carry the smelter; 1 = oil-fired steam (superseded).",
        "Fuel security (4 Nov 2026): in a short year the model draws stocks (stock_days), defers Asian exports (exp_cut), rations motor fuel (mf_cut), switches coal-capable plant (Paths dual_share × dual_x) and only then leaves demand unmet (Fuels unmet; check 10). Realm coal rises at most coal_ramp a year. The 1932 compact is a price floor unless compact_on = 1.",
        "Nitrogen after 1919: the arc runs to 1928–29 then stops (Paths arc_kt); Haber–Bosch from 1925 (Paths haber_kt).",
        "The Five's power seat: the Electricity sheet shows what that seat oversees (capacity, generation, investment).",
        "Native consent for every new dam: the royalty lever roy_mill applies to Rock Island and the Works' dams; other basins carry no compact yet.",
        "Halls after 1927 (halls_after, OPEN) and the Development Fund's share of power investment (dev_share, OPEN).",
    ]
    for i, t in enumerate(opens, start=r + 1):
        ws.cell(i, 1, t)
    ws.column_dimensions["A"].width = 44
    ws.column_dimensions["B"].width = 12
    for j in range(len(bench)):
        ws.column_dimensions[get_column_letter(3 + j)].width = 11


def write_changes(wb, sha):
    ws = wb.create_sheet("Changes")
    ws["A1"] = "Changes"
    ws["A1"].font = F_TITLE
    for i, h in enumerate(["Date", "CR", "Change", "Built from"], start=1):
        style_head(ws, 4, i, h)
    ws.append(["2026-11-03", "CR-052", "First build: fourteen sheets per the energy-workbook handoff; anchors; nine checks. Second build after the fresh-context review: one industrial weight (ind_w) for motors and fuel; mid-Columbia chain off; Boulder at historical dates. Third build: the author's sources (1917 Census of Electrical Industries, Devine 1983, Minerals Yearbook 1932); CT3 A–C and CT5 approved into the Story case; the Max case. Fourth build: field-by-field oil model; Northwest surplus spilled; Max after 1915 only.",
               f"finance SHA-256 {sha[:16]}…; energy/build/build_energy_workbook.py"])
    ws.append(["2026-11-04", "CR-052, CR-053", "Fifth build: the narrowed Max case into Story (M1 electric homes, M6 half the main lines, M7 Boulder 1920/1926 without the mid-Columbia chain, M8 early water flooding, M9 Northwest mill boilers); the chain off in every case; CR-053 concession crude (conc_*) added to the import ceiling.",
               f"finance SHA-256 {sha[:16]}…; energy/build/build_energy_workbook.py"])
    ws.append(["2026-11-04", "CR-052", "Sixth build: fuel security (stocks, export deferral and motor-fuel rationing before the switch to coal; a dual-fuel share, with the rest shown as unmet demand; a yearly ramp on Realm coal; the 1932 compact as a price floor; check 10); CT6, Hilo on the Hawaiian hydro board's Big Island plants.",
               f"finance SHA-256 {sha[:16]}…; energy/build/build_energy_workbook.py"])
    ws.append(["2026-11-04", "CR-052", "Seventh build (after Sol's review of the finance note): the Max case's electrified process heat is its own switch (heat_el) and no longer stacks on the industrial weight; a finance calibration hook (Paths ind_idx) scales ind_w and ind_mj together; the Development Fund's power credit is capped at the Fund's capacity, the remainder shown as privately financed (en_power_capex_private), and check 6 no longer waives the Fund test; electricity revenue split into utility receipts and self-generation (en_elec_revenue_utility, en_elec_revenue_selfgen). Results unchanged.",
               f"finance SHA-256 {sha[:16]}…; energy/build/build_energy_workbook.py"])
    ws.append(["2026-11-04", "CR-054", "Eighth build: the energy-intensive champions reworked — aluminium about 150 kt in 1929 (Columbia 70, Sierra 60, Hilo 18) with its uses as a memo (grid conductor, the fleet's aircraft, the Concord pool, civil, export); electrolytic ammonia 60 kt N on the Columbia from 1925 beside 30 kt N of Haber–Bosch on Valley gas; electric steel 12%; other electrochemistry × 1.2.",
               f"finance SHA-256 {sha[:16]}…; energy/build/build_energy_workbook.py"])
    ws.append(["2026-11-04", "CR-055", "Ninth build: the Columbia built early and its power used (CR-055 R0) — Bonneville 1908/1913 (500 MW), Rocky Reach 1914/1919 (800), Wells 1921/1926 (600), all laddered; electrolytic zinc at Spokane from 1908, magnesium from Great Salt Lake brine from 1909 and seawater at Tacoma from 1924, ammonia on the Columbia's cells from 1915 (heavy water found 1916–17), furnace phosphorus on the upper Snake from 1915, electrolytic copper refining from 1905; the new loads in the Northwest balance and the interruptible set.",
               f"finance SHA-256 {sha[:16]}…; energy/build/build_energy_workbook.py"])
    for col, w in zip("ABCD", [12, 10, 80, 60]):
        ws.column_dimensions[col].width = w


def add_named_columns(wb):
    for key, name in [("capex", "en_power_capex"), ("dev_credit", "en_dev_power_credit"), ("rev", "en_elec_revenue"),
                      ("roy", "en_royalties"), ("v_imp", "en_oil_import_value"), ("v_coal", "en_coal_import_value"),
                      ("v_net", "en_fuel_trade_net"), ("priv_fin", "en_power_capex_private"), ("rev_util", "en_elec_revenue_utility"),
                      ("rev_self", "en_elec_revenue_selfgen")]:
        L = LETTER[("Finance link", key)]
        wb.defined_names[name] = DefinedName(name, attr_text=f"'Finance link'!${L}${FIRST}:${L}${LAST}")


def main():
    fin_csv, out = Path(sys.argv[1]), Path(sys.argv[2])
    sha, fin, meta = load_finance(fin_csv)
    wb = openpyxl.Workbook()
    wb.active.title = "Start"
    write_levers(wb)
    write_paths(wb)
    write_anchors(wb)
    spec_people(); spec_hydro(); spec_strategic(); spec_uses(); spec_electricity(); spec_fuels(); spec_finance(); spec_checks()
    # arc_peak needs an absolute range on its own sheet
    for c in SHEETS["Strategic loads"]["cols"]:
        if c.key == "arc_peak":
            L = LETTER[("Strategic loads", "arc_mw")]
            c.tpl = f"MAX(${L}${FIRST}:${L}${row(1918)})"
    write_yearly(wb, PO, fin, meta)
    for name in ["Hydro", "Strategic loads", "Uses", "Electricity", "Fuels", "Finance link", "Checks"]:
        write_yearly(wb, name)
    write_register(wb)
    write_events(wb)
    write_changes(wb, sha)
    write_start(wb, sha)
    add_named_columns(wb)
    order = ["Start", "Levers", "Anchors", "Paths", PO, "Hydro", "Strategic loads", "Uses", "Electricity", "Fuels",
             "Finance link", "Events", "Checks", "Changes"]
    wb._sheets = [wb[n] for n in order]
    for ws in wb.worksheets:
        for rw in ws.iter_rows():
            for cell in rw:
                if cell.font and cell.font.name != FONT:
                    f = cell.font
                    cell.font = Font(name=FONT, bold=f.bold, italic=f.italic, color=f.color, size=f.size)
    wb.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
