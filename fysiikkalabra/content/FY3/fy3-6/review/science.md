VERDICT: PASS
CONTENT-HASH: 98419bdbb6075730

## Blocking

## Polish
- inquiry.json:333 (tarkistus-3 criterion 1) — "noin viisinkertainen hiekkaan tai maahan verrattuna": the factor 5 holds for dry sand (800); moist soil has c of about 1000–2000 J/(kg·K) — say "kuivaan hiekkaan" or "moninkertainen maahan verrattuna".
- figures.py (water-sand) — the sand layer is about 1,9 times lower than the water, while the density ratio in the lesson (1600 vs 1000 kg/m³) gives 1,6 (alt text claims no scale) — draw the sand height ≈ water height / 1,6.

## Checked
- All 12 exercise answers recomputed independently (Q = cmΔT, the equilibrium equation, Pt = Q, densities): match answers.py and exercises.json to within 0,8 % (rounding only); signs right (L1-04 negative, L1-05 ΔT = 18 K).
- Worked example: symbolic c_m before substitution; 374,6 J/(kg·K), the sensitivity value 383 at 24,6 °C, copper equilibrium 24,6 °C, heat capacities 1257 and 75 J/K all correct.
- Formula section: Q = cmΔT, C = cm, the balance equation and its weighted-mean solution with sign conventions and the K = °C difference statement correct and inside FY3 "aineen lämpeneminen ja jäähtyminen".
- Misconception example (35 °C, factor ≈ 9 for water vs iron) and exit ticket (419 kJ, ≈9×, 50/65 °C) correct.
- Figures: water-sand thermometer rises 20 vs 105 px (ratio 5,25 = 4190/800, to scale as stated); c-bars to scale within 0,3 %; calorimeter numbers match the worked example.
- ennuste-1/koe-1: 26,8 °C, 44,0 °C, 8,5 kJ, 30 kJ, C = 160 and 838 J/K correct; only cB varies, Teq and CB are in simState.
- ennuste-2/koe-2: 40,0 / 55,0 / 63,1 °C correct; only mB varies; screenshot shows Teq 40,0 °C and Q = 41,9 kJ on both sides.
- virhe: wrong result 6,6 °C, correct 30,0 °C, and the Kelvin-shift argument (the wrong formula also shifts by 273,15) verified.
- siirto 29,1 kg with mistakes 220 and 21,3; tarkistus-2 891 with mistakes 768 and 501; tarkistus-1 4500 vs 838 J/K — all verified.
- sim.js implements the lesson's equilibrium model with no losses and no phase change; the exponential approach is stated as illustration only (τ = 1,5 s) in both code and the "model" text; the readout's Q values are equal and correctly signed.
