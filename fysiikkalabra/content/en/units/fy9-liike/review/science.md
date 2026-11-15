VERDICT: FAIL
CONTENT-HASH: b242489c281d686d
Review of the recognition chart (queue 9c) and the term change against the version passed at 8e16b09b0e569f61; full on the chart, delta on the rest.

## Blocking
- **B, chart row 4 and aria-label: "acceleration not known → average velocity, $\Delta x = \tfrac{v_0 + v}{2}t$".** The mean of the initial and final velocity equals the average velocity only in uniformly accelerated motion; the Formula section derives it under exactly that condition. As written, the sign invites the classic error of using it for any motion whose acceleration is not given (a curved $(t,v)$ graph). Fix: "constant acceleration, $a$ not given".

## Polish
- Row 7 "distance from the velocity graph → area" is right for the geometric area, but the Formula section says the area is the displacement with the part below the axis negative; naming both (or "displacement") would match it. Row 3 "distance?" leads to the position formula, which gives a displacement.

## Checked
- Rows 1–3, 5–6: $x = x_0 + vt$ at constant velocity; $v = v_0 + at$ and $x = x_0 + v_0t + \tfrac12at^2$ at constant acceleration; slopes $v = \Delta x/\Delta t$, $a = \Delta v/\Delta t$. Agree with the Formula section.
- The aria-label matches the chart.
- Term change: the diff's other lines are "concept map" -> "recognition chart" in teacher.md and new figures.json keys; no formula, number or task changed.
- The en chart (docs/figures/fy9-tunnistus/fy9-liike-en-360.png) and the hash, taken at the start and the end (b242489c281d686d).
