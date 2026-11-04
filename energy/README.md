# Pacifica's energy workbook

Use the [energy workbook](Pacifica_energy_model_1846-1932.xlsx) alongside the [financial workbook](../finance/Pacifica_financial_model_1846-1932.xlsx) and the [current master storyline](../book-agent/revision/master_storyline.md).

**3 November 2026 (CR-052, first build):** fourteen sheets track every source of power in the Realm and Hawaii and what it is used for, 1846–1932, in two layers: primary energy (PJ, with Mtoe) and electricity (MW, GWh). Population, output, industry, oil output, the navy's oil and the atomic stations come from the financial workbook (Story and Stress), so the multiplier of Pacifica's electricity per person against the United States is an output, not an input: about two in the Story case and 2.6–3.6 in the Max case (1920–1932). Three cases on one switch (Levers!E4): Story, Stress and Max. All results are MODEL. See [CR-052-workbook.md](CR-052-workbook.md) for the results and what they mean for canon. SHA-256 `6b3ce6b2342bccd8b186bbe3980113b0ff9520e679c2dfeb6f7e6dd256d6b8ea`, built from the financial workbook with SHA-256 `22266bad58ee60da888c9b8de9bcd2c964498a5427d6b453b1f6a5a46f6120b2`.

## Reproduce

```bash
# 1. Read the financial workbook's Story and Stress results (Stress is recalculated in LibreOffice)
python3 energy/build/extract_finance.py finance/Pacifica_financial_model_1846-1932.xlsx \
    energy/build/finance_inputs.csv --recalc <xlsx skill>/scripts/recalc.py
# 2. Build the energy workbook (formulas only)
python3 energy/build/build_energy_workbook.py energy/build/finance_inputs.csv \
    energy/Pacifica_energy_model_1846-1932.xlsx
# 3. Recalculate in LibreOffice; expect "success", 0 errors (25,687 formulas)
python3 <xlsx skill>/scripts/recalc.py energy/Pacifica_energy_model_1846-1932.xlsx 300
```

Re-run step 1 whenever the financial workbook changes; its SHA-256 is printed on the energy workbook's Start sheet, so a stale import is visible.

## Files

| File | What it is |
| --- | --- |
| `Pacifica_energy_model_1846-1932.xlsx` | The workbook, saved in the Story case and recalculated. |
| `build/energy_inputs.py` | Every lever (Story and Stress), every benchmark path, the historical anchors with source and status, and the events. Edit inputs here and rebuild, or edit the blue cells in the workbook directly. |
| `build/build_energy_workbook.py` | Writes the sheets and formulas. |
| `build/extract_finance.py` | Reads the financial workbook's results for both cases into `finance_inputs.csv`. |
| `build/finance_inputs.csv` | The imported finance series, with the source workbook's SHA-256 on its first line. |
| `CR-052-workbook.md` | Workbook note: changes, results, checks and the questions for the author. |

## Conventions

As in the financial workbook: years down the page (row 6 = 1846, row 92 = 1932); blue = input, black = formula, green = link to another sheet, red = imported from the financial workbook, yellow = key result. `Levers!E4` picks the case (1 = Story, 2 = Stress, 3 = Max) and also picks which finance case feeds `People & output`, so one switch moves the whole system. Paths are given at benchmark years and interpolated by formula; bold blue cells were set, pale italic cells are filled in between.

## Link to the financial workbook

Nothing is pasted either way. The energy workbook reads finance results through the build script, and offers its own results to the financial workbook as named columns on `Finance link`: `en_power_capex`, `en_dev_power_credit`, `en_elec_revenue`, `en_royalties`, `en_oil_import_value`, `en_coal_import_value`, `en_fuel_trade_net`. The financial workbook does not read them yet: that is the next build, once the author approves CR-052.

## Data still to obtain

The building session could not reach census.gov or the USGS PDFs, so most US and state anchors are marked TO VERIFY on the Anchors sheet. Downloads that would settle them:

- *Census of Electrical Industries* 1902–1927 (HathiTrust record 001719357): central-station capacity and output by state.
- *Historical Statistics of the United States*, series S (electric utilities and industrial plants) and A 7 (population).
- USGS Water-Supply Paper 493 (Fowler 1923), *Hydroelectric power systems of California and their extensions into Oregon and Nevada*.
- *Mineral Resources of the United States* / *Minerals Yearbook*: oil, coal and gas by state, 1900–1932.
- Devine (1983), "From shafts to wires", *Journal of Economic History* 43: factory electrification.
- Statistics Norway's historical electricity tables; Swiss and Canadian historical electricity statistics.
