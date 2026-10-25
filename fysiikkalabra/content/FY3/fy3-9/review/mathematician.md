VERDICT: FAIL
CONTENT-HASH: 4bb4ef0158a6961f

## Blocking
1. lesson.md:37 — the right panel (1/V, p) has 6 points, but the left panel (lesson.md:31) has 8, and the aria-label (lesson.md:27) says both come "samoista mittauksista". The points p = 2 and p = 4 are missing from the line (figure units, pV = 5). The 6 points that are drawn are correct and to scale. — Add `<circle cx="417.2" cy="170" r="5" fill="currentColor"/>` and `<circle cx="504.4" cy="90" r="5" fill="currentColor"/>`. Both lie exactly on the drawn line.

## Polish
1. lesson.md:30 — the `Q … T` Bézier misses three points by 3–5 px and strays up to 5,4 px from p = k/V. — Replace it with a polyline sampled from y = 250 − 8360/(x − 50).
2. lesson.md:52 — "noin kolmanneksella" overstates the growth: 1,036/0,80 = 1,30. "1,04 l" has 3 figures, but the answer is given as 1,0 l. — Write "noin 30 %" and drop "1,04 l".
3. solutions.md:45 — the intermediate "2020 l" is already rounded (2019,8 l). — Write "≈ 2020 l".
4. lesson.md:19 — p = k · (1/V), which L2-03 and the figure use, appears only in prose. — Optionally add the display line `p = \frac{k}{V}` with k = pV.

## Checked
- SVG: the left points give pV = const (0,1 % spread). The right points lie on the drawn line (slope 0,917). Both panels use the same p scale.
- L2-03: the 1/V column is correct. pV = 1980–2030 kPa·ml. The least-squares slope through the origin is 2,01 J, so 2,0 J. Hand fits land at 1,98–2,03 J, inside tolerance 0,05. 1 kPa·ml = 10⁻³ J.
- All solutions L1-01 … L3-03 recomputed, including the sanity-check figures.
- Gauge versus absolute pressure (L3-02, L3-03) and the cancelled area A are correct.
- The inverse-proportionality statements (lesson.md:8, 10, 19, 55, 59–60) are correct.
- Misconception +3,5 %, exit ticket 160 kPa and 308/280 = 1,10, example 1,0 l.
- θ and T = θ + 273,15 K follow fy3-3.
- Lint: 0 errors. `check_layout.py`: OK at 360 px.
