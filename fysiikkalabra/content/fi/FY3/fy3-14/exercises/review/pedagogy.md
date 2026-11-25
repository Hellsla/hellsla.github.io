VERDICT: PASS
CONTENT-HASH: bdcb6b144c13c1bb
## Blocking
(none)
## Polish
- solutions.md L2-04, L3-03, L3-04 Kaava — the helper symbols K and N are not announced in the text, and they clash with the units K (kelvin) and N (newton) — name them (for example $A$ and $B$, or "merkitään hakasulkeen lauseketta kirjaimella …") and use a short note after the block.
- solutions.md L2-04 Sijoitus — "Hakasulkeiden lauseke" no longer matches the block, which now has K — write "Lauseke $K$ on …".
- solutions.md L3-03 Sijoitus — "Osoittajan termit" refers to a numerator that no longer exists now that the block ends in N — say "Lausekkeen $N$ termit".
## Checked
- Delta: array-numerator fractions replaced by named intermediate quantities, laid out one equation per row, no horizontal overflow risk.
- Algebra read from the file. L2-04: s m_j = c_v K with K = m_v(T_v - T) - m_j T. L3-03: N = c_v m_v ΔT_v + s m_v + c_j m_j T_j = c_j(m_j + m_v)T. L3-04: N = c_v K - c_j m_j ΔT_j and s = N/m_j. All correct and consistent with Sijoitus and answers.
- The chains start from Q_luovutettu = Q_vastaanotettu and simplify symbolically to the end.
- Judged from the solutions text; captures not opened.
