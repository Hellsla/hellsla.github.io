VERDICT: FAIL
CONTENT-HASH: a48aef79c9536188

## Blocking
- inquiry.json:222 (koe-3 question, third option) — A (assessment): "It does not fit, because no line passes through all the points, even if the measurements were accurate." Read literally, the reasoning holds: if the data had no measurement error, failing to lie on any straight line would show that the relationship is not linear. So this distractor can be defended, and its feedback ("because there is random error in measurements") answers a premise the option has already ruled out. Two options can then be argued as correct. — Fix: delete the clause "even if the measurements were accurate" (for example, "It does not fit, because no line passes through all the points."). The existing feedback is then right, and the en and fi texts must match.

## Polish
- inquiry.json:94 (ennuste-2, "first data point" feedback) — the extrapolation gives 78.5 g − 16 g = 62.5 g, written "≈ 63 g", while the correct option and the conclusion say "about 61 g". The sim's best b at k = 0.80 is 61.5 g, and least squares gives 62.3 g. — Say "about 62 g", or explain that the small difference comes from the locked slope.
- inquiry.json:105 (sim `calc`) and the sim readout — "mean deviation" names a root-mean-square value. It is defined correctly, but "mean deviation" usually means the mean of absolute deviations. — Consider "root-mean-square deviation (mean deviation) d".
- inquiry.json:312 (kuvaajasta) — the text says "the line fitted to the data points", but the figure shows no data points, only the line and P₁, P₂. — Say "the fitted line", or draw the points.
- sim.js `tx()` — on the English page the readout uses a decimal comma ("61,35 g", seen in the koe-2 capture). For the visual reviewer.

## Checked
- Recomputed every number in one script: dataset 1 with b = 0 has its best k at 0.49 m/s and d = 0.119 m; d(0.30) = 0.758 and d(0.60) = 0.436 (lesson 0.76 and 0.44). The successive slopes are 0.2/0.8/0.5/0.3/0.5 m/s and the single-point values 0.60/0.40/0.53 m/s.
- Dataset 2: d(b = 0) = 61.3 g; at k = 0.80 the best b is 61.5 g with d = 1.23 g; least squares gives k = 0.787 and b = 62.3 g.
- Dataset 3: with b = 80 locked the minimum is d = 5.80 °C at k = −1.90. The residuals run + − − − − + +, so the "above at the ends, below in the middle" pattern holds.
- Worked example: k = 8.0 °C/min, b = 20 °C, t = 2.5 min. Least squares gives 7.85 and 20.5, the residuals are at most 0.8 °C, and the "small heat losses" condition is stated.
- Cyclist 15 km/h (mistakes 16.7 and 0.067), plant 20 days (mistakes 25 and 16), hike 7.0 h (mistakes 8.3 and 5.5), exit ticket 1.5 m/s and 2.0 m, pysähdy 2.0 m/s: all correct.
- Figures checked against their pixels: the scatter (dataset 1, three points above and three below 0.5t), the slope figure (P₁ (2, 2), P₂ (8, 5), b = 1), the kettle figure (all points, A, B and the 2.5 min mark) and the cyclist figure (5 km intercept, P₁ (1 h, 20 km), P₂ (3 h, 50 km)). All are to scale.
- Sim: the RMS and least-squares formulas are correct, simState gives d at every experiment's initial values, the koe-2 capture shows k = 0.80, b = 0 and d = 61.35 g, and the slider ranges cover every setting.
- The origin line in prediction 1 has a physical reason (the trolley started from s = 0 at t = 0). Extrapolation is flagged in siirto and tarkistus-2, and outliers are not dropped automatically.
- Every choice item has exactly one correct option, apart from the item under Blocking. Scope stays within FY1 (graphical and linear models).
