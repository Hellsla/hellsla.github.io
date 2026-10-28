VERDICT: PASS
CONTENT-HASH: 54faa4daccae4100

## Blocking

## Polish
- lesson.md:172 and inquiry.json:382 (tarkistus-3 model) — the stated causes of the 0,2 AU gap (solar deceleration ≈ 0,06 AU, s₀ rounding ±0,05 AU) do not cover it alone; "osin" keeps it defensible — also name input uncertainty (speed epoch, JPL's exact date).
- inquiry.json:314 (siirto, Järkevyys) — `6 · 45 ≈ 270 m` repeats the substitution — use an independent estimate (360 m per minute → just under 300 m in 45 s).
- lessons/FY1/fy1-5/sim-spec.md — still Δs/Δt and s/t (not student-facing); align with the colon rule.

## Checked
- Round-3 change, lesson.md:129 Yksiköt: 1 km = 1000 m, 1 h = 3600 s substituted, 72 · 1000 m : 3600 s = 20 m/s — correct, units carried, \cdot product.
- lesson.md:181 Tiivistelmä: conversion by substitution, no 3,6 factor left.
- inquiry.json:299/302/307/314 (siirto hints, mistake 1092 feedback, solution): 21,6 · 1000 m : 3600 s = 6,0 m/s; s = 120 m + 6,0 m/s · 45 s = 390 m; no "jaa 3,6:lla" rule remains in student text.
- Notation sweep of the changed lines: \cdot only, no ×/\times; unit fractions as \dfrac with units in numerator and denominator.
- Worked example unchanged: 2922 d, 0,0088602 AU/vrk, Δs = 25,89 AU, s = 145,6 AU = 2,18·10¹⁰ km; 15 Feb 2026 model 143,26 AU vs JPL 143,05 AU (0,15 %).
- Misconception, ennuste, koe-1/2, Etsi virhe 23 m, tarkistus-2 s₀ = 4,0 m, exit ticket: unchanged since round 2 PASS, still correct.
- Figures and sim.js untouched; s = s₀ + vt, slope triangle 2 s / 6 m to scale.
- Hash identical at start and end.
