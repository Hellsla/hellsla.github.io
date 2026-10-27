VERDICT: PASS
CONTENT-HASH: 95f447a9c89c7a99

## Blocking

## Polish
- inquiry.json:227 (johtopaatos model) — gives "ΔL = 6,0 mm" beside "12,0 mm", while pred-1/pred-2 feedback uses 6,00 mm and 12,0 mm; the precision is inconsistent — write 6,00 mm.
- lesson.md:158 — "noin sadastuhannesosan pituudestaan jokaista kelviniä kohti": steel's 12 · 10⁻⁶ 1/K is about 1/83 000, so "runsaan sadastuhannesosan" is more accurate.
- lessons/FY3/fy3-8/sim.js:70 — the lattice spacing is set from ΔL/L₀ = αΔT, so exp-1 confirms the program's arithmetic and does not show the physics emerging. The `model` text discloses it; acceptable.

## Checked
- All 12 exercise answers, recomputed independently, match answers.py and exercises.json (457 cm³ → 460, 52,08 m → 52, −51,75 mm → −52). Solutions are symbolic first; conversions and rounding are right.
- Worked example: 12e-6 · 120 m · 60 K = 86,4 mm; the 0,072 % and the 60 mm order-of-magnitude estimate are correct.
- pred-1/pred-2 model values (6,00 mm and 12,0 mm, 0,0600 %), kertaus (60 K, 333 K distractor), virhe (27,9 mm against 1,8 mm, ×15, 0,7 %) and check-2 (23, and the mistakes 46 and 15,3) are all correct.
- siirto: 2,2 mm³ / 0,050 mm² = 44 mm; the mistakes 0,044 and 110 are right; with the glass included the answer is 42,9 ≈ 43 mm; ethanol/glass γ ≈ 41.
- olomuodot table: 0,36 / 2,1 / 11 / 34 cm³; the check-3 claim that air's γ is about 100 times steel's 3α is correct (≈94).
- The physics is correct: the anharmonic micro-model (asymmetric oscillation; Cem's symmetric-oscillation option is correctly marked wrong), γ ≈ 3α with its small-change condition, holes grow, the water anomaly at 4 °C, gases treated at constant pressure, the hook's comb joint overlapping less on a frosty morning, the bimetal strip bending toward the steel side.
- Table values for α and γ (water 0,21, ethanol 1,1, petrol 0,95, air 3,4 · 10⁻³) are realistic.
- sim.js: ΔT = T − 20 °C, ΔL = αL₀ΔT, amplitude ∝ √T (K), the ×100 exaggeration is labelled, particle size stays constant, and "alle 0,3 %" holds (maximum 0,23 %). simState carries dT, dL and rel for both experiments. exp-1 locks material and L₀ and varies T; exp-2 locks material and T and varies L₀, so each isolates its parameter.
- Figures: the particle, flask (V₀ + ΔV in the neck) and rod figures are labelled exaggerated and consistent.
- Exit ticket: 21 mm is correct; the hole and particle-size answers are correct.
