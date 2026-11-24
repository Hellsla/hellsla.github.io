VERDICT: PASS
CONTENT-HASH: 093bce03ecb85ed2

## Blocking

## Polish
- solutions.md:270 (fy3-6-L3-04): the block has $E = Q$ and $E = Q + E_\text{häviö}$ as plain rows. The parts are tagged only on the solved rows, so the two energy balances can look contradictory. The Periaate states the condition, so this is not an error. Tag the rows "(a: häviöt mitättömät)" and "(c)".
- solutions.md:238 (fy3-6-L3-02): the Kaava ends with four separate rows. One combined row, $\Delta T = Q/(c\,\rho\,h \cdot 1\,\text{m}^2)$, would finish the symbolic step before substituting.

## Checked
- The packet's diff shows the `aligned` blocks flattened. I read the real multi-row blocks on disk (solutions.md:60–270).
- The balance tasks (L2-01, L2-04, L2-07, L3-01) now open with $Q_\text{luov} = Q_\text{vast}$ and then $Q = c m \Delta T$. That is the order the teacher's rule asks for.
- Each is expanded and collected correctly to the weighted mean $T = \sum c_i m_i T_i / \sum c_i m_i$, or solved for $m_\text{k}$. The signs are right, with the hot body as $T_1 - T$ and the cold body as $T - T_2$.
- Same-liquid case (L2-01): the cancelling of $c$ is shown on its own row.
- Power and heat (L2-02, L2-05, L3-04): $E = Pt$, $E = Q$, so $c = Pt/(m\Delta T)$ and $c = (P/m)(\Delta t/\Delta T)$. $P_\text{häviö} = P - cm\Delta T/t$ is correct.
- L2-06: $Q_\text{ö} = Q_\text{v}$ is justified by the same power, time and mass, not by a mixing balance, as the Periaate says. The result $c_\text{ö} = c_\text{v}\Delta T_\text{B}/\Delta T_\text{A}$ is right.
- L3-03: $\Delta T$ cancels, so $m_\text{h} = c_\text{v}m_\text{v}/c_\text{h}$ and $V_\text{h} = m_\text{h}/\rho_\text{h}$ are right.
- I evaluated each final form again with the task data: 77,9 K, 77,6 °C, 900, 53,8 °C, 27,1 °C, 4140, 2083 J/(kg·K), 22,8 °C, 12,1 kg, 3,58 K and 3,27 m³. All match the unchanged Sijoitus and answers.
- $Q = cm\Delta T$ is used only where no change of state occurs, as each Periaate says (guardrail).
- The c-bars figure is teacher-approved, and its values match the lesson table.
- The hash was the same at the start and the end.
