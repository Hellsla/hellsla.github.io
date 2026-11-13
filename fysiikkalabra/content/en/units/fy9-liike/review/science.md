VERDICT: PASS
CONTENT-HASH: 8e16b09b0e569f61
Delta review (merge of #523 solution practice into #522, 2026-11-13) of the version passed at 0462ca982df89864.

## Blocking
(none)

## Polish
(none)

## Checked
Every hunk of the en merge diff (word diff). $y_\text{top} = y_{0A} + v_0^2/(2g)$ follows from $t_\text{top} = v_0/g$; $a_\text{min,max} = 2x/(t \pm \Delta t)^2$ (the longer time gives the smaller acceleration, correct). Every changed formula is symbolic before substitution and uses no symbol in a sense that differs from the unit's ```kaavat``` names or notation from #522; the $ and brace balance of each added line is checked; `units.py check` passes; the hash was taken at the start and the end and matches.
