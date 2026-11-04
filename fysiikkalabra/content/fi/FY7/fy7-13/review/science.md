VERDICT: PASS
CONTENT-HASH: b6c0f58ebdd909c0

## Blocking

## Polish
- content/fi/FY7/fy7-13/lesson.md:316 — "Hilan kirkkaat maksimit syntyvät samoihin suuntiin kuin kaksoisraon kirkkaat juovat" holds only for the same slit spacing — add "kun rakojen väli on sama".
- content/fi/FY7/fy7-13/lesson.md:318 (figure "pattern") — both curves are normalised to their own maximum, yet the alt text calls the grating peaks "korkeita" (really 16 times brighter) — say each curve is normalised to its own maximum, or drop "korkeita".
- content/fi/FY7/fy7-13/inquiry.json:19 — hook: "tasavälisiä" dots on a flat wall is a small-angle approximation (x = L tan θ); true for a coarse film (about 100 lines/mm), not for 600 — optionally "lähes tasavälisiä".
- lessons/FY7/fy7-13/lesson-answers.py:33-35 — keys "setup-x1/x2" compute 300 lines/mm, 650 nm while the "setup" figure is 600 lines/mm, 532 nm (covered by koe2-*-532); rename or drop. Comments at :47 and :51 say 11,25° and 15,67°; the values are 11,245° and 15,664° (the inquiry's 11,24° and 15,66° are right).
- Slot täsmennys names thin films; not treated here — confirm the thin-film chapter covers it.

## Checked
- All numeric answers recomputed in one script with my own formulas (koe-1 650 nm, koe-2 18,61°, mittaus 532,7 nm with range 529,7–535,7 nm and k = 1 range 526–536 nm, siirto 61,45°, tarkistus-2 36,09°) and every listed mistake value (705,9; 17,70; 1065; 932; 562; 23,97; 41,30; 17,13): all agree.
- Worked example: tan θ = 0,198, θ = 11,20°, λ = 647 nm; tangent check 660 nm; 7 steps, symbolic first.
- Grating equation, d = 1 mm : N, k_max condition (kλ < d, edge case explained), tan θ = x : L with the sine-vs-tangent warning: correct and consistent across theory, sim calc box, summary and checks.
- DVD/CD as reflection gratings: perpendicular incidence stated; result independent of the polycarbonate's refraction.
- Figures: "white" to scale (rays 6,88° and 12,12°; screen 555,5 px/m gives x = 12,1/21,5 cm, k = 2/3 overlap right); "setup" x/L = 0,337; "geometry" right angle and Δs = d sin θ correct; "pattern" curves match cos²(πu) and the 8-slit formula (max error 0,007/0,024).
- Sim: implements the lesson's model, screen ±0,90 m, limits stated (one wavelength, brightness illustrative, no slit width); simState gives theta1, x1, x2 at every experiment's initial values; each experiment locks the other two parameters.
- Predictions: exactly one correct option each; every distractor's feedback names the right physics.
- Diffraction, coherence, Young's dark fringes and the exit ticket: correct mechanism, consistent with the theory.
