VERDICT: PASS
CONTENT-HASH: 2d23734e5911e5bb

## Blocking

## Polish

## Checked
- Round 2: the only lesson change since cb4b8f4 is exercises.json:82, now "kokonaispaine (ei ylipaine) 300 kPa"; with absolute pressure p ∝ T holds and 300 · 308,15/288,15 = 320,8 ≈ 321 kPa; round-1 polish item fixed.
- T = θ + 273,15, ΔT = Δθ, 0 K with kinetic energy "pienimmillään"; p ∝ T at constant V and n with conditions stated; inside FY3 scope.
- Worked example: ideal-gas table 100 → 136,6 kPa; k = 0,37 kPa/°C, θ = −p₀/k ≈ −270 °C, symbolic first.
- Figures unchanged: kelvin scale to scale; extrapolation graph points match the table, line reaches p = 0 at −270 °C; micro-model labelled schematic.
- answers.py unchanged since round 1: all 12 matched; exercise data physically consistent.
- solutions.md unchanged: conversions and proportions set up symbolically first.
- Simulation unchanged: v ∝ √T, pressure from wall impulses averaged over both axes; Python port gave 104/50/194/54/202 vs theory 100/50/200/50/200 (statistical scatter); limits stated.
- exp-1 varies T at fixed V, exp-2 varies V at fixed T; simState carries vRel, pRel, pTheory.
- Predictions: 300 → 600 K doubles p, speed ×1,41; halving V doubles p.
- virhe 128 kPa, siirto 122 kPa, check-2 −273 °C, exit ticket 3,5 % and −273 °C.
