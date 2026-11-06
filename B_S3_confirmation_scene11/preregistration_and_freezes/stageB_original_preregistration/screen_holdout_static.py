"""H4177 stage B: static (CPU geometry only) screen of the frozen holdout tiers with the frozen B source.

Same construction as H4176 screen_joint_initials.py: initial all-144 pairs >= 2 mm, original joint
limits, frozen h1090 complete path <= 240 frames from the measured bootstrap-6 state. Base tiers move
the Root by the registered world offset / world-Z yaw (static_root_geometry_h1073.proposal). One fixed
candidate per tier, no search or replacement. Qualified tiers get a selection file the B v26 accepts.
"""
from pathlib import Path
import copy
import datetime
import hashlib
import json
import sys
import time

R = Path('/workspace/oilpalm_resume_20261013')
HERE = Path(__file__).resolve().parent
OUT = HERE / 'holdout_static_screen'
FREEZE = HERE / 'STAGE_B_SOURCE_FREEZE.json'
SPLIT = R / 'formal_confirmation/H4177_DEVELOPMENT/PERTURBATION_SPLIT_FREEZE.json'
FRAMES = R / 'formal_confirmation/H4176_EXECUTION_V1/joint_initial_screen_v2'
CASE = 'H4176040_NORMAL_STALK_CACHED_BRAKE_LIVE_D0'


def sha(p):
    with Path(p).open('rb') as f:
        return hashlib.file_digest(f, 'sha256').hexdigest()


def dump(path, value):
    with path.open('x') as f:
        json.dump(value, f, ensure_ascii=False, indent=2, allow_nan=False)
        f.write('\n')


