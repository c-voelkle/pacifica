"""Inputs for the energy workbook: levers, benchmark paths, historical anchors and events.

Every number here is either a historical anchor (with its source and whether it was
verified in the building session) or a MODEL assumption (with its basis). The build
script writes them into the workbook as blue input cells; nothing here is a result.

Status words used in the Anchors sheet:
  VERIFIED  read from the cited source in the building session (3 November 2026)
  CARRIED   verified in an earlier session and cited in a project document
  TO VERIFY recalled from the cited standard series; the primary table could not be
            reached from the session (census.gov and USGS PDFs are blocked). The
            author should check these against the downloads listed in README.md.
"""

# ---------------------------------------------------------------- benchmark years
# Paths are given at these years and interpolated linearly in between by formula.
PATH_YEARS = [1846, 1850, 1860, 1870, 1880, 1885, 1890, 1895, 1900, 1907, 1913, 1915,
              1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1926, 1927, 1928,
              1929, 1930, 1931, 1932]

# ---------------------------------------------------------------- levers
# (name, label, story, stress, unit, status, basis)
LEVERS = [
    ("— Demand —",),
    ("elec_pace", "Electrification pace (× Story shares of homes and factories)", 1.0, 0.85, "×", "Model estimate",
     "Stress electrifies later: the shares of homes and factory horsepower on electric drive are 15% lower, capped at 100%."),
    ("motor_full", "Electricity for motors in a fully electrified industry", 1.15, 1.15, "kWh per 1913 $ of real GDP", "Model estimate",
     "Calibrated to the US in 1929: about 57 TWh of industrial use (utility sales plus self-generation) on about $65bn of real GDP (1913 $) at 78% of factory horsepower electric (Devine 1983)."),
    ("ind_w", "Industrial weight of a Pacifican dollar against a US dollar", 0.5, 0.5, "×", "Model estimate",
     "Pacifica's real GDP per person is about 2.3 times the US's (finance), but its physical industry is 15–30% of the US's while its GDP is about two-thirds. "
     "The same weight scales factory motors here and is consistent with the industrial fuel path (ind_mj, about 0.35–0.4 of US intensity); a little higher because the champions lean to electrical and chemical work."),
    ("arc_mwh", "Electricity per tonne of nitrogen fixed in the arc", 70, 70, "MWh/t N", "Historical",
     "Birkeland–Eyde arc; the figure used in CR-051's power check (outside the texts)."),
    ("haber_mwh", "Electricity per tonne of Haber–Bosch nitrogen", 1.5, 1.5, "MWh/t N", "Model estimate", "Compressors and pumps; the hydrogen comes from gas."),
    ("haber_gj", "Fuel per tonne of Haber–Bosch nitrogen", 75, 75, "GJ/t N", "Model estimate", "1920s plants on reformed gas or water gas: roughly 70–100 GJ/t N."),
    ("carbide_mwh", "Electricity per tonne of calcium carbide", 3.3, 3.3, "MWh/t", "Historical (to verify)", "Willson-type furnaces, about 3–4 MWh/t."),
    ("chlor_mwh", "Electricity per tonne of chlorine", 3.6, 3.6, "MWh/t", "Historical (to verify)", "Castner–Kellner cells, about 3.5–4 MWh/t."),
    ("esteel_mwh", "Electricity per tonne of electric-furnace steel", 0.8, 0.8, "MWh/t", "Historical (to verify)", "About 0.6–0.9 MWh/t."),
    ("falloy_share", "Ferro-alloys as a share of steel output", 0.015, 0.015, "share", "Model estimate", "Ferrosilicon and ferromanganese for the steel champion."),
    ("falloy_mwh", "Electricity per tonne of ferro-alloys", 7, 7, "MWh/t", "Historical (to verify)", "75% ferrosilicon about 8–10 MWh/t, ferromanganese less."),
    ("abras_mwh", "Electricity per tonne of carborundum and graphite", 8, 8, "MWh/t", "Historical (to verify)", "Acheson furnaces."),
    ("pump_kwh", "Electricity per pumped irrigated acre", 400, 400, "kWh/acre/yr", "Model estimate", "Central Valley well pumping, lifts of 50–100 ft."),
    ("car_home", "Share of motor vehicles built that stay in Pacifica", 0.8, 0.8, "share", "Model estimate", "The rest are exported to partners (CR-020 B9 champions)."),
    ("car_scrap", "Vehicles scrapped each year", 0.08, 0.08, "share of stock", "Model estimate", "An average life of about twelve years."),
    ("gulf_home", "Share of the Pacifican-controlled Gulf crude that can be shipped home", 0.8, 0.6, "share", "Model estimate",
     "After the trust's Asian sales; the rest is sold in the Gulf and the Atlantic. Gulf crude by the canal."),
    ("asia_home", "Share of the trust's Asian oil sales refined from home crude", 0.5, 0.5, "share", "Model estimate", "The rest comes from Gulf crude refined by Pacifican firms (finance Champions!L:N)."),
    ("ref_own", "Refinery own use and losses", 0.07, 0.07, "share of throughput", "Model estimate", "1920s refineries burned 6–8% of their crude."),
    ("— Supply —",),
    ("hydro_pace", "Hydro building pace, ordinary basins (× Story path)", 1.0, 0.7, "×", "Model estimate",
     "Stress builds 30% fewer dams. Canon's strategic dams (the Works on the Pit and Feather, Rock Island) are not scaled."),
    ("dry_year", "Dry year applied to the main balance (0 = none)", 0, 1924, "year", "Historical",
     "1924 was a severe drought year in California and brought a power shortage (outside the texts). The Checks test a dry year in every year regardless."),
    ("dry_factor", "Hydro output in a dry year", 0.65, 0.6, "× normal", "Model estimate", "California hydro fell to roughly 60–70% of normal in the worst years."),
    ("hydro_firm", "Dependable hydro capacity", 0.6, 0.55, "× nameplate", "Model estimate", "Share of hydro nameplate counted on at the late-summer peak."),
    ("reserve", "Reserve margin planned above the peak", 0.2, 0.15, "share", "Model estimate", "1920s utility practice was 15–25%."),
    ("th_cf_max", "Highest yearly capacity factor of steam plant", 0.6, 0.6, "share", "Model estimate", "Above this the model builds more steam plant."),
    ("strat_lf", "Load factor of the strategic loads", 0.92, 0.92, "share", "Model estimate", "The halls and the station run day and night."),
    ("strat_loss", "Losses on the strategic loads' own lines", 0.04, 0.04, "share", "Model estimate", "Dedicated high-voltage lines from nearby dams."),
    ("works_cf", "Capacity factor of the Works' dams on the Pit and the Feather", 0.62, 0.6, "share", "Model estimate", "The Pit is spring-fed and unusually steady; storage on the upper Feather."),
    ("coal_mult", "Western coal output the Realm can raise (× historical by district)", 3.0, 2.0, "×", "Model estimate",
     "Historically western coal stayed small because California burned oil and hydro; Utah, Rock Springs and New Mexico have the reserves for several times that output if the demand is there. Above this coal is imported (Paths coal_imp_cap)."),
    ("coal_gj", "Heat value of western coal", 25, 25, "GJ/t", "Historical (to verify)", "Utah and Washington bituminous about 26–28, Rock Springs and New Mexico sub-bituminous 21–24."),
    ("atom_cf", "Capacity factor of the atomic stations", 0.75, 0.6, "share", "Model estimate", "Same lever as the financial workbook's atom_cf."),
    ("— Strategic loads (CR-051) —",),
    ("halls_pos", "Halls' draw within CR-051's range (0 = low, 1 = high)", 0.5, 1.0, "position", "Model estimate", "CR-051 M2 gives a range each year; Stress takes the top."),
    ("halls_after", "Halls' draw after 1927 (× 1925–27 level)", 0.75, 0.75, "×", "OPEN",
     "CR-050 keeps a separation-hall feed in 1928–1932 for a small arsenal; the plant is not cut back to nothing. Author to decide."),
    ("feed_pos", "Feed plant oil within CR-051's 0.4–0.75 Mt (0 = low, 1 = high)", 0.5, 1.0, "position", "Model estimate", "CR-051 M2."),
    ("hilo_src", "Power for the Hilo smelter (1 = oil-fired steam, 2 = windward hydro)", 1, 1, "switch", "OPEN",
     "Handoff §8. The Big Island's windward streams cannot carry a smelter (see Strategic loads). Default oil."),
    ("— Dams and lead times —",),
    ("colms_on", "Mid-Columbia chain of low dams with ladders (1 = yes)", 0, 0, "switch", "OPEN (option in CR-052)",
     "Handoff §8 'big dams earlier?'. Not needed for a hydro-led grid (64% hydro in 1929 without it); it would raise the Northwest's hydro share. Sites as the historical Rocky Reach, Wells and Chief Joseph; Native consent OPEN. "
     "The model pools the mainland, so Columbia power is counted as if it could reach California, which no 1920s line could."),
    ("colms_dec", "Mid-Columbia chain: decision", 1921, 1924, "year", "OPEN", "After Rock Island (1920); first power three years later."),
    ("colms_rate", "Mid-Columbia chain: capacity added each year", 300, 250, "MW/yr", "Model estimate", ""),
    ("colms_max", "Mid-Columbia chain: full size", 2000, 2000, "MW", "Model estimate", "Historically Rocky Reach, Wells and Chief Joseph together are about 4.6 GW (to verify); a 1920s first stage."),
    ("works_dec", "Works' dams on the Pit and the Feather: decision", 1920, 1920, "year", "Canon (CR-051 R2)", "Decided with the halls' expansion."),
    ("rock_dec", "Rock Island dam: decision", 1920, 1920, "year", "Canon (CR-051 S7)", "Built 1920–23."),
    ("boulder_dec", "Boulder Canyon dam: decision", 1928, 1928, "year", "OPEN",
     "Historically authorized 1928, first power 1936. Handoff §8 asks whether canon brings it earlier."),
    ("dam_lead", "Lead time of a large dam from decision to first power", 2, 3, "years", "Model estimate", "Pit 1 and Caribou took about two years; Boulder five."),
    ("boulder_lead", "Lead time for Boulder Canyon", 6, 7, "years", "Model estimate", "Historically authorized 1928, built 1931–36: no Boulder power before 1932."),
    ("mainline_on", "Main-line railway electrification (1 = yes; share by year in Paths rail_el)", 1, 0, "switch", "PROPOSED (CR-052)",
     "Handoff §8. The Milwaukee Road electrified 650 route-miles across the Rockies and Cascades in 1915–20 (to verify). Story electrifies the mountain crossings first, then the busiest valley lines."),
    ("rail_kwh_gj", "Electricity per GJ of locomotive fuel replaced", 22, 22, "kWh/GJ", "Model estimate",
     "A steam locomotive turns about 6% of its fuel into work at the rail, an electric one about 75% of what it takes from the wire."),
    ("— Money (1913 $ unless stated) —",),
    ("cost_hydro", "Hydro plant, built", 160, 200, "$/kW", "Model estimate", "Big Creek and Pit-era plants about $150–250/kW in 1913 money."),
    ("cost_steam", "Steam plant, built", 70, 85, "$/kW", "Model estimate", ""),
    ("cost_td", "Transmission and distribution per kW of new capacity", 110, 130, "$/kW", "Model estimate", "Lines, substations and the distribution network: about half of a 1920s utility's plant."),
    ("renewal", "Renewals each year", 0.015, 0.015, "share of the power plant stock", "Model estimate", ""),
    ("price_strat", "Price of power to the strategic loads", 0.5, 0.6, "cents/kWh", "Model estimate", "At cost from the Works' own dams."),
    ("coal_price", "Price of imported coal, delivered", 5.0, 6.0, "$/t", "Model estimate", "Australian and Japanese coal at San Francisco before 1914 was about $5–8/t (outside the texts)."),
    ("dev_share", "Share of power investment financed by the Development Fund", 0.35, 0.35, "share", "OPEN",
     "Canon: the Development Fund's power and industrial credit from 1880 (CR-020 B8). The finance workbook has no power line yet."),
    ("roy_mill", "Royalty per kWh on the compact dams (Rock Island, the Works' dams)", 0.5, 0.5, "mills/kWh", "Model estimate",
     "CR-051 S8 C2 sets the royalty, not its size. One mill = 0.1 cent."),
    ("— Check bands —",),
    ("kwh_max", "Highest believable electricity use per person", 4000, 4000, "kWh/person", "Model estimate",
     "Norway, the world's highest, was about 2,500–3,000 kWh per person around 1930 (to verify); allowance for canon's early electrification."),
    ("int_lo", "Energy per real $ against the US: lowest believable", 0.25, 0.25, "× US", "Model estimate", "Pacifica's physical industry (steel, vehicles, refining) is 15–30% of the US's while its real GDP is about two-thirds (finance), and hydro replaces fuel: energy per dollar falls well below the US."),
    ("int_hi", "Energy per real $ against the US: highest believable", 1.3, 1.3, "× US", "Model estimate", ""),
    ("cf_lo", "System capacity factor: lowest believable", 0.2, 0.2, "share", "Handoff §7, widened", "The handoff says 25%; US utilities ran at about 24% in 1902 (2.5 TWh on 1.2 GW, to verify), so 20% before 1910 is historical."),
    ("cf_hi", "System capacity factor: highest believable", 0.6, 0.6, "share", "Handoff §7", ""),
    ("capex_hi", "Power investment / GDP: highest believable", 0.04, 0.04, "share", "Model estimate", "US utilities invested about 0.8–1% of GDP a year in the 1920s (to verify)."),
    ("veh_max", "Most motor vehicles per person", 0.5, 0.5, "per person", "Model estimate", "California had about one vehicle for every 2.8 people in 1929 (to verify)."),
    ("df_max", "Most of the Development Fund's yearly investment that power can take", 0.6, 0.6, "share", "Model estimate", ""),
    ("halls_grid_max", "Halls' power taken from the common grid: most allowed", 0.25, 0.25, "share of the halls' draw", "Model estimate",
     "CR-051 says the halls need dedicated power; a quarter from the grid is the tolerance before the check fails."),
]

