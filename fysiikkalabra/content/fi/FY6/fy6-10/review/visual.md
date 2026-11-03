VERDICT: FAIL
CONTENT-HASH: 3f97158885e32b31

## Blocking
- [Major] Esimerkki Vaihe 5/7 Sijoitus (example-390-2) — after k changed to 8,988 the middle row of the aligned substitution is wider and at 390 px the fraction's numerator "9,6 · 10^-17 C^2" runs to the box edge and is clipped (the box border is missing on that row; it was fully inside in round 1) — a number of the central calculation is cut off on a phone — break the row: put the fraction on its own line, e.g. `&= 8{,}988 \cdot 10^{9}\,\tfrac{...}{...} \\ &\quad \cdot \frac{9{,}6 \cdot 10^{-17}\,\text{C}^2}{(0{,}060\,\text{m})^2} \\ &= 2{,}397 \cdot 10^{-4}\,\text{N}`.

## Polish
- [Minor] Esimerkki Vaihe 6/7 at 390 px — "2,4 ·" / "10^-4 N" still splits across lines (carried from round 1); keep the number unbroken.
- [Minor] sim-1280 control grid alignment (carried, shared template).
- [Minor] kuvaaja (fig-12-390) — curve still starts above the 4,0 mN point and is not marked as model-computed in view (carried).

## Checked
- Delta: k = 8,988 across lesson, example, glossary and regenerated figures; "testivaraus" wording change in the kenttä paragraph and its figure aria-label.
- Captures opened: example-390-2, fig-8-390 (kentta, regenerated), fig-12-390 (kuvaaja, regenerated), sim-390. Figures keep colours (force red, field green, negative blue disc with white minus); labels and arrows unchanged and legible; surrounding layout survived except the clipped Sijoitus row.
- Hash at start and end: 3f97158885e32b31.

## Scores
illustrations 4 · typography 3 · Finnish 5 · accessibility 4
