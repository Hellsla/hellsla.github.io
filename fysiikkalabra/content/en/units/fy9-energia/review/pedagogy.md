VERDICT: PASS
CONTENT-HASH: 0f8592564d0f83bc
Delta review (merge of #523 solution practice into #522, 2026-11-13) of the version passed at 3ee87f93108036ab.

## Blocking
(none)

## Polish
- Part c/d: $E_0$ is the line's value at $0\,{}^\circ\text{C}$ in both parts, consistent. In the wind-turbine answer $k = 0.30$ is reused for a capacity share while $k$ is a slope elsewhere in the unit; a different letter would be cleaner.

## Checked
Extrapolation formula $E = E_0 + k(T - T_0)$ with the same 230 kWh; part d $T = (E_\text{other} - E_0)/k = 16.5\,{}^\circ\text{C}$ matches the earlier text; wind turbine symbolic average power.
Read the diff hunks of this unit for how #522 notation and #523 symbolic-first solutions interact: no symbol used with two meanings inside one solution, no duplicated derivation, no contradiction with the unit text, LaTeX balanced, the answer lines still match the substitutions, and the formula still precedes the numbers (CLAUDE.md Lesson form 7). Staging of the worked solutions (Given, Find, Principle, Formula, Conversions, Substitution, Answer, Reasonableness) is intact.
