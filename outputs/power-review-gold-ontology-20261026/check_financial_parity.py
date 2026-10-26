"""Recompute the matched direct fiscal diagnostic from saved pilot inputs only."""
from decimal import Decimal
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = ROOT / 'docs/power-review/ontology/inputs/financial-analysis.json'
D = Decimal


def run():
    source_bytes = SOURCE.read_bytes()
    source = json.loads(source_bytes, parse_float=D)
    checks = []

    def check(name, value, expected):
        passed = abs(value - expected) <= D('0.000000000001')
        checks.append({'id': name, 'passed': passed})
        if not passed:
            raise AssertionError(name)

    output = sum(row['output_musd'] for row in source['baseline_rows'] if 1849 <= row['year'] <= 1852)
    check('same-output-aggregate', output, source['output_1849_1852_musd'])
    benchmark = output * D('0.05') * D('0.90')
    check('same-baseline-gross', benchmark, source['inherited_royalty_1849_1852_musd'])
    rows = []
    for case in source['sensitivity_cases']:
        gross = output * case['rate'] * case['collection']
        check(f"gross-{case['rate']}-{case['collection']}", gross, case['gross'])
        check(f"delta-{case['rate']}-{case['collection']}", gross - benchmark, case['gross_delta_vs_inherited_5pct_90pct_musd'])
        if case['net'] is not None or not case['reason']:
            raise AssertionError('Unestimated net result must stay unavailable with a reason')
        rows.append({'rate': str(case['rate']), 'collection': str(case['collection']),
                     'gross_million_period_USD': str(gross), 'net': None, 'reason': case['reason']})
    ten_point_gain = output * D('0.05') * D('0.10')
    required_collection = D('0.05') * D('0.90') / D('0.03')
    check('same-collection-cost-ceiling', ten_point_gain, source['break_even']['ten_percentage_point_collection_gain_1849_1852_musd'])
    check('same-three-percent-threshold', required_collection, source['break_even']['collection_required_at_3pct_to_match_5pct_90pct'])
    for name in ('alternative_policy_net_result', 'endpoint_1932_power_delta'):
        if source['break_even'][name] is not None:
            raise AssertionError('Unavailable endpoint/net result was supplied unexpectedly')
    report = {'scope': 'Decimal replay of saved 1849–1852 direct royalty diagnostic only; workbook not opened.',
              'source': SOURCE.relative_to(ROOT).as_posix(),
              'source_sha256_exact': hashlib.sha256(source_bytes).hexdigest(),
              'output_million_period_USD': str(output), 'benchmark_gross_million_period_USD': str(benchmark),
              'ten_point_gain_million_period_USD': str(ten_point_gain), 'required_collection_at_3_percent': str(required_collection),
              'cases': rows, 'net_service_result': None, 'endpoint_power_delta': None,
              'missing_reason': 'No new collection-response, cost, investment or institutional-control mechanism was estimated.',
              'checks': checks, 'all_passed': all(row['passed'] for row in checks)}
    (HERE / 'financial-parity.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8', newline='\n')
    print(json.dumps({'checks_passed': len(checks), 'source_unchanged': SOURCE.read_bytes() == source_bytes,
                      'benchmark_gross': str(benchmark), 'power_delta': None}))


if __name__ == '__main__':
    run()
