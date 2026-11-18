VERDICT: PASS
CONTENT-HASH: 19c370b7c9fc0c25
## Blocking

## Polish
- content/en/FY4/fy4-1/exercises/solutions.md:269 — still open from the earlier round: L2-09 Answer says the time $6.0\,\text{s}$ is "read from the graph", but the task gives it — "the velocities read from the graph and the given time $6.0\,\text{s}$ have two figures".

## Checked
- Captures opened: none (the diff is text and formulas only; judged from the files and the packet).
- Two carts: $x_{0\text{A}} + v_\text{A}t = x_{0\text{B}} + v_\text{B}t \Rightarrow (v_\text{A} - v_\text{B})t = x_{0\text{B}} - x_{0\text{A}}$ is right and ends in the unchanged display formula for $t$; B still substituted as negative.
- L3-04: from $k = \ell_\text{true}/\ell_\text{prog}$, $x = k\,x_\text{prog}$, $v = k\,v_\text{prog}$ and $x_\text{prog} = x_{0,\text{prog}} + v_\text{prog}t$ the step reaches $x = x_0 + vt$ with $x_0 = k\,x_{0,\text{prog}}$ and $t = (x - x_0)/v$; this now matches the substitution ($x_0 = 0.39\,\text{m}$, $t = 5.61/0.80 = 7.0\,\text{s}$).
- L3-05: $x_{0\text{T}} + v_\text{T}t = v_\text{P}t - v_\text{P}t_0 \Rightarrow x_{0\text{T}} + v_\text{P}t_0 = (v_\text{P} - v_\text{T})t$ is right; $t = 331/6.1 \approx 54\,\text{s}$, $x \approx 7.4 \cdot 10^2\,\text{m}$ unchanged.
- Each rewritten Formula step starts from the basic equation of uniform motion $x = x_0 + vt$ and solves symbolically before any number.
- Paragraph splits in Principle, Model answer, Reading the graph and Reasonableness (L1-05…L1-09, L3-04, L3-05, L2-09) change no wording, number or claim.
- answers.py run against exercises.json: every numeric answer agrees; answers, units and tolerances identical to content/fi.
- git diff origin/main: no task text, answer, unit, tolerance, id or answers.py line changed.
