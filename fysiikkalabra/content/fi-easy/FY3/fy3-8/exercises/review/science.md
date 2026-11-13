VERDICT: PASS
CONTENT-HASH: 65f7b748b1e5d4e4
SCOPE: delta added-exercise from 3ce9e680342bf801 base 5453544b2abc

## Blocking
- none

## Polish
1. lessons/FY3/fy3-8/answers.py:2,300-301 — the docstring and comments still say ΔL and L₀; rename them to Δl and l₀ (noted last round too).
2. content/fi-easy/FY3/fy3-8/exercises/exercises.json:117 (L1-09) — the task says "pituuden lämpölaajenemiskerroin" (MAFY's table name). Say once that this is the lesson's pituuden lämpötilakerroin $\alpha$, so the S2 reader links the two names.

## Checked
- The hash changed during the review (the packet's 6013df691366c118 became 65f7b748b1e5d4e4), so I reviewed again. The working-tree diff only renames ΔL, L₀, ΔL_koko to Δl, l₀, Δl_koko in L2-09's text (exercises.json:305) and in both added solutions (solutions.md:212-226). No number changed, and the diff is entirely inside the added exercises.
- The notation now matches the lesson, the other exercises and the figure axis $\Delta l\ (\text{mm})$.
- L1-09 recomputed: $\Delta l = \alpha l_0 \Delta T = 12 \cdot 10^{-6} \cdot 25 \cdot 50\,\text{m} = 15\,\text{mm}$, and answers.py gives 15,0. Steel's α in MAFY is 12·10⁻⁶ 1/K. The ±4 % tolerance covers differences between tables. ΔT = 50 K is within the roughly 100 K range where the linear model holds.
- L1-09: two significant figures (from 25 m and 50 K) and the reasonableness check (1,2 mm per m per 100 K) are right.
- L2-09 recomputed from the figure, (20 °C; 0) to (70 °C; 3,0 mm): $k = 0{,}060\,\text{mm/K}$ and $T = 20 + 2{,}0/0{,}060 = 53{,}3\,{}^\circ\text{C}$. answers.py gives 53,333.
- L2-09 tolerance: 3 % gives 51,7–54,9 °C, as the solution states, and the rounded answer 53 °C is inside it.
- L2-09 figure: both end points are on grid crossings, the description gives the same values, and neither gives the answer away. The proportionality is justified by the points lying on a line.
- The other 21 exercises are unchanged since the version passed (per the packet), so I did not review them again.
- Hash checked again at the end: 65f7b748b1e5d4e4.
