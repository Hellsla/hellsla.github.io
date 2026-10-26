VERDICT: PASS
CONTENT-HASH: 3c40c07fd4da8095

## Blocking

## Polish
- inquiry.json:13 (hook) — the Moon's albedo (about 0,12) is below the Earth's 0,30, so per square metre it absorbs more sunlight, not the same; its cold mean is also partly slow rotation — say "at least as much" sunlight is absorbed, which strengthens the point.
- lesson.md:6 — "laajentunut ja kevyempää" — say "harvempaa" (smaller density) rather than lighter.
- figures.py:energy_balance — the "heijastuu" arrow starts in mid-air above the atmosphere, detached from the incoming beam — start it where the incoming beam meets the clouds or the ground.
- figures.py:wall_temperature — the drops across the two boards are larger than real; acceptable in a periaatekuva.

## Checked
- Round 2 diff since the passed version (inquiry.json epatasapaino text and table header, exercises.json L3-02, exit-ticket.json item 1): every number, exponent and unit preserved in the maths conversion (5,1·10¹⁴ m², 2,6·10²⁰ kg, 4,0·10³ J/(kg·K), $\Delta T$ (K), 0,20 W/(m²K) · 50 m² · 30 K = 300 W); table renders correctly in the 390 px Tutki shot.
- answers.py run and recomputed independently in one script: all 12 answers match exercises.json within tolerance (432 W, 1,2, 30 K, 49 kWh, 238, −20 °C, 149 €, 212 kWh, 3,4, 20 K, 0,139 K, 984 kWh).
- Worked example: 734 W + 720 W ≈ 1,45 kW, ≈ 35 kWh/vrk; symbolic form before substitution.
- solutions.md: each unknown solved symbolically first; intermediate values (1356 kWh, 1,26 kW, 1,608·10²² J, 2755 kWh) and unit checks right.
- inquiry numerics: tase-ennusta 150 W/m², epatasapaino ΔT = 3,6/1,2 = 3,0 K (table rows consistent), siirto 0,461 kWh with mistakes 0,749 and 460,8, check-2 140 W/m² with atmosphere balance 290 = 150 + 140, virhe 45 W.
- Model values physical: σ(288 K)⁴ ≈ 390 W/m², σ(255 K)⁴ ≈ 240 W/m²; feedback 1,2 W/(m²·K); CO₂ 280 → 420 ppm; imbalance ≈ 1 W/m².
- Every correct option and distractor feedback in pr-tasapaino, pred-1, pred-2, tase, virhe, check-1: physics right.
- P = UAΔT with its steady-state condition; parallel parts add; scope within FY3 (cmΔT, lämpökerroin from earlier chapters).
- Figures: ΔT = 36 K matches 21 °C → −15 °C, largest drop in insulation; convection loop and radiation through vacuum correct.
- Hash identical at start and end.
