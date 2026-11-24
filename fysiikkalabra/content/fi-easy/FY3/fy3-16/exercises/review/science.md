VERDICT: PASS
CONTENT-HASH: bb3a5a0cdf1e707c
Round: 2
Mode: delta

## Blocking

## Polish
- exercises/solutions.md (L3-03 Kaava) — rows are broken by hand (`&\quad +`, a numerator split inside `\begin{array}`) and the wall energy is grouped under "Q_luovutettu"; physically right, but writing Q_vastaanotettu = E + Q_juomat on one row each would be clearer.

## Checked
- Every changed Kaava starts from the basic equation (Q_luovutettu = Q_vastaanotettu, E = Pt = Q, η = E_hyöty/E, P = UAΔT) and then the basic laws, and solves the asked quantity symbolically; every row algebraically right.
- L2-01 and L3-03 (limit values): UAΔT t = sm, and m(c_jää ΔT_jää + s) = UAΔT t + c m_j ΔT_j right; rounding up unchanged.
- L2-02: Q = cmΔT + rm with the two stages stated; L3-01: ΔT_k = m_v(c_v ΔT_v + r)/(c_k m_k) right.
- L3-02: T = (c m_v T_v − s m_jää)/(c(m_v + m_jää)) right, recomputed 8.06 °C; the all-melts check stays in Periaate.
- L2-04: c m_j ΔT = s m_jää with final 0 °C right.
- L2-05: η = cmΔT/(Pt) = 75.6 %; L2-06: E linear in T_ulko, slope k = −UAt, UA = −k/t = 139 W/K right.
- L3-04: E = UAt ΣΔT, fuel energy E/η, costs and saving right; L3-05: P = m(c_vesi ΔT_1 + s + c_jää ΔT_3)/t right.
- L1-05, L2-03, L1-08, L2-07, L2-09, L2-10 single-step derivations right.
- Sijoitus and answers unchanged; hash identical at start and end.
