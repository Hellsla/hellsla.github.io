VERDICT: FAIL
CONTENT-HASH: 6013df691366c118

## Blocking
- content/fi-easy/FY3/fy3-8/exercises/exercises.json:305 and solutions.md:213-229 — the two added exercises still use $\Delta L$, $L_0$, $\Delta L_\text{koko}$, while the lesson (after the MAFY notation change), every other exercise and solution, and the figure `fy3-8/length-graph` it shows (axis $\Delta l\ (\text{mm})$) use $\Delta l$, $l_0$. In L2-09 the task text names the quantity $\Delta L$ and its own graph labels it $\Delta l$ (category 6, internal consistency; this round's purpose was to bring the added tasks onto the merged notation) — write $\Delta l$, $l_0$, $\Delta l_\text{koko}$ in L2-09's text and in both solutions (Kysytty, Periaate, Kaava, Sijoitus, Annettu).

## Polish
1. lessons/FY3/fy3-8/answers.py:2,300-301 — docstring and comments still say ΔL, L₀; rename to Δl, l₀ (noted last round too).
2. exercises.json:117 (L1-09) — the task says "pituuden lämpölaajenemiskerroin" (MAFY's table name); add once that it is the lesson's pituuden lämpötilakerroin $\alpha$, so the S2 reader links the two names.

## Checked
- L1-09: $\Delta l = \alpha l_0 \Delta T = 12 \cdot 10^{-6} \cdot 25 \cdot 50\,\text{m} = 15\,\text{mm}$ (own script; answers.py 15,0); steel α from MAFY is 12·10⁻⁶ 1/K; ±4 % covers table differences of 11,5–12,5; ΔT = 50 K is within the about 100 K range the linear model holds for.
- L1-09 sig figs (two, from 25 m and 50 K) and the check (1,2 mm per m per 100 K) are right.
- L2-09: own reading of the figure (20 °C; 0) to (70 °C; 3,0 mm), $k = 0{,}060\,\text{mm/K}$, $T = 20 + 2{,}0/0{,}060 = 53{,}3\,{}^\circ\text{C}$; answers.py 53,333 agrees.
- L2-09 tolerance 3 % gives 51,7–54,9 °C, as the solution states; rounding to 53 °C stays inside.
- L2-09: the figure gives both end points on grid crossings, its description gives the same to a non-seeing reader, and neither gives the answer; the proportionality is justified from the points lying on a line.
- The other 21 exercises are unchanged from the version passed (packet), not re-reviewed.
- Hash the same at start and end.
