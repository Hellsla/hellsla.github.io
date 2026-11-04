VERDICT: PASS
CONTENT-HASH: 9addf2b0a041a809

## Blocking

## Polish
- solutions.md fy7-10-L2-04 — the step heading "Reading the graph" introduces a protractor reading, not a graph (fi "Kuvaajan lukeminen" has the same wording). Fix: "Reading the figure" (style, C).

## Checked
- One script recomputed all 12 answers from the English task text with my own formulas: 1.3636; 1.2397; 38; 34.733; 58.750; 36.602; 2.0019; 34.667 ps; 1.5321; 60.0; 52.940; 34.249 — all agree with exercises.json and answers.py to < 10⁻⁴ relative.
- Translation fidelity: exercises.json and solutions.md carry the same numbers, units, tolerances and answers as the passed fi set, task by task.
- The English task texts state what the physics needs: angles from the normal (L2-01 asks explicitly), the half-cylinder geometry (L2-04), the plane of the normals (L3-01), perpendicular passage (L2-03).
- L1-05 and L3-02 go water → air below the critical angle (48.75°); the solutions check sin α₂ < 1.
- L2-03: Δt = (n − 1)d : c derived symbolically, cm → m right, 35 ps to two figures; the 67/100 ps check is right. L2-01's wrong-route 16.1° is right.
- L3-03: sin α₁ : v₁ = sin α₂ : v₂ derived from n = c : v, cross-checked with 1.33 and 1.52.
- Every solution has all seven steps and solves symbolically first; rounding follows the limiting datum; "optically denser/less dense" and angle names match the lesson's English terms.
- Note (tooling, not a finding): this packet's "Exercise brief" block is empty for en (it looks for the Finnish section names); I judged notation against the en lesson's formula section instead.