def main():
    import numpy as np
    from scipy.spatial.transform import Rotation
    freeze = json.loads(FREEZE.read_text())
    assert sha(FREEZE) == (HERE / 'STAGE_B_SOURCE_FREEZE.sha256').read_text().split()[0]
    source = Path(freeze['source'])
    for rel, h in freeze['source_files'].items():
        assert sha(source / rel) == h, rel
    split = json.loads(SPLIT.read_text())
    assert sha(SPLIT) == (SPLIT.parent / 'PERTURBATION_SPLIT_FREEZE.sha256').read_text().split()[0]
    reg = json.loads((R / 'experiments' / CASE / 'PREREGISTRATION.json').read_text())
    sys.path[:0] = [str(source), str(R / 'src')]
    from static_root_geometry_h1073 import proposal
    from oilpalm.harvesting_rl.reference_contact_geometry_v36p9 import FullGeometry
    from oilpalm.harvesting_rl.wrist_convex_geometry_v18r2 import hull_from_vertices
    from oilpalm.harvesting_rl.stalk_shaft_clearance import shaft_definition
    from oilpalm.harvesting_rl.joint_frozen_route_proposals_h1090 import plan as original_plan
    from oilpalm.harvesting_rl import screened_initialization_protocol_v26 as v26
    assert Path(v26.__file__).resolve().is_relative_to(source)
    OUT.mkdir(exist_ok=False)
    selection_path = Path(reg['environment']['OILPALM_INIT_SELECTION_FILE'])
    original = v26.load_selection(selection_path, reg['environment']['OILPALM_INIT_SELECTION_SHA256'])
    rows = {s: json.loads((FRAMES / f'frame{s:04d}.original.json').read_text()) for s in (0, 6)}
    initial = np.asarray(original['selected']['q'], float)
    limits = np.asarray(original['original_limits'], float)
    assert np.array_equal(initial, rows[0]['geometry_controller']['temporal_motion']['joint_actual_rad'])
    base = rows[0]['geometry_controller']
    shaft = shaft_definition(reg['environment']['OILPALM_TEST_ASSET'])
    final = base['final_command_check']
    final = final.get('unchanged_original_final_screen', final)
    binding = final['original120_screen']['legacy_final_screen']['risk_audit']['binding']
    meshes = []
    for shape in base['object_cut_preaction_audit']['nonblade_native_evidence']['registry']['tools']:
        if '/Wrist/' in shape['path'] and not shape['path'].endswith(('/Blade', '/Shaft')):
            hull = hull_from_vertices(shape['body_local_vertices_m'], shape['path'])
            hull.update(margin_m=shape['surface_margin_m'], shape_id=shape['shape_id'])
            meshes.append(hull)

    def projected(step, q, extra, yaw_deg):
        g = rows[step]['geometry_controller']
        root = np.asarray(g['robot_root_pos_w']) + np.asarray(extra)
        return proposal(g, q, root, Rotation.from_euler('z', yaw_deg, degrees=True), ('petiole', 2))

    def pair_rows(g, q):
        return FullGeometry(g['object_cut_preaction_audit'], g['temporal_motion'], g, shaft, binding, meshes).rows(q)

    def key(p):
        name = p.get('tool_shape', '')
        name = 'Blade' if name.endswith('/Blade') else 'Shaft' if name.endswith('/Shaft') else name
        return name, tuple(p['object_id']), p['partner_shape'].split('/SelectiveTargets/', 1)[1]

    zero = pair_rows(projected(0, initial, (0, 0, 0), 0.), initial)
    expected = {key(p): p['effective_surface_gap_m'] for p in base['object_cut_preaction_audit']['nonblade_native_evidence']['pairs']}
    error = max(abs(p['gap_m'] - expected[key(p)]) for p in zero)
    assert len(zero) == len(expected) == 144 and error <= 1e-6
    hs = split['holdout_set']
    candidates = []
    for x in hs['joint']:
        if x['status'] != 'RESCREEN_WITH_FROZEN_STAGE_B_PLANNER':
            candidates.append(dict(level=x['level'], kind='joint', not_eligible_physical=x['h4176_screen']))
            continue
        j, sign = int(x['level'][6]), (1 if x['level'].endswith('POS') else -1)
        q = initial.copy(); q[j] += .01 * sign
        candidates.append(dict(level=x['level'], kind='joint', q=np.asarray(q, np.float32).astype(float).tolist(), extra=[0., 0., 0.], yaw_deg=0.))
    for x in hs['base_translation']:
        extra = [0., 0., 0.]; extra['XYZ'.index(x['axis'])] = x['delta_m']
        assert v26.H4177_HOLDOUT_BASE[x['level']] == (tuple(extra), 0.)
        candidates.append(dict(level=x['level'], kind='base', q=initial.tolist(), extra=extra, yaw_deg=0.))
    for x in hs['base_yaw']:
        assert v26.H4177_HOLDOUT_BASE[x['level']][1] == x['delta_deg']
        candidates.append(dict(level=x['level'], kind='base', q=initial.tolist(), extra=[0., 0., 0.], yaw_deg=x['delta_deg']))
    for x in hs['contact_degradation'] if isinstance(hs.get('contact_degradation'), list) else [hs['contact_degradation']]:
        candidates.append(dict(level=x['level'], kind='contact', q=initial.tolist(), extra=[0., 0., 0.], yaw_deg=0.))
    prereg = dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(), script_sha256=sha(__file__),
                  stage_b_freeze_sha256=sha(FREEZE), split_freeze_sha256=sha(SPLIT), frames_sha256={s: sha(FRAMES / f'frame{s:04d}.original.json') for s in (0, 6)},
                  candidates=candidates, thresholds=dict(initial_all144_min_gap_m=.002, original_complete_path_budget_frames=240),
                  zero_reconstruction_error_m=error, physics_calls=0, normal_starts=0, no_candidate_search_or_replacement=True,
                  limitations='Static geometry/path qualification only; the h1204 transfer and other frozen modules keep their own Root pins at runtime.')
    dump(OUT / 'SCREEN_PREREGISTRATION.json', prereg)
    results = []
    for number, c in enumerate(candidates):
        started = time.monotonic()
        if 'not_eligible_physical' in c:
            result = dict(**c, qualified=False, exclusion_reasons=c['not_eligible_physical'], carried_from='H4176 static screen (physical, version independent)')
            dump(OUT / f"{c['level']}_RESULT.json", result); results.append(result)
            continue
        q = np.asarray(c['q'], float)
        reasons = []
        if not (np.all(q >= limits[0]) and np.all(q <= limits[1])):
            reasons.append('outside_original_joint_limits')
        g0 = projected(0, q, c['extra'], c['yaw_deg'])
        pairs = pair_rows(g0, q)
        minimum = min(p['gap_m'] for p in pairs)
        if len(pairs) != 144 or len({key(p) for p in pairs}) != 144 or minimum < .002:
            reasons.append('initial_all144_below_2mm')
        best = evidence = None
        if not reasons:
            q6 = np.asarray(rows[6]['geometry_controller']['temporal_motion']['joint_actual_rad']) + (q - initial)
            g6 = projected(6, q6, c['extra'], c['yaw_deg'])
            try:
                best, evidence = original_plan(g6['object_cut_preaction_audit'], g6['temporal_motion'], g6, shaft, binding, meshes, spent_frames=5)
            except ValueError as error:  # frozen planner fails closed (e.g. h1204 Root pin); recorded, never bypassed
                best, evidence = None, dict(frozen_planner_refusal=str(error))
            if best is None or evidence.get('selected_complete_motion_budget_frames', 241) > 240:
                reasons.append('frozen_complete_initial_path_not_qualified')
        result = dict(**c, initial_all144_min_gap_m=minimum, qualified=not reasons, exclusion_reasons=reasons,
                      path_budget_frames=(evidence or {}).get('selected_complete_motion_budget_frames'), physics_calls=0,
                      path_evidence_summary={k: v for k, v in (evidence or {}).items() if isinstance(v, (str, int, float, bool)) or v is None},
                      runtime_root_pins_unchanged=['joint_first_clear_transfer_h1204 check_scope/begin (1e-6 m, 1e-7 quat)'] if c['kind'] == 'base' else [],
                      wall_s=time.monotonic() - started)
        if not reasons and c['kind'] != 'contact':
            proof = OUT / f"{c['level']}_PATH_PROOF.json"
            dump(proof, dict(results=[dict(original_complete_path_qualified=True, initial_joint_rad=q.tolist(),
                                           base_translation_m=original['authorized_base_translation_m'], holdout_extra_offset_m=c['extra'],
                                           holdout_extra_yaw_deg=c['yaw_deg'], initial_all144_min_gap_m=minimum, evidence=evidence, selected=best)],
                             physics_calls=0, static_only=True, not_a_physical_success=True, screening_plan_sha256=sha(OUT / 'SCREEN_PREREGISTRATION.json')))
            sel = copy.deepcopy(original)
            fingers = [p for p in pairs if '/FingerLeft/' in p['tool_shape'] or '/FingerRight/' in p['tool_shape']]
            others = [p for p in pairs if p not in fingers]
            sel.update(examined=1, eligible=1, excluded=0, new_pose_joint_screen_path=str(proof), new_pose_joint_screen_sha256=sha(proof),
                       population_scope='Exactly one preregistered H4177 holdout tier; no replacement/search.')
            if c['kind'] == 'base':
                sel['h4177_holdout_level'] = c['level']
                sel['selected']['root'] = (np.asarray(original['selected']['root']) + np.asarray(c['extra'])).tolist()
                sel['selected']['root_quat'] = v26._yawed_xyzw(original['selected']['root_quat'], c['yaw_deg']).tolist()
            sel['selected'].update(index=41770000 + number, q=q.tolist(), unclipped_q=q.tolist(), pairs=pairs, min_gap_m=minimum,
                                   original_120_min_gap_m=min(p['gap_m'] for p in others), additional_24_min_gap_m=min(p['gap_m'] for p in fingers),
                                   exclusion_reasons=[], within_original_limits=True, tip_world_m=g0['object_cut_preaction_audit']['tip_world_m'])
            path = OUT / f"{c['level']}_SELECTION.json"
            dump(path, sel)
            assert v26.load_selection(path, sha(path))['selected']['q'] == q.tolist()
            result.update(selection_path=str(path), selection_sha256=sha(path), proof_path=str(proof), proof_sha256=sha(proof))
        dump(OUT / f"{c['level']}_RESULT.json", result)
        results.append(result)
        print(json.dumps({k: result.get(k) for k in ['level', 'qualified', 'initial_all144_min_gap_m', 'exclusion_reasons', 'path_budget_frames', 'path_evidence_summary']}, default=str)[:600], flush=True)
    dump(OUT / 'RESULTS.json', dict(results=[{k: v for k, v in r.items() if k != 'initial_pairs'} for r in results],
                                   qualified=[r['level'] for r in results if r['qualified']], physics_calls=0, normal_starts=0,
                                   screening_plan_sha256=sha(OUT / 'SCREEN_PREREGISTRATION.json')))


if __name__ == '__main__':
    main()
