"""Story-first presentation over saved simulation evidence; no narrative generation service."""
import json
import streamlit as st

from metrics import comparison, resolve_input, samples
from ontology import entity_catalog
from stories import bookmark, candidate, replay_bookmark, save_bookmark


def story_card(s, h):
    story = candidate(s, h)
    with st.container(border=True):
        st.subheader(story.title)
        st.caption(f'World {h.world} · {story.claim_basis.replace("_", " ")} · DRAFT / LAB')
        effective = {**h.levers, **({h.branch['lever']: h.branch['value']} if h.branch else {})}
        requested = ', '.join(effective['concessions_1928']).replace('_', ' ') or 'none'
        st.write(f"Policy in this history: {effective['assurance_strategy']} assurance; "
                 f"{effective['commitment_priority'].replace('_', ' ')}; requested concessions: {requested}.")
        left, right = st.columns(2)
        with left:
            st.markdown('**Goal**')
            st.write(story.goal)
            st.markdown('**Obstacle**')
            st.write(story.obstacle)
        with right:
            st.markdown('**Choice**')
            st.write(story.choice)
            st.markdown('**Cost or sacrifice**')
            st.write(story.sacrifice or 'Not assessed: the trace does not establish a specific sacrifice.')
        st.markdown('**Recorded consequence**')
        st.write(story.consequence)
        st.markdown('**Next question to explore**')
        st.write(story.next_dilemma)
        st.caption('The next question is an author prompt, not a simulated future event. Private-assurance behavior is a visible LAB premise.')


def story_evidence(s, h):
    with st.expander('Why did they choose this?'):
        decisions = h.semantics.get('decisions', [])
        if not decisions:
            st.write('No executed decision record is available.')
            return
        selected = st.selectbox('Decision record', range(len(decisions)),
            format_func=lambda i: f"{decisions[i]['at']} · {s.actors[decisions[i]['actor_id']].name} · {decisions[i]['action'].replace('_', ' ')}")
        d = decisions[selected]
        for reason in d['reasons']:
            st.write(reason)
        st.write('Considered within the bounded procedure:', ', '.join(d['considered_alternatives']))
        st.caption('Private inputs below are author-visible. They are not delivered to other actors.')
        st.json(d, expanded=False)
        st.markdown('**Belief updates and persistent commitments**')
        st.json({key: h.semantics.get(key, []) for key in ('beliefs', 'commitments', 'plans')}, expanded=False)


def metric_inspector(s, h):
    with st.expander('Metric definitions, inputs and evidence'):
        measured = samples(s, h)
        st.dataframe([dict(Metric=d.name, Value='Unavailable' if m.value is None else str(m.value),
                           Units=m.units, Coverage=m.coverage, Basis=m.label,
                           Missing=m.missing_reason or '') for d, m in zip(s.metric_catalog, measured)],
                     hide_index=True, width='stretch')
        key = st.selectbox('Trace a metric', [m.id for m in s.metric_catalog], index=3,
                           format_func=lambda key: next(d.name for d in s.metric_catalog if d.id == key))
        definition = next(d for d in s.metric_catalog if d.id == key)
        value = next(m for m in measured if m.metric_id == key)
        st.write(definition.definition)
        st.json(dict(definition=definition.model_dump(), sample=value.model_dump(),
                     inputs={ref: resolve_input(s, ref) for ref in definition.input_refs},
                     realized_uncertainty=h.draws['uncertainty'],
                     original_policy=h.levers, policy_intervention=h.branch,
                     source_bundle=s.scenario.sources.model_dump()), expanded=False)
        wanted = set(value.event_refs)
        st.dataframe([dict(Event=e['id'], Month=e['month'], Action=e['action'], Evidence=e['reason'])
                      for e in h.events if e['id'] in wanted], hide_index=True, width='stretch')
        st.caption('A vote margin, import-cover estimate and Treasury cash balance are unavailable in this bounded model. Trust and influence are LAB indices.')


