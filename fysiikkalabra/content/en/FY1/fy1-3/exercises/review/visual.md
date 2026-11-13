VERDICT: FAIL
CONTENT-HASH: 92fd5d8209d459f3

## Blocking
- [Major] fy1-3-L1-09 solution (fy1-3-open-exercises-1280-10, -9) — set badly: the Formula and Substitution blocks put the second chain (`and deviation=` with a fraction) outside the tinted box on its own line, and the Answer paragraph sets `\dfrac` fractions inline, which stack in the running text so the lines collide (the `cm^3` exponent touches `1.005…1.015 g/cm^3` below) — clearly poor maths readability in new text, against NOTES §1 (`\tfrac` inline, one chain per step) — put the deviation on its own Substitution line as a second chain with `\tfrac`/colon form, and write the error estimate in the Answer with `\tfrac{\text{g}}{\text{cm}^3}` or `\text{g/cm}^3`.

## Polish
- [Minor] fy1-3-L1-09 — Answer says `(calculated value 1.18 %)`, other new tasks say `more precisely`; use one phrase across FY1.

## Checked
- fy1-3-open-exercises-1280-10 (new MAFY task L1-09 (3-9): text, hint, answer check, solution)
- fy1-3-open-exercises-1280-9 (task text and Formula block)
- Teacher-approved figure tasks: layout judged only; diff read for all changed lines (exercises.json, solutions.md, answers.py).

## Scores
illustrations 5 · typography 2 · Finnish 4 · accessibility 4