# ---------------------------------------------------------------- paths
# key -> (label, unit, points {year: value}, basis, status)
# Values between the given points are filled linearly; before the first point the first
# value is used, after the last point the last value.
P = {}


def path(key, label, unit, points, basis, status="Model estimate"):
    P[key] = (label, unit, points, basis, status)


# households and buildings
path("hh_size", "Persons per home", "persons", {1846: 5.5, 1900: 4.7, 1920: 4.3, 1932: 4.0},
     "US averages: 5.6 (1850), 4.8 (1900), 4.3 (1920), 4.1 (1930) (census, to verify).")
path("elec_home", "Homes with electricity", "share", {1880: 0, 1890: 0.01, 1900: 0.08, 1907: 0.2, 1913: 0.4, 1917: 0.55,
     1920: 0.65, 1924: 0.78, 1927: 0.86, 1929: 0.9, 1932: 0.93},
     "US 1930: 68% of homes (Construction Physics). Pacifica electrifies about a decade ahead (ledger L4, E10, E14).")
path("kwh_home", "Electricity per electrified home", "kWh/yr", {1890: 150, 1900: 200, 1913: 300, 1920: 450, 1924: 600,
     1927: 750, 1929: 850, 1932: 1000},
     "US about 500 kWh in 1929; Ontario's cheap hydro gave far more (to verify). Cheap hydro brings electric cooking early.")
path("kwh_comm", "Commerce and public lighting per person", "kWh/yr", {1885: 0, 1890: 3, 1900: 25, 1913: 80, 1920: 130,
     1927: 190, 1929: 210, 1932: 200}, "US 1929 about 135 kWh per person for commercial and street lighting (to verify).")
path("gj_home", "Heat for heating and cooking per home", "GJ/yr", {1846: 70, 1880: 60, 1900: 55, 1913: 50, 1920: 45, 1929: 40, 1932: 40},
     "Mild coast, cold interior (Utah, Idaho, Washington). Lower than the US average.")
path("gj_comm", "Heat for commerce per person", "GJ/yr", {1846: 1, 1900: 3, 1913: 5, 1929: 6, 1932: 6}, "")
path("lamp_bbl", "Lamp oil per home", "bbl/yr", {1846: 0, 1860: 0.1, 1870: 0.5, 1880: 1.0, 1890: 1.2, 1900: 1.0, 1913: 0.4,
     1920: 0.15, 1929: 0.05, 1932: 0.04}, "Kerosene lighting until the wire arrives.")
path("bld_wood", "Buildings' heat: wood", "share", {1846: 1.0, 1880: 0.85, 1900: 0.6, 1913: 0.4, 1920: 0.3, 1929: 0.2, 1932: 0.18}, "")
path("bld_gas", "Buildings' heat: gas", "share", {1846: 0, 1900: 0.02, 1913: 0.1, 1920: 0.15, 1929: 0.25, 1932: 0.27},
     "Oilfield gas piped to Los Angeles from 1913 and San Francisco from 1929 historically (to verify); earlier here.")
path("bld_oil", "Buildings' heat: oil", "share", {1846: 0, 1880: 0.1, 1900: 0.2, 1913: 0.25, 1920: 0.25, 1929: 0.22, 1932: 0.21},
     "Coal is the remainder.")
# industry
path("fact_elec", "Factory horsepower on electric drive", "share", {1885: 0, 1890: 0.01, 1900: 0.08, 1907: 0.2, 1913: 0.38,
     1917: 0.5, 1920: 0.6, 1924: 0.72, 1927: 0.8, 1929: 0.84, 1932: 0.88},
     "US 1909 25%, 1919 55%, 1929 78% (Devine 1983, to verify); Pacifica a few years ahead.")
path("ind_mj", "Industrial fuel (not electricity, not steel) per 1913 $ of real GDP", "MJ/$", {1846: 40, 1880: 60, 1900: 72,
     1913: 65, 1920: 60, 1929: 50, 1932: 48},
     "Process heat and steam. Below the US because Pacifica's output leans to services, champions and electrified plant.")
path("ind_oil", "Industrial fuel: oil", "share", {1846: 0, 1880: 0.05, 1890: 0.3, 1900: 0.55, 1913: 0.6, 1920: 0.55, 1929: 0.45, 1932: 0.45}, "")
path("ind_gas", "Industrial fuel: gas", "share", {1846: 0, 1900: 0.02, 1913: 0.06, 1920: 0.09, 1929: 0.15, 1932: 0.16}, "Wanted; limited by the oilfield gas actually marketed (Fuels).")
path("ind_wood", "Industrial fuel: wood", "share", {1846: 0.9, 1870: 0.7, 1880: 0.5, 1890: 0.2, 1900: 0.08, 1913: 0.03, 1920: 0.02, 1932: 0.01},
     "Coal is the remainder.")
path("steel_gj", "Fuel per tonne of steel (coke and coal)", "GJ/t", {1846: 45, 1900: 38, 1913: 32, 1920: 30, 1929: 26, 1932: 25}, "")
path("mine_int", "Electricity in mining and smelting per 1913 $m of metal and gold output", "GWh per $m", {1885: 0, 1890: 0.5,
     1900: 3, 1913: 8, 1920: 11, 1929: 15, 1932: 15}, "Comstock pumps and hoists, copper concentrators, gold dredges, cyanidation (K7).")
# electrochemistry (thousand tonnes)
path("alu_kt", "Aluminium, all smelters", "kt", {1888: 0, 1890: 0, 1895: 0.3, 1900: 2, 1907: 6, 1913: 22, 1917: 45, 1920: 50,
     1922: 55, 1924: 75, 1927: 115, 1929: 140, 1930: 120, 1932: 70},
     "US 1913 about 22 kt, 1929 about 100 kt (to verify). Canon's aluminium champion (CR-020 B9).")
path("alu_col", "Aluminium on the Columbia (incl. Wenatchee)", "kt", {1900: 0, 1907: 1, 1913: 6, 1920: 15, 1923: 20, 1924: 30,
     1927: 45, 1929: 55, 1932: 30}, "Ledger K9: the cluster is on Sierra and Columbia power.")
path("alu_wen", "… of which Wenatchee smelter (Rock Island)", "kt", {1922: 0, 1923: 0, 1924: 8, 1925: 12, 1927: 15, 1929: 18, 1932: 10},
     "CR-051 S7: the smelter takes most of Rock Island's output.")
path("alu_hilo", "Aluminium at Hilo (Keawe)", "kt", {1924: 0, 1925: 4, 1927: 12, 1929: 18, 1932: 10}, "Ledger I13, L14: built 1923–27.")
path("alu_mwh", "Electricity per tonne of aluminium", "MWh/t", {1888: 40, 1900: 32, 1913: 27, 1920: 25, 1929: 22, 1932: 21},
     "Hall–Héroult cells: about 30+ MWh/t before 1900, 22–25 MWh/t in the 1920s (to verify).")
path("arc_kt", "Nitrogen fixed in the arc", "kt N", {1906: 0, 1908: 1, 1913: 8, 1914: 12, 1915: 25, 1916: 38, 1917: 48, 1918: 50,
     1919: 30, 1920: 22, 1924: 24, 1927: 22, 1928: 15, 1929: 8, 1930: 0},
     "Ledger K11 and CR-051 R1: the war's nitrogen; about 250 MW freed for the halls in 1919–20. Arc ends 1928–29 as in Norway (OPEN).")
path("haber_kt", "Nitrogen fixed by Haber–Bosch", "kt N", {1924: 0, 1925: 2, 1927: 15, 1929: 45, 1932: 55},
     "With the seized German patents (canon O4). Handoff §8: OPEN.")
path("carb_kt", "Calcium carbide (and cyanamide)", "kt", {1892: 0, 1895: 2, 1900: 15, 1913: 50, 1920: 90, 1927: 140, 1929: 160, 1932: 100}, "Ledger K9.")
path("chlor_kt", "Chlorine and caustic", "kt Cl2", {1895: 0, 1900: 2, 1913: 20, 1920: 50, 1929: 110, 1932: 90}, "Ledger K9.")
path("esteel", "Electric-furnace steel as a share of steel output", "share", {1907: 0, 1913: 0.01, 1917: 0.05, 1920: 0.05, 1929: 0.08, 1932: 0.08}, "")
path("abras_kt", "Carborundum and furnace graphite", "kt", {1895: 0, 1900: 1, 1913: 6, 1920: 15, 1929: 30, 1932: 25},
     "Ledger K9; the Works' graphite (CR-049, CR-051 M5).")
# transport
path("rail_kwh", "Streetcars and interurbans per person", "kWh/yr", {1888: 0, 1890: 2, 1900: 25, 1907: 60, 1913: 90, 1920: 110,
     1924: 110, 1929: 100, 1932: 90}, "US about 60 kWh per person in 1929 (to verify); the Pacific coast's interurbans (Pacific Electric, Key System) were dense.")
path("rail_gj", "Railways' fuel per person, before electrification", "GJ/yr", {1846: 0, 1860: 0.5, 1870: 4, 1880: 10, 1890: 18, 1900: 24, 1913: 26, 1920: 26,
     1924: 24, 1929: 20, 1932: 17}, "US railways burned about 30 GJ per person around 1920 (to verify); oil firing is about a fifth more efficient.")
path("rail_el", "Railway traffic on electric main lines", "share", {1846: 0, 1912: 0, 1915: 0.01, 1920: 0.05, 1925: 0.15, 1929: 0.25, 1932: 0.3},
     "Used only if mainline_on = 1. Mountain crossings (Sierra, Cascades, Tehachapi) first.", "PROPOSED (CR-052)")
path("rail_oil", "Steam railways: oil", "share", {1846: 0, 1876: 0, 1880: 0.05, 1890: 0.4, 1900: 0.7, 1913: 0.8, 1929: 0.85, 1932: 0.85},
     "The Pacific coast railways burned oil historically from about 1895; here from the 1876 programme.")
path("rail_wood", "Steam railways: wood", "share", {1846: 1, 1860: 0.9, 1870: 0.6, 1880: 0.3, 1890: 0.05, 1900: 0}, "Coal is the remainder.")
path("gal_veh", "Motor fuel per vehicle on the road (cars, trucks, tractors)", "bbl/yr", {1900: 4, 1913: 9, 1920: 11, 1929: 13, 1932: 12},
     "US about 14 bbl per vehicle in 1929 (to verify).")
path("bunker", "Merchant bunkers taken at home ports", "m bbl", {1880: 0, 1890: 0.5, 1900: 4, 1913: 15, 1920: 28, 1929: 38, 1932: 32},
     "Pacific shipping on oil; the trust's bunkers sold in Asia are in the finance workbook's Asian sales.")
path("navy_coal", "Navy coal (before oil firing)", "Mt", {1852: 0, 1860: 0.02, 1880: 0.15, 1895: 0.3, 1905: 0.1, 1915: 0},
     "CR-020 B1: coal cruisers 1852–1887.")
path("pump_acres", "Irrigated land watered by electric pumps", "m acres", {1890: 0, 1900: 0.02, 1907: 0.2, 1913: 0.8, 1920: 1.4,
     1927: 2.2, 1929: 2.6, 1932: 2.8}, "Central Valley, Imperial and Columbia basin.")
path("sugar_kt", "Hawaiian sugar (bagasse burned in the mills)", "kt", {1846: 1, 1860: 1, 1880: 30, 1900: 300, 1913: 550, 1929: 900, 1932: 1000},
     "Historical Hawaii output (to verify); about 24 GJ of bagasse per tonne of sugar.")
path("hawaii", "Hawaii's share of ordinary electricity use", "share", {1846: 0.03, 1900: 0.02, 1913: 0.015, 1929: 0.012, 1932: 0.012},
     "Hawaii's 1930 population (368,000) against the Realm's.")
# electricity system
path("loss", "Transmission and distribution losses", "share", {1885: 0.25, 1900: 0.22, 1913: 0.17, 1920: 0.15, 1929: 0.12, 1932: 0.12},
     "Early high voltage in canon (E10, E14); US utilities lost about 12–15% in the 1920s (to verify).")
