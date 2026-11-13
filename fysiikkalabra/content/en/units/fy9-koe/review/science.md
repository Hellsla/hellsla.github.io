VERDICT: PASS
CONTENT-HASH: 33038199a3b55af5
Delta review (merge of #523 solution practice into #522, 2026-11-13) of the version passed at 33038199a3b55af5.

## Blocking
(none)

## Polish
1. sovella/solutions.md, pendulum c) Answer: the reason for two significant figures ("$0.46\,\text{s}^2$ has two digits") is not the rule for a difference: $3.68 - 0.46 = 3.22$ is known to the hundredth, i.e. three figures. $9.8\,\text{m/s}^2$ is still the right rounding given the stated reading uncertainty $\pm 0.3\,\text{m/s}^2$; giving that as the reason would be cleaner. The rubric accepts $9.8$ or $9.81$, so assessment is consistent.

## Checked
Every hunk of the en merge diff (word diff). $g = 4\pi^2/k$ with $k = 3.22/0.800 = 4.025$ s²/m gives 9.808 m/s², recomputed; unit.md rule on exact quantities (integers, conversion factors) correct. Every changed formula is symbolic before substitution and uses no symbol in a sense that differs from the unit's ```kaavat``` names or notation from #522; the $ and brace balance of each added line is checked; `units.py check` passes; the hash was taken at the start and the end and matches.
