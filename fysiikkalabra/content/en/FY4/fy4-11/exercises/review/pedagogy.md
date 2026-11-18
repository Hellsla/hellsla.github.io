VERDICT: PASS
CONTENT-HASH: 254239f26e91cde1

## Blocking
(none)

## Polish
1. exercises/solutions.md (L3 collision-speed task, Formula) — the Formula paragraph now holds the whole derivation (stopping distance from u, braking over d - v_0 t_r, then v); correct, but it is long: split it after "…$s_\text{stop}$" so the first paragraph gives the distance d and the second the speed.
2. exercises/solutions.md (L2 force/distance tasks) — the Substitution now puts the main result first and the intermediate value second ("The stopping time is …"); label the second as a check ("The stopping time, for reference, is …").
3. exercises/solutions.md:143 (F against 1/Δt task, Formula) — the same row holds the impulse principle, the slope reading and the answer for $v_0$; give the last step its own sentence so the slope is clearly the product $m\,\Delta v$ read from the graph.

## Checked
- Delta: the Kaava rewrite only; numbers, answers, ids, tasks and tolerances unchanged. Recomputed the two reordered substitutions ($31.5\,\text{m}$, $11\,253\,\text{N}$): consistent.
- Force solutions start from $I = F\,\Delta t$, $p = mv$, $I = \Delta p$; friction solutions from $\Sigma F = ma$, $F_\mu = \mu N$, $N = mg$, so $a = \mu g$; distance solutions from $v = s/t$, $s_\text{b} = \tfrac12 v_0 t_\text{b}$, $t_\text{b} = v_0/a$; each ends in the symbolic form that is substituted.
- The multi-step collision-speed, following-distance and graph-intercept tasks are derived in the right order and the limiting case ($d + s_1 = s_2$) is stated.
- Paragraph splits (Principle, Reasonableness, Given, parts d and e) give one idea per paragraph; the previous polish on the long Kaava paragraph is only partly met (see 1).
- The previous L2-10 polish items (hint, overlap of b and e) are untouched by this delta.
- Captures: none opened (derivation/presentation rewrite judged from the diff).
