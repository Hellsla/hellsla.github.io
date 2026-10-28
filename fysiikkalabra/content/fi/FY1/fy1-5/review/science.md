VERDICT: PASS
CONTENT-HASH: da2cc58228b58e6a

## Blocking

## Polish
- lesson.md:172 and inquiry.json:382 (tarkistus-3 model) — the stated causes of the 0,2 AU gap are small: solar deceleration shifts the distance by ≈ 0,06 AU (½aT², a ≈ 3,5·10⁻⁷ m/s²) and makes the model overshoot only if 15,341 km/s is the 2018 speed; s₀ rounding is ±0,05 AU. "Osin" keeps it defensible — also name input uncertainty (speed epoch, JPL's exact date).
- inquiry.json:314 (siirto, Järkevyys) — `6 · 45 ≈ 270 m` repeats the substitution rather than checking it — use an independent estimate (360 m per minute → just under 300 m in 45 s).
- lessons/FY1/fy1-5/sim-spec.md — still Δs/Δt and s/t (round 1 polish); not student-facing, but align with the colon rule.

## Checked
- Round-1 blocker fixed: siirto hint 3 (:302) and mistake 1092 feedback (:307) now `(21,6 : 3,6) m/s = 6,0 m/s`, unambiguous.
- Notation sweep (lesson.md, inquiry.json, exit-ticket.json, sim.js): no ×/\times; products \cdot (8 · 365 + 2, 2,18 · 10¹⁰); operation divisions with `:` (s : t, Δs : t, 10 : 2,0, 12 m : 4,0 s); slashes only in unit fractions (m/s, km/h, AU/vrk, km/AU).
- Worked example recomputed: 2922 d, v = 1 325 462 km/vrk = 0,0088602 AU/vrk, Δs = 25,89 AU, s = 145,59 → 145,6 AU = 2,18·10¹⁰ km; rounding by the addition rule; symbolic first.
- Reasonableness: 15 km/s · 3,16·10⁷ s = 4,7·10⁸ km ≈ 3,2 AU/a; model 15 Feb 2026 = 143,26 AU vs 143,05 AU, 0,21 AU = 0,15 % (< 0,2 % as stated).
- Misconception / ennuste-2: 6 m + 2 m/s → 10 m, 14 m (not 20 m), Δs 4 → 8 m; ennuste-1 values 4,0/8,0 m.
- koe-1/koe-2 quotients (2,0 m/s; 5,0 and 3,5 m/s vs Δs : t = 2,0 m/s); experiments lock s₀ and v, vary t; simState gives s and ds; values within the 0–60 m track.
- Etsi virhe 23 m (not 33 m), siirto 390 m (mistakes 1092, 270), tarkistus-2 s₀ = 4,0 m (mistakes 7, 3), exit ticket 17 m, 29 m (not 34 m), Δs = 12 m, v = 3,0 m/s, s₀ = 8 m: all correct.
- Figures to scale: (t, s) graph slopes 3 m/s, s₀ = 5 m, parallel, triangle 2 s / 6 m; motion figure equal 115 px steps.
- sim.js implements s = s₀ + vt; slope triangle 2–6 s with Δt = 4,0 s matches the calc box; assumptions stated.
