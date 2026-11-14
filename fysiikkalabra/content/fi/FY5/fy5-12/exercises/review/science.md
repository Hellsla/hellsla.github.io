VERDICT: PASS
CONTENT-HASH: 21165e7fa5250d9b
SCOPE: delta added-exercise from 37891267a0068020 base 81db4a6fd727

## Blocking

## Polish
- fy5-12/exercises/solutions.md (L3-06, Järkevyys) — "joten täydellistä vaimenemista ei syntyisi" implies that at 340 Hz the sound vanishes at P, yet s₁ = 6,0 m and s₂ = 6,5 m give unequal amplitudes, and the lesson itself says the sound "ei käytännössä katoa kokonaan". Write "joten heikentävää interferenssiä ei syntyisi".
- fy5-12/exercises (L2-09, L3-06) — L3-06 contains all of L2-09 as its first step, and its solution prints Δs = 0,50 m. This is acceptable as a progression on the same figure, but L3-06 could give s₁ and d as already read ("kuten edellisessä tehtävässä") or ask from the figure only what L2-09 does not.
- lessons/FY5/fy5-12/answers.py:327 — `import math` is repeated (it is already imported on line 284).

## Checked
- Figure data (figures.py): S1 is at (0,0), S2 is 5 squares above, and P is 12 squares to the right, with 1 square = 0,50 m. The squares are counted from grid lines, so the reading is exact. The 5-12-13 triangle gives s₂ = 6,5 m and |Δs| = 0,50 m (recomputed: 0,500).
- L2-09: answer 0,50 m with 2 significant figures, the same as the square size. Tolerance 2 % (the page's floor). A student rounding to 0,50 m is exact.
- L3-06: destructive at the lowest f means n = 0, so λ = 2Δs = 1,0 m and f = v/(2Δs) = 340 Hz (recomputed). The next frequency is 1020 Hz, which is right. The no-reflection assumption is stated in the task.
- Neither the figure nor its description writes s₁, s₂ or Δs. The alt text gives the same counts as the drawing, so nothing is given away.
- The notation follows the lesson: Δs = |s₁ − s₂|, (n + ½)λ, v = fλ. Solutions are complete in seven parts and solved in symbols first.
- answers.py lines for L2-09 and L3-06 agree with exercises.json and with my own recomputation.
- The hash was the same at the start and at the end.
