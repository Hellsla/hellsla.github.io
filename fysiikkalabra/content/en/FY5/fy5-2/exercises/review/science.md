VERDICT: PASS
CONTENT-HASH: 12fd99898cff8cce
Mode: delta (Formula steps rewritten as aligned derivations from the basic equations)
Round 1

## Blocking
(none)

## Polish
- solutions.md fy5-2-L3-01 Formula — the derivation ends at $x - x_2 = r_2 = \dfrac{m_\text{p}(x_2 - x_\text{p})}{m_\text{pt}}$, while the Substitution starts from $x = x_2 + \dots$ — add a last line $x = x_2 + \dfrac{m_\text{p}(x_2 - x_\text{p})}{m_\text{pt}}$ so the unknown is solved to the end (the old version had it).

## Checked
- All 19 Formula diffs: each new chain starts from $\Sigma M = 0$, $\Sigma F = 0$ or the centre-of-mass definition, and every algebra step is right; the end formula is the same as the old one and the one used in the Substitution.
- L1-04: $2N - mg = 0$ relies on $N_1 = N_2$, which the Principle still derives from the moment condition about the centre of mass.
- L1-05, L1-08: the balance about the centre of mass $m_1(x_\text{cm}-x_1) = m_2(x_2-x_\text{cm})$ leads correctly to $x_\text{cm} = \dfrac{m_1x_1+m_2x_2}{m_1+m_2}$.
- L3-03: $F(L-a) = mg(\tfrac{L}{2}-a) \Rightarrow (mg-F)a = \tfrac12 mgL - FL$ checked term by term.
- L3-04: force conditions, the limit $N_\text{s} = f = \mu N$ and the moments about the lower end (sin for the wall force, cos for the weights) are right; $s$ follows.
- L2-03: the geometry text only moved out of a single paragraph into paragraphs; $\tan\alpha = d/h$ is unchanged.
- Non-formula hunks: the text is the same word for word once whitespace and paragraph breaks are ignored (checked by script). The only additions are `\quad` continuation lines in the L3-03 and L3-04 Substitution displays.
- Substitutions, answers and tolerances are unchanged. Spot-recomputed: 960 N, 0.75 N, 206.7 N, 58.86 N, 0.60 m, 0.98 m, 1.6 m, 98.1 N, 555.9 N, 12.53°, 448.65 N, 61.9 kg, 209.9 N, 110.2 g, 3.333 m, 196.2 N, 1.213 m, 4.575 m, 42.2 cm and 52.97°.
- Hash is the same at the start and the end.
