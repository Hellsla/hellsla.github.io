VERDICT: PASS
CONTENT-HASH: 6b9b9e1b703a33c2

## Blocking
None.

## Polish
None left. All four points from the review of hash 58e6d75f8b62d752 are fixed:
1. Teoria now gives the real reason for avoiding a reflector or lens. They redirect the light, so it appears to come from somewhere other than the glowing part, and the model fails worst near the lamp.
2. Tuki O says that the lamp-off reading removes ambient light only. The lamp's own light reflected from the room stays as a systematic error that raises the far readings most.
3. The power-fit paragraph says that distances which are too small throughout (measured from the bulb's glass) also give $|n|<2$, and links this to the Laajennus. My check: $d=2$ cm gives $n\approx-1.91$.
4. The $E_\text{tausta}$ label is now left of the axis at its tick (checked rendered).

## Checked
- $E=I/r^2$ is derived from the straight-edged beam ($A\to4A$). Its conditions are stated: a point source, no absorption, a steady lamp, direct light only, the sensor face perpendicular and always in the same direction, no reflector or lens.
- Spread figure: side/distance is 70/190 = 140/380, and the rays pass through the corners of both squares. The labels $A$, $4A$, $r$ and $2r$ are correct.
- Background: the reading is $I/r^2+E_\text{tausta}$. On the $E$–$1/r^2$ graph the slope is unchanged and the intercept is $E_\text{tausta}$, in both text and figure. Without subtraction $|n|<2$, which I checked numerically.
- Power fit $E=A\cdot r^n$: $n=-2$ is predicted, and the test is whether $-2$ lies within $n\pm\Delta n$.
- Extension, now with its equations in a tuki O OO block: $1/\sqrt{E}=r/\sqrt{I}+d/\sqrt{I}$, the line meets the horizontal axis at $r=-d$, and $d=b/a$. $d>0$ means the measured distance is too short. The background is subtracted before the root. The new hint is correct: far points are made uncertain by background and reflections, and near points carry the information on $d$. Mode I derives it itself.
- Uncertainty: the sum rule for a difference, $2\Delta r/r$ for $1/r^2$, the fit standard error or steepest/shallowest lines with $\Delta I=(I_\text{max}-I_\text{min})/2$, rounding, and "sopusoinnussa, ei todista".
- No invented equipment values, safety limits or menu names.
- Figures show models only, with no measured points. Labels are LaTeX, and there are no arrows.
- Card (pp. 4–5): the aim, a model compared with theory, both tips and the uncertainty request are all present. FY7 is explained on the page.
