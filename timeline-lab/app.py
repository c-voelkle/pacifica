"""Run locally: streamlit run app.py"""
import json
import time

import streamlit as st

from model import bands, batch, chosen, diverse, months, outcome_counts, simulate
from run import DEFAULT_SCENARIO, grid

st.set_page_config(page_title='Pacifica · Timeline Lab', page_icon='◈', layout='wide')
st.caption('PACIFICA / TIMELINE LAB / LOCAL PROTOTYPE')
st.title('One crisis. Many possible histories.')
st.write('Change a decision, follow the consequences, and find a history worth writing.')


@st.cache_resource
def scenario_file(modified):
    from model import load_scenario
    return load_scenario(DEFAULT_SCENARIO)


def pretty(value):
    return str(value).replace('_', ' ').capitalize()


def control(scenario, key, value, prefix):
    spec = scenario.levers[key]
    label = f'{pretty(key)} · {spec.label}'
    if spec.multi_select:
        return st.multiselect(label, spec.options, default=value, format_func=pretty, key=f'{prefix}_{key}')
    return st.selectbox(label, spec.options, index=spec.options.index(value), format_func=pretty, key=f'{prefix}_{key}')


def history_name(history):
    m = history.measures
    return (f"World {history.world} · {pretty(m['japan_path'])} · Concord {m['concord_status_end']} · "
            f"{m['months_of_illegal_application']} illegal months")


def timeline(scenario, history, prefix):
    st.caption(f'World {history.world} · seed {history.seed} · DRAFT / LAB')
    m = history.measures
    cols = st.columns(4)
    cols[0].metric('Japan', pretty(m['japan_path']))
    cols[1].metric('Concord', pretty(m['concord_status_end']))
    cols[2].metric('Public credit · LAB $m', f"{m['public_drawn_musd']:.1f}")
    cols[3].metric('Illegal application · LAB months', m['months_of_illegal_application'])
    if m['june_payments_met'] and not history.series[-1]['reserve_target_met']:
        st.warning('June payments are met, but the reserve target is missed. A second run can still occur under the LAB rules.')
    if history.series[-1]['effective_public_share'] != history.levers['public_share'] and m['credit_drawn_musd']:
        st.info(f"The refusal fallback changed the effective public share to {history.series[-1]['effective_public_share']:.1%}.")
    records = []
    for event in history.events:
        if event['kind'] == 'state':
            continue
        actor = scenario.actors[event['actor']].name if event['actor'] else 'World'
        records.append(dict(Month=event['month'], Kind=pretty(event['kind']), Actor=actor,
                            Event=pretty(event['action']), Basis=event['label'], Detail=event['reason']))
    st.dataframe(records, hide_index=True, width='stretch', height=430)
    st.download_button('Export this history as JSON', json.dumps(history.export(scenario), indent=2,
                       ensure_ascii=False), file_name=f'pacifica-world-{history.world}.json', mime='application/json',
                       key=f'download_{prefix}')


try:
    s = scenario_file(DEFAULT_SCENARIO.stat().st_mtime_ns)
except (ValueError, OSError, KeyError) as exc:
    st.error(f'The scenario cannot run: {exc}')
    st.stop()

st.caption(s.scenario.question)
st.info('All histories are drafts. MODEL inputs come from the scenario; LAB behavior and ranges are guesses to explore. Counts are not forecasts.')
defaults = chosen(s)
with st.sidebar:
    st.header('Set the choices')
    st.caption('You control Julian’s choices. Every other actor can refuse or change course.')
    with st.form('choices'):
        levers = {key: control(s, key, defaults[key], 'run') for key in s.levers}
        count = st.selectbox('Worlds', [1000, 10000], key='world_count')
        run_clicked = st.form_submit_button('Run histories', type='primary', width='stretch')
    st.caption('The first offer month and loan-refusal fallback use LAB defaults, not settled canon.')

if run_clicked:
    with st.spinner(f'Following {count:,} histories…'):
        start = time.perf_counter()
        try:
            histories = batch(s, count, levers)
            previous = st.session_state.get('result')
            st.session_state['previous'] = previous
            st.session_state['result'] = dict(histories=histories, count=count, levers=levers,
                                            seconds=time.perf_counter() - start, hash=s.digest)
            st.session_state.pop('branch_result', None)
            st.session_state.pop('replayed', None)
        except ValueError as exc:
            st.error(str(exc))

outcomes_tab, histories_tab, grid_tab, assumptions_tab = st.tabs(['Outcomes', 'Explore histories', 'Trade-offs', 'Assumptions'])
result = st.session_state.get('result')
if result and result['hash'] != s.digest:
    for key in ('result', 'previous', 'branch_result', 'replayed', 'grid'):
        st.session_state.pop(key, None)
    result = None
    st.warning('Scenario inputs changed. Run a fresh set of histories before comparing outcomes.')
