# Bounded royalty diagnostic

Executable: `diagnostic.py`. Input: `docs/power-review/ontology/inputs/financial-analysis.json`, `$.baseline_rows` for 1849–1852. Output: `financial-diagnostic.json`. The input SHA-256 is recorded in that output and in `input-manifest.json`. No workbook was opened, parsed or recalculated.

Inherited annual output values are 40, 41, 75 and 81 period USD millions: $237m total. Formula is `gross = output × statutory_rate × collection_fraction`. The inherited 5%/90% diagnostic is $10.665m. Values are gross aggregates before collection costs and any further receipt adjustments; they are neither an observed tax series nor discretionary Treasury cash.

| Rate | Collection fraction | Gross $m, 1849–1852 | Difference from 5%/90% $m |
|---:|---:|---:|---:|
| 3% | 0.50 | 3.555 | −7.110 |
| 3% | 0.70 | 4.977 | −5.688 |
| 3% | 0.90 | 6.399 | −4.266 |
| 3% | 1.00 | 7.110 | −3.555 |
| 5% | 0.50 | 5.925 | −4.740 |
| 5% | 0.70 | 8.295 | −2.370 |
| 5% | 0.90 | 10.665 | 0 |
| 5% | 1.00 | 11.850 | +1.185 |

At unchanged output, 3% needs a collection fraction of `0.05 × 0.90 / 0.03 = 1.50`, above the feasible maximum. Equivalently, at full capture it needs 50% more output to match that gross baseline. This is an algebraic threshold, not a predicted output elasticity. At 5%, moving capture from 90% to 100% adds $1.185m gross; incremental service cost and other losses must be lower to improve net revenue under that hypothetical response. No response or cost is estimated.

Four checks executed and passed: summed output equals 237; 5%/90% replay agrees with the inherited gross to 1e−12; full capture at 3% is below that baseline; the ten-point collection increment is 1.185. These checks verify arithmetic, not empirical parameters or policy efficacy. Decimal arithmetic avoids inherited binary-float display noise.

RDF provenance: Q01 is an inherited MODEL parameter aggregate; Q02–Q04/Q08 are independently checked bounded arithmetic; Q05 is explicitly conditional; Q06, Q07 and Q10 retain unmodeled states and reasons. Q09 is an inherited rescue result from the saved finance-review note, not part of this arithmetic replay. No score, century-long growth path or 1932 power difference is computed.

1848 is excluded because first collection and specific receipt adjustments differ; its inherited $0.11m after-adjustment figure is not replayed. The inherited JSON's debt-timing and workbook-component checks are not claimed as executed here. £3m at a 5% coupon would yield £150,000/year only as a historical-analogue sensitivity; no applicable Pacifican coupon or payment date is inferred. Ownership, liabilities, pledges and instrument access still need separate analysis after this gross diagnostic.
