VERDICT: PASS
CONTENT-HASH: f349fa81cb155b7b

## Blocking

## Polish
- solutions.md (fy3-7-L3-04, Formula): the block ends with $s = Q/m$. Combining the rows gives $s = \dfrac{c\,\Delta T\,\Delta t_\text{sol}}{\Delta t}$ (the mass cancels), which would be the fully simplified form the house rule asks for. The physics is right.

## Checked
- The diff changes only the Formula steps. Its one new prose line in L3-05 introduces the comparison case, which is part of that Formula step.
- The balances start from $Q_\text{out} = Q_\text{received}$ or $E = Q$ and are solved symbolically. L2-01: $t = rm/P$. L2-05: $s = P\Delta t/m$. L2-06: $m = Pt/r$. L3-02: $\Delta T = \dfrac{cm(T_2 - T_1) + rm}{c_\text{s} m_\text{s}}$. L3-05: $m_\text{s} = \dfrac{cM(T - T_0)}{r + c(100\,{}^\circ\text{C} - T)}$, and for the comparison $m_\text{w} = M(T - T_0)/(100\,{}^\circ\text{C} - T)$, in which $c$ cancels correctly.
- L3-01: I checked each row of the rearrangement. $c(m_1 + m_2)T = cm_1T_1 + cm_2T_0 - sm_2$ is correct, and a positive $T$ confirms that all the ice melts.
- L3-03: subtracting the two balances removes the unknown loss and gives $r = \dfrac{(P_1 - P_2)t}{\Delta m_1 - \Delta m_2}$. This is correct, provided the loss power is the same at $100\,{}^\circ\text{C}$, which the task states.
- L2-02 and L2-04: the sums of the heating and phase-change heats are right.
- Recomputed: L3-01 $9.68\,{}^\circ\text{C}$, L3-02 $27.0\,\text{K}$, L3-03 $2.264\,\text{MJ/kg}$, L3-05 $23.5\,\text{g}$, L3-04 $s \approx 199\,\text{kJ/kg}$. Each matches.
- The hash was the same at the start and the end.
