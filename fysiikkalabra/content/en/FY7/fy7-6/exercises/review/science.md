VERDICT: FAIL
CONTENT-HASH: 038a37e0201e14a4

## Blocking
- exercises.json:51 and :64 (fy7-6-L1-06, the answer and the correct option) — A: "the field of the induced current keeps the flux unchanged" says the induced current stops the flux from changing. That is false for a resistive ring, where the flux still decreases and Lenz's law only opposes the decrease. It is also the misconception the set is meant to correct. The feedback and solutions.md already say "tries to keep" — fix: in both places write "tries to keep the flux unchanged" (or "opposes the decrease in flux").

## Polish
- solutions.md:217 (fy7-6-L3-05 Principle) — "When the resistance stays the same, the power grows as the square of the voltage" is not true for a sheet. A thinner sheet also narrows the current paths, so their resistance grows. The per-sheet argument with a constant resistance would give a total loss ∝ d rather than ∝ d². The conclusion still holds — fix: write "the induced voltage is smaller and the narrow current paths have more resistance, so the currents and the loss fall sharply".
- exercises.json:426 (fy7-6-L3-06) — "the same aluminium tube" points back to L2-09, which a student may not have done — fix: "an aluminium tube" or "the tube of the graph".
- fy7-6-L2-05 c) — "brakes more strongly at the same speed" uses F ∝ v, which the task does not state. F : v as the measure of braking is a fair reading — optionally add "assume the braking force is proportional to the speed".

## Checked
- I recomputed all 16 numeric answers in one script with my own formulas. All match answers.py and the answer values within tolerance; a student who rounds the intermediate values still lands inside the tolerance (L2-05, L3-04, L3-06).
- L3-04 data fit v = v_t(1 − e^(−t/τ)) with τ = v_t/g within ±0.005 m/s. The claim that the central difference (2.8 m/s²) exceeds the tangent slope (2.65 m/s²) is right for this concave curve.
- L3-05 ratios P : d² are 1.17–1.24 (within ±3 % of the mean). The ratio (1.0/0.35)² = 8.2 is right, and the condition "sheets thin compared with the penetration depth" is stated.
- L3-03: e = vBl, F = IlB = 0.60 N; the energy balance Fv = RI² = 1.8 W is right.
- L3-01: Q = cmΔT with no change of state is stated; the exit speed matches L2-03.
- Multiple choice L1-06, L1-07 and L2-08 (both stages): exactly one correct answer, and every distractor's feedback gives the right physical reason.
- Lenz directions in L1-02, L2-02, L2-06 and L2-08, plus the energy-conservation argument, are right.
- brake-task figure (F = 1.6 N·s/m · v, point at 0.25 m/s → 0.402 N) gives the 0.40 N and 1.6 N·s/m that the solutions read off it. Its description gives the grid but not the answer.
- Units, magnitudes and significant-figure reasons are right throughout; "converted into internal energy" is used as the guardrails require.
- Scope: induction, Lenz's law and eddy currents (FY7). The solutions use fy7-5 induction and F = IlB, the force on a current-carrying wire, from FY7.
