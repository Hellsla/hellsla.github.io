VERDICT: PASS
CONTENT-HASH: 1d39d74a7173b860
SCOPE: delta round 1 (work queue 8g, Kaava steps from basic equations)

## Blocking
- none

## Polish
- content/fi/FY1/fy1-3/exercises/solutions.md:143 — the last row $\Delta x_\text{v} : \Delta x_\text{t} = \Delta x_\text{v}/\Delta x_\text{t}$ only restates itself, so the simplification stops short — end with $= \dfrac{d_\text{v}}{d_\text{t}}$.
- content/fi/FY1/fy1-3/exercises/solutions.md:185 — the row $n = 7$ inside the aligned formula block is a datum, not an equation of the model — move "missä $n = 7$" back into the text after the block.

## Checked
- I checked every changed Kaava step, in L1-01–L1-05, L2-01–L2-06 and L3-01–L3-05. The formulas are right:
  - the mean as $\sum t_i/n$ with the right $n$ (4, 5, 6, 8, 7);
  - the half-range;
  - zero-error correction, starting from $m_\text{lukema} = m + m_0$;
  - $\Delta t_\text{sys} = t_\text{lukema} - t_\text{oikea} = \tau_2 - \tau_1$, with the sign right;
  - $\Delta h_1 = d/(2n)$;
  - the inequality chain giving $N \ge \Delta t/(0{,}01\,T)$;
  - the OPERA rows $s = ct$, $\Delta s = c\Delta t$.
- I recomputed the numbers myself: $N \ge 13{,}3$; ε = 4,83 %; and the means and half-ranges of L2-03 and L2-05. All are unchanged and correct.
- No answer, tolerance or wording changed. All the guardrails noted in the previous report still hold.
- The hash was 1d39d74a7173b860 at the start and at the end.
