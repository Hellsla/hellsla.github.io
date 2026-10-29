VERDICT: PASS
CONTENT-HASH: e946aeb0cf3ea333

## Blocking

## Polish
- lessons/FY4/fy4-12/figures.py:232 — the kaksi_karrya docstring says B starts "from 30 m", but the drawing (which L1-04 and L2-04 read) starts it at 40 m. — Fix the comment.
- L3-02 — "Kuinka lähelle bussia" treats the bus as a point. That is fine at this level (C); if wanted, add "(bussin takaosaan)".

## Checked
- One script recomputed all 12 answers from the task text with a general meeting-root solver (L3-02 by a numeric minimum of the gap). All agree with exercises.json and answers.py: 4,0; 20; 24; 5,0; 35; 30; 5,0; 9,0; 3,75; 2,0; 4,0; 10.
- L3-01 roots are 2,0 s and 8,0 s, and both are named as meetings. In L3-02 the discriminant is −4 m²/s² < 0, the minimum gap at v_bus = v_runner is 4,0 m, and the 5,0 m values at 6 s and 10 s are checked. L3-03 rejects the root −18 s with a reason.
- Round-1 A (L1-04, "vaakasuoran ruudukkoviivan") is fixed. L2-04 states 3,8 s as the answer and 3,75 s as the unrounded value. The 2 % tolerance accepts 3,8.
- Figure fy4-12/kaksi-karrya: A goes 0→60 m and B 40→20 m in 10 s. The meeting at 5,0 s and 30 m lies on the grid as the L1-04 solution reads it.
- Conversions are right: 90/72 km/h = 25/20 m/s, and 12 km / 144 km/h = 5,0 min.
- Every solution has all seven parts, is solved symbolically first, rounds by the data, and has a real check by substitution.
- Standing rules: all symbols are in LaTeX, multiplication uses \cdot and × never appears. No vectors or arrows appear in this set.
