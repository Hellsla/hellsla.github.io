VERDICT: PASS
CONTENT-HASH: 78c192e9688da8a6

## Blocking

## Polish

## Checked
- I read every changed Kaava block on disk: L1-05, L2-01, L2-02, L2-03, L2-04, L3-01, L3-02, L3-03, L1-08, L2-05, L2-06, L3-04, L3-05 and L2-09.
- L3-01: the block starts from $Q_\text{luovutettu} = Q_\text{vastaanotettu}$. The juice cools, $cm_1(T_1 - T)$; the ice melts and the meltwater warms, $sm_2 + cm_2(T - T_0)$. The block collects $T$ and gives $T = (cm_1T_1 + cm_2T_0 - sm_2)/(c(m_1 + m_2)) = 16\,622{,}5/1717{,}9 = 9{,}68\,{}^\circ\text{C}$. Every row is correct. The check that the energy suffices to melt all the ice ($36\,662{,}5 > 20\,040\,\text{J}$) stays in the Periaate, as the guardrails' boundary-case rule asks.
- L3-02: $c_\text{k}m_\text{k}\Delta T = cm(T_2 - T_1) + rm$, so $\Delta T = 648\,800/24\,000 = 27{,}0\,\text{K}$. Correct.
- L3-03: subtracting the two balances eliminates $P_\text{h}$. $r = (P_1 - P_2)t/(\Delta m_1 - \Delta m_2) = 2{,}264\,\text{MJ/kg}$. The algebra is correct, and the equal loss at $100\,{}^\circ\text{C}$ is stated.
- L3-05: the steam condenses and then cools, $m_\text{h}(r + c(100\,{}^\circ\text{C} - T))$, so $m_\text{h} = 56\,565/2\,406\,650\,\text{kg} = 23{,}5\,\text{g}$. The comparison $m_\text{v} = M(T - T_0)/(100\,{}^\circ\text{C} - T) = 386\,\text{g}$ is correct, and $c$ cancels there.
- L2-01, L2-05 and L2-06: $E = Pt$, $E = Q$ and $Q = rm$ or $sm$. That gives $t = rm/P = 565\,\text{s}$, $s = P\Delta t/m$ and $m = Pt/r$. The no-loss assumption is in each Annettu.
- L2-02 and L2-04: the two-stage sums $c_\text{jää}m\Delta T + sm = 278{,}85\,\text{kJ}$ and $cm(T_2 - T_1) + rm_\text{h} = 0{,}9383\,\text{MJ}$. In L2-04 only the evaporating part takes $r$. Correct.
- L3-04: $P = cm\Delta T/\Delta t$ from the cooling liquid, then $Q = P\Delta t_\text{jähm} = sm$. The constant power is stated in Annettu.
- L1-05 and L2-09: from the melting curve, $s = 200\,\text{kJ}/0{,}60\,\text{kg} = 333\,\text{kJ/kg}$ and $c = 20\,\text{kJ}/(0{,}60\,\text{kg} \cdot 16\,\text{K}) = 2083\,\text{J/(kg·K)}$. Both agree with the grid crossings in the figure description.
- Constant temperature during a change of state is tied to a pure substance at constant pressure (L1-06, L2-10). The hash was the same at the start and the end.
