VERDICT: PASS
CONTENT-HASH: b724230f4c3afce5
SCOPE: delta added-exercise from 969eff4b4ef9e204 base 81db4a6fd727

## Blocking

## Polish
- exercises/exercises.json (fy3-14-L2-09, text) — "Kuinka paljon lisälämpöä veden pitäisi vielä luovuttaa": once the water is at 0 °C it can give off more heat only by freezing, so the question is a counterfactual. "Kuinka paljon lisälämpöä astiaan pitäisi vielä tuoda, jotta kaikki jää sulaisi?" (or "…enemmän lämpöä veden pitäisi voida luovuttaa") asks the same 40 kJ without that picture.
- exercises/solutions.md (fy3-14-L2-09) — $Q_\text{kaikki}$ (60 kJ) is the brief's $s m_\text{j}$, not its $Q_\text{j} = Q_\text{j,läm} + s m_\text{j}$ (65 kJ); the brief's symbols would tie the solution to the case list. With them the result is $Q_\text{j} - Q_\text{v} = 65 - 25 = 40\,\text{kJ}$, the same answer, which also makes a good one-line check.

## Checked
- L2-09 (new question, same figure): heat left for melting $25 - 5 = 20\,\text{kJ} < 60\,\text{kJ}$, so ice is left and $T = 0\,{}^\circ\text{C}$ (brief's case 2: $Q_\text{j,läm} \le Q_\text{v} < Q_\text{j}$); missing heat $60 - 20 = 40\,\text{kJ}$; answers.py gives 40.
- L2-09 agrees with L1-03 on the same figure (melted $20/334\,\text{kg} = 60\,\text{g}$, a third of the ice), so the two tasks do not contradict each other; the check (two thirds of the ice unmelted) is right because the melting heat is proportional to mass.
- L2-09 conditions: an insulated vessel ("lämpöä ei siirry astiaan eikä ympäristöön") stated; the figure's bars end on 5 kJ grid lines at 25, 5 and 60 kJ, to scale (6,6 px/kJ from one origin); the description gives the same values and not the answer.
- L1-09 (new situation): ice at 0 °C melting to water at 0 °C, so $Q = sm$ alone applies; $333 \cdot 0{,}080 = 26{,}6\,\text{kJ} \approx 27\,\text{kJ}$; with 334 kJ/kg 26,7 kJ, inside tolerance 0,04; MAFY 333 kJ/kg as in docs/mafy-arvot.tsv; the 333/334 difference is explained.
- L1-09 check (the same heat warms 0,25 kg water by about 25 K) is right; two figures from 80 g; g→kg conversion shown.
- Both solutions complete and solved symbolically before substitution; units kJ; inside FY3 (olomuodon muutokset).
- Rest of the set unchanged since PASS; hash same at start and end.
