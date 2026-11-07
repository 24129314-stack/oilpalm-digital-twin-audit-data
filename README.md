# Supplementary Data: Auditing Selective Oil Palm Harvesting in a Physics-Gated Digital Twin

This package contains the run-level data behind the manuscript *"Auditing Selective Oil Palm Harvesting in a Physics-Gated Digital Twin: Success Predicates, Full-Arm Clearance, and Generalization Limits"* (submitted to IEEE Access). It has the per-run tables, the figure source data, the preregistrations and freeze records, the safety-stop reports and the cumulative launch ledger.

- **DATA_DICTIONARY.md** explains every column of every CSV file: what it means, its unit, and the values observed in that file.
- **PROVENANCE.csv** maps each file to the original frozen data package it came from, with SHA-256 hashes of the original and of the copy.
- **SHA256SUMS.txt** lists the SHA-256 hash of every file in this package.

Version: v1 (2026-11-06). Contact: [corresponding author, see manuscript].

## Demonstration video

[media/selective_harvest_demo_2026-09-28.mp4](media/selective_harvest_demo_2026-09-28.mp4) (75 s, 2560 × 1600, recorded 2026-09-28) is a screen recording of the digital twin in Isaac Sim. Watch it in the browser at https://24129314-stack.github.io/oilpalm-digital-twin-audit-data/video.html. It shows the rover-mounted arm approaching a palm crown, the third-person view, and the arm-camera view of the fresh fruit bunches and petioles. It is a qualitative illustration from the S1-era development stage, not one of the preregistered S3 runs.

---

## 1. Folder map

| Folder | Study | Success predicate | Paper items |
|---|---|---|---|
| `A_S1_S2_blade_and_object_gates/` | Learned-policy attribution: component ablation, five-seed paired robustness (D vs zero-RL E), fixed library vs online IK, incomplete-episode audit | S1 | Table 2, Table 5, Fig. 5, Table 12 (row S1), Discussion §"Why each success predicate misled" |
| `B_S3_confirmation_scene11/` | Preregistered confirmations of the modular controller on scene 11: Confirmation I (H4176), Stage A development (H4177), Stage B / Confirmation II (H4177) | S3+L | Table 8, Fig. 7, Fig. 8, Fig. 10, Table 13 |
| `C_S3_ablations_baselines_generalization/` | Component ablation AB1–AB7 (exp1), baselines BL1–BL5 (exp2), held-out tiers (exp3a), unseen geometries (exp3b) | S3+L, with strict S3 reported alongside | Table 9, Table 10, Fig. 9, Table 13 |
| `D_S3_fair_planner_BL5e/` | Fair sampling-planner baseline BL5e on T1 (scene 11), T2 (held-out tiers), T3 (unseen geometries) | S3+L | Table 11, Fig. 9, Discussion §"What the fair planner baseline reveals", Table 13 |
| `E_launch_ledger/` | Every simulator process launched for the S3 work (1,649 launches) | — | Recommendation 6, Data availability |

Inside B, C and D:

- `run_tables/` has one row per registered unit, including units that were not started.
- `figure_data/` has the tables the figures were drawn from.
- `preregistration_and_freezes/` has the preregistrations, amendments and freezes, copied verbatim.
- `safety_stop_reports/` (C and D only) has one JSON report for each run that a safety monitor stopped, copied verbatim.

Each folder in A also holds a `statistics.json`: the frozen statistical output of that analysis, copied verbatim. It contains the exact tests reported, such as the McNemar and sign-flip p-values and the Wilson intervals.

## 2. Task, objects and success predicates

The robot must cut two blocking petioles and then the stalk of a ripe fresh fruit bunch (FFB), always in this order. After each cut, the attachment of the severed object is released and the arm must move clear (exit) before the next object.

| Code in data | Paper name | Meaning |
|---|---|---|
| `petiole2`, `petiole_2`, `P2` | P2 | First blocking petiole |
| `petiole0`, `petiole_0`, `P0` | P0 | Second blocking petiole |
| `stalk1`, `stalk_1` | stalk | Stalk of the ripe FFB |
| `stalk_FFB_04`, `petiole_FFB_03` | — | Object names used by the S1-era learned-policy studies |

Milestones are written `<object>_<event>`, with event ∈ {`CUT`, `release`, `exit`}. A full harvest reaches all nine milestones, ending with `stalk1_exit`. `furthest_stage` gives the last milestone reached.

The success predicates get stricter in this order (paper Fig. 2):