with outcomes_tab:
    if not result:
        st.subheader('Start with the reference choices')
        st.write('Run histories to see whether the rescue, treaty and settlement survive different actors’ responses.')
    else:
        runs = result['histories']
        st.caption(f"{len(runs):,} worlds · {result['seconds']:.2f} seconds · includes every failure and collapse")
        previous = st.session_state.get('previous')
        current_counts = outcome_counts(runs)
        comparable = previous and previous['hash'] == result['hash'] and previous['count'] == result['count']
        old_counts = outcome_counts(previous['histories']) if comparable else {}
        if previous and not comparable:
            st.warning('The previous run has a different sample size or scenario. Run with the same settings for matched counts.')
        rows = []
        for measure, counts in current_counts.items():
            for value in sorted(set(counts) | set(old_counts.get(measure, {}))):
                row = dict(Measure=pretty(measure), Outcome=pretty(value), Worlds=counts.get(value, 0))
                if comparable:
                    row['Previous'] = old_counts.get(measure, {}).get(value, 0)
                    row['Change'] = row['Worlds'] - row['Previous']
                rows.append(row)
        st.dataframe(rows, hide_index=True, width='stretch')
        st.subheader('How the histories develop')
        st.caption('Median and 10–90% band across every world. All derived values are LAB; financial inputs are MODEL.')
        chart_rows = bands(runs)
        columns = st.columns(2)
        measures = list(dict.fromkeys(row['measure'] for row in chart_rows))
        for i, measure in enumerate(measures):
            with columns[i % 2]:
                st.caption(pretty(measure))
                st.vega_lite_chart([row for row in chart_rows if row['measure'] == measure], {
                    'height': 180, 'encoding': {'x': {'field': 'month', 'type': 'ordinal', 'title': None}},
                    'layer': [
                        {'mark': {'type': 'area', 'opacity': .2, 'color': '#65CDB1'},
                         'encoding': {'y': {'field': 'low', 'type': 'quantitative', 'title': None}, 'y2': {'field': 'high'}}},
                        {'mark': {'type': 'line', 'color': '#65CDB1'},
                         'encoding': {'y': {'field': 'median', 'type': 'quantitative'},
                                      'tooltip': [{'field': k} for k in ('month', 'low', 'median', 'high')]}}]}, width='stretch')

with histories_tab:
    if not result:
        st.write('Run histories to choose a path and branch from one decision.')
    else:
        st.subheader('Five different histories')
        candidates = diverse(result['histories'])
        st.caption('Selected by differences in dated event sequences, including failures. This is variety, not a ranking of writing quality.')
        selected = st.selectbox('Choose a history', candidates, format_func=history_name)
        timeline(s, selected, 'selected')
        with st.expander('Replay any world in this run'):
            world = st.number_input('World number', min_value=0, max_value=result['count'] - 1, step=1)
            if st.button('Replay world'):
                st.session_state['replayed'] = simulate(s, int(world), result['levers'])
            if st.session_state.get('replayed'):
                timeline(s, st.session_state['replayed'], 'replayed')
        st.subheader('Change one decision')
        st.caption('Earlier months and external draws stay identical. Settled credit cannot be rewritten.')
        branch_month = st.selectbox('Branch month', months(s.scenario.start, s.scenario.end))
        branch_key = st.selectbox('Decision to change', list(s.levers), format_func=pretty)
        branch_value = control(s, branch_key, selected.levers[branch_key], 'branch')
        if st.button('Branch this history'):
            try:
                branch = dict(month=branch_month, lever=branch_key, value=branch_value)
                st.session_state['branch_result'] = simulate(s, selected.world, selected.levers, selected.seed, branch)
            except ValueError as exc:
                st.error(str(exc))
        if st.session_state.get('branch_result'):
            st.caption('Branched history')
            timeline(s, st.session_state['branch_result'], 'branch')

with grid_tab:
    st.subheader('Explore a small choice grid')
    st.caption('Every point uses the same world numbers and external draws. Each point includes failures.')
    axes = st.multiselect('Choose up to three levers', [k for k, v in s.levers.items() if not v.multi_select],
                          default=['credit_size_musd', 'public_share'], max_selections=3)
    values = {k: st.multiselect(pretty(k), s.levers[k].options, default=s.levers[k].options[:2], key=f'grid_{k}') for k in axes}
    grid_count = st.selectbox('Worlds per setting', [100, 1000, 10000], index=1)
    if st.button('Run grid', disabled=not axes):
        try:
            with st.spinner('Comparing lever settings…'):
                st.session_state['grid'] = grid(s, values, grid_count, result['levers'] if result else defaults)
        except ValueError as exc:
            st.error(str(exc))
    if st.session_state.get('grid'):
        options = ['rescue_rate', 'consent_rate', 'cabinet_survival_rate', 'mean_public_draw', 'mean_illegal_months']
        x = st.selectbox('Horizontal measure · LAB', options, index=3)
        y = st.selectbox('Vertical measure · LAB', options, index=1)
        rows = [{**{k: r[k] for k in options}, 'choices': json.dumps(r['levers']), 'worlds': r['worlds']} for r in st.session_state['grid']]
        st.vega_lite_chart(rows, {'mark': {'type': 'point', 'filled': True, 'size': 90},
                                'encoding': {'x': {'field': x, 'type': 'quantitative'},
                                             'y': {'field': y, 'type': 'quantitative'},
                                             'tooltip': [{'field': k} for k in (*options, 'choices')]}}, width='stretch')
        st.dataframe(rows, hide_index=True, width='stretch')

with assumptions_tab:
    st.subheader('Know what produced a history')
    st.write(s.execution.observation_note)
    st.caption('Actor utilities, extra execution coefficients, timing defaults and uncertainty ranges are LAB. Existing source labels are retained below.')
    st.json(s.model_dump(by_alias=True), expanded=False)
    st.subheader('Protected facts')
    for fact in s.protected:
        st.write(f'• {fact}')
    st.subheader('Still open')
    for item in s.open_items:
        st.write(f'• {item}')
    st.caption('The question for an evening: did any history suggest a plot idea you would keep?')
