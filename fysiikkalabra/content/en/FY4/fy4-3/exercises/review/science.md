VERDICT: PASS
CONTENT-HASH: ad5de609bd6f028a
## Blocking

## Polish
- content/en/FY4/fy4-3/exercises/solutions.md:165 — the lift: $G_\text{p}$ appears first in the Formula with no name; say "the passengers' weight $G_\text{p} = mg$".
- content/en/FY4/fy4-3/exercises/solutions.md:327 — the sensor task reads "so … where … so"; e.g. "Constant velocity, so the net force is zero: $F_\text{av} - F_\text{f} = 0$, that is, $F_\text{f} = F_\text{av} = \dfrac{\Sigma F}{n}$".

## Checked
- Captures opened: none (text and formula changes only; judged from the files and the packet).
- Every rewritten Formula step (twelve tasks) now opens from the basic equation, the first law $\Sigma F = 0$ in component form along the chosen positive direction, then the third law or $G = mg$ where used, then the solved symbol; the signs agree with each task's force diagram and positive direction.
- Lift: $T - G_\text{c} - G_\text{p} = 0$, $G_\text{p} = mg$ gives $T = G_\text{c} + mg = 8939.2\,\text{N} \approx 8.9\,\text{kN}$, unchanged.
- Horse and cart: both bodies separately, $T = F_\text{r} + F_\text{k} = 450\,\text{N}$ and $F_\text{t} = T + F_\text{h} = 480\,\text{N}$, unchanged.
- Stacked books, magnets, scales: first law on each body plus the third-law pair ($F_2 = G_2$, $F_\text{m} = G$, $F_\text{a} = G_\text{a}$) give the unchanged $13\,\text{N}$, $0.60\,\text{N}$, $1.9\,\text{N}$.
- Sensor task: constant velocity, so friction equals the mean pull $10.2/3 = 3.40\,\text{N}$, unchanged.
- Paragraph splits (force diagrams, Principle, Model answer, Reasonableness) change no wording, number or claim; the third-law pairs stay between the bodies that interact.
- answers.py run: every numeric answer agrees with exercises.json within rounding; answers, units and tolerances identical to content/fi.
- git diff origin/main: no task text, answer, unit, tolerance, id or answers.py line changed.
