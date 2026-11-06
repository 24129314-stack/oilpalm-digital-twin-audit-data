"""Recompute the paper's key numbers from the public data package.
Run from the repository root:  python reproduce_numbers.py
"""
import pandas as pd
from math import sqrt

A = "A_S1_S2_blade_and_object_gates/"
B = "B_S3_confirmation_scene11/"
C = "C_S3_ablations_baselines_generalization/"
D = "D_S3_fair_planner_BL5e/"
T = lambda s: (s == True) | (s.astype(str) == "True")   # robust bool test


def wilson(k, n, z=1.96):
    if n == 0:
        return (0.0, 0.0)
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return float(round(c - h, 2)), float(round(c + h, 2))


print("== Table 5: matched-initialization ablation (S1, 20 episodes per group)")
g = pd.read_csv(A + "control_ablation_stage3_matched_training/group_metrics.csv")
print(g[["group", "successes", "started", "strict_success_rate", "timeout_rate", "mean_harvest_time_s"]].to_string(index=False))

print("\n== Fig. 5: five-seed paired robustness, D (learned) vs E (zero-RL)")
p = pd.read_csv(A + "paired_robustness_D_vs_E/episodes.csv")
print(p.groupby("group").success.apply(lambda s: f"{T(s).sum()}/{len(s)}").to_string())

print("\n== Table 12 row S1: strict vs conditional denominator")
i = pd.read_csv(A + "incomplete_episode_audit/incomplete_episodes.csv")
print(f"incomplete episodes = {len(i)}; strict = 120/150 = {120/150:.0%}; conditional = 120/120 = 100%")

print("\n== Table 8: preregistered S3+L confirmation on scene 11")
h = pd.read_csv(B + "run_tables/run_table_H4176_confirmation_I.csv")
nom = h[h.group.isin(["S1_FULL", "S2_UNPERTURBED"])]
print(f"Confirmation I full harvests: {T(nom.passed).sum()}/{len(nom)}  Wilson95 = {wilson(T(nom.passed).sum(), len(nom))}")
s = pd.read_csv(B + "run_tables/run_table_H4177_stageB_confirmation_II.csv")
nb = s[s.group.isin(["B1_FULL", "B1_NOMINAL_FULL"])]
print(f"Stage B full harvests:         {T(nb.passed).sum()}/{len(nb)}  Wilson95 = {wilson(T(nb.passed).sum(), len(nb))}")
cold = s[s.group == "AUX_COLD_RESTORE"]
print(f"Stage B cold replays passed:   {T(cold.passed).sum()}/{len(cold)}")
ho = s[s.group == "B1_HANDOFF"]
print(f"Stage B handoff:               {T(ho.passed).sum()}/{len(ho)}")
dg = s[s.group == "B2_CONTACT_DROP3_FORCE08"]
print(f"Held-out contact tier:         {T(dg.passed).sum()}/{len(dg)}")

print("\n== Fig. 7 / Fig. 10: margins of the 13 Stage B harvests")
f = pd.read_csv(B + "figure_data/fig1_full_harvest_repeatability.csv")
print(f"landing peak {f.peak_substep_force_n.min():.1f}-{f.peak_substep_force_n.max():.1f} N (cap 300 N); "
      f"min non-blade clearance {f.nonblade_min_mm.min():.3f} mm (threshold 2 mm); "
      f"landing periods {f.landing_cycles_used.max()} (cap 25); penetration {f.landing_max_penetration_mm.max():.2f} mm (cap 8)")
print("cut frames: P2", sorted(map(int, f.cut1_step.unique())), "P0", sorted(map(int, f.cut2_step.unique())), "stalk", sorted(map(int, f.cut3_step.unique())))

print("\n== Fig. 8: held-out tier screening")
t = pd.read_csv(B + "figure_data/fig3_holdout_tier_status.csv")
print(f"eligible tiers {T(t.eligible).sum()}/14; in primary denominator {T(t.in_primary_denominator).sum()}")
print(t.exclusion_reason.value_counts().to_string())

print("\n== Table 9: component ablation (S3+L successes out of 3)")
e1 = pd.read_csv(C + "run_tables/run_table_exp1.csv")
print(e1.groupby("group").landing_success.apply(lambda s: f"{T(s).sum()}/{len(s)}").to_string())

print("\n== Table 10: baselines on scene 11")
e2 = pd.read_csv(C + "run_tables/run_table_exp2.csv")
e2 = e2[e2.kind != "reference_only"]   # OURS rows are copied from Stage B, not re-run
print(e2.groupby("group").agg(landing=("landing_success", lambda s: T(s).sum()), n=("case", "size"),
                              furthest=("furthest_stage", lambda s: s.mode().iat[0] if s.notna().any() else "")).to_string())

print("\n== Table 11: fair planner BL5e (v2), all three test sets")
u = pd.read_csv(D + "figure_data/ANALYSIS_UNIT_PROGRESS_AND_FAILURE_CAUSES.csv")
x = u[u.group.str.contains("BL5E2")]
done3 = x[T(x.all_three_cuts_gated)]
print(f"units {len(x)}; first gated cut {x.gated_cuts.fillna('').str.contains('petiole2').sum()}; "
      f"all three gated cuts {len(done3)}; S3+L harvests {T(x.landing_success).sum()}")
big = x[x.solver_peak_landing_force_n > 300]
print(f"landing peaks above the 300 N cap: {big.solver_peak_landing_force_n.min():.0f}-{big.solver_peak_landing_force_n.max():.0f} N")
