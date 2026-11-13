VERDICT: PASS
CONTENT-HASH: af340b69e0e4d6ab
SCOPE: delta added-exercise from 0402e8c61e005ae8 base 7db0992d648a
## Blocking

## Polish
- content/en/FY4/fy4-1/exercises/solutions.md:269 — L2-09 Answer says the time $6.0\,\text{s}$ is "read from the graph", but the task text gives it; only the velocities are read (same in the Finnish) — "the velocities read from the graph and the given time $6.0\,\text{s}$ have two figures".

## Checked
- Round 2 diff: L2-08 symbol $v_\text{av}$ → $v_\text{sp}$ (average speed, kept apart from average velocity), used consistently in Find, Formula and Substitution; the Finnish uses $v_\text{kv}$ in the same three places.
- L2-08 recomputed: $s = 12 + 0 + 8 = 20\,\text{m}$, $v_\text{sp} = 2.0\,\text{m/s}$; average velocity $0.4\,\text{m/s}$ check right.
- L2-09 recomputed: $v_\text{A} = +2.0$, $v_\text{B} = -2.0\,\text{m/s}$, $d = |16 - 8| = 8\,\text{m}$; the significant-figure reason now matches the Finnish ("luettu kuvaajasta").
- answers.py run: every numeric answer equals exercises.json.
- Script comparison with content/fi for all 23 tasks: answers, units, tolerances, figures and every number in the texts and solutions.md identical.
