VERDICT: PASS
CONTENT-HASH: f9189f30c9a2f688
SCOPE: delta added-exercise from 734da372eebee885 base 81db4a6fd727
## Blocking

## Polish

## Checked
- Round 2 diff, L3-06 Answer: "$m_1 \approx 1.2\,\text{kg}$, two significant figures" is now consistent (my earlier polish item is fixed). The calculated $1.21\,\text{kg}$ stays as answer with 4 % tolerance, and 1.2 is 0.8 % away.
- L3-06 recomputed: $m_1 = 0.30\,(9.81/1.95 - 1) = 1.209\,\text{kg}$; $T = 2.36\,\text{N} < m_2 g = 2.94\,\text{N}$.
- L2-09 recomputed: $a = 3.9/2.0 = 1.95\,\text{m/s}^2$, $T = 0.80 \cdot 1.95 = 1.56\,\text{N} \to 1.6\,\text{N}$.
- The force diagrams are unchanged and agree with the motion (equal $T$ for a light string and pulley, acceleration not drawn as a force).
- The Finnish diff makes the same change.
- answers.py run: every entry equals exercises.json or differs only by rounding inside its tolerance.
- Script comparison with content/fi: every number in the texts and solutions.md identical.
