VERDICT: FAIL
CONTENT-HASH: a45dcdabb4f5a4b1

## Blocking
- solutions.md:209 (L3-03) — A: the rounding is justified by the wrong rule. N = 0,10 N − 0,0392 N is a difference, and 0,10 N is known only to 0,01 N, so the result is good to about 0,01 N. That gives 0,06 N, not "kaksi merkitsevää numeroa … 0,061 N". The lesson's exp-1 solution teaches this exact rule ("Erotuksessa ratkaisee desimaalien määrä, ei merkitsevien numeroiden määrä"). — Answer 0,06 N with that reason; exercises.json 0.061 stays within tolerance, or set it to 0.06.

## Polish
- solutions.md:78 (L1-05) — "kulma 40° … eikä 250 N ole sitä tarkempi" is a shaky reason, since 250 N may have three significant figures. Simpler: two significant figures, as in the angle, the least precise datum.
- solutions.md L1-03 — the rendered diagram draws the wall's N̄ across the book from the contact face. This follows the convention (it starts at the contact surface), but a push-style arrow ending at the face would read more clearly.

## Checked
- Recomputed all twelve answers in one script with my own formulas: 14,7 / 15 / 4,9 / 637,7 / 191,5 / 52,0 / 660,6 / 0,598 / 1,0 / 581,7 / 1,9 / 0,0608. All agree with answers.py and exercises.json, within tolerance.
- Models: static friction on the wall equals mg; a lift moving up and slowing has downward a, so N < G; the curling stone has no forward force; the ceiling's N points down, with F_noste = G + N; the L2-04 pulls add as vectors.
- Every solution goes diagram → axes → equations → symbolic → numbers, with units and a real reasonableness check.
- Rendered all 11 voimakuvio blocks: correct forces, directions and relative lengths; v and a are off the body; no third-law pairs; components are dashed; every body is a rectangle.
- Figures ruutu, malli-pulkka and malli-hissi match their tasks and descriptions; ruutu gives the values without giving away the answer.
- Scope is within FY4; L3-02 uses a = Δv/Δt from the earlier chapter.
- The hash was a45dcdabb4f5a4b1 at both start and end.
