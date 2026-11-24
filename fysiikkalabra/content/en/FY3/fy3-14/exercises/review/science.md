VERDICT: PASS
CONTENT-HASH: a734d296f9991e3e

## Blocking

## Polish
- solutions.md (fy3-14-L2-04, Substitution): the Formula now names the bracket expression $K = m_\text{w}(T_\text{w} - T) - m_\text{i}T$, but the Substitution still says "The expression in the square brackets is …". Fix: "$K = \ldots$". The value $3.975\,\text{kg}\cdot\text{K}$ and the final form $s = c_\text{w}K/m_\text{i}$ agree.
- solutions.md (fy3-14-L2-01): "when $Q_\text{w} > s m_\text{i}$" excludes the boundary, at which the formula still holds and gives $0\,{}^\circ\text{C}$. Fix: "$\ge$".
- solutions.md (fy3-14-L3-03, Formula): one row writing out the balance before $N$ is defined, $c_\text{w}m_\text{w}\Delta T_\text{w} + sm_\text{w} - c_\text{i}m_\text{w}T = c_\text{i}m_\text{i}(T - T_\text{i})$, would make the step to $N$ visible.

## Checked
- The Round 1 Blocking item is fixed. L2-04 is now laid out without `array` numerators. It runs from $Q_\text{released} = Q_\text{absorbed}$ through $sm_\text{i} = c_\text{w}K$ to $s = c_\text{w}K/m_\text{i}$, and the Substitution uses that last form. The Polish item about the split parenthesis is resolved too.
- L3-03: $N = c_\text{w}m_\text{w}\Delta T_\text{w} + sm_\text{w} + c_\text{i}m_\text{i}T_\text{i}$ and $N = c_\text{i}(m_\text{i} + m_\text{w})T$ are a correct rearrangement of the balance (the $T$ terms are collected, and the sign of $T_\text{i}$ is right).
- L3-04: $sm_\text{i} = c_\text{w}K - c_\text{i}m_\text{i}\Delta T_\text{i}$ is correct, and it reduces to the L2-04 form when $\Delta T_\text{i} = 0$.
- L3-05: $Q_\text{i}$ comes from a row where all the ice melts, $\Delta T_\text{i} = (Q_\text{i} - sm_\text{i})/(c_\text{i}m_\text{i})$, and the exactly-enough limit is $\Delta T_\text{w,min} = Q_\text{i}/(c_\text{w}m_\text{w})$. All correct.
- The other changed Formula steps (L1-03, L1-04, L2-01, L2-02, L2-03, L2-05, L2-06, L3-01, L3-02, L2-09) start from the balance or from $E = Pt$, $E = Q$ and solve symbolically.
- Recomputed in one script: L2-04 $333\,\text{kJ/kg}$, L3-03 $-3.5\,{}^\circ\text{C}$, L3-05 $-15.7\,{}^\circ\text{C}$ and $29.2\,{}^\circ\text{C}$, L2-01 $13.9\,{}^\circ\text{C}$, L3-01 $234\,\text{g}$, L3-02 $18.8\,\text{g}$ melts. Each matches.
- The paragraph splits leave the text unchanged. The bar figure the teacher approved was not re-judged.
- The hash was the same at the start and the end.
