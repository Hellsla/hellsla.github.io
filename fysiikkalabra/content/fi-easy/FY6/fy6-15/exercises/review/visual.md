VERDICT: PASS
CONTENT-HASH: 250518ce070eda9b
SCOPE: delta numbers from a41d2773d2998e16 base 3076572

## Blocking
- none

## Polish
- [Minor] solutions.md Formula blocks — consecutive rows of unrelated starting equations share one aligned `=` column, so the left sides drift (e.g. `I_talo + I_a = I_p` sits left of its neighbours); acceptable, no change needed.

## Checked
- Delta (solutions.md): the new Kaava/Formula blocks that start from basic-principle equations, as aligned multi-row display maths. Captures opened (1280 px, every solution open): L3-8 (residual current, 6 rows).
- Blocks render without red KaTeX, equals signs aligned, fractions and subscripts legible, nothing clipped at 664 px column; the following Muunnokset/Sijoitus blocks survived. English: no Finnish words in the maths of the captured blocks (text-subscript grep over every Formula line too).
- Not opened: 390 px solution captures (none made for open solutions; check_layout 360 px passes).

## Scores
illustrations 5 · typography 4 · Finnish 4 · accessibility 4
