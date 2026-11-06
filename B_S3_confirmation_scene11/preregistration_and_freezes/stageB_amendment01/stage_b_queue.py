"""Run preregistered stage-B units serially, in preregistered order (or the groups given).

Per unit: free disk >= 1500 MiB (else stop the queue; unit stays not started) -> run
(hold/handoff: stage_b_run.py; full: registration + unchanged coordinator) -> stage_b_accept.py
-> lossless raw cleanup. A unit directory that already exists is never rerun.
usage: stage_b_queue.py [GROUP ...]
"""
import copy
import datetime
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

R = Path('/workspace/oilpalm_resume_20261013')
HERE = Path(__file__).resolve().parent
E = R / 'evidence'
S = R / 'src'
PY = '/workspace/oilpalm_diagnostic_venv/bin/python'
OBSERVER = R / 'formal_confirmation/H4176_EXECUTION_V1/substep_observer_entry.py'
WRAPPER = S / 'normal_livepause_with_owner_entry_h3200014.py'
MIN_FREE = 1500 * 1024 ** 2


def sha(p):
    with open(p, 'rb') as f:
        return hashlib.file_digest(f, 'sha256').hexdigest()


def load(p):
    return json.loads(Path(p).read_text())


def say(*a):
    print(datetime.datetime.now(datetime.timezone.utc).strftime('%FT%TZ'), *a, flush=True)


def register_full(unit, freeze, prereg_sha):
    base = load(R / 'experiments/H4176040_NORMAL_STALK_CACHED_BRAKE_LIVE_D0/PREREGISTRATION.json')
    case = unit['case']
    D = R / 'experiments' / case
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    plan = copy.deepcopy(load(base['live_qualification_plan']))
    plan.update(utc=now, case=case, cold_cases=[f"{case}_COLD_{c}" for c in (1, 2, 3)], copied_from=base['live_qualification_plan'])
    pp = E / f'{case}_LIVE_QUALIFICATION_PLAN.json'
    pp.open('x').write(json.dumps(plan, indent=2))
    pins = copy.deepcopy(base['input_sha256'])
    pins[str(pp)] = sha(pp); pins[str(Path(__file__).resolve())] = sha(__file__); pins[str(OBSERVER)] = sha(OBSERVER)
    pins[str(HERE / 'STAGE_B_SOURCE_FREEZE.json')] = sha(HERE / 'STAGE_B_SOURCE_FREEZE.json')
    pins[str(HERE / 'STAGE_B_PREREGISTRATION.json')] = prereg_sha
    raw = str(R / 'raw' / case)
    args = [v.replace(base['raw_output'], raw) for v in base['original_environment_initialization_arguments']]
    args[args.index('--seeds') + 1] = str(unit['seed'])
    reg = copy.deepcopy(base)
    reg.update(case=case, registered_utc=now, source=freeze['source'], source_sha256=freeze['source_files'],
               source_freeze_sha256=sha(HERE / 'STAGE_B_SOURCE_FREEZE.json'), input_sha256=pins, raw_output=raw,
               original_environment_initialization_arguments=args, command=[base['command'][0], '-B', str(OBSERVER), case],
               observer_original_argv=[str(WRAPPER), case], observer_original_entry_sha256=sha(WRAPPER),
               live_qualification_plan=str(pp), native_lease_session=dict(job=case, role='normal'),
               kind='H4177_stage_B_formal_full_harvest', version='H4177_stage_B', level=unit['level'], group=unit['group'],
               process_seed=unit['seed'], formal_confirmation=True, not_confirmation=False, development_only=False,
               previous_version_milestones_borrowed=False, stage_b_preregistration_sha256=prereg_sha,
               stop_policy='One fresh continuous full-task run; unchanged gates, clocks, exemptions; failures kept, no rerun overwrite.')
    reg['environment'] = dict(reg['environment'], TMPDIR=str(R / 'native_cache' / case), **unit['extra_environment'])
    D.mkdir()
    rp = D / 'PREREGISTRATION.json'
    rp.open('x').write(json.dumps(reg, indent=2))
    (D / 'PREREGISTRATION.sha256').open('x').write(sha(rp) + '  PREREGISTRATION.json\n')
    manifest = dict(case=case, manager_sha256=sha(S / 'coordinator_live_Normal_three_cold_h4124017.py'), prereg_sha256=sha(rp))
    (D / 'COORDINATOR_MANIFEST.json').open('x').write(json.dumps(manifest, indent=2))
    return D / 'COORDINATOR_MANIFEST.json'


def main():
    prereg = load(HERE / 'STAGE_B_PREREGISTRATION.json')
    prereg_sha = sha(HERE / 'STAGE_B_PREREGISTRATION.json')
    assert prereg_sha == (HERE / 'STAGE_B_PREREGISTRATION.sha256').read_text().split()[0]
    freeze = load(HERE / 'STAGE_B_SOURCE_FREEZE.json')
    groups = sys.argv[1:] or prereg['run_order']
    assert all(g in prereg['run_order'] for g in groups)
    for group in groups:
        for unit in [u for u in prereg['units'] if u['group'] == group]:
            case = unit['case']
            if (R / 'experiments' / case).exists():
                say('SKIP_EXISTS', case)
                continue
            free = shutil.disk_usage(R).free
            if free < MIN_FREE:
                say('DISK_STOP', case, f'{free >> 20}MiB', 'NOT_STARTED')
                return 2
            say('START', case, f'free={free >> 20}MiB')
            if unit['mode'] in ('hold', 'handoff'):
                assert not unit['extra_environment']
                rc = subprocess.run([PY, '-B', str(HERE / 'stage_b_run.py'), case, '--source', freeze['source'], '--level', unit['level'],
                                     '--mode', unit['mode'], '--seed', str(unit['seed']), '--purpose', f"H4177 stage B {group}"],
                                    stdout=subprocess.DEVNULL).returncode
            else:
                manifest = register_full(unit, freeze, prereg_sha)
                with open(manifest.parent / 'COORDINATOR.original.log', 'x') as log:
                    rc = subprocess.run([PY, '-B', str(S / 'coordinator_live_Normal_three_cold_h4124017.py'), str(manifest)],
                                        stdout=log, stderr=subprocess.STDOUT).returncode
            say('RUN_RC', case, rc)
            acc = subprocess.run([PY, '-B', str(HERE / 'stage_b_accept.py'), case], capture_output=True, text=True, timeout=3600)
            say('ACCEPT', case, (acc.stdout.strip().splitlines() or [''])[-1] or acc.stderr.strip().splitlines()[-1:])
            clean = subprocess.run([PY, str(S / 'cleanup_verified_raw_h4176110.py'), '--apply'], capture_output=True, text=True)
            say('CLEAN', (clean.stdout.strip().splitlines() or [''])[-1])
    say('QUEUE_DONE')
    return 0


if __name__ == '__main__':
    sys.exit(main())
