VERDICT: FAIL
CONTENT-HASH: c181f69fde99c348

## Blocking
- solutions.md:111/114 (fy3-14-L2-04) — category A, internal consistency. The new Formula ends in the unfactored form $s = [c_\text{w} m_\text{w}(T_\text{w} - T) - c_\text{w} m_\text{i} T]/m_\text{i}$. The unchanged Substitution (line 114) still says "The expression in the square brackets is $0.200\,\text{kg} \cdot 21.9\,\text{K} - 0.0500\,\text{kg} \cdot 8.1\,\text{K}$" and then multiplies by $c_\text{w}$. That is the old factored form $c_\text{w}[m_\text{w}(T_\text{w} - T) - m_\text{i}T]/m_\text{i}$, which the Formula no longer contains. There are no square brackets to refer to, and the Substitution no longer substitutes into the last symbolic form (house rule: simplify to the end, substitute into the last form). — Fix: add a final row $s = \dfrac{c_\text{w}\left[m_\text{w}(T_\text{w} - T) - m_\text{i}T\right]}{m_\text{i}}$ to the Formula. This also removes the `array` split of the parenthesis $(T_\text{w}\ \backslash\backslash\ -T)$ at line 111.

## Polish
- solutions.md:65 (L2-01) — "when $Q_\text{w} > s m_\text{i}$" excludes the boundary, but the formula also holds there and gives exactly 0 °C (guardrail: "≥, not >"). This wording predates the change. — Fix: "$Q_\text{w} \ge s m_\text{i}$".
- solutions.md:111 (L2-04) and fy3-14-L3-04 Formula — the `array` numerators split $(T_\text{w} - T)$ across two rows. The physics is right, but the expression is hard to read. — Fix: break only between terms.

## Checked
- Diff: only Formula steps changed. Each starts from $Q_\text{released} = Q_\text{absorbed}$ (or $E = Pt$, $E = Q$), then the basic laws $Q = cm\Delta T$ and $Q = sm$, then solves symbolically.
- L2-01: the form $Q_\text{w} = sm_\text{i} + c_\text{w}(m_\text{w} + m_\text{i})T$ correctly rewrites $c_\text{w}m_\text{w}(30\,\text{K} - T) = sm_\text{i} + c_\text{w}m_\text{i}T$. T = 13.9 °C.
- L3-02: the validity range (water warms the ice, but not enough to melt all of it) is stated, and the final state is 0 °C. Left: 281 g.
- L3-03 (all the water freezes): every term (cooling, freezing, cooling of the new ice, warming of the old ice) has the right sign, and the rearrangement is correct. T = −3.5 °C.
- L3-01: factoring $m_\text{i}(c_\text{i}\Delta T_\text{i} + s)$ gives 234 g.
- L3-05: $c_\text{w}m_\text{w}\Delta T_\text{w} = Q_\text{i} + c_\text{w}(m_\text{w} + m_\text{i})T$ is correct. The limit $T_\text{w,min} = Q_\text{i}/(c_\text{w}m_\text{w})$ is the exactly-enough case at 0 °C. $Q_\text{i}$ = 36.7 kJ.
- L2-05: $s = Pt/m = P/k$ with $k = m/t$, which is correct.
- L1-03, L1-04, L2-02, L2-03, L2-06, L2-09: the chains are consistent with their Substitutions. I recomputed them in one script, and all match.
- The hash is identical at start and end.
