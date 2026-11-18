VERDICT: PASS
CONTENT-HASH: a04e83ee8aa101f4
## Blocking

## Polish
- content/en/FY4/fy4-5/exercises/solutions.md:134 — "Newton's second law $\Sigma F_x = ma$" mixes a component and a magnitude; the other steps write $ma_x$: "$\Sigma F_x = ma_x$, and the acceleration is along $x$, so $F\cos\alpha - F_\mu = ma$".

## Checked
- Captures opened: none (text and formula changes only; judged from the files and the packet).
- Rest and constant-velocity tasks (lamp, book on the wall, person, balloon, horizontal pull at $30^\circ$, sensor ring): each starts from $\Sigma F_y = ma_y$ or $\Sigma F_x = ma_x$ with $a = 0$, then the component balance and the solved symbol; $14.715$, $4.905$, $637.65$, $0.06076$, $51.96\,\text{N}$ unchanged.
- Sensor ring: $F_\text{B}\cos\alpha = F_\text{A}$, $F_\text{B}\sin\alpha = F_\text{C}$, division gives $\tan\alpha = F_\text{C}/F_\text{A}$: correct derivation of the formula already used.
- Accelerating lifts: $N - mg = ma_y \Rightarrow N = m(g + a_y)$ with the sign of $a_y$ from the chosen $y$ up; $660.6\,\text{N}$ and $581.7\,\text{N}$ ($a_y = -1.5\,\text{m/s}^2$) unchanged.
- Perpendicular forces: $a = \sqrt{F_1^2 + F_2^2}/m = 1.0\,\text{m/s}^2$; grid forces $a = \sqrt{(F_{1x} + F_{2x})^2 + (F_{1y} + F_{2y})^2}/m = 4.0\,\text{m/s}^2$; substitution now goes into the last symbolic form.
- Friction-only tasks: $-F_\mu = ma_x$ with $a_x = (v - v_0)/\Delta t$ gives $F_\mu = m(v_0 - v)/\Delta t = 1.9\,\text{N}$ and $a = F_\mu/m = 2.5\,\text{m/s}^2$ against the motion.
- Oblique rope with acceleration: $T\cos\alpha - F_\mu = ma$, $N + T\sin\alpha - mg = 0$ (no vertical acceleration) and $a = \Delta v/\Delta t$; crane phases $a_y = (T - mg)/m$ and the phase distances unchanged.
- Vector-sum tasks open from $\Sigma\overline{F} = \overline{F}_1 + \dots$ with the overline, then components: matches the course's vector notation.
- Paragraph splits in Principle, Model answer, free-body diagrams and Reasonableness change no wording, number or claim.
- answers.py run: every numeric answer agrees with exercises.json within rounding; answers, units and tolerances identical to content/fi; git diff origin/main touches no task text, answer, unit, tolerance, id or answers.py.
