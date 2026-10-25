VERDICT: PASS
CONTENT-HASH: cf1d04190c313c7e

## Blocking

## Polish
- lesson.md:90 — "laajenee, kunnes pussin sisäpuolinen paine on yhtä suuri kuin ulkopuolinen" holds only while the bag is slack; once it is taut (the opening question), the film carries the difference and the inside pressure is higher — add "niin kauan kuin pussi on löysä" or similar.
- exercises.json:14 (L1-02) — real pressure-tank gauges show overpressure, and L3-02 teaches exactly that distinction; write "ilman kokonaispaine" so the 160/280 kPa values cannot be read as gauge readings.
- solutions.md:47 (L2-01) — "ilma on noin 10 % jäykempää" is vague; say that at 300 bar the product pV of air is about 10 % larger than Boyle's law predicts (Z ≈ 1,1), so the real volume is about 1,8 m³.
- solutions.md:61 (L2-03) — say that the point (0,100 1/ml; 201 kPa) is read from the fitted line, not the measured 203 kPa.

## Checked
- Formulas p₁V₁ = p₂V₂, V/T and p/T constant: correct, with conditions stated (fixed amount, kelvins, total pressure); within the FY3 content "kaasujen tilanmuutokset" and the "Boylen lain todentaminen" lab in docs/lops2019.
- Pa·m³ = J and 1 kPa·1 l = 1 J are correct; using kPa and litres on both sides is valid.
- Worked example: solved symbolically, then values substituted; 1,036 l ≈ 1,0 l, an increase of about 30 %.
- All 12 answers.py lines model the problem text correctly. Recomputed by hand: L2-03 least-squares slope through the origin 2009 kPa·ml = 2,01 J (pV 1980–2030); L3-02 absolute 351 → 303,1 kPa, gauge 202 kPa (216 kPa if the gauge reading is used, as the solution says); L3-03 L₂ = 10,07 cm, travel 29,9 cm.
- Side claims (7 kN lid, 40 min, 24 %) and exit ticket (160 kPa; ×1,1) are correct.
- Figure 1: gas heights 2 : 1, the same arrow lengths, 4 → 8 hit marks, so pressure doubles.
- Figure 2: every (V, p) point has xy = 8360 (hyperbola); the (1/V, p) points lie on a line through the origin with slope 0,917 matching the drawn line.
- Figure 3: 1,2 px/K, points at 253–373 K, and the dashed extension meets the origin at 0 K.
- sim.js uses the exact formulas pV = p₀V₀, V = V₀T/T₀, p = p₀T/T₀; particle speed ∝ √T; the converted constant is correct (kPa·ml·10⁻³ = J); the dashed extension and thermometer direction are correct.
