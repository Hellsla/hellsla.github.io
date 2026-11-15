VERDICT: FAIL
CONTENT-HASH: 87d5c9e95d017f53
Review of the recognition chart (queue 9c) and the term change against the version passed at 2b347105827eead3; full on the chart, delta on the rest.

## Blocking
- **B, chart row 2: "light ejects electrons → $hf = W + E_\text{k}$".** The equation holds for the maximum kinetic energy only; the Formula section writes $hf = W + E_\text{k,max}$ and the aria-label says "the maximum kinetic energy", so the chart contradicts both. Fix: $E_\text{k,max}$ in the pill (fi figures.py line 105 too).

## Polish
(none)

## Checked
- Rows 1, 3–9: $E = hf$; $hf = E_\text{u} - E_\text{l}$; $N = N_0e^{-\lambda t}$; $A = \lambda N$; $E = \Delta mc^2$; $H = w_\text{R}D$; point source $\dot H \propto 1/r^2$; $I = I_0e^{-\mu x}$. All agree with the Formula section.
- The aria-label matches the chart apart from the item above.
- Term change: the diff's other lines are "concept map" -> "recognition chart" in teacher.md and new figures.json keys; no formula, number or task changed.
- The en chart (docs/figures/fy9-tunnistus/fy9-moderni-en-360.png) and the hash, taken at the start and the end (87d5c9e95d017f53).
