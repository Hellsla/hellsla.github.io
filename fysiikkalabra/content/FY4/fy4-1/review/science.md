VERDICT: PASS
CONTENT-HASH: d1e3f3544f8c599a

## Blocking
(none)

## Polish
- solutions.md fy4-1-L2-01 — the task asks for "matka" but the solution names it "siirtymä $\Delta x$"; equal here (one direction), but in a lesson built on matka ≠ siirtymä write $s = v\,\Delta t$ or say why they coincide.
- inquiry.json simulaatio `model` — "Kitkaa … ei huomioida" is unnecessary for carts that simply keep a constant velocity (forces are not in this lesson); "Kärryjen nopeus on vakio" says the assumption without inviting a force question.

## Checked
- One Python run recomputed all 12 exercises and 12 inquiry/example numerics; answers.py matches (8,0 / −17 / 42 / 2,0 / 45 / 300 / 5,0 / −3,0 / 16 / 4,0 / 50 / 0,25; 4,0, −3,0, 1,49, 39, 13, 2,5, 170, 16) and stated answers are within tolerance.
- Formulas Δx = x₂ − x₁, v_ka = Δx/Δt, x = x₀ + vt with symbols and the t = 0 condition; vector vs. component notation stated; within FY4 "tasainen suoraviivainen liike".
- Displacement figure to scale (40 px/m: 2→8 m = +6 m, 8→3 m = −5 m); jogger graph to scale (20, 120, 170 m at 0, 40, 60 s).
- Worked example symbolic first, 2,5 m/s ≈ 9 km/h, 170 m with independent check.
- Robot data: least-squares slope 1,494 m/s, intercept 4,10 m; drawn line (0; 4,1)–(10; 19,1) and all six points at the right pixels; residuals ±0,3 m on both sides; answer 1,5 with 3 % tolerance; mistakes 1,91 / 1,3 / 0,67 correct.
- Predictions: model values A 2 m/s, B 4 m/s, C x₀ = 20 m, D x₀ = 30 m, v = −3 m/s, A and D meet at 6 s, 12 m — all feedback numbers match sim.js CASES.
- Experiments lock `tapaus`, vary `t`; simState exposes xA and x2 at the slider's 0,5 s steps; exp-1 4,0 m/s, exp-3 −3,0 m/s.
- Round trip E: 8 m out, 2 s stop, back to 0 at 10 s; path 16 m, v_ka = 0; graph vertices at the right times; keskivauhti 1,6 m/s distinguished correctly.
- sim.js pos/vel/path correct for all four cases; arrows scale with signed v; implements the lesson's model, limits stated.
- Etsi virhe, siirto (39 m, mistakes 50/74/5,0), check-2 (13 m) and exit ticket correct; hash identical at start and end.
