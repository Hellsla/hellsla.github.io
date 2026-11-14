VERDICT: PASS
CONTENT-HASH: 6252f2afbde508b5
SCOPE: delta added-exercise from 5b627e2749906f73 base 5a45b28682e8

## Blocking

## Polish
- lessons/FY8/fy8-1/answers.py:45 — the comment says "387,6 nm -> 388 nm", but the line computes 387,50 nm, which is the exercise's answer of 387 and the value in solutions.md (387,5 nm). Only the comment is wrong. — Change the comment to "387,5 nm -> 387 nm".
- solutions.md fy8-1-L2-09 Vastaus — the step from a reading with two significant figures (7,0e14 Hz) to an answer with three (428 nm) is justified only by "±1 %". — Say the reading is about ±0,1e14 Hz, so the result is about 428 nm ± 6 nm. That is also why the tolerance is 4 %.

## Checked
- Delta scope: only the three added exercises were judged: fy8-1-L1-10, L2-08 and L2-09.
- fy8-1-L1-10: λ0 = hc/W with W = 3,20 eV gives 387,5 nm. The answer 387 is right and the 5 % tolerance is fine. The MAFY value for calcium, 3,20 eV, matches docs/mafy-arvot.tsv, which lists it as VERIFIED. 387 nm is UV-A, as the solution says ✓.
- fy8-1-L2-08: the figure's line A has W = 2,30 eV, so f0 = 5,561e14 Hz. At 12e14 Hz, (h/e)f − W = 4,963 − 2,30 = 2,663 eV. Reading f0 ≈ 5,6e14 Hz gives 2,647 eV, which is also inside the 5 % tolerance ✓.
- fy8-1-L2-09: line B has W = 2,90 eV, so f0 = 7,011e14 Hz. That is halfway between the 6 and 8 grid lines, as the solution says. c/7,0e14 Hz = 428,3 nm, and the exact f0 gives 427,6 nm; both are within the 4 % tolerance ✓. The error-analysis remark (the vertical intercept is −W, not f0) is correct.
- The figure is drawn to scale from the same work functions (2,30 and 2,90 eV) that answers.py uses. Its two lines are parallel with slope h/e and start on the horizontal axis at their own f0. The lines end inside the axes: 4,32 eV and 3,72 eV at 16e14 Hz. The figure does not give away any answer ✓.
- Notation (E_k,max, W, f0, λ0, hc ≈ 1240 eV nm) matches the brief's lesson. All three solutions are symbolic before the numbers, and their unit conversions and checks are sound.
- I recomputed every answer in one independent Python script.
- The hash was 6252f2afbde508b5 at the start and at the end.
