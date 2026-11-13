VERDICT: PASS
CONTENT-HASH: 62a144b4944a81b5
Delta review (merge of #523 solution practice into #522, 2026-11-13) of the version passed at 7ec58540d76c5256.

## Blocking
(none)

## Polish
(none)

## Checked
- $y_\text{l} = y_{0\text{A}} + v_0^2/(2g) = 8.84$ m, the same as the stepwise substitution.
- $a_\text{min} = 2x/(t+\Delta t)^2 = 0.741$ and $a_\text{max} = 1.224$ m/s²: the bounds are the right way round.
Every number in the changed lines was recomputed with an independent script (scratchpad fy9merge/sci_fi.py); `units.py hash` gave the same value at the start and the end. LaTeX in all added lines has balanced `$` and braces.
