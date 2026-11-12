VERDICT: FAIL
CONTENT-HASH: e4232d6393f7c87c
Delta review (solution practice, 2026-11-12) of the version passed before.

## Blocking
1. (A) `sovella/tasks.json` s5 a, criterion `units_precision`: it awards "$\rho \approx 2680\,\text{kg/m}^3$", but the model answer now gives $\rho \approx 2{,}7 \cdot 10^3\,\text{kg/m}^3$ and says three figures are too many without the uncertainty (b gives ±80 kg/m³). Rubric and solution contradict. Fix: "$\rho \approx 2{,}7 \cdot 10^3\,\text{kg/m}^3$ (two figures, $V = 70\,\text{cm}^3$), or $(2680 \pm 80)\,\text{kg/m}^3$ with the uncertainty".

## Polish
(none)

## Checked
s5 a: 2677 kg/m³, two figures from $V = 70\,\text{cm}^3$ is a sound reason; b (78 kg/m³) unchanged. s6 b–d with the unrounded $a = 4{,}1667\,\text{m/s}^2$: $\mu_0 \ge 0{,}4247$, $a_\text{true}$ = 3,779 m/s², +10,25 %; the component equations in c (positive direction stated) are right. All agree with answers.py. The fi, fi-easy and en diffs carry identical mathematics (every changed formula compared token by token); answers.py run; `units.py check` passes.