def tracks(s, h, original=None):
    st.subheader('Follow the consequences')
    month = st.select_slider('Inspect month', options=[row['month'] for row in h.series], value=h.series[-1]['month'])
    row = next(r for r in h.series if r['month'] == month)
    a, b, c = st.columns(3)
    a.metric('Credit drawn · LAB $m', f"{row['credit_drawn_musd']:.1f}")
    b.metric('Concord', row['concord'].replace('_', ' '))
    c.metric('Illegal application · months', row['illegal_months'])
    points = []
    for label, history in [('Selected', h)] + ([('Original', original)] if original else []):
        for step in history.series:
            for field, measure in [('public_drawn_musd', 'Treasury credit drawn · $m'),
                                   ('credit_drawn_musd', 'Total drawing · $m')]:
                points.append(dict(month=step['month'], value=step[field], measure=measure, history=label))
    st.vega_lite_chart(points, {'height': 185, 'mark': {'type': 'line', 'point': False},
        'encoding': {'x': {'field': 'month', 'type': 'ordinal', 'title': 'Month'},
                     'y': {'field': 'value', 'type': 'quantitative', 'title': 'Period US $m · LAB'},
                     'color': {'field': 'measure', 'type': 'nominal'},
                     'strokeDash': {'field': 'history', 'type': 'nominal'},
                     'tooltip': [{'field': k} for k in ('month', 'measure', 'history', 'value')]}}, width='stretch')
    lanes = [('Concord authority', 'concord'), ('Constitutional case', 'court'), ('Public mediation', 'mediator_role')]
    if h.semantics.get('commitments'):
        lanes += [('Assurance · actual', 'assurance_status'), ('Mediator · belief', 'mediator_assessment'),
                  ('Public report', 'public_assurance_report')]
    states = [dict(month=r['month'], track=label, state=str(r[key] or 'none').replace('_', ' '))
              for r in h.series for label, key in lanes]
    st.vega_lite_chart(states, {'height': 35 * len(lanes), 'mark': 'rect',
        'encoding': {'x': {'field': 'month', 'type': 'ordinal', 'title': 'Month'},
                     'y': {'field': 'track', 'type': 'nominal', 'sort': [label for label, _ in lanes], 'title': None},
                     'color': {'field': 'state', 'type': 'nominal', 'legend': {'orient': 'bottom', 'title': 'Recorded LAB state'}},
                     'tooltip': [{'field': k} for k in ('month', 'track', 'state')]}}, width='stretch')
    st.write(f"At {month}: authority {row['concord']}; court {row['court']}; mediation {row['mediator_role'] or 'none'}.")
    with st.expander('Monthly state table'):
        st.dataframe([dict(Month=r['month'], Authority=r['concord'], Court=r['court'],
                           Mediation=r['mediator_role'] or 'No public posture',
                           Illegal_months=r['illegal_months']) for r in h.series],
                     hide_index=True, width='stretch', height=220)
    st.caption('Authority and mediation are categorical model states. The displayed month does not grant actors future information.')


def branch_difference(s, original, changed):
    st.subheader('What changed?')
    before, after = candidate(s, original), candidate(s, changed)
    a, b = st.columns(2)
    a.markdown('**Original**')
    a.write(before.consequence)
    b.markdown('**Changed policy**')
    b.write(after.consequence)
    rows = comparison(s, original, changed)
    changed_rows = [{**r, 'Original': 'Unavailable' if r['Original'] is None else str(r['Original']),
                        'Changed': 'Unavailable' if r['Changed'] is None else str(r['Changed'])}
                    for r in rows if r['Original'] != r['Changed']]
    if changed_rows:
        st.dataframe(changed_rows, hide_index=True, width='stretch')
    else:
        st.info('No named metric changed in this matched world. This comparison does not demonstrate a material consequence.')
    st.caption('Same scenario, seed and external random tape. This branch changes a continuing policy from the selected month; it is conditional consequence evidence.')


def bookmarks(s, h):
    with st.expander('Keep or restore an idea'):
        rationale = st.text_input('Why is this history useful?', key='bookmark_rationale')
        record = bookmark(s, h, rationale)
        if st.button('Bookmark this history'):
            try:
                path = save_bookmark(record)
                st.success(f'Saved {path.name}. Download the bundle to retain it outside this server.')
            except (ValueError, OSError) as exc:
                st.error(str(exc))
        st.download_button('Download bookmark bundle', json.dumps(record.model_dump(), ensure_ascii=False, indent=2),
                           file_name=f'pacifica-bookmark-{record.id}.json', mime='application/json')
        uploaded = st.file_uploader('Restore a downloaded bookmark', type=['json'])
        if uploaded and st.button('Verify and replay bookmark'):
            try:
                restored_s, restored_h, saved = replay_bookmark(json.loads(uploaded.getvalue()))
                st.success(f'Verified replay of World {restored_h.world}: {saved.candidate.title}')
                st.json({'rationale': saved.rationale, 'metrics': restored_h.measures}, expanded=False)
            except (ValueError, KeyError, TypeError, OSError) as exc:
                st.error(f'Bookmark cannot be verified: {exc}')
    with st.expander('Explicit ontology'):
        st.write('People, institutions and the executive office retain separate identities. Promises remain separate from law; observations remain separate from adjudicator truth.')
        st.json(dict(entities=entity_catalog(s), goals=[g.model_dump() for g in s.drama.goals]), expanded=False)
        if st.button('Build ontology evidence for this history'):
            st.json(h.export(s)['ontology'], expanded=False)
