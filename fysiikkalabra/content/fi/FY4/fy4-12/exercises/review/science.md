VERDICT: PASS
CONTENT-HASH: d363d2c649b787b2

## Blocking

## Polish
- L3-02 — "Kuinka lähelle bussia" treats the bus as a point. That is fine at this level (C). If wanted, add "(bussin takaosaan)".

## Checked
- The only change since my PASS is the kaksi_karrya docstring in figures.py, which now says "B from 40 m" and matches the drawing and the L1-04 and L2-04 solutions. Round-2 polish is fixed.
- One script recomputed all 12 answers from the task text with a general meeting-root solver (L2-04 and L3-02 by a numeric search over the gap). All agree with exercises.json and answers.py: 4,0; 20; 24; 5,0; 35; 30; 5,0; 9,0; 3,75; 2,0; 4,0; 10.
- L3-01: the roots are 2,0 s and 8,0 s, and both are named as meetings. L3-02: the discriminant is −4 m²/s² < 0, the minimum gap at 8,0 s is 4,0 m, and the gap at 6 s and at 10 s is 5,0 m. L3-03: the roots are −18 s and 10 s, and the negative root is rejected with a reason.
- Conversions are right: 90 km/h and 72 km/h are 25 m/s and 20 m/s, and 12 km / 144 km/h = 5,0 min. L2-04 states 3,8 s, gives 3,75 s as the unrounded value, and the tolerance accepts it.
- Figure fy4-12/kaksi-karrya: A goes 0→60 m and B 40→20 m in 10 s, so they meet at 5,0 s and 30 m on the grid.
- Every solution has all seven parts, solves symbolically first, rounds according to the data and checks the result by substitution. Symbols are in LaTeX, multiplication uses \cdot, and there are no vectors.
