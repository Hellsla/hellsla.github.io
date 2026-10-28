VERDICT: FAIL
CONTENT-HASH: e78dc963eb683250

## Blocking
- inquiry.json:302 (siirto, hint 3) and inquiry.json:307 (mistake 1092 feedback) — the colon replacement made `$v = 21{,}6 : 3{,}6\,\text{m/s}$` ambiguous: it reads as 21,6 divided by 3,6 m/s (= 6,0 s/m) — write `$v = (21{,}6 : 3{,}6)\,\text{m/s} = 6{,}0\,\text{m/s}$` or `\tfrac{21{,}6}{3{,}6}\,\text{m/s}` as the solution does.

## Polish
- lessons/FY1/fy1-5/sim-spec.md — still writes Δs/Δt and s/t; not shown to students, but align with the colon rule.

## Checked
- Worked example: v = 0,0088602 AU/vrk, Δs = 25,89 AU, s = 145,59 → 145,6 AU (2,18·10¹⁰ km); 2922 days incl. leap days 2020, 2024.
- Reasonableness check: 3,16 AU/yr; model 15 Feb 2026 = 143,26 AU vs JPL 143,05 AU, difference 0,21 AU = 0,15 % — text correct.
- Misconception example (6 m, 2 m/s: 10 m, 14 m; matka 4 → 8 m), ennuste-1/2 feedbacks, koe-1/2 quotients (5,0 and 3,5 m/s vs 2,0 m/s), Etsi virhe 23 m, siirto 390 m (mistakes 1092, 270), tarkistus-2 4,0 m (7, 3): all correct.
- (t, s) figure to scale (slope 3 m/s, s₀ = 5 m, triangle 2 s / 6 m); motion figure equal spacing.
- sim.js implements s = s₀ + vt, ranges fit the 60 m track, slope triangle 2–6 s correct; assumptions (no friction, constant speed, model values) stated.
- Exit ticket: 17 m, 29 m (not 34 m), Δs = 12 m; 3,0 m/s and s₀ = 8 m.
- Notation: no ×/δ; other colon divisions unambiguous.
