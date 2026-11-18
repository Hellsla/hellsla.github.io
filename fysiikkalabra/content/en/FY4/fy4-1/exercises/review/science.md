VERDICT: PASS
CONTENT-HASH: 19c370b7c9fc0c25
SCOPE: delta Kaava-step rewrite, round 1 (base af340b69e0e4d6ab)
## Blocking

## Polish
- content/en/FY4/fy4-1/exercises/solutions.md:269 — carried from the previous round: L2-09 Answer says the time $6.0\,\text{s}$ is "read from the graph", but the task gives it — "the velocities read from the graph and the given time $6.0\,\text{s}$ have two figures".

## Checked
- Diff against origin/main for the en exercises: only the three Formula lines (L2 two carts, L3-04, L3-05); the paragraph splits in the packet diff change no physics.
- Two carts (line 182): from $x_\text{A} = x_\text{B}$, $(v_\text{A} - v_\text{B})\,t = x_{0\text{B}} - x_{0\text{A}}$ is right, and it gives the existing $t$ formula; B substituted as negative.
- L3-04 (line 213): $x = k\,x_\text{prog}$, $v = k\,v_\text{prog}$, $x = k\,x_{0,\text{prog}} + k\,v_\text{prog}\,t = x_0 + v\,t$ with $x_0 = k\,x_{0,\text{prog}}$, then $t = (x - x_0)/v$: correct, and it now matches the substitution ($x_0 = 1.25 \cdot 0.31 = 0.39\,\text{m}$, $t = 5.61/0.80 = 7.0\,\text{s}$).
- L3-05 (line 244): $x_{0\text{T}} + v_\text{T}\,t = v_\text{P}\,t - v_\text{P}\,t_0$ rearranges to $x_{0\text{T}} + v_\text{P}\,t_0 = (v_\text{P} - v_\text{T})\,t$; $t = 331/6.1 \approx 54\,\text{s}$, $x \approx 7.4 \cdot 10^2\,\text{m}$ unchanged.
- Each rewritten Formula step starts from the basic equation of uniform motion $x = x_0 + v\,t$ and solves symbolically before substitution.
- The three English Formula steps match the Finnish Kaava steps (lines 170, 197, 220) symbol for symbol.
- No number, answer, unit or task text changed; answers.py and exercises.json untouched.
