VERDICT: PASS
CONTENT-HASH: 0bbd2756f9f41784

## Blocking

## Polish
- lesson.md:210-225 — the Kaava SVG writes "p = p₀ + ρgh" and "ilmanpaine p₀" as plain SVG text — use LaTeX in foreignObject like the Ydinajatus figure (form rule, not physics).
- lesson.md:191 / inquiry.json pred-2 — "noste" is in the curriculum slot's glossary list but is only named in a feedback line and never defined — either define it in one sentence or drop it from the slot.
- lesson.md:228 — "huoneessa on ilmaa normaalipaineessa" (101,325 kPa) is equated with the surface p₀ = 101 kPa — say "samassa ilmanpaineessa kuin pinnalla" so the cancellation is exact.
- solutions.md fy3-4-L1-02 — substitution ends "≈ 932 kPa", answer 930 kPa — round once, to the 2 s.f. the 95 m gives.

## Checked
- All 12 answers recomputed independently; equal to answers.py, stored values within 0,93 % (tolerance 2 %).
- Worked example: ρgh = 117,72 kPa, p ≈ 219 kPa, F = 1,77 kN ≈ 1,8 kN; overpressure-only reasoning for the window correct; symbolic before substitution.
- Dam claim 30 m → 294 kPa ≈ 290 kPa; 10 m ≈ 1 atm.
- pred-1 (150 → 199 kPa, ×1,33), pred-2 (98 → 122 kPa, 199 → 223 kPa, +12 %), pred-3 correct options and all feedback numbers.
- exp-1/exp-2: initial values, locked/varied params isolate the variable; simState has h, rho, pOver, pTotal; slider steps reach 720/1000/1240; exp-1 answer 9,81 kPa and mistakes 9810, 19,9.
- Transfer (barometer 0,757 m; mistakes 10,3 m, 0,000757 m), check-2 (892; 2180, 0,892), virhe (29 kPa), check-3 model (29 kPa, ≈1,8 N on 0,6 cm²), exit ticket (49/150 kPa).
- Solutions L1–L3: physics, unit conversions (cm², bar, MPa), two-layer sum, Pascal's barrel ΔF = ρghA.
- sim.js: pOver = ρgh/1000, pTotal = p₀ + pOver, slope ρg, overpressure mode drops intercept; screenshot shows line 101 → 297 kPa over 0–20 m, reading 199 kPa at 10 m.
- Kaava SVG: 199 kPa plotted at y=52 vs exact 53 (fine); Ydinajatus SVG derivation G = ρAhg, p = ρgh.
- Scope: p = F/A and p = p₀ + ρgh only, force as scalar normal to surface, matches FY3 slot.
