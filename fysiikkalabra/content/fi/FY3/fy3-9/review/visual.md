VERDICT: FAIL
CONTENT-HASH: 988c2059ac45b91e

## Blocking
- [Major] fig 6 `absolute-zero` (lesson.md:348–423, captures fig-6-390, theory-1280-3) — the lower graph's label "−273 °C" under the origin is cut off at the figure's bottom edge (label box ends at y 628,5 in a 622 high viewBox; the glyph bottoms are lost at 390 and 1280 px). It is the label that carries the point of the figure (0 K = −273 °C), and breaks the 12 px margin rule — fix: raise the viewBox height to about 640 (or move the lower graph/label up) so the box ends 12 px inside the edge.

## Polish
- [Minor] lesson.md Esimerkki, Ennusta, Koe 1 — number+unit in prose is mixed: "$0{,}80\,\textsf{l}$ ilmaa 101 kPa:n paineessa", "50 ml", "100 kPa" plain, "$20\,{}^\circ\text{C}$" and "$78\,\text{kPa}$" in maths, in the same sentence — set all in maths (NOTES §1) so one typeface runs through.
- [Minor] litre `\textsf{l}` renders as a bare vertical stroke in the example ("0,80 |", "1,036 |"); project convention, so only the implication: it can read as a bar or the digit 1. Nothing to change here.
- [Minor] Summary bullet 1: "isokoorisessa $V$ ." shows a space before the full stop (inline maths at the end of a line after a break); check that the sentence ends "…$V$." without a gap.
- [Minor] Alkutila lines of the experiments (Koe 1–2) set "θ = 20 °C", "tilavuus V = 50 ml" partly in sans text, partly in KaTeX (tex_name only turns the symbol into maths).

## Checked
- 390 px: top-390, fig-1, fig-3, fig-4, fig-5, fig-6, example-390-1/2, sim-390, stage-ennusta-390-1/2, exp-exp-1-390-2; contact sheets 2 (Tutki, Teoriatiivistelmä, Sovella, Tarkista).
- 1280 px: intro, fig-row, sim-1280, lab-1280-1/2, theory-1280-3/4, open-ennusta-1280-1, open-tarkista-1280-1.
- Figures 1–6 all opened; the other figures are legible, consistent in palette (force/velocity colours distinct), labelled in KaTeX, with graphs having units, ticks, points apart from the curve, dashed extrapolation.

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
