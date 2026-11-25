VERDICT: PASS
CONTENT-HASH: 250da0413dc684b5

## Blocking

## Polish
- exercises.json (fy3-8-L3-04, a)) — the solution now gives the safe two-figure lower limit $14\,\text{mm}$, but the check (`answer` 13.2, `tolerance` 0.03, about 12.8–13.6) rejects $14$ and accepts the unsafe $13$. The stored value was left unchanged on purpose. — If the teacher agrees, widen the tolerance so it accepts 14, or word the question so it asks for the computed value $g_\text{min}$.
- solutions.md (fy3-8-L3-03, Formula): as before, a last row $= (\gamma_\text{petrol} - 3\alpha_\text{steel})V_0\Delta T$ would take the simplification all the way.

## Checked
- The diff is one line, the L3-04 Answer. It now says $g_\text{min} = 13.2\,\text{mm}$ and, as a lower limit, rounded up to at least $14\,\text{mm}$. This follows the house rule that an "at least" value is rounded up, and it resolves my earlier polish item.
- Recomputed: $12\cdot10^{-6}\,\tfrac{1}{\text{K}}\cdot 25.0\,\text{m}\cdot 44\,\text{K} = 13.2\,\text{mm}$, and $g_\text{max} = 30\,\text{mm} - 12.0\,\text{mm} = 18\,\text{mm}$. answers.py line 37 gives 13.2.
- "Good to two figures": the coefficient $12\cdot10^{-6}\,\tfrac{1}{\text{K}}$ is the limiting datum, so the reason is right.
- $g_\text{max} = 18\,\text{mm}$ is an upper limit and is not rounded up, so it stays on the safe side.
- Model answer c) still agrees with a): $15\,\text{mm}$ lies in $13.2$–$18\,\text{mm}$ (and in $14$–$18\,\text{mm}$), the summer margin is $1.8\,\text{mm}$ and the winter gap is $27\,\text{mm} < 30\,\text{mm}$.
- Nothing else changed since the earlier PASS.
- The hash was the same at the start and the end.
