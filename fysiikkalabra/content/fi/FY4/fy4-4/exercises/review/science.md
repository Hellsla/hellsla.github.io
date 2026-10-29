VERDICT: PASS
CONTENT-HASH: af4183cda0dc00ef

## Blocking

## Polish
- solutions.md fy4-4-L2-02 — the task leaves out the counterweight and friction of a real lift; "Kannatinköyden jännitysvoima" is fine at this level (C), but one clause "kun vastavoimia ei oteta huomioon" would make the model explicit.
- solutions.md fy4-4-L3-01 — the 2-significant-figure reason (difference 6,0 kg) is right; could also say the answer 0,981 is kept to 0,98.

## Checked
- All 12 answers recomputed with my own formulas: 2,4; 120; 15; 1,5; 78,48; 3000; 7479; 1297; 0,50; 0,981 (down); 20; 6,67 — equal to exercises.json and answers.py.
- Signs and directions: L2-02 positive down, T = m(g − a); L2-03 slowing downward → a up, T = m(g + a); L3-01 N < G → a down; L3-03 only friction horizontal.
- Each force solution names the object, the forces with causes, the positive direction and the diagram (rectangle, G from centre, N from the contact face, friction from the bottom edge, v and a beside, not as forces) before the equation; symbolic first.
- Conversions (90 km/h, 36 km/h, t → kg) and significant figures justified by the limiting datum.
- Reasonableness checks are real checks (ratios to g, 2,5× mass → 2,5× time).
- Notation: \overline{} vectors, \cdot, all symbols in LaTeX.
