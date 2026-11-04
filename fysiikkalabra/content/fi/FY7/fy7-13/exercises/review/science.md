VERDICT: PASS
CONTENT-HASH: 5fe3cd0bf7cda970

## Blocking

## Polish
- content/fi/FY7/fy7-13/exercises/solutions.md:55 — L2-01 Kaava writes k ≤ d : λ while Periaate says kλ < d; use kλ < d in both (equality gives no spot on the screen, as the lesson says).
- content/fi/FY7/fy7-13/exercises/solutions.md (L1-03 Järkevyys) — 625 nm is red rather than "oranssinpunainen"; harmless.

## Checked
- All 12 answers recomputed with my own formulas in one script; all match exercises.json and answers.py (relative difference below 2 · 10⁻⁵).
- L2-01: d : λ = 3,70, k = 3 at 54°, k = 4 impossible: 7 spots; "leveä varjostin" makes all reach the screen.
- L2-03, L3-02: half the spot-to-spot distance used as x; tan then sin, never tan ≈ sin at 18–24°.
- L2-04: spectrum edges 12,09 cm and 21,48 cm, width 9,39 cm; proportionality check 44 % right.
- L3-01: 3λ₃ = 2 · 700 nm, grating-independent; overlap of orders 2 and 3 and no overlap of 1 and 2 argued correctly.
- L3-02: reflection-grating model with perpendicular incidence stated; 1,6 µm agrees with IEC 60908; two significant figures justified by 89 mm; orders k = 1, 2 only (d : λ = 2,46) right.
- L3-03: calibration d = 3,330 µm from the red laser, then λ = 532,6 nm; reasoning valid.
- Every solution has the seven steps, the unknown solved symbolically before substitution, conversions right, rounding justified by the limiting datum.
- Scope: within FY7 "valon interferenssi ja diffraktio" and the lab "laserin aallonpituuden määrittäminen hilan avulla".
