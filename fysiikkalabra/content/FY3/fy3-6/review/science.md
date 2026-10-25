VERDICT: PASS
CONTENT-HASH: 973809139551d72e

## Blocking

## Polish
- inquiry.json:330 — "noin viisinkertainen hiekkaan tai maahan verrattuna": moist soil has a much larger c than dry sand (often 1,5–3 kJ/(kg·K)), so "maahan" overstates the ratio — say "kuivaan hiekkaan tai maahan" or "moninkertainen maahan verrattuna".
- sim.js:1016 — the curve snaps from e^(−10/1,5) ≈ 0,13 % of the gap to exactly 0 at T_END. This is invisible at chart scale and harmless; it is noted only so nobody "fixes" the readout.

## Checked
- answers.py and my own formulas agree on all 12 answers. Each stated answer is within 0,81 % of the computed value, inside the 2 % tolerance, and the significant figures match the data.
- Worked example: c_m = 374,6 → 3,7·10² J/(kg·K). Copper with no losses gives 24,6 °C, and 24,6 °C would give 383 J/(kg·K). Both are correct, and the solution is symbolic before substitution.
- Equilibrium derivation, the weighted-average formula, the sign conventions, and the misconception calculation (35 °C) are correct.
- Ennuste-1 values: sand 26,8 °C / 8,5 kJ, water 44,0 °C / 30 kJ, C = 160 and 838 J/K. Ennuste-2 values: 40,0, 55,0 and 63,1 °C.
- Koe-1 and koe-2 isolate the varied parameter. The initial values are inside the slider ranges, the cB option values are strings, and simState exposes Teq and CB.
- Virhe item: wrong formula 6,6 °C, correct 30,0 °C. The kelvin-shift feedback is correct.
- siirto 29,1 kg, with mistakes 220 and 21,3. tarkistus-2 890,6, with mistakes 768 and 501. All are correct.
- Exit ticket: 419 kJ, ratio 9,3 and 65 °C are correct. tarkistus-1: C = 4500 vs 838 J/K.
- SVGs: the bar heights are proportional to c within 1 px, and the water/sand thermometer rise ratio is 5,25 (true value 5,24).
- sim.js implements T = ΣCT/ΣC, Q = C_B(T_B0 − T) = Q_W, and the exponential approach is labelled as illustration only. The screenshot (default copper example) shows 24,6 °C.
