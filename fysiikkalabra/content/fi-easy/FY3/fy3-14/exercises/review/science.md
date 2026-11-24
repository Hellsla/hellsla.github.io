VERDICT: PASS
CONTENT-HASH: dcf9a25f9b327a71
Round: 2
Mode: delta

## Blocking

## Polish
- exercises/solutions.md (L2-04, L3-03, L3-04, L3-05, Kaava) — rows are broken by hand (`&\quad +`, a numerator split inside `\begin{array}`, in L2-04 and L3-04 even inside the bracket "(T_v \\ − T)"); the house rule leaves wrapping to the page — keep each equation on one row.

## Checked
- Every changed Kaava starts from Q_luovutettu = Q_vastaanotettu (or E = Pt = Q) and then Q = cmΔT, Q = sm, and solves the asked quantity symbolically; every row algebraically right.
- L2-01: c_v m_v ΔT_v = s m_j + c_v(m_v + m_j)T is the correct balance with 0 °C as reference; recomputed 13.94 °C.
- L3-01 boundary case (exactly melted, final 0 °C) m_j = c_v m_v ΔT_v/(c_j ΔT_j + s) right, 234 g.
- L3-02, L2-06, L1-03: ice warmed first, m_s = (Q_v − c_j m_j ΔT_j)/s right; boundary comparison stated.
- L3-03 all water freezes: released c_v m_v ΔT_v + s m_v − c_j m_v T, received c_j m_j(T − T_j); T = −3.5 °C recomputed, matches answers.py.
- L2-04, L3-04: s = [c_v m_v(T_v − T) − c_v m_j T (− c_j m_j ΔT_j)]/m_j right; recomputed 335 kJ/kg.
- L3-05: Q_j from the balance, then ΔT_j and the minimum water temperature Q_j/(c_v m_v) right.
- L2-05: s = Pt/m = P/k with k the (t, m) slope right.
- Sijoitus and answers unchanged; hash identical at start and end.
