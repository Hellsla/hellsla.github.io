VERDICT: PASS
CONTENT-HASH: d5eedf037682347f

## Blocking

## Polish
- solutions.md:270 (fy3-6-L3-04): one block holds both $E = Q$ (no losses, part a) and $E = Q + E_\text{häviö}$ (part c). Only the solved rows carry the labels a) and c). Label the rows $E = Q$ (a) and $E = Q + E_\text{häviö}$ (c), or split the block into a) and c) as L3-05 does, so the two energy balances do not read as one system of equations.
- solutions.md:238 (L3-02) and 253 (L3-03): the blocks stop before the last combination. They could end in $\Delta T = \dfrac{Q}{c\rho h \cdot 1\,\text{m}^2}$ and $V_\text{h} = \dfrac{c_\text{v} m_\text{v}}{c_\text{h}\rho_\text{h}}$ (house rule "simplify to the end"). The two-stage Sijoitus is correct.

## Checked
- I read every changed Kaava block on disk: L1-07, L2-01, L2-02, L2-03, L2-04, L2-05, L2-06, L2-07, L3-01, L3-02, L3-03 and L3-04.
- Each balance starts from $Q_\text{luov} = Q_\text{vast}$ (or $E = Pt$ with $E = Q$), then uses $Q = cm\Delta T$, then gives the combined form. Each opening equation is the basic one, as the house rule asks.
- L2-01: the same $c$ cancels, and $T = (m_1T_1 + m_2T_2)/(m_1 + m_2) = 77{,}6\,{}^\circ\text{C}$. Every algebra row is correct.
- L2-04: $T = (225 \cdot 95 + 1676 \cdot 18)/1901 = 27{,}11\,{}^\circ\text{C}$. L2-07: $T = 22{,}84\,{}^\circ\text{C}$, with $c_\text{k}m_\text{k} = 77\,\text{J/K}$ and $c_\text{v}m_\text{v} = 2095\,\text{J/K}$. Both rearrangements are correct.
- L3-01: $m_\text{k} = c_\text{v}m_\text{v}(T - T_\text{v})/(c_\text{k}(T_\text{k} - T)) = 12{,}09\,\text{kg}$. The stones cool to $40\,{}^\circ\text{C}$, not to $0\,{}^\circ\text{C}$, and the Periaate says so.
- L2-02 and L2-05: $c = Pt/(m\Delta T) = 900\,\text{J/(kg·K)}$, and $c = (P/m)(\Delta t/\Delta T) = 100/(0{,}50 \cdot 0{,}0483) = 4138\,\text{J/(kg·K)}$. The no-loss assumption is stated in Annettu.
- L2-03: $T_\text{loppu} = T_\text{alku} + Q/(cm) = 53{,}75\,{}^\circ\text{C}$. L1-07: $\Delta T = 77{,}9\,\text{K}$. Both correct.
- L2-06: equal $Q$ and $m$ give $c_\text{ö} = c_\text{v}\Delta T_\text{B}/\Delta T_\text{A} = 2083\,\text{J/(kg·K)}$. A, which warms more, is the oil.
- L3-03: equal $Q$ and $\Delta T$ give equal $cm$. $m_\text{h} = 5237{,}5\,\text{kg}$ and $V_\text{h} = 3{,}27\,\text{m}^3$. Correct.
- The condition "no change of state" ($Q = cm\Delta T$) is stated in every Periaate that uses it. The figure c-bars carries the teacher's approval. The hash was the same at the start and the end.
