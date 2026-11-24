VERDICT: PASS
CONTENT-HASH: bdcb6b144c13c1bb

## Blocking

## Polish
- solutions.md:116 (fy3-14-L2-04): the Sijoitus still says "Hakasulkeiden lauseke", but the Kaava no longer has brackets; the quantity is now named $K$. Fix: "Ensin $K = \dots$". The numbers are right.
- solutions.md:166 (fy3-14-L3-03): the Sijoitus still says "Osoittajan termit", but the quantity is now $N$, not an array numerator. Fix: "Lausekkeen $N$ termit". Also consider adding the row $c_\text{v} m_\text{v} \Delta T_\text{v} + s m_\text{v} - c_\text{j} m_\text{v} T = c_\text{j} m_\text{j} T - c_\text{j} m_\text{j} T_\text{j}$ (solutions.md:154–161). It would show how moving terms gives $N = c_\text{j}(m_\text{j}+m_\text{v})T$; the jump is correct but not shown.
- Carried over: L2-01, L1-03, L2-06 and L3-02 open with $Q_\text{v} = \dots$ instead of $Q_\text{luovutettu} = Q_\text{vastaanotettu}$. The repeated "$Q = sm$, joten … $Q = sm$" rows are also still there.

## Checked
- I read all three changed Kaava blocks on disk (solutions.md:107–115, 154–162, 259–270), not the flattened diff. None uses an array numerator any more.
- L2-04: $K = m_\text{v}(T_\text{v}-T) - m_\text{j}T$ follows correctly from the row above by factoring out $c_\text{v}$. $s = c_\text{v}K/m_\text{j}$; $K$ comes out in kg·K, so $c_\text{v}K$ is in J. Recomputed: $3{,}975\,\text{kg·K}$ and $333{,}1\,\text{kJ/kg}$.
- L3-03: $Q_\text{luovutettu}$ and $Q_\text{vastaanotettu}$ are now written out separately, with the right signs ($c_\text{j}m_\text{v}(0-T)$ is positive for $T<0$). Equating them gives $N = c_\text{v}m_\text{v}\Delta T_\text{v} + sm_\text{v} + c_\text{j}m_\text{j}T_\text{j} = c_\text{j}(m_\text{j}+m_\text{v})T$, which is correct. Recomputed $T = -4410/1260 = -3{,}5\,{}^\circ\text{C}$, below 0 °C as the all-freezes case requires.
- L3-04: $N = c_\text{v}K - c_\text{j}m_\text{j}\Delta T_\text{j}$ and $s = N/m_\text{j}$ are correct, with $\Delta T_\text{j} = 0$ in a). Recomputed 331, 373 and 335 kJ/kg, which match the Sijoitus and the Vastaus.
- No Sijoitus, answer or answers.py value changed.
- The hash was the same at the start and the end.
