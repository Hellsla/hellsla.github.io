VERDICT: PASS
CONTENT-HASH: 3c539493529e1ad9

## Blocking

## Polish
- solutions.md (fy3-6-L3-02, Formula): the block ends with $m = \rho V$ and $V = h \cdot 1\,\text{m}^2$ but does not combine them into $\Delta T = \dfrac{Q}{c\,\rho\,h \cdot 1\,\text{m}^2}$, the form the Substitution uses. The house rule asks for the symbolic form to the end.
- solutions.md (fy3-6-L3-03, Formula): in the same way, a last row $V_\text{s} = \dfrac{c_\text{w} m_\text{w}}{c_\text{s}\rho_\text{s}}$ would complete the derivation.

## Checked
- The diff changes only the Formula steps. No number, answer or Substitution changed.
- The mixing problems start from $Q_\text{out} = Q_\text{in}$, then use $Q = cm\Delta T$, and the algebra is right in every row. In L2-01, $c$ cancels and gives the mass-weighted mean. L2-04 and L2-07 give $T = \dfrac{\sum c_i m_i T_i}{\sum c_i m_i}$. L3-01 gives $m_\text{s}$ correctly.
- The energy balances start from $E = Pt$, $Q = cm\Delta T$ and $E = Q$. L2-02 and L2-05 then give $c = P\Delta t/(m\Delta T)$. L3-04 c) gives $P_\text{loss} = P - cm\Delta T/t$.
- L2-06: the oil, liquid A, has the larger $\Delta T$, so $c_\text{oil} = c_\text{w}\Delta T_\text{B}/\Delta T_\text{A}$ is correct.
- L3-05: the cooling power $P = Q/t$ and $k = P/(T_\text{mean} - T_\text{room})$ are consistent with the stated model.
- Recomputed: L2-01 $77.6\,{}^\circ\text{C}$, L2-04 $27.11\,{}^\circ\text{C}$, L2-07 $22.84\,{}^\circ\text{C}$, L3-03 $3.27\,\text{m}^3$, L3-04 $81.3\,\text{W}$. Each matches.
- The hash was the same at the start and the end.
