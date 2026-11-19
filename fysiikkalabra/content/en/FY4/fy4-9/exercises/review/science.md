VERDICT: PASS
CONTENT-HASH: 228beb400ac948b4
## Blocking

## Polish
- content/en/FY4/fy4-9/exercises/solutions.md:201 (L3-04) — the subscript in $\Delta t_\text{e}$ comes from Finnish *este*; in English a reader expects e.g. $\Delta t_\text{o}$ (obstacle) or $\Delta t_\text{rigid}$.
- content/en/FY4/fy4-9/exercises/solutions.md:202 (L3-04) — Conversions omits $\Delta t_\text{e} = 25\,\text{ms} = 0.025\,\text{s}$, which the Substitution uses; add it beside $10\,\text{ms} = 0.010\,\text{s}$.
- content/en/FY4/fy4-9/exercises/solutions.md:201 (L3-04) — older text: $I = \Delta t \cdot \Sigma F$ writes the sum of the interior readings with the net-force symbol; e.g. $I = \Delta t\,(F_1 + F_2 + \dots + F_9)$.

## Checked
- Captures opened: none (one Formula and one Substitution change; judged from the diff in context).
- Round 1 Blocking fixed: the rigid-obstacle stopping time now has its own symbol $\Delta t_\text{e} = 25\,\text{ms}$, distinct from the trapezoid width $\Delta t = 10\,\text{ms}$; $F_\text{avg} = I/\Delta t_\text{e}$ is solved symbolically and the Substitution uses the same symbol.
- c) $981\,\text{N·s} / 0.025\,\text{s} = 39\,240\,\text{N} \approx 39\,\text{kN}$, unchanged; a) $981\,\text{N·s}$ and b) $14.01\,\text{m/s} = 50.45\,\text{km/h}$ unchanged.
- Sign convention unchanged and consistent: $-I = \Delta p = 0 - mv_0$, $I$ the magnitude.
- Reasonableness ($981/0.100 = 9.81\,\text{kN} < 17.4\,\text{kN}$) still uses the airbag time and is right.
- Hash identical at start and end.