path("sys_lf", "Load factor of ordinary demand", "share", {1885: 0.25, 1900: 0.3, 1913: 0.38, 1920: 0.42, 1929: 0.45, 1932: 0.42}, "")
path("heat_rate", "Steam plant heat rate", "MJ/kWh", {1880: 60, 1890: 45, 1900: 32, 1913: 24, 1920: 20, 1925: 17, 1929: 15, 1932: 14.5},
     "US average 1930 about 1.6 lb of coal per kWh, about 22 MJ/kWh (to verify); Pacifica's turbines (L3) run ahead.")
path("th_oil", "Steam plant fuel: oil", "share", {1880: 0.05, 1885: 0.1, 1895: 0.6, 1900: 0.75, 1913: 0.8, 1920: 0.72, 1929: 0.55, 1932: 0.52}, "")
path("th_gas", "Steam plant fuel: gas", "share", {1880: 0, 1900: 0, 1913: 0.04, 1920: 0.08, 1929: 0.18, 1932: 0.2}, "Coal is the remainder. Oil and gas shares are wanted shares; where oil runs short the Fuels sheet moves the rest to coal.")
path("el_price", "Average price of electricity", "1913 cents/kWh", {1885: 25, 1890: 15, 1900: 6, 1913: 3.0, 1920: 2.0, 1929: 1.4, 1932: 1.4},
     "US average revenue about 2.7 cents (current) in 1929, about 1.6 cents in 1913 money (to verify); Pacifica's hydro is cheaper.")
# hydro by basin (MW nameplate, Story)
path("h_sierra", "Hydro: Sierra west slope (Yuba, American, Mokelumne, Stanislaus, Tuolumne)", "MW", {1887: 0, 1888: 1, 1890: 15, 1895: 60, 1900: 150, 1907: 350, 1913: 750, 1917: 1000, 1920: 1200, 1924: 1600, 1927: 1900, 1929: 2100, 1932: 2300},
     "PG&E had 67 MW of hydro in 1911 (Electrical World 1912). Canon's Sierra polyphase lines from 1888 (L4).")
path("h_pit", "Hydro: Pit and Feather (ordinary)", "MW", {1895: 0, 1900: 30, 1907: 100, 1913: 250, 1917: 400, 1920: 500, 1924: 650, 1927: 800, 1929: 900, 1932: 1000}, "Historically Caribou (1921) and Pit 1 (1922).")
path("h_sj", "Hydro: San Joaquin, Big Creek and Kern", "MW", {1895: 0, 1900: 40, 1907: 100, 1913: 300, 1917: 500, 1920: 650, 1924: 900, 1927: 1150, 1929: 1300, 1932: 1450}, "Historically Big Creek from 1913.")
path("h_col", "Hydro: Columbia and Snake (ordinary)", "MW", {1888: 0, 1890: 2, 1900: 40, 1907: 120, 1913: 350, 1917: 550, 1920: 700, 1924: 950, 1927: 1200, 1929: 1350, 1932: 1500}, "Spokane Falls from 1885 historically; the Columbia's own stem from Rock Island (strategic).")
path("h_wil", "Hydro: Willamette, Cascades and Puget Sound", "MW", {1888: 0, 1889: 1, 1895: 15, 1900: 60, 1907: 180, 1913: 450, 1917: 650, 1920: 800, 1924: 1100, 1927: 1400, 1929: 1600, 1932: 1800}, "Willamette Falls 1889 (canon E14); Snoqualmie 1899; Skagit 1924.")
path("h_colo", "Hydro: Colorado (excluding Boulder)", "MW", {1900: 0, 1913: 10, 1920: 40, 1927: 100, 1929: 120, 1932: 140}, "")
path("h_int", "Hydro: interior (Salt, Wasatch, Bear, upper Snake, Clark Fork)", "MW", {1890: 0, 1891: 2, 1900: 40, 1913: 200, 1920: 400, 1927: 650, 1932: 850}, "Ames (1891) on Pacifican ground (CR-049); Roosevelt Dam 1911.")
path("h_haw", "Hydro: Hawaii (windward streams)", "MW", {1890: 0, 1900: 2, 1913: 10, 1920: 20, 1927: 40, 1932: 50}, "")
path("h_works", "Hydro: the Works' dams on the Pit and upper Feather (CR-051 R2)", "MW", {1921: 0, 1922: 100, 1923: 220, 1924: 330,
     1925: 430, 1926: 480, 1932: 500}, "CR-051 R2: about 400–500 MW by 1925–26.", "Canon (CR-051 R2)")
path("h_rock", "Hydro: Rock Island (CR-051 S7)", "MW", {1922: 0, 1923: 120, 1925: 180, 1927: 210, 1932: 210},
     "Historically 1930–33, about 80 MW at first and 212 MW by 1953 (to verify).", "Canon (CR-051 S7)")
path("gas_yield", "Gasoline the home refineries can make from a barrel", "share", {1846: 0.1, 1900: 0.12, 1909: 0.18, 1913: 0.22,
     1920: 0.3, 1929: 0.45, 1932: 0.46}, "Heavy California crude yields little straight-run gasoline; canon's cracking from about 1909 (ledger K13, L12). US 1929 about 42% (to verify).")
# strategic
path("halls_lo", "Halls' draw, low end (CR-051 M2)", "MW", {1919: 0, 1920: 150, 1921: 200, 1922: 300, 1923: 400, 1924: 500,
     1925: 600, 1927: 600}, "CR-051 M2 table.", "Canon (CR-051 M2), MODEL")
path("halls_hi", "Halls' draw, high end (CR-051 M2)", "MW", {1919: 0, 1920: 200, 1921: 300, 1922: 400, 1923: 520, 1924: 650,
     1925: 800, 1927: 800}, "CR-051 M2 table.", "Canon (CR-051 M2), MODEL")
path("station", "Columbia station's draw (CR-051 S7)", "MW", {1922: 0, 1923: 15, 1924: 25, 1925: 40, 1932: 40},
     "\"Some tens of megawatts\" (S7): pumps, the separation plant, workshops and town.", "Canon (CR-051 S7), MODEL")
path("hetch", "Walled college and Tuolumne Station (Hetch Hetchy)", "MW", {1910: 0, 1911: 2, 1913: 4, 1920: 6, 1932: 8},
     "Low-power research installation and the valley; supplied from the Eleanor–Cherry system O'Shaughnessy builds (CR-051 C2).", "Canon (CR-050, CR-051), MODEL")
path("canal_mw", "Canal locks and zone (memo, outside the Realm)", "MW", {1899: 0, 1900: 6, 1913: 15, 1932: 25},
     "Gatun hydro served the locks historically (22.5 MW, to verify). Canal opened 1900 in canon.", "Memo")
# oil fields and coal districts
path("oil_cap", "Plausible output of the home oilfields", "m bbl", {1846: 0, 1876: 0.1, 1880: 0.5, 1890: 6, 1900: 30, 1907: 60,
     1913: 115, 1920: 140, 1923: 300, 1929: 330, 1932: 330},
     "Historical California plus canon's early discoveries: the 1876 programme finds Kern River, Coalinga and Midway–Sunset a decade early; "
     "the Los Angeles basin giants (1919–21) as history.")
path("oil_known", "Oil known to be recoverable in the home fields (cumulative)", "bn bbl", {1876: 0.01, 1890: 0.1, 1900: 0.5, 1910: 1.5,
     1913: 2.0, 1920: 3.0, 1925: 4.5, 1929: 5.5, 1932: 6.0},
     "California: about 3.0bn bbl produced by 1932 and about 3bn more proved then (to verify).")
path("gor", "Gas produced with the oil", "thousand cf/bbl", {1890: 0.2, 1900: 0.3, 1913: 0.8, 1920: 1.0, 1929: 1.2, 1932: 1.2},
     "California 1929: about 330 bcf with 292m bbl (to verify).")
path("other_imp", "Oil the Realm can import from elsewhere (the Union, Peru, Russia)", "m bbl", {1846: 0, 1860: 0.3, 1880: 3,
     1890: 5, 1900: 6, 1905: 3, 1913: 0, 1932: 0}, "Kerosene and fuel oil before Spindletop; historically California imported Pennsylvania kerosene and Peruvian oil (to verify).")
path("coal_imp_cap", "Coal the Realm can import", "Mt", {1846: 0.05, 1860: 0.4, 1880: 2.5, 1890: 3.5, 1900: 4.5, 1913: 8, 1920: 9, 1929: 12, 1932: 12},
     "British Columbia (Nanaimo), Australia (Newcastle), Japan, Keelung and Kaiping under partner contracts (canon §Industry). Japan mined about 34 Mt in 1929, Australia about 11 Mt, British Columbia about 2.5 Mt (to verify).")
path("wood_cap", "Wood and mill waste the forests can give as fuel", "PJ", {1846: 20, 1870: 100, 1880: 180, 1900: 320, 1913: 380,
     1920: 400, 1929: 420, 1932: 420}, "Sierra and Pacific Northwest forests; sawmill waste (hog fuel) fired much of the Northwest's industry (to verify). Used before imported coal.")
path("gas_mkt", "Share of oilfield gas marketed", "share", {1890: 0, 1900: 0.1, 1913: 0.3, 1920: 0.45, 1929: 0.65, 1932: 0.7}, "The rest is flared or vented.")
path("c_wa", "Coal: Washington (historical)", "Mt", {1870: 0, 1880: 0.2, 1890: 1.2, 1900: 2.2, 1913: 3.5, 1918: 3.7, 1932: 3.7},
     "Roslyn and the Cascades; held at the historical peak, as capacity (to verify; short tons converted).")
path("c_ut", "Coal: Utah (historical)", "Mt", {1870: 0, 1880: 0.1, 1890: 0.3, 1900: 1.0, 1913: 2.9, 1920: 5.4, 1932: 5.4}, "Carbon County (to verify).")
path("c_nm", "Coal: New Mexico (historical)", "Mt", {1870: 0, 1880: 0.2, 1890: 0.4, 1900: 1.2, 1913: 3.4, 1920: 3.3, 1932: 3.4}, "Raton and Gallup (to verify).")
path("c_wy", "Coal: Rock Springs and Kemmerer, Wyoming west of the divide (historical)", "Mt", {1868: 0, 1870: 0.1, 1880: 0.5, 1890: 1.2, 1900: 2.2, 1913: 4.0, 1920: 5.0, 1932: 5.0}, "About 55% of Wyoming's output (to verify).")

PATHS = P

# ---------------------------------------------------------------- anchors used in formulas
# Interpolation table for the US comparison (a complete row is needed for each series).
US_YEARS = [1880, 1890, 1900, 1902, 1907, 1912, 1917, 1920, 1922, 1925, 1927, 1929, 1930, 1932]
_E1 = {1880: 5.001, 1885: 5.645, 1890: 7.012, 1895: 7.661, 1900: 9.587, 1905: 13.212, 1910: 16.565, 1915: 17.734,
       1920: 21.344, 1925: 22.382, 1930: 23.68, 1935: 20.436}


def _lin(d, y):
    ks = sorted(d)
    if y in d:
        return d[y]
    lo = max(k for k in ks if k < y)
    hi = min(k for k in ks if k > y)
    return d[lo] + (y - lo) * (d[hi] - d[lo]) / (hi - lo)


US_SERIES = [
    # key, label, unit, values by US_YEARS, source, status
    ("us_pop", "US population", "m", [50.19, 62.98, 76.09, 79.16, 87.01, 95.34, 103.27, 106.46, 110.05, 115.83, 119.04, 121.77, 123.08, 124.84],
     "Historical Statistics of the United States, series A 7 (mid-year estimates)", "TO VERIFY"),
    ("us_cap", "US electric utilities: generating capacity", "GW", [0, 0, 0, 1.21, 2.71, 5.17, 8.99, 12.71, 14.19, 21.47, 25.6, 29.8, 32.38, 34.38],
     "Census of Electrical Industries (1902–1927) and FPC series in Historical Statistics S 49–69; 1880–1900 not reported", "TO VERIFY"),
    ("us_gen", "US electricity produced, utilities and industry", "TWh", [0, 0, 0, 5.97, 14.12, 24.75, 43.43, 56.56, 61.2, 84.67, 101.39, 116.75, 114.64, 99.36],
     "Historical Statistics S 15 (total electric energy production); 1930 checks against Construction Physics' 114 TWh", "TO VERIFY (1930 VERIFIED)"),
    ("us_energy", "US primary energy consumption", "quadrillion Btu", [round(_lin(_E1, y), 3) for y in US_YEARS],
     "EIA Annual Energy Review, Table E1 (from Schurr and Netschert 1960, Table II); years between the five-year values interpolated", "VERIFIED"),
]

