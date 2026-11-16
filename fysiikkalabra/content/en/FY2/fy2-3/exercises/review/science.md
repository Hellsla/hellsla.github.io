VERDICT: PASS
CONTENT-HASH: 05fd3289498b07ef

## Blocking
(none)

## Polish
(none)

## Checked
- L2-09 (FY2-A4): E = P Δt = 2.0 kW · 4 h = 8.0 kWh, C = hE = -40 snt; +15 snt/kWh gives 120 snt, difference 160 snt; margin 0.41 · 8.0 = 3.28 snt ≈ 3.3 snt; credit 40 is a third of 120. My recomputation, answers.py and exercises.json agree.
- Symbolic C = hPΔt before substitution; 4 h stated exact, two s.f. from 2.0 kW and -5.0 snt/kWh; reasonableness and model limits (steady power, same hourly price) stated.
- Article values (0.41, 0.25, 0.50 snt/kWh; negative price when production exceeds consumption; Vaasan sähkö counts negative hours as zero) and Fingrid's "without taxes and transmission costs" match docs/audits/2026-11-16-fy2-aineistot.md.
- d) storage losses worded per guardrail P1 (internal energy, transferred to the surroundings as heat).
- Compared with the Finnish: answer, unit, tolerance, level and every number identical (only date formats differ).
- Scope: P = E/t and energy cost, inside FY2. No guardrail break.
