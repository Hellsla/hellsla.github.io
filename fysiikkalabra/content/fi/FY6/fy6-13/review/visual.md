VERDICT: FAIL
CONTENT-HASH: 011b4e99d4a6ac33

## Blocking
- [Major] lesson.md, `## Kaava` "missä" lines and the table header (rendered in theory-1280-3/4, stage-selita-390-4/5) — units in parentheses are plain text: "kapasitanssi (F)", "varaus (C)", "jännite (V)", "etäisyys (m)", "(V/m)", "energia (J)", header "$E_\text{max}$ (MV/m)". The same sentence mixes KaTeX "($\text{m}^2$)" with plain "(m)". NOTES §1: a plain-text symbol the student reads is blocking; the sibling chapter fy6-12 sets all of these as `$\text{J}$` — wrap each in `$\text{…}$` (`($\text{F}$)`, `($\text{C}$)`, `($\text{V}$)`, `($\text{m}$)`, `($\text{V/m}$)`, `($\text{J}$)`) and the header as `$E_\text{max}\ (\text{MV/m})$`. Mechanical, quick fix.

## Polish
- [Minor] fig `rakenne` — the `eriste` leader line crosses the right plate before reaching the gap; end it inside the gap from the side.
- [Minor] fig `energia` (fig-10-390) — `U = Q/C` and `U/2` use `\tfrac` at figure size and are tiny at 390 px; use a larger fraction or `U = Q : C`.
- [Minor] sim-1280 — a white rectangle shows around the battery symbol against the gradient background.
- [Minor] exp-koe-4-390 — the `Eriste` and `Lähde` labels sit at different heights.
- [Minor] stage-selita-390-5 — the inline chain breaks after "16 ·" from its power of ten; keep `16 \cdot 10^{6}` together.

## Checked
- Opened: fig-1 (hero), fig-4 `rakenne`, fig-6 `lataus`, fig-8 `eriste`, fig-10 `energia` (390); intro-1280, theory-1280-1/2/3/4, sim-390, sim-1280 (plus a cropped zoom of the circuit), example-390-1/2, stage-selita-390-4/5, exp-koe-4-390-1, open-ennusta-1280-1, open-tarkista-1280-1.
- Circuit polarity, +Q red / -Q blue discs, green field, dipoles in the dielectric, and the charge and discharge curves are consistent with the text. Graphs have quantities on the axes; the figure descriptions match.
- Layout holds in the opened states.

## Scores
illustrations 4 · typography 3 · Finnish 4 · accessibility 4