# ---------------------------------------------------------------- anchor facts (long list)
# region, series, unit, year, value, source, status
ANCHOR_FACTS = [
    ("US", "Primary energy, total", "quadrillion Btu", y, v, "EIA AER Table E1 (Schurr & Netschert, Table II)", "VERIFIED") for y, v in sorted(_E1.items())
] + [
    ("US", "Primary energy: coal", "quadrillion Btu", 1900, 6.841, "EIA AER Table E1", "VERIFIED"),
    ("US", "Primary energy: wood", "quadrillion Btu", 1900, 2.015, "EIA AER Table E1", "VERIFIED"),
    ("US", "Primary energy: petroleum", "quadrillion Btu", 1920, 2.676, "EIA AER Table E1", "VERIFIED"),
    ("US", "Primary energy: hydro (fossil-fuel equivalent)", "quadrillion Btu", 1920, 0.738, "EIA AER Table E1", "VERIFIED"),
    ("US", "Primary energy: coal", "quadrillion Btu", 1930, 13.639, "EIA AER Table E1", "VERIFIED"),
    ("US", "Primary energy: petroleum", "quadrillion Btu", 1930, 5.897, "EIA AER Table E1", "VERIFIED"),
    ("US", "Primary energy: natural gas", "quadrillion Btu", 1930, 1.932, "EIA AER Table E1", "VERIFIED"),
    ("US", "Electricity produced (the article says utility-provided; the figure matches all producers, utilities alone were about 91)", "TWh", 1930, 114, "Construction Physics, 'The Grid, Part II'", "VERIFIED (label to check)"),
    ("US", "Generation mix: coal / hydro", "share", 1930, "56% / 34%", "Construction Physics, 'The Grid, Part II'", "VERIFIED"),
    ("US", "Homes with electricity (all / urban)", "share", 1930, "68% / 84%", "Construction Physics, 'The Grid, Part II'", "VERIFIED"),
    ("US", "Farms with utility power", "share", 1935, "12%", "Construction Physics, 'The Grid, Part II'", "VERIFIED"),
    ("US", "Utility generating capacity", "GW", 1920, 12.7, "Historical Statistics S; used in CR-051 power check", "TO VERIFY"),
    ("US", "Utility generating capacity", "GW", 1925, 21.5, "Historical Statistics S; used in CR-051 power check", "TO VERIFY"),
    ("US", "Utility generating capacity", "GW", 1930, 32.4, "Historical Statistics S; used in CR-051 power check", "TO VERIFY"),
    ("US", "Central-station electricity", "TWh", 1902, 2.507, "Census of Electrical Industries 1902", "TO VERIFY"),
    ("US", "Factory horsepower on electric drive", "share", 1909, 0.25, "Devine (1983), J. Econ. Hist. 43", "TO VERIFY"),
    ("US", "Factory horsepower on electric drive", "share", 1919, 0.55, "Devine (1983)", "TO VERIFY"),
    ("US", "Factory horsepower on electric drive", "share", 1929, 0.78, "Devine (1983)", "TO VERIFY"),
    ("US", "Utility fuel per kWh", "lb coal/kWh", 1920, 3.05, "Historical Statistics S (EEI)", "TO VERIFY"),
    ("US", "Utility fuel per kWh", "lb coal/kWh", 1930, 1.62, "Historical Statistics S (EEI)", "TO VERIFY"),
    ("US", "Motor vehicle registrations", "m", 1913, 1.26, "Historical Statistics Q 148", "TO VERIFY"),
    ("US", "Motor vehicle registrations", "m", 1920, 9.24, "Historical Statistics Q 148", "TO VERIFY"),
    ("US", "Motor vehicle registrations", "m", 1929, 26.7, "Historical Statistics Q 148", "TO VERIFY"),
    ("US", "Crude oil output", "m bbl", 1900, 63.6, "Mineral Resources of the US / Minerals Yearbook", "TO VERIFY"),
    ("US", "Crude oil output", "m bbl", 1913, 248.4, "Mineral Resources of the US", "TO VERIFY"),
    ("US", "Crude oil output", "m bbl", 1920, 442.9, "Mineral Resources of the US", "TO VERIFY"),
    ("US", "Crude oil output", "m bbl", 1929, 1007.3, "Minerals Yearbook", "TO VERIFY"),
    ("US", "Oak Ridge power allocation (Y-12 of the total)", "MW", 1945, "200 of 310", "Wikipedia, 'Clinton Engineer Works' (CR-051 power check)", "CARRIED"),
    ("California", "Crude oil output", "m bbl", 1895, 1.2, "Wikipedia, 'History of oil in California through 1930'", "VERIFIED"),
    ("California", "Crude oil output", "m bbl", 1900, 4.0, "Wikipedia, 'History of oil in California through 1930' (USGS: 4.3)", "VERIFIED"),
    ("California", "Crude oil output", "m bbl", 1910, 73.0, "Mineral Resources of the US", "TO VERIFY"),
    ("California", "Crude oil output", "m bbl", 1913, 97.8, "Mineral Resources of the US", "TO VERIFY"),
    ("California", "Crude oil output", "m bbl", 1920, 103.4, "Mineral Resources of the US (Wikipedia gives 77; conflict to resolve)", "TO VERIFY"),
    ("California", "Crude oil output", "m bbl", 1923, 262.9, "Mineral Resources of the US", "TO VERIFY"),
    ("California", "Crude oil output", "m bbl", 1929, 292.5, "Minerals Yearbook", "TO VERIFY"),
    ("California", "Crude oil output", "m bbl", 1932, 178.1, "Minerals Yearbook", "TO VERIFY"),
    ("California", "Hydroelectric output", "TWh", 1922, 3.227, "Geiger (1923), quoting the USGS (CR-051 power check)", "CARRIED"),
    ("California", "PG&E capacity (hydro 66.8 MW, steam about 71.8 MW)", "MW", 1911, 140, "Electrical World (1912) (CR-051 power check)", "CARRIED"),
    ("Pacific NW", "Coal output, Washington", "Mt", 1913, 3.5, "Mineral Resources of the US", "TO VERIFY"),
    ("Mountain", "Coal output, Utah", "Mt", 1920, 5.4, "Mineral Resources of the US", "TO VERIFY"),
    ("Norway", "Electricity per person", "kWh", 1930, "about 2,500–3,000", "Statistics Norway historical tables (to download)", "TO VERIFY"),
    ("Canada", "Central-station electricity", "TWh", 1930, 18.1, "Dominion Bureau of Statistics (to download)", "TO VERIFY"),
    ("Switzerland", "Electricity produced", "TWh", 1930, "about 5", "Swiss historical statistics (to download)", "TO VERIFY"),
    ("Units", "Crude oil", "GJ/bbl", None, 6.12, "EIA: 5.8 million Btu per barrel", "VERIFIED (standard)"),
    ("Units", "Motor gasoline", "GJ/bbl", None, 5.54, "EIA: 5.253 million Btu per barrel", "VERIFIED (standard)"),
    ("Units", "Residual fuel oil", "GJ/bbl", None, 6.63, "EIA: 6.287 million Btu per barrel", "VERIFIED (standard)"),
    ("Units", "Kerosene", "GJ/bbl", None, 5.98, "EIA: 5.670 million Btu per barrel", "VERIFIED (standard)"),
    ("Units", "Natural gas", "MJ/cf", None, 1.087, "EIA: about 1,030 Btu per cubic foot", "VERIFIED (standard)"),
    ("Units", "Tonne of oil equivalent", "GJ", None, 41.868, "IEA convention", "VERIFIED (standard)"),
]

# ---------------------------------------------------------------- events
# year, event, where it shows, section/CR, status
EVENTS = [
    (1876, "Oil programme after Pico Canyon; fuel-oil experiments", "Fuels (oil fields), Uses (railways)", "§Industry; CR-020 B1", "CANON"),
    (1882, "Oil-fired torpedo boats", "Fuels (navy oil from finance)", "CR-020 B1", "CANON"),
    (1884, "Tesla and the electrical institute (1884–86)", "Paths (electrification shares)", "Ledger L4", "CANON"),
    (1885, "Turbine programme", "Paths (heat rate)", "Ledger L3; CR-020 B1", "CANON"),
    (1888, "Polyphase transmission in the Sierra", "Hydro (Sierra west slope)", "Ledger E10, L4", "CANON"),
    (1889, "Willamette Falls transmission", "Hydro (Willamette)", "Ledger E14", "CANON"),
    (1891, "Ames plant near Telluride, on Pacifican ground", "Hydro (interior)", "CR-049", "CANON"),
    (1892, "Electrochemistry on cheap power: carbide, carborundum, chlor-alkali (1891–94)", "Uses (electrochemistry)", "Ledger K9", "CANON"),
    (1900, "Lock-and-lake canal opens (Gatun)", "Strategic loads (memo)", "Canon; CR-051 C1", "CANON"),
    (1901, "Spindletop; the trust refines Gulf crude", "Fuels (Gulf imports)", "Ledger K12; CR-020 B9", "CANON"),
    (1908, "Arc nitrogen licensed from Norway", "Uses (arc nitrogen)", "Ledger K11", "CANON (date MODEL)"),
    (1909, "Pacifican thermal cracking (or Shukhov licence)", "Fuels (gasoline yield)", "Ledger K13, L12", "PROGRAMME"),
    (1911, "Moving assembly line; walled college in the valley", "Fuels (vehicles); Strategic loads", "Ledger M10; CR-050", "CANON"),
    (1913, "Research installation in the valley", "Strategic loads (Hetch Hetchy)", "CR-050 X6", "CANON"),
    (1914, "War with Germany: munitions and the arc plants' peak (1914–18)", "Uses (arc nitrogen)", "CR-040; CR-051 R1", "CANON"),
    (1917, "Halls decided", "Strategic loads", "CR-050; CR-051 M2", "CANON"),
    (1919, "First halls on the arc plants' power", "Strategic loads (freed arc power)", "CR-051 R1", "APPROVED"),
    (1920, "Works' dams on the Pit and upper Feather begun", "Hydro (Works)", "CR-051 R2", "APPROVED; consent OPEN"),
    (1920, "Rock Island dam begun (1920–23); Columbia station and compacts", "Hydro (Rock Island); Strategic loads", "CR-051 S7, S8", "APPROVED"),
    (1923, "Columbia station runs; Wenatchee smelter", "Strategic loads", "CR-051 S7", "APPROVED"),
    (1923, "Hilo aluminium built (1923–27)", "Strategic loads (Hilo)", "Ledger I13, L14", "CANON; power OPEN"),
    (1924, "Desert test; halls at 500–650 MW", "Strategic loads", "CR-050; CR-051 M2", "APPROVED"),
    (1925, "Halls at full size, 600–800 MW (1925–27)", "Strategic loads", "CR-051 M2", "APPROVED (MODEL)"),
    (1927, "Demonstration at sea; the Concord", "Strategic loads", "CR-049, CR-050", "CANON"),
    (1928, "Boulder Canyon decision (historical date)", "Hydro (Boulder)", "Handoff §8", "OPEN"),
    (1929, "Motor vehicles: 1.15m built a year", "Fuels (vehicle stock)", "CR-020 B9", "CANON"),
    (1931, "Tokyo atomic station first power; Pacifican stations follow", "Electricity (atomic, from finance)", "CR-050", "CANON"),
    (1932, "Oil compact with the Gulf", "Fuels (finance oil output)", "CR-020 B6", "CANON"),
]


# =====================================================================================
# Second revision, 3 November 2026 (evening): the author's sources, the approved
# CR-052 CT3 A, B and C and CT5 (amended), and the Max case.
# =====================================================================================

def set_lever(name, **kw):
    """Change a lever's Story or Stress value, status or basis in place."""
    for i, lv in enumerate(LEVERS):
        if len(lv) > 1 and lv[0] == name:
            n, label, st, sx, unit, status, basis = lv
            LEVERS[i] = (n, label, kw.get("story", st), kw.get("stress", sx), unit, kw.get("status", status),
                         kw.get("basis", basis))
            return
    raise KeyError(name)


# CT3 A and B, approved by the author on 3 November 2026 ("I absolutely recommend A, B and C").
set_lever("coal_mult", story=4.0, status="APPROVED (CR-052 CT3 A)",
          basis="Author, 3 Nov 2026: Realm coal at about four times its historical output by district (Utah's Carbon County and Rock Springs "
                "mechanized for Pacifican demand). Historically western coal stayed small because California burned oil and hydro.")
set_lever("gulf_home", story=1.0, status="APPROVED (CR-052 CT3 B)",
          basis="Author, 3 Nov 2026: all the Pacifican-controlled Gulf crude, after the trust's Asian sales, is shipped home through the canal.")

