VERDICT: FAIL
CONTENT-HASH: f528605d63d6c53e

## Blocking
- assets/sims/fy1/fy1-6/sim.js:70–71 via lang/fi.json:567–568 (sims.fy1-6.rivi, rivi_alku) — the readout the student sees writes the division as an operation with a slash, `$v/t = …$` and "`$v/t$` ei ole vielä määritelty", against the notation rule; the sim's own calc box already says `v : t` — write `$v : t = {{q}}\,\text{m/s}^2$` and "`$v : t$` ei ole vielä määritelty".

## Polish
- lesson.md:171 — the km/h conversion drops the units (`3{,}6 \cdot 14{,}715`); write `3{,}6\,\tfrac{\text{km/h}}{\text{m/s}} \cdot 14{,}715\,\text{m/s}` or convert as $14{,}715 \cdot 3{,}6\,\text{km/h}$.
- lessons/FY1/fy1-6/sim-spec.md — "v/t" (twice); not student-facing, align with the colon rule.

## Checked
- Worked example 14,715 → 15 m/s, 52,97 → 53 km/h from the unrounded value; check against the graph correct.
- Free-fall figure to scale: drops 4,9/19,6/44,1 m at 6,2 px/m (10 m bar = 62 px), arrows ∝ v (1 : 2 : 3); same-fall figure drops ratio 1 : 4, equal arrows; (t, v) figure points 9,81…39,2 m/s exact.
- Air model: quadratic drag, K = ½·1,2·0,47·π·0,10², v = v_T tanh(gt/v_T); at 4,0 s 0,1 kg → 10,5 m/s, 10 kg → 37,5 m/s as the model answer says; never exceeds gt.
- exp-1 9,81 m/s² (solution 9,8 inside 2 %, mistakes 19,6, 29,4), data task 9,8 m/s² (LS 9,78; residuals ≤ 0,04 m/s; ±0,2 m/s² estimate fair), siirto 11,1 → 11 m/s (mistakes 29,4, 22,2, 3,7), check-2 3,06 s (11,0, 30, 0,327): all correct.
- Experiments lock environment and the other mass/time; vary isolates t or m_B; simState keys present.
- Limits stated (model values, same-size balls, no wind/spin); massa ei vaikuta tyhjiössä explained without forces (scope).
- Notation elsewhere: \cdot, `v : t` in calc, no ×/δ.
