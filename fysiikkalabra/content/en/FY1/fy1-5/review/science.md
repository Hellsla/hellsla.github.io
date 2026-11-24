VERDICT: PASS
CONTENT-HASH: 149d9f8c6d577024

## Blocking

## Polish
- content/en/FY1/fy1-5/lesson.md:202 (and inquiry.json hook, tarkistus-3 model) — "the speed of the probe relative to the Sun at the crossing was 15.341 km/s": 15.341 km/s is JPL's current (2026) heliocentric speed (packet scope note); at the 2018 crossing it was about 15.4 km/s (the lesson's own "slows by about 0.1 km/s over 2018–2026" implies this). Fix: "The probe's speed relative to the Sun is now $v = 15.341\,\text{km/s}$ (NASA/JPL)" or drop "at the crossing".
- content/en/FY1/fy1-5/lesson.md:202 — $s_0 = 119.0\,\text{AU}$ (Burlaga et al. 2019, a correct peer-reviewed value) differs from the course brief's 119,7 AU; if *Units and prefixes*/fy1-2 shows 119,7 AU, one sentence should say why the chapters differ (guardrails "Numbers agree between chapters").
- assets/sims/fy1/fy1-5/sim.js:776 — the readout writes a decimal comma ($2{,}0$) on the English page too (screenshot koe-2); not physics, for the visual reviewer.

## Checked
- One script recomputed: worked example v = 0.0088602 AU/day, 2922 days, s = 144.89 AU ≈ 2.17·10¹⁰ km; reasonableness 3.2 AU/yr; Feb 15 2026 model 142.56 AU, difference 0.49 AU; solar deceleration over 2018–2026 integrated ≈ 0.09 km/s ("about 0.1 km/s" right).
- Siirto 390 m, mistakes 1092 and 270 m; tarkistus-2 v = 3.0 m/s, s₀ = 4.0 m, mistakes 7 and 3; predictions 14 m (distractors 20, 12 m), virhe 23 vs 33 m; exit ticket 30 km and 10 m; pysähdy 18 m, 25 m/s, 72 km/h = 20 m/s.
- Exactly one correct option in every choice item; every distractor's feedback states the right reason (kertaus slope Δt:Δs on an (s,t) graph; horizontal (t,s) line = rest).
- Graph figure is to scale (68.8 px/s, 9.6 px/m): lines 3 m/s through 0 and 5 m, triangle Δt = 2 s, Δs = 6 m.
- Distance-from-Earth vs distance-from-Sun caveat (≤ about 1 AU) stated in the worked example and the tarkistus-3 model answer; comparison conclusion sound.
- sim.js implements s = s₀ + vt, ds = vt; slope readout (pos(6) − pos(2))/4 s = v; ranges fit the 0–60 m track (10 + 5·10 = 60).
- Experiments: s₀ and v locked, t varied on a 0.5 s slider (2, 4, 8 s reachable); simState gives s and ds; koe-2 starts at s₀ = 6 m (screenshot).
- Model box states its assumptions; model values named as such; scope stays at s = s₀ + vt.
- Hash identical at start and end.
