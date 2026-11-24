VERDICT: PASS
CONTENT-HASH: 374766fe1b22fc4c

## Blocking

## Polish
- exercises/solutions.md (fy3-14-L2-01, fy3-14-L1-03, L2-06, L3-02 Kaava) — these balances open with $Q_\text{v} = \dots$ and go straight to the combined balance; the other tasks start from $Q_\text{luovutettu} = Q_\text{vastaanotettu}$ as the teacher's rule asks. Physics right; for consistency add that first row.
- exercises/solutions.md (fy3-14-L1-01, L1-02, L1-05, L1-07) — "$Q = sm$, joten kysytty on suoraan $Q = sm$" says the same thing twice; one row is enough.

## Checked
- The packet's diff drops the line breaks of the aligned blocks; every Kaava was read from the file on disk.
- L2-01 (0 °C ice): $Q_\text{v} = c_\text{v}m_\text{v}\Delta T_\text{v}$ is the cooling to 0 °C, so $Q_\text{v} = sm_\text{j} + c_\text{v}(m_\text{v}+m_\text{j})T$ is the right balance; 13,9 °C. The condition $Q_\text{v} > sm_\text{j}$ is stated.
- L2-04 and L3-04: $c_\text{v}m_\text{v}(T_\text{v} - T) = c_\text{j}m_\text{j}\Delta T_\text{j} + sm_\text{j} + c_\text{v}m_\text{j}T$ solved for $s$; signs right; 333 kJ/kg recomputed.
- L3-01 boundary case: final exactly 0 °C, all ice just melted, melt water not warmed (guardrail ≥ case); $m_\text{j} = c_\text{v}m_\text{v}\Delta T_\text{v}/(c_\text{j}\Delta T_\text{j} + s) = 234\,\text{g}$.
- L3-02: $m_\text{s} = (Q_\text{v} - c_\text{j}m_\text{j}\Delta T_\text{j})/s$ with the condition $c_\text{j}m_\text{j}\Delta T_\text{j} \le Q_\text{v} < Q_\text{j}$ exact; 281,2 g left.
- L3-03 (all water freezes): water gives $c_\text{v}m_\text{v}\Delta T_\text{v} + sm_\text{v} - c_\text{j}m_\text{v}T$, ice takes $c_\text{j}m_\text{j}(T - T_\text{j})$; solved $T = -3{,}5\,{}^\circ\text{C}$, below 0 °C as case 4 requires.
- L3-05: $Q_\text{j} = c_\text{v}m_\text{v}\Delta T_\text{v} - c_\text{v}(m_\text{v}+m_\text{j})T$, $\Delta T_\text{j} = (Q_\text{j} - sm_\text{j})/(c_\text{j}m_\text{j}) = 15{,}7\,\text{K}$, $T_\text{v,min} = Q_\text{j}/(c_\text{v}m_\text{v}) = 29{,}2\,{}^\circ\text{C}$.
- L2-03 $t = (c_\text{j}m\Delta T + sm)/P = 177{,}5\,\text{s}$; L2-05 $s = Pt/m = P/k = 338\,\text{kJ/kg}$; L2-02 67,7 g; L2-06 61,1 g; L2-09 $Q_\text{lisä} = Q_\text{kaikki} - (Q_\text{vesi} - Q_\text{lämm}) = 40\,\text{kJ}$.
- Numbers, Sijoitus and answers unchanged against the previous PASS. Hash the same at start and end.
