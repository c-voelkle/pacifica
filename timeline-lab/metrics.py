"""Named, unit-bearing metrics with scenario inputs and supporting event references."""
from ontology import ENGINE_VERSION, MetricSample


def resolve_input(s, ref):
    kind, _, path = ref.partition(':')
    if kind == 'world':
        role, key = path.split('.', 1)
        value = s.world[s.execution.worlds[role]][key]
    elif kind == 'param':
        role, key = path.split('.', 1)
        value = s.actor(role).params[key]
    elif kind == 'lever':
        value = s.levers[path]
    elif kind == 'coefficient':
        value = s.execution.coefficients[path]
    elif kind == 'drama' and path == 'rules':
        value = s.drama.rules
    elif kind == 'phase':
        value = s.execution.phases[path]
    else:
        raise ValueError(f'Unsupported metric input reference: {ref}')
    return value.model_dump() if hasattr(value, 'model_dump') else value


def samples(s, h):
    end = h.series[-1]
    first = lambda action: next((e['month'] for e in h.events if e['action'] == action), None)
    consent = next((row['month'] for row in h.series if row['concord'] == 'consented'), None)
    commitments = h.semantics.get('commitments', [])
    extra = dict(payment_gap_musd=max(0.0, end['payment_need_musd'] - h.measures['credit_drawn_musd']),
                 reserve_shortfall_musd=max(0.0, end['funding_target_musd'] - h.measures['credit_drawn_musd']),
                 credit_committed_musd=end['credit_committed_musd'], consent_month=consent,
                 indemnity_month=next((r['month'] for r in h.series if r['legality'] == 'indemnified'), None),
                 disclosure_month=first('assurance_breach_disclosed'),
                 assurance_status=commitments[0]['status'] if commitments else 'not_made', treasury_cash_musd=None)
    missing = dict(treasury_cash_musd='Treasury opening cash, revenue, spending and debt service are not modelled.',
                   consent_month='Consent was not obtained within the assessed horizon.',
                   indemnity_month='No successful indemnity was recorded within the horizon.',
                   disclosure_month='No breach disclosure was recorded within the horizon.')
    events = [e['id'] for e in h.events if e['kind'] != 'state']
    definitions = {d.id: d for d in s.metric_catalog}
    result = []
    for key, definition in definitions.items():
        value = h.measures[key] if key in h.measures else extra[key]
        support = events
        if key == 'disclosure_month':
            support = [e['id'] for e in h.events if e['action'] == 'assurance_breach_disclosed']
        elif key in ('credit_drawn_musd', 'public_drawn_musd', 'payment_gap_musd', 'reserve_shortfall_musd', 'credit_committed_musd'):
            support = [e['id'] for e in h.events if e['action'] in ('payments_met', 'payments_short', 'private_only_credit', 'unauthorized_public_credit')]
        result.append(MetricSample(metric_id=key, value=value,
            missing_reason=missing.get(key, 'Not assessed') if value is None else None,
            period=f'{s.scenario.start}/{s.scenario.end}', scenario_hash=h.scenario_hash,
            engine_version=ENGINE_VERSION, world=h.world, seed=h.seed,
            owner_id=s.execution.roles[definition.owner_role], units=definition.units,
            coverage=definition.coverage, label='LAB', mechanism=definition.mechanism,
            input_refs=definition.input_refs, event_refs=support))
    return result


def comparison(s, original, changed):
    if original.seed != changed.seed or original.scenario_hash != changed.scenario_hash:
        raise ValueError('Comparison requires the same scenario and external world')
    old = {m.metric_id: m for m in samples(s, original)}
    rows = []
    for new in samples(s, changed):
        before = old[new.metric_id].value
        delta = new.value - before if type(new.value) in (int, float) and type(before) in (int, float) else None
        definition = next(d for d in s.metric_catalog if d.id == new.metric_id)
        rows.append(dict(Metric=definition.name, Original=before, Changed=new.value, Delta=delta,
                         Units=new.units, Coverage=new.coverage, Basis=new.label))
    return rows
