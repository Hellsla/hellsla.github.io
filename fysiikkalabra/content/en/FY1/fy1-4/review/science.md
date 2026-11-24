VERDICT: PASS
CONTENT-HASH: 0dca5b5e4df10101

## Blocking

## Polish
- inquiry.json:625 (ennuste-2, "first data point" feedback) — the extrapolation gives 78.5 g − 16 g = 62.5 g, written "≈ 63 g", while the correct option and the conclusion say "about 61 g". The sim's best b at k = 0.80 g/ml is 61.3 g (least squares: 62.3 g). — Write "about 62 g", or say that the small difference comes from the locked slope.
- inquiry.json:636 (sim `calc`) and the sim readout — "mean deviation" names a root-mean-square value. The definition given is correct, but "mean deviation" usually means the mean absolute deviation. — Consider "root-mean-square deviation d".
- inquiry.json:843 (kuvaajasta) — the text says "the line fitted to the data points", but the figure shows only the line, P₁ and P₂. — Write "the fitted line", or draw the points.

## Checked
- The round-1 blocker is fixed. The koe-3 distractor now reads "no line passes through all the points", and its random-error feedback answers it. The koe-3 item now has exactly one correct option, and every other choice item (kertaus, ennuste-1/2, virhe, tarkistus-1, check-c2) has exactly one correct option, with feedback that is right.
- Dataset 1 (b = 0): best k = 0.49 m/s with d = 0.119 m; d(0.30) = 0.758 m and d(0.60) = 0.436 m. Successive slopes are 0.2/0.8/0.5/0.3/0.5 m/s and single-point s/t values are 0.60/0.40/0.53 m/s. All match the text.
- Dataset 2 (k = 0.80 g/ml): d(b = 0) = 61.3 g; the best b is about 61 g with d = 1.2 g.
- Dataset 3 (b = 80 °C locked): d is smallest at 5.80 °C, at k = −1.90 °C/min. The residuals run + − − − − + +, and the least-squares residuals show the same pattern. d at the initial state is 17.2 °C, which matches the koe-3 capture.
- Worked example: k = 8.0 °C/min, b = 20 °C, t = 2.5 min. Least squares gives 7.85 °C/min and 20.5 °C. The residuals from the line are at most 0.8 °C. The condition "constant power, small heat losses" is stated. The solution is symbolic first.
- Cyclist 15 km/h (mistakes 16.7 and 0.067 km/h), plant 20 days (mistakes 25 and 16 days), hike 7.0 h (mistakes 8.3 and 5.5 h), exit ticket 1.5 m/s and 2.0 m, pysähdy 2.0 m/s: all recomputed and correct. Extrapolation is flagged where it is used.
- Figures recomputed from their pixel coordinates, all to scale: the scatter (0.5t, three points above and three below), the slope figure (b = 1, P₁ (2, 2), P₂ (8, 5)), the kettle figure (points, A, B and the 2.5 min mark) and the cyclist figure (5 km intercept, (1.0 h; 20 km), (3.0 h; 50 km), 35 km at 2.0 h).
- Sim: the RMS and least-squares formulas are correct. simState gives d at every experiment's initial values, the slider ranges cover every setting, and the locks isolate the varied parameter. The model box says the data are example data and that y carries the error.
- Guardrails are followed: fits use "usually", and outliers are not dropped automatically. The line through the origin has a physical reason (the trolley starts from s = 0 at t = 0), and the slope is read from the line. Interpolation and extrapolation are distinguished.
- Scope stays within FY1 (graphical and linear models).
