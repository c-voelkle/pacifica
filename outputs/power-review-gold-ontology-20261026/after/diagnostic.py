"""Bounded fixed-output royalty replay; reads only the inherited JSON."""
from decimal import Decimal as D
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
INPUT = ROOT / 'docs/power-review/ontology/inputs/financial-analysis.json'
data = json.loads(INPUT.read_text(encoding='utf-8'), parse_float=D)
rows = [r for r in data['baseline_rows'] if 1849 <= r['year'] <= 1852]
output = sum(r['output_musd'] for r in rows)
baseline = output * D('.05') * D('.9')
sweep = []
for rate in (D('.03'), D('.05')):
    for collection in (D('.5'), D('.7'), D('.9'), D('1')):
        gross = output * rate * collection
        sweep.append(dict(rate=str(rate), collection=str(collection), gross_musd=str(gross),
                          delta_musd=str(gross-baseline), net_musd=None,
                          missing_reason='Incremental collection costs and output/avoidance response unestimated.'))
result = {
    'method': 'Decimal arithmetic from inherited JSON baseline_rows; no workbook access.',
    'input_path': INPUT.relative_to(ROOT).as_posix(),
    'input_sha256_exact_bytes': hashlib.sha256(INPUT.read_bytes()).hexdigest(),
    'scope': 'California public royalty, 1849-1852 period USD millions; gross before further receipt adjustments.',
    'output_musd': str(output), 'baseline_5pct_90pct_gross_musd': str(baseline),
    'sensitivity': sweep,
    'ten_point_collection_gain_at_5pct_musd': str(output * D('.05') * D('.1')),
    'required_collection_at_3pct_fixed_output': str(D('.05')*D('.9')/D('.03')),
    'output_multiplier_for_3pct_full_collection': str(D('.05')*D('.9')/D('.03')),
    'service_net_gain_condition': 'For a collection rise from 0.9 to 1.0 at 5%, incremental 1849-1852 cost plus other losses must be less than $1.185m. No rise is predicted.',
    '1848_excluded': 'Specific adjustment and start timing differ; inherited after-adjustment value 0.11m is not independently replayed.',
    'debt_analogue': 'Inherited 5% coupon on proposed GBP3m gives GBP150000/year only as analogy, with no Pacifican due date or contract inferred.',
    'endpoint_1932_power_delta': None,
    'unmodeled': ['Net policy receipts', 'Policy-to-collection response', 'Output and avoidance response', 'Subsequent investment path', 'Institutional transmission response', '1932 power'],
    'checks': {'output_sum_237': output == D('237'),
               'baseline_replay_within_1e_12': abs(baseline-data['inherited_royalty_1849_1852_musd']) < D('1e-12'),
               'full_collection_3pct_below_baseline': output*D('.03') < baseline,
               'ten_point_gain_1_185': output*D('.05')*D('.1') == D('1.185')},
}
assert all(result['checks'].values())
(OUT/'financial-diagnostic.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'checks': result['checks'], 'gross_baseline_musd': str(baseline)}, indent=2))
