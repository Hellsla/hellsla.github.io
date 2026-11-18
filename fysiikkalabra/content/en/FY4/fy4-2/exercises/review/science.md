VERDICT: PASS
CONTENT-HASH: ff8e846ca5d74476
## Blocking

## Polish
- content/en/FY4/fy4-2/exercises/solutions.md:79 — the vertical throw's Substitution still computes $t \approx 1.529\,\text{s}$, which the final formula $h = v_0^2/(2g)$ no longer needs; it is used only in the Reasonableness check — say so ("the rise time, for the check below") or move it there.

## Checked
- Captures opened: none (text and formula changes only; judged from the files and the packet).
- Vertical throw: from $v = v_0 - gt$ and $y = y_0 + v_0t - \tfrac12 gt^2$, $v = 0$ gives $t = v_0/g$ and $h = v_0^2/g - v_0^2/(2g) = v_0^2/(2g)$; substitution into the last form $225/19.62 \approx 11.47\,\text{m}$, answer $11.5\,\text{m}$ unchanged.
- Train: triangle + rectangle + triangle areas give $s = \tfrac12 vt_1 + vt_2 + \tfrac12 vt_3 = 1162.5\,\text{m}$, unchanged.
- Fitted polynomial: starts from $y = y_0 + v_0t + \tfrac12 at^2$ and $v = v_0 + at$; $v_0 = B$, $a = 2A$, $v = B + 2At = -1.76\,\text{m/s}$.
- Scooter trapezoid $v_1t + \tfrac12(v_2 - v_1)t = 22.5\,\text{m}$; $(t^2, x)$ line from $x = \tfrac12 at^2$, $k = \tfrac12 a$, $a = 2k \approx 1.15\,\text{m/s}^2$.
- L3-04: $a = \Delta v/\Delta t$ and the interval area $v_1\Delta t + \tfrac12(v_2 - v_1)\Delta t = \tfrac{v_1 + v_2}{2}\Delta t$ is right; sums $128.3\,\text{m}$ unchanged.
- Paragraph splits (L1-06, L1-08, L2-07, L2-08, L3-04, L3-05) change no wording, number or claim.
- answers.py run: every numeric answer agrees with exercises.json within rounding; answers, units and tolerances identical to content/fi.
- git diff origin/main: no task text, answer, unit, tolerance, id or answers.py line changed.
