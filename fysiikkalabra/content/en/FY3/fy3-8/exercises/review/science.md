VERDICT: PASS
CONTENT-HASH: cd25322f12bff34e
SCOPE: delta added-exercise from c8fd8fdeae438699 base 5453544b2abc

## Blocking
(none)

## Polish
1. lessons/FY3/fy3-8/answers.py:166 — the docstring still writes ΔL, L₀ (carried over). Rename to Δl, l₀.
2. exercises.json fy3-8-L1-09 — a tolerance of $4\,\%$ is tight if a table gives steel as $11\ldots13 \cdot 10^{-6}\,\text{1/K}$. Check the MAFY row and widen the tolerance if it gives a range.

## Checked
- The round-3 blockers are fixed. L1-09 and L2-09 now write $\Delta l$ and $l_0$ in the task text and the solutions (exercises.json:305, solutions.md L1-09 and L2-09), the same as the rest of the set and the figure's axis $\Delta l$. Neither file has any $\Delta L$ or $L_0$ left.
- L1-09: $\Delta l = \alpha l_0 \Delta T = 12 \cdot 10^{-6} \cdot 25 \cdot 50\,\text{m} = 15\,\text{mm}$, the same as answers.py. The linear model holds for a solid over $50\,\text{K}$, with two significant figures.
- L2-09: $k = 3.0/50 = 0.060\,\text{mm/K}$ and $T = 20 + 2.0/0.060 = 53.3\,{}^\circ\text{C}$, the same as answers.py. The $3\,\%$ tolerance is the stated range $51.7\ldots54.9\,{}^\circ\text{C}$.
- The figure's end points, (20 °C; 0 mm) and (70 °C; 3.0 mm), lie on grid intersections, and the description gives the same values without the answer.
- Both solutions are complete: the seven parts are there, the unknown is solved in symbols first, and the reasonableness checks are real checks.
- The hash was the same at the start and at the end.
