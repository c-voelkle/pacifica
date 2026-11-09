# Pacifica's energy workbook

Use the [energy workbook](Pacifica_energy_model_1846-1932.xlsx) alongside the [financial workbook](../finance/Pacifica_financial_model_1846-1932.xlsx) and the [current master storyline](../book-agent/revision/master_storyline.md).

**Current build (CR-052, CR-054, CR-055; fourteenth):** fourteen sheets track every source of power in the Realm and Hawaii and what it is used for, 1846–1932, in two layers: primary energy (PJ, with Mtoe) and electricity (MW, GWh). Population, output, industry, oil output, the navy's oil and the atomic stations come from the financial workbook (Story and Stress), so the multiplier of Pacifica's electricity per person against the United States is an output, not an input. Three cases on one switch (Levers!E4): Story, Stress and Max. All results are MODEL. See [CR-052-workbook.md](CR-052-workbook.md) for the build history, the results, the checks and what they mean for canon; its first line gives the workbook's SHA-256 and the financial workbook's it was built from.

## Reproduce

The two workbooks read each other (the energy workbook takes population, output and industry; the financial workbook takes home oil, vehicles and the power memos), so they are rebuilt together and iterated until the values stop moving (two or three passes):

```bash
R=<xlsx skill>/scripts/recalc.py
# 1. Read the financial workbook's Story and Stress results (Stress is recalculated in LibreOffice)
python3 energy/build/extract_finance.py finance/Pacifica_financial_model_1846-1932.xlsx energy/build/finance_inputs.csv --recalc $R
# 2. Build the energy workbook and recalculate it; expect "success", 0 errors (29,029 formulas)
python3 energy/build/build_energy_workbook.py energy/build/finance_inputs.csv energy/Pacifica_energy_model_1846-1932.xlsx
python3 $R energy/Pacifica_energy_model_1846-1932.xlsx 300
# 3. Export its Story and Stress results for the financial workbook
python3 energy/build/export_energy.py energy/Pacifica_energy_model_1846-1932.xlsx energy/build/energy_outputs.csv --recalc $R
# 4. Rebuild the financial workbook from the CR-050 workbook (git show 04155c7:finance/Pacifica_financial_model_1846-1932.xlsx),
#    first the CR-052 link, then the CR-051/054/055 build, and recalculate it (62,030 formulas)
python3 finance/build/cr052_energy_link.py CR-050.xlsx energy/build/energy_outputs.csv CR-052.xlsx
python3 finance/build/cr051_054_055_champions.py CR-052.xlsx energy/build/energy_outputs.csv finance/Pacifica_financial_model_1846-1932.xlsx
python3 $R finance/Pacifica_financial_model_1846-1932.xlsx 300
# repeat 1-4 until energy_outputs.csv no longer changes
```

Each workbook records the SHA-256 of the other it was built from (Start sheet here, Energy link A2 there). Because each records the other's, the pair is checked by values: a last pass changes no value.

## Files

| File | What it is |
| --- | --- |
| `Pacifica_energy_model_1846-1932.xlsx` | The workbook, saved in the Story case and recalculated. |
| `build/energy_inputs.py` | Every lever (Story and Stress), every benchmark path, the historical anchors with source and status, and the events. Edit inputs here and rebuild, or edit the blue cells in the workbook directly. |
| `build/build_energy_workbook.py` | Writes the sheets and formulas. |
| `build/extract_finance.py` | Reads the financial workbook's results for both cases into `finance_inputs.csv`. |
| `build/finance_inputs.csv` | The imported finance series, with the source workbook's SHA-256 on its first line. |
| `build/export_energy.py` | Writes the energy results the financial workbook reads (home oil, vehicles, the `en_*` columns, the concession crude; since the CR-051/054/055 build also the strategic dams' capacity, the strategic loads, Rock Island's balance, the aluminium memo and the CR-054/055 quantities; since CR-056 also factory drive, homes wired, pumped acres, the power price, kWh a home, vehicles per person, and industry's motors and the US's electricity per person, not yet read, for the financial workbook's dynamic layer) for both cases. |
| `build/energy_outputs.csv` | Those results, with the energy workbook's SHA-256 on its first line; read by `finance/build/cr052_energy_link.py` and `finance/build/cr051_054_055_champions.py`. |
| `CR-052-workbook.md` | Workbook note: the eleven builds, results for the three cases, checks and the questions for the author. |

## Conventions

As in the financial workbook: years down the page (row 6 = 1846, row 92 = 1932); blue = input, black = formula, green = link to another sheet, red = imported from the financial workbook, yellow = key result. `Levers!E4` picks the case (1 = Story, 2 = Stress, 3 = Max) and also picks which finance case feeds `People & output`, so one switch moves the whole system. Paths are given at benchmark years and interpolated by formula; bold blue cells were set, pale italic cells are filled in between.

## Link to the financial workbook

Nothing is pasted either way. The energy workbook reads finance results through the build script, and offers its own results to the financial workbook as named columns on `Finance link`: `en_power_capex`, `en_dev_power_credit`, `en_elec_revenue`, `en_royalties`, `en_oil_import_value`, `en_coal_import_value`, `en_fuel_trade_net`. Since 4 November the financial workbook reads them through `export_energy.py` and its own build (`finance/CR-052-workbook.md`): oil and vehicles replace its Story paths, the rest are memos and an investment account.

## Data still to obtain

The building session could not reach census.gov or the USGS PDFs, so most US and state anchors are marked TO VERIFY on the Anchors sheet. Downloads that would settle them:

- *Census of Electrical Industries* 1902–1927 (HathiTrust record 001719357): central-station capacity and output by state.
- *Historical Statistics of the United States*, series S (electric utilities and industrial plants) and A 7 (population).
- USGS Water-Supply Paper 493 (Fowler 1923), *Hydroelectric power systems of California and their extensions into Oregon and Nevada*.
- *Mineral Resources of the United States* / *Minerals Yearbook*: oil, coal and gas by state, 1900–1932.
- Devine (1983), "From shafts to wires", *Journal of Economic History* 43: factory electrification.
- Statistics Norway's historical electricity tables; Swiss and Canadian historical electricity statistics.
