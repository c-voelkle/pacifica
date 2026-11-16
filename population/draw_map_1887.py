"""Draw the 124 counties of 1887 (CR-071 Part I) from the Newberry atlas's geometry.

    python3 population/draw_map_1887.py /path/to/county-boundaries-topology/output
        -> population/outputs/map_1887.png

The geometry is not in this repository. It is the CC0 conversion of the Atlas of Historical
County Boundaries at https://github.com/localgeohistoryproject/county-boundaries-topology
(folder `output`: output_counties_metadata.csv, output_counties_ways.csv, output_ways.shp).
Needs shapely, pyshp and matplotlib.

What the picture is and is not: each new county is the union of our timeline's counties of
1 August 1887 named in data/counties/map_1887.toml. Where a historical county is divided between
two new ones, the cut is a straight line chosen by eye (CUTS below). The homelands' outlines are
rough sketches from Part I's verbal lines, not surveyed boundaries. MODEL and PROPOSED throughout.
"""
from __future__ import annotations

import csv
import json
import math
import sys
import tomllib
from collections import defaultdict
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.patheffects as pe
import matplotlib.pyplot as plt
import shapefile
from matplotlib.patches import PathPatch
from matplotlib.path import Path as MPath
from shapely.geometry import LineString, Point, Polygon, box, shape
from shapely.ops import nearest_points, polylabel
from shapely.ops import polygonize, unary_union
import numpy as np
import shapely

HERE = Path(__file__).parent
DATA = HERE / "data" / "counties"
DAY = 18870801

# historical county -> [(new county, lon_min, lat_min, lon_max, lat_max)], the rest stays with the
# new county that holds the largest fraction in map_1887.toml. Lines chosen by eye.
CUTS = {
    "UT;Salt Lake": [("Jordan", -113.0, 40.0, -111.0, 40.69)],
    "UT;Box Elder": [("Bear River", -112.45, 41.62, -111.0, 42.1)],
    "CA;Solano": [("Suisun", -122.12, 38.17, -121.0, 39.0)],
    "CA;Contra Costa": [("Carquinez", -122.5, 37.97, -122.02, 38.2)],
    "CA;Los Angeles": [("Santa Ana", -118.12, 33.2, -117.3, 33.95)],
    "CA;San Bernardino": [("Mojave", -118.0, 34.55, -114.0, 36.0)],
    "NM;Lincoln": [("Mesilla", -106.6, 32.0, -105.85, 34.3)],
    "NM;Bernalillo": [("Little Colorado", -109.2, 34.9, -108.2, 35.75)],
    "NV;Lander": [("Elko", -118.0, 40.0, -116.0, 41.1)],
    "AZ;Mohave": [("Virgin", -114.2, 36.2, -112.0, 37.1)],
    "AZ;Yavapai": [("Coconino", -114.0, 35.0, -110.6, 37.1)],
}
# the homelands' sketched lines and the enclaves' places: data/counties/homelands_1887.toml
# where a county's detached remainder should go when the longest shared line is a mountain crest
PREFER = {"Spokane": "Big Bend"}
UNIT_COLOUR = {"California": "#f3d9a4", "Oregon": "#b9d8b0", "Columbia": "#a9cfe0", "Deseret": "#e6c3d6",
               "New Mexico": "#f2b8a0", "Idaho": "#d5d0ea", "Arizona": "#f6e39a", "Washoe": "#d9d9c3",
               "The Rockies": "#c9b79c", "Hawaii": "#b6e0d4", "Western Montana": "#c7dcef", "Baja": "#f0cfa0",
               "Thalassia": "#e86f5a"}


def albers(lon, lat, z=None, lon0=-114.0, lat0=38.0, p1=30.0, p2=46.0):
    r = math.radians
    n = (math.sin(r(p1)) + math.sin(r(p2))) / 2
    c = math.cos(r(p1)) ** 2 + 2 * n * math.sin(r(p1))
    rho0 = math.sqrt(c - 2 * n * math.sin(r(lat0))) / n
    if isinstance(lon, (int, float)):
        lon, lat = [lon], [lat]
    xs, ys = [], []
    for lo, la in zip(lon, lat):
        rho = math.sqrt(c - 2 * n * math.sin(r(la))) / n
        th = n * r(lo - lon0)
        xs.append(rho * math.sin(th))
        ys.append(rho0 - rho * math.cos(th))
    return (xs[0], ys[0]) if len(xs) == 1 else (xs, ys)


