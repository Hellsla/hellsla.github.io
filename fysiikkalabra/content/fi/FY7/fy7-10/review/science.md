VERDICT: PASS
CONTENT-HASH: 8627fcebb3296c19

## Blocking

## Polish
- lesson.md:51 — "Mitä suurempi on taitekertoimien ero, sitä enemmän säde taittuu" holds in general only for the ratio n₂ : n₁, not the difference (with the sim's five materials the order happens to agree, but e.g. 2,00 → 2,42 differs more than 1,00 → 1,33 and bends less) — write "mitä enemmän taitekertoimet poikkeavat toisistaan (suhde n₂ : n₁)" or "mitä suurempi on taitekertoimien suhde". (B, minor)
- inquiry.json:445 (tarkistus-3) — "katsotaan sivulta vinosti ylhäältä": seen from the side, light from the straw also crosses the glass wall (as the photo caption says), while the model answer and criteria use only the water surface; align with lesson.md "vinosti ylhäältä vedenpinnan läpi".
- lessons/FY7/fy7-10/lesson-answers.py:54 — comment says 0,674; 1 : 1,4895 = 0,671 (the mistake value 0,671 in inquiry.json is right).

## Checked
- Recomputed in one script with my own formulas every number of lesson.md, inquiry.json and exit-ticket.json: worked example (0,6159; 38,0°; 2,26·10⁸ m/s), pysähdy items (2,26·10⁸, 1,24·10⁸ m/s, 25°), misconception 22,1°/40,6°/44,2°, koe-1 and koe-2 values, sine and angle ratios 1,33 / 1,36 / 1,48, ennuste feedback, siirto 41,7° (and 25,9°, 22,1°, 39,9° mistakes), tarkistus-2 1,47 (0,680, 1,59), nopeus 2,01 (4,47), exit 25°/50°, 1,33: all agree with lesson-answers.py.
- Mittaus: own least-squares fit gives A = 1,4895, B = −0,0041, ΔA = 0,0162; single-row ratios 1,42 and 1,49; read-off point (0,60; 0,89) on the line; data consistent with n = 1,49 rounded to 1°; half-cylinder geometry (radial exit, no refraction at the curved face) correct; guardrail fit sentence present.
- Partial reflection 4,3 % (glass) and 2,0 % (water) at normal incidence; unpolarised Fresnel R checked monotonic in θ for air→water, air→diamond and water→air, so "larger angle, larger share" holds.
- Graph polylines to scale (end points 48,8° and 24,4°); interface, wavefront and apparent-depth figures show the right bending, shorter λ₂ and the image raised.
- sim.js: β = α₁, Snell, TIR when n₁ sin α₁ > n₂, Fresnel rs/rp correct, T = 1 − R; arcs and rays drawn in the right directions; simState holds alpha, m1, m2, beta, alpha2, sin1, sin2, n2 for both experiments; model box states 589 nm, no absorption, unpolarised, model values.
- Experiments: koe-1 locks both materials and varies α₁; koe-2 locks m1 and α₁ = 50°, varies m2.
- Choice items: exactly one correct option each (kertaus, ennuste-1, ennuste-2, virhe, check-1); every distractor's feedback correct.
- Causality: refraction from speed change via wavefronts; frequency fixed by the source, λ shortens; apparent depth via back-extended rays.
- Scope: reflection and refraction within FY7; Fresnel only in the sim's calc box, marked outside the syllabus; TIR, dispersion, polarisation referred to their chapters.
- Refractive-index table values (CRC) and air 1,0003 correct.
