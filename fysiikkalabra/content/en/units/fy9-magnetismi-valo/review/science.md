VERDICT: PASS
CONTENT-HASH: 086631afee2d127b
Delta review (merge of #523 solution practice into #522, 2026-11-13) of the version passed at bf5117373f141a6c.

## Blocking
(none)

## Polish
1. sovella/solutions.md: $\beta$ is now the decibel factor in the fibre-link task while the refraction task earlier in the same file uses $\beta_\text{max}$ for an angle. They are separate tasks, so nothing contradicts, but another letter would avoid the clash.

## Checked
Every hunk of the en merge diff (word diff). $P_\text{h}/P = RP/U^2$; fibre $A = aL + N_\text{s}A_\text{s}$, $P = P_0\cdot10^{-A/\beta}$ ($\beta = 10$ dB) consistent with the unit's decibel formula; grating $d = 1/N$, $\lambda = \sin(\tan^{-1}(x_k/L))/(kN)$. Every changed formula is symbolic before substitution and uses no symbol in a sense that differs from the unit's ```kaavat``` names or notation from #522; the $ and brace balance of each added line is checked; `units.py check` passes; the hash was taken at the start and the end and matches.
