VERDICT: PASS
CONTENT-HASH: d83301a5d06970e5
## Blocking

## Polish
- content/en/FY4/fy4-9/exercises/solutions.md:105 — L3-02 "When the force and the time are at their greatest". The time $0.12\,\text{s}$ is fixed; only the force has a maximum. Suggest "When the average force is at its greatest".
- content/en/FY4/fy4-9/exercises/solutions.md:151 — L2-05 mean speed $v_\text{k}$ next to $\Delta t_\text{avg}$. Use one convention, e.g. $v_\text{avg}$.
- content/en/FY4/fy4-9/exercises/solutions.md L2-07 Answer — "the velocity $1.50\,\text{m/s}$ rounded" is an unclear reason. The limiting data are the mass $0.50\,\text{kg}$ and the force values read.

## Checked
- One Python script recomputed every answer from the task data: 5.1; 6.0; 4.86; 6.0; 150; 1.8; 18 000; 400 N (L1-09); 6.0 kN; 6.44 kN; 1.5; 25.65; 927.5; 5.0 (metal 67 N); 2.88; 450; 3.0; 57.6; 60; 50.45 (39.2 kN); 447.3 N (clay 251.1 N). All equal answers.py and exercises.json.
- Sign conventions are right in the rebound tasks (L2-03, L3-03, L3-05). L3-05 includes the weight during contact: $N_\text{avg} = mg + m\Delta v/\Delta t$.
- Trapezoid sums: L2-07 has seven intervals with interior sum 144.0 N; L3-04 has ten intervals with interior sum 98.1 kN. Endpoints are 0, so the shortcut is valid.
- L1-09 distractors: each one really comes from its stated error (ms not converted 0.4 N; kinetic energy/time 4000; grams 400 000), and the feedback is right. L1-06 has exactly one correct option.
- Figures: ex-potku (trapezoid area 48 N·s) and tarkistus-kolmio (triangle area 5.4 N·s) give every value at a grid point, the area is not shaded, and the descriptions match.
- Diff (L2-08 Answer): the two-figure reason ($900\,\text{N}$, $12\,\text{ms}$ read to two figures) is now definite, as in the Finnish.
- Physics stays within FY4 momentum and impulse. Neglected weights and friction are stated where they matter, and the reasonableness checks are real checks (L3-05 heights 1.23 m and 0.78 m).
- Script comparison with content/fi: answers, units, tolerances, correct flags and every number in the texts and solutions.md identical.
