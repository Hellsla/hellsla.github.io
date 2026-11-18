VERDICT: PASS
CONTENT-HASH: 228beb400ac948b4

## Blocking
None.

## Polish
- solutions.md L3-04 Formula — "$I = \Delta t \cdot \Sigma F$" uses ΣF for the sum of the table's interior readings, while ΣF elsewhere is the net force; write $F_1 + \dots + F_9$ or "sum of the readings".
- solutions.md L3-04 Formula — $-I = \Delta p$ with $I$ as a magnitude is dense; say in words that the impulse points opposite to the motion.
- solutions.md L3-04 Reasonableness — the airbag time $0.100\,\text{s}$ has no symbol while $\Delta t_\text{e}$ now has one; one clause would help.

## Checked
- Round 2, delta (work queue 8g): only L3-04 Formula and Substitution changed; no number, answer or tolerance.
- The stopping-time symbol is fixed: $\Delta t = 10\,\text{ms}$ is the table step, $\Delta t_\text{e} = 25\,\text{ms}$ the stopping time against the rigid wheel; $I = F_\text{avg}\Delta t_\text{e}$ is no longer confused with the area step.
- Numbers verified from the table: interior sum $98.1\,\text{kN}$, $I = 981\,\text{N s}$, $v_0 = 14.0\,\text{m/s} = 50\,\text{km/h}$, $F_\text{avg} = 981/0.025 = 39.2\,\text{kN}$.
- Task text gives $25\,\text{ms}$, so the new symbol is defined from given data; Substitution uses the last symbolic form.
- Captures not opened: text-only change.
