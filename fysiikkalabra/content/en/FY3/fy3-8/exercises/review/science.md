VERDICT: FAIL
CONTENT-HASH: 48b88e71ff165016

## Blocking
1. content/en/FY3/fy3-8/exercises/exercises.json:305 and solutions.md:222–226 — (A, internal consistency) The fy3-8-L2-09 text and solution write $\Delta L$, but the figure it shows (`fy3-8/length-graph`) labels its axis $\Delta l$. Every other task and solution in the set uses the MAFY notation $\Delta l$, $l_0$ (19 × $\Delta l$ in exercises.json, 70 in solutions.md). So the task's symbol is not the one on its own graph. — Write $\Delta l$ in the task text and in the solution (including $\Delta l_\text{whole}$).
2. content/en/FY3/fy3-8/exercises/solutions.md:212–217 — (A, internal consistency) The fy3-8-L1-09 solution writes $L_0$, $\Delta L$ and $\Delta L = \alpha L_0 \Delta T$, while the rest of the set (the #522 MAFY notation) writes $\Delta l = \alpha l_0 \Delta T$. The added tasks did not get the merged notation. — Use $l_0$ and $\Delta l$ throughout.

## Polish
1. lessons/FY3/fy3-8/answers.py:166 — the docstring still writes ΔL, L₀ (carried over from the last report). Rename to Δl, l₀.
2. exercises.json fy3-8-L1-09 — the tolerance of $4\,\%$ is tight if a table lists steel as $11\ldots13 \cdot 10^{-6}\,\text{1/K}$ (that is $\pm 8\,\%$). Check the MAFY row and widen the tolerance if MAFY gives a range.

## Checked
- L1-09: $\Delta l = 12 \cdot 10^{-6} \cdot 25 \cdot 50\,\text{m} = 0.015\,\text{m} = 15\,\text{mm}$, the same as answers.py. The linear model holds for a solid over $50\,\text{K}$, and the unit and two significant figures are right.
- L2-09: $k = 3.0/50 = 0.060\,\text{mm/K}$, $T = 20 + 2.0/0.060 = 53.3\,{}^\circ\text{C}$, the same as answers.py. A tolerance of $3\,\%$ gives $51.7\ldots54.9\,{}^\circ\text{C}$, which is the range the solution states.
- The figure's data (20 °C; 0 mm) and (70 °C; 3.0 mm) lie on grid intersections and match the solution's reading. The figure does not give the answer away, and its description holds the same values.
- Both solutions are complete: the seven parts are there, the unknown is solved in symbols first, and the reasonableness checks really check the result (two-thirds interpolation, 0.6 mm per metre).
- The hash was the same at the start and at the end.
