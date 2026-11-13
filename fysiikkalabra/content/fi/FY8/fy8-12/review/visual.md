VERDICT: PASS
CONTENT-HASH: c8fedeca02ca08f2
Mode: delta (changed file lesson.md only: the new vaimennuskerroin passage and the edited summary bullet)

## Blocking
- none

## Polish
- [Minor] lesson.md, line 359 (new μ text) — The unit is set as the inline fractions `$\tfrac{1}{\text{m}}$` and `$\tfrac{1}{\text{cm}}$`. They render very small and cramped at 1280 px. Write `$\text{m}^{-1}$` and `$\text{cm}^{-1}$`, or `$1/\text{m}$`.
- [Minor] lesson.md, lines 359–361 — The half-value step `$\tfrac{I}{I_0} = \tfrac{1}{2} = e^{-\mu d_{1/2}}$` sits in running text as a tiny chain, and the lead-in "eli" is orphaned at the end of a line before the display. Make the chain a short aligned display block and keep "eli" with the final formula.
- [Minor] lesson.md, line 495 (summary bullet) — The chain `I = I_0(1/2)^{d/d_{1/2}} = I_0 e^{-\mu d}, missä \mu = \tfrac{\ln 2}{d_{1/2}}` is dense inline. It stays readable and the layout holds, so it is acceptable. Splitting it into two sentences would be gentler.
- [Minor] The graph "vaimeneminen" shows only the halving form. The new μ is introduced beside it without a note that the same curve is `e^{-\mu d}`. Optional: add a half-sentence to the paragraph under the graph.

## Checked
- Opened fy8-12-theory-1280-4.png. It shows the new paragraph and both display formulas (`I = I_0 e^{-\mu d}` and `\mu = \ln 2 / d_{1/2}`), set cleanly with correct operator spacing and the term in bold and underlined. The graph "vaimeneminen" below is unchanged and intact, and the layout survived the insertion (no overflow or clipping, display blocks aligned).
- Opened fy8-12-theory-1280-6.png. The Tiivistelmä bullet renders correctly, and the concept chips now include "Vaimennuskerroin".
- Source diff read for LaTeX (`\cdot` is not involved, `\text` units, no plain number-with-unit in the new text).
- I did not open the other captures. The diff touches no figure body, simulation or exercise.

## Scores
illustrations 5 · typography 4 · Finnish 4 · accessibility 4
