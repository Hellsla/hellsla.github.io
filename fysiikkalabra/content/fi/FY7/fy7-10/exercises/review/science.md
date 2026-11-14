VERDICT: PASS
CONTENT-HASH: 3f1a684d0e3d8b8e
SCOPE: delta added-exercise from 0103d8f31883bc59 base 8f23aa7ae3bd

## Blocking

## Polish
- lessons/FY7/fy7-10/answers.py:51–52 — the comment still says "slope k = 0,596 / 0,40 = 1,49 = n" and computes an unused `k`, while line 53 (and the solution) use n = 1,50 — drop the dead line or reword the comment to the solution's readings 0,30 / 0,90 → 1,50.

## Checked
- Delta round 3: L1-09 and L2-09 (added exercises); hash identical at start and end.
- Round-2 polish fixed: L2-09 answers.py now uses n = 1,50: asin(sin 35,0° / 1,50) = asin(0,3824) = 22,481° = stored 22.48145, matching the solution's 22,5°.
- fit figure: least-squares line of the plotted data has slope 1,4895, intercept −0,004, so it passes 0,294 at 0,20 and 0,890 at 0,60; readings 0,30 / 0,90 are right to the grid's precision, and the 3 % tolerance covers k = 1,49 too (22,64°).
- L2-09 physics: sin α₁ = (n₂/n₁) sin α₂, slope = n₂ with n₁ = 1,00; read from the line, not raw points (guardrail).
- L1-09: MAFY water 1,333; sin α₂ = 0,7880 / 1,333 = 0,5912, α₂ = 36,24° = answers.py; refraction toward the normal; three figures from 52,0°.
