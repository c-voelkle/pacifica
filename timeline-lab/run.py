"""CLI: batch runs, a small lever grid, replay/branch and a single-history export."""
from __future__ import annotations

import argparse
import itertools
import json
import sys
import time
from pathlib import Path

from model import bands, batch, chosen, diverse, outcome_counts, simulate

DEFAULT_SCENARIO = Path(__file__).parent / 'scenarios' / '1927_rescue.yaml'


def grid(scenario, axes, count, levers=None):
    if not axes or len(axes) > 3:
        raise ValueError('Choose one to three grid axes')
    if any(not isinstance(v, list) or not v for v in axes.values()):
        raise ValueError('Each grid axis needs a nonempty list')
    size = math_product(len(v) for v in axes.values())
    if size * count > 100000:
        raise ValueError('Grid exceeds 100,000 world runs; reduce axes or worlds per setting')
    rows = []
    for values in itertools.product(*axes.values()):
        controls = chosen(scenario, {**(levers or {}), **dict(zip(axes, values))})
        runs = batch(scenario, count, controls)
        rows.append(dict(levers=controls, worlds=count,
                         rescue_rate=sum(h.measures['june_payments_met'] for h in runs) / count,
                         consent_rate=sum(h.measures['concord_status_end'] == 'consented' for h in runs) / count,
                         cabinet_survival_rate=sum(h.measures['cabinet_survives'] for h in runs) / count,
                         mean_public_draw=sum(h.measures['public_drawn_musd'] for h in runs) / count,
                         mean_illegal_months=sum(h.measures['months_of_illegal_application'] for h in runs) / count,
                         outcomes=outcome_counts(runs)))
    return rows


def math_product(values):
    result = 1
    for value in values:
        result *= value
    return result


def parse_assignments(entries):
    result = {}
    for entry in entries:
        if '=' not in entry:
            raise ValueError('Use NAME=JSON, for example public_share=0.5')
        name, value = entry.split('=', 1)
        if name in result:
            raise ValueError(f'Duplicate assignment: {name}')
        try:
            result[name] = json.loads(value)
        except json.JSONDecodeError:
            result[name] = value
    return result


def write_json(payload, output):
    text = json.dumps(payload, indent=2, ensure_ascii=False, allow_nan=False)
    if output:
        path = Path(output).resolve()
        repo = Path(__file__).resolve().parent.parent
        # Export never overwrites canon, scenario inputs, code or other repository files.
        exports = Path(__file__).resolve().parent / 'exports'
        if path.is_relative_to(repo) and not path.is_relative_to(exports):
            raise ValueError('Inside the repository, exports must go in timeline-lab/exports/')
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open('x', encoding='utf-8') as stream:
            stream.write(text + '\n')
        print(f'Saved {path}')
    else:
        print(text)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--scenario', type=Path, default=DEFAULT_SCENARIO)
    commands = parser.add_subparsers(dest='command', required=True)
    for command in ('batch', 'grid', 'replay', 'benchmark'):
        p = commands.add_parser(command)
        p.add_argument('--set', action='append', default=[], metavar='NAME=JSON')
        p.add_argument('--output', type=Path)
        if command in ('batch', 'grid'):
            p.add_argument('--worlds', type=int, default=1000)
        if command == 'batch':
            p.add_argument('--start', type=int, default=0)
        if command == 'grid':
            p.add_argument('--axis', action='append', required=True, metavar='NAME=JSON_LIST')
        if command == 'replay':
            p.add_argument('--world', type=int, default=0)
            p.add_argument('--seed', type=int)
            p.add_argument('--branch-month')
            p.add_argument('--change', help='One NAME=JSON decision change')
    args = parser.parse_args(argv)
    try:
        from model import load_scenario
        scenario = load_scenario(args.scenario)
        controls = chosen(scenario, parse_assignments(args.set))
        start = time.perf_counter()
        payload = dict(status='DRAFT / LAB', scenario_hash=scenario.digest, levers=controls,
                       interpretation='Frequencies across LAB assumptions, not calibrated real-world probabilities.')
        if args.command == 'batch':
            runs = batch(scenario, args.worlds, controls, args.start)
            payload.update(worlds=len(runs), start=args.start, outcomes=outcome_counts(runs), bands=bands(runs),
                           different_histories=[h.export(scenario) for h in diverse(runs)])
        elif args.command == 'grid':
            payload['grid'] = grid(scenario, parse_assignments(args.axis), args.worlds, controls)
        elif args.command == 'replay':
            if bool(args.branch_month) != bool(args.change):
                raise ValueError('--branch-month and --change must be used together')
            branch = None
            if args.change:
                key, value = next(iter(parse_assignments([args.change]).items()))
                branch = dict(month=args.branch_month, lever=key, value=value)
            payload = simulate(scenario, args.world, controls, args.seed, branch).export(scenario)
        else:
            payload['benchmarks'] = []
            for count in (1000, 10000):
                tick = time.perf_counter()
                runs = batch(scenario, count, controls)
                elapsed = time.perf_counter() - tick
                payload['benchmarks'].append(dict(worlds=count, seconds=elapsed,
                                                  events=sum(len(h.events) for h in runs), outcomes=outcome_counts(runs)))
                del runs
        payload['elapsed_seconds'] = time.perf_counter() - start
        write_json(payload, args.output)
        return 0
    except (ValueError, OSError, KeyError) as exc:
        print(f'Cannot run sketch: {exc}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
