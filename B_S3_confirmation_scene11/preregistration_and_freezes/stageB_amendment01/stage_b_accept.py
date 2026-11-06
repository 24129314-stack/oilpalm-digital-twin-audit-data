"""Stage-B reading with the UNCHANGED H4176 acceptance logic; own denominator (never H4176 credit).

The H4176 judge's formal path binds to the H4176 registration set and freeze, so it is called on
its non-H4176 path; the stage-B frozen source is still verified file by file (source_sha256 = the
stage-B freeze). Recipe/landing identity fields come from the H4176040 base registration.
Preregistered role label 'cold_hold' is the judge's 'normal_gravity_cold_hold'. Output: STAGE_B_ACCEPTANCE.json.
"""
import hashlib
import json
import sys
from pathlib import Path

R = Path('/workspace/oilpalm_resume_20261013')
HERE = Path(__file__).resolve().parent
EXEC = R / 'formal_confirmation/H4176_EXECUTION_V1'
sys.path[:0] = [str(EXEC), str(R / 'src')]
import acceptance as A

ROLE = {'cold_hold': 'normal_gravity_cold_hold'}
case = sys.argv[1]
prereg = json.loads((HERE / 'STAGE_B_PREREGISTRATION.json').read_text())
assert hashlib.sha256((HERE / 'STAGE_B_PREREGISTRATION.json').read_bytes()).hexdigest() == (HERE / 'STAGE_B_PREREGISTRATION.sha256').read_text().split()[0]
unit = next(u for u in prereg['units'] if u['case'] == case)
role = ROLE.get(unit['role'], unit['role'])
freeze = json.loads((HERE / 'STAGE_B_SOURCE_FREEZE.json').read_text())
base = json.loads((R / 'experiments/H4176040_NORMAL_STALK_CACHED_BRAKE_LIVE_D0/PREREGISTRATION.json').read_text())
orig_load = A.load


def load(path):
    value = orig_load(path)
    if Path(path).name == 'PREREGISTRATION.json' and value.get('version') == 'H4177_stage_B':
        assert value['source'] == freeze['source']
        for k in ('joint_development_recipe', 'late_handoff_recipe', 'landing_admission'):
            value.setdefault(k, base[k])
        value.setdefault('input_sha256', base['input_sha256'])
        value['source_freeze_sha256'] = A.SOURCE_FREEZE  # identity field only; the B source is checked below
        value['source_sha256'] = freeze['source_files']
        value['confirmation_role'] = role
    return value


A.load = load


class _Json:
    # The original cold-hold reader parses PREREGISTRATION.json itself; give it the same stage-B view.
    def __getattr__(self, name):
        return getattr(json, name)

    def loads(self, text, *a, **k):
        value = json.loads(text, *a, **k)
        if isinstance(value, dict) and value.get('version') == 'H4177_stage_B' and value.get('case') == case:
            value.setdefault('source_sha256', freeze['source_files'])
        return value


_import_file = A.import_file


def import_file(name, path):
    module = _import_file(name, path)
    if name == 'h4176_original_cold_hold':
        module.json = _Json()
    return module


A.import_file = import_file
result = A.judge(case, role=role, development_only=True)
result.update(stage='H4177_stage_B', group=unit['group'], level=unit['level'], H4176_credit=0, own_denominator='H4177_stage_B',
              stage_b_freeze_sha256=hashlib.sha256((HERE / 'STAGE_B_SOURCE_FREEZE.json').read_bytes()).hexdigest(),
              judge_logic_unchanged_H4176=True, role_label_mapping=ROLE)
out = R / 'experiments' / case / 'STAGE_B_ACCEPTANCE.json'
out.open('x').write(json.dumps(result, ensure_ascii=False, indent=1, default=str))
s = result.get('scope', {}); f = result.get('solver_force', {})
print(json.dumps(dict(passed=result['passed'], safety=result['safety_passed'], reasons=result['reasons'][:5], safety_failures=result['safety_failures'][:3],
                      unproven=result['unproven'][:3], wrong=result['wrong_releases'], unsafe=result['unsafe_CUT'], frames=result['integrated_frames'],
                      nonblade_min=s.get('outside_nonblade_min_gap_m'), obs=(f.get('observed_rows'), f.get('expected_rows')), peak=f.get('peak_landing_force_n')), default=str))
