VERDICT: PASS
CONTENT-HASH: 65496fbb78cfc318

## Blocking

## Polish
- solutions.md fy3-16-L3-03 Formula — the energy conducted through the wall is put under $Q_\text{released}$. The outside air gives that energy and the wall only conducts it, so the label is loose. The balance itself is right. — Optional fix: name it $Q_\text{in}$ ("energy into the box"), or write $Q_\text{absorbed} = E + c\,m_\text{j}\,\Delta T_\text{j}$ directly.
- solutions.md fy3-16-L2-06 Formula — the chain ends in $UA = -k/t$, but the Substitution puts in the slope's magnitude 100 kWh/K without its sign. The result is right, because the Conversions speaks of the magnitude. — Optional fix: write $UA = |k|/t$, or substitute $k = -100$ kWh/K.

## Checked
- Diff: only Formula steps changed. Each now starts from the basic equation ($Q_\text{released} = Q_\text{absorbed}$, $E = Q$, $\eta = E_\text{useful}/E$), then the basic laws ($Q = cm\Delta T$, $Q = sm$, $Q = rm$, $E = Pt$, $P = UA\Delta T$), then the combined form. This follows the teacher's rule.
- L1-05, L2-03: the step $m/t$ is shown, giving 14 kW and 0.857 kg/s. L2-02: Q = 649 kJ.
- L2-01, L2-07: wall power times time equals $sm$, giving m = 1.617 kg (key rounded up to 1.7) and t = 2.91 h.
- L2-04: m_ice = 91.1 g. L3-01: factoring $m_\text{v}(c_\text{v}\Delta T_\text{v} + r)$ gives ΔT_k = 26.0 K.
- L3-02: the rearrangement $c\,m_\text{v}T_\text{v} - s\,m_\text{ice} = c(m_\text{v} + m_\text{ice})T$ is correct, giving T = 8.06 °C. The check 251 400 J > 167 000 J is unchanged.
- L3-03: $m(c_\text{ice}\Delta T_\text{ice} + s) = UA\Delta T\,t + c\,m_\text{j}\Delta T_\text{j}$ gives m = 1.511 kg, rounded up to 1.6 kg (limit value, guardrail).
- L2-05: η = 75.6 %. L1-08: t = 251 s. L2-09: c = 900 J/(kg·K). L2-10: t = 2.44 h.
- L2-06: $E = UAt(T_\text{in} - T_\text{out})$ is linear in $T_\text{out}$ with slope $-UAt$. UA = 139 W/K, and the axis crossing is the indoor temperature.
- L3-04: E = 5443 kWh; the costs follow from $E/\eta$ and $m = E/(\eta_\text{B}H)$. L3-05: the three stages are factored over $m$ and divided by $t$.
- I recomputed every changed solution in one script, and all match. The hash is identical at start and end.
