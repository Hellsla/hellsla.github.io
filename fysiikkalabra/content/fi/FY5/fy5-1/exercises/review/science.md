VERDICT: PASS
CONTENT-HASH: cccfc1b2c9ae2b50
SCOPE: delta added-exercise from 23f25874b515562a base 81db4a6fd727

## Blocking

## Polish
- exercises.json:145 (L1-10): this figure has only one reading, the arm of 3 squares, and L1-04 uses the same figure for that same reading. L1-10 only reverses the unknown (F from M instead of M from F), so the figure work is a repeat. It gives nothing of L1-04 away, because the task text states no arm and no moment of L1-04. Acceptable. If the figure needs a new reading, ask instead for the force at a point P' at another height.

## Checked
- The hash was the same at the start and at the end. Only L1-10 was judged, as the delta packet says.
- Recomputed from the figure data in `figures.py`. P lies 4 squares right of O and 3 squares above it, and the horizontal line of action passes through P, so the arm is 3 · 0,10 m = 0,30 m. Then F = M/r = 21 Nm / 0,30 m = 70 N, which equals answers.py and exercises.json.
- The trap is right: the bar length is 5 squares (3-4-5), and using 0,50 m would give 42 N, as the reasonableness check says.
- Sig figs: M = 21 Nm has 2, so the answer 70 N has 2. A student who rounds stays well inside the 2 % tolerance.
- The figure's description holds the same information as the drawing. Neither the figure nor the description gives the arm or the answer.
- Notation ($M = Fr$, the arm $r$ as the perpendicular distance from O to the line of action) is the brief's. The task stays inside fy5-1.
- The solution has all seven parts. F is solved in symbols first. The reasonableness check is a real check: it multiplies back and compares with the bar-length mistake.
