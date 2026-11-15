VERDICT: PASS
CONTENT-HASH: 0bb2960dd8b3e142

## Blocking

## Polish
- inquiry.json siirto solution, Järkevyys — "kansi painuu ulospäin": the net force on the lid is outward, but a tight lid need not move; "ilma painaa kantta ulospäin" says what the numbers show.
- lesson.md Esimerkki, Tulos — two significant figures are claimed but the slope 0,37 kPa/°C comes from 137 − 100 (two figures by subtraction); a least-squares fit gives −271 °C, so −270 °C is fine; one clause saying the difference of the end readings limits the precision would make the reason exact.

## Checked
- Changed lines: siirto check 60/293 ≈ 0,205, 0,205 · 101 kPa ≈ 21 kPa, 122 kPa — right; "ala-asteikko" wording only.
- Definitions: system, closed system, state variables, pressure, temperature with its limits (dilute gas: translational KE; liquids/solids: interaction energy; motion does not stop at 0 K) follow the guardrails.
- Mechanism: volume change → more frequent hits, not harder; temperature rise → more frequent and harder hits — stated consistently in text, predictions, model answer and exit ticket.
- p ∝ T stated with its conditions (constant V and n, dilute gas far from condensing).
- Worked example: symbolic θ₀ = −p₀/k first; k = 0,37, θ₀ = −270 °C; check 136,6 kPa vs 137 kPa; extrapolation flagged as a model (gases condense first); endpoints are not neighbouring points.
- Kelvin-scale figure is to scale as claimed; formula T/K = θ/°C + 273,15 right.
- sim.js: 2D momentum flux per wall length averaged over both axes gives p ∝ T/V; pRef and pTheory consistent; speed control does not alter pressure; equal-speed, no-collision 2D assumptions stated in `model`.
- exp-1 (T varied, V = 1 locked) and exp-2 (V varied, T = 300 K locked) isolate their variable; simState gives theta, vRel, pRel, pTheory.
- Recomputed: 600,15/300,15 ≈ 2, √2 = 1,41; 128 kPa; 122/404/83,8 kPa; 1,035; −273 °C; all predictions and checks have exactly one correct option with correct distractor feedback.
- Misconception, summary, check-3 model and exit ticket agree with the theory.
