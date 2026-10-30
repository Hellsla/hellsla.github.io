VERDICT: PASS
CONTENT-HASH: 3e4500116d25106f

## Blocking

## Polish
- exercises.json L2-03 / figures.py:326 — the task presents the points as the students' measurements, but the figure's description calls them "keksitty esimerkkiaineisto". Make the two say the same thing (e.g. "esimerkkiaineisto" in both).
- solutions.md:8 (L1-01) — "kolme merkitsevää numeroa kuten … massassa 160 kg": the number of significant figures in 160 kg is ambiguous. Justify the rounding with 1,62 m/s² alone.
- L1-02, L1-03, L2-02 — air resistance is not set aside in the task text, as L2-01 and L3-02 do. This is a fair simplification (C); add it only if it is done everywhere.

## Checked
- All 12 answers recomputed independently in one script and matched against answers.py and exercises.json: 259,2 N; 35,3 N; 0,306; 7,37 N; 58,9 N; 0,213; 0,807 m/s²; 0,2145 (least-squares fit through the origin); 48,2 N vs G_x 56,3 N (it slides); 0,357; 0,795 m; 0,529 m/s².
- The answer rounded to the data's significant figures stays inside the relative tolerance every time (largest gap: L2-03 2,1 % against 5 %).
- Every solution solves symbolically first, describes the diagram in words (rectangle, G from the centre, N perpendicular, friction at the corner, components dashed, a orange) and checks reasonableness. The signs agree with the stated axes.
- Physics conditions: kinetic vs static friction chosen correctly; L3-01 friction points forward; L3-02 notes that the puck stays at rest at the top only if μ₀ ≥ tan 20°; L2-04 compares μ₀N with G_x; L2-03 reads the slope from the fitted line and justifies a line through the origin.
- Scope fits FY4 (paino ja kitka, kalteva taso). Notation uses \overline and \cdot.
