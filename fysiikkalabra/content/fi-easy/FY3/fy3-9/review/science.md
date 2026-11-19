VERDICT: PASS
CONTENT-HASH: f8b27cc6d10596c7

## Blocking

## Polish
- inquiry.json `siirto` prompt — "1,50 litran" is a plain number with a unit, while the solution writes $1{,}50\,\textsf{l}$ — write it in LaTeX.
- inquiry.json `check-2` solution, Järkevyys — "Paine on hiukan yli ilmanpaineen" for 120 kPa against 101 kPa (about 19 % more) — say "selvästi yli" or "noin viidenneksen yli".
- inquiry.json `pred-2`, feedback of the 50 ml option — "osuvat mäntään useammin ja kovempaa" describes only the moment before the piston rises. In the final state, and in the sim's isobaric flashes (rate ∝ 1/√T), the hits are fewer but harder. The next sentence already implies this; adding "lopussa harvemmin mutta kovempaa" would remove the apparent mismatch with what the student sees.

## Checked
- I recomputed every number in one script with my own formulas: the worked example (1,036 → 1,0 l, +29 %), the misconception (1,035 → 1,04 l, 3,5 %), kertaus (2020 N; p/A = 5,05 MN), pred-1 (200 kPa, 5,00 J), pred-2 (60,2 ml, 0,171 ml/K, all distractors), γ = 1/293 = 3,41·10⁻³ 1/K, ruisku (pV = 5040/5050/5040/5430/5040, 168 kPa, +7,7 %), siirto (1,07 l; mistakes 2,10 and 0,00107), check-c2 (1,0999), check-2 (120; mistakes 108 and 0,12), exit ticket (160 kPa). lesson-answers.py agrees.
- Conditions are stated where the laws are used: a closed gas amount, isothermal for Boyle, a dilute gas and kelvins for V∝T and p∝T, absolute pressure, and the extrapolation to 0 K marked as the model's prediction.
- The micro model's causality is right: same speed, twice the hit rate at V/2, and faster particles when heated (speed ∝ √T in the sim's model box).
- The figures are to scale: in boyle-graphs every point and the 1/V line fit pV = 2000 kPa·ml. In absolute-zero the points from 253 to 373 K have V/T and p/T constant and the dashed lines reach the origin. micro-boyle has heights 2:1 and twice the hit marks.
- sim.js implements pV/T = const in all three modes. simState.constant is in SI units (J, m³/K, Pa/K). The adapter supplies Vgas and VperT. The calc box and the pred-3 feedback say that the sim's numbers are model values and prove nothing.
- exp-1 locks T = 20 °C and the mode and varies V (slider 20–100 ml covers 25, 50 and 100). exp-2 has the isobaric mode at 100 kPa and varies θ (−50…150 °C).
- Every choice item has exactly one correct option, and every distractor's feedback is correct.
- Content is within FY3's central contents (kaasujen tilanmuutokset, Boylen lain todentaminen) and nothing comes from FY4.
- The worked example and the numeric solutions are symbolic first, with the limiting data named and a real reasonableness check.
- The theory, summary, learn goals, sim boxes, explain models and exit ticket are consistent with each other.
