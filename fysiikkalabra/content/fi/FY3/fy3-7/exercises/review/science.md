VERDICT: PASS
CONTENT-HASH: 8bb8903fbb269fb9

## Blocking

## Polish
- solutions.md:311 (fy3-7-L3-04): the Kaava stops at $s = Q/m$ with $Q$ and $P$ on earlier rows. One more row would finish the symbolic step, $s = \dfrac{c\,\Delta T\,\Delta t_\text{jähm}}{\Delta t}$ (the mass cancels), before the Sijoitus.

## Checked
- The packet's diff shows the `aligned` blocks flattened. I read the real multi-row blocks on disk (for example solutions.md:311 and :346–360).
- The changed blocks open with the basic laws: $E = Pt$, $Q = sm$, $Q = rm$, $Q = cm\Delta T$, or $Q_\text{luovutettu} = Q_\text{vastaanotettu}$ in the balance tasks. The combined equation comes only after them, as the teacher's rule asks.
- Algebra checked row by row, all correct:
  - $s = Q/m$, $t = rm/P$, $m = Q/s$, $m = Q/r$, $m = Pt/r$, $s = P\Delta t/m$, $c = Q/(m\Delta T)$
  - two-stage heating, $Q = c m\Delta T + sm$ or $+ r m_\text{h}$, with $\Delta T = 0\,{}^\circ\text{C} - T_1$ positive
  - juice and ice: $T = (cm_1T_1 + cm_2T_0 - sm_2)/(c(m_1+m_2))$, from correct collecting
  - sauna stones: $\Delta T = (cm(T_2-T_1) + rm)/(c_\text{k}m_\text{k})$
  - two-power method: $P_\text{h}$ cancels on subtracting, so $r = (P_1-P_2)t/(\Delta m_1-\Delta m_2)$
  - steam into milk: $m_\text{h} = cM(T-T_0)/(r + c(100\,{}^\circ\text{C} - T))$ and $m_\text{v} = M(T-T_0)/(100\,{}^\circ\text{C} - T)$
- I evaluated each final form again with the task data: 333 kJ/kg, 9,42 min, 279 kJ, 35,9 kg, 0,938 MJ, 9,68 °C, 27,0 K, 2,26 MJ/kg, 0,602 kg, 23,5 g against 386 g, and 2,1·10³ J/(kg·K). All match the unchanged Sijoitus.
- Juice and ice boundary case: the Periaate shows that the juice can give 36,7 kJ while melting needs only 20,0 kJ, so all the ice melts. The guardrail's case split holds.
- Each use of a phase-change formula says the temperature stays constant at constant pressure while the state changes.
- The hash was the same at the start and the end.