LEVERS += [
    ("— CR-052 second revision: oil, vehicles and the Max case —",),
    ("oil_src", "Home oil output (1 = financial workbook, 2 = CR-052 discovery path in Paths oil_c52)", 2, 1, "switch", "APPROVED (CR-052 CT3 C)",
     "Author, 3 Nov 2026: find the Los Angeles basin giants 'with the greatest believable haste'. The financial workbook still has the old path; "
     "its next build should read Paths oil_c52 (see Finance link: extra home oil)."),
    ("veh_src", "Motor vehicles on the road (1 = built in finance × share kept; 2 = vehicles per person, Paths veh_pp)", 2, 1, "switch",
     "APPROVED (CR-052 CT5 amended)",
     "Author, 3 Nov 2026: California must be the most motorized place on earth. Finance Champions!U should build what Finance link shows."),
    ("cal_mult", "California's vehicles per person against the Realm's average", 1.25, 1.25, "×", "Model estimate",
     "Historically California had about 1.6 times the US rate (0.36 against 0.22 in 1929, to verify); the Realm's interior counties have fewer."),
    ("eln_mwh", "Electricity per tonne of nitrogen as ammonia from electrolytic hydrogen", 13, 13, "MWh/t N", "Historical (to verify)",
     "Norsk Hydro's electrolytic ammonia at Rjukan from 1927–29: about 10–11 MWh per tonne of ammonia, 12–14 MWh per tonne of nitrogen."),
    ("eln_col", "Share of electrolytic nitrogen on the Columbia", 0.6, 0.6, "share", "Model estimate", "Beside the Columbia's cheap water power."),
    ("nw_ord", "Northwest's share of ordinary electricity use (Washington, Oregon, Idaho)", 0.22, 0.22, "share", "Model estimate",
     "Population share of the Northwest counties, about a fifth to a quarter (to verify)."),
]

# Max case: every source Pacifica can reach and every use that can absorb it. Levers
# not listed take their Story value.
MAX = {
    "elec_pace": 1.15, "ind_w": 0.75, "motor_full": 1.15, "hydro_pace": 1.35, "hydro_firm": 0.6,
    "colms_on": 1, "colms_dec": 1918, "colms_rate": 400, "colms_max": 3000,
    "boulder_dec": 1920, "boulder_lead": 6, "mainline_on": 1, "coal_mult": 4.0, "gulf_home": 1.0,
    "oil_src": 2, "veh_src": 2, "kwh_max": 5000, "int_hi": 1.5, "halls_pos": 0.5,
}
MAX_NOTES = {
    "kwh_max": "Max case: Montana used 3,522 kWh per person for power alone in 1917 (Census of Electrical Industries 1917).",
    "ind_w": "Max case: factories electrify process heat on cheap hydro (electric furnaces and boilers, as in Norway and Switzerland).",
}

# ------------------------------------------------------------------ new paths (Story)
path("oil_c52", "Home oil output, CR-052 discovery path", "m bbl", {1846: 0, 1876: 0.1, 1880: 1, 1885: 4, 1890: 15, 1895: 35, 1900: 70,
     1905: 120, 1910: 180, 1913: 220, 1917: 270, 1920: 320, 1923: 380, 1925: 400, 1927: 420, 1929: 450, 1931: 450, 1932: 400},
     "Approved CT3 C. The state survey of the 1876 programme maps the anticlines. Shallow fields first: Los Angeles City and Puente–Brea in "
     "the early 1880s (historically 1892 and 1880s), Kern River about 1885 (1899), Coalinga and McKittrick about 1890, Midway–Sunset about 1893. "
     "The deep basin giants need 2,000–4,500 ft: Huntington Beach about 1895 (1920), Signal Hill and Santa Fe Springs 1900–1905 (1921, 1919) "
     "with the rotary drilling of Spindletop (1897 in canon); Elk Hills 1905 (1919); Kettleman Hills and Wilmington about 1915 (1928, 1932). "
     "Output is held to what the fields could deliver within a few years of discovery (Signal Hill gave about 90m bbl a year within two years, "
     "historically) and falls in 1932 under the oil compact.", "APPROVED (CR-052 CT3 C), MODEL")
path("veh_pp", "Motor vehicles on the road per person", "per person", {1846: 0, 1900: 0, 1905: 0.001, 1910: 0.01, 1913: 0.04, 1917: 0.09,
     1920: 0.15, 1924: 0.24, 1927: 0.30, 1929: 0.33, 1932: 0.33},
     "Approved CT5 (amended). US 1929: 26.7m vehicles for 121.8m people, 0.22 (to verify). With California at 1.25 times the Realm's rate "
     "(0.41 in 1929), it is the most motorized place on earth.", "APPROVED (CR-052 CT5), MODEL")
path("eln_kt", "Nitrogen as ammonia from electrolytic hydrogen", "kt N", {1846: 0, 1932: 0},
     "None in the Story case. Max case only.", "Max case")
path("dry_gas", "Dry gas fields (Rio Vista, Buttonwillow, Kettleman's gas cap)", "PJ", {1846: 0, 1905: 0, 1913: 10, 1920: 40, 1929: 120, 1932: 130},
     "With C: the survey finds the Sacramento Valley's dry gas early (Rio Vista historically 1936; Buttonwillow 1927). Piped to the Bay cities.",
     "APPROVED with CT3 C, MODEL")
path("nw_share", "Northwest's share of ordinary use (memo for the Northwest balance)", "share", {1846: 0.15, 1900: 0.2, 1929: 0.22, 1932: 0.22}, "")

# field capability and reserves, re-derived for C (overwrites the earlier paths)
path("oil_cap", "Plausible output of the home oilfields", "m bbl", {1846: 0, 1876: 0.2, 1880: 2, 1885: 6, 1890: 25, 1895: 50, 1900: 110,
     1905: 160, 1910: 230, 1913: 280, 1917: 330, 1920: 380, 1923: 450, 1929: 560, 1932: 560},
     "What the fields found by each year could deliver if developed hard: the historical peak rates of the fields in oil_c52's basis "
     "(Long Beach about 90m bbl, Huntington Beach about 40m, Santa Fe Springs about 80m, Midway–Sunset about 45m, Kern River about 20m, "
     "Elk Hills, Kettleman Hills and Wilmington later; to verify), summed from their canon discovery years.")
path("oil_known", "Oil known to be recoverable in the home fields (cumulative)", "bn bbl", {1876: 0.01, 1885: 0.3, 1890: 1.5, 1895: 3,
     1900: 6, 1905: 9, 1910: 11, 1915: 14, 1920: 16, 1932: 19},
     "The giants' ultimate recovery (Midway–Sunset about 3bn bbl, Wilmington about 3bn, Kern River about 2bn, Belridge about 2bn, "
     "Elk Hills about 1.3bn, Huntington Beach about 1.1bn, Long Beach about 0.9bn; to verify), counted from canon discovery years at about two-thirds.")
path("gas_mkt", "Share of oilfield gas marketed", "share", {1890: 0, 1895: 0.1, 1900: 0.2, 1913: 0.4, 1920: 0.55, 1929: 0.7, 1932: 0.72},
     "The rest is flared or vented. Higher with C: the fields are near the cities earlier.")

# ------------------------------------------------------------------ Max-case paths
PATHS_MAX = {
    "oil_c52": {1846: 0, 1876: 0.2, 1880: 2, 1885: 6, 1890: 25, 1895: 50, 1900: 100, 1905: 150, 1910: 210, 1913: 260, 1917: 310,
                1920: 360, 1923: 420, 1925: 440, 1927: 470, 1929: 520, 1931: 520, 1932: 460},
    "veh_pp": {1846: 0, 1900: 0, 1905: 0.002, 1910: 0.02, 1913: 0.06, 1917: 0.12, 1920: 0.19, 1924: 0.28, 1927: 0.34, 1929: 0.37, 1932: 0.37},
    "elec_home": {1880: 0, 1890: 0.02, 1900: 0.12, 1907: 0.3, 1913: 0.55, 1917: 0.7, 1920: 0.8, 1924: 0.9, 1927: 0.95, 1929: 0.97, 1932: 0.98},
    "kwh_home": {1890: 200, 1900: 300, 1913: 450, 1920: 800, 1924: 1200, 1927: 1500, 1929: 1800, 1932: 2200},
    "kwh_comm": {1885: 0, 1890: 5, 1900: 35, 1913: 110, 1920: 170, 1927: 250, 1929: 280, 1932: 280},
    "fact_elec": {1885: 0, 1890: 0.02, 1900: 0.12, 1907: 0.3, 1913: 0.5, 1917: 0.62, 1920: 0.72, 1924: 0.82, 1927: 0.88, 1929: 0.92, 1932: 0.94},
    "alu_kt": {1888: 0, 1890: 0.2, 1895: 1, 1900: 4, 1907: 12, 1913: 40, 1917: 80, 1920: 100, 1922: 110, 1924: 150, 1927: 220, 1929: 280,
               1930: 240, 1932: 180},
    "alu_col": {1900: 0, 1907: 3, 1913: 12, 1920: 35, 1923: 50, 1924: 70, 1927: 110, 1929: 150, 1932: 100},
    "carb_kt": {1892: 0, 1895: 4, 1900: 25, 1913: 80, 1920: 140, 1927: 220, 1929: 250, 1932: 160},
    "chlor_kt": {1895: 0, 1900: 4, 1913: 35, 1920: 80, 1929: 180, 1932: 150},
    "esteel": {1907: 0.005, 1913: 0.03, 1917: 0.08, 1920: 0.1, 1929: 0.2, 1932: 0.22},
    "abras_kt": {1895: 0, 1900: 2, 1913: 10, 1920: 25, 1929: 50, 1932: 45},
    "eln_kt": {1846: 0, 1920: 0, 1922: 10, 1925: 60, 1927: 100, 1929: 150, 1932: 180},
    "haber_kt": {1846: 0, 1932: 0},
    "rail_el": {1846: 0, 1910: 0, 1913: 0.02, 1915: 0.05, 1920: 0.15, 1925: 0.35, 1929: 0.5, 1932: 0.6},
    "rail_kwh": {1888: 0, 1890: 4, 1900: 35, 1907: 80, 1913: 120, 1920: 140, 1924: 140, 1929: 130, 1932: 120},
    "pump_acres": {1890: 0, 1900: 0.05, 1907: 0.4, 1913: 1.2, 1920: 2.0, 1927: 3.2, 1929: 3.8, 1932: 4.2},
    "dry_gas": {1846: 0, 1900: 0, 1905: 5, 1913: 25, 1920: 70, 1929: 180, 1932: 200},
    "bld_wood": {1846: 1.0, 1880: 0.8, 1900: 0.5, 1913: 0.3, 1920: 0.2, 1929: 0.12, 1932: 0.1},
}
MAX_BASIS = ("Max case: every source Pacifica can reach and every use that can absorb it. Electric cooking and water heating on cheap hydro "
             "(Ontario and Norway levels), aluminium at half the world's 1929 output, electric steel, ammonia from electrolytic hydrogen "
             "(Norsk Hydro's route), half the main lines electrified, the Central Valley pumped.")

# ------------------------------------------------------------------ anchors from the author's sources
_US = {k: i for i, (k, *_r) in enumerate(US_SERIES)}
_k, _l, _u, _v, _s, _st = US_SERIES[_US["us_cap"]]
US_SERIES[_US["us_cap"]] = (_k, _l, _u, _v, _s + "; 1907, 1912 and 1917 checked against the 1917 Census of Electrical Industries "
                            "(2,709,225, 5,165,439 and 8,994,407 kW)", "VERIFIED 1907–1917; TO VERIFY otherwise")

