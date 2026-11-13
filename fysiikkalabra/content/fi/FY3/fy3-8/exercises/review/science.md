VERDICT: PASS
CONTENT-HASH: 57f3663372e291af
SCOPE: delta added-exercise from bd98847c91c69f13 base 5453544b2abc

## Blocking
- none

## Polish
1. content/fi/FY3/fy3-8/exercises/solutions.md:210–229 and exercises.json:117, 303 — the added tasks write ΔL, L₀, while the lesson, the other tasks and the figure's axis (fy3-8/length-graph) use Δl, l₀ — use Δl, l₀ (or say why MAFY's symbol differs).
2. exercises.json:117 — "pituuden lämpölaajenemiskerroin" is MAFY's table name; the glossary term is *pituuden lämpötilakerroin*. Keeping the table name in the hint is fine, but the question could name the glossary term once as well.

## Checked
- L1-09: ΔL = αL₀ΔT = 12·10⁻⁶ 1/K · 25 m · 50 K = 0,015 m = 15 mm; answers.py 15,0, which matches. Two significant figures are right (25 m, 50 K). A ±4 % tolerance covers a table value of 11,5…12,5 · 10⁻⁶ 1/K.
- L1-09: a solid over 50 K is inside the linear model's range (under 100 K); the rail is steel, so it uses the right table row.
- L2-09: from the figure, (20 °C; 0 mm) to (70 °C; 3,0 mm) gives k = 0,060 mm/K, ΔT = 2,0 mm / k = 33,3 K, T = 53,3 °C. answers.py gives 53,33, which matches. ±3 % is 51,7…54,9 °C, the same range as the solution states.
- L2-09: the solution solves ΔT symbolically before substituting. It explains why adding K to °C is valid (a temperature difference). The reasonableness check (two thirds of the range) is a real independent check, and the result is inside the measured range, so there is no extrapolation.
- Figure: its description and its code give both end points and the grid spacing. The task can be solved from them, and neither gives away the answer or α.
- Both tasks are inside FY3's central content (lämpölaajeneminen) and need nothing the lesson does not teach.
