# Data Dictionary

This file explains every column of every CSV file in the supplementary package. Read README.md first for the success predicates (S1, S2, S3, S3+L), the objects (P2, P0, stalk), the time base (frames) and the group codes.

Conventions used below:

- **frame**: one control period of the S3 controller, 1/30 s of simulated time (physics dt 1/120 s × decimation 4). A full harvest takes about 600 frames (20 s). Frame indices are the `physics_step` counter of the episode. Each frame contains 16 solver substeps.
- **control steps (1/30 s)**: the same period, used by the S1/S2 learned-policy studies.
- **bool** columns contain `True`/`False`; an empty cell means not applicable (e.g. a unit that was not started).
- **JSON** columns contain a JSON (or Python-literal) object written into one cell; parse with `json.loads` (or `ast.literal_eval` when keys are Python tuples such as `('petiole', 2)`).
- **Observed values** were computed from the file itself when this dictionary was generated (range for numeric columns, value list for short categorical columns).
- Gaps are signed distances: negative means interpenetration.

## Contents

- **A_S1_S2_blade_and_object_gates**
  - [control_ablation_stage2_same_checkpoint/episodes.csv](#a_s1_s2_blade_and_object_gatescontrol_ablation_stage2_same_checkpointepisodescsv)
  - [control_ablation_stage2_same_checkpoint/group_metrics.csv](#a_s1_s2_blade_and_object_gatescontrol_ablation_stage2_same_checkpointgroup_metricscsv)
  - [control_ablation_stage3_matched_training/episodes.csv](#a_s1_s2_blade_and_object_gatescontrol_ablation_stage3_matched_trainingepisodescsv)
  - [control_ablation_stage3_matched_training/group_metrics.csv](#a_s1_s2_blade_and_object_gatescontrol_ablation_stage3_matched_traininggroup_metricscsv)
  - [geometry_adaptive_ik/episodes.csv](#a_s1_s2_blade_and_object_gatesgeometry_adaptive_ikepisodescsv)
  - [geometry_adaptive_ik/paired.csv](#a_s1_s2_blade_and_object_gatesgeometry_adaptive_ikpairedcsv)
  - [geometry_adaptive_ik/phase_metrics.csv](#a_s1_s2_blade_and_object_gatesgeometry_adaptive_ikphase_metricscsv)
  - [incomplete_episode_audit/incomplete_episodes.csv](#a_s1_s2_blade_and_object_gatesincomplete_episode_auditincomplete_episodescsv)
  - [paired_robustness_D_vs_E/episodes.csv](#a_s1_s2_blade_and_object_gatespaired_robustness_d_vs_eepisodescsv)
  - [paired_robustness_D_vs_E/five_seed_aggregates.csv](#a_s1_s2_blade_and_object_gatespaired_robustness_d_vs_efive_seed_aggregatescsv)
  - [paired_robustness_D_vs_E/training_seed_metrics.csv](#a_s1_s2_blade_and_object_gatespaired_robustness_d_vs_etraining_seed_metricscsv)
- **B_S3_confirmation_scene11**
  - [figure_data/fig1_full_harvest_repeatability.csv](#b_s3_confirmation_scene11figure_datafig1_full_harvest_repeatabilitycsv)
  - [figure_data/fig2_event_timeline_long.csv](#b_s3_confirmation_scene11figure_datafig2_event_timeline_longcsv)
  - [figure_data/fig3_holdout_tier_status.csv](#b_s3_confirmation_scene11figure_datafig3_holdout_tier_statuscsv)
  - [figure_data/fig4_hold_drift.csv](#b_s3_confirmation_scene11figure_datafig4_hold_driftcsv)
  - [figure_data/fig5_contact_degradation_stops.csv](#b_s3_confirmation_scene11figure_datafig5_contact_degradation_stopscsv)
  - [figure_data/fig6_cross_version_nominal_full_harvest.csv](#b_s3_confirmation_scene11figure_datafig6_cross_version_nominal_full_harvestcsv)
  - [run_tables/run_table_H4176_confirmation_I.csv](#b_s3_confirmation_scene11run_tablesrun_table_h4176_confirmation_icsv)
  - [run_tables/run_table_H4177_stageA_development.csv](#b_s3_confirmation_scene11run_tablesrun_table_h4177_stagea_developmentcsv)
  - [run_tables/run_table_H4177_stageB_confirmation_II.csv](#b_s3_confirmation_scene11run_tablesrun_table_h4177_stageb_confirmation_iicsv)
- **C_S3_ablations_baselines_generalization**
  - [figure_data/exp1_fig_group_outcomes.csv](#c_s3_ablations_baselines_generalizationfigure_dataexp1_fig_group_outcomescsv)
  - [figure_data/exp1_fig_stage_and_safety.csv](#c_s3_ablations_baselines_generalizationfigure_dataexp1_fig_stage_and_safetycsv)
  - [figure_data/exp2_fig_group_outcomes.csv](#c_s3_ablations_baselines_generalizationfigure_dataexp2_fig_group_outcomescsv)
  - [figure_data/exp2_fig_stage_and_safety.csv](#c_s3_ablations_baselines_generalizationfigure_dataexp2_fig_stage_and_safetycsv)
  - [figure_data/exp3a_fig_group_outcomes.csv](#c_s3_ablations_baselines_generalizationfigure_dataexp3a_fig_group_outcomescsv)
  - [figure_data/exp3a_fig_stage_and_safety.csv](#c_s3_ablations_baselines_generalizationfigure_dataexp3a_fig_stage_and_safetycsv)
  - [figure_data/exp3b_fig_group_outcomes.csv](#c_s3_ablations_baselines_generalizationfigure_dataexp3b_fig_group_outcomescsv)
  - [figure_data/exp3b_fig_stage_and_safety.csv](#c_s3_ablations_baselines_generalizationfigure_dataexp3b_fig_stage_and_safetycsv)
  - [run_tables/run_table_exp1.csv](#c_s3_ablations_baselines_generalizationrun_tablesrun_table_exp1csv)
  - [run_tables/run_table_exp2.csv](#c_s3_ablations_baselines_generalizationrun_tablesrun_table_exp2csv)
  - [run_tables/run_table_exp3a.csv](#c_s3_ablations_baselines_generalizationrun_tablesrun_table_exp3acsv)
  - [run_tables/run_table_exp3b.csv](#c_s3_ablations_baselines_generalizationrun_tablesrun_table_exp3bcsv)
- **D_S3_fair_planner_BL5e**
  - [figure_data/ANALYSIS_GROUP_PROGRESS_SUMMARY.csv](#d_s3_fair_planner_bl5efigure_dataanalysis_group_progress_summarycsv)
  - [figure_data/ANALYSIS_UNIT_PROGRESS_AND_FAILURE_CAUSES.csv](#d_s3_fair_planner_bl5efigure_dataanalysis_unit_progress_and_failure_causescsv)
  - [figure_data/T1_fig_bl5e_planning.csv](#d_s3_fair_planner_bl5efigure_datat1_fig_bl5e_planningcsv)
  - [figure_data/T1_fig_candidate_rejections.csv](#d_s3_fair_planner_bl5efigure_datat1_fig_candidate_rejectionscsv)
  - [figure_data/T1_fig_group_outcomes.csv](#d_s3_fair_planner_bl5efigure_datat1_fig_group_outcomescsv)
  - [figure_data/T2_fig_bl5e_planning.csv](#d_s3_fair_planner_bl5efigure_datat2_fig_bl5e_planningcsv)
  - [figure_data/T2_fig_candidate_rejections.csv](#d_s3_fair_planner_bl5efigure_datat2_fig_candidate_rejectionscsv)
  - [figure_data/T2_fig_group_outcomes.csv](#d_s3_fair_planner_bl5efigure_datat2_fig_group_outcomescsv)
  - [figure_data/T3_fig_bl5e_planning.csv](#d_s3_fair_planner_bl5efigure_datat3_fig_bl5e_planningcsv)
  - [figure_data/T3_fig_candidate_rejections.csv](#d_s3_fair_planner_bl5efigure_datat3_fig_candidate_rejectionscsv)
  - [figure_data/T3_fig_group_outcomes.csv](#d_s3_fair_planner_bl5efigure_datat3_fig_group_outcomescsv)
  - [run_tables/run_table_T1.csv](#d_s3_fair_planner_bl5erun_tablesrun_table_t1csv)
  - [run_tables/run_table_T2.csv](#d_s3_fair_planner_bl5erun_tablesrun_table_t2csv)
  - [run_tables/run_table_T3.csv](#d_s3_fair_planner_bl5erun_tablesrun_table_t3csv)
- **E_launch_ledger**
  - [launch_ledger_cumulative.csv](#e_launch_ledgerlaunch_ledger_cumulativecsv)
- **Package root**
  - [PROVENANCE.csv](#provenancecsv)

## A_S1_S2_blade_and_object_gates

### A_S1_S2_blade_and_object_gates/control_ablation_stage2_same_checkpoint/episodes.csv

One row per evaluation episode of the same-checkpoint component intervention (no retraining): groups A–E and E_zero, 10 episodes each (seeds 49/743 × 5). S1 predicate.

Rows: 60. Columns: 12.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `group` | Policy configuration (paper Table 2): A = RL on, target servo off, alignment assist off; B = RL on, servo on, assist off; C = RL on, servo off, assist on; D = RL on, servo on, assist on (learned policy); E = RL output zeroed, servo on, assist on; E_zero = all policy outputs zeroed (sanity check that zeroing works). |  | `D`, `E`, `A`, `B`, `C`, `E_zero` |
| `seed` | Random seed. In S3 studies this is the process seed passed to the simulator; in S1/S2 studies it is the evaluation (scene) seed. |  | `49`, `743` |
| `episode` | Episode index within group × seed. |  | `0`, `1`, `2`, `3`, `4` |
| `outcome` | Episode outcome: success, timeout (time limit reached), policy_failure (terminated by a wrong target or other policy error). |  | `success`, `timeout`, `policy_failure` |
| `length` | Episode length. | control steps (1/30 s) | 1 to 3600 |
| `min_distance` | Minimum blade-tip distance to the required cut point over the episode. | m | 0.02879 to 0.5773 |
| `min_alignment` | Minimum blade-to-petiole alignment error over the episode. | rad | 2.056e-05 to 0.08952 |
| `cutter_commands` | Number of control steps with the cutter commanded. | count | 0 to 91 |
| `fruit_release` | The fruit stalk was released. | bool | `True`, `False` |
| `first_arrival_s` | Time of first arrival within the distance gate. | s | 1.433 to 2.5; 10 empty |
| `first_leaf_cut_s` | Time of the first petiole cut. | s | 1.967 to 4.167; 20 empty |
| `fruit_release_s` | Time of the stalk release. | s | 4.267 to 6.167; 30 empty |

### A_S1_S2_blade_and_object_gates/control_ablation_stage2_same_checkpoint/group_metrics.csv

Per-group aggregates of the episodes above.

Rows: 6. Columns: 35.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `group` | Policy configuration (paper Table 2): A = RL on, target servo off, alignment assist off; B = RL on, servo on, assist off; C = RL on, servo off, assist on; D = RL on, servo on, assist on (learned policy); E = RL output zeroed, servo on, assist on; E_zero = all policy outputs zeroed (sanity check that zeroing works). |  | `D`, `E`, `A`, `B`, `C`, `E_zero` |
| `started` | Number of started episodes; an episode is started when at least one control action was executed (an automatic reset alone does not count). | count | `10` |
| `completed` | Number of episodes that reached a terminal state. | count | `10` |
| `normally_completed` | Number of episodes that terminated normally (not by infrastructure or simulation fault). | count | `10` |
| `policy_failures` | Number of episodes terminated by a policy failure. | count | `0`, `10` |
| `successes` | Number of successful episodes. | count | `10`, `0` |
| `incomplete` | Number of episodes stopped before a terminal state (e.g. by a global completion quota). | count | `0` |
| `timeouts` | Number of episodes that hit the time limit. | count | `0`, `10` |
| `wrong_targets` | Number of episodes terminated by cutting a wrong target. | count | `0`, `10` |
| `simulation_anomalies` | Number of episodes with a numerical simulation anomaly. | count | `0` |
| `infrastructure_failures` | Number of episodes lost to infrastructure faults. | count | `0` |
| `excluded` | Number of episodes excluded from the strict denominator (always 0). | count | `0` |
| `strict_success_rate` | successes / started (strict denominator: every started episode). | fraction | `1.0`, `0.0` |
| `conditional_success_rate` | successes / normally terminated episodes (excludes incomplete episodes; shown only to expose the difference). | fraction | `1.0`, `0.0` |
| `incomplete_rate` | incomplete / started. | fraction | `0.0` |
| `timeout_rate` | timeouts / started. | fraction | `0.0`, `1.0` |
| `wrong_target_rate` | wrong_targets / started. | fraction | `0.0`, `1.0` |
| `infrastructure_failure_rate` | infrastructure_failures / started. | fraction | `0.0` |
| `simulation_anomaly_rate` | simulation_anomalies / started. | fraction | `0.0` |
| `strict_success_wilson95` | Wilson 95% interval of strict_success_rate, [lower, upper]. | fraction | `[0.7224672001371107, 0.9999999999999999]`, `[0.0, 0.2775327998628892]` |
| `conditional_denominator` | Text definition of the conditional denominator. |  | 1 distinct, e.g. `terminal episodes excluding infrastru…` |
| `started_definition` | Text definition of a started episode. |  | 1 distinct, e.g. `at least one control action executed;…` |
| `episode_length_mean` | Mean episode length. | control steps (1/30 s) | `3600`, `137.6`, `139.8`, `151.5`, `1` |
| `min_tip_distance_m_mean` | Mean over episodes of the minimum blade-tip distance. | m | `0.030445603281259538`, `0.03058614917099476`, `0.17818497493863106`, `0.030864715576171875`, `0.18049110621213912`, `0.5417327523231507` |
| `mean_harvest_time_s` | Mean time to harvest over successful episodes. | s | `4.586666666666667`, `4.66`, `5.05`; 3 empty |
| `release_failure_rate` | Fraction of episodes in which the stalk was never released. | fraction | `0.0`, `1.0` |
| `cutter_gate_rejection_rate` | Fraction of executed cutter commands rejected by the blade gate. | fraction | `0.9109792284866469`, `0.9159663865546218`, `0.9676258992805755`, `0.9368421052631579`, `0.9671532846715328`; 1 empty |
| `cutter_command_steps` | Number of control steps with the cutter executed. | count | `337`, `357`, `278`, `475`, `274`, `0` |
| `cutter_gate_rejected_steps` | Number of those steps rejected by the blade gate. | count | `307`, `327`, `269`, `445`, `265`, `0` |
| `requested_cutter_command_steps` | Number of control steps on which the policy requested the cutter. | count | `36000`, `1376`, `1398`, `1515`, `0` |
| `request_level_gate_rejection_rate` | Fraction of requested cutter steps rejected. | fraction | `0.99975`, `0.9781976744186046`, `0.9785407725321889`, `0.9801980198019802`; 1 empty |
| `safety_suppressed_cutter_steps` | Number of requested cutter steps suppressed by the safety layer before execution. | count | `1039`, `1041`, `35722`, `1040`, `35726`, `0` |
| `rl_residual_norm_mean` | Mean norm of the RL residual action. |  | `0.0`, `1.1509087409737497`, `1.1731416716741192`, `1.176142929096033`, `1.1727587429417503` |
| `action_override_fraction_mean` | Mean fraction of action components overridden. | fraction | `0.6517280569343373`, `0.5240820408485649`, `0.2180771622368031`, `0.6430509930396631`, `0.21810802643415`, `0.5555555820465088` |
| `action_clip_fraction_mean` | Mean fraction of actions clipped at execution. | fraction | `0.0`, `0.12338501383918662`, `0.10782407491571373`, `0.1223322341347685`, `0.10784259343437022` |

### A_S1_S2_blade_and_object_gates/control_ablation_stage3_matched_training/episodes.csv

One row per final evaluation episode of the matched-initialization training ablation (paper Table 5): groups A–E, training seed 49, 20 episodes each. S1 predicate.

Rows: 100. Columns: 12.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `group` | Policy configuration (paper Table 2): A = RL on, target servo off, alignment assist off; B = RL on, servo on, assist off; C = RL on, servo off, assist on; D = RL on, servo on, assist on (learned policy); E = RL output zeroed, servo on, assist on; E_zero = all policy outputs zeroed (sanity check that zeroing works). |  | `A`, `B`, `C`, `D`, `E` |
| `seed` | Random seed. In S3 studies this is the process seed passed to the simulator; in S1/S2 studies it is the evaluation (scene) seed. |  | `49`, `743` |
| `episode` | Episode index within group × seed. |  | 0 to 9 |
| `outcome` | Episode outcome: success, timeout (time limit reached), policy_failure (terminated by a wrong target or other policy error). |  | `success`, `timeout` |
| `length` | Episode length. | control steps (1/30 s) | 136 to 3600 |
| `min_distance` | Minimum blade-tip distance to the required cut point over the episode. | m | 0.01969 to 0.3575 |
| `min_alignment` | Minimum blade-to-petiole alignment error over the episode. | rad | 7.749e-07 to 0.002124 |
| `cutter_commands` | Number of control steps with the cutter commanded. | count | 0 to 195 |
| `fruit_release` | The fruit stalk was released. | bool | `True`, `False` |
| `first_arrival_s` | Time of first arrival within the distance gate. | s | 1.433 to 1.933; 40 empty |
| `first_leaf_cut_s` | Time of the first petiole cut. | s | 2.267 to 3.2; 40 empty |
| `fruit_release_s` | Time of the stalk release. | s | 4.3 to 9.467; 40 empty |

### A_S1_S2_blade_and_object_gates/control_ablation_stage3_matched_training/group_metrics.csv

Per-group aggregates for paper Table 5.

Rows: 5. Columns: 35.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `group` | Policy configuration (paper Table 2): A = RL on, target servo off, alignment assist off; B = RL on, servo on, assist off; C = RL on, servo off, assist on; D = RL on, servo on, assist on (learned policy); E = RL output zeroed, servo on, assist on; E_zero = all policy outputs zeroed (sanity check that zeroing works). |  | `A`, `B`, `C`, `D`, `E` |
| `started` | Number of started episodes; an episode is started when at least one control action was executed (an automatic reset alone does not count). | count | `20` |
| `completed` | Number of episodes that reached a terminal state. | count | `20` |
| `normally_completed` | Number of episodes that terminated normally (not by infrastructure or simulation fault). | count | `20` |
| `policy_failures` | Number of episodes terminated by a policy failure. | count | `0` |
| `successes` | Number of successful episodes. | count | `20`, `0` |
| `incomplete` | Number of episodes stopped before a terminal state (e.g. by a global completion quota). | count | `0` |
| `timeouts` | Number of episodes that hit the time limit. | count | `0`, `20` |
| `wrong_targets` | Number of episodes terminated by cutting a wrong target. | count | `0` |
| `simulation_anomalies` | Number of episodes with a numerical simulation anomaly. | count | `0` |
| `infrastructure_failures` | Number of episodes lost to infrastructure faults. | count | `0` |
| `excluded` | Number of episodes excluded from the strict denominator (always 0). | count | `0` |
| `strict_success_rate` | successes / started (strict denominator: every started episode). | fraction | `1.0`, `0.0` |
| `conditional_success_rate` | successes / normally terminated episodes (excludes incomplete episodes; shown only to expose the difference). | fraction | `1.0`, `0.0` |
| `incomplete_rate` | incomplete / started. | fraction | `0.0` |
| `timeout_rate` | timeouts / started. | fraction | `0.0`, `1.0` |
| `wrong_target_rate` | wrong_targets / started. | fraction | `0.0` |
| `infrastructure_failure_rate` | infrastructure_failures / started. | fraction | `0.0` |
| `simulation_anomaly_rate` | simulation_anomalies / started. | fraction | `0.0` |
| `strict_success_wilson95` | Wilson 95% interval of strict_success_rate, [lower, upper]. | fraction | `[0.8388748419471806, 1.0]`, `[0.0, 0.16112515805281938]` |
| `conditional_denominator` | Text definition of the conditional denominator. |  | 1 distinct, e.g. `terminal episodes excluding infrastru…` |
| `started_definition` | Text definition of a started episode. |  | 1 distinct, e.g. `at least one control action executed;…` |
| `episode_length_mean` | Mean episode length. | control steps (1/30 s) | `3600`, `145.35`, `160.8`, `140.65` |
| `min_tip_distance_m_mean` | Mean over episodes of the minimum blade-tip distance. | m | `0.34294274300336836`, `0.030587583780288696`, `0.3111651584506035`, `0.028457869961857795`, `0.030439040251076223` |
| `mean_harvest_time_s` | Mean time to harvest over successful episodes. | s | `4.845`, `5.359999999999999`, `4.6883333333333335`; 2 empty |
| `release_failure_rate` | Fraction of episodes in which the stalk was never released. | fraction | `0.0`, `1.0` |
| `cutter_gate_rejection_rate` | Fraction of executed cutter commands rejected by the blade gate. | fraction | `0.9256505576208178`, `0.9469964664310954`, `0.9158485273492286`; 2 empty |
| `cutter_command_steps` | Number of control steps with the cutter executed. | count | `0`, `807`, `1132`, `713` |
| `cutter_gate_rejected_steps` | Number of those steps rejected by the blade gate. | count | `0`, `747`, `1072`, `653` |
| `requested_cutter_command_steps` | Number of control steps on which the policy requested the cutter. | count | `72000`, `2907`, `3216`, `2813` |
| `request_level_gate_rejection_rate` | Fraction of requested cutter steps rejected. | fraction | `1.0`, `0.9793601651186791`, `0.9813432835820896`, `0.9786704585851405` |
| `safety_suppressed_cutter_steps` | Number of requested cutter steps suppressed by the safety layer before execution. | count | `72000`, `2100`, `2084` |
| `rl_residual_norm_mean` | Mean norm of the RL residual action. |  | `1.0229940921217202`, `1.1226933094534137`, `1.0069694299631649`, `1.1337485938374676`, `0.0` |
| `action_override_fraction_mean` | Mean fraction of action components overridden. | fraction | `0.2225694461259991`, `0.6096013686810321`, `0.11152314897906035`, `0.6132531989347282`, `0.5233242674215892` |
| `action_clip_fraction_mean` | Mean fraction of actions clipped at execution. | fraction | `0.11145833416376263`, `0.08489087706103045`, `0.0004120370401069522`, `0.09680762924531948`, `0.0` |

### A_S1_S2_blade_and_object_gates/geometry_adaptive_ik/episodes.csv

Fixed target library vs online IK ('adaptive') under robot root-pose changes (S1). Supports the statement that online IK recovered root-pose changes that broke a fixed library.

Rows: 80. Columns: 35.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `action_saturations` | Number of action components saturated at their limits. | count | 144 to 14398; 40 empty |
| `anomalies` | Number of numerical anomalies in the episode. | count | `0` |
| `approach_time_s` | Time until the blade first satisfied the distance gate. | s | 2 to 4.5; 27 empty |
| `batch` | Evaluation batch of the geometry-adaptive study (matrix, matrix_v4, matrix_v5 = successive frozen matrices; extension, cold_repeat, legacy_roll, bias_stress = supplementary batches). |  | 7 distinct, e.g. `matrix` |
| `condition` | Perturbation condition of the S1 robustness study: baseline (nominal), unseen_pose_light/heavy (robot root pose not seen in training), perception_light/heavy (observation noise), delay_light/heavy (action delay), joint_bias_light/heavy (joint encoder bias), combined; translation_only / yaw_only = root-pose components in isolation. |  | `unseen_pose_light`, `unseen_pose_heavy`, `baseline`, `translation_only`, `yaw_only`, `joint_bias_heavy` |
| `elapsed_s` | Simulated episode time. | s | 4.467 to 120 |
| `errors` | Number of runtime errors in the episode. | count | `0` |
| `final_phase` | Task-phase index at episode end (phases advance through the ordered cut sequence; 5 = harvest complete). |  | `4`, `1`, `2`, `3` |
| `geometry_signature` | Root-pose perturbation [dx, dy, dz, dyaw] relative to the nominal root (m, m, m, rad). | m / rad | 12 distinct, e.g. `[0.0, 0.0, 0.0, 0.0]` |
| `harvest_time_s` | Time to harvest (successful episodes only). | s | 4.467 to 8.5; 33 empty |
| `ik_calls` | Number of IK solver calls. | count | 0 to 3600 |
| `ik_failures` | Number of IK solver failures. | count | `0`; 40 empty |
| `incomplete` | 1 if the episode was incomplete. | count | `0` |
| `initial_joint` | Initial joint state and root pose (JSON). | JSON | 14 distinct, e.g. `{'phase': [0], 'robot_root_pos_w': [[…` |
| `initial_observation_sha256` | SHA-256 of the initial observation vector (identical within a pair). | hex | 16 distinct, e.g. `35afd9e3718b0f6de8516b3feed6d80047df3…` |
| `initial_quat` | Initial robot root orientation quaternion [x, y, z, w]. |  | 7 distinct, e.g. `[0.0, 0.0, 0.0, 1.0]` |
| `initial_root` | Initial robot root position [x, y, z] in the world frame. | m | 9 distinct, e.g. `[0.09528571367263794, -0.507142841815…` |
| `joint_limit_saturations` | Number of joint-limit saturations. | count | `0`, `152035`; 40 empty |
| `method` | Controller under test. OURS = frozen modular S3 controller; BL1–BL5 = baselines (paper Table 3); BL5E_V1 / BL5E2 = fair sampling-planner baseline BL5e, version 1 (voided after Amendment 01) and version 2 (reported). In A_*/geometry_adaptive_ik: fixed = fixed target library, adaptive = online damped-least-squares IK. |  | `fixed`, `adaptive` |
| `min_tip_distance_m` | Minimum blade-tip distance to the cut point. | m | 0.01441 to 0.7324 |
| `name` | Run name: <condition>_<scene seed>_cold<k>_<method>. |  | 30 distinct, e.g. `baseline_1743_cold0_fixed` |
| `penalized_time_s` | Time to success, with failed episodes assigned the 120 s time limit. | s | 4.467 to 120 |
| `pose_protocol` | Quaternion convention used to compose the root pose (corrected_xyzw, or legacy_wxyz which caused the earlier roll/yaw error). |  | `corrected_xyzw`, `legacy_wxyz` |
| `reachable_call_fraction` | Fraction of IK calls whose target was reachable. | fraction | `1.0`; 40 empty |
| `release_order_valid` | Releases occurred in the required order. | bool | `True` |
| `repeat` | Repeat index of the paired episode (0 = first). |  | `0` |
| `seed` | Scene seed (1743 or 2743). |  | `2743`, `1743`, `3817`, `4919` |
| `solve_time_s_mean` | Mean IK solve time. | s | 0.0008414 to 0.03294; 40 empty |
| `started` | 1 if the episode was started. | count | `1` |
| `successes` | 1 if the episode succeeded (S1). | count | `1`, `0` |
| `timeouts` | 1 if the episode timed out. | count | `0`, `1` |
| `trace` | Path of the per-step trace (relative to the source tree). |  | 80 distinct, e.g. `output/analysis/geometry_adaptive_202…` |
| `visited_target_reachable_fraction` | Fraction of visited targets that were reachable. | fraction | `1.0`; 40 empty |
| `wrong_cuts` | Number of cuts of a wrong object. | count | `0` |
| `wrong_targets` | 1 if the episode ended on a wrong target. | count | `0` |

### A_S1_S2_blade_and_object_gates/geometry_adaptive_ik/paired.csv

Paired adaptive − fixed differences with identical initial observations.

Rows: 40. Columns: 8.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `batch` | Evaluation batch of the geometry-adaptive study (matrix, matrix_v4, matrix_v5 = successive frozen matrices; extension, cold_repeat, legacy_roll, bias_stress = supplementary batches). |  | 7 distinct, e.g. `matrix` |
| `condition` | Perturbation condition of the S1 robustness study: baseline (nominal), unseen_pose_light/heavy (robot root pose not seen in training), perception_light/heavy (observation noise), delay_light/heavy (action delay), joint_bias_light/heavy (joint encoder bias), combined; translation_only / yaw_only = root-pose components in isolation. |  | `unseen_pose_light`, `unseen_pose_heavy`, `baseline`, `translation_only`, `yaw_only`, `joint_bias_heavy` |
| `initial_observation_identical` | The paired episodes started from byte-identical observations. | bool | `True` |
| `initial_root_identical` | The paired episodes started from the identical robot root pose. | bool | `True` |
| `penalized_time_difference_s` | Penalized time of the adaptive-IK episode minus that of the paired fixed-library episode. | s | -115.5 to 115.4 |
| `repeat` | Repeat index of the paired episode (0 = first). |  | `0` |
| `seed` | Scene seed (1743 or 2743). |  | `2743`, `1743`, `3817`, `4919` |
| `success_difference` | Success of the adaptive-IK episode minus success of the paired fixed-library episode (−1, 0, 1). |  | `1`, `0`, `-1` |

### A_S1_S2_blade_and_object_gates/geometry_adaptive_ik/phase_metrics.csv

Per-episode, per-phase approach and gate-rejection metrics for the geometry-adaptive study.

Rows: 181. Columns: 14.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `alignment_at_min_rad` | Alignment error at the step of minimum distance. | rad | 0.009785 to 0.3664 |
| `alignment_at_valid_cut_rad` | Alignment error at the first step on which a cut would have been valid. | rad | 0.009785 to 0.3664; 33 empty |
| `batch` | Evaluation batch of the geometry-adaptive study (matrix, matrix_v4, matrix_v5 = successive frozen matrices; extension, cold_repeat, legacy_roll, bias_stress = supplementary batches). |  | 7 distinct, e.g. `matrix` |
| `final_rejections` | Gate components still rejecting at the end of the phase. |  | 6 distinct, e.g. `[]` |
| `first_step` | First control step of the phase. | control steps | 0 to 198 |
| `last_step` | Last control step of the phase. | control steps | 59 to 3599 |
| `min_alignment_rad` | Minimum blade alignment error. | rad | 0.0002189 to 0.223 |
| `min_tip_distance_m` | Minimum blade-tip distance to the cut point. | m | 0.02042 to 0.7324 |
| `name` | Run name: <condition>_<scene seed>_cold<k>_<method>. |  | 30 distinct, e.g. `baseline_1743_cold0_fixed` |
| `nearest_step` | Control step of minimum distance in the phase. | control steps | 0 to 3189 |
| `phase` | Task-phase index the row describes (1 = first required cut, 2 = second, 3 = third). |  | `1`, `2`, `3` |
| `reachable_solved` | The phase target was solved as reachable. | bool | `True`; 69 empty |
| `rejection_counts` | JSON {gate component: number of steps rejected} within the phase (distance, alignment, contact, blade_face, cut_zone, order). | JSON / count | 92 distinct, e.g. `{'distance': 56, 'alignment': 0, 'con…` |
| `time_to_valid_cut_s` | Time from phase start to the first valid-cut step. | s | 0.5 to 4.467; 33 empty |

### A_S1_S2_blade_and_object_gates/incomplete_episode_audit/incomplete_episodes.csv

The 30 training-evaluation episodes (of 150) that were stopped by a global completion quota before reaching a terminal state. Including them gives 120/150 = 80% strict success; excluding them gives 100% (paper Table 12, Discussion). Two Chinese values were translated (see README §7).

Rows: 30. Columns: 23.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `run` | Training run (named by training seed) in which the episode occurred. |  | `training_seed_149`, `training_seed_249`, `training_seed_349`, `training_seed_449`, `training_seed_49` |
| `seed` | Training environment seed. |  | `49`, `743` |
| `env_id` | Index of the parallel simulation environment during training. |  | `1`, `3`, `2`, `0` |
| `episode_id` | Episode index within the run. |  | `3` |
| `checkpoint` | Policy checkpoint file evaluated. |  | `model_iter_000300.pt` |
| `final_state` | Controller phase at the final step (1 = still approaching the first petiole). |  | `1` |
| `min_tip_distance_m` | Minimum blade-tip distance to the cut point. | m | 0.2714 to 0.5395 |
| `min_alignment_rad` | Minimum blade alignment error. | rad | 2.447e-05 to 0.07655 |
| `final_alignment_rad` | Blade alignment error at the final step. | rad | 0.001214 to 0.07941 |
| `cutter_command_count` | Number of control steps with the cutter commanded. | count | `0` |
| `cutter_gate_rejections` | JSON count of gate rejections by component. | JSON | `{}` |
| `episode_length` | Episode length. | control steps (1/30 s) | 1 to 51 |
| `final_gate_reasons` | Same as final_gate_rejections_json. | JSON | 1 distinct, e.g. `["cutter", "contact", "blade_face", "…` |
| `final_cutter_masked` | The cutter command was masked by the safety layer at the final step. | bool | `True` |
| `leaf_release` | A petiole was released. | bool | `False` |
| `fruit_release` | The fruit stalk was released. | bool | `False` |
| `timeout` | Episode hit the time limit. | bool | `False` |
| `classification` | Reason the training episode was incomplete. Translated from the original Chinese value (insufficient episode time; stopped early by the global completion quota). |  | 1 distinct, e.g. `insufficient_episode_time_stopped_by_…` |
| `secondary_state` | State of the arm when the episode was stopped (arm_not_yet_arrived; translated from Chinese). |  | `arm_not_yet_arrived` |
| `evidence` | Path of the training log that contains the episode. |  | 30 distinct, e.g. `output/training/selective_goal_traini…` |
| `final_distance_m` | Blade-tip distance to the required cut point at episode end. | m | 0.2714 to 0.5395 |
| `final_step` | Last control step recorded. | control steps | 434 to 464 |
| `finite_joint_state` | All joint values finite at the final step. | bool | `True` |

### A_S1_S2_blade_and_object_gates/paired_robustness_D_vs_E/episodes.csv

One row per episode of the five-seed paired robustness study (paper Fig. 5): learned policy D vs zero-RL E, 5 training seeds × 2 scene seeds × 10 conditions = 100 paired episodes per group. D succeeded in 51/100 and E (zero-RL) in 54/100.

Rows: 200. Columns: 39.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `group` | D = learned policy; E = same checkpoint with RL output zeroed (zero-RL). |  | `D`, `E` |
| `condition` | Perturbation condition of the S1 robustness study: baseline (nominal), unseen_pose_light/heavy (robot root pose not seen in training), perception_light/heavy (observation noise), delay_light/heavy (action delay), joint_bias_light/heavy (joint encoder bias), combined; translation_only / yaw_only = root-pose components in isolation. |  | 10 distinct, e.g. `baseline` |
| `training_seed` | Seed of the PPO training run whose checkpoint was evaluated (five seeds: 49, 149, 249, 349, 449). |  | `49`, `149`, `249`, `349`, `449` |
| `evaluation_seed` | Seed used for evaluation episodes (S1). |  | `1743`, `2743` |
| `scenario_seed` | Seed of the procedural plantation scene. 71011 = scene 11 (the only S3 scene); 1743 / 2743 = the two S1 nominal scene seeds. |  | `1743`, `2743` |
| `episode_id` | Episode index within the run. |  | `0` |
| `checkpoint_sha256` | SHA-256 of the policy checkpoint. | hex | 5 distinct, e.g. `8dbac8b2643121ac766dffa6bd12c7fd7caa7…` |
| `outcome` | Episode outcome: success, timeout (time limit reached), policy_failure (terminated by a wrong target or other policy error). |  | `success`, `timeout` |
| `terminal` | Episode reached a terminal state (not truncated by infrastructure). | bool | `True` |
| `success` | Episode success under S1 (ordered blade-gated cuts and stalk release). | bool | `True`, `False` |
| `final_phase` | Task-phase index at episode end (phases advance through the ordered cut sequence; 5 = harvest complete). |  | `5`, `1`, `3` |
| `failure_category` | Classified failure: success; administrative_stop; contact_or_other_gate_rejected; approach_distance_not_reached; delayed_distance_mask_at_ready_gate. In S3 tables: post-hoc classification of non-passing runs. |  | `success`, `approach_distance_not_reached`, `contact_or_other_gate_rejected`, `delayed_distance_mask_at_ready_gate` |
| `final_required_cut` | Object that was required to be cut next at episode end. |  | `stalk_FFB_04`, `petiole_FFB_03` |
| `phase_min_distance_json` | JSON {phase: minimum blade-tip distance in m}. | JSON / m | 178 distinct, e.g. `{"1": 0.06545865535736084, "2": 0.085…` |
| `final_distance_m` | Blade-tip distance to the required cut point at episode end. | m | 0.02774 to 3.069 |
| `final_gate_rejections_json` | JSON list of blade-gate components that rejected the cut at the final step. | JSON | 6 distinct, e.g. `["cutter", "contact", "blade_face", "…` |
| `wrong_target` | Episode terminated by a wrong target. | bool | `False` |
| `release` | The required object was released. | bool | `True`, `False` |
| `length` | Episode length. | control steps (1/30 s) | 137 to 3600 |
| `time_s` | Episode duration. | s | 4.567 to 120 |
| `penalized_time_s` | Time to success, with failed episodes assigned the 120 s time limit. | s | 4.567 to 120 |
| `min_distance_m` | Minimum blade-tip distance to the required cut point. | m | 0.004704 to 0.7324 |
| `min_alignment_rad` | Minimum blade alignment error. | rad | 4.768e-07 to 0.002372 |
| `wrong_petiole_attempts` | Number of cut attempts on a non-target petiole. | count | `0` |
| `cutter_commands` | Number of control steps with the cutter commanded. | count | 0 to 3485 |
| `cutter_gate_rejected` | Number of cutter commands rejected by the blade gate. | count | 0 to 3485 |
| `controller_cut_requests` | Number of cut requests issued by the controller. | count | 0 to 3485 |
| `rl_retained_norm_mean` | Mean norm of the RL action component that survived the servo override. |  | 0 to 1.422 |
| `rl_modified_fraction` | Fraction of action components modified by the servo/safety layer. | fraction | 0.3376 to 0.6667 |
| `execution_clip_fraction` | Fraction of actions clipped at execution. | fraction | 0 to 0.1985 |
| `source_trace` | Path of the compressed per-step trace in the simulation container. |  | 200 distinct, e.g. `/workspace/oilpalmplantation_all_code…` |
| `first_line` | First line of the trace used. |  | `1` |
| `last_line` | Last line of the trace used. |  | 137 to 3600 |
| `initial_observation_sha256` | SHA-256 of the initial observation vector (identical within a pair). | hex | 12 distinct, e.g. `35afd9e3718b0f6de8516b3feed6d80047df3…` |
| `physical_pose_verified` | The episode's physical start pose was verified against the registered pose. | bool | `True` |
| `gate_ready_steps` | Number of steps on which all blade gates were satisfied. | count | 0 to 837 |
| `eligible_but_cutter_missing_steps` | Gate-ready steps without a cutter command. | count | 0 to 835 |
| `eligible_but_rl_withheld_steps` | Gate-ready steps on which the RL output withheld the cut. | count | `0` |
| `eligible_but_source_safety_masked_steps` | Gate-ready steps masked by the source safety mask. | count | 0 to 835 |

### A_S1_S2_blade_and_object_gates/paired_robustness_D_vs_E/five_seed_aggregates.csv

Aggregates per condition × group × training seed (over 2 scene seeds).

Rows: 100. Columns: 21.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `condition` | Perturbation condition of the S1 robustness study: baseline (nominal), unseen_pose_light/heavy (robot root pose not seen in training), perception_light/heavy (observation noise), delay_light/heavy (action delay), joint_bias_light/heavy (joint encoder bias), combined; translation_only / yaw_only = root-pose components in isolation. |  | 10 distinct, e.g. `baseline` |
| `group` | D = learned policy; E = same checkpoint with RL output zeroed (zero-RL). |  | `D`, `E` |
| `training_seed` | Seed of the PPO training run whose checkpoint was evaluated (five seeds: 49, 149, 249, 349, 449). |  | `49`, `149`, `249`, `349`, `449` |
| `started` | Number of started episodes; an episode is started when at least one control action was executed (an automatic reset alone does not count). | count | `2` |
| `strict_success_rate` | successes / started (strict denominator: every started episode). | fraction | `1.0`, `0.0`, `0.5` |
| `conditional_success_rate` | successes / normally terminated episodes (excludes incomplete episodes; shown only to expose the difference). | fraction | `1.0`, `0.0`, `0.5` |
| `incomplete_rate` | incomplete / started. | fraction | `0.0` |
| `timeout_rate` | timeouts / started. | fraction | `0.0`, `1.0`, `0.5` |
| `wrong_target_rate` | wrong_targets / started. | fraction | `0.0` |
| `infrastructure_failure_rate` | infrastructure_failures / started. | fraction | `0.0` |
| `simulation_anomaly_rate` | simulation_anomalies / started. | fraction | `0.0` |
| `release_failure_rate` | Fraction of episodes in which the stalk was never released. | fraction | `0.0`, `1.0`, `0.5` |
| `cutter_gate_rejection_rate` | Fraction of executed cutter commands rejected by the blade gate. | fraction | 0.8636 to 0.9992; 40 empty |
| `min_tip_distance_m` | Minimum blade-tip distance to the cut point. | m | 0.0174 to 0.6684 |
| `min_alignment_rad` | Minimum blade alignment error. | rad | 0.0001021 to 0.001695 |
| `success_time_s` | Mean time to success over successful episodes. | s | 4.567 to 15.03; 41 empty |
| `penalized_time_s` | Time to success, with failed episodes assigned the 120 s time limit. | s | 4.567 to 120 |
| `episode_length` | Episode length. | control steps (1/30 s) | 137 to 3600 |
| `rl_retained_norm` | Mean retained RL action norm. |  | 0 to 1.364 |
| `action_modified_fraction` | Fraction of action components modified by the servo/safety layer. | fraction | 0.3376 to 0.6667 |
| `execution_clip_fraction` | Fraction of actions clipped at execution. | fraction | 0 to 0.1557 |

### A_S1_S2_blade_and_object_gates/paired_robustness_D_vs_E/training_seed_metrics.csv

Paired D − E differences per condition × training seed.

Rows: 50. Columns: 9.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `condition` | Perturbation condition of the S1 robustness study: baseline (nominal), unseen_pose_light/heavy (robot root pose not seen in training), perception_light/heavy (observation noise), delay_light/heavy (action delay), joint_bias_light/heavy (joint encoder bias), combined; translation_only / yaw_only = root-pose components in isolation. |  | 10 distinct, e.g. `baseline` |
| `training_seed` | Seed of the PPO training run whose checkpoint was evaluated (five seeds: 49, 149, 249, 349, 449). |  | `49`, `149`, `249`, `349`, `449` |
| `n_pairs` | Number of paired episodes (D vs E, identical initial observation). | count | `2` |
| `D_success_rate` | Success rate of group D (learned policy) for this training seed and condition. | fraction | `1`, `0`, `0.5` |
| `D_penalized_time_s` | Mean penalized time of group D. | s | 4.583 to 120 |
| `E_success_rate` | Success rate of group E (zero-RL) for this training seed and condition. | fraction | `1`, `0`, `0.5` |
| `E_penalized_time_s` | Mean penalized time of group E. | s | 4.567 to 120 |
| `success_delta_D_minus_E` | D success rate minus E success rate. | fraction | `0`, `0.0`, `-0.5`, `0.5`, `-1` |
| `time_delta_D_minus_E_s` | D penalized time minus E penalized time. | s | -57.43 to 115.1 |

## B_S3_confirmation_scene11

### B_S3_confirmation_scene11/figure_data/fig1_full_harvest_repeatability.csv

The 13 Stage B nominal full harvests: clearance, landing peak, landing usage and the frame of every cut, release and exit (paper Fig. 7 and Fig. 10a).

Rows: 13. Columns: 22.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `case` | Unique run identifier. Prefix encodes the study (H4176/H4177 = S3 confirmation, H4178 = ablations/baselines/generalization, H4179 = fair planner BL5e) and the suffix encodes group, level and repetition. |  | 13 distinct, e.g. `H4177209_STAGE_B_B1_FULL_01` |
| `group` | Experimental arm. See README §5 (group codes) for the meaning of every code in this file. |  | `B1_NOMINAL_FULL`, `B1_FULL` |
| `seed` | Random seed. In S3 studies this is the process seed passed to the simulator; in S1/S2 studies it is the evaluation (scene) seed. |  | 77209 to 77221 |
| `passed` | Run passed its role's acceptance criterion under the S3+L judge (for full-harvest roles: complete ordered harvest and no safety failure). In fig3: number of passing runs for the tier. | bool / count | `True` |
| `safety` | True if no safety failure was found under the S3+L judge (full-arm clearance ≥ 2 mm outside the blade's legal contact, landing within the registered exemption, no ungated cut, no wrong release). | bool | `True` |
| `frames` | Number of integrated control frames in the run (one frame = 1/30 s simulated; a full harvest takes about 600 frames = 20 s). | frame | `600`, `599`, `597` |
| `nonblade_min_mm` | Minimum gap between any non-blade arm part and the plant over the run, over all 144 arm–plant shape pairs (S3 requires ≥ 2 mm). | mm | 2.944 to 2.965 |
| `outside_min_gap_incl_blade_mm` | Minimum signed gap over all pairs including the blade, outside the blade's legal contact with the current target (negative = penetration). | mm | `-0.425`, `-0.426` |
| `peak_substep_force_n` | Peak contact force on any single arm shape during landing of a severed object, read at solver substeps (16 per frame). Registered cap: 300 N. | N | 282.5 to 283.3 |
| `landing_cycles_used` | Number of control periods spent under the landing exemption (cap 25). | periods | `11` |
| `landing_max_penetration_mm` | Maximum penetration recorded during exempted landing (cap 8 mm). | mm | `6.293`, `6.279`, `6.28`, `6.294`, `6.278`, `6.292` |
| `observer_rows` | Number of solver-substep observer records written (16 per frame; 9,600 for 600 frames). | count | `9600`, `9584`, `9552` |
| `wall_min` | Wall-clock time of the run. | min | 101.2 to 106.6 |
| `cut1_step` | Frame of the P2 cut. | frame | `28` |
| `cut2_step` | Frame of the P0 cut. | frame | `356`, `355` |
| `cut3_step` | Frame of the stalk cut. | frame | `588`, `587`, `585` |
| `release1_step` | Frame of the P2 release. | frame | `29` |
| `release2_step` | Frame of the P0 release. | frame | `357`, `356` |
| `release3_step` | Frame of the stalk release. | frame | `589`, `588`, `586` |
| `exit1_step` | Frame of sustained exit from P2. | frame | `229` |
| `exit2_step` | Frame of sustained exit from P0. | frame | `399`, `398` |
| `exit3_step` | Frame of sustained exit from the stalk. | frame | `599`, `598`, `596` |

### B_S3_confirmation_scene11/figure_data/fig2_event_timeline_long.csv

Long-format event timeline of the 13 Stage B harvests (paper Fig. 7a): one row per event.

Rows: 123. Columns: 6.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `case` | Unique run identifier. Prefix encodes the study (H4176/H4177 = S3 confirmation, H4178 = ablations/baselines/generalization, H4179 = fair planner BL5e) and the suffix encodes group, level and repetition. |  | 15 distinct, e.g. `H4177206_STAGE_B_B1_HANDOFF_01` |
| `group` | Experimental arm. See README §5 (group codes) for the meaning of every code in this file. |  | `B1_NOMINAL_FULL`, `B1_FULL`, `B1_HANDOFF` |
| `event` | Event type: CUT, release, exit. |  | `CUT`, `release`, `exit` |
| `order` | Position of the object in the cut order (1 = P2, 2 = P0, 3 = stalk). |  | `1`, `2`, `3` |
| `object` | Object: petiole_2 (P2, first blocking petiole), petiole_0 (P0, second blocking petiole), stalk_1 (stalk of the ripe FFB). |  | `petiole_2`, `petiole_0`, `stalk_1` |
| `physics_step` | Frame at which the event occurred. | frame | 28 to 599 |

### B_S3_confirmation_scene11/figure_data/fig3_holdout_tier_status.csv

Static screening status of the 14 held-out tiers before Stage B (paper Fig. 8). The Chinese duplicate column exclusion_reason_zh was removed; exclusion_reason carries the same content in English.

Rows: 14. Columns: 15.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `tier` | Held-out perturbation tier (same codes as `level`). |  | 14 distinct, e.g. `JOINT_0_POS` |
| `eligible` | Tier passed the static start screen and could be executed by the frozen controller. | bool | `False`, `True` |
| `in_primary_denominator` | Tier is in the primary Stage B denominator (10 of 14 tiers; the 4 physically infeasible tiers are reported but excluded). | bool | `True`, `False` |
| `exclusion_reason` | Why the tier was refused: frozen_complete_initial_path_not_qualified (start route not qualified within the first-object clock), initial_all144_below_2mm (start already violates 2 mm clearance), outside_original_joint_limits. |  | 3 distinct, e.g. `frozen_complete_initial_path_not_qual…`; 1 empty |
| `base_offset_m` | Robot base offset of the tier [x, y, z]. | m | 7 distinct, e.g. `[0.0, 0.0, 0.0]`; 3 empty |
| `yaw_deg` | Robot base yaw offset of the tier. | deg | `0.0`, `-2.0`, `2.0`; 3 empty |
| `initial_all144_min_gap_mm` | Minimum gap over all 144 arm–plant shape pairs at the start configuration (negative = start already interpenetrates). | mm | -25.45 to 41.58; 1 empty |
| `joint_limit_violation` | Violated joint limit, if any (radians). | rad | `q3=-1.540804 < lower -1.539380`; 13 empty |
| `frozen_path_failure` | Why the frozen route could not be used from this tier's start. |  | `fresh_frozen_endpoint_refused`, `fresh_joint_path_or_original240_refused`, `frozen transfer root mismatch`; 5 empty |
| `path_version` | Version of the frozen joint routes used in screening. |  | 1 distinct, e.g. `fresh_original_checked_joint_routes_h…`; 5 empty |
| `carried_from` | Earlier study whose screening result was reused (physical, version independent). |  | 1 distinct, e.g. `H4176 static screen (physical, versio…`; 11 empty |
| `evidence_files` | Paths of the screening evidence files. |  | 14 distinct, e.g. `formal_confirmation/H4177_STAGE_B/hol…` |
| `evidence_sha256` | SHA-256 of the evidence file(s). | hex | 14 distinct, e.g. `72eb092fa56c54271cbe605e64c5da89f6607…` |
| `runs` | Number of runs executed for the tier. | count | `0`, `3` |
| `passed` | Number of passing runs for the tier. | count | `0` |

### B_S3_confirmation_scene11/figure_data/fig4_hold_drift.csv

Cold hold tests: drift of the blade tip and joints while holding the start pose.

Rows: 5. Columns: 8.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `case` | Unique run identifier. Prefix encodes the study (H4176/H4177 = S3 confirmation, H4178 = ablations/baselines/generalization, H4179 = fair planner BL5e) and the suffix encodes group, level and repetition. |  | `H4177201_STAGE_B_B1_HOLD_01`, `H4177202_STAGE_B_B1_HOLD_02`, `H4177203_STAGE_B_B1_HOLD_03`, `H4177204_STAGE_B_B1_HOLD_04`, `H4177205_STAGE_B_B1_HOLD_05` |
| `seed` | Random seed. In S3 studies this is the process seed passed to the simulator; in S1/S2 studies it is the evaluation (scene) seed. |  | `77201`, `77202`, `77203`, `77204`, `77205` |
| `passed` | Run passed its role's acceptance criterion under the S3+L judge (for full-harvest roles: complete ordered harvest and no safety failure). In fig3: number of passing runs for the tier. | bool / count | `True` |
| `safety` | True if no safety failure was found under the S3+L judge (full-arm clearance ≥ 2 mm outside the blade's legal contact, landing within the registered exemption, no ungated cut, no wrong release). | bool | `True` |
| `frames` | Number of integrated control frames in the run (one frame = 1/30 s simulated; a full harvest takes about 600 frames = 20 s). | frame | `34` |
| `nonblade_min_mm` | Minimum gap between any non-blade arm part and the plant over the run, over all 144 arm–plant shape pairs (S3 requires ≥ 2 mm). | mm | `10.204` |
| `hold_max_tip_drift_mm` | Maximum drift of the blade tip during the cold hold test. | mm | `1.201` |
| `hold_max_q_drift_mrad` | Maximum joint-angle drift during the cold hold test. | mrad | `0.3682` |

### B_S3_confirmation_scene11/figure_data/fig5_contact_degradation_stops.csv

Runs of the contact-degradation tier and why each stopped.

Rows: 5. Columns: 13.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `case` | Unique run identifier. Prefix encodes the study (H4176/H4177 = S3 confirmation, H4178 = ablations/baselines/generalization, H4179 = fair planner BL5e) and the suffix encodes group, level and repetition. |  | 5 distinct, e.g. `H4177222_STAGE_B_B2_CONTACT_DROP3_FOR…` |
| `seed` | Random seed. In S3 studies this is the process seed passed to the simulator; in S1/S2 studies it is the evaluation (scene) seed. |  | `77222`, `77223`, `77224` |
| `status` | Run status from the queue: finished / PASSED / FAILED = executed; NOT_STARTED = registered but not launched (counted in the denominator); stopped_at_screening = refused by the start screen before physics; static_check = evaluated by static geometry only; reference_only = copied from an earlier study; INTERRUPTED_INFRASTRUCTURE = interrupted by instance migration (counted as failure); running = still running when the table was frozen (development table only). |  | `finished`, `NOT_STARTED` |
| `passed` | Run passed its role's acceptance criterion under the S3+L judge (for full-harvest roles: complete ordered harvest and no safety failure). In fig3: number of passing runs for the tier. | bool / count | `False`; 2 empty |
| `safety` | True if no safety failure was found under the S3+L judge (full-arm clearance ≥ 2 mm outside the blade's legal contact, landing within the registered exemption, no ungated cut, no wrong release). | bool | `True`; 2 empty |
| `frames` | Number of integrated control frames in the run (one frame = 1/30 s simulated; a full harvest takes about 600 frames = 20 s). | frame | `32`; 2 empty |
| `n_cut` | Number of executed cuts. | count | `0`; 2 empty |
| `nonblade_min_mm` | Minimum gap between any non-blade arm part and the plant over the run, over all 144 arm–plant shape pairs (S3 requires ≥ 2 mm). | mm | `10.204`; 2 empty |
| `last_state` | Controller state at the end of the run. |  | `approach_cut`; 2 empty |
| `administrative_stop` | Administrative stop reason, if any. |  | 1 distinct, e.g. `finite_material_contact_refit_budget_…`; 2 empty |
| `failure_category` | Classified failure: success; administrative_stop; contact_or_other_gate_rejected; approach_distance_not_reached; delayed_distance_mask_at_ready_gate. In S3 tables: post-hoc classification of non-passing runs. |  | `administrative_stop`; 2 empty |
| `rejecting_gate` | Gate that rejected the run (incomplete_or_wrong_CUT_order = the three cuts were not completed in the required order). |  | `incomplete_or_wrong_CUT_order`; 2 empty |
| `refusal_reasons` | JSON counts of cut refusals by gate component (cut:cutter, cut:contact, cut:blade_face, …) over the run. | JSON / count | 1 distinct, e.g. `{"cut:cutter": 33, "cut:contact": 31,…`; 2 empty |

### B_S3_confirmation_scene11/figure_data/fig6_cross_version_nominal_full_harvest.csv

Nominal full harvests across controller versions (H4176, Stage A versions, Stage B version).

Rows: 32. Columns: 13.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `version` | Controller version compared across studies (H4176 = Confirmation I version; E3F, E3G = Stage A development versions; E3g+contact_hook = Stage B version with contact-degradation input). |  | `H4176`, `E3g+contact_hook`, `E3F`, `E3G` |
| `stage` | Study stage. In run_table_H4176_confirmation_I: 1 = nominal stage, 2 = perturbation stage. In fig6: the study the row comes from. |  | `H4177_stage_B`, `2`, `H4177_stage_A`, `1` |
| `case` | Unique run identifier. Prefix encodes the study (H4176/H4177 = S3 confirmation, H4178 = ablations/baselines/generalization, H4179 = fair planner BL5e) and the suffix encodes group, level and repetition. |  | 32 distinct, e.g. `H4176_CONFIRM_S1_FULL_01` |
| `seed` | Random seed. In S3 studies this is the process seed passed to the simulator; in S1/S2 studies it is the evaluation (scene) seed. |  | 71011 to 77221 |
| `attempted` | In per-run tables: True if the unit was launched. In group-outcome tables: number of units launched. | bool / count | `True`, `False` |
| `passed` | Run passed its role's acceptance criterion under the S3+L judge (for full-harvest roles: complete ordered harvest and no safety failure). In fig3: number of passing runs for the tier. | bool / count | `True`, `False`; 2 empty |
| `frames` | Number of integrated control frames in the run (one frame = 1/30 s simulated; a full harvest takes about 600 frames = 20 s). | frame | `600`, `599`, `418`, `597`; 2 empty |
| `P2_CUT` | Frame of the P2 cut. | frame | `28`, `30`; 2 empty |
| `P0_CUT` | Frame of the P0 cut. | frame | `356`, `355`, `360`; 2 empty |
| `stalk1_CUT` | Frame of the stalk cut. | frame | `588`, `587`, `585`; 3 empty |
| `nonblade_min_mm` | Minimum gap between any non-blade arm part and the plant over the run, over all 144 arm–plant shape pairs (S3 requires ≥ 2 mm). | mm | 2.912 to 2.965; 2 empty |
| `peak_substep_force_n` | Peak contact force on any single arm shape during landing of a severed object, read at solver substeps (16 per frame). Registered cap: 300 N. | N | 282.5 to 283.3; 3 empty |
| `source_table` | Original table from which the row was taken. |  | 4 distinct, e.g. `formal_confirmation/H4176_EXECUTION_V…` |

### B_S3_confirmation_scene11/run_tables/run_table_H4176_confirmation_I.csv

Confirmation I (paper Table 8, left part): every registered unit, including excluded perturbation tiers, with eligibility decision, verdict, landing measurements and event frames. Stage 1 = nominal (hold, handoff, full harvest); stage 2 = perturbation tiers. Note: group prefixes S1_/S2_ in this file mean stage 1 / stage 2 of Confirmation I, not success predicates.

Rows: 72. Columns: 54.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `case` | Unique run identifier. Prefix encodes the study (H4176/H4177 = S3 confirmation, H4178 = ablations/baselines/generalization, H4179 = fair planner BL5e) and the suffix encodes group, level and repetition. |  | 72 distinct, e.g. `H4176_CONFIRM_S1_HOLD_01` |
| `stage` | Study stage. In run_table_H4176_confirmation_I: 1 = nominal stage, 2 = perturbation stage. In fig6: the study the row comes from. |  | `2`, `1` |
| `group` | Experimental arm. See README §5 (group codes) for the meaning of every code in this file. |  | 21 distinct, e.g. `S1_HOLD` |
| `role` | Purpose of the run inside the protocol: full_harvest / main = complete three-cut harvest; first_petiole_handoff = runs until the first petiole has been cut, released and exited; normal_gravity_cold_hold / cold_hold = holds the start pose under gravity to measure drift; auxiliary_cold / aux_same_input_cold_restore = cold process restored from the same saved input to check replay identity. |  | `full_harvest`, `normal_gravity_cold_hold`, `first_petiole_handoff` |
| `process_seed` | Simulator process seed of the run. |  | 71011 to 71072 |
| `scenario_seed` | Seed of the procedural plantation scene. 71011 = scene 11 (the only S3 scene); 1743 / 2743 = the two S1 nominal scene seeds. |  | `71011` |
| `perturbation` | JSON description of the perturbation applied to the start (kind = base_translation [axis, value_m], base_yaw [value_deg], initial_joint [joint_index, delta_rad, screening evidence], or contact_reading_degradation [drop_every_nth_frame, force_scale]). Empty for nominal units. | JSON | 17 distinct, e.g. `{"kind": "base_translation", "axis": …`; 21 empty |
| `eligibility` | Eligibility decision for the unit: included, or the reason for exclusion (frozen root translation/quaternion locked; start route not qualified; start clearance below 2 mm on some of the 144 pairs; start outside joint limits; no frozen interface for contact degradation). |  | 7 distinct, e.g. `included` |
| `status` | Run status from the queue: finished / PASSED / FAILED = executed; NOT_STARTED = registered but not launched (counted in the denominator); stopped_at_screening = refused by the start screen before physics; static_check = evaluated by static geometry only; reference_only = copied from an earlier study; INTERRUPTED_INFRASTRUCTURE = interrupted by instance migration (counted as failure); running = still running when the table was frozen (development table only). |  | `NOT_STARTED`, `PASSED`, `FAILED` |
| `eligibility_details` | JSON with the detailed exclusion reason. | JSON | 4 distinct, e.g. `{}` |
| `attempted` | In per-run tables: True if the unit was launched. In group-outcome tables: number of units launched. | bool / count | `False`, `True` |
| `process_started` | True if a simulator process was started for this unit. | bool | `False`, `True` |
| `passed` | Run passed its role's acceptance criterion under the S3+L judge (for full-harvest roles: complete ordered harvest and no safety failure). In fig3: number of passing runs for the tier. | bool / count | `True`, `False`; 42 empty |
| `safety_passed` | Same as `safety`. | bool | `True`; 42 empty |
| `full_success` | True if all three objects were cut, released and exited in order (P2 → P0 → stalk) with no safety failure. | bool | `False`, `True`; 42 empty |
| `integrated_frames` | Number of integrated control frames. | frame | `600`, `36`, `34`, `229`, `599`, `32`; 42 empty |
| `wall_s` | Wall-clock time of the run. | s | 101.5 to 8894; 42 empty |
| `wrong_releases` | Number of attachment releases that were duplicated, out of order or mistimed (release must occur at cut frame + 1). | count | `0`; 42 empty |
| `unsafe_CUT` | Number of executed cuts for which the original physical blade gates (before or after the frame) or the identity permission did not pass. | count | `0`; 42 empty |
| `termination_reason` | Termination record: a JSON with success=true for a completed harvest, otherwise a stop code (see `stop_reason`). |  | 5 distinct, e.g. `screened_init_actual_hold_verified_no…`; 42 empty |
| `landing_entered` | The landing exemption was entered. | bool | `False`, `True`; 42 empty |
| `landing_used_cycles` | Same as landing_cycles_used. | periods | `0`, `11`; 42 empty |
| `landing_observed_boundary_force_peak_n` | Peak landing force read only at control boundaries (shows the under-estimate, ≈70 N vs ≈283 N). | N | 69.96 to 70.02; 59 empty |
| `landing_actual_solver_force_peak_n` | Peak landing force read at solver substeps. | N | 282.5 to 283.3; 59 empty |
| `landing_max_recorded_penetration_m` | Same, in metres. | m | 0.006279 to 0.006294; 59 empty |
| `outside_min_gap_m` | Same as outside_min_gap_incl_blade_mm, in metres. | m | -0.0004256 to 0.0102; 42 empty |
| `outside_nonblade_min_gap_m` | Minimum non-blade gap over the run, in metres. | m | 0.002944 to 0.02164; 42 empty |
| `solver_coverage_complete` | Every solver substep was observed. | bool | `True`; 42 empty |
| `observed_solver_substeps` | Number of solver substeps observed. | count | `9600`, `576`, `544`, `3664`, `9584`, `512`; 42 empty |
| `expected_solver_substeps` | Number of solver substeps expected. | count | `9600`, `576`, `544`, `3664`, `9584`, `512`; 42 empty |
| `fatal_observer_failure` | The substep observer failed. | bool | `False`; 42 empty |
| `fatal_evidence_failure` | Evidence for the verdict was missing or corrupt. | bool | `False`; 42 empty |
| `failure_category` | Classified failure: success; administrative_stop; contact_or_other_gate_rejected; approach_distance_not_reached; delayed_distance_mask_at_ready_gate. In S3 tables: post-hoc classification of non-passing runs. |  | `administrative_stop`; 63 empty |
| `failed_object` | Object being handled when the run failed (empty if none). |  | always empty |
| `failed_stage` | Controller state in which the run failed. |  | `await_task_completion`, `approach_cut`, `deferred_until_hold_gate_passes`, `exit`; 42 empty |
| `failed_frame` | Frame of the failure (empty if none). | frame | always empty |
| `rejecting_gate` | Gate that rejected the run (incomplete_or_wrong_CUT_order = the three cuts were not completed in the required order). |  | `incomplete_or_wrong_CUT_order`; 63 empty |
| `associated_gap_m` | Gap at the failing event (empty if none). | m | always empty |
| `associated_force_n` | Force at the failing event (empty if none). | N | always empty |
| `reader_error` | Error while reading the raw archive (empty if none). |  | always empty |
| `process_returncode` | Exit code of the simulator process. |  | `0`; 42 empty |
| `attempt_error` | Launcher error (empty if none). |  | always empty |
| `raw_archive_sha256` | SHA-256 of the raw trajectory archive of the run (raw archives are not in this package; available on request). | hex | 30 distinct, e.g. `3d6e28345cb128a5b37bc3605940f2a49f654…`; 42 empty |
| `acceptance_sha256` | SHA-256 of the acceptance (judge) output. | hex | 30 distinct, e.g. `285d73c91f81492bd865dd5125749357852e3…`; 42 empty |
| `root_causes` | List of diagnosed root causes (empty if none). |  | `[]` |
| `P2_CUT_frame` | Frame of the P2 cut. | frame | `28`; 56 empty |
| `P2_release_frame` | Frame of the P2 release. | frame | `29`; 56 empty |
| `P2_exit_frame` | Frame of sustained exit from P2. | frame | `229`; 56 empty |
| `P0_CUT_frame` | Frame of the P0 cut. | frame | `356`, `355`; 59 empty |
| `P0_release_frame` | Frame of the P0 release. | frame | `357`, `356`; 59 empty |
| `P0_exit_frame` | Frame of sustained exit from P0. | frame | `399`, `398`; 59 empty |
| `stalk1_CUT_frame` | Frame of the stalk cut. | frame | `588`, `587`; 59 empty |
| `stalk1_release_frame` | Frame of the stalk release. | frame | `589`, `588`; 59 empty |
| `stalk1_exit_frame` | Frame of sustained exit from the stalk. | frame | `599`, `598`; 59 empty |

### B_S3_confirmation_scene11/run_tables/run_table_H4177_stageA_development.csv

Stage A development runs (not part of any confirmatory denominator), by controller variant.

Rows: 41. Columns: 18.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `case` | Unique run identifier. Prefix encodes the study (H4176/H4177 = S3 confirmation, H4178 = ablations/baselines/generalization, H4179 = fair planner BL5e) and the suffix encodes group, level and repetition. |  | 41 distinct, e.g. `H4177101_DEV_E1_J0NEG_D0` |
| `variant` | Development version of the S3 controller (E1 … E3G). E3G is the frozen version used for Stage B. |  | 9 distinct, e.g. `E1` |
| `source` | Original path of the run directory inside the simulation container (/workspace/…). Kept for traceability; not needed to read the data. |  | 9 distinct, e.g. `source_h4177001` |
| `level` | Perturbation tier or scene. NOMINAL = registered start on scene 11; TRANSLATION_{X,Y,Z}_{NEG,POS} = robot base offset of ∓/±0.01 m; YAW_{NEG,POS} = base yaw ∓/±2°; JOINT_k_{NEG,POS} = joint k start offset ∓/±0.01 rad; CONTACT_DROP3_FORCE08 = contact-sensor degradation (contact reading dropped every 3rd frame, reported force scaled ×0.8); h4178_unseen_783xx = one of five unseen procedurally generated geometries. |  | `NOMINAL`, `JOINT_0_NEG`, `JOINT_2_POS`, `JOINT_3_POS` |
| `mode` | Execution mode of the run (full_harvest, handoff, hold, cold_restore, cold_P0_qualification = cold replay that qualifies the P0 route, full_nolive = full harvest without the live/cold comparison). |  | `handoff`, `cold_P0_qualification`, `full_harvest`, `full_nolive` |
| `role` | Purpose of the run inside the protocol: full_harvest / main = complete three-cut harvest; first_petiole_handoff = runs until the first petiole has been cut, released and exited; normal_gravity_cold_hold / cold_hold = holds the start pose under gravity to measure drift; auxiliary_cold / aux_same_input_cold_restore = cold process restored from the same saved input to check replay identity. |  | `main`, `auxiliary_cold` |
| `seed` | Random seed. In S3 studies this is the process seed passed to the simulator; in S1/S2 studies it is the evaluation (scene) seed. |  | 77101 to 77129 |
| `status` | Run status from the queue: finished / PASSED / FAILED = executed; NOT_STARTED = registered but not launched (counted in the denominator); stopped_at_screening = refused by the start screen before physics; static_check = evaluated by static geometry only; reference_only = copied from an earlier study; INTERRUPTED_INFRASTRUCTURE = interrupted by instance migration (counted as failure); running = still running when the table was frozen (development table only). |  | `finished`, `NOT_STARTED` |
| `passed` | Run passed its role's acceptance criterion under the S3+L judge (for full-harvest roles: complete ordered harvest and no safety failure). In fig3: number of passing runs for the tier. | bool / count | `True`, `False`; 2 empty |
| `safety` | True if no safety failure was found under the S3+L judge (full-arm clearance ≥ 2 mm outside the blade's legal contact, landing within the registered exemption, no ungated cut, no wrong release). | bool | `True`; 7 empty |
| `frames` | Number of integrated control frames in the run (one frame = 1/30 s simulated; a full harvest takes about 600 frames = 20 s). | frame | 0 to 600; 2 empty |
| `cut_steps` | Executed cuts as object@frame (e.g. petiole2@28 petiole0@355 stalk1@587). | frame | 12 distinct, e.g. `36`; 22 empty |
| `stop_reason` | Why the controller stopped. Examples: h4178_uniform_no_release_within_480_frames:(object) = baseline-only administrative stop when no new release occurs within 480 frames; bl5_no_collision_free_plan / bl5e_no_collision_free_plan = planner found no plan within budget; first_handoff_mechanism_complete = handoff role finished; finite_*_budget_exhausted = a bounded retry budget of our controller ran out; *_refused / invalid_* = our controller refused to continue because a frozen route or forecast was not valid for the current state; 'our frozen pipeline refused the unseen geometry before physics' = start refused. |  | 8 distinct, e.g. `finite_preCUT_departure_budget_exhausted`; 17 empty |
| `nonblade_min_mm` | Minimum gap between any non-blade arm part and the plant over the run, over all 144 arm–plant shape pairs (S3 requires ≥ 2 mm). | mm | 2.912 to 21.22; 18 empty |
| `peak_substep_force_n` | Peak contact force on any single arm shape during landing of a severed object, read at solver substeps (16 per frame). Registered cap: 300 N. | N | `283.32781982421875`, `282.5999755859375`, `282.5054626464844`; 38 empty |
| `observer_rows` | Number of solver-substep observer records written (16 per frame; 9,600 for 600 frames). | count | 480 to 9600; 15 empty |
| `archive_sha256` | SHA-256 of the run archive. | hex | 39 distinct, e.g. `41c89dfb7a5c4fa631bf498d937326d5e85bb…`; 2 empty |
| `note` | Free-text note. |  | 8 distinct, e.g. `pre-acceptance-tool run (E1-E3b); jud…`; 21 empty |

### B_S3_confirmation_scene11/run_tables/run_table_H4177_stageB_confirmation_II.csv

Stage B / Confirmation II (paper Table 8): 26 registered units (B1 nominal full harvest, handoff and hold; B2 held-out contact-degradation tier) plus 39 auxiliary cold-restore processes.

Rows: 65. Columns: 46.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `case` | Unique run identifier. Prefix encodes the study (H4176/H4177 = S3 confirmation, H4178 = ablations/baselines/generalization, H4179 = fair planner BL5e) and the suffix encodes group, level and repetition. |  | 65 distinct, e.g. `H4177201_STAGE_B_B1_HOLD_01` |
| `group` | Experimental arm. See README §5 (group codes) for the meaning of every code in this file. |  | `AUX_COLD_RESTORE`, `B1_NOMINAL_FULL`, `B1_HOLD`, `B2_CONTACT_DROP3_FORCE08`, `B1_HANDOFF`, `B1_FULL` |
| `role` | Purpose of the run inside the protocol: full_harvest / main = complete three-cut harvest; first_petiole_handoff = runs until the first petiole has been cut, released and exited; normal_gravity_cold_hold / cold_hold = holds the start pose under gravity to measure drift; auxiliary_cold / aux_same_input_cold_restore = cold process restored from the same saved input to check replay identity. |  | `aux_same_input_cold_restore`, `full_harvest`, `cold_hold`, `first_petiole_handoff` |
| `mode` | Execution mode of the run (full_harvest, handoff, hold, cold_restore, cold_P0_qualification = cold replay that qualifies the P0 route, full_nolive = full harvest without the live/cold comparison). |  | `cold_restore`, `full_harvest`, `hold`, `handoff` |
| `level` | Perturbation tier or scene. NOMINAL = registered start on scene 11; TRANSLATION_{X,Y,Z}_{NEG,POS} = robot base offset of ∓/±0.01 m; YAW_{NEG,POS} = base yaw ∓/±2°; JOINT_k_{NEG,POS} = joint k start offset ∓/±0.01 rad; CONTACT_DROP3_FORCE08 = contact-sensor degradation (contact reading dropped every 3rd frame, reported force scaled ×0.8); h4178_unseen_783xx = one of five unseen procedurally generated geometries. |  | `NOMINAL`, `CONTACT_DROP3_FORCE08` |
| `seed` | Random seed. In S3 studies this is the process seed passed to the simulator; in S1/S2 studies it is the evaluation (scene) seed. |  | 77201 to 77224; 39 empty |
| `contact_degradation` | Contact-sensor degradation applied (drop3_force08 = contact reading dropped every 3rd frame, force scaled ×0.8). |  | `drop3_force08`; 60 empty |
| `status` | Run status from the queue: finished / PASSED / FAILED = executed; NOT_STARTED = registered but not launched (counted in the denominator); stopped_at_screening = refused by the start screen before physics; static_check = evaluated by static geometry only; reference_only = copied from an earlier study; INTERRUPTED_INFRASTRUCTURE = interrupted by instance migration (counted as failure); running = still running when the table was frozen (development table only). |  | `finished`, `NOT_STARTED`, `INTERRUPTED_INFRASTRUCTURE` |
| `attempted` | In per-run tables: True if the unit was launched. In group-outcome tables: number of units launched. | bool / count | `True`, `False` |
| `passed` | Run passed its role's acceptance criterion under the S3+L judge (for full-harvest roles: complete ordered harvest and no safety failure). In fig3: number of passing runs for the tier. | bool / count | `True`, `False`; 2 empty |
| `safety` | True if no safety failure was found under the S3+L judge (full-arm clearance ≥ 2 mm outside the blade's legal contact, landing within the registered exemption, no ungated cut, no wrong release). | bool | `True`; 42 empty |
| `full_task_complete` | True if the full three-object task completed (Stage B). | bool | `True`, `False`; 42 empty |
| `started_utc` | Launch time (UTC, ISO 8601). |  | 63 distinct, e.g. `2026-10-31T09:45:11.060364+00:00`; 2 empty |
| `finished_utc` | End time (UTC, ISO 8601). |  | 62 distinct, e.g. `2026-10-31T09:46:50.779784+00:00`; 3 empty |
| `wall_min` | Wall-clock time of the run. | min | 1.7 to 138; 42 empty |
| `returncode` | Exit code of the simulator process (0 = normal exit; negative = terminated by signal, e.g. −15 SIGTERM, −11 SIGSEGV). |  | `0`; 3 empty |
| `frames` | Number of integrated control frames in the run (one frame = 1/30 s simulated; a full harvest takes about 600 frames = 20 s). | frame | `600`, `34`, `599`, `32`, `229`, `597`; 42 empty |
| `n_cut` | Number of executed cuts. | count | `3`, `0`, `1`; 42 empty |
| `cut_steps` | Executed cuts as object@frame (e.g. petiole2@28 petiole0@355 stalk1@587). | frame | `petiole2@28 petiole0@356 stalk1@588`, `petiole2@28 petiole0@355 stalk1@587`, `petiole2@28`, `petiole2@28 petiole0@355 stalk1@585`; 50 empty |
| `release_steps` | Frame at which each cut object's attachment was released: object@frame in folder B, JSON {object: frame} in folders C and D. | frame | `petiole2@29 petiole0@357 stalk1@589`, `petiole2@29 petiole0@356 stalk1@588`, `petiole2@29`, `petiole2@29 petiole0@356 stalk1@586`; 50 empty |
| `exit_steps` | Sustained-exit frame of each object, object@frame. | frame | `petiole2@229 petiole0@399 stalk1@599`, `petiole2@229 petiole0@398 stalk1@598`, `petiole2@229`, `petiole2@229 petiole0@398 stalk1@596`; 50 empty |
| `wrong_releases` | Number of attachment releases that were duplicated, out of order or mistimed (release must occur at cut frame + 1). | count | `0`; 42 empty |
| `unsafe_CUT` | Number of executed cuts for which the original physical blade gates (before or after the frame) or the identity permission did not pass. | count | `0`; 42 empty |
| `nonblade_min_mm` | Minimum gap between any non-blade arm part and the plant over the run, over all 144 arm–plant shape pairs (S3 requires ≥ 2 mm). | mm | 2.944 to 10.2; 42 empty |
| `outside_min_gap_incl_blade_mm` | Minimum signed gap over all pairs including the blade, outside the blade's legal contact with the current target (negative = penetration). | mm | `-0.425`, `10.204`, `-0.053`, `-0.063`, `-0.426`, `-0.064`; 42 empty |
| `peak_substep_force_n` | Peak contact force on any single arm shape during landing of a severed object, read at solver substeps (16 per frame). Registered cap: 300 N. | N | 282.5 to 283.3; 52 empty |
| `landing_cycles_used` | Number of control periods spent under the landing exemption (cap 25). | periods | `11`, `0`; 42 empty |
| `landing_max_penetration_mm` | Maximum penetration recorded during exempted landing (cap 8 mm). | mm | `6.293`, `6.279`, `6.28`, `6.294`, `6.278`, `6.292`; 52 empty |
| `observer_rows` | Number of solver-substep observer records written (16 per frame; 9,600 for 600 frames). | count | `9600`, `544`, `9584`, `512`, `3664`, `9552`; 42 empty |
| `observer_expected` | Number of observer records expected from the frame count. | count | `9600`, `544`, `9584`, `512`, `3664`, `9552`; 42 empty |
| `hold_max_tip_drift_mm` | Maximum drift of the blade tip during the cold hold test. | mm | `1.201`; 60 empty |
| `hold_max_q_drift_mrad` | Maximum joint-angle drift during the cold hold test. | mrad | `0.3682`; 60 empty |
| `three_cold_passed` | True if all three cold replays of the same saved input matched the live run (all 144 gaps and nine rigid-body poses). | bool | `True`; 52 empty |
| `stop_or_termination` | Termination record or stop code (see `termination_reason`). |  | 4 distinct, e.g. `screened_init_actual_hold_verified_no…`; 42 empty |
| `last_state` | Controller state at the end of the run. |  | `await_task_completion`, `deferred_until_hold_gate_passes`, `approach_cut`, `exit`; 42 empty |
| `administrative_stop` | Administrative stop reason, if any. |  | 1 distinct, e.g. `finite_material_contact_refit_budget_…`; 62 empty |
| `failure_category` | Classified failure: success; administrative_stop; contact_or_other_gate_rejected; approach_distance_not_reached; delayed_distance_mask_at_ready_gate. In S3 tables: post-hoc classification of non-passing runs. |  | `administrative_stop`; 62 empty |
| `failed_stage` | Controller state in which the run failed. |  | `await_task_completion`, `deferred_until_hold_gate_passes`, `approach_cut`, `exit`; 42 empty |
| `rejecting_gate` | Gate that rejected the run (incomplete_or_wrong_CUT_order = the three cuts were not completed in the required order). |  | `incomplete_or_wrong_CUT_order`; 62 empty |
| `refusal_reasons` | JSON counts of cut refusals by gate component (cut:cutter, cut:contact, cut:blade_face, …) over the run. | JSON / count | 4 distinct, e.g. `{"cut:cutter": 596, "cut:contact": 58…`; 49 empty |
| `reasons` | ';'-separated list of rejection reasons. |  | 1 distinct, e.g. `incomplete_or_wrong_CUT_order;incompl…`; 62 empty |
| `raw_archive_sha256` | SHA-256 of the raw trajectory archive of the run (raw archives are not in this package; available on request). | hex | 23 distinct, e.g. `6dfde5c5b8c165f6e4e746c93287fb5eb209d…`; 42 empty |
| `launch_ledger_sha256` | SHA-256 of this launch's ledger record. | hex | 63 distinct, e.g. `b894e05626cfa58f40fab44a7b4c8e7504887…`; 2 empty |
| `evidence` | Path of the evidence file for the row inside the source tree. |  | 26 distinct, e.g. `experiments/H4177201_STAGE_B_B1_HOLD_…`; 39 empty |
| `evidence_sha256` | SHA-256 of the evidence file(s). | hex | 26 distinct, e.g. `9b7b89dd87abb2d64a06a6ef885eab66f6984…`; 39 empty |
| `note` | Free-text note. |  | 15 distinct, e.g. `started 2026-10-31T13:39Z; interrupte…`; 23 empty |

## C_S3_ablations_baselines_generalization

### C_S3_ablations_baselines_generalization/figure_data/exp1_fig_group_outcomes.csv

Per-group outcome counts and Wilson intervals for exp1.

Rows: 8. Columns: 10.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `group` | Experimental arm. See README §5 (group codes) for the meaning of every code in this file. |  | 8 distinct, e.g. `E1_CONTROL` |
| `n` | Number of registered units in the cell. | count | `3` |
| `attempted` | In per-run tables: True if the unit was launched. In group-outcome tables: number of units launched. | bool / count | `3` |
| `strict` | Number of full harvests under strict S3. | count | `0` |
| `landing` | Number of full harvests under S3+L. | count | `0`, `3`, `2` |
| `safety_fail_landing` | Number of units with at least one safety failure under S3+L. | count | `0` |
| `safety_fail_strict` | Number of units with at least one safety failure under strict S3. | count | `3`, `0` |
| `not_started` | Number of registered units that were not started. | count | `0` |
| `wilson_strict` | Wilson 95% interval of strict / n. | fraction | `[0.0, 0.561]` |
| `wilson_landing` | Wilson 95% interval of landing / n. | fraction | `[0.0, 0.561]`, `[0.439, 1.0]`, `[0.208, 0.939]` |

### C_S3_ablations_baselines_generalization/figure_data/exp1_fig_stage_and_safety.csv

Per-run furthest stage and safety counters for exp1 (paper Fig. 9, top).

Rows: 24. Columns: 21.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `case` | Unique run identifier. Prefix encodes the study (H4176/H4177 = S3 confirmation, H4178 = ablations/baselines/generalization, H4179 = fair planner BL5e) and the suffix encodes group, level and repetition. |  | 24 distinct, e.g. `H4178101_E1_CONTROL_R1` |
| `group` | Experimental arm. See README §5 (group codes) for the meaning of every code in this file. |  | 8 distinct, e.g. `E1_CONTROL` |
| `method` | Controller under test. OURS = frozen modular S3 controller; BL1–BL5 = baselines (paper Table 3); BL5E_V1 / BL5E2 = fair sampling-planner baseline BL5e, version 1 (voided after Amendment 01) and version 2 (reported). In A_*/geometry_adaptive_ik: fixed = fixed target library, adaptive = online damped-least-squares IK. |  | `OURS` |
| `switch_off` | Ablation switch disabled in this run (AB1 landing admission, AB2 stalk cached brake, AB3 E3g entry press, AB4 zero-force manifold admission, AB5 temporal interlock, AB6 screened initialization, AB7 live/cold barrier). Empty = no switch disabled. |  | 7 distinct, e.g. `AB1_landing`; 3 empty |
| `level` | Perturbation tier or scene. NOMINAL = registered start on scene 11; TRANSLATION_{X,Y,Z}_{NEG,POS} = robot base offset of ∓/±0.01 m; YAW_{NEG,POS} = base yaw ∓/±2°; JOINT_k_{NEG,POS} = joint k start offset ∓/±0.01 rad; CONTACT_DROP3_FORCE08 = contact-sensor degradation (contact reading dropped every 3rd frame, reported force scaled ×0.8); h4178_unseen_783xx = one of five unseen procedurally generated geometries. |  | `NOMINAL` |
| `rep` | Repetition index within a group × level cell. |  | `1`, `2`, `3` |
| `furthest_stage` | Last milestone reached in the ordered chain P2 cut → P2 release → P2 exit → P0 cut → P0 release → P0 exit → stalk cut → stalk release → stalk exit (written petiole2_CUT … stalk1_exit). none = no milestone; screening = refused at start screening. |  | `stalk1_exit`, `petiole0_exit`, `petiole0_release`; 3 empty |
| `stop_reason` | Why the controller stopped. Examples: h4178_uniform_no_release_within_480_frames:(object) = baseline-only administrative stop when no new release occurs within 480 frames; bl5_no_collision_free_plan / bl5e_no_collision_free_plan = planner found no plan within budget; first_handoff_mechanism_complete = handoff role finished; finite_*_budget_exhausted = a bounded retry budget of our controller ran out; *_refused / invalid_* = our controller refused to continue because a frozen route or forecast was not valid for the current state; 'our frozen pipeline refused the unseen geometry before physics' = start refused. |  | 6 distinct, e.g. `global_P0_bounded_firstfree_all_Origi…`; 14 empty |
| `stop_state` | Controller state machine state at the stop (approach_route, approach_cut, exit, await_task_completion). |  | `await_task_completion`, `approach_cut`, `exit`, `approach_route`; 3 empty |
| `frames` | Number of integrated control frames in the run (one frame = 1/30 s simulated; a full harvest takes about 600 frames = 20 s). | frame | 357 to 600; 3 empty |
| `dangerous_executed_CUT` | Number of integrated frames on which a cut was executed while the full-arm (S3) permission evaluated at that frame was False. | frames | `0`; 3 empty |
| `dangerous_requested_CUT` | Number of integrated frames on which a cut was requested while the full-arm (S3) permission was False (a request may be blocked before execution). | frames | `0`; 3 empty |
| `nonblade_lt2mm_boundaries_strict` | Number of control boundaries at which some non-blade gap was below 2 mm (strict S3). | count | `8`, `0`, `7`; 3 empty |
| `nonblade_lt2mm_boundaries_landing` | Same, under S3+L (exempted landing contacts excluded). | count | `0`; 3 empty |
| `wrong_releases` | Number of attachment releases that were duplicated, out of order or mistimed (release must occur at cut frame + 1). | count | `0`; 3 empty |
| `unsafe_CUT` | Number of executed cuts for which the original physical blade gates (before or after the frame) or the identity permission did not pass. | count | `0`; 3 empty |
| `solver_peak_landing_force_n` | Peak landing contact force at solver substeps (S3+L cap 300 N). | N | 260.7 to 283.3; 6 empty |
| `landing_cycles` | Number of control boundaries handled under the landing exemption. | periods | `10`, `0`, `8`; 3 empty |
| `landing_max_penetration_mm` | Maximum penetration recorded during exempted landing (cap 8 mm). | mm | 6.229 to 6.294; 6 empty |
| `wall_min` | Wall-clock time of the run. | min | 71.5 to 111.9; 3 empty |
| `controller_wall_s` | Wall-clock time spent inside the controller (planning, screening, forecasting). | s | always empty |

### C_S3_ablations_baselines_generalization/figure_data/exp2_fig_group_outcomes.csv

Per-group outcome counts for exp2.

Rows: 5. Columns: 10.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `group` | Experimental arm. See README §5 (group codes) for the meaning of every code in this file. |  | `E2_BL1`, `E2_BL2`, `E2_BL3`, `E2_BL4`, `E2_BL5` |
| `n` | Number of registered units in the cell. | count | `3` |
| `attempted` | In per-run tables: True if the unit was launched. In group-outcome tables: number of units launched. | bool / count | `3` |
| `strict` | Number of full harvests under strict S3. | count | `0` |
| `landing` | Number of full harvests under S3+L. | count | `0` |
| `safety_fail_landing` | Number of units with at least one safety failure under S3+L. | count | `0`, `3` |
| `safety_fail_strict` | Number of units with at least one safety failure under strict S3. | count | `0`, `3` |
| `not_started` | Number of registered units that were not started. | count | `0` |
| `wilson_strict` | Wilson 95% interval of strict / n. | fraction | `[0.0, 0.561]` |
| `wilson_landing` | Wilson 95% interval of landing / n. | fraction | `[0.0, 0.561]` |

### C_S3_ablations_baselines_generalization/figure_data/exp2_fig_stage_and_safety.csv

Per-run furthest stage and safety counters for exp2 (paper Fig. 9, top).

Rows: 15. Columns: 21.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `case` | Unique run identifier. Prefix encodes the study (H4176/H4177 = S3 confirmation, H4178 = ablations/baselines/generalization, H4179 = fair planner BL5e) and the suffix encodes group, level and repetition. |  | 15 distinct, e.g. `H4178201_E2_BL1_R1` |
| `group` | Experimental arm. See README §5 (group codes) for the meaning of every code in this file. |  | `E2_BL1`, `E2_BL2`, `E2_BL3`, `E2_BL4`, `E2_BL5` |
| `method` | Controller under test. OURS = frozen modular S3 controller; BL1–BL5 = baselines (paper Table 3); BL5E_V1 / BL5E2 = fair sampling-planner baseline BL5e, version 1 (voided after Amendment 01) and version 2 (reported). In A_*/geometry_adaptive_ik: fixed = fixed target library, adaptive = online damped-least-squares IK. |  | `BL1`, `BL2`, `BL3`, `BL4`, `BL5` |
| `switch_off` | Ablation switch disabled in this run (AB1 landing admission, AB2 stalk cached brake, AB3 E3g entry press, AB4 zero-force manifold admission, AB5 temporal interlock, AB6 screened initialization, AB7 live/cold barrier). Empty = no switch disabled. |  | always empty |
| `level` | Perturbation tier or scene. NOMINAL = registered start on scene 11; TRANSLATION_{X,Y,Z}_{NEG,POS} = robot base offset of ∓/±0.01 m; YAW_{NEG,POS} = base yaw ∓/±2°; JOINT_k_{NEG,POS} = joint k start offset ∓/±0.01 rad; CONTACT_DROP3_FORCE08 = contact-sensor degradation (contact reading dropped every 3rd frame, reported force scaled ×0.8); h4178_unseen_783xx = one of five unseen procedurally generated geometries. |  | `NOMINAL` |
| `rep` | Repetition index within a group × level cell. |  | `1`, `2`, `3` |
| `furthest_stage` | Last milestone reached in the ordered chain P2 cut → P2 release → P2 exit → P0 cut → P0 release → P0 exit → stalk cut → stalk release → stalk exit (written petiole2_CUT … stalk1_exit). none = no milestone; screening = refused at start screening. |  | `none`, `petiole2_CUT`, `petiole2_exit` |
| `stop_reason` | Why the controller stopped. Examples: h4178_uniform_no_release_within_480_frames:(object) = baseline-only administrative stop when no new release occurs within 480 frames; bl5_no_collision_free_plan / bl5e_no_collision_free_plan = planner found no plan within budget; first_handoff_mechanism_complete = handoff role finished; finite_*_budget_exhausted = a bounded retry budget of our controller ran out; *_refused / invalid_* = our controller refused to continue because a frozen route or forecast was not valid for the current state; 'our frozen pipeline refused the unseen geometry before physics' = start refused. |  | 2 distinct, e.g. `h4178_uniform_no_release_within_480_f…` |
| `stop_state` | Controller state machine state at the stop (approach_route, approach_cut, exit, await_task_completion). |  | always empty |
| `frames` | Number of integrated control frames in the run (one frame = 1/30 s simulated; a full harvest takes about 600 frames = 20 s). | frame | `482`, `59` |
| `dangerous_executed_CUT` | Number of integrated frames on which a cut was executed while the full-arm (S3) permission evaluated at that frame was False. | frames | `0`, `427` |
| `dangerous_requested_CUT` | Number of integrated frames on which a cut was requested while the full-arm (S3) permission was False (a request may be blocked before execution). | frames | `0`, `427` |
| `nonblade_lt2mm_boundaries_strict` | Number of control boundaries at which some non-blade gap was below 2 mm (strict S3). | count | `0`, `394` |
| `nonblade_lt2mm_boundaries_landing` | Same, under S3+L (exempted landing contacts excluded). | count | `0`, `394` |
| `wrong_releases` | Number of attachment releases that were duplicated, out of order or mistimed (release must occur at cut frame + 1). | count | `0` |
| `unsafe_CUT` | Number of executed cuts for which the original physical blade gates (before or after the frame) or the identity permission did not pass. | count | `0`, `427` |
| `solver_peak_landing_force_n` | Peak landing contact force at solver substeps (S3+L cap 300 N). | N | always empty |
| `landing_cycles` | Number of control boundaries handled under the landing exemption. | periods | `0` |
| `landing_max_penetration_mm` | Maximum penetration recorded during exempted landing (cap 8 mm). | mm | always empty |
| `wall_min` | Wall-clock time of the run. | min | 1 to 4.6 |
| `controller_wall_s` | Wall-clock time spent inside the controller (planning, screening, forecasting). | s | 1.564 to 46.65 |

### C_S3_ablations_baselines_generalization/figure_data/exp3a_fig_group_outcomes.csv

Per-group outcome counts for exp3a.

Rows: 5. Columns: 10.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `group` | Experimental arm. See README §5 (group codes) for the meaning of every code in this file. |  | `E3A_BL1`, `E3A_BL2`, `E3A_BL3`, `E3A_BL4`, `E3A_BL5` |
| `n` | Number of registered units in the cell. | count | `10` |
| `attempted` | In per-run tables: True if the unit was launched. In group-outcome tables: number of units launched. | bool / count | `10` |
| `strict` | Number of full harvests under strict S3. | count | `0` |
| `landing` | Number of full harvests under S3+L. | count | `0` |
| `safety_fail_landing` | Number of units with at least one safety failure under S3+L. | count | `0`, `10` |
| `safety_fail_strict` | Number of units with at least one safety failure under strict S3. | count | `0`, `10` |
| `not_started` | Number of registered units that were not started. | count | `0` |
| `wilson_strict` | Wilson 95% interval of strict / n. | fraction | `[0.0, 0.278]` |
| `wilson_landing` | Wilson 95% interval of landing / n. | fraction | `[0.0, 0.278]` |

### C_S3_ablations_baselines_generalization/figure_data/exp3a_fig_stage_and_safety.csv

Per-run furthest stage and safety counters for exp3a (paper Fig. 9, middle).

Rows: 50. Columns: 21.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `case` | Unique run identifier. Prefix encodes the study (H4176/H4177 = S3 confirmation, H4178 = ablations/baselines/generalization, H4179 = fair planner BL5e) and the suffix encodes group, level and repetition. |  | 50 distinct, e.g. `H4178301_E3A_BL1_JOINT_0_POS` |
| `group` | Experimental arm. See README §5 (group codes) for the meaning of every code in this file. |  | `E3A_BL1`, `E3A_BL2`, `E3A_BL3`, `E3A_BL4`, `E3A_BL5` |
| `method` | Controller under test. OURS = frozen modular S3 controller; BL1–BL5 = baselines (paper Table 3); BL5E_V1 / BL5E2 = fair sampling-planner baseline BL5e, version 1 (voided after Amendment 01) and version 2 (reported). In A_*/geometry_adaptive_ik: fixed = fixed target library, adaptive = online damped-least-squares IK. |  | `BL1`, `BL2`, `BL3`, `BL4`, `BL5` |
| `switch_off` | Ablation switch disabled in this run (AB1 landing admission, AB2 stalk cached brake, AB3 E3g entry press, AB4 zero-force manifold admission, AB5 temporal interlock, AB6 screened initialization, AB7 live/cold barrier). Empty = no switch disabled. |  | always empty |
| `level` | Perturbation tier or scene. NOMINAL = registered start on scene 11; TRANSLATION_{X,Y,Z}_{NEG,POS} = robot base offset of ∓/±0.01 m; YAW_{NEG,POS} = base yaw ∓/±2°; JOINT_k_{NEG,POS} = joint k start offset ∓/±0.01 rad; CONTACT_DROP3_FORCE08 = contact-sensor degradation (contact reading dropped every 3rd frame, reported force scaled ×0.8); h4178_unseen_783xx = one of five unseen procedurally generated geometries. |  | 10 distinct, e.g. `JOINT_0_POS` |
| `rep` | Repetition index within a group × level cell. |  | always empty |
| `furthest_stage` | Last milestone reached in the ordered chain P2 cut → P2 release → P2 exit → P0 cut → P0 release → P0 exit → stalk cut → stalk release → stalk exit (written petiole2_CUT … stalk1_exit). none = no milestone; screening = refused at start screening. |  | `none`, `petiole2_CUT`, `petiole2_exit` |
| `stop_reason` | Why the controller stopped. Examples: h4178_uniform_no_release_within_480_frames:(object) = baseline-only administrative stop when no new release occurs within 480 frames; bl5_no_collision_free_plan / bl5e_no_collision_free_plan = planner found no plan within budget; first_handoff_mechanism_complete = handoff role finished; finite_*_budget_exhausted = a bounded retry budget of our controller ran out; *_refused / invalid_* = our controller refused to continue because a frozen route or forecast was not valid for the current state; 'our frozen pipeline refused the unseen geometry before physics' = start refused. |  | 2 distinct, e.g. `h4178_uniform_no_release_within_480_f…` |
| `stop_state` | Controller state machine state at the stop (approach_route, approach_cut, exit, await_task_completion). |  | always empty |
| `frames` | Number of integrated control frames in the run (one frame = 1/30 s simulated; a full harvest takes about 600 frames = 20 s). | frame | `482`, `59`, `60`, `61`, `57` |
| `dangerous_executed_CUT` | Number of integrated frames on which a cut was executed while the full-arm (S3) permission evaluated at that frame was False. | frames | 0 to 482 |
| `dangerous_requested_CUT` | Number of integrated frames on which a cut was requested while the full-arm (S3) permission was False (a request may be blocked before execution). | frames | 0 to 482 |
| `nonblade_lt2mm_boundaries_strict` | Number of control boundaries at which some non-blade gap was below 2 mm (strict S3). | count | `0`, `394`, `395`, `396`, `393`, `374` |
| `nonblade_lt2mm_boundaries_landing` | Same, under S3+L (exempted landing contacts excluded). | count | `0`, `394`, `395`, `396`, `393`, `374` |
| `wrong_releases` | Number of attachment releases that were duplicated, out of order or mistimed (release must occur at cut frame + 1). | count | `0` |
| `unsafe_CUT` | Number of executed cuts for which the original physical blade gates (before or after the frame) or the identity permission did not pass. | count | 0 to 482 |
| `solver_peak_landing_force_n` | Peak landing contact force at solver substeps (S3+L cap 300 N). | N | always empty |
| `landing_cycles` | Number of control boundaries handled under the landing exemption. | periods | `0` |
| `landing_max_penetration_mm` | Maximum penetration recorded during exempted landing (cap 8 mm). | mm | always empty |
| `wall_min` | Wall-clock time of the run. | min | 0.9 to 5 |
| `controller_wall_s` | Wall-clock time spent inside the controller (planning, screening, forecasting). | s | 1.63 to 76.43 |

### C_S3_ablations_baselines_generalization/figure_data/exp3b_fig_group_outcomes.csv

Per-group outcome counts for exp3b.

Rows: 6. Columns: 10.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `group` | Experimental arm. See README §5 (group codes) for the meaning of every code in this file. |  | `E3B_OURS`, `E3B_BL1`, `E3B_BL2`, `E3B_BL3`, `E3B_BL4`, `E3B_BL5` |
| `n` | Number of registered units in the cell. | count | `5` |
| `attempted` | In per-run tables: True if the unit was launched. In group-outcome tables: number of units launched. | bool / count | `5` |
| `strict` | Number of full harvests under strict S3. | count | `0` |
| `landing` | Number of full harvests under S3+L. | count | `0` |
| `safety_fail_landing` | Number of units with at least one safety failure under S3+L. | count | `0`, `5` |
| `safety_fail_strict` | Number of units with at least one safety failure under strict S3. | count | `0`, `5` |
| `not_started` | Number of registered units that were not started. | count | `0` |
| `wilson_strict` | Wilson 95% interval of strict / n. | fraction | `[0.0, 0.434]` |
| `wilson_landing` | Wilson 95% interval of landing / n. | fraction | `[0.0, 0.434]` |

### C_S3_ablations_baselines_generalization/figure_data/exp3b_fig_stage_and_safety.csv

Per-run furthest stage and safety counters for exp3b (paper Fig. 9, bottom).

Rows: 30. Columns: 21.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `case` | Unique run identifier. Prefix encodes the study (H4176/H4177 = S3 confirmation, H4178 = ablations/baselines/generalization, H4179 = fair planner BL5e) and the suffix encodes group, level and repetition. |  | 30 distinct, e.g. `H4178401_E3B_OURS_h4178_unseen_78301` |
| `group` | Experimental arm. See README §5 (group codes) for the meaning of every code in this file. |  | `E3B_OURS`, `E3B_BL1`, `E3B_BL2`, `E3B_BL3`, `E3B_BL4`, `E3B_BL5` |
| `method` | Controller under test. OURS = frozen modular S3 controller; BL1–BL5 = baselines (paper Table 3); BL5E_V1 / BL5E2 = fair sampling-planner baseline BL5e, version 1 (voided after Amendment 01) and version 2 (reported). In A_*/geometry_adaptive_ik: fixed = fixed target library, adaptive = online damped-least-squares IK. |  | `OURS`, `BL1`, `BL2`, `BL3`, `BL4`, `BL5` |
| `switch_off` | Ablation switch disabled in this run (AB1 landing admission, AB2 stalk cached brake, AB3 E3g entry press, AB4 zero-force manifold admission, AB5 temporal interlock, AB6 screened initialization, AB7 live/cold barrier). Empty = no switch disabled. |  | always empty |
| `level` | Perturbation tier or scene. NOMINAL = registered start on scene 11; TRANSLATION_{X,Y,Z}_{NEG,POS} = robot base offset of ∓/±0.01 m; YAW_{NEG,POS} = base yaw ∓/±2°; JOINT_k_{NEG,POS} = joint k start offset ∓/±0.01 rad; CONTACT_DROP3_FORCE08 = contact-sensor degradation (contact reading dropped every 3rd frame, reported force scaled ×0.8); h4178_unseen_783xx = one of five unseen procedurally generated geometries. |  | `h4178_unseen_78301`, `h4178_unseen_78302`, `h4178_unseen_78303`, `h4178_unseen_78304`, `h4178_unseen_78305` |
| `rep` | Repetition index within a group × level cell. |  | always empty |
| `furthest_stage` | Last milestone reached in the ordered chain P2 cut → P2 release → P2 exit → P0 cut → P0 release → P0 exit → stalk cut → stalk release → stalk exit (written petiole2_CUT … stalk1_exit). none = no milestone; screening = refused at start screening. |  | `none`, `screening`, `petiole2_CUT`, `petiole2_exit` |
| `stop_reason` | Why the controller stopped. Examples: h4178_uniform_no_release_within_480_frames:(object) = baseline-only administrative stop when no new release occurs within 480 frames; bl5_no_collision_free_plan / bl5e_no_collision_free_plan = planner found no plan within budget; first_handoff_mechanism_complete = handoff role finished; finite_*_budget_exhausted = a bounded retry budget of our controller ran out; *_refused / invalid_* = our controller refused to continue because a frozen route or forecast was not valid for the current state; 'our frozen pipeline refused the unseen geometry before physics' = start refused. |  | 3 distinct, e.g. `our frozen pipeline refused the unsee…` |
| `stop_state` | Controller state machine state at the stop (approach_route, approach_cut, exit, await_task_completion). |  | always empty |
| `frames` | Number of integrated control frames in the run (one frame = 1/30 s simulated; a full harvest takes about 600 frames = 20 s). | frame | `482`, `64`, `76`, `67`, `35`, `60`; 5 empty |
| `dangerous_executed_CUT` | Number of integrated frames on which a cut was executed while the full-arm (S3) permission evaluated at that frame was False. | frames | `0`, `73`, `92`, `211`, `449`, `456`; 5 empty |
| `dangerous_requested_CUT` | Number of integrated frames on which a cut was requested while the full-arm (S3) permission was False (a request may be blocked before execution). | frames | `0`, `73`, `92`, `211`, `449`, `456`; 5 empty |
| `nonblade_lt2mm_boundaries_strict` | Number of control boundaries at which some non-blade gap was below 2 mm (strict S3). | count | `0`, `389`, `391`, `399`, `415`; 5 empty |
| `nonblade_lt2mm_boundaries_landing` | Same, under S3+L (exempted landing contacts excluded). | count | `0`, `389`, `391`, `399`, `415`; 5 empty |
| `wrong_releases` | Number of attachment releases that were duplicated, out of order or mistimed (release must occur at cut frame + 1). | count | `0`; 5 empty |
| `unsafe_CUT` | Number of executed cuts for which the original physical blade gates (before or after the frame) or the identity permission did not pass. | count | `0`, `73`, `92`, `211`, `449`, `456`; 5 empty |
| `solver_peak_landing_force_n` | Peak landing contact force at solver substeps (S3+L cap 300 N). | N | always empty |
| `landing_cycles` | Number of control boundaries handled under the landing exemption. | periods | `0`; 5 empty |
| `landing_max_penetration_mm` | Maximum penetration recorded during exempted landing (cap 8 mm). | mm | always empty |
| `wall_min` | Wall-clock time of the run. | min | 0.8 to 4.9; 5 empty |
| `controller_wall_s` | Wall-clock time spent inside the controller (planning, screening, forecasting). | s | 1.633 to 57.77; 5 empty |

### C_S3_ablations_baselines_generalization/run_tables/run_table_exp1.csv

Component ablation on scene 11 (paper Table 9): 7 switches × 3 paired runs plus control runs; AB6 is evaluated by static start screening.

Rows: 24. Columns: 50.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `experiment` | Study identifier: exp1 = component ablation, exp2 = baselines on scene 11, exp3a = held-out perturbation tiers, exp3b = unseen geometries, T1/T2/T3 = BL5e test sets (scene 11 / held-out tiers / unseen geometries). |  | `exp1` |
| `case` | Unique run identifier. Prefix encodes the study (H4176/H4177 = S3 confirmation, H4178 = ablations/baselines/generalization, H4179 = fair planner BL5e) and the suffix encodes group, level and repetition. |  | 24 distinct, e.g. `H4178101_E1_CONTROL_R1` |
| `kind` | Run category: ours_full = our controller, full harvest; baseline = baseline controller; reference_only = row copied from an earlier frozen study for comparison (not re-run); ab6_static = AB6 ablation evaluated by static start screening only (no physics). |  | `ours_full`, `ab6_static` |
| `group` | Experimental arm. See README §5 (group codes) for the meaning of every code in this file. |  | 8 distinct, e.g. `E1_CONTROL` |
| `method` | Controller under test. OURS = frozen modular S3 controller; BL1–BL5 = baselines (paper Table 3); BL5E_V1 / BL5E2 = fair sampling-planner baseline BL5e, version 1 (voided after Amendment 01) and version 2 (reported). In A_*/geometry_adaptive_ik: fixed = fixed target library, adaptive = online damped-least-squares IK. |  | `OURS` |
| `switch_off` | Ablation switch disabled in this run (AB1 landing admission, AB2 stalk cached brake, AB3 E3g entry press, AB4 zero-force manifold admission, AB5 temporal interlock, AB6 screened initialization, AB7 live/cold barrier). Empty = no switch disabled. |  | 7 distinct, e.g. `AB1_landing`; 3 empty |
| `level` | Perturbation tier or scene. NOMINAL = registered start on scene 11; TRANSLATION_{X,Y,Z}_{NEG,POS} = robot base offset of ∓/±0.01 m; YAW_{NEG,POS} = base yaw ∓/±2°; JOINT_k_{NEG,POS} = joint k start offset ∓/±0.01 rad; CONTACT_DROP3_FORCE08 = contact-sensor degradation (contact reading dropped every 3rd frame, reported force scaled ×0.8); h4178_unseen_783xx = one of five unseen procedurally generated geometries. |  | `NOMINAL` |
| `seed` | Random seed. In S3 studies this is the process seed passed to the simulator; in S1/S2 studies it is the evaluation (scene) seed. |  | `78101`, `78102`, `78103`; 3 empty |
| `rep` | Repetition index within a group × level cell. |  | `1`, `2`, `3` |
| `label` | Evidential status of the study. Always 'exploratory' (preregistered but not confirmatory). Translated from the original Chinese value '探索性'. |  | `exploratory` |
| `status` | Run status from the queue: finished / PASSED / FAILED = executed; NOT_STARTED = registered but not launched (counted in the denominator); stopped_at_screening = refused by the start screen before physics; static_check = evaluated by static geometry only; reference_only = copied from an earlier study; INTERRUPTED_INFRASTRUCTURE = interrupted by instance migration (counted as failure); running = still running when the table was frozen (development table only). |  | `finished`, `static_check` |
| `attempted` | In per-run tables: True if the unit was launched. In group-outcome tables: number of units launched. | bool / count | `True` |
| `returncode` | Exit code of the simulator process (0 = normal exit; negative = terminated by signal, e.g. −15 SIGTERM, −11 SIGSEGV). |  | `0`; 3 empty |
| `wall_min` | Wall-clock time of the run. | min | 71.5 to 111.9; 3 empty |
| `frames` | Number of integrated control frames in the run (one frame = 1/30 s simulated; a full harvest takes about 600 frames = 20 s). | frame | 357 to 600; 3 empty |
| `strict_success` | Full harvest success under the strict S3 predicate (no landing exemption). | bool | `False`; 3 empty |
| `landing_success` | In per-run tables: full harvest success under S3+L (landing exemption 300 N / 25 periods / 8 mm). In group summaries: number of such successes. | bool / count | `True`, `False`; 3 empty |
| `strict_safety` | No safety failure under strict S3. | bool | `False`, `True`; 3 empty |
| `landing_safety` | No safety failure under S3+L. | bool | `True`; 3 empty |
| `strict_safety_failures` | Number of safety-failure records under strict S3 (one record per failing gate event). | count | `71`, `0`, `68`; 3 empty |
| `landing_safety_failures` | Number of safety-failure records under S3+L. | count | `0`; 3 empty |
| `h4176_judge_passed` | Verdict of the Confirmation I (H4176) acceptance judge, re-applied to OURS runs as a cross-check. Empty for baselines. | bool | `True`, `False`; 3 empty |
| `h4176_judge_safety` | Safety verdict of the H4176 acceptance judge (OURS only). | bool | `True`; 3 empty |
| `furthest_stage` | Last milestone reached in the ordered chain P2 cut → P2 release → P2 exit → P0 cut → P0 release → P0 exit → stalk cut → stalk release → stalk exit (written petiole2_CUT … stalk1_exit). none = no milestone; screening = refused at start screening. |  | `stalk1_exit`, `petiole0_exit`, `petiole0_release`; 3 empty |
| `milestones` | Space-separated list of all milestones reached, in order. |  | 3 distinct, e.g. `petiole2_CUT petiole2_release petiole…`; 3 empty |
| `cut_steps` | Executed cuts as object@frame (e.g. petiole2@28 petiole0@355 stalk1@587). | frame | `petiole2@28 petiole0@356`, `petiole2@28 petiole0@355 stalk1@587`, `petiole2@28 petiole0@355`, `petiole2@28 petiole0@355 stalk1@585`, `petiole2@28 petiole0@356 stalk1@588`; 3 empty |
| `release_steps` | Frame at which each cut object's attachment was released: object@frame in folder B, JSON {object: frame} in folders C and D. | frame | 5 distinct, e.g. `{"('petiole', 2)": 29, "('petiole', 0…`; 3 empty |
| `physical_exit_steps` | JSON {object: frame} at which the arm had sustained physical exit from each released object. | frame | 6 distinct, e.g. `{"('petiole', 2)": 32, "('petiole', 0…`; 3 empty |
| `dangerous_executed_CUT` | Number of integrated frames on which a cut was executed while the full-arm (S3) permission evaluated at that frame was False. | frames | `0`; 3 empty |
| `dangerous_requested_CUT` | Number of integrated frames on which a cut was requested while the full-arm (S3) permission was False (a request may be blocked before execution). | frames | `0`; 3 empty |
| `temporal_decision_unavailable_frames` | Number of frames for which no full-arm permission decision was available. | frames | `0`; 3 empty |
| `nonblade_lt2mm_boundaries_strict` | Number of control boundaries at which some non-blade gap was below 2 mm (strict S3). | count | `8`, `0`, `7`; 3 empty |
| `nonblade_lt2mm_boundaries_landing` | Same, under S3+L (exempted landing contacts excluded). | count | `0`; 3 empty |
| `nonblade_min_gap_mm_strict` | Minimum non-blade gap under strict S3 (negative = interpenetration). | mm | -6.294 to 2.951; 3 empty |
| `nonblade_min_gap_mm_landing` | Minimum non-blade gap under S3+L, excluding contacts covered by the landing exemption. | mm | 2.94 to 2.965; 3 empty |
| `wrong_releases` | Number of attachment releases that were duplicated, out of order or mistimed (release must occur at cut frame + 1). | count | `0`; 3 empty |
| `unsafe_CUT` | Number of executed cuts for which the original physical blade gates (before or after the frame) or the identity permission did not pass. | count | `0`; 3 empty |
| `solver_peak_landing_force_n` | Peak landing contact force at solver substeps (S3+L cap 300 N). | N | 260.7 to 283.3; 6 empty |
| `landing_cycles` | Number of control boundaries handled under the landing exemption. | periods | `10`, `0`, `8`; 3 empty |
| `landing_max_penetration_mm` | Maximum penetration recorded during exempted landing (cap 8 mm). | mm | 6.229 to 6.294; 6 empty |
| `controller_wall_s` | Wall-clock time spent inside the controller (planning, screening, forecasting). | s | always empty |
| `stop_reason` | Why the controller stopped. Examples: h4178_uniform_no_release_within_480_frames:(object) = baseline-only administrative stop when no new release occurs within 480 frames; bl5_no_collision_free_plan / bl5e_no_collision_free_plan = planner found no plan within budget; first_handoff_mechanism_complete = handoff role finished; finite_*_budget_exhausted = a bounded retry budget of our controller ran out; *_refused / invalid_* = our controller refused to continue because a frozen route or forecast was not valid for the current state; 'our frozen pipeline refused the unseen geometry before physics' = start refused. |  | 6 distinct, e.g. `global_P0_bounded_firstfree_all_Origi…`; 14 empty |
| `stop_state` | Controller state machine state at the stop (approach_route, approach_cut, exit, await_task_completion). |  | `await_task_completion`, `approach_cut`, `exit`, `approach_route`; 3 empty |
| `termination` | JSON termination record of the environment (success, or motion_management_stop). | JSON | `{"success": true}`, `{"motion_management_stop": true}`; 3 empty |
| `first_strict_failure` | First safety-failure record under strict S3: JSON {frame, gate, object_id, …}. Gate codes: nonBlade_below_2mm_strict = a non-blade part closer than 2 mm to the plant; CUT_without_original_physical_gates_or_identity = a cut executed although the physical blade gates or the identity check did not pass; Blade_near_pair_outside_current_cut_or_nonworsening_scope = blade near a shape pair it is not allowed to approach; solver_landing_single_shape_force_above_300N = landing force above the cap. null = no failure. | JSON | 19 distinct, e.g. `{"frame": 359, "gate": "nonBlade_belo…`; 3 empty |
| `first_landing_failure` | First safety-failure record under S3+L (same format and gate codes as first_strict_failure). | JSON | `null`; 3 empty |
| `initial_all144_min_gap_mm` | Minimum gap over all 144 arm–plant shape pairs at the start configuration (negative = start already interpenetrates). | mm | `-99.078`; 21 empty |
| `pairs_below_2mm` | Number of the 144 arm–plant shape pairs with gap below 2 mm at the start configuration. | count | `3`; 21 empty |
| `would_start` | Whether the controller would start from this configuration after static screening (AB6 rows). | bool | `False`; 21 empty |
| `note` | Free-text note. |  | `static geometry only (no physics)`; 21 empty |

### C_S3_ablations_baselines_generalization/run_tables/run_table_exp2.csv

Baselines BL1–BL5 on scene 11, 3 runs each, plus OURS reference rows (paper Table 10).

Rows: 18. Columns: 47.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `experiment` | Study identifier: exp1 = component ablation, exp2 = baselines on scene 11, exp3a = held-out perturbation tiers, exp3b = unseen geometries, T1/T2/T3 = BL5e test sets (scene 11 / held-out tiers / unseen geometries). |  | `exp2` |
| `case` | Unique run identifier. Prefix encodes the study (H4176/H4177 = S3 confirmation, H4178 = ablations/baselines/generalization, H4179 = fair planner BL5e) and the suffix encodes group, level and repetition. |  | 18 distinct, e.g. `H4178101_E1_CONTROL_R1` |
| `kind` | Run category: ours_full = our controller, full harvest; baseline = baseline controller; reference_only = row copied from an earlier frozen study for comparison (not re-run); ab6_static = AB6 ablation evaluated by static start screening only (no physics). |  | `baseline`, `reference_only` |
| `group` | Experimental arm. See README §5 (group codes) for the meaning of every code in this file. |  | `E2_OURS`, `E2_BL1`, `E2_BL2`, `E2_BL3`, `E2_BL4`, `E2_BL5` |
| `method` | Controller under test. OURS = frozen modular S3 controller; BL1–BL5 = baselines (paper Table 3); BL5E_V1 / BL5E2 = fair sampling-planner baseline BL5e, version 1 (voided after Amendment 01) and version 2 (reported). In A_*/geometry_adaptive_ik: fixed = fixed target library, adaptive = online damped-least-squares IK. |  | `OURS`, `BL1`, `BL2`, `BL3`, `BL4`, `BL5` |
| `switch_off` | Ablation switch disabled in this run (AB1 landing admission, AB2 stalk cached brake, AB3 E3g entry press, AB4 zero-force manifold admission, AB5 temporal interlock, AB6 screened initialization, AB7 live/cold barrier). Empty = no switch disabled. |  | always empty |
| `level` | Perturbation tier or scene. NOMINAL = registered start on scene 11; TRANSLATION_{X,Y,Z}_{NEG,POS} = robot base offset of ∓/±0.01 m; YAW_{NEG,POS} = base yaw ∓/±2°; JOINT_k_{NEG,POS} = joint k start offset ∓/±0.01 rad; CONTACT_DROP3_FORCE08 = contact-sensor degradation (contact reading dropped every 3rd frame, reported force scaled ×0.8); h4178_unseen_783xx = one of five unseen procedurally generated geometries. |  | `NOMINAL` |
| `seed` | Random seed. In S3 studies this is the process seed passed to the simulator; in S1/S2 studies it is the evaluation (scene) seed. |  | `78101`, `78102`, `78103` |
| `rep` | Repetition index within a group × level cell. |  | `1`, `2`, `3` |
| `label` | Evidential status of the study. Always 'exploratory' (preregistered but not confirmatory). Translated from the original Chinese value '探索性'. |  | `exploratory` |
| `status` | Run status from the queue: finished / PASSED / FAILED = executed; NOT_STARTED = registered but not launched (counted in the denominator); stopped_at_screening = refused by the start screen before physics; static_check = evaluated by static geometry only; reference_only = copied from an earlier study; INTERRUPTED_INFRASTRUCTURE = interrupted by instance migration (counted as failure); running = still running when the table was frozen (development table only). |  | `finished`, `reference_only` |
| `attempted` | In per-run tables: True if the unit was launched. In group-outcome tables: number of units launched. | bool / count | `True`; 3 empty |
| `note` | Free-text note. |  | 1 distinct, e.g. `our-method arm of exp2 = the exp1 CON…`; 15 empty |
| `returncode` | Exit code of the simulator process (0 = normal exit; negative = terminated by signal, e.g. −15 SIGTERM, −11 SIGSEGV). |  | `0`; 3 empty |
| `wall_min` | Wall-clock time of the run. | min | 1 to 4.6; 3 empty |
| `frames` | Number of integrated control frames in the run (one frame = 1/30 s simulated; a full harvest takes about 600 frames = 20 s). | frame | `482`, `59`; 3 empty |
| `strict_success` | Full harvest success under the strict S3 predicate (no landing exemption). | bool | `False`; 3 empty |
| `landing_success` | In per-run tables: full harvest success under S3+L (landing exemption 300 N / 25 periods / 8 mm). In group summaries: number of such successes. | bool / count | `False`; 3 empty |
| `strict_safety` | No safety failure under strict S3. | bool | `True`, `False`; 3 empty |
| `landing_safety` | No safety failure under S3+L. | bool | `True`, `False`; 3 empty |
| `strict_safety_failures` | Number of safety-failure records under strict S3 (one record per failing gate event). | count | `0`, `14132`; 3 empty |
| `landing_safety_failures` | Number of safety-failure records under S3+L. | count | `0`, `14132`; 3 empty |
| `h4176_judge_passed` | Verdict of the Confirmation I (H4176) acceptance judge, re-applied to OURS runs as a cross-check. Empty for baselines. | bool | always empty |
| `h4176_judge_safety` | Safety verdict of the H4176 acceptance judge (OURS only). | bool | always empty |
| `furthest_stage` | Last milestone reached in the ordered chain P2 cut → P2 release → P2 exit → P0 cut → P0 release → P0 exit → stalk cut → stalk release → stalk exit (written petiole2_CUT … stalk1_exit). none = no milestone; screening = refused at start screening. |  | `none`, `petiole2_CUT`, `petiole2_exit`; 3 empty |
| `milestones` | Space-separated list of all milestones reached, in order. |  | 2 distinct, e.g. `petiole2_CUT`; 12 empty |
| `cut_steps` | Executed cuts as object@frame (e.g. petiole2@28 petiole0@355 stalk1@587). | frame | `none@0 petiole2@1-481(n=426)`, `petiole2@24`; 12 empty |
| `release_steps` | Frame at which each cut object's attachment was released: object@frame in folder B, JSON {object: frame} in folders C and D. | frame | `{}`, `{"('petiole', 2)": 25}`; 3 empty |
| `physical_exit_steps` | JSON {object: frame} at which the arm had sustained physical exit from each released object. | frame | `{}`, `{"('petiole', 2)": 28}`; 3 empty |
| `dangerous_executed_CUT` | Number of integrated frames on which a cut was executed while the full-arm (S3) permission evaluated at that frame was False. | frames | `0`, `427`; 3 empty |
| `dangerous_requested_CUT` | Number of integrated frames on which a cut was requested while the full-arm (S3) permission was False (a request may be blocked before execution). | frames | `0`, `427`; 3 empty |
| `temporal_decision_unavailable_frames` | Number of frames for which no full-arm permission decision was available. | frames | `0`; 3 empty |
| `nonblade_lt2mm_boundaries_strict` | Number of control boundaries at which some non-blade gap was below 2 mm (strict S3). | count | `0`, `394`; 3 empty |
| `nonblade_lt2mm_boundaries_landing` | Same, under S3+L (exempted landing contacts excluded). | count | `0`, `394`; 3 empty |
| `nonblade_min_gap_mm_strict` | Minimum non-blade gap under strict S3 (negative = interpenetration). | mm | `10.204`, `-59.877`, `-59.873`, `-59.872`; 3 empty |
| `nonblade_min_gap_mm_landing` | Minimum non-blade gap under S3+L, excluding contacts covered by the landing exemption. | mm | `10.204`, `-59.877`, `-59.873`, `-59.872`; 3 empty |
| `wrong_releases` | Number of attachment releases that were duplicated, out of order or mistimed (release must occur at cut frame + 1). | count | `0`; 3 empty |
| `unsafe_CUT` | Number of executed cuts for which the original physical blade gates (before or after the frame) or the identity permission did not pass. | count | `0`, `427`; 3 empty |
| `solver_peak_landing_force_n` | Peak landing contact force at solver substeps (S3+L cap 300 N). | N | always empty |
| `landing_cycles` | Number of control boundaries handled under the landing exemption. | periods | `0`; 3 empty |
| `landing_max_penetration_mm` | Maximum penetration recorded during exempted landing (cap 8 mm). | mm | always empty |
| `controller_wall_s` | Wall-clock time spent inside the controller (planning, screening, forecasting). | s | 1.564 to 46.65; 3 empty |
| `stop_reason` | Why the controller stopped. Examples: h4178_uniform_no_release_within_480_frames:(object) = baseline-only administrative stop when no new release occurs within 480 frames; bl5_no_collision_free_plan / bl5e_no_collision_free_plan = planner found no plan within budget; first_handoff_mechanism_complete = handoff role finished; finite_*_budget_exhausted = a bounded retry budget of our controller ran out; *_refused / invalid_* = our controller refused to continue because a frozen route or forecast was not valid for the current state; 'our frozen pipeline refused the unseen geometry before physics' = start refused. |  | 2 distinct, e.g. `h4178_uniform_no_release_within_480_f…`; 3 empty |
| `stop_state` | Controller state machine state at the stop (approach_route, approach_cut, exit, await_task_completion). |  | always empty |
| `termination` | JSON termination record of the environment (success, or motion_management_stop). | JSON | `{"motion_management_stop": true}`; 3 empty |
| `first_strict_failure` | First safety-failure record under strict S3: JSON {frame, gate, object_id, …}. Gate codes: nonBlade_below_2mm_strict = a non-blade part closer than 2 mm to the plant; CUT_without_original_physical_gates_or_identity = a cut executed although the physical blade gates or the identity check did not pass; Blade_near_pair_outside_current_cut_or_nonworsening_scope = blade near a shape pair it is not allowed to approach; solver_landing_single_shape_force_above_300N = landing force above the cap. null = no failure. | JSON | 2 distinct, e.g. `{"frame": 0, "gate": "CUT_without_ori…`; 3 empty |
| `first_landing_failure` | First safety-failure record under S3+L (same format and gate codes as first_strict_failure). | JSON | 2 distinct, e.g. `{"frame": 0, "gate": "CUT_without_ori…`; 3 empty |

### C_S3_ablations_baselines_generalization/run_tables/run_table_exp3a.csv

Generalization to the 10 held-out perturbation tiers in the primary denominator: BL1–BL5 × tiers, plus OURS reference rows copied from Stage B (paper Fig. 9, middle).

Rows: 60. Columns: 47.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `experiment` | Study identifier: exp1 = component ablation, exp2 = baselines on scene 11, exp3a = held-out perturbation tiers, exp3b = unseen geometries, T1/T2/T3 = BL5e test sets (scene 11 / held-out tiers / unseen geometries). |  | `exp3a` |
| `case` | Unique run identifier. Prefix encodes the study (H4176/H4177 = S3 confirmation, H4178 = ablations/baselines/generalization, H4179 = fair planner BL5e) and the suffix encodes group, level and repetition. |  | 60 distinct, e.g. `H4178301_E3A_OURS_JOINT_0_POS` |
| `kind` | Run category: ours_full = our controller, full harvest; baseline = baseline controller; reference_only = row copied from an earlier frozen study for comparison (not re-run); ab6_static = AB6 ablation evaluated by static start screening only (no physics). |  | `baseline`, `reference_only` |
| `group` | Experimental arm. See README §5 (group codes) for the meaning of every code in this file. |  | `E3A_OURS`, `E3A_BL1`, `E3A_BL2`, `E3A_BL3`, `E3A_BL4`, `E3A_BL5` |
| `method` | Controller under test. OURS = frozen modular S3 controller; BL1–BL5 = baselines (paper Table 3); BL5E_V1 / BL5E2 = fair sampling-planner baseline BL5e, version 1 (voided after Amendment 01) and version 2 (reported). In A_*/geometry_adaptive_ik: fixed = fixed target library, adaptive = online damped-least-squares IK. |  | `OURS`, `BL1`, `BL2`, `BL3`, `BL4`, `BL5` |
| `switch_off` | Ablation switch disabled in this run (AB1 landing admission, AB2 stalk cached brake, AB3 E3g entry press, AB4 zero-force manifold admission, AB5 temporal interlock, AB6 screened initialization, AB7 live/cold barrier). Empty = no switch disabled. |  | always empty |
| `level` | Perturbation tier or scene. NOMINAL = registered start on scene 11; TRANSLATION_{X,Y,Z}_{NEG,POS} = robot base offset of ∓/±0.01 m; YAW_{NEG,POS} = base yaw ∓/±2°; JOINT_k_{NEG,POS} = joint k start offset ∓/±0.01 rad; CONTACT_DROP3_FORCE08 = contact-sensor degradation (contact reading dropped every 3rd frame, reported force scaled ×0.8); h4178_unseen_783xx = one of five unseen procedurally generated geometries. |  | 10 distinct, e.g. `JOINT_0_POS` |
| `seed` | Random seed. In S3 studies this is the process seed passed to the simulator; in S1/S2 studies it is the evaluation (scene) seed. |  | `78201`; 10 empty |
| `rep` | Repetition index within a group × level cell. |  | always empty |
| `label` | Evidential status of the study. Always 'exploratory' (preregistered but not confirmatory). Translated from the original Chinese value '探索性'. |  | `exploratory` |
| `status` | Run status from the queue: finished / PASSED / FAILED = executed; NOT_STARTED = registered but not launched (counted in the denominator); stopped_at_screening = refused by the start screen before physics; static_check = evaluated by static geometry only; reference_only = copied from an earlier study; INTERRUPTED_INFRASTRUCTURE = interrupted by instance migration (counted as failure); running = still running when the table was frozen (development table only). |  | `finished`, `reference_only` |
| `attempted` | In per-run tables: True if the unit was launched. In group-outcome tables: number of units launched. | bool / count | `True`; 10 empty |
| `note` | Free-text note. |  | 2 distinct, e.g. `stage-B screening conclusion reused, …`; 50 empty |
| `returncode` | Exit code of the simulator process (0 = normal exit; negative = terminated by signal, e.g. −15 SIGTERM, −11 SIGSEGV). |  | `0`; 10 empty |
| `wall_min` | Wall-clock time of the run. | min | 0.9 to 5; 10 empty |
| `frames` | Number of integrated control frames in the run (one frame = 1/30 s simulated; a full harvest takes about 600 frames = 20 s). | frame | `482`, `59`, `60`, `61`, `57`; 10 empty |
| `strict_success` | Full harvest success under the strict S3 predicate (no landing exemption). | bool | `False`; 10 empty |
| `landing_success` | In per-run tables: full harvest success under S3+L (landing exemption 300 N / 25 periods / 8 mm). In group summaries: number of such successes. | bool / count | `False`; 10 empty |
| `strict_safety` | No safety failure under strict S3. | bool | `True`, `False`; 10 empty |
| `landing_safety` | No safety failure under S3+L. | bool | `True`, `False`; 10 empty |
| `strict_safety_failures` | Number of safety-failure records under strict S3 (one record per failing gate event). | count | 0 to 14194; 10 empty |
| `landing_safety_failures` | Number of safety-failure records under S3+L. | count | 0 to 14194; 10 empty |
| `h4176_judge_passed` | Verdict of the Confirmation I (H4176) acceptance judge, re-applied to OURS runs as a cross-check. Empty for baselines. | bool | always empty |
| `h4176_judge_safety` | Safety verdict of the H4176 acceptance judge (OURS only). | bool | always empty |
| `furthest_stage` | Last milestone reached in the ordered chain P2 cut → P2 release → P2 exit → P0 cut → P0 release → P0 exit → stalk cut → stalk release → stalk exit (written petiole2_CUT … stalk1_exit). none = no milestone; screening = refused at start screening. |  | `none`, `petiole2_CUT`, `petiole2_exit`; 10 empty |
| `milestones` | Space-separated list of all milestones reached, in order. |  | 2 distinct, e.g. `petiole2_CUT`; 40 empty |
| `cut_steps` | Executed cuts as object@frame (e.g. petiole2@28 petiole0@355 stalk1@587). | frame | 12 distinct, e.g. `none@0 petiole2@1-481(n=426)`; 40 empty |
| `release_steps` | Frame at which each cut object's attachment was released: object@frame in folder B, JSON {object: frame} in folders C and D. | frame | `{}`, `{"('petiole', 2)": 25}`, `{"('petiole', 2)": 26}`, `{"('petiole', 2)": 27}`, `{"('petiole', 2)": 23}`; 10 empty |
| `physical_exit_steps` | JSON {object: frame} at which the arm had sustained physical exit from each released object. | frame | `{}`, `{"('petiole', 2)": 28}`, `{"('petiole', 2)": 29}`, `{"('petiole', 2)": 30}`, `{"('petiole', 2)": 26}`; 10 empty |
| `dangerous_executed_CUT` | Number of integrated frames on which a cut was executed while the full-arm (S3) permission evaluated at that frame was False. | frames | 0 to 482; 10 empty |
| `dangerous_requested_CUT` | Number of integrated frames on which a cut was requested while the full-arm (S3) permission was False (a request may be blocked before execution). | frames | 0 to 482; 10 empty |
| `temporal_decision_unavailable_frames` | Number of frames for which no full-arm permission decision was available. | frames | `0`; 10 empty |
| `nonblade_lt2mm_boundaries_strict` | Number of control boundaries at which some non-blade gap was below 2 mm (strict S3). | count | `0`, `394`, `395`, `396`, `393`, `374`; 10 empty |
| `nonblade_lt2mm_boundaries_landing` | Same, under S3+L (exempted landing contacts excluded). | count | `0`, `394`, `395`, `396`, `393`, `374`; 10 empty |
| `nonblade_min_gap_mm_strict` | Minimum non-blade gap under strict S3 (negative = interpenetration). | mm | -67.59 to 51.95; 10 empty |
| `nonblade_min_gap_mm_landing` | Minimum non-blade gap under S3+L, excluding contacts covered by the landing exemption. | mm | -67.59 to 51.95; 10 empty |
| `wrong_releases` | Number of attachment releases that were duplicated, out of order or mistimed (release must occur at cut frame + 1). | count | `0`; 10 empty |
| `unsafe_CUT` | Number of executed cuts for which the original physical blade gates (before or after the frame) or the identity permission did not pass. | count | 0 to 482; 10 empty |
| `solver_peak_landing_force_n` | Peak landing contact force at solver substeps (S3+L cap 300 N). | N | always empty |
| `landing_cycles` | Number of control boundaries handled under the landing exemption. | periods | `0`; 10 empty |
| `landing_max_penetration_mm` | Maximum penetration recorded during exempted landing (cap 8 mm). | mm | always empty |
| `controller_wall_s` | Wall-clock time spent inside the controller (planning, screening, forecasting). | s | 1.63 to 76.43; 10 empty |
| `stop_reason` | Why the controller stopped. Examples: h4178_uniform_no_release_within_480_frames:(object) = baseline-only administrative stop when no new release occurs within 480 frames; bl5_no_collision_free_plan / bl5e_no_collision_free_plan = planner found no plan within budget; first_handoff_mechanism_complete = handoff role finished; finite_*_budget_exhausted = a bounded retry budget of our controller ran out; *_refused / invalid_* = our controller refused to continue because a frozen route or forecast was not valid for the current state; 'our frozen pipeline refused the unseen geometry before physics' = start refused. |  | 2 distinct, e.g. `h4178_uniform_no_release_within_480_f…`; 10 empty |
| `stop_state` | Controller state machine state at the stop (approach_route, approach_cut, exit, await_task_completion). |  | always empty |
| `termination` | JSON termination record of the environment (success, or motion_management_stop). | JSON | `{"motion_management_stop": true}`; 10 empty |
| `first_strict_failure` | First safety-failure record under strict S3: JSON {frame, gate, object_id, …}. Gate codes: nonBlade_below_2mm_strict = a non-blade part closer than 2 mm to the plant; CUT_without_original_physical_gates_or_identity = a cut executed although the physical blade gates or the identity check did not pass; Blade_near_pair_outside_current_cut_or_nonworsening_scope = blade near a shape pair it is not allowed to approach; solver_landing_single_shape_force_above_300N = landing force above the cap. null = no failure. | JSON | 2 distinct, e.g. `{"frame": 0, "gate": "CUT_without_ori…`; 10 empty |
| `first_landing_failure` | First safety-failure record under S3+L (same format and gate codes as first_strict_failure). | JSON | 2 distinct, e.g. `{"frame": 0, "gate": "CUT_without_ori…`; 10 empty |

### C_S3_ablations_baselines_generalization/run_tables/run_table_exp3b.csv

Generalization to five unseen geometries: OURS (refused before physics) and BL1–BL5 (paper Fig. 9, bottom).

Rows: 30. Columns: 46.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `experiment` | Study identifier: exp1 = component ablation, exp2 = baselines on scene 11, exp3a = held-out perturbation tiers, exp3b = unseen geometries, T1/T2/T3 = BL5e test sets (scene 11 / held-out tiers / unseen geometries). |  | `exp3b` |
| `case` | Unique run identifier. Prefix encodes the study (H4176/H4177 = S3 confirmation, H4178 = ablations/baselines/generalization, H4179 = fair planner BL5e) and the suffix encodes group, level and repetition. |  | 30 distinct, e.g. `H4178401_E3B_OURS_h4178_unseen_78301` |
| `kind` | Run category: ours_full = our controller, full harvest; baseline = baseline controller; reference_only = row copied from an earlier frozen study for comparison (not re-run); ab6_static = AB6 ablation evaluated by static start screening only (no physics). |  | `baseline`, `ours_full` |
| `group` | Experimental arm. See README §5 (group codes) for the meaning of every code in this file. |  | `E3B_OURS`, `E3B_BL1`, `E3B_BL2`, `E3B_BL3`, `E3B_BL4`, `E3B_BL5` |
| `method` | Controller under test. OURS = frozen modular S3 controller; BL1–BL5 = baselines (paper Table 3); BL5E_V1 / BL5E2 = fair sampling-planner baseline BL5e, version 1 (voided after Amendment 01) and version 2 (reported). In A_*/geometry_adaptive_ik: fixed = fixed target library, adaptive = online damped-least-squares IK. |  | `OURS`, `BL1`, `BL2`, `BL3`, `BL4`, `BL5` |
| `switch_off` | Ablation switch disabled in this run (AB1 landing admission, AB2 stalk cached brake, AB3 E3g entry press, AB4 zero-force manifold admission, AB5 temporal interlock, AB6 screened initialization, AB7 live/cold barrier). Empty = no switch disabled. |  | always empty |
| `level` | Perturbation tier or scene. NOMINAL = registered start on scene 11; TRANSLATION_{X,Y,Z}_{NEG,POS} = robot base offset of ∓/±0.01 m; YAW_{NEG,POS} = base yaw ∓/±2°; JOINT_k_{NEG,POS} = joint k start offset ∓/±0.01 rad; CONTACT_DROP3_FORCE08 = contact-sensor degradation (contact reading dropped every 3rd frame, reported force scaled ×0.8); h4178_unseen_783xx = one of five unseen procedurally generated geometries. |  | `h4178_unseen_78301`, `h4178_unseen_78302`, `h4178_unseen_78303`, `h4178_unseen_78304`, `h4178_unseen_78305` |
| `seed` | Random seed. In S3 studies this is the process seed passed to the simulator; in S1/S2 studies it is the evaluation (scene) seed. |  | `78301`, `78302`, `78303`, `78304`, `78305` |
| `rep` | Repetition index within a group × level cell. |  | always empty |
| `label` | Evidential status of the study. Always 'exploratory' (preregistered but not confirmatory). Translated from the original Chinese value '探索性'. |  | `exploratory` |
| `status` | Run status from the queue: finished / PASSED / FAILED = executed; NOT_STARTED = registered but not launched (counted in the denominator); stopped_at_screening = refused by the start screen before physics; static_check = evaluated by static geometry only; reference_only = copied from an earlier study; INTERRUPTED_INFRASTRUCTURE = interrupted by instance migration (counted as failure); running = still running when the table was frozen (development table only). |  | `finished`, `stopped_at_screening` |
| `attempted` | In per-run tables: True if the unit was launched. In group-outcome tables: number of units launched. | bool / count | `True` |
| `strict_success` | Full harvest success under the strict S3 predicate (no landing exemption). | bool | `False` |
| `landing_success` | In per-run tables: full harvest success under S3+L (landing exemption 300 N / 25 periods / 8 mm). In group summaries: number of such successes. | bool / count | `False` |
| `furthest_stage` | Last milestone reached in the ordered chain P2 cut → P2 release → P2 exit → P0 cut → P0 release → P0 exit → stalk cut → stalk release → stalk exit (written petiole2_CUT … stalk1_exit). none = no milestone; screening = refused at start screening. |  | `none`, `screening`, `petiole2_CUT`, `petiole2_exit` |
| `stop_reason` | Why the controller stopped. Examples: h4178_uniform_no_release_within_480_frames:(object) = baseline-only administrative stop when no new release occurs within 480 frames; bl5_no_collision_free_plan / bl5e_no_collision_free_plan = planner found no plan within budget; first_handoff_mechanism_complete = handoff role finished; finite_*_budget_exhausted = a bounded retry budget of our controller ran out; *_refused / invalid_* = our controller refused to continue because a frozen route or forecast was not valid for the current state; 'our frozen pipeline refused the unseen geometry before physics' = start refused. |  | 3 distinct, e.g. `our frozen pipeline refused the unsee…` |
| `returncode` | Exit code of the simulator process (0 = normal exit; negative = terminated by signal, e.g. −15 SIGTERM, −11 SIGSEGV). |  | `0`; 5 empty |
| `wall_min` | Wall-clock time of the run. | min | 0.8 to 4.9; 5 empty |
| `frames` | Number of integrated control frames in the run (one frame = 1/30 s simulated; a full harvest takes about 600 frames = 20 s). | frame | `482`, `64`, `76`, `67`, `35`, `60`; 5 empty |
| `strict_safety` | No safety failure under strict S3. | bool | `True`, `False`; 5 empty |
| `landing_safety` | No safety failure under S3+L. | bool | `True`, `False`; 5 empty |
| `strict_safety_failures` | Number of safety-failure records under strict S3 (one record per failing gate event). | count | `0`, `13896`, `14176`, `13793`, `7881`, `14237`; 5 empty |
| `landing_safety_failures` | Number of safety-failure records under S3+L. | count | `0`, `13896`, `14176`, `13793`, `7881`, `14237`; 5 empty |
| `h4176_judge_passed` | Verdict of the Confirmation I (H4176) acceptance judge, re-applied to OURS runs as a cross-check. Empty for baselines. | bool | always empty |
| `h4176_judge_safety` | Safety verdict of the H4176 acceptance judge (OURS only). | bool | always empty |
| `milestones` | Space-separated list of all milestones reached, in order. |  | 2 distinct, e.g. `petiole2_CUT`; 21 empty |
| `cut_steps` | Executed cuts as object@frame (e.g. petiole2@28 petiole0@355 stalk1@587). | frame | 9 distinct, e.g. `none@0 petiole2@1-72(n=72)`; 21 empty |
| `release_steps` | Frame at which each cut object's attachment was released: object@frame in folder B, JSON {object: frame} in folders C and D. | frame | `{}`, `{"('petiole', 2)": 30}`, `{"('petiole', 2)": 42}`, `{"('petiole', 2)": 33}`, `{"('petiole', 2)": 26}`; 5 empty |
| `physical_exit_steps` | JSON {object: frame} at which the arm had sustained physical exit from each released object. | frame | `{}`, `{"('petiole', 2)": 33}`, `{"('petiole', 2)": 45}`, `{"('petiole', 2)": 36}`, `{"('petiole', 2)": 29}`; 5 empty |
| `dangerous_executed_CUT` | Number of integrated frames on which a cut was executed while the full-arm (S3) permission evaluated at that frame was False. | frames | `0`, `73`, `92`, `211`, `449`, `456`; 5 empty |
| `dangerous_requested_CUT` | Number of integrated frames on which a cut was requested while the full-arm (S3) permission was False (a request may be blocked before execution). | frames | `0`, `73`, `92`, `211`, `449`, `456`; 5 empty |
| `temporal_decision_unavailable_frames` | Number of frames for which no full-arm permission decision was available. | frames | `0`; 5 empty |
| `nonblade_lt2mm_boundaries_strict` | Number of control boundaries at which some non-blade gap was below 2 mm (strict S3). | count | `0`, `389`, `391`, `399`, `415`; 5 empty |
| `nonblade_lt2mm_boundaries_landing` | Same, under S3+L (exempted landing contacts excluded). | count | `0`, `389`, `391`, `399`, `415`; 5 empty |
| `nonblade_min_gap_mm_strict` | Minimum non-blade gap under strict S3 (negative = interpenetration). | mm | -140.8 to 177; 5 empty |
| `nonblade_min_gap_mm_landing` | Minimum non-blade gap under S3+L, excluding contacts covered by the landing exemption. | mm | -140.8 to 177; 5 empty |
| `wrong_releases` | Number of attachment releases that were duplicated, out of order or mistimed (release must occur at cut frame + 1). | count | `0`; 5 empty |
| `unsafe_CUT` | Number of executed cuts for which the original physical blade gates (before or after the frame) or the identity permission did not pass. | count | `0`, `73`, `92`, `211`, `449`, `456`; 5 empty |
| `solver_peak_landing_force_n` | Peak landing contact force at solver substeps (S3+L cap 300 N). | N | always empty |
| `landing_cycles` | Number of control boundaries handled under the landing exemption. | periods | `0`; 5 empty |
| `landing_max_penetration_mm` | Maximum penetration recorded during exempted landing (cap 8 mm). | mm | always empty |
| `controller_wall_s` | Wall-clock time spent inside the controller (planning, screening, forecasting). | s | 1.633 to 57.77; 5 empty |
| `stop_state` | Controller state machine state at the stop (approach_route, approach_cut, exit, await_task_completion). |  | always empty |
| `termination` | JSON termination record of the environment (success, or motion_management_stop). | JSON | `{"motion_management_stop": true}`; 5 empty |
| `first_strict_failure` | First safety-failure record under strict S3: JSON {frame, gate, object_id, …}. Gate codes: nonBlade_below_2mm_strict = a non-blade part closer than 2 mm to the plant; CUT_without_original_physical_gates_or_identity = a cut executed although the physical blade gates or the identity check did not pass; Blade_near_pair_outside_current_cut_or_nonworsening_scope = blade near a shape pair it is not allowed to approach; solver_landing_single_shape_force_above_300N = landing force above the cap. null = no failure. | JSON | 3 distinct, e.g. `{"frame": 0, "gate": "CUT_without_ori…`; 5 empty |
| `first_landing_failure` | First safety-failure record under S3+L (same format and gate codes as first_strict_failure). | JSON | 3 distinct, e.g. `{"frame": 0, "gate": "CUT_without_ori…`; 5 empty |

## D_S3_fair_planner_BL5e

### D_S3_fair_planner_BL5e/figure_data/ANALYSIS_GROUP_PROGRESS_SUMMARY.csv

Per test set × group progress summary: units reaching all three gated cuts, environment success, S3+L success, and failure classes (paper Table 11, Discussion; post hoc, descriptive).

Rows: 8. Columns: 10.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `key` | Test set and group, formatted <test set>\|<group>. |  | 8 distinct, e.g. `T1\|T1_BL5E2` |
| `n` | Number of units in the group. | count | `5`, `3`, `30`, `10`, `15` |
| `all_three_cuts_gated` | Per unit: all three cuts executed with all physical blade gates passing (regardless of later safety failures). Per group: count. | bool / count | `0`, `3`, `9` |
| `env_termination_success` | The environment reported task success (all three objects harvested), independently of the S3+L safety verdict. Per group: count. | bool / count | `0`, `3`, `9` |
| `landing_success` | In per-run tables: full harvest success under S3+L (landing exemption 300 N / 25 periods / 8 mm). In group summaries: number of such successes. | bool / count | `0`, `3` |
| `safety_failed` | Number of units with at least one S3+L safety failure. | count | `0`, `1`, `6`, `9` |
| `no_collision_free_plan_stop` | Number of units stopped because no collision-free plan was found. | count | `0`, `5`, `3` |
| `uniform_480_stop` | Number of units stopped by the uniform 480-frame no-release rule (baselines only). | count | `0`, `5`, `22`, `3` |
| `failure_class_units` | JSON count of units per failure class. | JSON | 4 distinct, e.g. `{}` |
| `three_cut_failure_patterns` | JSON count of failure-class combinations among units that completed all three gated cuts. | JSON | 4 distinct, e.g. `{}` |

### D_S3_fair_planner_BL5e/figure_data/ANALYSIS_UNIT_PROGRESS_AND_FAILURE_CAUSES.csv

Per-unit progress and failure causes across T1–T3 (post hoc, descriptive). Source of the 464–828 N landing peaks and of the 44/50 first-cut and 12/50 three-cut counts.

Rows: 76. Columns: 20.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `experiment` | Study identifier: exp1 = component ablation, exp2 = baselines on scene 11, exp3a = held-out perturbation tiers, exp3b = unseen geometries, T1/T2/T3 = BL5e test sets (scene 11 / held-out tiers / unseen geometries). |  | `T2`, `T3`, `T1` |
| `group` | Experimental arm. See README §5 (group codes) for the meaning of every code in this file. |  | 8 distinct, e.g. `T1_BL5E2` |
| `method` | Controller under test. OURS = frozen modular S3 controller; BL1–BL5 = baselines (paper Table 3); BL5E_V1 / BL5E2 = fair sampling-planner baseline BL5e, version 1 (voided after Amendment 01) and version 2 (reported). In A_*/geometry_adaptive_ik: fixed = fixed target library, adaptive = online damped-least-squares IK. |  | `BL5E2`, `BL5`, `BL5E_V1`, `OURS` |
| `case` | Unique run identifier. Prefix encodes the study (H4176/H4177 = S3 confirmation, H4178 = ablations/baselines/generalization, H4179 = fair planner BL5e) and the suffix encodes group, level and repetition. |  | 76 distinct, e.g. `H4179111_T1_BL5E2_S78101` |
| `level` | Perturbation tier or scene. NOMINAL = registered start on scene 11; TRANSLATION_{X,Y,Z}_{NEG,POS} = robot base offset of ∓/±0.01 m; YAW_{NEG,POS} = base yaw ∓/±2°; JOINT_k_{NEG,POS} = joint k start offset ∓/±0.01 rad; CONTACT_DROP3_FORCE08 = contact-sensor degradation (contact reading dropped every 3rd frame, reported force scaled ×0.8); h4178_unseen_783xx = one of five unseen procedurally generated geometries. |  | 16 distinct, e.g. `NOMINAL` |
| `seed` | Random seed. In S3 studies this is the process seed passed to the simulator; in S1/S2 studies it is the evaluation (scene) seed. |  | 78101 to 79302 |
| `furthest_stage` | Last milestone reached in the ordered chain P2 cut → P2 release → P2 exit → P0 cut → P0 release → P0 exit → stalk cut → stalk release → stalk exit (written petiole2_CUT … stalk1_exit). none = no milestone; screening = refused at start screening. |  | `petiole2_exit`, `stalk1_exit`, `none`, `stalk1_release` |
| `gated_cuts` | Cuts that passed the physical blade gates, object@frame, '\|'-separated. | frame | 26 distinct, e.g. `petiole2@28`; 7 empty |
| `all_three_cuts_gated` | Per unit: all three cuts executed with all physical blade gates passing (regardless of later safety failures). Per group: count. | bool / count | `False`, `True` |
| `env_termination_success` | The environment reported task success (all three objects harvested), independently of the S3+L safety verdict. Per group: count. | bool / count | `False`, `True` |
| `admin_stop` | Administrative stop reason, if any (same codes as `stop_reason`). |  | 3 distinct, e.g. `h4178_uniform_no_release_within_480_f…`; 15 empty |
| `landing_success` | In per-run tables: full harvest success under S3+L (landing exemption 300 N / 25 periods / 8 mm). In group summaries: number of such successes. | bool / count | `False`, `True` |
| `landing_safety_passed` | Same as `landing_safety`. | bool | `True`, `False` |
| `landing_safety_failures` | Number of safety-failure records under S3+L. | count | 0 to 454 |
| `failure_classes` | Post-hoc failure classes of the unit, '\|'-separated: blade_near_out_scope, blade_force_out_scope, landing_force_gt300N, nonblade_lt2mm, ungated_CUT. |  | 7 distinct, e.g. `blade_near_out_scope`; 60 empty |
| `nonblade_min_gap_mm` | Minimum non-blade gap over the run (negative = interpenetration). | mm | -4.03 to 148.8 |
| `solver_peak_landing_force_n` | Peak landing contact force at solver substeps (S3+L cap 300 N). | N | 96 to 828.3; 61 empty |
| `unsafe_CUT` | Number of executed cuts for which the original physical blade gates (before or after the frame) or the identity permission did not pass. | count | `0`, `1` |
| `dangerous_executed_CUT` | Number of integrated frames on which a cut was executed while the full-arm (S3) permission evaluated at that frame was False. | frames | `0` |
| `wall_min` | Wall-clock time of the run. | min | 0.8 to 103.6 |

### D_S3_fair_planner_BL5e/figure_data/T1_fig_bl5e_planning.csv

BL5e planning statistics per run, T1.

Rows: 10. Columns: 19.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `case` | Unique run identifier. Prefix encodes the study (H4176/H4177 = S3 confirmation, H4178 = ablations/baselines/generalization, H4179 = fair planner BL5e) and the suffix encodes group, level and repetition. |  | 10 distinct, e.g. `H4179111_T1_BL5E2_S78101` |
| `group` | Experimental arm. See README §5 (group codes) for the meaning of every code in this file. |  | `T1_BL5E2`, `T1_BL5E_V1` |
| `level` | Perturbation tier or scene. NOMINAL = registered start on scene 11; TRANSLATION_{X,Y,Z}_{NEG,POS} = robot base offset of ∓/±0.01 m; YAW_{NEG,POS} = base yaw ∓/±2°; JOINT_k_{NEG,POS} = joint k start offset ∓/±0.01 rad; CONTACT_DROP3_FORCE08 = contact-sensor degradation (contact reading dropped every 3rd frame, reported force scaled ×0.8); h4178_unseen_783xx = one of five unseen procedurally generated geometries. |  | `NOMINAL` |
| `seed` | Random seed. In S3 studies this is the process seed passed to the simulator; in S1/S2 studies it is the evaluation (scene) seed. |  | `78101`, `78102`, `78103`, `79101`, `79102` |
| `furthest_stage` | Last milestone reached in the ordered chain P2 cut → P2 release → P2 exit → P0 cut → P0 release → P0 exit → stalk cut → stalk release → stalk exit (written petiole2_CUT … stalk1_exit). none = no milestone; screening = refused at start screening. |  | `petiole2_exit` |
| `p2_cut_gated` | Per run: the first petiole (P2) was cut with all physical blade gates passing. Per group: number of such units. | bool / count | `True` |
| `landing_success` | In per-run tables: full harvest success under S3+L (landing exemption 300 N / 25 periods / 8 mm). In group summaries: number of such successes. | bool / count | `False` |
| `landing_safety` | No safety failure under S3+L. | bool | `True`, `False` |
| `landing_safety_failures` | Number of safety-failure records under S3+L. | count | `0`, `82` |
| `stop_reason` | Why the controller stopped. Examples: h4178_uniform_no_release_within_480_frames:(object) = baseline-only administrative stop when no new release occurs within 480 frames; bl5_no_collision_free_plan / bl5e_no_collision_free_plan = planner found no plan within budget; first_handoff_mechanism_complete = handoff role finished; finite_*_budget_exhausted = a bounded retry budget of our controller ran out; *_refused / invalid_* = our controller refused to continue because a frozen route or forecast was not valid for the current state; 'our frozen pipeline refused the unseen geometry before physics' = start refused. |  | 1 distinct, e.g. `h4178_uniform_no_release_within_480_f…` |
| `controller_stop_reason` | Stop reason reported by the BL5e controller. |  | 1 distinct, e.g. `h4178_uniform_no_release_within_480_f…` |
| `planning_calls` | Number of motion-planning calls. | count | `7`, `4`, `5`, `6`, `10`, `8` |
| `plans_accepted` | Number of plans accepted for execution. | count | `2`, `3` |
| `planning_wall_s_total` | Total wall-clock time spent planning. | s | 1287 to 3730 |
| `monitor_stops` | Number of times the execution monitor stopped a plan (clearance margin violated during execution). | count | `1`, `0` |
| `retreats` | Number of retreat manoeuvres. | count | `0`, `1` |
| `replans_by_object` | JSON {object: number of replans}. | JSON / count | 6 distinct, e.g. `{"('petiole', 2)": 1, "('petiole', 0)…` |
| `frames` | Number of integrated control frames in the run (one frame = 1/30 s simulated; a full harvest takes about 600 frames = 20 s). | frame | `511` |
| `wall_min` | Wall-clock time of the run. | min | 29.5 to 68.7 |

### D_S3_fair_planner_BL5e/figure_data/T1_fig_candidate_rejections.csv

Why sampled BL5e cut-pose candidates were rejected, summed over T1.

Rows: 7. Columns: 2.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `rejection_reason` | Reason a sampled cut-pose candidate was rejected: tip_distance_gate, alignment_dynamic_axis_blade_scope, blade_face_not_facing_approach, no_blade_contact_window, cut_pose_collision, ik_unreachable_cut; passed_unrefined = candidate passed. |  | 7 distinct, e.g. `no_blade_contact_window` |
| `count_over_all_BL5E2_planning_calls` | Number of candidates with this outcome, summed over all BL5e (v2) planning calls in the test set. | count | 10 to 6982 |

### D_S3_fair_planner_BL5e/figure_data/T1_fig_group_outcomes.csv

Per-group outcome counts and Wilson intervals, T1.

Rows: 4. Columns: 11.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `group` | Experimental arm. See README §5 (group codes) for the meaning of every code in this file. |  | `T1_BL5E2`, `T1_OURS`, `T1_BL5`, `T1_BL5E_V1` |
| `n` | Number of registered units in the cell. | count | `5`, `3` |
| `attempted` | In per-run tables: True if the unit was launched. In group-outcome tables: number of units launched. | bool / count | `5`, `3` |
| `not_started` | Number of registered units that were not started. | count | `0` |
| `landing` | Number of full harvests under S3+L. | count | `0`, `3` |
| `strict` | Number of full harvests under strict S3. | count | `0` |
| `p2_cut_gated` | Per run: the first petiole (P2) was cut with all physical blade gates passing. Per group: number of such units. | bool / count | `5`, `3` |
| `safety_fail_landing` | Number of units with at least one safety failure under S3+L. | count | `0`, `1` |
| `furthest` | JSON counts of units by furthest_stage. | JSON | `{"petiole2_exit": 5}`, `{"stalk1_exit": 3}`, `{"petiole2_exit": 3}` |
| `wilson_landing` | Wilson 95% interval of landing / n. | fraction | `[0.0, 0.434]`, `[0.439, 1.0]`, `[0.0, 0.561]` |
| `wilson_p2_cut_gated` | Wilson 95% interval of p2_cut_gated / n. | fraction | `[0.566, 1.0]`, `[0.439, 1.0]` |

### D_S3_fair_planner_BL5e/figure_data/T2_fig_bl5e_planning.csv

BL5e planning statistics per run, T2.

Rows: 30. Columns: 19.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `case` | Unique run identifier. Prefix encodes the study (H4176/H4177 = S3 confirmation, H4178 = ablations/baselines/generalization, H4179 = fair planner BL5e) and the suffix encodes group, level and repetition. |  | 30 distinct, e.g. `H4179211_T2_BL5E2_JOINT_0_POS_S78201` |
| `group` | Experimental arm. See README §5 (group codes) for the meaning of every code in this file. |  | `T2_BL5E2` |
| `level` | Perturbation tier or scene. NOMINAL = registered start on scene 11; TRANSLATION_{X,Y,Z}_{NEG,POS} = robot base offset of ∓/±0.01 m; YAW_{NEG,POS} = base yaw ∓/±2°; JOINT_k_{NEG,POS} = joint k start offset ∓/±0.01 rad; CONTACT_DROP3_FORCE08 = contact-sensor degradation (contact reading dropped every 3rd frame, reported force scaled ×0.8); h4178_unseen_783xx = one of five unseen procedurally generated geometries. |  | 10 distinct, e.g. `JOINT_0_POS` |
| `seed` | Random seed. In S3 studies this is the process seed passed to the simulator; in S1/S2 studies it is the evaluation (scene) seed. |  | `78201`, `79201`, `79202` |
| `furthest_stage` | Last milestone reached in the ordered chain P2 cut → P2 release → P2 exit → P0 cut → P0 release → P0 exit → stalk cut → stalk release → stalk exit (written petiole2_CUT … stalk1_exit). none = no milestone; screening = refused at start screening. |  | `petiole2_exit`, `stalk1_exit`, `none` |
| `p2_cut_gated` | Per run: the first petiole (P2) was cut with all physical blade gates passing. Per group: number of such units. | bool / count | `True`, `False` |
| `landing_success` | In per-run tables: full harvest success under S3+L (landing exemption 300 N / 25 periods / 8 mm). In group summaries: number of such successes. | bool / count | `False` |
| `landing_safety` | No safety failure under S3+L. | bool | `True`, `False` |
| `landing_safety_failures` | Number of safety-failure records under S3+L. | count | 0 to 454 |
| `stop_reason` | Why the controller stopped. Examples: h4178_uniform_no_release_within_480_frames:(object) = baseline-only administrative stop when no new release occurs within 480 frames; bl5_no_collision_free_plan / bl5e_no_collision_free_plan = planner found no plan within budget; first_handoff_mechanism_complete = handoff role finished; finite_*_budget_exhausted = a bounded retry budget of our controller ran out; *_refused / invalid_* = our controller refused to continue because a frozen route or forecast was not valid for the current state; 'our frozen pipeline refused the unseen geometry before physics' = start refused. |  | 2 distinct, e.g. `h4178_uniform_no_release_within_480_f…`; 3 empty |
| `controller_stop_reason` | Stop reason reported by the BL5e controller. |  | 2 distinct, e.g. `h4178_uniform_no_release_within_480_f…`; 3 empty |
| `planning_calls` | Number of motion-planning calls. | count | 2 to 12 |
| `plans_accepted` | Number of plans accepted for execution. | count | 0 to 6 |
| `planning_wall_s_total` | Total wall-clock time spent planning. | s | 594 to 4660 |
| `monitor_stops` | Number of times the execution monitor stopped a plan (clearance margin violated during execution). | count | `0`, `1`, `2` |
| `retreats` | Number of retreat manoeuvres. | count | `0`, `1`, `2` |
| `replans_by_object` | JSON {object: number of replans}. | JSON / count | 14 distinct, e.g. `{"('petiole', 2)": 1, "('petiole', 0)…` |
| `frames` | Number of integrated control frames in the run (one frame = 1/30 s simulated; a full harvest takes about 600 frames = 20 s). | frame | 415 to 819 |
| `wall_min` | Wall-clock time of the run. | min | 12.5 to 82.1 |

### D_S3_fair_planner_BL5e/figure_data/T2_fig_candidate_rejections.csv

Why sampled BL5e cut-pose candidates were rejected, summed over T2.

Rows: 7. Columns: 2.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `rejection_reason` | Reason a sampled cut-pose candidate was rejected: tip_distance_gate, alignment_dynamic_axis_blade_scope, blade_face_not_facing_approach, no_blade_contact_window, cut_pose_collision, ik_unreachable_cut; passed_unrefined = candidate passed. |  | 7 distinct, e.g. `ik_unreachable_cut` |
| `count_over_all_BL5E2_planning_calls` | Number of candidates with this outcome, summed over all BL5e (v2) planning calls in the test set. | count | 76 to 51684 |

### D_S3_fair_planner_BL5e/figure_data/T2_fig_group_outcomes.csv

Per-group outcome counts and Wilson intervals, T2.

Rows: 3. Columns: 11.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `group` | Experimental arm. See README §5 (group codes) for the meaning of every code in this file. |  | `T2_BL5E2`, `T2_OURS`, `T2_BL5` |
| `n` | Number of registered units in the cell. | count | `10`, `30` |
| `attempted` | In per-run tables: True if the unit was launched. In group-outcome tables: number of units launched. | bool / count | `10`, `30` |
| `not_started` | Number of registered units that were not started. | count | `0` |
| `landing` | Number of full harvests under S3+L. | count | `0` |
| `strict` | Number of full harvests under strict S3. | count | `0` |
| `p2_cut_gated` | Per run: the first petiole (P2) was cut with all physical blade gates passing. Per group: number of such units. | bool / count | `27`, `0`, `10` |
| `safety_fail_landing` | Number of units with at least one safety failure under S3+L. | count | `0`, `6` |
| `furthest` | JSON counts of units by furthest_stage. | JSON | 3 distinct, e.g. `{"petiole2_exit": 24, "stalk1_exit": …` |
| `wilson_landing` | Wilson 95% interval of landing / n. | fraction | `[0.0, 0.278]`, `[0.0, 0.114]` |
| `wilson_p2_cut_gated` | Wilson 95% interval of p2_cut_gated / n. | fraction | `[0.744, 0.965]`, `[0.0, 0.278]`, `[0.722, 1.0]` |

### D_S3_fair_planner_BL5e/figure_data/T3_fig_bl5e_planning.csv

BL5e planning statistics per run, T3.

Rows: 15. Columns: 19.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `case` | Unique run identifier. Prefix encodes the study (H4176/H4177 = S3 confirmation, H4178 = ablations/baselines/generalization, H4179 = fair planner BL5e) and the suffix encodes group, level and repetition. |  | 15 distinct, e.g. `H4179311_T3_BL5E2_h4178_unseen_78301_…` |
| `group` | Experimental arm. See README §5 (group codes) for the meaning of every code in this file. |  | `T3_BL5E2` |
| `level` | Perturbation tier or scene. NOMINAL = registered start on scene 11; TRANSLATION_{X,Y,Z}_{NEG,POS} = robot base offset of ∓/±0.01 m; YAW_{NEG,POS} = base yaw ∓/±2°; JOINT_k_{NEG,POS} = joint k start offset ∓/±0.01 rad; CONTACT_DROP3_FORCE08 = contact-sensor degradation (contact reading dropped every 3rd frame, reported force scaled ×0.8); h4178_unseen_783xx = one of five unseen procedurally generated geometries. |  | `h4178_unseen_78301`, `h4178_unseen_78302`, `h4178_unseen_78303`, `h4178_unseen_78304`, `h4178_unseen_78305` |
| `seed` | Random seed. In S3 studies this is the process seed passed to the simulator; in S1/S2 studies it is the evaluation (scene) seed. |  | 78301 to 79302 |
| `furthest_stage` | Last milestone reached in the ordered chain P2 cut → P2 release → P2 exit → P0 cut → P0 release → P0 exit → stalk cut → stalk release → stalk exit (written petiole2_CUT … stalk1_exit). none = no milestone; screening = refused at start screening. |  | `stalk1_exit`, `petiole2_exit`, `none`, `stalk1_release` |
| `p2_cut_gated` | Per run: the first petiole (P2) was cut with all physical blade gates passing. Per group: number of such units. | bool / count | `True`, `False` |
| `landing_success` | In per-run tables: full harvest success under S3+L (landing exemption 300 N / 25 periods / 8 mm). In group summaries: number of such successes. | bool / count | `False` |
| `landing_safety` | No safety failure under S3+L. | bool | `False`, `True` |
| `landing_safety_failures` | Number of safety-failure records under S3+L. | count | 0 to 57 |
| `stop_reason` | Why the controller stopped. Examples: h4178_uniform_no_release_within_480_frames:(object) = baseline-only administrative stop when no new release occurs within 480 frames; bl5_no_collision_free_plan / bl5e_no_collision_free_plan = planner found no plan within budget; first_handoff_mechanism_complete = handoff role finished; finite_*_budget_exhausted = a bounded retry budget of our controller ran out; *_refused / invalid_* = our controller refused to continue because a frozen route or forecast was not valid for the current state; 'our frozen pipeline refused the unseen geometry before physics' = start refused. |  | 2 distinct, e.g. `h4178_uniform_no_release_within_480_f…`; 9 empty |
| `controller_stop_reason` | Stop reason reported by the BL5e controller. |  | 2 distinct, e.g. `h4178_uniform_no_release_within_480_f…`; 9 empty |
| `planning_calls` | Number of motion-planning calls. | count | `6`, `5`, `11`, `4`, `7`, `9` |
| `plans_accepted` | Number of plans accepted for execution. | count | `4`, `3`, `5`, `0`, `7` |
| `planning_wall_s_total` | Total wall-clock time spent planning. | s | 593 to 3134 |
| `monitor_stops` | Number of times the execution monitor stopped a plan (clearance margin violated during execution). | count | `0`, `1`, `2` |
| `retreats` | Number of retreat manoeuvres. | count | `0`, `1`, `2` |
| `replans_by_object` | JSON {object: number of replans}. | JSON / count | 9 distinct, e.g. `{"('petiole', 2)": 1, "('petiole', 0)…` |
| `frames` | Number of integrated control frames in the run (one frame = 1/30 s simulated; a full harvest takes about 600 frames = 20 s). | frame | 415 to 810 |
| `wall_min` | Wall-clock time of the run. | min | 12.7 to 60.6 |

### D_S3_fair_planner_BL5e/figure_data/T3_fig_candidate_rejections.csv

Why sampled BL5e cut-pose candidates were rejected, summed over T3.

Rows: 7. Columns: 2.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `rejection_reason` | Reason a sampled cut-pose candidate was rejected: tip_distance_gate, alignment_dynamic_axis_blade_scope, blade_face_not_facing_approach, no_blade_contact_window, cut_pose_collision, ik_unreachable_cut; passed_unrefined = candidate passed. |  | 7 distinct, e.g. `ik_unreachable_cut` |
| `count_over_all_BL5E2_planning_calls` | Number of candidates with this outcome, summed over all BL5e (v2) planning calls in the test set. | count | 110 to 33834 |

### D_S3_fair_planner_BL5e/figure_data/T3_fig_group_outcomes.csv

Per-group outcome counts and Wilson intervals, T3.

Rows: 3. Columns: 11.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `group` | Experimental arm. See README §5 (group codes) for the meaning of every code in this file. |  | `T3_BL5E2`, `T3_OURS`, `T3_BL5` |
| `n` | Number of registered units in the cell. | count | `5`, `15` |
| `attempted` | In per-run tables: True if the unit was launched. In group-outcome tables: number of units launched. | bool / count | `5`, `15` |
| `not_started` | Number of registered units that were not started. | count | `0` |
| `landing` | Number of full harvests under S3+L. | count | `0` |
| `strict` | Number of full harvests under strict S3. | count | `0` |
| `p2_cut_gated` | Per run: the first petiole (P2) was cut with all physical blade gates passing. Per group: number of such units. | bool / count | `12`, `0`, `4` |
| `safety_fail_landing` | Number of units with at least one safety failure under S3+L. | count | `0`, `9` |
| `furthest` | JSON counts of units by furthest_stage. | JSON | 3 distinct, e.g. `{"stalk1_exit": 7, "stalk1_release": …` |
| `wilson_landing` | Wilson 95% interval of landing / n. | fraction | `[0.0, 0.434]`, `[0.0, 0.204]` |
| `wilson_p2_cut_gated` | Wilson 95% interval of p2_cut_gated / n. | fraction | `[0.548, 0.93]`, `[0.0, 0.434]`, `[0.376, 0.964]` |

### D_S3_fair_planner_BL5e/run_tables/run_table_T1.csv

BL5e test set T1 = scene 11 (paper Table 11): BL5e v2 (BL5E2, reported), BL5e v1 (BL5E_V1, superseded by Amendment 01, reported separately), and BL5/OURS reference rows.

Rows: 16. Columns: 56.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `experiment` | Study identifier: exp1 = component ablation, exp2 = baselines on scene 11, exp3a = held-out perturbation tiers, exp3b = unseen geometries, T1/T2/T3 = BL5e test sets (scene 11 / held-out tiers / unseen geometries). |  | `T1` |
| `case` | Unique run identifier. Prefix encodes the study (H4176/H4177 = S3 confirmation, H4178 = ablations/baselines/generalization, H4179 = fair planner BL5e) and the suffix encodes group, level and repetition. |  | 16 distinct, e.g. `H4179111_T1_BL5E2_S78101` |
| `kind` | Run category: ours_full = our controller, full harvest; baseline = baseline controller; reference_only = row copied from an earlier frozen study for comparison (not re-run); ab6_static = AB6 ablation evaluated by static start screening only (no physics). |  | `reference_only`, `baseline` |
| `group` | Experimental arm. See README §5 (group codes) for the meaning of every code in this file. |  | `T1_BL5E2`, `T1_BL5E_V1`, `T1_OURS`, `T1_BL5` |
| `method` | Controller under test. OURS = frozen modular S3 controller; BL1–BL5 = baselines (paper Table 3); BL5E_V1 / BL5E2 = fair sampling-planner baseline BL5e, version 1 (voided after Amendment 01) and version 2 (reported). In A_*/geometry_adaptive_ik: fixed = fixed target library, adaptive = online damped-least-squares IK. |  | `BL5E2`, `BL5E_V1`, `OURS`, `BL5` |
| `switch_off` | Ablation switch disabled in this run (AB1 landing admission, AB2 stalk cached brake, AB3 E3g entry press, AB4 zero-force manifold admission, AB5 temporal interlock, AB6 screened initialization, AB7 live/cold barrier). Empty = no switch disabled. |  | always empty |
| `level` | Perturbation tier or scene. NOMINAL = registered start on scene 11; TRANSLATION_{X,Y,Z}_{NEG,POS} = robot base offset of ∓/±0.01 m; YAW_{NEG,POS} = base yaw ∓/±2°; JOINT_k_{NEG,POS} = joint k start offset ∓/±0.01 rad; CONTACT_DROP3_FORCE08 = contact-sensor degradation (contact reading dropped every 3rd frame, reported force scaled ×0.8); h4178_unseen_783xx = one of five unseen procedurally generated geometries. |  | `NOMINAL` |
| `seed` | Random seed. In S3 studies this is the process seed passed to the simulator; in S1/S2 studies it is the evaluation (scene) seed. |  | `78101`, `78102`, `78103`, `79101`, `79102` |
| `rep` | Repetition index within a group × level cell. |  | `1`, `2`, `3`, `4`, `5`; 11 empty |
| `label` | Evidential status of the study. Always 'exploratory' (preregistered but not confirmatory). Translated from the original Chinese value '探索性'. |  | `exploratory` |
| `status` | Run status from the queue: finished / PASSED / FAILED = executed; NOT_STARTED = registered but not launched (counted in the denominator); stopped_at_screening = refused by the start screen before physics; static_check = evaluated by static geometry only; reference_only = copied from an earlier study; INTERRUPTED_INFRASTRUCTURE = interrupted by instance migration (counted as failure); running = still running when the table was frozen (development table only). |  | `finished` |
| `attempted` | In per-run tables: True if the unit was launched. In group-outcome tables: number of units launched. | bool / count | `True` |
| `returncode` | Exit code of the simulator process (0 = normal exit; negative = terminated by signal, e.g. −15 SIGTERM, −11 SIGSEGV). |  | `0` |
| `wall_min` | Wall-clock time of the run. | min | 1 to 103.6 |
| `frames` | Number of integrated control frames in the run (one frame = 1/30 s simulated; a full harvest takes about 600 frames = 20 s). | frame | `511`, `599`, `59` |
| `strict_success` | Full harvest success under the strict S3 predicate (no landing exemption). | bool | `False` |
| `landing_success` | In per-run tables: full harvest success under S3+L (landing exemption 300 N / 25 periods / 8 mm). In group summaries: number of such successes. | bool / count | `False`, `True` |
| `strict_safety` | No safety failure under strict S3. | bool | `True`, `False` |
| `landing_safety` | No safety failure under S3+L. | bool | `True`, `False` |
| `strict_safety_failures` | Number of safety-failure records under strict S3 (one record per failing gate event). | count | `0`, `71`, `82` |
| `landing_safety_failures` | Number of safety-failure records under S3+L. | count | `0`, `82` |
| `h4176_judge_passed` | Verdict of the Confirmation I (H4176) acceptance judge, re-applied to OURS runs as a cross-check. Empty for baselines. | bool | `True`; 13 empty |
| `h4176_judge_safety` | Safety verdict of the H4176 acceptance judge (OURS only). | bool | `True`; 13 empty |
| `furthest_stage` | Last milestone reached in the ordered chain P2 cut → P2 release → P2 exit → P0 cut → P0 release → P0 exit → stalk cut → stalk release → stalk exit (written petiole2_CUT … stalk1_exit). none = no milestone; screening = refused at start screening. |  | `petiole2_exit`, `stalk1_exit` |
| `milestones` | Space-separated list of all milestones reached, in order. |  | 2 distinct, e.g. `petiole2_CUT petiole2_release petiole…` |
| `cut_steps` | Executed cuts as object@frame (e.g. petiole2@28 petiole0@355 stalk1@587). | frame | `petiole2@28`, `petiole2@28 petiole0@355 stalk1@587`, `petiole2@24` |
| `release_steps` | Frame at which each cut object's attachment was released: object@frame in folder B, JSON {object: frame} in folders C and D. | frame | 3 distinct, e.g. `{"('petiole', 2)": 29}` |
| `physical_exit_steps` | JSON {object: frame} at which the arm had sustained physical exit from each released object. | frame | 3 distinct, e.g. `{"('petiole', 2)": 32}` |
| `dangerous_executed_CUT` | Number of integrated frames on which a cut was executed while the full-arm (S3) permission evaluated at that frame was False. | frames | `0` |
| `dangerous_requested_CUT` | Number of integrated frames on which a cut was requested while the full-arm (S3) permission was False (a request may be blocked before execution). | frames | `0` |
| `temporal_decision_unavailable_frames` | Number of frames for which no full-arm permission decision was available. | frames | `0` |
| `nonblade_lt2mm_boundaries_strict` | Number of control boundaries at which some non-blade gap was below 2 mm (strict S3). | count | `0`, `8` |
| `nonblade_lt2mm_boundaries_landing` | Same, under S3+L (exempted landing contacts excluded). | count | `0` |
| `nonblade_min_gap_mm_strict` | Minimum non-blade gap under strict S3 (negative = interpenetration). | mm | -6.294 to 10.2 |
| `nonblade_min_gap_mm_landing` | Minimum non-blade gap under S3+L, excluding contacts covered by the landing exemption. | mm | 2.196 to 10.2 |
| `wrong_releases` | Number of attachment releases that were duplicated, out of order or mistimed (release must occur at cut frame + 1). | count | `0` |
| `unsafe_CUT` | Number of executed cuts for which the original physical blade gates (before or after the frame) or the identity permission did not pass. | count | `0` |
| `solver_peak_landing_force_n` | Peak landing contact force at solver substeps (S3+L cap 300 N). | N | `282.4805908203125`, `282.486328125`, `283.1697998046875`; 13 empty |
| `landing_cycles` | Number of control boundaries handled under the landing exemption. | periods | `0`, `10` |
| `landing_max_penetration_mm` | Maximum penetration recorded during exempted landing (cap 8 mm). | mm | `6.294`, `6.293`; 13 empty |
| `controller_wall_s` | Wall-clock time spent inside the controller (planning, screening, forecasting). | s | 19.44 to 3846; 3 empty |
| `stop_reason` | Why the controller stopped. Examples: h4178_uniform_no_release_within_480_frames:(object) = baseline-only administrative stop when no new release occurs within 480 frames; bl5_no_collision_free_plan / bl5e_no_collision_free_plan = planner found no plan within budget; first_handoff_mechanism_complete = handoff role finished; finite_*_budget_exhausted = a bounded retry budget of our controller ran out; *_refused / invalid_* = our controller refused to continue because a frozen route or forecast was not valid for the current state; 'our frozen pipeline refused the unseen geometry before physics' = start refused. |  | 2 distinct, e.g. `h4178_uniform_no_release_within_480_f…`; 3 empty |
| `stop_state` | Controller state machine state at the stop (approach_route, approach_cut, exit, await_task_completion). |  | `await_task_completion`; 13 empty |
| `termination` | JSON termination record of the environment (success, or motion_management_stop). | JSON | `{"motion_management_stop": true}`, `{"success": true}` |
| `first_strict_failure` | First safety-failure record under strict S3: JSON {frame, gate, object_id, …}. Gate codes: nonBlade_below_2mm_strict = a non-blade part closer than 2 mm to the plant; CUT_without_original_physical_gates_or_identity = a cut executed although the physical blade gates or the identity check did not pass; Blade_near_pair_outside_current_cut_or_nonworsening_scope = blade near a shape pair it is not allowed to approach; solver_landing_single_shape_force_above_300N = landing force above the cap. null = no failure. | JSON | 5 distinct, e.g. `null` |
| `first_landing_failure` | First safety-failure record under S3+L (same format and gate codes as first_strict_failure). | JSON | 2 distinct, e.g. `null` |
| `planning_calls` | Number of motion-planning calls. | count | `7`, `4`, `5`, `6`, `10`, `8`; 6 empty |
| `plans_accepted` | Number of plans accepted for execution. | count | `2`, `3`; 6 empty |
| `planning_wall_s_total` | Total wall-clock time spent planning. | s | 1287 to 3730; 6 empty |
| `replans_by_object` | JSON {object: number of replans}. | JSON / count | 6 distinct, e.g. `{"('petiole', 2)": 1, "('petiole', 0)…`; 6 empty |
| `monitor_stops` | Number of times the execution monitor stopped a plan (clearance margin violated during execution). | count | `1`, `0`; 6 empty |
| `retreats` | Number of retreat manoeuvres. | count | `0`, `1`; 6 empty |
| `controller_stop_reason` | Stop reason reported by the BL5e controller. |  | 1 distinct, e.g. `h4178_uniform_no_release_within_480_f…`; 6 empty |
| `mode_frames` | JSON {controller mode: number of frames} (idle, track, cut_dwell, exit, …). | JSON / frames | 9 distinct, e.g. `{"idle": 202, "exit": 5, "track": 291…`; 6 empty |
| `plans` | JSON list of plans: frame, object, planning wall time, path length, verdict. | JSON | 10 distinct, e.g. `[{"frame": 4, "object": "petiole2", "…`; 6 empty |
| `p2_cut_gated` | Per run: the first petiole (P2) was cut with all physical blade gates passing. Per group: number of such units. | bool / count | `True` |

### D_S3_fair_planner_BL5e/run_tables/run_table_T2.csv

BL5e test set T2 = the 10 held-out tiers × 3 seeds (paper Table 11).

Rows: 50. Columns: 57.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `experiment` | Study identifier: exp1 = component ablation, exp2 = baselines on scene 11, exp3a = held-out perturbation tiers, exp3b = unseen geometries, T1/T2/T3 = BL5e test sets (scene 11 / held-out tiers / unseen geometries). |  | `T2` |
| `case` | Unique run identifier. Prefix encodes the study (H4176/H4177 = S3 confirmation, H4178 = ablations/baselines/generalization, H4179 = fair planner BL5e) and the suffix encodes group, level and repetition. |  | 50 distinct, e.g. `H4179211_T2_BL5E2_JOINT_0_POS_S78201` |
| `kind` | Run category: ours_full = our controller, full harvest; baseline = baseline controller; reference_only = row copied from an earlier frozen study for comparison (not re-run); ab6_static = AB6 ablation evaluated by static start screening only (no physics). |  | `baseline`, `reference_only` |
| `group` | Experimental arm. See README §5 (group codes) for the meaning of every code in this file. |  | `T2_BL5E2`, `T2_OURS`, `T2_BL5` |
| `method` | Controller under test. OURS = frozen modular S3 controller; BL1–BL5 = baselines (paper Table 3); BL5E_V1 / BL5E2 = fair sampling-planner baseline BL5e, version 1 (voided after Amendment 01) and version 2 (reported). In A_*/geometry_adaptive_ik: fixed = fixed target library, adaptive = online damped-least-squares IK. |  | `BL5E2`, `OURS`, `BL5` |
| `switch_off` | Ablation switch disabled in this run (AB1 landing admission, AB2 stalk cached brake, AB3 E3g entry press, AB4 zero-force manifold admission, AB5 temporal interlock, AB6 screened initialization, AB7 live/cold barrier). Empty = no switch disabled. |  | always empty |
| `level` | Perturbation tier or scene. NOMINAL = registered start on scene 11; TRANSLATION_{X,Y,Z}_{NEG,POS} = robot base offset of ∓/±0.01 m; YAW_{NEG,POS} = base yaw ∓/±2°; JOINT_k_{NEG,POS} = joint k start offset ∓/±0.01 rad; CONTACT_DROP3_FORCE08 = contact-sensor degradation (contact reading dropped every 3rd frame, reported force scaled ×0.8); h4178_unseen_783xx = one of five unseen procedurally generated geometries. |  | 10 distinct, e.g. `JOINT_0_POS` |
| `seed` | Random seed. In S3 studies this is the process seed passed to the simulator; in S1/S2 studies it is the evaluation (scene) seed. |  | `78201`, `79201`, `79202`; 10 empty |
| `rep` | Repetition index within a group × level cell. |  | `1`, `2`, `3`; 20 empty |
| `label` | Evidential status of the study. Always 'exploratory' (preregistered but not confirmatory). Translated from the original Chinese value '探索性'. |  | `exploratory` |
| `status` | Run status from the queue: finished / PASSED / FAILED = executed; NOT_STARTED = registered but not launched (counted in the denominator); stopped_at_screening = refused by the start screen before physics; static_check = evaluated by static geometry only; reference_only = copied from an earlier study; INTERRUPTED_INFRASTRUCTURE = interrupted by instance migration (counted as failure); running = still running when the table was frozen (development table only). |  | `finished`, `reference_only` |
| `attempted` | In per-run tables: True if the unit was launched. In group-outcome tables: number of units launched. | bool / count | `True`; 10 empty |
| `returncode` | Exit code of the simulator process (0 = normal exit; negative = terminated by signal, e.g. −15 SIGTERM, −11 SIGSEGV). |  | `0`; 10 empty |
| `wall_min` | Wall-clock time of the run. | min | 0.9 to 82.1; 10 empty |
| `frames` | Number of integrated control frames in the run (one frame = 1/30 s simulated; a full harvest takes about 600 frames = 20 s). | frame | 57 to 819; 10 empty |
| `strict_success` | Full harvest success under the strict S3 predicate (no landing exemption). | bool | `False` |
| `landing_success` | In per-run tables: full harvest success under S3+L (landing exemption 300 N / 25 periods / 8 mm). In group summaries: number of such successes. | bool / count | `False` |
| `strict_safety` | No safety failure under strict S3. | bool | `True`, `False`; 10 empty |
| `landing_safety` | No safety failure under S3+L. | bool | `True`, `False`; 10 empty |
| `strict_safety_failures` | Number of safety-failure records under strict S3 (one record per failing gate event). | count | 0 to 514; 10 empty |
| `landing_safety_failures` | Number of safety-failure records under S3+L. | count | 0 to 454; 10 empty |
| `h4176_judge_passed` | Verdict of the Confirmation I (H4176) acceptance judge, re-applied to OURS runs as a cross-check. Empty for baselines. | bool | always empty |
| `h4176_judge_safety` | Safety verdict of the H4176 acceptance judge (OURS only). | bool | always empty |
| `furthest_stage` | Last milestone reached in the ordered chain P2 cut → P2 release → P2 exit → P0 cut → P0 release → P0 exit → stalk cut → stalk release → stalk exit (written petiole2_CUT … stalk1_exit). none = no milestone; screening = refused at start screening. |  | `petiole2_exit`, `screening`, `stalk1_exit`, `none`, `stage-B runs 0/3` |
| `milestones` | Space-separated list of all milestones reached, in order. |  | 2 distinct, e.g. `petiole2_CUT petiole2_release petiole…`; 13 empty |
| `cut_steps` | Executed cuts as object@frame (e.g. petiole2@28 petiole0@355 stalk1@587). | frame | 12 distinct, e.g. `petiole2@29`; 13 empty |
| `release_steps` | Frame at which each cut object's attachment was released: object@frame in folder B, JSON {object: frame} in folders C and D. | frame | 13 distinct, e.g. `{"('petiole', 2)": 30}`; 10 empty |
| `physical_exit_steps` | JSON {object: frame} at which the arm had sustained physical exit from each released object. | frame | 13 distinct, e.g. `{"('petiole', 2)": 33}`; 10 empty |
| `dangerous_executed_CUT` | Number of integrated frames on which a cut was executed while the full-arm (S3) permission evaluated at that frame was False. | frames | `0`; 10 empty |
| `dangerous_requested_CUT` | Number of integrated frames on which a cut was requested while the full-arm (S3) permission was False (a request may be blocked before execution). | frames | `0`; 10 empty |
| `temporal_decision_unavailable_frames` | Number of frames for which no full-arm permission decision was available. | frames | `0`; 10 empty |
| `nonblade_lt2mm_boundaries_strict` | Number of control boundaries at which some non-blade gap was below 2 mm (strict S3). | count | `0`, `47`, `15`, `13`; 10 empty |
| `nonblade_lt2mm_boundaries_landing` | Same, under S3+L (exempted landing contacts excluded). | count | `0`, `47`, `1`, `6`; 10 empty |
| `nonblade_min_gap_mm_strict` | Minimum non-blade gap under strict S3 (negative = interpenetration). | mm | -7.17 to 51.89; 10 empty |
| `nonblade_min_gap_mm_landing` | Minimum non-blade gap under S3+L, excluding contacts covered by the landing exemption. | mm | -4.029 to 51.89; 10 empty |
| `wrong_releases` | Number of attachment releases that were duplicated, out of order or mistimed (release must occur at cut frame + 1). | count | `0`; 10 empty |
| `unsafe_CUT` | Number of executed cuts for which the original physical blade gates (before or after the frame) or the identity permission did not pass. | count | `0`; 10 empty |
| `solver_peak_landing_force_n` | Peak landing contact force at solver substeps (S3+L cap 300 N). | N | `95.99048614501953`, `682.8005981445312`, `779.9795532226562`; 47 empty |
| `landing_cycles` | Number of control boundaries handled under the landing exemption. | periods | `0`, `24`, `15`, `8`; 10 empty |
| `landing_max_penetration_mm` | Maximum penetration recorded during exempted landing (cap 8 mm). | mm | `1.071`, `5.594`, `7.17`; 47 empty |
| `controller_wall_s` | Wall-clock time spent inside the controller (planning, screening, forecasting). | s | 19.18 to 4751; 10 empty |
| `stop_reason` | Why the controller stopped. Examples: h4178_uniform_no_release_within_480_frames:(object) = baseline-only administrative stop when no new release occurs within 480 frames; bl5_no_collision_free_plan / bl5e_no_collision_free_plan = planner found no plan within budget; first_handoff_mechanism_complete = handoff role finished; finite_*_budget_exhausted = a bounded retry budget of our controller ran out; *_refused / invalid_* = our controller refused to continue because a frozen route or forecast was not valid for the current state; 'our frozen pipeline refused the unseen geometry before physics' = start refused. |  | 3 distinct, e.g. `h4178_uniform_no_release_within_480_f…`; 13 empty |
| `stop_state` | Controller state machine state at the stop (approach_route, approach_cut, exit, await_task_completion). |  | always empty |
| `termination` | JSON termination record of the environment (success, or motion_management_stop). | JSON | `{"motion_management_stop": true}`, `{"success": true}`; 10 empty |
| `first_strict_failure` | First safety-failure record under strict S3: JSON {frame, gate, object_id, …}. Gate codes: nonBlade_below_2mm_strict = a non-blade part closer than 2 mm to the plant; CUT_without_original_physical_gates_or_identity = a cut executed although the physical blade gates or the identity check did not pass; Blade_near_pair_outside_current_cut_or_nonworsening_scope = blade near a shape pair it is not allowed to approach; solver_landing_single_shape_force_above_300N = landing force above the cap. null = no failure. | JSON | 7 distinct, e.g. `null`; 10 empty |
| `first_landing_failure` | First safety-failure record under S3+L (same format and gate codes as first_strict_failure). | JSON | 7 distinct, e.g. `null`; 10 empty |
| `planning_calls` | Number of motion-planning calls. | count | 2 to 12; 20 empty |
| `plans_accepted` | Number of plans accepted for execution. | count | 0 to 6; 20 empty |
| `planning_wall_s_total` | Total wall-clock time spent planning. | s | 594 to 4660; 20 empty |
| `replans_by_object` | JSON {object: number of replans}. | JSON / count | 14 distinct, e.g. `{"('petiole', 2)": 1, "('petiole', 0)…`; 20 empty |
| `monitor_stops` | Number of times the execution monitor stopped a plan (clearance margin violated during execution). | count | `0`, `1`, `2`; 20 empty |
| `retreats` | Number of retreat manoeuvres. | count | `0`, `1`, `2`; 20 empty |
| `controller_stop_reason` | Stop reason reported by the BL5e controller. |  | 2 distinct, e.g. `h4178_uniform_no_release_within_480_f…`; 23 empty |
| `mode_frames` | JSON {controller mode: number of frames} (idle, track, cut_dwell, exit, …). | JSON / frames | 28 distinct, e.g. `{"idle": 413, "exit": 5, "track": 82,…`; 20 empty |
| `plans` | JSON list of plans: frame, object, planning wall time, path length, verdict. | JSON | 30 distinct, e.g. `[{"frame": 4, "object": "petiole2", "…`; 20 empty |
| `p2_cut_gated` | Per run: the first petiole (P2) was cut with all physical blade gates passing. Per group: number of such units. | bool / count | `True`, `False` |
| `note` | Free-text note. |  | 2 distinct, e.g. `stage-B screening conclusion reused, …`; 40 empty |

### D_S3_fair_planner_BL5e/run_tables/run_table_T3.csv

BL5e test set T3 = the 5 unseen geometries × 3 seeds (paper Table 11).

Rows: 25. Columns: 57.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `experiment` | Study identifier: exp1 = component ablation, exp2 = baselines on scene 11, exp3a = held-out perturbation tiers, exp3b = unseen geometries, T1/T2/T3 = BL5e test sets (scene 11 / held-out tiers / unseen geometries). |  | `T3` |
| `case` | Unique run identifier. Prefix encodes the study (H4176/H4177 = S3 confirmation, H4178 = ablations/baselines/generalization, H4179 = fair planner BL5e) and the suffix encodes group, level and repetition. |  | 25 distinct, e.g. `H4179311_T3_BL5E2_h4178_unseen_78301_…` |
| `kind` | Run category: ours_full = our controller, full harvest; baseline = baseline controller; reference_only = row copied from an earlier frozen study for comparison (not re-run); ab6_static = AB6 ablation evaluated by static start screening only (no physics). |  | `baseline`, `reference_only` |
| `group` | Experimental arm. See README §5 (group codes) for the meaning of every code in this file. |  | `T3_BL5E2`, `T3_OURS`, `T3_BL5` |
| `method` | Controller under test. OURS = frozen modular S3 controller; BL1–BL5 = baselines (paper Table 3); BL5E_V1 / BL5E2 = fair sampling-planner baseline BL5e, version 1 (voided after Amendment 01) and version 2 (reported). In A_*/geometry_adaptive_ik: fixed = fixed target library, adaptive = online damped-least-squares IK. |  | `BL5E2`, `OURS`, `BL5` |
| `switch_off` | Ablation switch disabled in this run (AB1 landing admission, AB2 stalk cached brake, AB3 E3g entry press, AB4 zero-force manifold admission, AB5 temporal interlock, AB6 screened initialization, AB7 live/cold barrier). Empty = no switch disabled. |  | always empty |
| `level` | Perturbation tier or scene. NOMINAL = registered start on scene 11; TRANSLATION_{X,Y,Z}_{NEG,POS} = robot base offset of ∓/±0.01 m; YAW_{NEG,POS} = base yaw ∓/±2°; JOINT_k_{NEG,POS} = joint k start offset ∓/±0.01 rad; CONTACT_DROP3_FORCE08 = contact-sensor degradation (contact reading dropped every 3rd frame, reported force scaled ×0.8); h4178_unseen_783xx = one of five unseen procedurally generated geometries. |  | `h4178_unseen_78301`, `h4178_unseen_78302`, `h4178_unseen_78303`, `h4178_unseen_78304`, `h4178_unseen_78305` |
| `seed` | Random seed. In S3 studies this is the process seed passed to the simulator; in S1/S2 studies it is the evaluation (scene) seed. |  | 78301 to 79302 |
| `rep` | Repetition index within a group × level cell. |  | `1`, `2`, `3`; 10 empty |
| `label` | Evidential status of the study. Always 'exploratory' (preregistered but not confirmatory). Translated from the original Chinese value '探索性'. |  | `exploratory` |
| `status` | Run status from the queue: finished / PASSED / FAILED = executed; NOT_STARTED = registered but not launched (counted in the denominator); stopped_at_screening = refused by the start screen before physics; static_check = evaluated by static geometry only; reference_only = copied from an earlier study; INTERRUPTED_INFRASTRUCTURE = interrupted by instance migration (counted as failure); running = still running when the table was frozen (development table only). |  | `finished`, `reference_only` |
| `attempted` | In per-run tables: True if the unit was launched. In group-outcome tables: number of units launched. | bool / count | `True`; 5 empty |
| `returncode` | Exit code of the simulator process (0 = normal exit; negative = terminated by signal, e.g. −15 SIGTERM, −11 SIGSEGV). |  | `0`; 5 empty |
| `wall_min` | Wall-clock time of the run. | min | 0.8 to 60.6; 5 empty |
| `frames` | Number of integrated control frames in the run (one frame = 1/30 s simulated; a full harvest takes about 600 frames = 20 s). | frame | 35 to 810; 5 empty |
| `strict_success` | Full harvest success under the strict S3 predicate (no landing exemption). | bool | `False` |
| `landing_success` | In per-run tables: full harvest success under S3+L (landing exemption 300 N / 25 periods / 8 mm). In group summaries: number of such successes. | bool / count | `False` |
| `strict_safety` | No safety failure under strict S3. | bool | `True`, `False`; 5 empty |
| `landing_safety` | No safety failure under S3+L. | bool | `True`, `False`; 5 empty |
| `strict_safety_failures` | Number of safety-failure records under strict S3 (one record per failing gate event). | count | 0 to 157; 5 empty |
| `landing_safety_failures` | Number of safety-failure records under S3+L. | count | 0 to 57; 5 empty |
| `h4176_judge_passed` | Verdict of the Confirmation I (H4176) acceptance judge, re-applied to OURS runs as a cross-check. Empty for baselines. | bool | always empty |
| `h4176_judge_safety` | Safety verdict of the H4176 acceptance judge (OURS only). | bool | always empty |
| `furthest_stage` | Last milestone reached in the ordered chain P2 cut → P2 release → P2 exit → P0 cut → P0 release → P0 exit → stalk cut → stalk release → stalk exit (written petiole2_CUT … stalk1_exit). none = no milestone; screening = refused at start screening. |  | `stalk1_exit`, `petiole2_exit`, `screening`, `none`, `stalk1_release` |
| `milestones` | Space-separated list of all milestones reached, in order. |  | 3 distinct, e.g. `petiole2_CUT petiole2_release petiole…`; 9 empty |
| `cut_steps` | Executed cuts as object@frame (e.g. petiole2@28 petiole0@355 stalk1@587). | frame | 15 distinct, e.g. `petiole2@17 petiole0@334 stalk1@601`; 9 empty |
| `release_steps` | Frame at which each cut object's attachment was released: object@frame in folder B, JSON {object: frame} in folders C and D. | frame | 16 distinct, e.g. `{"('petiole', 2)": 18, "('petiole', 0…`; 5 empty |
| `physical_exit_steps` | JSON {object: frame} at which the arm had sustained physical exit from each released object. | frame | 16 distinct, e.g. `{"('petiole', 2)": 21, "('petiole', 0…`; 5 empty |
| `dangerous_executed_CUT` | Number of integrated frames on which a cut was executed while the full-arm (S3) permission evaluated at that frame was False. | frames | `0`; 5 empty |
| `dangerous_requested_CUT` | Number of integrated frames on which a cut was requested while the full-arm (S3) permission was False (a request may be blocked before execution). | frames | `0`; 5 empty |
| `temporal_decision_unavailable_frames` | Number of frames for which no full-arm permission decision was available. | frames | `0`; 5 empty |
| `nonblade_lt2mm_boundaries_strict` | Number of control boundaries at which some non-blade gap was below 2 mm (strict S3). | count | 0 to 20; 5 empty |
| `nonblade_lt2mm_boundaries_landing` | Same, under S3+L (exempted landing contacts excluded). | count | `0`, `1`, `13`; 5 empty |
| `nonblade_min_gap_mm_strict` | Minimum non-blade gap under strict S3 (negative = interpenetration). | mm | -6.425 to 148.8; 5 empty |
| `nonblade_min_gap_mm_landing` | Minimum non-blade gap under S3+L, excluding contacts covered by the landing exemption. | mm | -1.317 to 148.8; 5 empty |
| `wrong_releases` | Number of attachment releases that were duplicated, out of order or mistimed (release must occur at cut frame + 1). | count | `0`; 5 empty |
| `unsafe_CUT` | Number of executed cuts for which the original physical blade gates (before or after the frame) or the identity permission did not pass. | count | `0`, `1`; 5 empty |
| `solver_peak_landing_force_n` | Peak landing contact force at solver substeps (S3+L cap 300 N). | N | 464.5 to 828.3; 16 empty |
| `landing_cycles` | Number of control boundaries handled under the landing exemption. | periods | `0`, `8`, `10`, `12`, `13`; 5 empty |
| `landing_max_penetration_mm` | Maximum penetration recorded during exempted landing (cap 8 mm). | mm | 5.606 to 6.425; 16 empty |
| `controller_wall_s` | Wall-clock time spent inside the controller (planning, screening, forecasting). | s | 11.91 to 3368; 5 empty |
| `stop_reason` | Why the controller stopped. Examples: h4178_uniform_no_release_within_480_frames:(object) = baseline-only administrative stop when no new release occurs within 480 frames; bl5_no_collision_free_plan / bl5e_no_collision_free_plan = planner found no plan within budget; first_handoff_mechanism_complete = handoff role finished; finite_*_budget_exhausted = a bounded retry budget of our controller ran out; *_refused / invalid_* = our controller refused to continue because a frozen route or forecast was not valid for the current state; 'our frozen pipeline refused the unseen geometry before physics' = start refused. |  | 3 distinct, e.g. `bl5_no_collision_free_plan`; 14 empty |
| `stop_state` | Controller state machine state at the stop (approach_route, approach_cut, exit, await_task_completion). |  | always empty |
| `termination` | JSON termination record of the environment (success, or motion_management_stop). | JSON | `{"motion_management_stop": true}`, `{"success": true}`; 5 empty |
| `first_strict_failure` | First safety-failure record under strict S3: JSON {frame, gate, object_id, …}. Gate codes: nonBlade_below_2mm_strict = a non-blade part closer than 2 mm to the plant; CUT_without_original_physical_gates_or_identity = a cut executed although the physical blade gates or the identity check did not pass; Blade_near_pair_outside_current_cut_or_nonworsening_scope = blade near a shape pair it is not allowed to approach; solver_landing_single_shape_force_above_300N = landing force above the cap. null = no failure. | JSON | 10 distinct, e.g. `{"frame": 338, "gate": "nonBlade_belo…`; 5 empty |
| `first_landing_failure` | First safety-failure record under S3+L (same format and gate codes as first_strict_failure). | JSON | 10 distinct, e.g. `{"row": 5424, "control_step": 339, "g…`; 5 empty |
| `planning_calls` | Number of motion-planning calls. | count | `6`, `5`, `11`, `4`, `7`, `9`; 10 empty |
| `plans_accepted` | Number of plans accepted for execution. | count | `4`, `3`, `5`, `0`, `7`; 10 empty |
| `planning_wall_s_total` | Total wall-clock time spent planning. | s | 593 to 3134; 10 empty |
| `replans_by_object` | JSON {object: number of replans}. | JSON / count | 9 distinct, e.g. `{"('petiole', 2)": 1, "('petiole', 0)…`; 10 empty |
| `monitor_stops` | Number of times the execution monitor stopped a plan (clearance margin violated during execution). | count | `0`, `1`, `2`; 10 empty |
| `retreats` | Number of retreat manoeuvres. | count | `0`, `1`, `2`; 10 empty |
| `controller_stop_reason` | Stop reason reported by the BL5e controller. |  | 2 distinct, e.g. `h4178_uniform_no_release_within_480_f…`; 19 empty |
| `mode_frames` | JSON {controller mode: number of frames} (idle, track, cut_dwell, exit, …). | JSON / frames | 13 distinct, e.g. `{"idle": 60, "exit": 22, "track": 487…`; 10 empty |
| `plans` | JSON list of plans: frame, object, planning wall time, path length, verdict. | JSON | 15 distinct, e.g. `[{"frame": 4, "object": "petiole2", "…`; 10 empty |
| `p2_cut_gated` | Per run: the first petiole (P2) was cut with all physical blade gates passing. Per group: number of such units. | bool / count | `True`, `False` |
| `note` | Free-text note. |  | 1 distinct, e.g. `H4178 exp3b ours (refused before phys…`; 20 empty |

## E_launch_ledger

### E_launch_ledger/launch_ledger_cumulative.csv

Cumulative launch ledger of every simulator process launched for the S3 work (development, confirmatory and exploratory), 1,649 rows. Supports recommendation 6 (keep stopped runs in the denominator and publish the ledger).

Rows: 1649. Columns: 17.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `case` | Unique run identifier. Prefix encodes the study (H4176/H4177 = S3 confirmation, H4178 = ablations/baselines/generalization, H4179 = fair planner BL5e) and the suffix encodes group, level and repetition. |  | 1649 distinct, e.g. `H1000040_PRIVATE_BALANCED_FIRSTFREE_F…` |
| `process_started` | True if a simulator process was started for this unit. | bool | `True` |
| `status` | Run status from the queue: finished / PASSED / FAILED = executed; NOT_STARTED = registered but not launched (counted in the denominator); stopped_at_screening = refused by the start screen before physics; static_check = evaluated by static geometry only; reference_only = copied from an earlier study; INTERRUPTED_INFRASTRUCTURE = interrupted by instance migration (counted as failure); running = still running when the table was frozen (development table only). |  | `finished`, `running` |
| `returncode` | Exit code of the simulator process (0 = normal exit; negative = terminated by signal, e.g. −15 SIGTERM, −11 SIGSEGV). |  | `0`, `1`, `-15`, `-11`, `-2`; 1 empty |
| `integrated_control_frames` | Number of integrated control frames. | frame | 0 to 600; 223 empty |
| `actual_CUT` | Number of executed cuts. | count | `0`, `1`, `3`, `2`; 223 empty |
| `true_release_count` | Number of attachment releases confirmed in the physics engine. | count | `0`, `1`, `3`, `2`; 219 empty |
| `sustained_exit_count` | Number of sustained exits. | count | `0`, `1`, `3`, `2`; 219 empty |
| `independent_full_complete` | An independent re-reading of the raw log confirms 3 cuts, 3 releases and 3 sustained exits. | bool | `False`, `True` |
| `identity_audit_passed` | Run passed the identity audit (the object cut is the expected one and the input matches the registered input). | bool | `True`; 1531 empty |
| `nonblade_safety_violation` | A non-blade part came closer than 2 mm to the plant during the run. | bool | `False`; 1531 empty |
| `source` | Original path of the run directory inside the simulation container (/workspace/…). Kept for traceability; not needed to read the data. |  | 719 distinct, e.g. `/workspace/oilpalmplantation_all_code…` |
| `launch_ledger_sha256` | SHA-256 of this launch's ledger record. | hex | 1649 distinct, e.g. `9ba04b8023bdad8855b16b4db3a8555c964cf…` |
| `not_confirmation` | Run belongs to development or exploratory work, not to a confirmatory denominator. | bool | `True`, `False` |
| `formal_confirmation` | Run belongs to a preregistered confirmatory denominator. | bool | `False`, `True` |
| `confirmation_role` | Role inside the confirmation protocol (see `role`); private_exact_same_paused_input_qualification = cold qualification replay. |  | 4 distinct, e.g. `full_harvest`; 1580 empty |
| `measurement_incomplete` | Some measurement of the run is missing (e.g. no substep observer), so its safety cannot be proven. | bool | `False`, `True`; 1530 empty |

## Package root

### PROVENANCE.csv

Mapping of every file in this package to its original file in the frozen data packages, with hashes.

Rows: 125. Columns: 5.

| Column | Meaning | Unit | Observed values |
|---|---|---|---|
| `package_path` | Path of the file in this package. |  | 125 distinct, e.g. `A_S1_S2_blade_and_object_gates/contro…` |
| `original_path` | Path of the source file in the original frozen data packages (folder names translated to English; original names were Chinese). |  | 125 distinct, e.g. `S1_S2_archive/oilpalm_geometry_result…` |
| `original_sha256` | SHA-256 of the original file. | hex | 120 distinct, e.g. `fa43161a3e8e6ed3dfacf730a2ee0d6fb32ab…` |
| `package_sha256` | SHA-256 of the file in this package. | hex | 120 distinct, e.g. `57314e345836204bd64f5efe838cd13829095…` |
| `modification` | What was changed when copying (see README §6). |  | 5 distinct, e.g. `rewritten as UTF-8/LF` |