- **S1 (blade-only):** cuts are permitted by a blade gate (distance, alignment, contact, blade face, cut zone, order). Contact by other arm parts is not checked.
- **S2 (object-level):** S1, plus the blade must not touch non-target petioles.
- **S3 (full-arm clearance, "strict"):** every non-blade arm part must stay at least 2 mm from the plant over all 144 arm–plant shape pairs, at every control boundary and every solver substep. Cuts must pass the physical blade gates and the identity check. Releases must happen at the cut frame + 1, in order.
- **S3+L ("landing"):** S3 with one bounded exemption. When a severed object lands on the tool, contact is tolerated for at most 25 control periods, with a peak force of at most 300 N at solver substeps and a penetration of at most 8 mm. Table 13 and Section IV-D of the paper describe the provenance of this rule (it was registered after observation) and its sensitivity analysis.

Columns with suffix `_strict` are evaluated under S3. Columns with suffix `_landing` are evaluated under S3+L.

## 3. Time base and units

- **Frame:** one control period of the S3 controller, 1/30 s of simulated time (physics dt 1/120 s × decimation 4). A full harvest takes about 600 frames (20 s). Frame indices equal the `physics_step` counter. Example: `petiole2@28` means P2 was cut at frame 28.
- **Solver substeps:** 16 per frame. A 600-frame run therefore has 9,600 observer rows (`observer_rows`).
- **S1/S2 studies** use the same 1/30 s control step. Their time limit is 3,600 steps (120 s). `penalized_time_s` assigns failed episodes this 120 s limit.
- **Distances and gaps:** in mm when the column name ends in `_mm`, otherwise in m. Gaps are signed, so a negative value means interpenetration.
- **Forces:** in N. Contact forces come from the rigid-body solver and are not calibrated loads (see the paper's Limitations).
- **Angles:** in rad, except `yaw_deg`.
- **Wall time:** `wall_min` (minutes) or `wall_s` / `controller_wall_s` (seconds). These are wall-clock times on the simulation host, not simulated time.

## 4. Denominators and status values

All rates use strict denominators. Every registered unit stays in its table, including units that were `NOT_STARTED`, stopped administratively, or interrupted by infrastructure, and each such unit counts as a failure. The incomplete-episode audit (folder A) shows why this matters: including 30 quota-stopped episodes gives 120/150 = 80% success under S1, while excluding them gives 100%.

| `status` | Meaning |
|---|---|
| `finished`, `PASSED`, `FAILED` | Unit was executed. PASSED/FAILED is the verdict under S3+L. |
| `NOT_STARTED` | Registered but not launched. It stays in the denominator. |
| `stopped_at_screening` | Refused by the static start screen before any physics step |
| `static_check` | Evaluated by static geometry only (AB6) |
| `reference_only` | Row copied from an earlier frozen study for comparison and not re-run |
| `INTERRUPTED_INFRASTRUCTURE` | Interrupted by an instance migration after launch. Counted as a failure. |
| `running` | Still running when a development table was frozen (Stage A only) |

The `label` column in folders C and D is always `exploratory`. These studies were preregistered but do not change the confirmatory verdicts.

## 5. Group and method codes

**Folder A (S1, learned policy; paper Table 2)**

| Group | RL output | Target servo | Alignment assist |
|---|---|---|---|
| A | on | off | off |
| B | on | on | off |
| C | on | off | on |
| D (learned policy) | on | on | on |
| E (zero-RL) | zeroed | on | on |
| E_zero | all policy outputs zeroed (sanity check) | on | on |

In `geometry_adaptive_ik`, `method` = `fixed` (fixed target library) or `adaptive` (online damped-least-squares IK).

**Folder B (S3 confirmations)**

| Code | Meaning |
|---|---|
| `S1_HOLD`, `S1_HANDOFF`, `S1_FULL` | Confirmation I, stage 1 (nominal): cold hold, first-petiole handoff, full harvest. **These S1/S2 prefixes number the stages of Confirmation I and are unrelated to the S1/S2 success predicates.** |
| `S2_UNPERTURBED`, `S2_<tier>` | Confirmation I, stage 2: unperturbed full harvests and perturbation tiers |
| `B1_HOLD`, `B1_HANDOFF`, `B1_FULL`, `B1_NOMINAL_FULL` | Stage B, nominal: hold, handoff, full harvest |
| `B2_CONTACT_DROP3_FORCE08` | Stage B, the one executable held-out tier (contact-sensor degradation) |
| `AUX_COLD_RESTORE` | Auxiliary cold processes that restore the same saved input and compare all 144 gaps and nine rigid-body poses with the live run (39 per stage) |
| `variant` E1…E3G | Stage A development versions. E3G is frozen for Stage B. |

The 13/13 nominal full harvests per stage are `S1_FULL` (3) + `S2_UNPERTURBED` (10) in Confirmation I, and `B1_FULL` (3) + `B1_NOMINAL_FULL` (10) in Stage B.

**Folders C and D (S3+L)**

| Code | Meaning |
|---|---|
| `OURS` | Frozen modular S3 controller |
| `BL1` | Fixed target library, no safety layer, requests a cut on every frame |
| `BL2` | Frozen v5 online DLS IK (S1-era, old-root templates) |
| `BL3` | Locked repair (S1-era, old-root templates) |
| `BL4` | Object-level candidate v8r3 (S2-era, old-root templates) |
| `BL5` | OMPL RRT-Connect with 12 fixed cut poses near the oracle cut point |
| `BL5E_V1`, `BL5E2` | Fair planner baseline BL5e, versions 1 and 2. Only v2 (`BL5E2`) is reported in Table 11. v1 was superseded by Amendment 01 and is kept for disclosure. |
| `E1_CONTROL`, `E1_AB<k>_<name>` | exp1 ablation: control runs, and runs with switch AB*k* disabled (`switch_off`) |
| `E2_<method>`, `E3A_<method>`, `E3B_<method>` | exp2 (scene 11), exp3a (held-out tiers), exp3b (unseen geometries) |
| `T1_…`, `T2_…`, `T3_…` | BL5e test sets: scene 11, held-out tiers, unseen geometries |

The ablation switches (paper Fig. 4) are:

| Switch | Component disabled |
|---|---|
| AB1 | Landing admission |
| AB2 | Stalk cached brake |
| AB3 | E3g entry press |
| AB4 | Zero-force manifold admission |
| AB5 | Temporal interlock |
| AB6 | Screened initialization |
| AB7 | Live/cold barrier |

**Perturbation tiers (`level`, `tier`)**

| Code | Perturbation |
|---|---|
| `NOMINAL` | Registered start on scene 11 |
| `TRANSLATION_{X,Y,Z}_{NEG,POS}` | Robot base offset of ∓/± 0.01 m along the axis |
| `YAW_{NEG,POS}` | Base yaw ∓/± 2° |
| `JOINT_k_{NEG,POS}` | Start offset of joint *k* by ∓/± 0.01 rad |
| `CONTACT_DROP3_FORCE08` | Contact reading dropped every 3rd frame and reported force scaled × 0.8 |
| `h4178_unseen_78301` … `78305` | The five unseen procedurally generated geometries |

Scene 11 has `scenario_seed` 71011.

## 6. What was changed relative to the frozen originals

The original data packages are frozen and hash-verified. This package is a curated copy of them. Exactly these changes were made:

1. **File and folder names were translated into English.** For example, `RUN_TABLE_H4176_阶段1-2.csv` became `run_table_H4176_confirmation_I.csv`, and `05_预登记与冻结` became `preregistration_and_freezes`. PROVENANCE.csv lists every original path.
2. **CSV cell values were translated in three places.** No other cell was changed.
   - `label`: `探索性` → `exploratory`
   - `incomplete_episodes.csv`, column `classification`: `episode时间不足/全局完成配额提前停止` → `insufficient_episode_time_stopped_by_global_completion_quota`
   - `incomplete_episodes.csv`, column `secondary_state`: `机械臂尚未到达` → `arm_not_yet_arrived`
3. **One duplicate column was removed:** `exclusion_reason_zh` in `fig3_holdout_tier_status.csv`. It repeated `exclusion_reason` in Chinese.
4. **All CSVs were rewritten as UTF-8 with LF line endings.** Their SHA-256 hashes therefore differ from the originals even where the content is unchanged. PROVENANCE.csv records both hashes.
5. **JSON, `.sha256` and `.py` files were copied byte for byte.** This keeps their hashes, and the hashes quoted inside the preregistrations, verifiable. Each `.sha256` file next to a preregistration or freeze matches its JSON file in this package.

## 7. Chinese text remaining in verbatim files

A few verbatim files still contain short Chinese strings. Translating them would break their hashes, so here are the translations:

| File | Original string | English |
|---|---|---|
| `C_…/preregistration_and_freezes/H4178_PREREGISTRATION.json`, `REPORT_SCRIPT_AMENDMENT_01.json`, `h4178_report.PREREG_ORIGINAL.py`; `D_…/preregistration_and_freezes/BL5E_COLLISION_MODEL_CHECK.json`, `H4179_PREREGISTRATION*.json` | 探索性 (EXPLORATORY) | exploratory |
| `D_…/preregistration_and_freezes/H4179_PREREGISTRATION.json`, `H4179_PREREGISTRATION_AMENDMENT_01.json` | 一个通用规划器在与本方法相同的约束下，能否完成完整采摘？ | Can a generic planner complete a full harvest under the same constraints as our method? |
| `D_…/preregistration_and_freezes/H4179_PREREGISTRATION_AMENDMENT_01.json` | 修复后重跑 T1 | Rerun T1 after the fix |
| `A_…/incomplete_episode_audit/failure_summary.json` | 时间不足/全局完成配额提前停止 | Insufficient episode time / stopped early by the global completion quota |

The frozen `.py` scripts in `B_…/preregistration_and_freezes/` (stage_b_run.py, stage_b_accept.py, stage_b_queue.py, screen_holdout_static.py, freeze_stage_b_results.py) are included because the source-freeze records hash them. Their comments and log messages are partly in Chinese. They are not needed to read the data.

## 8. Checking the headline numbers

Run `python reproduce_numbers.py` from the repository root to recompute the headline numbers of Tables 5 and 8–11 and Figs. 5, 7, 8 and 10 (requires pandas). The short excerpt below shows the idea. All paths are relative to the package root.

```python
import pandas as pd
A = "A_S1_S2_blade_and_object_gates/"; B = "B_S3_confirmation_scene11/"
D = "D_S3_fair_planner_BL5e/"

# S1: zero-RL E matched learned D (paper: 51/100 vs 54/100)
p = pd.read_csv(A + "paired_robustness_D_vs_E/episodes.csv")
print(p.groupby("group").success.sum())                       # D 51, E 54

# S3+L: 13/13 nominal full harvests in Stage B, landing peak 282.5–283.3 N
f = pd.read_csv(B + "figure_data/fig1_full_harvest_repeatability.csv")
print(f.passed.sum(), len(f), f.peak_substep_force_n.agg(["min", "max"]),
      f.nonblade_min_mm.min())                                 # 13 13, 282.5–283.3, 2.944 mm

# Confirmation I: 13/13 (S1_FULL 3 + S2_UNPERTURBED 10)
h = pd.read_csv(B + "run_tables/run_table_H4176_confirmation_I.csv")
print(h[h.group.isin(["S1_FULL", "S2_UNPERTURBED"])].passed.sum())

# BL5e (v2): 44/50 first gated cut, 12/50 all three, 0 S3+L harvests
u = pd.read_csv(D + "figure_data/ANALYSIS_UNIT_PROGRESS_AND_FAILURE_CAUSES.csv")
x = u[u.group.str.contains("BL5E2")]
print(len(x), x.gated_cuts.fillna("").str.contains("petiole2").sum(),
      (x.all_three_cuts_gated == True).sum(), (x.landing_success == True).sum())
```

## 9. What is not included

- **Raw per-substep trajectory archives** (about 3.6 GB for the H4177 package alone). Each run row carries the SHA-256 of its archive (`raw_archive_sha256`, `archive_sha256`). The archives are available on request and will be deposited with the code.
- **Source code of the simulator, controllers and judges.** The frozen scripts that preregistrations hash are included, as described in §7. The full source trees will be released with the repository/DOI stated in the paper's Data and Code Availability section.
- **Source data for Fig. 6, Table 6 and Table 7** (S1 held-out geometries 03–10 and S2 first-unseen scenes). These are stored in the S1/S2-era archives as JSON and compressed traces, and will be added in v2 of this package.
- **Internal reports written in Chinese** (`*_REPORT_ZH.md` and the summary reports). Every number they contain is derived from the tables included here.

Paths in columns such as `source`, `source_trace`, `evidence` and `source_table` are locations inside the simulation container (`/workspace/…`). They are kept only for traceability.

## 10. Verifying integrity

```bash
sha256sum -c SHA256SUMS.txt          # Linux / macOS (shasum -a 256 -c on macOS)
```

To check a preregistration against its own hash file, for example:

```bash
cd D_S3_fair_planner_BL5e/preregistration_and_freezes && sha256sum -c H4179_PREREGISTRATION.sha256
```

## 11. License and citation

[To be completed by the authors: license, e.g. CC BY 4.0, and the citation of the published article and data DOI.]
