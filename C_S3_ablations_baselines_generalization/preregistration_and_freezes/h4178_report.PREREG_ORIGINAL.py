"""H4178 (EXPLORATORY) per-experiment tables: RUN_TABLE.csv, REPORT.json, figure-data CSVs. Read only.
usage: h4178_report.py EXPERIMENT   (exp1 | exp2 | exp3a | exp3b)  -> reports/<EXPERIMENT>/
"""
import csv
import json
import math
import sys
from pathlib import Path

R = Path('/workspace/oilpalm_resume_20261013')
HERE = Path(__file__).resolve().parent
PREREG = json.loads((HERE / 'H4178_PREREGISTRATION.json').read_text())
STAGE_B = R / 'formal_confirmation/H4177_STAGE_B'


def wilson(k, n, z=1.959963984540054):
    if not n:
        return (None, None)
    p = k / n; d = 1 + z * z / n; c = (p + z * z / (2 * n)) / d; h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (round(max(0., c - h), 3), round(min(1., c + h), 3))


def mcnemar_exact(b, c):
    """Two-sided exact McNemar = exact binomial test on the discordant pairs (b, c)."""
    n = b + c
    if n == 0:
        return 1.0
    k = min(b, c)
    p = sum(math.comb(n, i) for i in range(0, k + 1)) / 2 ** n
    return min(1.0, 2 * p)


def load(p):
    p = Path(p)
    return json.loads(p.read_text()) if p.exists() else None


def unit_row(u):
    case = u['case']; d = R / 'experiments' / case
    row = dict(experiment=u['experiment'], case=case, kind=u['kind'], group=u['group'], method=u.get('method'), switch_off=u.get('switch') or '',
               level=u.get('level', 'NOMINAL'), seed=u.get('seed', ''), rep=u.get('rep', ''), label='探索性')
    if u['kind'] == 'ab6_static':
        a = load(HERE / 'ab6_static' / f"AB6_STATIC_CHECK_{u['repeat']:02d}.json") or {}
        row.update(status='static_check' if a else 'NOT_STARTED', attempted=bool(a), strict_success='', landing_success='',
                   initial_all144_min_gap_mm=round(1000 * a['all144_min_gap_m'], 3) if a else '', pairs_below_2mm=a.get('pairs_below_2mm', ''),
                   would_start=a.get('would_start', ''), note='static geometry only (no physics)')
        return row
    if u['kind'] == 'reference_only':
        row.update(status='reference_only', attempted='', note=u.get('note', ''))
        return row
    led = load(d / 'LAUNCH_LEDGER.json')
    if led is None:
        pre = load(d / 'PRELAUNCH_REFUSAL_RECORD.json') or load(d / 'NOT_STARTED_RECORD.json')
        row.update(status='stopped_at_screening' if (pre or {}).get('interpretation', '').startswith('our frozen pipeline refused') else 'NOT_STARTED',
                   attempted=bool(pre and (pre or {}).get('interpretation', '').startswith('our frozen pipeline refused')),
                   strict_success=False if pre else '', landing_success=False if pre else '', furthest_stage='screening' if pre else '',
                   stop_reason=(pre or {}).get('interpretation', (pre or {}).get('reason', '')))
        return row
    j = load(d / 'H4178_UNIFORM_JUDGE.json') or {}
    h = load(d / 'H4176_JUDGE_ACCEPTANCE.json') or {}
    v = j.get('verdict', {}); s, l = v.get('strict', {}), v.get('landing', {})
    stop = j.get('stop', {})
    row.update(status=led.get('status'), attempted=True, returncode=led.get('returncode'), wall_min=round((j.get('wall_s') or 0) / 60, 1) if j else '',
               frames=j.get('frames'), strict_success=s.get('success'), landing_success=l.get('success'),
               strict_safety=s.get('safety_passed'), landing_safety=l.get('safety_passed'),
               strict_safety_failures=s.get('safety_failure_count'), landing_safety_failures=l.get('safety_failure_count'),
               h4176_judge_passed=h.get('passed', ''), h4176_judge_safety=h.get('safety_passed', ''),
               furthest_stage=j.get('furthest_stage'), milestones=' '.join(j.get('milestones', [])),
               cut_steps=' '.join(f"{c['object_id'][0]}{c['object_id'][1]}@{c['step']}" for c in j.get('cuts', [])),
               release_steps=json.dumps(j.get('release_steps', {})), physical_exit_steps=json.dumps(j.get('physical_exit_steps', {})),
               dangerous_executed_CUT=j.get('dangerous_executed_CUT'), dangerous_requested_CUT=j.get('dangerous_requested_CUT'),
               temporal_decision_unavailable_frames=j.get('temporal_decision_unavailable_frames'),
               nonblade_lt2mm_boundaries_strict=s.get('nonblade_lt2mm_boundaries'), nonblade_lt2mm_boundaries_landing=l.get('nonblade_lt2mm_boundaries'),
               nonblade_min_gap_mm_strict=None if s.get('nonblade_min_gap_m') is None else round(1000 * s['nonblade_min_gap_m'], 3),
               nonblade_min_gap_mm_landing=None if l.get('nonblade_min_gap_m') is None else round(1000 * l['nonblade_min_gap_m'], 3),
               wrong_releases=j.get('wrong_releases'), unsafe_CUT=j.get('unsafe_CUT'),
               solver_peak_landing_force_n=l.get('solver_peak_landing_force_n'), landing_cycles=j.get('landing_cycles'),
               landing_max_penetration_mm=None if j.get('landing_max_penetration_m') is None else round(1000 * j['landing_max_penetration_m'], 3),
               controller_wall_s=j.get('controller_wall_s_total'), stop_reason=stop.get('administrative_stop') or stop.get('handoff_stop') or stop.get('final_command_stop') or '',
               stop_state=stop.get('handoff_state') or '', termination=json.dumps(stop.get('termination') or {}),
               first_strict_failure=json.dumps((s.get('first_safety_failures') or [None])[0], default=str)[:300],
               first_landing_failure=json.dumps((l.get('first_safety_failures') or [None])[0], default=str)[:300])
    return row


