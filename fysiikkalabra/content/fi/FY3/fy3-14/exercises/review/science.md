VERDICT: PASS
CONTENT-HASH: 2ff9673004c38076
SCOPE: delta added-exercise from 969eff4b4ef9e204 base 81db4a6fd727

## Blocking

## Polish
- exercises/solutions.md (fy3-14-L2-09) — $Q_\text{kaikki}$ is the brief's $s m_\text{j}$; with the brief's $Q_\text{j}$ (65 kJ) the same result $65 - 25 = 40\,\text{kJ}$ would make a one-line check (carried over).

## Checked
- L2-09 question now "lisälämpöä astiaan pitäisi vielä tuoda" (my previous polish point): no counterfactual about water at 0 °C giving more heat; the principle says why the heat must come from outside.
- Recomputed: heat for melting $25 - 5 = 20\,\text{kJ} < 60\,\text{kJ}$, so ice is left at 0 °C (brief's case "ei riitä"); extra heat $60 - 20 = 40\,\text{kJ}$; answers.py 40, tolerance 0,02.
- Check right: 40/60 = 2/3 of the ice unmelted, consistent with L1-03 (60 g melted, a third).
- Figure bars end at 25, 5 and 60 kJ on 5 kJ grid lines; description gives the values, not the answer.
- L1-09 unchanged: $Q = 333 \cdot 0{,}080 = 26{,}6\,\text{kJ}$.
- Every answers.py value lies inside its tolerance.
- Hash same at start and end.
