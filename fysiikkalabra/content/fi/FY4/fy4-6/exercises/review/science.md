VERDICT: PASS
CONTENT-HASH: f3b0097c04bf99a2
SCOPE: delta added-exercise from 3327555d5e0791a2 base 81db4a6fd727

## Blocking

## Polish
- lessons/FY4/fy4-6/answers.py (L2-09) — the slope 0,2145 is typed in, not computed from `pts` as L2-03 does. Computing it with `sum(n*f)/sum(n*n)` keeps the two tasks tied to the same figure data.

## Checked
- The round-1 blocking finding is fixed. L2-09 no longer repeats L2-03. The student reads the friction off the fitted line at N = mg = 7,85 N, where the figure has no point (between 5 N and 10 N), and then finds a = F_μ/m. The question is now the last sentence.
- Physics of L2-09: the line goes through the origin because F_μ = μN (the reason is stated). On level ground with only weight, normal force and friction, N = mg and a_x = −F_μ/m. The signs and the condition are stated, and the force diagram (G = N, F_μ opposite to v, a opposite to v) agrees with the motion.
- Recomputed: the least-squares slope through the origin is 0,21455. F_μ(7,848 N) = 1,684 N and a = 2,105 m/s², against 2,1 in exercises.json (tolerance 0,05). A hand line with slope 0,20 to 0,22 gives 1,96 to 2,16 m/s², mostly inside the tolerance. Rounding to two figures is justified (a hand-drawn line, two-figure points).
- The reasonableness check is real: the reading lies between the neighbouring points (1,1 N and 2,1 N).
- L1-09: "liukukitkakerroin" is the teacher's decision (MAFY's word) and is not a finding. μ = 0,014 gives F = μmg = 6,18 N, and answers.py agrees.
- I recomputed both answers in one script, beside python -I answers.py, and all values agree with exercises.json.
- Hash f3b0097c04bf99a2 at the start and at the end.
