VERDICT: PASS
CONTENT-HASH: 105250496aeacbbe

## Blocking

## Polish
- sim.js:1075 — `meas` takes the label width from `p.textWidth` of the TeX source (`$\text{ilma, } p_0 = …$`), much wider than the KaTeX output; layout only, physics unaffected — measure the rendered KaTeX box via the overlay, or a stripped string; drop the now unused `fi`.
- solutions.md:777 — writes "≈ 932 kPa" and then answers 930 kPa — round once, to the two significant figures of 95 m.
- sim.js:1007 — at h = 20 m the gauge circle is drawn centred on the floor line (half below the pool) — clamp gy to TANK.bottom − 10.

## Checked
- Formulas p = F/A, p = p₀ + ρgh correct, conditions stated (lesson, sim `model`), derivation symbolic, inside FY3 scope and the slot's line-with-intercept skill.
- answers.py and all 12 exercises recomputed independently: every answer within 0.2 % (L1-02 931.95→930, L3-03 19.03→19); units and significant figures fit the data.
- solutions.md and the staged worked example: symbolic first, then units; 117,72 kPa, 219 kPa, F = ρghA ≈ 1,8 kN (≈180 kg), 2,2 × p₀ — correct; ρgh alone on the window justified.
- Figures: brick contact areas 40 vs 120 px (A₂ = 3A₁) to scale; pressure-depth graph line 101 → 199 kPa matches axes within 1 px.
- inquiry.json numbers recomputed: pred-1 150→199 kPa (×1,33), pred-2 98→122 kPa and 199→223 kPa (+24 %, +12 %), exp-1 9,81 kPa/m with mistakes 9810 and 19,9, virhe 29 kPa, siirto 0,757 m (mistakes 10,3 and 0,000757), check-2 892 kg/m³ (mistakes 2180, 0,892), check-3 29 kPa and ≈1,8 N and the prior item; every correct option right.
- Experiments: exp-1 locks ρ and varies h, exp-2 locks h and varies ρ; 720/1000/1240 reachable with step 5; simState exposes pOver and pTotal.
- sim.js physics unchanged by the LaTeX pass (only label strings and text measuring changed): pOver = ρgh/1000, pTotal = 101 + pOver, slope ρg, chart base 0 or p₀; arrows equal in all four directions.
- tests/sims/fy3-4.json: all 22 numeric simState assertions untouched; the 4 changed ones read the same values (117,7, 218,7, 2,17, 356,1, 3,53, 0–400 kPa, h = 12,0 m, ρ = 1025 kg/m³, liquid names) from the TeX via simText — no physics check lost.
- Shots at 390/1280 px consistent (98,1 / 199,1 kPa, 1,97 × p₀, 0–300 kPa); the former sim note now in `calc`/`model` is correct.
