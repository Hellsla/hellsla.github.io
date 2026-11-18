VERDICT: PASS
CONTENT-HASH: 06ba6f297e70e37e

## Blocking
(none)

## Polish
1. exercises/solutions.md (bus and runner, minimum-distance task, Substitution) — $s_\text{min} = -(-20\,\text{m}) - \dfrac{(4.0\,\text{m/s})^2}{2 \cdot 0.50\,\text{m/s}^2}$ is correct but the double minus is hard to follow; add the symbolic last form $s_\text{min} = -x_{0\text{R}} - \dfrac{v^2}{2a}$ to the Formula row, since the Substitution now uses it.
2. exercises/solutions.md (several meeting tasks) — the same "In uniform motion $x = x_0 + v\,t$ … At the meeting $x_\text{A} = x_\text{B}$" opening is repeated in about ten solutions; harmless, but the tasks with a quadratic could name the origin and positive direction once at the start of the Principle.
3. exercises/solutions.md (graph-intersection task, Formula) — "From the graph $t$ is also read directly…" ends without a full stop; add one.

## Checked
- Delta: the Kaava rewrite only; numbers, answers, ids, tasks and tolerances unchanged.
- Every meeting and passing solution now starts from $x = x_0 + v\,t$ (or $x = x_0 + v_0 t + \tfrac12 a t^2$), writes each body's position, sets the positions equal, and solves for $t$ in symbols before the Substitution.
- The three Substitution rows that changed ($2.0 - (-3.0)$, $6.0 - (-2.0)$, the minimum distance $20 - 16 = 4.0\,\text{m}$) give the same values as before and follow the last symbolic form; recomputed.
- The accelerated cases state the quadratic, the condition under the root, and the choice of the root; the maximum-gap task derives $s_\text{max} = \tfrac12 t v_\text{A}$ from $s = v_\text{A} t - \tfrac12 a t^2$ and equal velocities.
- Paragraph splits (Reading the graph, Principle, Model answers) give one idea per paragraph; the Formula label starts its own line.
- Captures: none opened (derivation/presentation rewrite judged from the diff; the open-solution captures predate it).
