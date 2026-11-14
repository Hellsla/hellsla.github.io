VERDICT: PASS
CONTENT-HASH: 216bb34ce703f90c
SCOPE: delta added-exercise from fb4a6839555b1dd9 base 8f23aa7ae3bd

## Blocking

## Polish
- exercises.json:269 (L2-09) — "Siirtojohdon pienoismalli" for a 200 MW line: it is a simplified model, not a scale model (the same word in L2-04 means a real small rig) — "Siirtojohdon yksinkertaistettu malli:".

## Checked
- Delta: L2-09 added; hash identical at start and end.
- loss-graph-curve is 6,0 Ω · P/U²: 3,0 % at 200 kV (grid point) and 12 % at 100 kV, as the check says.
- I = P/U = 1000 A, P_h = 0,030 P = 6,0 MW, R = P_h/I² = 6,0 Ω = answers.py; two-wire model stated in the task as the lesson requires.
- Solution starts from P_h = RI² and P = UI, symbolic before substitution; magnitude realistic.
