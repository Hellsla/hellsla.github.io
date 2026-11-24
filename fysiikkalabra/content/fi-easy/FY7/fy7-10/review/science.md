VERDICT: PASS
CONTENT-HASH: d7ae202c216bd3fb

## Blocking

## Polish
- assets/sims/fy7/fy7-10/sim.js:1025 — the reflected beam is always drawn with width at least 1.5 and alpha 70, even when R = 0 (same material above and below, so no interface at all). A faint reflected ray then shows that the 0 % readout contradicts. — Skip the reflected beam, or fade it to zero, when R is about 0 (for example when m1 = m2).
- lessons/FY7/fy7-10/lesson-answers.py:900 — the comment says 0,674, but 1/A = 0,6714 (the printed value and the inquiry mistake 0,671 are right). — Correct the comment.
- inquiry.json `nopeus` hint 3, `siirto` hint 3, `tarkistus-2` hint 3 — a stray "." after the display block. — Remove it.
- lesson.md:174 — "Mitä suurempi on taitekertoimien ero" is fine at this level (C). Snell's law uses the ratio n₂ : n₁, so "suhde" would be more exact. Optional.

## Checked
- One script recomputed every number from the task data: worked example 38,0° / 2,26·10⁸ m/s, pysähdy 25° and 1,24·10⁸ m/s, graph end points 48,8° / 24,4°, koe-1 (14,9; 22,1; 28,9; 40,6; 47,8°; angle ratios 1,36 / 1,48; 1,84-fold), koe-2 (35,2; 30,9; 30,3; 18,5°), mittaus fit A = 1,4895, B = −0,0041, ΔA = 0,016, nopeus 2,01, siirto 41,7° with mistakes 25,9 / 22,1 / 39,9, tarkistus-2 1,47 with mistakes 0,680 / 1,59, exit 25° / 50° / 1,33. Every value agrees with lesson-answers.py.
- Fresnel R in the sim is correct for unpolarised light (2,0 % / 2,4 % / 35 % for air to water at 0°, 40°, 80°). R rises steadily with the angle of incidence for every pair of materials tested, so "suurempi tulokulma, suurempi osa heijastuu" holds. The 4 % and 2 % at normal incidence are right.
- Sim: tir when n₁ sin α₁ > n₂, β = α₁, T = 1 − R. simState holds beta, alpha2, sin1, sin2 and n2. The koe-1 setup locks m1 and m2 and varies alpha; koe-2 locks m1 and alpha and varies m2. The model box states every assumption.
- Mittaus: the half-cylinder geometry is correct (radial ray, no second refraction). The example data fits n = 1,49 to within 1°. The slope n₂ : n₁, the line through the origin, the reading point (0,60; 0,89) and the rounding to ±0,02 are right.
- Every correct option is right and is the only right one (kertaus, ennuste-1, ennuste-2, virhe, check-1), and each distractor's feedback is correct.
- Causality: wavefronts slow down and turn, the frequency is fixed by the source, λ shortens by 1,33. The apparent-depth and straw explanations are consistent across the theory, the model answer and the criteria.
- Figures checked: the interface figure (50° to 35°), the wavefront figure, the depth figure and the fit plot agree with the text. The graph polylines are checked at α₁ = 45° and 90°.
- In scope: reflection and refraction from LOPS FY7. Brewster and total internal reflection are only referred forward.