ANCHOR_FACTS += [
    ("US", "Central stations: generating capacity", "kW", 1907, 2709225, "Census of Electrical Industries 1917, comparative summary", "VERIFIED"),
    ("US", "Central stations: generating capacity", "kW", 1912, 5165439, "Census of Electrical Industries 1917, comparative summary", "VERIFIED"),
    ("US", "Central stations: generating capacity", "kW", 1917, 8994407, "Census of Electrical Industries 1917, comparative summary", "VERIFIED"),
    ("US", "Central stations: electricity generated", "m kWh", 1907, 5862, "Census of Electrical Industries 1917", "VERIFIED"),
    ("US", "Central stations: electricity generated", "m kWh", 1912, 11569, "Census of Electrical Industries 1917", "VERIFIED"),
    ("US", "Central stations: electricity generated", "m kWh", 1917, 25438, "Census of Electrical Industries 1917", "VERIFIED"),
    ("US", "Central-station power sold per person, districts served", "kWh", 1917, 200, "Census of Electrical Industries 1917 (210 with the large plants omitted)", "VERIFIED"),
    ("California", "Central stations: dynamo capacity", "kW", 1917, 817194, "Census of Electrical Industries 1917", "VERIFIED"),
    ("California", "Central stations and electric railways: electricity generated", "m kWh", 1917, 2769, "Census of Electrical Industries 1917", "VERIFIED"),
    ("California", "Central-station electricity per person: light / power", "kWh", 1917, "152 / 489", "Census of Electrical Industries 1917", "VERIFIED"),
    ("California", "Hydroelectric plants: water horsepower", "hp", 1917, 1114356, "Census of Electrical Industries 1917", "VERIFIED"),
    ("California", "Average price of hydro power sold", "cents/kWh", 1917, 1.5, "Census of Electrical Industries 1917", "VERIFIED"),
    ("Montana", "Central-station power per person (mining and smelting)", "kWh", 1917, 3522, "Census of Electrical Industries 1917", "VERIFIED"),
    ("Pacific division", "Central-station electricity per person: light / power", "kWh", 1917, "124 / 372", "Census of Electrical Industries 1917", "VERIFIED"),
    ("Washington", "Central stations and electric railways: electricity generated", "m kWh", 1917, 869, "Census of Electrical Industries 1917", "VERIFIED"),
    ("US", "Manufacturing: electric motors' share of mechanical drive", "share", 1899, 0.048, "Devine (1983), Table 3 (475 of 9,853 thousand hp)", "VERIFIED"),
    ("US", "Manufacturing: electric motors' share of mechanical drive", "share", 1909, 0.247, "Devine (1983), Table 3 (4,582 of 18,563)", "VERIFIED"),
    ("US", "Manufacturing: electric motors' share of mechanical drive", "share", 1919, 0.531, "Devine (1983), Table 3 (15,612 of 29,394)", "VERIFIED"),
    ("US", "Manufacturing: electric motors' share of mechanical drive", "share", 1929, 0.784, "Devine (1983), Table 3 (33,844 of 43,158)", "VERIFIED"),
    ("US", "Manufacturing: electric motor capacity", "thousand hp", 1929, 33844, "Devine (1983), Table 3", "VERIFIED"),
    ("California", "Crude oil output", "m bbl", 1931, 188, "Minerals Yearbook 1932–33, chart p. 472 (read from the bars, ±3)", "VERIFIED"),
    ("Texas", "Crude oil output", "m bbl", 1932, 312, "Minerals Yearbook 1932–33, chart p. 472 (read from the bars, ±3)", "VERIFIED"),
    ("Oklahoma", "Crude oil output", "m bbl", 1932, 153, "Minerals Yearbook 1932–33, chart p. 472 (read from the bars, ±3)", "VERIFIED"),
    ("California", "Largest fields", "rank", 1932, "Long Beach, Santa Fe Springs, Kettleman Hills", "Minerals Yearbook 1932–33, p. 472", "VERIFIED"),
]
# California 1932 oil and the Devine shares now verified
for i, f in enumerate(ANCHOR_FACTS):
    if f[0] == "California" and f[1] == "Crude oil output" and f[3] == 1932:
        ANCHOR_FACTS[i] = f[:5] + ("Minerals Yearbook 1932–33, chart p. 472 (about 178)", "VERIFIED")
    if f[1] == "Factory horsepower on electric drive":
        ANCHOR_FACTS[i] = f[:4] + ({1909: 0.247, 1919: 0.531, 1929: 0.784}[f[3]], "Devine (1983), Table 3", "VERIFIED")

EVENTS += [
    (1882, "Los Angeles City and Puente–Brea fields (CR-052 C)", "Fuels (oil_c52)", "CR-052 CT3 C", "APPROVED (dates MODEL)"),
    (1885, "Kern River field (CR-052 C)", "Fuels (oil_c52)", "CR-052 CT3 C", "APPROVED (dates MODEL)"),
    (1895, "Huntington Beach found by the survey (CR-052 C)", "Fuels (oil_c52)", "CR-052 CT3 C", "APPROVED (dates MODEL)"),
    (1902, "Signal Hill and Santa Fe Springs with rotary drilling (CR-052 C)", "Fuels (oil_c52)", "CR-052 CT3 C", "APPROVED (dates MODEL)"),
    (1915, "Kettleman Hills and Wilmington (CR-052 C)", "Fuels (oil_c52)", "CR-052 CT3 C", "APPROVED (dates MODEL)"),
]


# =====================================================================================
# Third revision (after the fresh-context review of the third build, 3 November 2026)
# =====================================================================================
# 1. Oilfields modelled field by field: what the Story and Max paths, the plausible
#    output (oil_cap) and the known reserves (oil_known) all come from.
# Each field: canon discovery year, flush peak rate if developed in the 1920s manner
# (m bbl/yr), and primary recovery with the methods of 1900-1930 (bn bbl). All MODEL;
# historical discovery years, peaks and recoveries to verify.
OILFIELDS = [
    # name, canon year, historical year, peak, primary URR
    ("Los Angeles City", 1882, 1892, 2, 0.06),
    ("Puente, Brea–Olinda, Whittier, Fullerton", 1882, 1880, 10, 0.5),
    ("Kern River", 1885, 1899, 17, 0.6),
    ("Coalinga", 1890, 1896, 18, 0.7),
    ("McKittrick", 1891, 1898, 5, 0.1),
    ("Midway–Sunset", 1893, 1901, 45, 1.0),
    ("Huntington Beach", 1895, 1920, 35, 0.8),
    ("Lost Hills and Belridge", 1898, 1910, 10, 0.3),
    ("Signal Hill (Long Beach)", 1902, 1921, 90, 0.9),
    ("Santa Fe Springs", 1903, 1919, 80, 0.6),
    ("Elk Hills", 1905, 1919, 25, 0.6),
    ("Buena Vista", 1906, 1909, 20, 0.6),
    ("Torrance, Richfield, Montebello", 1906, 1922, 30, 0.65),
    ("Kern Front, Round Mountain, Mount Poso", 1908, 1912, 15, 0.4),
    ("Ventura Avenue", 1910, 1916, 30, 0.7),
    ("Dominguez, Rosecrans, Inglewood, Seal Beach", 1910, 1923, 30, 0.65),
    ("Wilmington", 1915, 1932, 40, 1.2),
    ("Kettleman Hills North Dome", 1923, 1928, 35, 0.45),
]


def _era(y):
    """How hard a field found in year y is developed at first: fewer rigs and smaller markets early."""
    return 0.5 if y < 1895 else 0.7 if y < 1905 else 0.85 if y < 1915 else 1.0


def _ramp(y):
    return 5 if y < 1900 else 3 if y < 1910 else 2


def field_model(utilization=1.0):
    """Deliverable output by year (m bbl) and known primary reserves (bn bbl, fields found by then).

    A field ramps linearly to its peak (era-scaled) over its ramp years, then declines
    exponentially at the rate that exhausts its primary recovery: remaining = q / d.
    `utilization` scales the whole field model (production below deliverability)."""
    out = {y: 0.0 for y in range(1846, 1933)}
    known = {y: 0.0 for y in range(1846, 1933)}
    for name, y0, yh, peak, urr in OILFIELDS:
        q = peak * _era(y0)
        n = _ramp(y0)
        cum = 0.0
        d = None
        for y in range(y0, 1933):
            known[y] += urr
            if y < y0 + n:
                p = q * (y - y0 + 1) / n
            else:
                if d is None:
                    rem = max(urr * 1000 - cum, q)
                    d = q / rem
                p = q * (1 - d) ** (y - (y0 + n))
            p = min(p, max(0.0, urr * 1000 - cum))
            out[y] += p * utilization
            cum += p
    return out, known


_cap, _known = field_model(1.0)
_compact = {1932: 0.85}  # CR-020 B6: the oil compact holds output down in 1932
_story = {y: v * 0.85 * _compact.get(y, 1.0) for y, v in _cap.items()}
_max = {y: v * 1.0 * _compact.get(y, 1.0) for y, v in _cap.items()}
_basis_fields = "; ".join(f"{n} {c} (hist. {h}), peak {p}m, {u}bn" for n, c, h, p, u in OILFIELDS)

path("oil_cap", "Plausible output of the home oilfields (field model)", "m bbl", {y: round(v, 2) for y, v in _cap.items()},
     "Sum over the fields found by each year: each ramps to its peak (scaled down for early, smaller-market development: "
     "×0.5 before 1895, ×0.7 to 1905, ×0.85 to 1915) and then declines at the rate its primary recovery allows. Fields "
     "(canon year, historical year, peak, primary recovery; to verify): " + _basis_fields + ".")
path("oil_known", "Primary reserves of the fields found (cumulative)", "bn bbl", {y: round(v, 3) for y, v in _known.items()},
     "Primary recovery with 1900–1930 methods only (no steam flood or water flood), summed over the fields found by each year. "
     "Kern River and Midway–Sunset hold far more oil, but most of it came out by steam after the 1960s.")
path("oil_c52", "Home oil output, CR-052 discovery path (85% of the field model)", "m bbl", {y: round(v, 2) for y, v in _story.items()},
     "Approved CT3 C: the 1876 survey finds the fields listed under oil_cap, from the early 1880s. Story produces 85% of what the "
     "fields could deliver; 1932 is held down by the oil compact. Kettleman Hills needs a 7,000 ft well: about 1923 at the earliest.",
     "APPROVED (CR-052 CT3 C), MODEL")
PATHS_MAX["oil_c52"] = {y: round(v, 2) for y, v in _max.items()}

# dry gas: Kettleman's gas only from 1923
path("dry_gas", "Dry gas fields (Rio Vista, Buttonwillow; Kettleman from 1923)", "PJ", {1846: 0, 1905: 0, 1913: 10, 1920: 35, 1923: 45,
     1929: 110, 1932: 120}, "With C: the Sacramento Valley's dry gas found early (Rio Vista historically 1936; Buttonwillow 1927); "
     "Kettleman Hills' gas after its discovery about 1923. Piped to the Bay cities.", "APPROVED with CT3 C, MODEL")
PATHS_MAX["dry_gas"] = {1846: 0, 1900: 0, 1905: 5, 1913: 20, 1920: 50, 1923: 65, 1929: 160, 1932: 180}

# 2. Vehicles: fewer in 1913 (California had about 0.045 per person historically)
path("veh_pp", "Motor vehicles on the road per person", "per person", {1846: 0, 1900: 0, 1905: 0.001, 1910: 0.008, 1913: 0.025,
     1917: 0.07, 1920: 0.14, 1924: 0.24, 1927: 0.30, 1929: 0.33, 1932: 0.33},
     "Approved CT5 (amended). US 1913 about 0.013, 1929 0.22; historical California 1913 about 0.045 (to verify). California at 1.25 times "
     "the Realm's rate (0.41 in 1929) is the most motorized place on earth.", "APPROVED (CR-052 CT5), MODEL")
PATHS_MAX["veh_pp"] = {1846: 0, 1900: 0, 1905: 0.001, 1910: 0.01, 1913: 0.03, 1917: 0.08, 1920: 0.16, 1924: 0.27, 1927: 0.33,
                       1929: 0.36, 1932: 0.36}

# 3. Max diverges from Story after the war: multiplier paths instead of constant levers
path("indw_x", "Industrial weight multiplier (× ind_w)", "×", {1846: 1, 1932: 1}, "Story 1. Max rises after 1915 as process heat electrifies.")
path("hyd_x", "Hydro building multiplier (× hydro_pace)", "×", {1846: 1, 1932: 1}, "Story 1. Max builds faster after 1915.")
path("nwboil", "Electric boilers in Northwest pulp, paper and lumber mills", "GWh", {1846: 0, 1932: 0},
     "Max only: secondary spring and summer hydro sold to mill boilers, as Canada did in the 1920s and 1930s.")
path("tie_mw", "California–Northwest transfer capacity", "MW", {1846: 0, 1932: 0},
     "No 1920s line could carry Columbia power to California (the Pacific Intertie came in 1968). Zero in every case unless the author adds one.")
PATHS_MAX.update({
    "indw_x": {1846: 1, 1915: 1, 1920: 1.2, 1925: 1.45, 1929: 1.5, 1932: 1.5},
    "hyd_x": {1846: 1, 1915: 1, 1920: 1.15, 1925: 1.3, 1932: 1.35},
    "nwboil": {1846: 0, 1921: 0, 1925: 2000, 1929: 5000, 1932: 7000},
    "elec_home": {1880: 0, 1890: 0.01, 1900: 0.09, 1907: 0.22, 1913: 0.44, 1917: 0.6, 1920: 0.72, 1924: 0.86, 1927: 0.93, 1929: 0.96, 1932: 0.97},
    "kwh_home": {1890: 150, 1900: 220, 1913: 330, 1917: 450, 1920: 600, 1924: 1000, 1927: 1400, 1929: 1700, 1932: 2000},
    "kwh_comm": {1885: 0, 1890: 3, 1900: 27, 1913: 90, 1920: 150, 1927: 230, 1929: 260, 1932: 260},
    "fact_elec": {1885: 0, 1890: 0.01, 1900: 0.09, 1907: 0.22, 1913: 0.42, 1917: 0.55, 1920: 0.66, 1924: 0.8, 1927: 0.87, 1929: 0.91, 1932: 0.93},
    "alu_kt": {1888: 0, 1890: 0, 1895: 0.3, 1900: 2, 1907: 7, 1913: 25, 1917: 50, 1920: 60, 1922: 70, 1924: 95, 1927: 140, 1929: 180, 1930: 160, 1932: 120},
    "alu_col": {1900: 0, 1907: 1, 1913: 8, 1920: 25, 1923: 40, 1924: 60, 1927: 100, 1929: 140, 1932: 95},
    "carb_kt": {1892: 0, 1895: 2, 1900: 15, 1913: 55, 1920: 110, 1927: 190, 1929: 220, 1932: 150},
    "chlor_kt": {1895: 0, 1900: 2, 1913: 22, 1920: 60, 1929: 160, 1932: 140},
    "esteel": {1846: 0, 1900: 0, 1907: 0.003, 1913: 0.015, 1917: 0.06, 1920: 0.08, 1929: 0.2, 1932: 0.22},
    "abras_kt": {1895: 0, 1900: 1, 1913: 7, 1920: 20, 1929: 45, 1932: 40},
    "rail_el": {1846: 0, 1912: 0, 1915: 0.02, 1920: 0.1, 1925: 0.3, 1929: 0.5, 1932: 0.6},
    "rail_kwh": {1888: 0, 1890: 2, 1900: 27, 1907: 65, 1913: 100, 1920: 130, 1924: 135, 1929: 125, 1932: 115},
    "pump_acres": {1890: 0, 1900: 0.02, 1907: 0.25, 1913: 0.9, 1920: 1.7, 1927: 3.0, 1929: 3.6, 1932: 4.0},
    # fuel displaced by Max's electric heat
    "ind_mj": {1846: 40, 1880: 60, 1900: 72, 1913: 65, 1920: 59, 1925: 53, 1929: 47, 1932: 45},
    "gj_home": {1846: 70, 1880: 60, 1900: 55, 1913: 50, 1920: 44, 1925: 40, 1929: 36, 1932: 35},
})
MAX_BASIS = ("Max case: every source Pacifica can reach and every use that can absorb it, diverging from Story after the war. "
             "Electric cooking and water heating (Ontario level), factories fully electric with process heat, aluminium at Alcoa's "
             "scale (180 kt in 1929, bauxite from Guiana and Bintan through partners, to verify), ammonia from electrolytic hydrogen "
             "for the Valley and for Japan, electric steel, half the main lines electric, electric boilers in the Northwest mills, "
             "the Central Valley and Columbia Basin pumped. Fuel paths lowered where electricity replaces heat.")
