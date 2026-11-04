VERDICT: FAIL
CONTENT-HASH: 9b8a1649f0d52ce2

## Blocking
1. Task fy8-s1 energy-level figure, en: the right-hand labels "upper excited state" and "lower excited state" are cut off at the edge of the viewBox (the last letter is clipped) at 390, 768 and 1280 px. The labels are essential to the figure (Critical: essential labels clipped). The English strings are longer than the Finnish ones the figure was drawn for; widen the viewBox or move/shorten the labels (lessons/FY8/sovella/figures.py, "fy8-s1-levels"). "ground state" fits.

## Polish
- s3 a solution table (4 columns) is 418 px wide in a 298 px card at 390 px, so the 4th column (Rr^2) clips (already logged).
- The source box ("Statistical data...") at the top of each task is a rounded blob with uneven curvature at 390 px; readable, but the shape looks accidental.
- Figure text at 390 px is small (about 9-10 px); legible, at the lower limit.

## Checked
Captures at 390, 768 and 1280 px, full page, solutions revealed and details opened (scratchpad shots-sov/). No horizontal page overflow at any width, no red KaTeX errors. The s3 graphs (1/r^2 with dashed model line; linearised graph with dashed extrapolation to the r axis and a labelled intercept) have quantity and unit on both axes, markers distinct from the line, and aria-labels. The other tables (substance, decay, particle, nucleus) fit. Display maths in the solutions breaks into rows and fits at 390 px; decimal point, \cdot and units are consistent. Hierarchy of task card, parts, solution reveal and marking is clear.
