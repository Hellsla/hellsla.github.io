VERDICT: PASS
CONTENT-HASH: e099a0ff33b8b15c
## Blocking
(none)
## Polish
- solutions.md fy3-16-L3-03 Kaava — the row "E_yht = U A ΔT t + c m_j ΔT_j" has no line saying that E_yht is the total energy the ice takes. Add "E_yht = Q_luovutettu".
## Checked
- Delta: L3-03 Kaava is now one step per row. It starts from Q_vastaanotettu = Q_luovutettu and gives Q_vastaanotettu = m(c_jää ΔT_jää + s). Next come P = UAΔT, E = Pt and Q_luovutettu = E + c m_j ΔT_j. It ends in m = E_yht/(c_jää ΔT_jää + s).
- The array numerator is gone, and the old repeated rows are removed.
- Sijoitus agrees: 486 000 J + 50 280 J over 355 000 J/kg gives 1,511 kg, rounded up to 1,6 kg.
- Judged from the diff and the solutions file on disk. Hash unchanged at start and end.