# 4. Max levers: no double counting, same check bands as Story
for k in ("elec_pace", "kwh_max", "int_hi", "hydro_pace", "ind_w"):
    MAX.pop(k, None)
MAX.update({"eln_col": 1.0})
MAX_NOTES.pop("kwh_max", None)
MAX_NOTES["ind_w"] = "Max case: the weight stays 0.5; Paths indw_x raises it after 1915 as process heat electrifies."
LEVERS[:] = [lv for lv in LEVERS if not (len(lv) > 1 and lv[0] == "nw_ord")]

# Fields left out of the first list, and secondary recovery in the Max case
OILFIELDS += [
    ("Santa Maria, Orcutt, Lompoc, Cat Canyon", 1895, 1901, 12, 0.3),
    ("Deeper zones under the old fields (rotary, 3,000–6,000 ft)", 1918, 1922, 60, 1.2),
    ("Edison, Mountain View, Ten Section", 1920, 1928, 25, 0.6),
    ("Playa del Rey, Venice, Huntington tidelands", 1922, 1929, 25, 0.6),
]


def field_model2(urr_mult=1.0):
    """field_model with every field's primary recovery scaled (Max: pressure maintenance and water flooding)."""
    global OILFIELDS
    saved = OILFIELDS
    OILFIELDS = [(n, y, h, p, u * urr_mult) for n, y, h, p, u in saved]
    try:
        return field_model(1.0)
    finally:
        OILFIELDS = saved


_cap, _known = field_model2(1.0)
_capm, _knownm = field_model2(1.3)
_story = {y: v * 0.9 * _compact.get(y, 1.0) for y, v in _cap.items()}
_max = {y: v * 1.0 * _compact.get(y, 1.0) for y, v in _capm.items()}
_basis_fields = "; ".join(f"{n} {c} (hist. {h}), peak {p}m, {u}bn" for n, c, h, p, u in OILFIELDS)
for key, pts in [("oil_cap", _cap), ("oil_known", _known), ("oil_c52", _story)]:
    lab, unit, _old, basis, status = PATHS[key]
    if key == "oil_cap":
        basis = basis.split("Fields (canon year")[0] + "Fields (canon year, historical year, peak, primary recovery; to verify): " + _basis_fields + "."
    if key == "oil_c52":
        lab = "Home oil output, CR-052 discovery path (90% of the field model)"
        basis = basis.replace("Story produces 85%", "Story produces 90%")
    PATHS[key] = (lab, unit, {y: round(v, 3) for y, v in pts.items()}, basis, status)
PATHS_MAX["oil_c52"] = {y: round(v, 3) for y, v in _max.items()}
PATHS_MAX["oil_cap"] = {y: round(v, 3) for y, v in _capm.items()}
PATHS_MAX["oil_known"] = {y: round(v, 3) for y, v in _knownm.items()}
MAX_BASIS += (" Oil: pressure maintenance and water flooding about fifteen years before history raise every field's recovery by 30% "
              "(oil_cap, oil_known and oil_c52 Max rows).")

# The financial workbook's oil path (oil_src = 1) is tested against the same fields at
# their historical discovery years.
def field_model_hist():
    global OILFIELDS
    saved = OILFIELDS
    OILFIELDS = [(n, h, h, p, u) for n, y, h, p, u in saved]
    try:
        return field_model(1.0)
    finally:
        OILFIELDS = saved


_caph, _knownh = field_model_hist()
path("oil_caph", "Plausible output of the home oilfields at their historical discovery years", "m bbl", {y: round(v, 3) for y, v in _caph.items()},
     "As oil_cap, with each field found in its historical year; the test for the financial workbook's own oil path (oil_src = 1).")
path("oil_knownh", "Primary reserves of the fields found, at historical discovery years", "bn bbl", {y: round(v, 3) for y, v in _knownh.items()},
     "As oil_known, at historical discovery years.")
MAX.update({"colms_max": 1500, "colms_rate": 300})


# =====================================================================================
# Fourth revision, 4 November 2026: the narrowed Max case goes into Story
# (CR-052 decision of 4 November, outputs/CR-052/review-3.md) and the CR-053
# concessions join the import ceiling.
# =====================================================================================
# Author, 4 November 2026, on the narrowed take: "that sounds reasonable"; on the
# concessions: "conc_* import paths also good to go". Into Story: M1 (electric homes),
# M6 (half the main lines), M7 (Boulder decided 1920, first power 1926; no mid-Columbia
# chain, which collides with CR-051 S7), M8 (pressure maintenance and water flooding
# fifteen years early; vehicles stay on the CT5 path), M9 (electric boilers in the
# Northwest mills; the Columbia's electrochemistry sized to the unchanged M3).
# Not into Story: M2 (industrial weight, referred to the financial workbook; electric
# process heat only in the Northwest), M3 and M4 (sent back for rework), M5 (held).
# Max keeps its full parts except the chain, as the exploration case.

def _story_takes_max(key):
    """Story adopts the Max path for `key`; Max's row stays identical."""
    lab, unit, _old, basis, status = PATHS[key]
    PATHS[key] = (lab, unit, dict(PATHS_MAX[key]), basis + " 4 Nov 2026: Story takes the Max path (CR-052 Max decision).",
                  "APPROVED direction (CR-052, 4 Nov), MODEL")


# M1: electric homes (Ontario level); rural electrification through the county grids.
for _k in ("elec_home", "kwh_home"):
    _story_takes_max(_k)
# M6: half the main lines electric by 1929; the 1914–18 oil strain as the motive.
for _k in ("rail_el", "rail_kwh"):
    _story_takes_max(_k)
# M7: hydro 35% faster after 1915; Boulder decided 1920, first power 1926. No chain.
_story_takes_max("hyd_x")
set_lever("boulder_dec", story=1920, stress=1928, status="APPROVED direction (CR-052 Max M7, 4 Nov)",
          basis="4 Nov 2026: decided 1920, first power 1926 (Story). Nevada, Arizona and the Western Slope are all Pacifican, so there is "
                "no interstate-compact decade; the peoples of the reach consent under CR-033. Stress keeps the historical 1928.")
set_lever("boulder_lead", story=6, stress=7)
set_lever("colms_on", story=0, stress=0, status="OFF (CR-052 CT8, 4 Nov)",
          basis="A 1.5 GW chain before 1932 collides with CR-051 S7 (Rock Island the first main-stem dam; no dam at Priest Rapids; "
                "not yet Grand Coulee). Off in every case; a later CR may add named sites with consents.")
MAX.pop("colms_on", None); MAX.pop("colms_dec", None); MAX.pop("colms_rate", None); MAX.pop("colms_max", None)
# M8: pressure maintenance and water flooding about fifteen years early, in Story too.
# Story still produces 90% of what the fields can deliver; Max 100%.
_cap13, _known13 = field_model2(1.3)
_story = {y: v * 0.9 * _compact.get(y, 1.0) for y, v in _cap13.items()}
for key, pts in [("oil_cap", _cap13), ("oil_known", _known13), ("oil_c52", _story)]:
    lab, unit, _old, basis, status = PATHS[key]
    if key == "oil_c52":
        basis += (" 4 Nov 2026 (Max M8 into Story): pressure maintenance and water flooding from the 1910s raise every field's "
                  "primary recovery by 30%; Story still produces 90% of deliverability.")
    else:
        basis += " 4 Nov 2026: with early pressure maintenance and water flooding (recovery × 1.3), in Story as in Max."
    PATHS[key] = (lab, unit, {y: round(v, 3) for y, v in pts.items()}, basis, status)
# M9: electric boilers in the Northwest mills; the Columbia's electrochemistry stays at
# Story's M3 size (rework pending).
_story_takes_max("nwboil")

# CR-053: oil abroad. Entitlement crude from minority stakes and the Gulf-coast options,
# added to "Most oil that can be imported" (Fuels imp_max) in every case. MODEL.
path("conc_ven", "CR-053 P1: Lake Maracaibo entitlement (minority stake in Lago Petroleum)", "m bbl",
     {1846: 0, 1923: 0, 1924: 0.5, 1926: 3, 1929: 9, 1932: 12},
     "Author, 4 Nov 2026 (company: Lago, bought from the independents in 1923–24 before Standard of Indiana). Venezuela about 137m bbl "
     "in 1929 (to verify); a fifth to a quarter of a company holding about a quarter of the lake. Shipped through the canal.",
     "PROPOSED (CR-053 P1), MODEL")
path("conc_col", "CR-053 P2: De Mares entitlement (minority stake in Tropical Oil)", "m bbl",
     {1846: 0, 1920: 0, 1926: 1, 1927: 2, 1929: 4, 1932: 5},
     "Stake taken 1920–21 as International Petroleum assembles Tropical Oil; Andian pipeline to Cartagena 1926 (to verify).",
     "PROPOSED (CR-053 P2), MODEL")
path("conc_peru", "CR-053 P3: the Peruvian position (Lobitos and the northern concessions; Union minority)", "m bbl",
     {1846: 0, 1923: 0, 1924: 2, 1926: 4, 1929: 7, 1932: 7},
     "Pacifican company from about 1924, the Union holding a reciprocal fifth. Peru about 13m bbl in 1929 (to verify). The pre-1901 "
     "Peruvian imports are in other_imp.", "PROPOSED (CR-053 P3), MODEL")
path("conc_bah", "CR-053 P4: Bahrain (Holmes's option, 1926; nationality clause waived 1927)", "m bbl",
     {1846: 0, 1931: 0, 1932: 0.3}, "First oil June 1932 (historical, to verify); nothing before.", "PROPOSED (CR-053 P4), MODEL")
path("conc_kuw", "CR-053 P4: Kuwait (Holmes's option, 1926)", "m bbl", {1846: 0, 1932: 0},
     "Burgan struck 1938 historically; nothing in the window.", "PROPOSED (CR-053 P4), MODEL")
path("conc_mes", "CR-053 P5: the Mesopotamian share (with the Union's group, 1928)", "m bbl", {1846: 0, 1932: 0},
     "Kirkuk's pipeline to the Mediterranean opens 1934 historically; nothing in the window. Pacifica joins the American group "
     "(author, 4 Nov 2026) rather than displacing it.", "PROPOSED (CR-053 P5), MODEL")
CONC_KEYS = ["conc_ven", "conc_col", "conc_peru", "conc_bah", "conc_kuw", "conc_mes"]

MAX_BASIS = ("Max case (exploration, 4 Nov 2026): what Story does not yet take — factories fully electric with process heat "
             "(indw_x), aluminium at Alcoa's scale, ammonia from electrolytic hydrogen, electric steel; M3 and M4 await rework. "
             "The mid-Columbia chain is off in every case (CR-051 S7). Max produces 100% of the fields' deliverability.")

EVENTS += [
    (1920, "Boulder Canyon decided; first power 1926 (CR-052 Max M7 into Story)", "Hydro (Boulder)", "CR-052, 4 Nov", "APPROVED direction (MODEL)"),
    (1915, "Main-line electrification begins on the mountain crossings; half the traffic by 1929 (M6)", "Uses (rail_el)", "CR-052, 4 Nov", "APPROVED direction (MODEL)"),
    (1921, "Tropical Oil (De Mares) minority stake", "Fuels (conc_col)", "CR-053 P2", "PROPOSED"),
    (1923, "Lago Petroleum (Maracaibo) minority stake", "Fuels (conc_ven)", "CR-053 P1", "PROPOSED"),
    (1924, "Peruvian position with the Union's reciprocal minority", "Fuels (conc_peru)", "CR-053 P3", "PROPOSED"),
    (1926, "Holmes's Bahrain and Kuwait options bought", "Fuels (conc_bah, conc_kuw)", "CR-053 P4", "PROPOSED"),
    (1927, "Settlement with Britain: nationality clause waived; Mesopotamian share with the Union's group (1928)", "Fuels (conc_mes)", "CR-053 P4, P5", "PROPOSED"),
]
EVENTS[:] = [e for e in EVENTS if not e[1].startswith("Boulder Canyon decision (historical date)")]

