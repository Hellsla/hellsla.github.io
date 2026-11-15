VERDICT: FAIL
CONTENT-HASH: 95262ce9df1aca45
Review of the recognition chart (queue 9c) and the term change against the version passed at fdfc56cdc13d1300; full on the chart, delta on the rest.

## Blocking
- **B, chart row 7 and aria-label: "the line misses the origin → systematic error, $b \neq 0$".** Only true when the model predicts a line through the origin; the Formula section states exactly that condition ("If according to the model the line should pass through the origin but $b$ clearly differs from zero"), and row 5 of the same chart fits $y = kx + b$ with a legitimate $b$ (guardrail: a line through the origin needs a physical reason). Fix: e.g. "model: through the origin, but the line misses it".

## Polish
(none)

## Checked
- Rows 1–6: $\bar{x} = \sum x_i/n$; $\Delta x = (x_\text{max} - x_\text{min})/2$; $\bar{x} \pm \Delta x$; $\varepsilon = \Delta x/\bar{x}$; $y = kx + b$; $k = \Delta y/\Delta x$ from far-apart points of the line. All agree with the Formula section.
- The aria-label matches the chart.
- Term change: sovella/solutions.md (2 lines) and the link title in unit.md "kinetic" -> "sliding friction"; the physics of both lines (steady pull = sliding friction, grip = static friction) is unchanged and correct.
- The en chart (docs/figures/fy9-tunnistus/fy9-kokeellisuus-en-360.png) and the hash, taken at the start and the end (95262ce9df1aca45).
