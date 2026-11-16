VERDICT: PASS
CONTENT-HASH: 66d5ebc227c0907c

## Blocking

## Polish
- inquiry.json check-3 model: "about a hundred times" (3.4·10⁻³ / 3.6·10⁻⁵ ≈ 94) is right as an order of magnitude; "nearly a hundred times" would be exact.
- inquiry.json siirto reasonableness: "≈ 4 mm per kelvin … the order of magnitude of the scale of an ordinary thermometer". A laboratory thermometer is nearer 1–2 mm/K; a softer wording would fit better.
- inquiry.json johtopaatos model: "Δl = 6.0 mm" next to "12.0 mm". Give both to the same precision (6.00 and 12.0 mm, as the sim and pred-1 do).
- inquiry.json hook: "you cannot make a steel railing longer, however hard you pull it". Steel stretches elastically, so "not noticeably longer" would be exact. Rhetoric, not taught as a claim.
- sim.js readout shows a decimal comma (10,0000 m) on the English page. Language and visual, not physics.

## Checked
- Recomputed in one script: worked example 0.0864 m → 87 mm (an "at least" value rounded up, two figures from α and ΔT), αΔT = 0.072 %, 60 mm estimate; pred-1/pred-2 6.00/12.0 mm, 0.0600 %; table of 1 l at 10 K (0.36, 2.1, 11, 34 cm³); virhe 28 mm vs 1.8 mm (×15, 0.7 %); siirto 44 mm with mistakes 0.044 and 110, glass ratio ≈ 41, 43 mm with glass; check-2 23·10⁻⁶ from both columns, mistakes 46 and 15.3; exit ticket 21 mm. All agree.
- Changed figure (particles, now animated): same-size particles, larger symmetric vibration and larger mean spacing when warm, exaggeration stated. The asymmetry is explained in the text beside it, as in the sim's model box (C).
- Micro-model mechanism (repulsion close up, gradually weakening attraction, so the mean spacing grows) is correct and worded the same in theory, pred-3, the conclusion and check-3.
- Conditions stated: about 100 K for solids, liquids' γ only near 20 °C, gas at constant pressure, γ ≈ 3α for small changes.
- Water anomaly, the lake and the hole in a plate: correct, and theory, misconception, summary and checks agree.
- Exactly one correct option in kertaus, pred-1–3, olomuodot, virhe, check-1 and check-c2; every distractor's feedback right.
- exp-1 locks material and L0 and varies T; exp-2 locks material and T and varies L0. simState gives dT, dL and rel at those values.
- sim.js: ΔT = T − 20 °C, ΔL = αL₀ΔT, ×100 drawing, amplitude ∝ √T. The chart lines match the readout (steel at 120 °C: 12 mm). Its limits are in the model box.
- Scope: within FY3 "lämpölaajeneminen"; no FY4 content.
- Hash 66d5ebc227c0907c at the start and the end.
