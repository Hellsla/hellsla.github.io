VERDICT: PASS
CONTENT-HASH: 9ec4f09c8c0c138a

Full review, round 1: exercise bank additions L1-06…08, L2-05…07, L3-04…05; the 12 earlier tasks re-checked.

## Blocking

## Polish
- exercises.json:243 — L2-07 "Kaksi tasaista metallikappaletta, A ja B, punnittiin eri tilavuuksilla": one rigid piece has one volume, and "tasainen" is not "homogeneous" — "Kahdesta tasalaatuisesta metallista, A ja B, punnittiin eri tilavuuksisia kappaleita."
- exercises.json:76 — L1-07 "Metallikappaleiden massa": the slope is a density only if all pieces are the same metal — "Saman metallin kappaleiden massa …".
- solutions.md:183 — L3-04 Vastaus says the model holds on 0…500 g, Periaate (178) and Järkevyys say 100…500 g, and 0 g was not measured — write "100…500 g (suora kulkee lähes origon kautta, joten myös pienemmillä kuormilla)" so the extrapolation is stated, as the guardrails ask.
- solutions.md:172 — L2-07 rounding reason ("luetaan kolmen numeron tarkkuudella ja hajonta rajoittaa") is muddled — say: the point-by-point ratios vary 2,87…2,91 and the by-eye slopes by a few per cent, so two figures.
- solutions.md:150, 195 — L2-05: most extensions have three figures (11,8; 23,9), so the two-figure reason should be the by-eye fit, not "kuten venymissä". L3-05 Järkevyys "uncertainty smaller than k" is not a real check; better: the mean 0,475 m/s lies between 0,40 and 0,55 m/s, and the two lines cross at t ≈ 2,7 s, inside the data.

## Checked
- Every answer recomputed in one script with numpy polyfit, separate from answers.py: all 18 numbers agree (L2-05 0,0797; L2-06 b = 0,829 m; L2-07 2,707/7,835 → 2,89; L3-04 0,0802; L3-05 15,8 %).
- The values read off the line in the solutions match the least-squares line: L2-05 (0; 0,19)/(300; 24,09), L2-06 3,068 m at 5 s, L2-07 0,27/135,6 and 0,55/392,3 g, L3-04 40,28 mm at 500 g, 48,3/56,3 mm predicted, residuals ≤ 0,24 mm, 3,5/12,6 mm deviations, all-7 slope larger (0,096).
- Tolerances fit by-eye fits (5 %, 10 %); the shown answer 0,080 gives a fine step.
- L1-06, L1-07: exactly one correct option; every distractor really wrong, its feedback right; the outlier wording follows the guardrail.
- L1-08, L2-06: intercept meaning (unloaded length, start position) is physically right; b ≠ 0 explained.
- L3-05: steepest/shallowest range stated as an estimate, not a guarantee (guardrail).
- Realistic magnitudes (Al/Fe densities, spring 0,08 mm/g, cart 0,45 m/s); FY1 scope kept (no Hooke's law or forces needed).
- Notation k, b, Δy/Δx and (x; y) points the same as the lesson; solutions symbolic before substitution.
- Old 12 tasks: unchanged physics, answers re-verified.
- Hash identical at start and end.