def main(exp):
    out = HERE / 'reports' / exp; out.mkdir(parents=True, exist_ok=True)
    units = [u for u in PREREG['units'] if u['experiment'] == exp]
    rows = [unit_row(u) for u in units]
    cols = []
    for r in rows:
        for k in r:
            if k not in cols:
                cols.append(k)
    with (out / 'RUN_TABLE.csv').open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(rows)
    groups = {}
    for r in rows:
        if r['kind'] in ('reference_only',):
            continue
        g = groups.setdefault(r['group'], dict(n=0, attempted=0, strict=0, landing=0, safety_fail_landing=0, safety_fail_strict=0, not_started=0))
        g['n'] += 1
        if r.get('status') == 'NOT_STARTED':
            g['not_started'] += 1; continue
        if r.get('attempted'):
            g['attempted'] += 1
            g['strict'] += int(r.get('strict_success') is True); g['landing'] += int(r.get('landing_success') is True)
            g['safety_fail_landing'] += int(r.get('landing_safety') is False); g['safety_fail_strict'] += int(r.get('strict_safety') is False)
    for g in groups.values():
        g['wilson_strict'] = wilson(g['strict'], g['attempted']); g['wilson_landing'] = wilson(g['landing'], g['attempted'])
    paired = {}
    if exp in ('exp1', 'exp2'):
        ref = {r['rep']: r for r in rows if r['group'] == 'E1_CONTROL'}
        if exp == 'exp2':
            ref = {u['rep']: unit_row(dict(u, experiment='exp1', kind='ours_full')) for u in PREREG['units'] if u['experiment'] == 'exp1' and u['group'] == 'E1_CONTROL'}
        for gname in sorted({r['group'] for r in rows if r['group'] not in ('E1_CONTROL', 'E2_OURS') and r['kind'] != 'ab6_static'}):
            for mode in ('strict', 'landing'):
                b = c = 0
                for r in rows:
                    if r['group'] != gname or not r.get('attempted') or r['rep'] not in ref:
                        continue
                    a = ref[r['rep']].get(mode + '_success') is True; x = r.get(mode + '_success') is True
                    b += int(a and not x); c += int(x and not a)
                paired[f'{gname}|{mode}'] = dict(reference='our method (all components on)', ours_only=b, other_only=c, exact_mcnemar_p=mcnemar_exact(b, c))
    if exp in ('exp3a', 'exp3b'):
        for m in ('BL1', 'BL2', 'BL3', 'BL4', 'BL5'):
            for mode in ('strict', 'landing'):
                b = c = 0
                for r in rows:
                    if r.get('method') != m or not r.get('attempted'):
                        continue
                    ours = next((o for o in rows if o.get('method') == 'OURS' and o['level'] == r['level']), None)
                    a = bool(ours and ours.get(mode + '_success') is True)
                    x = r.get(mode + '_success') is True
                    b += int(a and not x); c += int(x and not a)
                paired[f'{m}|{mode}'] = dict(ours_only=b, other_only=c, exact_mcnemar_p=mcnemar_exact(b, c), unit='tier' if exp == 'exp3a' else 'scene')
    rep = dict(experiment=exp, label='探索性 (EXPLORATORY)', not_formal_confirmation=True, stage_b_verdict_unchanged=True,
               preregistration_sha256=(HERE / 'H4178_PREREGISTRATION.sha256').read_text().split()[0], groups=groups, paired_exact_mcnemar=paired,
               statistics_note='statistical unit = scene or tier; same-scene repeats descriptive only; Wilson 95% descriptive only; never pooled across versions',
               rows=rows)
    (out / 'REPORT.json').write_text(json.dumps(rep, ensure_ascii=False, indent=1, default=str))
    fig = [dict(group=k, **{kk: (json.dumps(vv) if isinstance(vv, tuple) else vv) for kk, vv in v.items()}) for k, v in groups.items()]
    if fig:
        with (out / 'fig_group_outcomes.csv').open('w', encoding='utf-8-sig', newline='') as f:
            w = csv.DictWriter(f, fieldnames=list(fig[0])); w.writeheader(); w.writerows(fig)
    stage_cols = ['case', 'group', 'method', 'switch_off', 'level', 'rep', 'furthest_stage', 'stop_reason', 'stop_state', 'frames',
                  'dangerous_executed_CUT', 'dangerous_requested_CUT', 'nonblade_lt2mm_boundaries_strict', 'nonblade_lt2mm_boundaries_landing',
                  'wrong_releases', 'unsafe_CUT', 'solver_peak_landing_force_n', 'landing_cycles', 'landing_max_penetration_mm', 'wall_min', 'controller_wall_s']
    with (out / 'fig_stage_and_safety.csv').open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=stage_cols, extrasaction='ignore'); w.writeheader(); w.writerows([r for r in rows if r['kind'] != 'reference_only'])
    print(json.dumps(dict(groups=groups, paired=paired), ensure_ascii=False, indent=1, default=str))


if __name__ == '__main__':
    main(sys.argv[1])
