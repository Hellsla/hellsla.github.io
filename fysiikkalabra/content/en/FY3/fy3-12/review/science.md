VERDICT: PASS
CONTENT-HASH: db131c2d781a107a

## Blocking

## Polish
- The newly wrapped values use decimal commas in English text: `$1{,}5\,\text{m}^2$` in the find-the-error prompt, `$4{,}0\,\text{m}^2$` in the refrigerator prompt and `$20{,}0\,\text{m}^2$` in the worked-example problem. In each case the same text states the same value with a point (1.5, 20.0). The values are unchanged, but they should be written 1.5, 4.0 and 20.0.

## Checked
batch delta review: I recomputed every number the diff touches.
- Exit ticket: 0.20 · 50 · 30 = 300 W.
- Window: the correct answer is 1.0 · 1.5 · 30 = 45 W, so the student's 15 W error (ΔT = 10 K) is still the only error.
- Refrigerator: 0.30 · 4.0 · 16 W · 24 h = 0.461 kWh.
- Worked example: (20.4 + 20.0) W/K · 36 K = 1454 W ≈ 1.5 kW, and 34.9 kWh ≈ 35 kWh. The two-significant-figure reasoning and the reasonableness check are unchanged.

The worked-example stages were only split into paragraphs. The hash was the same at the start and the end.
