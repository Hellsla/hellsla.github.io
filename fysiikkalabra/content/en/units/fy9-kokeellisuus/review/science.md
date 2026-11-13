VERDICT: PASS
CONTENT-HASH: fdfc56cdc13d1300
Delta review (merge of #523 solution practice into #522, 2026-11-13) of the version passed at cc45b31ff1a97ba3.

## Blocking
(none)

## Polish
(none)

## Checked
Every hunk of the en merge diff (word diff). $\rho = 2677$ kg/m³ → $2.7\cdot10^3$ with $(2680 \pm 80)$ kg/m³ written to the uncertainty; rubric accepts 2680. Braking task: $a = 1/(2k) = 4.1667$ m/s², $\mu_0 \ge a/g = 0.4247$, $a/1.1025 = 3.779$ m/s², recomputed; the force equations ($N = mg$, $F_{\mu0} = ma \le \mu_0 N$) are correct. Every changed formula is symbolic before substitution and uses no symbol in a sense that differs from the unit's ```kaavat``` names or notation from #522; the $ and brace balance of each added line is checked; `units.py check` passes; the hash was taken at the start and the end and matches.
