VERDICT: PASS
CONTENT-HASH: 1cd4b5de867dc84f

## Blocking

## Polish
- inquiry.json:117,121,223 — measure labels `E_A (kJ)` etc. show the unit as plain text in the experiment table header (koe shots part 2), against the all-LaTeX label rule — make the header LaTeX (`$E_\text{A}\ (\text{kJ})$`) or fix the shared table renderer.
- sim.js:133 — `fP` drops trailing zeros: canvas $P_\text{A} = 2\,\text{kW}$ beside readout $2000\,\text{W}$ — show W on the canvas or keep $2{,}0\,\text{kW}$.
- inquiry.json:81 `model`, sim.js:53 — "sama määrä kierroksia kilowattituntia kohti": disc speed ∝ P in real time, but its turns do not count the model's E and it spins regardless of the slider — say only that its speed shows the power.
- lesson.md:35,126,140 and inquiry.json — symbol products as $P\,t$ while the example uses $E \cdot \text{yksikköhinta}$ — use `\cdot` throughout if the teacher's rule covers symbol products.
- inquiry.json tarkistus-2 mistake 0.8 — "kerro 1000:lla" is not a substitution — write $0{,}8\,\text{kW} = 0{,}8 \cdot 1000\,\text{W}$.

## Checked
- All numbers of lesson.md, inquiry.json, exit ticket and lesson-answers.py recomputed in one script: all match.
- Every correct option and every feedback/mistake number (ennuste-1 incl. 150 h → 5,4 MJ, mittari, virhe, tarkistukset, koe mistakes, siirto).
- koe-1: A, tA, B locked, tB varied; at tB = 900 min EB_kJ = EA_kJ = 540 exactly; measured keys in simState; reveal after 3 rows.
- koe-2: A, B, tB locked, tA varied; tA = 30 min gives EA_kWh = 1 exactly.
- sim.js: E = P t (t in s); graph slope P·3600/f consistent with the plotted point, one scale for both, dashed extension clipped, 1–2–5 axes; canvas and readouts LaTeX (shots 1280/390); speed affects only the disc.
- Model box states the constant-power assumption, typical rounded ratings, fridge/thermostat caveat, model values not measurements.
- Figures 1 and 2 to scale (bars 400/200/16 px; lines and ΔE/Δt = 40 kJ : 20 s = 2000 W).
- P = ΔE/Δt, E = P t, t = E : P, 1 kWh = 3,6 MJ with conditions; inside FY2 scope, no work or force.
- Worked example: seven stages, conversions by substitution, 2-figure rounding justified, real reasonableness check.
- OL3 ~1600 MW (TVO) and price ~18 snt/kWh (Tilastokeskus 2025) sourced and realistic.
