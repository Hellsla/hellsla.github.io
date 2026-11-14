VERDICT: PASS
CONTENT-HASH: 39cdae8624fc0e8c
SCOPE: delta added-exercise from 44f907a0c5ed6d70 base 8f23aa7ae3bd

## Blocking
- none

## Polish
- exercises/solutions.md fy6-4-L2-09 Answer — "500 mA, two significant figures" does not show two figures as written; "0.50 A = 500 mA" (already in the substitution) or 5.0 · 10² mA would make the claim visible.

## Checked
- fy6-4-L2-09 recomputed: R = 30 Ω · 45 Ω : 75 Ω = 18 Ω, I = 9.0 V : 18 Ω = 0.50 A = 500 mA; branch currents 0.30 A + 0.20 A = 0.50 A agree; answers.py and exercises.json agree; unit mA, tolerance 0.02 fits.
- Figure fy6-4/task-parallel traced from figures.py: R1 runs from node (236, 86) along the top wire to the right corner and down to node (476, 196); R2 runs from (236, 86) down to (236, 196) and right to the same node; both resistors lie between the same two nodes, the battery feeds them: a true parallel connection, as the task and description say.
- Figure gives 9.0 V, R1 = 30 Ω, R2 = 45 Ω and no currents; the description carries the same values.
- Conditions stated in the task (ideal battery, wire resistance ignored), so the full 9.0 V is across both branches.
- Solution complete: principle with reason (same two branching points), reading of the figure, symbolic 1/R and I = U/R before numbers, conversion to mA, two independent checks (branch sum, R smaller than the smaller resistor).
- Inside FY6 central contents (resistor connections, Kirchhoff's laws).
- Content hash checked at start and end.
