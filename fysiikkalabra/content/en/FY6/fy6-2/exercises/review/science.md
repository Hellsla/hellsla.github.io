VERDICT: PASS
CONTENT-HASH: 5d5b49dbc8de8981
SCOPE: delta added-exercise from d1e122ce80fd069c base 8f23aa7ae3bd

## Blocking
- none

## Polish
- exercises/solutions.md fy6-2-L2-10 Answer — "the reading is not consistent with the manufacturer's value" can read as if the lamp or reading were faulty; the real point (already in Reasonableness) is that the lamp is not running at its rated voltage, the meter's error cannot explain the 0.08 V gap. Could say "the lamp's voltage really differs from the rated value" in the Answer line too.
- exercises/solutions.md fy6-2-L2-09 Reasonableness — "the same follows from 0.03 V : 1.37 V" restates the result rather than checking it; a check against the range-share argument (0.02 V of digits dominates) is already there and is enough.

## Checked
- L2-09 recomputed: ΔU = 0.005 · 1.37 V + 2 · 0.01 V = 0.02685 V ≈ 0.03 V; answers.py, exercises.json agree; a student's 0.03 V is 11.7 % off and stays inside tolerance 0.12.
- L2-10 recomputed: (1.45 V − 1.37 V) : 0.02685 V = 2.98; with the rounded ΔU = 0.03 V a student gets 2.67, 10.6 % off, inside 0.12; unit empty (pure number) correct.
- Figure fy6-2/multimeter-task: display 1.37 V, pointer at −35° on the 20 V range, the error limit not shown; the description gives the same reading and range; resolution 0.01 V on 20 V with two decimals is realistic for a 3½-digit meter.
- Error-limit model ±(p % of reading + n digits) and the consistency criterion (difference ≤ error limit, the rated value taken as exact) match the lesson's model and the guardrail term "valmistajan ilmoittama virheraja".
- Interval 1.34–1.40 V excludes 1.45 V: conclusion consistent with the ratio > 1.
- Both solutions complete (given, principle, symbolic formula, conversion of 0.5 %, substitution with units, rounding reason, check).
- Inside FY6 scope (basic electrical measurements).
- Content hash checked at start and end.
