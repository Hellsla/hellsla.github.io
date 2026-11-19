VERDICT: PASS
CONTENT-HASH: 3b8da62f2de25dff

## Blocking

## Polish
- lesson.md, photo caption under iso-processes ("Helium fills only the top of the balloon, because the gas expands …"): the "because" puts the cause the wrong way round. The partial fill at launch is chosen *so that* the gas has room to expand later, and the air also gets colder as the balloon rises. Fix: "At launch helium fills only the top of the balloon, so that the gas has room to expand as the outside pressure falls during the ascent."
- inquiry.json pred-2, feedback of the "$50\,\text{ml}$" option: "push on it as much as the weight does". The 100 kPa prompt includes the outside air as well as the weight. This is fine at the level (C). Optional wording: "as much as the weight and the outside air do".
- sim.js `tx`/`txs`: the readout and table show a decimal comma on the English page (screenshot exp-2: "50,0 ml", "293,15 K"). The physics is unaffected; this is a language and visual matter.

## Checked
- Recomputed every number in one script with my own formulas (all agree): the worked example ($V_2 = 1.036 \to 1.0$ l, +30 %), the misconception ($1.04$ l, 3.5 %), kertaus (2020 N; 5.05 MN distractor), pred-1 (200 kPa, 5.00 J), pred-2 (60.2 ml, 0.171 ml/K, ×1.20), exp-2 question ($3.41\cdot10^{-3}$ = 1/293), syringe rows (pV 5040/5050/5040/5430/5040, 168 kPa, +7.7 %), virhe (252.5 → 250 kPa; 40.4), siirto (1.069 → 1.07 l, mistakes 2.10 and 0.00107, 71 %, 108), check-c2 (1.0999), check-2 (120 kPa, mistakes 108 and 0.12), exit ticket (160 kPa). lesson-answers.py output matches.
- Boyle's law, $V/T$ and $p/T$ are stated with their conditions: a fixed amount of gas, isothermal/isobaric/isochoric, a dilute gas, kelvins, total pressure rather than gauge pressure, and condensation before 0 K. All are within FY3's central contents.
- The micro-model mechanism is right in the theory, check-1 and pred-1/-4 feedback: same speed, hits twice as often. The temperature dependence is right too: faster and harder hits.
- Figures are to scale as claimed. micro-boyle: 220:110 px heights, 4 vs 8 hit marks. boyle-graphs: every point on $pV = 2000$ kPa·ml, and the line through the origin has slope ≈2010. absolute-zero: both graphs give point ratios of 1.474 = 373/253, and the lines pass through the origin.
- Every choice item has exactly one correct option, every distractor is really wrong, and its feedback is correct.
- exp-1 locks the mode (T fixed by the model) and varies Vml; `p` (Pa) and `constant` (pV in J = kPa·ml·10⁻³) exist in simState. exp-2 locks the isobaric mode (the mode change resets to 50 ml, 100 kPa) and varies Tc; the adapter supplies `T`, `Vgas` and `VperT` in the stated units.
- The sim implements pV/T = constant in all three modes. Its axis ranges hold every slider value. Hit rate ∝ √T/V and flash size ∝ speed, so it is consistent with p ∝ T/V. The calc box and the pred-3/johtopäätös texts say the sim's pressure is computed by the model and does not prove the law.
- The model answers (johtopäätös, check-3) and their criteria match the theory. The syringe data are labelled as invented example values.
- The hash was the same at the start and at the end.
