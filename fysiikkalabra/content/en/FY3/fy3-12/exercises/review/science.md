VERDICT: PASS
CONTENT-HASH: a68d988512663089

## Blocking
(none)

## Polish
- None.

## Checked
- The diff (solutions.md:45 and :222) only changes how the reflected-power arrow is described. No number or symbol changed, and the readings stay $P_\text{in} = 341\,\text{W/m}^2$ and $P_\text{refl} = 102\,\text{W/m}^2$.
- figures.py `earth_flows`: the Sun's disc is centred at $x = -4$ (radius 52) and the Earth at $x = 304$ (radius 62). The reflected arrow runs from (262, 102) to (176, 50), so it lies between the Sun and the Earth and points up and to the left. The new description fits the drawing, and the old one ("upper right arrow") did not.
- The arrow leaves the Earth back toward space, which is physically right for reflected radiation. Its label "heijastuu", $102\,\text{W/m}^2$, sits beside it.
- The physics is unchanged. L1-05: $P_\text{rad} = 341 - 102 = 239\,\text{W/m}^2$ in balance. L2-09: $102/341 = 29.9\,\%$. Both match answers.py.
- The hash was the same at the start and at the end.
