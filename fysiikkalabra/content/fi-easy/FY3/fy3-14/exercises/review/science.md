VERDICT: PASS
CONTENT-HASH: fac43d3c5888a291

## Blocking

## Polish
- solutions.md:111–116 (fy3-14-L2-04): the Kaava block now names the expression $K$, but the Sijoitus still calls it "Hakasulkeiden lauseke", and there are no brackets any more. Write "$K$ on" so the substitution points at the row it fills.
- solutions.md:158–160 (fy3-14-L3-03): $N$ is introduced as the left side and then set equal to $c_\text{j}(m_\text{j}+m_\text{v})T$. There is no row where the two $Q$ expressions are equated and rearranged, so the step from the balance to $N = \ldots T$ is left to the reader. A row such as "$c_\text{v} m_\text{v}\Delta T_\text{v} + s m_\text{v} - c_\text{j} m_\text{v} T = c_\text{j} m_\text{j} T - c_\text{j} m_\text{j} T_\text{j}$" before $N$ would make it explicit. The algebra is right as it stands. In the same solution, "Osoittajan termit" could be written "$N$:n termit".

## Checked
- I read all three re-laid-out Kaava blocks on disk as aligned blocks. No `array` numerators remain. $K$ and $N$ are defined in their own rows before they are used, and each block ends in the form the Sijoitus uses.
- L2-04: from $s m_\text{j} = c_\text{v} m_\text{v}(T_\text{v}-T) - c_\text{v} m_\text{j} T$ with $K = m_\text{v}(T_\text{v}-T) - m_\text{j}T$, we get $s = c_\text{v}K/m_\text{j}$. The factoring is right. Recomputed: $4190 \cdot 3{,}975/0{,}0500 = 333\,105\,\text{J/kg}$, so $333\,\text{kJ/kg}$.
- L3-03: $Q_\text{luovutettu} = c_\text{v} m_\text{v}\Delta T_\text{v} + s m_\text{v} + c_\text{j} m_\text{v}(0-T)$ and $Q_\text{vastaanotettu} = c_\text{j} m_\text{j}(T-T_\text{j})$. Equating them gives exactly $N = c_\text{j}(m_\text{j}+m_\text{v})T$. Recomputed: $(4190 + 33\,400 - 42\,000)/1260 = -3{,}5\,{}^\circ\text{C}$. The boundary test that all the water freezes ($37\,590\,\text{J} < 42\,000\,\text{J}$) is stated before the formula is used.
- L3-04: $N = c_\text{v}K - c_\text{j} m_\text{j}\Delta T_\text{j}$ and $s = N/m_\text{j}$ are correct. Part a) sets $\Delta T_\text{j} = 0$, as the task asks. Recomputed: $s_1 = 331\,\text{kJ/kg}$, $s_2 = 373\,\text{kJ/kg}$ and the corrected $s_2' = (18\,645{,}5 - 1890)/0{,}0500 = 335\,\text{kJ/kg}$.
- No answer, unit or tolerance changed. My previous checks (L2-01, L3-01, L3-02, L3-05, L2-05) still hold.
- The hash was the same at the start and the end.
