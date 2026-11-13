VERDICT: FAIL
CONTENT-HASH: fcb044feb02ea296

## Blocking
- [Major] contact-5 #60 (task 7e, rubric criterion "conclusion", model answer) — LaTeX renders as raw source: "texttbq / approx9,6 / cdot10^3" instead of "2,7 TBq" and "≈ 9,6·10³" (the criterion text in the exam data has doubled backslashes `\\\\,\\\\text{TBq}`, `\\\\approx`, `\\\\cdot`) — broken notation in a rubric the student self-assesses against, essential numbers unreadable — use single-escaped `\\,\\text{TBq}`, `\\approx`, `\\cdot` in the JSON string like the other criteria (7e, `conclusion` detail).

## Polish
- [Minor] fig-1 (task 1b graph) — axis reads U_s while the text and the other graphs use U_k (threshold voltage); use one symbol, or say it is the same quantity.
- [Minor] fig-3 (k2 graph) — dashed extrapolation to the origin is not labelled as extrapolation, only the two read points; add a legend note "ekstrapolointi".
- [Minor] fig-6 (k3 graph) — read-off "401" has no unit in the label; add the quantity (N = 401).
- [Minor] fig-18 (k6 graph) — fitted line extends past the last point without marking; acceptable, but the axis label $\ln(R/\text{s}^{-1})$ is clipped close to the left edge at 390 px.

## Checked
- contact-1 and contact-5 (pages #1–#12, #49–#60): opening, rubric, solutions, sub-parts, point summary at 390 px; no overflow or clipping seen.
- fig-1, fig-3, fig-6, fig-18 at 390 px (the four graphs): axes with units, readable ticks, data points distinct from the fit.
- fig-2, 4, 10, 20 (and by size the other 18 tiny captures): inline formulas (square roots, symbols) render correctly; they are not diagrams.
- Not opened individually: the 1280 captures and the remaining contact sheets (judged from the sampled sheets only).

## Scores
illustrations 4 · typography 3 · Finnish 4 · accessibility 4
