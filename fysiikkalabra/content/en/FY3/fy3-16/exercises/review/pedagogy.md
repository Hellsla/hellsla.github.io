VERDICT: PASS
CONTENT-HASH: 490134ab5599396c
## Blocking
(none)
## Polish
- solutions.md fy3-16 ice-box task, Formula — $E_\text{tot}$ is the sum of the heat through the wall and the heat of the drinks, but the row "$E_\text{tot} = UA\,\Delta T\,t$" ends with a "+ c m_j ΔT_j" continuation. Fine, but add "(the total energy the ice must absorb)" so the name is explained.
## Checked
- The round 1 array numerator is gone: $E_\text{tot}$ is a named quantity and the last row is $m = E_\text{tot}/(c_\text{ice}\Delta T_\text{ice} + s)$.
- Chain is right: $Q_\text{released} = E + c\,m_\text{j}\Delta T_\text{j}$, $E = Pt$, $P = UA\Delta T$, then $m(c_\text{ice}\Delta T_\text{ice}+s) = E_\text{tot}$; the repeated rows of the old version are removed.
- It starts from the balance $Q_\text{absorbed} = Q_\text{released}$ and is symbolic to the end.
- No number, unit or data changed.
- Judged from the diff and solutions.md on disk; captures not opened.