def load_geometry(topo: Path, wanted: dict[str, str], extra_ids: dict[str, str]):
    """wanted: key -> newberry id (version valid on DAY); extra_ids: key -> id_num (fixed versions)."""
    id_num = {}
    for r in csv.DictReader(open(topo / "output_counties_metadata.csv", encoding="utf-8")):
        if int(r["start_n"]) <= DAY <= int(r["end_n"]):
            for k, nid in wanted.items():
                if r["id"] == nid:
                    id_num[r["id_num"]] = k
    for k, n in extra_ids.items():
        id_num[n] = k
    edges = defaultdict(lambda: {"outer": [], "inner": []})
    for r in csv.DictReader(open(topo / "output_counties_ways.csv")):
        if r["id_num"] in id_num:
            edges[id_num[r["id_num"]]]["inner" if r["edge_type"] == "inner" else "outer"].append(int(r["edge_id"]))
    sf = shapefile.Reader(str(topo / "output_ways"))
    need = {e for v in edges.values() for t in v.values() for e in t}
    lines = {}
    for i, rec in enumerate(sf.iterRecords()):
        if rec[0] in need:
            shp = sf.shape(i)
            parts = list(shp.parts) + [len(shp.points)]
            lines[rec[0]] = [LineString(shp.points[a:b]) for a, b in zip(parts, parts[1:]) if b - a > 1]
    geom = {}
    for k, v in edges.items():
        outer = unary_union(list(polygonize([l for e in v["outer"] for l in lines.get(e, [])])))
        inner = unary_union(list(polygonize([l for e in v["inner"] for l in lines.get(e, [])]))) if v["inner"] else None
        geom[k] = outer.difference(inner) if inner is not None and not inner.is_empty else outer
    return geom


def colville(data: Path):
    """The ground between the Columbia and the Okanogan south of 49 N, from river centre lines."""
    riv = json.load(open(data / "rivers_colville.geojson"))
    lines = [shape(f["geometry"]) for f in riv["features"]]
    lines.append(LineString([(-120.2, 49.0), (-117.0, 49.0)]))
    col = unary_union([l for l, f in zip(lines, riv["features"]) if f["properties"]["name"] == "Columbia"])
    for l, f in zip(list(lines), riv["features"]):  # close the gap at the Okanogan's mouth
        if f["properties"]["name"] == "Okanogan":
            end = Point(l.coords[-1])
            lines.append(LineString([end, nearest_points(end, col)[1]]))
    net = unary_union([l.buffer(0.004) for l in lines]).boundary
    net = unary_union(lines + [net])
    faces = [f for f in polygonize(net) if f.area > 0.05 and f.representative_point().within(box(-119.55, 48.0, -118.1, 49.0))]
    return unary_union(faces).buffer(0.006).intersection(box(-121.0, 47.0, -117.0, 49.0))


def draw_poly(ax, g, **kw):
    if g.is_empty:
        return
    for p in getattr(g, "geoms", [g]):
        if p.geom_type != "Polygon":
            continue
        verts, codes = [], []
        for ring in [p.exterior, *p.interiors]:
            xy = list(ring.coords)
            verts += xy
            codes += [MPath.MOVETO] + [MPath.LINETO] * (len(xy) - 2) + [MPath.CLOSEPOLY]
        ax.add_patch(PathPatch(MPath(verts, codes), **kw))


