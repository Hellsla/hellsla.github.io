VERDICT: PASS
CONTENT-HASH: 80e44fd6110c09bb

## Blocking
- None.

## Polish
- Step 7 (and the common-error line): "Jos vakiotermi on epävarmuuksien rajoissa nolla" — the student needs the intercept's uncertainty for that; add a link to [[ohje:tvt-epavarmuus|…]] (fit-parameter uncertainty, Pro, or the steepest/shallowest lines, whose intercepts give a range).
- Step 8 list: the toy-car line $v^2 = 2g \cdot h$ holds only when friction (and the wheels' rotation) is negligible; a few words ("kun kitka on pieni") would state the condition (guardrails B). Cooling line: the model is Newton's cooling law; optional to name it.
- Step 4: "RMSE kertoo, kuinka kaukana pisteet ovat keskimäärin suorasta" is a fair simplification (root-mean-square, not mean) — keep, or say "neliöllisesti keskimäärin".

## Checked
- Least squares described correctly: vertical residuals, minimum sum of squares; line not through first/last point; points "yleensä" not exactly on the line (guardrails wording).
- Linear (with intercept) vs Proportional (y = kx); fit Linear first, Proportional only with a physical reason; r near ±1 does not prove the model; residual pattern check; outlier wording is the guardrails sentence; extrapolation rule.
- UI names: Graph Tools > Apply Curve Fit, Linear, Proportional, region selection by dragging, fit box with coefficients, RMSE and r (Linear) — all in ga-facts.md.
- Linearisations correct: T^2 vs l, v^2 vs h, E vs 1/r^2, ln(T − T_huone) vs t.
- Figures match figures.py: `fit` line is the computed least-squares line, residuals vertical; `linearise` left panel's LSQ line is above the points at the ends and below in the middle, exactly as the text and aria-label say; no overlaps; schematic, no numbers.
