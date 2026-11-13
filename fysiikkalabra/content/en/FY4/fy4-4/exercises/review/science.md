VERDICT: PASS
CONTENT-HASH: 7441d559115f1f83
SCOPE: delta added-exercise from 61bbd8dbfca10bbc base 81db4a6fd727
## Blocking

## Polish

## Checked
- Round 2 change, L2-09 now asks about cart A: $m_\text{A} = 3.0\,\text{N} / 6.0\,\text{m/s}^2 = 0.50\,\text{kg}$, $a = 2.4\,\text{N} / 0.50\,\text{kg} = 4.8\,\text{m/s}^2$ (recomputed). The answer no longer equals the given force, as it did for B at $1.0\,\text{kg}$.
- L2-09 reasonableness: A's line at $2.4\,\text{N}$ lies between $4$ and $6\,\text{m/s}^2$, which is right. The text, answer, Given, Reading, Substitution and Answer all name cart A.
- L1-09 unchanged: $F = m(g + a) = 15\,000 \cdot 2.122 = 31.83\,\text{kN}$. L1-10: $m_\text{A} = 0.50\,\text{kg}$.
- Figure kuvaaja-ab: the English labels "cart A" and "cart B" were added to figures.json. The points (1;2), (2;4), (3;6) for A agree with the solutions.
- answers.py: the new `m_A` line gives 4.8, which equals exercises.json. Other entries differ only by rounding inside their tolerance (unchanged).
- Script comparison with content/fi: answers, units, tolerances, figure ids and every number in the texts and solutions.md identical.
