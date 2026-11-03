VERDICT: FAIL
CONTENT-HASH: d1d3324e92599f1f

## Blocking
- lessons/FY7/fy7-12/lesson-answers.py:16-17 — A: the number record says the diamond figure's back facets are at 41° to the girdle and the ray meets them at 41°. The published figure (lesson.md diamond SVG, its aria-label, its $38^\circ$ labels) and figures.py:303 use 38° (facet slope atan(98,5 : 126) = 38,0°). The record disagrees with the figure it documents — fix: `a["dia-inc1"] = 38.0` and change the comment to 38° (38° > 24,4° diamond reflects totally; 38° < 41,8° glass leaks).

## Polish
- lesson.md:159 — "kuitu viivästyttää signaalia hieman enemmän kuin pelkkä matka antaisi odottaa": the delay is 1,47 times the vacuum time (5,74 ms against 3,91 ms in siirto), so "hieman" understates it — write "noin puolitoista kertaa niin kauan kuin tyhjiössä".
- lessons/FY7/fy7-12/figures.py:58 — hit points are computed from ly = 312, but the rays are drawn from ly − 10 = 302, so the drawn incidence angles are 31,6°, 50,5° and 66,4° instead of 30°, 48,8° and 65°. The middle "α = α_r" ray is past the critical angle, yet it is drawn grazing, and the arcs do not meet the rays — compute hx with (ly − 10 − ys).
- lesson.md (Kaava graph) — the x-axis labels 1,0, 1,2, 1,6, 2,0, 2,4 skip 1,4: the spacing is uneven (taste).

## Checked
- Recomputed in one script: 41,7°, 48,8°, 80,57°, θ 10/14/15/30° → α 83,26/80,59/79,93/70,25°, α_r 42,51/63,98/80,57°, θ limit 14,03°, siirto 5,743 ms and its mistake values, virhe 40,6°, check-2 69,98°, exit 38,7°.
- Predictions: exactly one correct option each. Every distractor's feedback is right, and with air around the core every θ gives α ≥ 47,5° > 42,5°.
- koe-1 and koe-2 isolate θ and n2. simState gives alpha and alphar.
- sim.js implements the stated model. Its limits are said in the model box.
- Graph to scale (points and curve checked). Diamond figure ray-traced: 38° and 65,9° reflect totally; glass refracts out at 67,4°, as drawn.
- Worked example: 7 steps, symbolic first, 3 sig figs, a real check.
- Data: 1550 nm, about 15 km to half power (0,2 dB/km), C-Lion1 1172 km (Cinia, 2016).
- Condition n1 > n2 and the mechanism are stated the same in the theory, summary, check-1 and glossary. Within FY7 scope.
