VERDICT: PASS
CONTENT-HASH: 490134ab5599396c

## Blocking

## Polish
- solutions.md (fy3-16-L3-03, Formula): $E_\text{tot}$ is the same quantity as $Q_\text{released}$, so two names stand for one quantity. Writing the row as $Q_\text{released} = UA\,\Delta T\,t + c\,m_\text{j}\,\Delta T_\text{j}$, or "$E_\text{tot} = Q_\text{released}$", would make that visible. The earlier note still applies: the outside air gives the wall's energy and the wall only conducts it, so a label such as $Q_\text{in}$ would be more exact.
- solutions.md (fy3-16-L2-06, Formula): as before, the chain ends in $UA = -k/t$ while the Substitution uses the magnitude $100\,\text{kWh/K}$. $UA = |k|/t$ would match.

## Checked
- Only L3-03's Formula changed. The `array` numerator is gone, and the chain now runs from $Q_\text{absorbed} = Q_\text{released}$ through the basic laws ($Q = m(c_\text{ice}\Delta T_\text{ice} + s)$, $P = UA\,\Delta T$, $E = Pt$) to $m = E_\text{tot}/(c_\text{ice}\Delta T_\text{ice} + s)$.
- $E_\text{tot} = UA\,\Delta T\,t + c\,m_\text{j}\,\Delta T_\text{j}$ is $Q_\text{released}$ with $E = Pt$ substituted, which is correct. The Substitution adds exactly these two terms.
- Recomputed: wall $486\,000\,\text{J}$, drinks $50\,280\,\text{J}$, $355\,000\,\text{J/kg}$ and $m = 1.511\,\text{kg}$. It is rounded up to $1.6\,\text{kg}$ as a limit value, following the guardrail.
- The constant wall power is justified by the stated assumption that the inside is at $0\,{}^\circ\text{C}$.
- Nothing else changed since the earlier PASS.
- The hash was the same at the start and the end.
