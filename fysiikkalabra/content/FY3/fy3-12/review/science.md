VERDICT: PASS
CONTENT-HASH: 460738fe192260c8

## Blocking

## Polish
- figures.py:energy_balance (lesson.md:186) — the "heijastuu" arrow starts in mid-air above the atmosphere, detached from the incoming beam, so it is not visible what reflects the light — start it where the incoming arrow crosses the atmosphere (clouds) or at the ground.
- inquiry.json:13 (hook) — the Moon's albedo (about 0,12) is far below the Earth's 0,30, so the Moon absorbs more per square metre, not the same; its cold mean also comes partly from slow rotation — say "at least as much" sunlight is absorbed, which strengthens the point.
- lesson.md:6 — "laajentunut ja kevyempää" — say "harvempaa" (smaller density) rather than lighter.
- figures.py:wall_temperature — the drops in the two boards (5 % each) are larger than real (about 1–2 %); acceptable as a periaatekuva.

## Checked
- answers.py run and recomputed independently in one script: all 12 exercise answers match exercises.json within tolerance (432 W, 1,2, 30 K, 49 kWh, 238, −20 °C, 149 €, 212 kWh, 3,4, 20 K, 0,139 K, 984 kWh).
- Worked example: 734 W + 720 W ≈ 1,45 kW, 35 kWh/vrk; U ratio 1,0/0,17 ≈ 5,9 and area ratio 1/6 consistent; symbolic form before substitution.
- solutions.md: every formula solved symbolically first; intermediate values (1356 kWh, 1,26 kW, 1,76/0,50 kW, 1,608·10²² J, 2755 kWh) correct; unit checks right.
- inquiry numerics: tase-ennusta 150 W/m², epätasapaino ΔT = 3,6/1,2 = 3,0 K (table rows consistent), siirto 0,461 kWh with mistakes 0,749 (26 K) and 460,8 Wh, check-2 140 W/m² with atmosphere balance 290 = 150 + 140, virhe 45 W, exit ticket 300 W.
- Model values physical: σ(288 K)⁴ ≈ 390 W/m², 240 W/m² ↔ 255 K (−18 °C), feedback 1,2 W/(m²·K) gives ≈ 3 K for a 3,6 W/m² forcing; CO₂ 280 → 420 ppm, imbalance ≈ 1 W/m², ocean layer mass 2,6·10²⁰ kg plausible.
- Every correct option and every distractor's feedback in pr-tasapaino, pred-1, pred-2, tase, virhe, check-1: physics right; no option referred to by place.
- P = UAΔT with its steady-state condition stated; parallel parts add; scope (lämpökerroin, cmΔT from earlier FY3 chapters) within FY3.
- Figures (code and 390 px shots): ΔT = 36 K matches 21 °C → −15 °C, largest drop in the insulation, P from inside out; convection loop and radiation through empty space correct; all labels LaTeX.
- Hash identical at start and end.