# Stress stays the lean case: it keeps the fourth build's Story shape where Story has
# now taken a Max part (kWh per home, mill boilers, the hydro pace); Boulder stays 1928
# and the main lines stay steam there (mainline_on = 0, as before).
LEVERS += [
    ("— CR-052 fourth revision (4 Nov 2026): Stress scaling of the parts Story took from Max —",),
    ("home_kwh_x", "Electricity per home (× Paths kwh_home)", 1.0, 0.5, "×", "Model estimate",
     "Story and Max: Ontario-level electric cooking and water heating (M1). Stress: half, about the fourth build's Story path (850 kWh a home in 1929)."),
    ("nwboil_x", "Electric boilers in the Northwest mills (× Paths nwboil)", 1.0, 0.0, "×", "Model estimate",
     "Story and Max: secondary spring and summer hydro sold to the mills (M9). Stress: none."),
]
LEVERS.append(("hydx_on", "Apply the post-1915 hydro multiplier Paths hyd_x (M7; 1 = yes)", 1, 0, "switch", "Model estimate",
               "Story and Max build hydro 35% faster after 1915 (M7). Stress keeps the fourth build's pace (0.7 of Story before M7)."))
MAX["hydx_on"] = 1


# =====================================================================================
# Fifth revision, 4 November 2026: fuel security (the five additions of review-3's
# oil question), CT6 (Hilo on windward hydro through a Hawaiian hydro board) and the
# 1932 oil compact as a price floor. Author: "Yes please" (4 Nov 2026).
# =====================================================================================
LEVERS += [
    ("— CR-052 fifth revision (4 Nov 2026): fuel security and Hilo —",),
    ("dual_x", "Dual-fuel share of the flexible oil demand (× Paths dual_share)", 1.0, 0.85, "×", "Model estimate",
     "Story and Max: the coastal stations and railways are built coal-capable by policy, the oil programme's twin. Stress: 15% less of the plant can switch."),
    ("stock_days", "Oil stocks held (days of last year's products use)", 75, 45, "days", "Model estimate",
     "Navy reserve plus commercial tankage. Drawn in a short year, refilled from surplus in a long one (Fuels stk)."),
    ("prio", "Ration exports and motor fuel before putting industry on coal (1 = yes)", 1, 1, "switch", "Model estimate",
     "Policy order in a short year: stocks, then the trust's Asian exports (up to exp_cut), then motor fuel (up to mf_cut), then the switch to coal, then unmet demand."),
    ("exp_cut", "Most of the trust's Asian exports that can be cut in a short year", 0.5, 0.5, "share", "Model estimate", "Contracts allow half to be deferred."),
    ("mf_cut", "Most motor fuel that can be rationed in a short year", 0.15, 0.15, "share", "Model estimate", "Pleasure driving; 1917–18 style."),
    ("coal_ramp", "Most that Realm coal output can rise in a year", 0.10, 0.08, "share", "Model estimate",
     "Mines, cars and the Utah–Los Angeles line: about a tenth a year, plus 1 Mt of slack. Above it the cascade goes to wood, imports and 'coal beyond reach'."),
    ("compact_on", "1932 oil compact cuts output (1 = yes; 0 = a price floor, no cut)", 0, 1, "switch", "PROPOSED (CR-052, 4 Nov)",
     "Review-3: a 15% cut in the year the Gulf ceiling also falls is the model's one real bottleneck. Story: the compact is a price floor; Stress keeps the cut."),
    ("unmet_max", "Oil demand left unmet: most allowed (share of the flexible demand)", 0.02, 0.02, "share", "Model estimate", "Check 10."),
]
set_lever("hilo_src", story=2, stress=2, status="APPROVED (CR-052 CT6, 4 Nov 2026)",
          basis="Author, 4 Nov 2026: Hilo on windward hydro through a Hawaiian hydro board (Paths h_hilo), whose twelve-year bonds are the 1932 price problem. "
                "1 = oil-fired steam (superseded).")
MAX.update({"hilo_src": 2, "compact_on": 0})

path("dual_share", "Share of the flexible oil demand at plants and locomotives that can burn coal", "share",
     {1846: 1, 1890: 1, 1900: 0.95, 1913: 0.85, 1920: 0.75, 1929: 0.65, 1932: 0.65},
     "Interior railways and stations burn coal anyway; coastal stations and the Pacific lines are built dual-fuel by policy; the share falls as oil-only plant spreads in the 1920s.",
     "PROPOSED (CR-052, 4 Nov), MODEL")
path("h_hilo", "Hydro: the Hawaiian hydro board's Big Island plants (Wailuku, Honoliʻi, Hakalau; CT6)", "MW",
     {1920: 0, 1922: 8, 1923: 25, 1924: 45, 1925: 65, 1926: 85, 1927: 105, 1930: 110, 1932: 115},
     "CT6 (approved 4 Nov 2026): built 1922–27 on twelve-year bonds for the 18 kt smelter (about 45 MW average at a 0.45 capacity factor); Waimanu would be the next dam. Not scaled by hydro_pace.",
     "APPROVED (CR-052 CT6), MODEL")
# the 1932 compact leaves the oil paths and is applied in the Fuels formula by compact_on
for key in ("oil_c52",):
    lab, unit, pts, basis, status = PATHS[key]
    PATHS[key] = (lab, unit, {y: round(v / (0.85 if y == 1932 else 1.0), 3) for y, v in pts.items()},
                  basis.replace("; 1932 is held down by the oil compact", "; the 1932 oil compact is applied by the lever compact_on"), status)
PATHS_MAX["oil_c52"] = {y: round(v / (0.85 if y == 1932 else 1.0), 3) for y, v in PATHS_MAX["oil_c52"].items()}

EVENTS += [
    (1922, "Hawaiian hydro board: Big Island windward plants begun (1922–27)", "Hydro (h_hilo); Strategic loads (Hilo)", "CR-052 CT6", "APPROVED (MODEL)"),
]
EVENTS[:] = [e if not e[1].startswith("Hilo aluminium built") else (e[0], e[1], e[2], e[3], "CANON; power: hydro board (CT6)") for e in EVENTS]


# =====================================================================================
# Sixth revision, 4 November 2026 (seventh build): after Sol's review of the finance
# note. Process heat is its own switch; a calibration hook for the finance workbook's
# industrial series; the Fund's credit capped; revenue split.
# =====================================================================================
LEVERS += [
    ("— CR-052 sixth revision (4 Nov 2026): the finance calibration —",),
    ("heat_el", "Electrified process heat in factories (1 = yes; applies Paths indw_x)", 0, 0, "switch", "Model estimate",
     "Max case only. Kept apart from the industrial weight so that a higher finance weight (Paths ind_idx) is never multiplied by it."),
    ("self_gen", "Share of electricity that is industrial self-generation, not utility sales", 0.2, 0.25, "share", "Model estimate",
     "US industrial plants made about a third of electricity in the 1920s (to verify); Pacifica's champions less, on utility hydro."),
]
MAX.update({"heat_el": 1})
path("ind_idx", "Industrial output per real dollar of GDP, relative to 1913 (finance calibration)", "×", {1846: 1, 1932: 1},
     "Hook for the financial workbook's next build (claude/finance-investment-share-note.md v2): the domestic industrial output series "
     "derived from the investment mix, domestic sourcing and manufactured exports, checked against steel and vehicles, indexed to 1913. "
     "Scales ind_w (factory motors) and ind_mj (industrial fuel) together. 1 until finance exports it; Sol's proportional estimate is "
     "about 1.08 by 1929 (ind_w 0.50 to 0.54).", "PROPOSED (awaiting finance), MODEL")


# =====================================================================================
# Seventh revision, 4 November 2026 (eighth build): CR-054, the energy-intensive
# champions reworked — aluminium at Alcoa's scale absorbed at home and in the Concord,
# nitrogen for the Valley and the Concord's own market, electric steel at 12%.
# Author, 4 Nov 2026: "The amounts and the division of labor makes sense."
# =====================================================================================
def _set_story(key, points, note):
    lab, unit, _old, basis, status = PATHS[key]
    PATHS[key] = (lab, unit, points, basis + " " + note, "APPROVED direction (CR-054, 4 Nov), MODEL")


_set_story("alu_kt", {1888: 0, 1890: 0, 1895: 0.3, 1900: 2, 1907: 6, 1913: 22, 1917: 45, 1920: 52, 1922: 60, 1924: 85, 1927: 125, 1929: 150, 1930: 135, 1932: 120},
           "CR-054 A1: about 150 kt in 1929, half the world's output; the grid's conductor, the fleet's aircraft, the Concord pool, civil uses, a third exported.")
_set_story("alu_col", {1900: 0, 1907: 1, 1913: 6, 1920: 16, 1923: 22, 1924: 35, 1927: 55, 1929: 70, 1932: 55},
           "CR-054 A1: the Columbia (Wenatchee and the Rock Island reach) about 70 kt in 1929.")
_set_story("alu_wen", {1922: 0, 1923: 0, 1924: 10, 1925: 15, 1927: 20, 1929: 25, 1932: 18}, "CR-054 A1.")
_set_story("eln_kt", {1846: 0, 1924: 0, 1925: 5, 1927: 25, 1929: 60, 1932: 65},
           "CR-054 A2: electrolytic ammonia on the Columbia from 1925 (Haber synthesis on hydrogen from the river's secondary power), about 60 kt N by 1929, for the Valley, the Columbia Basin, Hawaii, the Philippines and the China trade; not Japan's market.")
_set_story("haber_kt", {1924: 0, 1925: 2, 1927: 10, 1929: 30, 1932: 35},
           "CR-054 A2: Haber–Bosch on Sacramento Valley gas for the Bay and the south, about 30 kt N by 1929; the licence bought from BASF, not seized.")
_set_story("esteel", {1907: 0, 1913: 0.01, 1917: 0.05, 1920: 0.06, 1929: 0.12, 1932: 0.12}, "CR-054 A5: 12% of steel electric by 1929, for the aircraft and electrical champions' alloys.")
for _k in ("carb_kt", "chlor_kt", "abras_kt"):
    lab, unit, pts, basis, status = PATHS[_k]
    PATHS[_k] = (lab, unit, {y: round(v * (1.2 if y >= 1920 else 1.0 + 0.2 * max(0, y - 1913) / 7), 2) for y, v in pts.items()},
                 basis + " CR-054 A5: about 1.2 times the earlier path from 1920.", "APPROVED direction (CR-054, 4 Nov), MODEL")
set_lever("eln_col", story=1.0, stress=1.0, basis="CR-054 A2: all the electrolytic ammonia on the Columbia.")
# aluminium-use memo (kt), CR-054 A1
path("alu_grid", "Aluminium: steel-cored conductor for the grid (memo)", "kt", {1915: 0, 1917: 3, 1920: 8, 1924: 20, 1927: 30, 1929: 35, 1932: 25},
     "CR-054 A1: Boulder–Los Angeles, the Sierra lines, the Columbia's, the main lines. ACSR's share of US aluminium in the late 1920s to verify.", "Memo (CR-054), MODEL")
path("alu_air", "Aluminium: the Concord fleet's aircraft (memo)", "kt", {1920: 0, 1922: 1, 1925: 3, 1929: 7, 1932: 10},
     "CR-054 A1: carriers from 1922 (canon); all-metal air arm from the mid-1920s; the 1931–32 programme is counter-cyclical.", "Memo (CR-054), MODEL")
path("alu_pool", "Aluminium: the Concord pool, to Japan (memo)", "kt", {1920: 0, 1922: 3, 1925: 10, 1927: 18, 1929: 24, 1932: 22},
     "CR-054 A1, A3: Japan's navy and electrical industry; Japan builds no aluminium industry against Pacifica's before 1937.", "Memo (CR-054), MODEL")
path("alu_civil", "Aluminium: civil uses at home (memo)", "kt", {1900: 1, 1913: 10, 1920: 20, 1929: 38, 1932: 30},
     "CR-054 A1: cookware, vehicles, rail cars, film equipment, electrical castings.", "Memo (CR-054), MODEL")
EVENTS += [
    (1925, "Electrolytic ammonia on the Columbia; the grid's aluminium conductor (CR-054)", "Uses (eln_kt, alu_grid)", "CR-054 A1, A2", "APPROVED direction (MODEL)"),
    (1927, "Hayama annex: the Concord's division of labour; the Concord aluminium pool (CR-054)", "Uses (alu_pool)", "CR-054 A3", "APPROVED direction; annex PROPOSED"),
    (1930, "The Concord joins the nitrogen convention as one party; stays outside the European aluminium cartel (CR-054)", "Uses (eln_kt, alu_kt)", "CR-054 A3, A4", "PROPOSED"),
]