def main():
    topo = Path(sys.argv[1])
    counties = tomllib.load(open(DATA / "map_1887.toml", "rb"))["county"]
    atlas = {f"{r['state']};{r['county']}": r["newberry_id"]
             for r in csv.DictReader(open(DATA / "newberry_1887.csv", encoding="utf-8")) if r["kind"] == "county"}
    hawaii = {"HI;Kauaʻi": "4434", "HI;Maui": "4436", "HI;Kalawao": "4432", "HI;Oʻahu": "4430"}
    for r in csv.DictReader(open(topo / "output_counties_metadata.csv", encoding="utf-8")):
        if r["state_terr"].startswith("Hawaii") and r["name"].startswith("EAST HAWAII"):
            hawaii["HI;Hilo"] = r["id_num"]
        if r["state_terr"].startswith("Hawaii") and r["name"].startswith("WEST HAWAII"):
            hawaii["HI;Kona"] = r["id_num"]
    geom = load_geometry(topo, atlas, hawaii)

    # assemble the new counties
    owner = {}
    new = defaultdict(list)
    unit = {c["name"]: c["unit"] for c in counties}
    for c in counties:
        for k, f in c["parts"].items():
            if k not in owner or f > owner[k][1]:
                owner[k] = (c["name"], f)
    for k, (name, _) in owner.items():
        g = geom[k]
        for other, x1, y1, x2, y2 in CUTS.get(k, []):
            piece = g.intersection(box(x1, y1, x2, y2))
            new[other].append(piece)
            g = g.difference(piece)
        new[name].append(g)
    for name, key in (("Oʻahu", "HI;Oʻahu"), ("Maui", "HI;Maui"), ("Maui", "HI;Kalawao"), ("Kauaʻi", "HI;Kauaʻi"),
                      ("Hilo", "HI;Hilo"), ("Kona", "HI;Kona")):
        if key in geom:
            new[name].append(geom[key])
    thal = box(-157.87, 21.38, -157.76, 21.53)
    oahu = unary_union(new["Oʻahu"])
    new["Thalassia"] = [oahu.intersection(thal)]
    new["Oʻahu"] = [oahu.difference(thal)]
    baja = {f["properties"]["name"]: shape(f["geometry"]) for f in json.load(open(DATA / "baja_outline.geojson"))["features"]}
    new["Ensenada"] = [baja["Baja California"]]
    new["La Paz"] = [baja["Baja California Sur"]]
    merged = {n: unary_union(gs).buffer(0) for n, gs in new.items()}
    hl = tomllib.load(open(DATA / "homelands_1887.toml", "rb"))
    homes = {}
    for h in hl["large"]:
        g = Polygon(h["ring"]) if "ring" in h else None
        if h.get("rivers"):  # Colville: between the Columbia and the Okanogan, south of 49 N
            g = colville(DATA)
        if "counties" in h:
            cg = unary_union([geom[k] for k in h["counties"]])
            if "box" in h:
                cg = cg.intersection(box(*h["box"]))
            g = cg if g is None else g.intersection(cg)
        homes[h["name"]] = g.buffer(0)
    report = []
    KM = 1 / 111.0  # degrees, roughly
    all_homes = unary_union(list(homes.values()))
    skip = {c["name"] for c in counties if c["unit"] in ("Hawaii", "Thalassia", "Baja")}
    for n in list(merged):
        if n in skip or not merged[n].intersects(all_homes):
            continue
        rest = merged[n].difference(all_homes)
        opened = rest.buffer(-6 * KM).buffer(6 * KM).intersection(rest)  # drop spikes and slivers under about 12 km
        slivers = rest.difference(opened)
        for h in homes:  # slivers touching a homeland go to it
            near = [q for q in getattr(slivers, "geoms", [slivers]) if not q.is_empty and q.intersects(homes[h].buffer(2 * KM))]
            if near:
                homes[h] = unary_union([homes[h]] + near).buffer(0)
        pieces = sorted([q for q in getattr(opened, "geoms", [opened]) if q.geom_type == "Polygon"], key=lambda q: -q.area)
        merged[n] = pieces[0]
        for pc in pieces[1:]:
            sqmi = pc.area * 69.0 * 69.0 * math.cos(math.radians(pc.centroid.y))
            best, blen = None, 0.0
            for m2, g2 in merged.items():
                if m2 == n or m2 in skip:
                    continue
                shared = pc.buffer(1.5 * KM).intersection(g2).area
                if shared > blen:
                    best, blen = m2, shared
            near_home = max(homes, key=lambda h: pc.buffer(1.5 * KM).intersection(homes[h]).area)
            best = PREFER.get(n, best)
            if sqmi < 500 and pc.buffer(1.5 * KM).intersects(homes[near_home]):
                homes[near_home] = unary_union([homes[near_home], pc]).buffer(0)
                report.append(f"{n}: a detached {sqmi:,.0f} sq mi goes to the {near_home} homeland")
            elif best:
                merged[best] = unary_union([merged[best], pc]).buffer(0)
                report.append(f"{n}: a detached {sqmi:,.0f} sq mi goes to {best}")
            else:
                merged[n] = unary_union([merged[n], pc])
                report.append(f"{n}: a detached {sqmi:,.0f} sq mi stays with it (no neighbour)")
    areas = {h: g.area * 69.0 * 69.0 * math.cos(math.radians(g.centroid.y)) for h, g in homes.items()}
    missing = [c["name"] for c in counties if c["name"] not in merged or merged[c["name"]].is_empty]
    # ground of Pacifican states in no county: the Utes' Slope, the Wallowa
    assigned = set(owner)
    states_in = ("CA", "OR", "WA", "ID", "NV", "UT", "AZ", "NM")
    shares = tomllib.load(open(DATA / "overrides.toml", "rb"))["pacifica_share"]
    outside = [g for k, g in geom.items() if k not in assigned and not k.startswith("HI;")
               and (k.split(";")[0] in states_in or float(shares.get(k, 0)) == 1)]
    union_side = [g for k, g in geom.items() if k not in assigned and not k.startswith("HI;")
                  and k.split(";")[0] in ("MT", "WY", "CO") and float(shares.get(k, 0)) < 1]

    def proj_with(fn):
        def f(g):
            def tr(c):
                xs, ys = fn(list(c[:, 0]), list(c[:, 1]))
                return np.column_stack([xs, ys])
            return shapely.transform(g, tr)
        return f

    P = proj_with(albers)
    local = lambda lon, lat: ([(a + 157.5) * math.cos(math.radians(20.5)) for a in lon], list(lat))
    PH = proj_with(local)
    fig = plt.figure(figsize=(17, 21), dpi=170)
    ax = fig.add_axes([0.01, 0.01, 0.98, 0.95])
    ax.set_aspect("equal")
    ax.axis("off")
    for g in union_side:
        draw_poly(ax, P(g), facecolor="#f4f4f4", edgecolor="#dddddd", linewidth=0.3)
    for g in outside:
        left = g.difference(unary_union(list(homes.values())).buffer(3 * KM))
        if not left.is_empty:
            draw_poly(ax, P(left), facecolor="#ffffff", edgecolor="#999999", linewidth=0.4, hatch="////")
    for k, g in geom.items():  # our timeline's county lines, faint
        if k in assigned:
            draw_poly(ax, P(g), facecolor="none", edgecolor="#b0b0b0", linewidth=0.25, linestyle=":")
    main_names = [c["name"] for c in counties if c["unit"] not in ("Hawaii", "Thalassia")]
    for n in main_names:
        draw_poly(ax, P(merged[n]), facecolor=UNIT_COLOUR[unit[n]], edgecolor="#333333", linewidth=0.9)
    for name, hg in homes.items():
        draw_poly(ax, P(hg), facecolor="#fdf1e7", edgecolor="#7a3b12", linewidth=1.3)
    for h in hl["inner"]:
        draw_poly(ax, P(Polygon(h["ring"])), facecolor="#f6d9c2", edgecolor="#7a3b12", linewidth=1.1, linestyle="--")
    cal_land = unary_union([merged[c["name"]] for c in counties if c["unit"] == "California"])
    tracts = {t["name"]: Polygon(t["ring"]).intersection(cal_land) for t in hl["tract"]}
    for tg in tracts.values():
        draw_poly(ax, P(tg), facecolor="#f9e3d0", edgecolor="#7a3b12", linewidth=0.8, zorder=5)
    ax.autoscale_view()
    x0, x1 = ax.get_xlim()
    ax.set_xlim(x0 - 0.02, x1 + 0.005)

    def inset(rect, names, title, lonlat, P=P, fn=albers):
        a = fig.add_axes(rect)
        a.set_aspect("equal")
        for n in names:
            draw_poly(a, P(merged[n]), facecolor=UNIT_COLOUR[unit[n]], edgecolor="#333333", linewidth=0.9)
        xs_, ys_ = fn([lonlat[0], lonlat[2]], [lonlat[1], lonlat[3]])
        a.set_xlim(min(xs_), max(xs_))
        a.set_ylim(min(ys_), max(ys_))
        a.set_xticks([])
        a.set_yticks([])
        a.set_title(title, fontsize=9, loc="left")
        return a, box(min(xs_), min(ys_), max(xs_), max(ys_))

    hawaii_names = ["Kauaʻi", "Oʻahu", "Thalassia", "Maui", "Hilo", "Kona"]
    insets = [
        (*inset([0.02, 0.04, 0.33, 0.20], hawaii_names, "Hawaii's five and Thalassia (red, on Kāneʻohe Bay)",
                (-160.4, 18.7, -154.6, 22.4), P=PH, fn=local), hawaii_names, PH, True),
        (*inset([0.02, 0.26, 0.24, 0.20], main_names, "San Francisco Bay", (-123.25, 36.9, -120.9, 38.95)), main_names, P, False),
        (*inset([0.66, 0.13, 0.20, 0.19], main_names, "The Wasatch Front", (-113.3, 39.9, -110.8, 42.3)), main_names, P, False),
        (*inset([0.80, 0.56, 0.18, 0.21], main_names, "Puget Sound and the lower Columbia", (-124.3, 45.2, -121.6, 48.6)), main_names, P, False),
    ]

    # ---- labels: white halo, drawn above every line, and never two on top of each other ----
    fig.canvas.draw()
    rend = fig.canvas.get_renderer()
    halo = [pe.withStroke(linewidth=2.0, foreground="white")]
    taken = []          # display-space boxes already used by labels and squares
    keep_off = []       # ground the main map's labels keep off: the insets, the key
    key = []            # labels that did not fit: (number, name)

    def free(bb, a):
        return not any(bb.overlaps(o) for o in (taken + keep_off if a is ax else taken))

    def put(a, text, cands, sizes, inside=None, min_inside=0.0, **style):
        """Try each size and candidate (x, y, ha, va) in turn; keep the first that touches no other label."""
        clip = a.get_window_extent(rend)
        for fs in sizes:
            for x, y, ha, va in cands:
                t = a.text(x, y, text, ha=ha, va=va, fontsize=fs, zorder=12, path_effects=halo, linespacing=0.92, **style)
                bb = t.get_window_extent(rend).expanded(1.06, 1.12)
                ok = free(bb, a) and clip.x0 <= bb.x0 and bb.x1 <= clip.x1 and clip.y0 <= bb.y0 and bb.y1 <= clip.y1
                if ok and inside is not None and min_inside > 0:
                    inv = a.transData.inverted()
                    (ax0, ay0), (ax1, ay1) = inv.transform((bb.x0, bb.y0)), inv.transform((bb.x1, bb.y1))
                    bx = box(ax0, ay0, ax1, ay1)
                    ok = bx.intersection(inside).area >= min_inside * bx.area
                if ok:
                    taken.append(bb)
                    return True
                t.remove()
        return False

    def interior_points(g, n=7):
        big = max(getattr(g, "geoms", [g]), key=lambda q: q.area)
        pts = [big.representative_point()]
        try:
            pts.insert(0, polylabel(big, tolerance=max(1e-5, math.sqrt(big.area) / 40)))
        except Exception:
            pass
        x0_, y0_, x1_, y1_ = big.bounds
        grid = [Point(x0_ + (i + 0.5) * (x1_ - x0_) / n, y0_ + (j + 0.5) * (y1_ - y0_) / n) for i in range(n) for j in range(n)]
        grid = sorted((q for q in grid if big.contains(q)), key=lambda q: -big.exterior.distance(q))
        return big, [(q.x, q.y, "center", "center") for q in pts + grid[:14]]

    def wraps(name):
        out = [name]
        if " " in name:
            out.append(name.replace(" ", "\n"))
            if name.count(" ") > 1:
                out.append(name.replace(" ", "\n", 1))
        return out

    def label_area(a, name, g, sizes, style, allow_outside=False, numbered=True, key_suffix=""):
        g = g if g.is_valid else g.buffer(0)
        if g.is_empty:
            return
        big, cands = interior_points(g)
        for need in (0.92, 0.7):
            for form in wraps(name):
                if put(a, form, cands, sizes, inside=big, min_inside=need, **style):
                    return
        if allow_outside:
            x0_, y0_, x1_, y1_ = big.bounds
            cx, cy = (x0_ + x1_) / 2, (y0_ + y1_) / 2
            vx0, vx1 = a.get_xlim()
            for k in (0.25, 0.9, 1.8, 3.0):  # a little way off, then further, with a leader line back
                d = k * max(x1_ - x0_, y1_ - y0_) + 0.004 * (vx1 - vx0)
                outside = [(x1_ + d, cy, "left", "center"), (x0_ - d, cy, "right", "center"), (cx, y1_ + d, "center", "bottom"),
                           (cx, y0_ - d, "center", "top"), (x1_ + d, y1_ + d, "left", "bottom"), (x0_ - d, y0_ - d, "right", "top"),
                           (x1_ + d, y0_ - d, "left", "top"), (x0_ - d, y1_ + d, "right", "bottom")]
                for cand in outside:
                    if put(a, name, [cand], sizes[:2], **style):
                        c0 = big.representative_point()
                        a.plot([c0.x, cand[0]], [c0.y, cand[1]], color="#222222", lw=0.7, zorder=11, solid_capstyle="round")
                        a.plot([c0.x], [c0.y], marker="o", ms=2.2, color="#222222", zorder=11)
                        return
        if numbered:
            num = len(key) + 1
            if put(a, str(num), cands, (5.4, 4.6, 4.0), weight="bold", color=style.get("color", "#111111")):
                key.append((num, name + key_suffix))
                return
        put(a, name, cands[:1], sizes[-1:], **style)  # last resort: at the best point whatever is there

    # ground the labels must keep off: the insets on the main map, the key, the legend
    for a_, *_ in insets:
        keep_off.append(a_.get_window_extent(rend).expanded(1.02, 1.06))
    key_box = fig.transFigure.transform([[0.015, 0.50], [0.165, 0.705]])
    from matplotlib.transforms import Bbox
    keep_off.append(Bbox(key_box))
    county_style = dict(color="#111111")
    home_style = dict(color="#7a3b12", style="italic", weight="bold")
    # 1. enclave squares first, so that names keep off them
    marks = []
    for group in ("elsewhere",):
        for name, lo, la in hl["enclaves"][group]:
            x, y = albers(lo, la)
            ax.plot([x], [y], marker="s", ms=3.4, color="#7a3b12", mec="white", mew=0.5, zorder=11)
            dx, dy = ax.transData.transform((x, y))
            taken.append(Bbox([[dx - 4, dy - 4], [dx + 4, dy + 4]]))
            marks.append((name, x, y))
    # 2. the homelands, then the counties from the smallest up (the hardest first)
    for name, hg in homes.items():
        label_area(ax, name, P(hg), (7.4, 6.6, 5.8), home_style, numbered=False)
    for h in hl["inner"]:
        label_area(ax, h["name"], P(Polygon(h["ring"])), (6.4, 5.6), home_style, numbered=False)
    late = []
    in_inset = set()
    for _, view, names, proj, _o in insets[1:]:
        for n in names:
            g = proj(merged[n]).buffer(0)
            if g.intersection(view).area > 0.9 * g.area:
                in_inset.add(n)
    for n in sorted(main_names, key=lambda n: P(merged[n]).area):
        if n in in_inset:
            continue
        label_area(ax, n, P(merged[n]), (7.6, 6.6, 5.8, 5.0), county_style)
    for tname, tg in sorted(tracts.items(), key=lambda kv: kv[1].area):
        label_area(ax, tname, P(tg), (5.0, 4.4), dict(color="#5a2a0c", style="italic"), allow_outside=True, key_suffix=" (homeland)")
    # 3. the insets
    for a_, view, names, proj, outside_ok in insets:
        for n in sorted(names, key=lambda n: proj(merged[n]).area):
            g = proj(merged[n]).buffer(0).intersection(view)
            if g.is_empty or (g.area < 0.3 * proj(merged[n]).buffer(0).area and g.area < 0.02 * view.area):
                continue
            label_area(a_, n, g, (8.0, 7.0, 6.2, 5.4), county_style, allow_outside=True, numbered=False)
    # 4. the enclaves' names round their squares
    off = 0.0011
    for name, x, y in marks:
        cands = [(x + off, y, "left", "center"), (x - off, y, "right", "center"), (x, y + off, "center", "bottom"),
                 (x, y - off, "center", "top"), (x + off, y + off, "left", "bottom"), (x + off, y - off, "left", "top"),
                 (x - off, y + off, "right", "bottom"), (x - off, y - off, "right", "top")]
        if not put(ax, name, cands, (4.8, 4.3), color="#5a2a0c", style="italic"):
            num = len(key) + 1
            if put(ax, str(num), cands, (4.6, 4.0), color="#5a2a0c", weight="bold"):
                key.append((num, name + " (homeland)"))
    if key:
        fig.text(0.018, 0.70, "Names that do not fit on the map\n" + "\n".join(f"{i}  {n}" for i, n in key),
                 fontsize=7.2, va="top", linespacing=1.25)

    fig.text(0.02, 0.975, "The 124 counties of the Constitution of the Realm, 1 August 1887", fontsize=20, weight="bold")
    fig.text(0.02, 0.962, "CR-071 Part I, draft 8 (16 November 2026). Colours: the old members and territories the counties replace. "
             "Dotted grey: our timeline's county lines of 1887.\n"
             "Heavy brown outlines: the large homelands, outside the 124 (Royce's lines where our timeline has a text). Dashed: the Hopi. "
             "Thin brown outlines: California's nineteen treaty tracts of 1851-52, traced from Royce's plate; they lie inside counties.\n"
             "Brown squares: other homelands inside a county, not yet outlined. Not shown: Alaska. MODEL and PROPOSED.",
             fontsize=9.5, va="top")
    handles = [plt.Rectangle((0, 0), 1, 1, fc=c, ec="#333333") for c in UNIT_COLOUR.values()]
    fig.legend(handles, list(UNIT_COLOUR), loc="lower right", bbox_to_anchor=(0.985, 0.03), fontsize=9, ncol=2,
               title="Old unit", frameon=True)
    out = HERE / "outputs" / "map_1887.png"
    fig.savefig(out)
    with open(HERE / "outputs" / "homelands_1887.md", "w", encoding="utf-8") as f:
        f.write("# The large homelands as drawn (MODEL)\n\nBuilt by `population/draw_map_1887.py` from "
                "`data/counties/homelands_1887.toml`.\n\n| Homeland | Square miles as drawn | Royce |\n|---|---|---|\n")
        for h in hl["large"]:
            f.write(f"| {h['name']} | {areas[h['name']]:,.0f} | {h['royce']} |\n")
        f.write(f"| **Total** | {sum(areas.values()):,.0f} | |\n\n## California's nineteen tracts (enclaves)\n\n| Royce | Treaty | Tract | Square miles as drawn |\n|---|---|---|---|\n")
        tot = 0.0
        for t in hl["tract"]:
            g = tracts[t["name"]]
            sq = g.area * 69.0 * 69.0 * math.cos(math.radians(g.centroid.y))
            tot += sq
            f.write(f"| {t['royce']} | {t['treaty']} | {t['name']} | {sq:,.0f} |\n")
        f.write(f"| | | **Total** | {tot:,.0f} |\n\n## Counties adjusted to the homelands' lines\n\n")
        f.write("\n".join(f"- {r}" for r in report) + "\n")
    print("\n".join(report))
    print({h: round(a) for h, a in areas.items()})
    print("numbered:", key)
    print("wrote", out, "| counties with no shape:", missing or "none", "| drawn:", len([n for n in merged if not merged[n].is_empty]))


if __name__ == "__main__":
    main()
