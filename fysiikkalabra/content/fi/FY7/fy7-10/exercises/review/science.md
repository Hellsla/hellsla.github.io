VERDICT: PASS
CONTENT-HASH: 91929cab691c65d8
SCOPE: delta added-exercise from 0103d8f31883bc59 base 8f23aa7ae3bd

## Blocking

## Polish
- exercises.json (L2-09 answer 22.6407) and answers.py:329–331 — the stored answer uses k = 1,49 (line read to three decimals) while the solution now reads 0,30 / 0,90 and gets k = 1,50, α₂ = 22,5°; both are inside the 3 % tolerance, but the shown answer (22,6°) and the solution (22,5°) differ — compute answers.py from the solution's readings (0,30 and 0,90), so the answer is 22.48.

## Checked
- Delta round 2: L1-09 and L2-09 (added exercises); hash identical at start and end.
- Round-1 blocking fixed: L2-09 Sijoitus now 0,60 : 0,40 = 1,50, n₂ = 1,50, α₂ = asin(sin 35,0° / 1,50) = 22,48° → 22,5°, arithmetic right.
- fit figure: least-squares line of the drawn data has slope 1,4895, intercept −0,004, so it passes 0,294 (0,20) and 0,890 (0,60); readings 0,30 and 0,90 are right to the grid's precision.
- Physics of L2-09: sin α₁ = (n₂/n₁) sin α₂, slope = n₂ with n₁ = 1,00; reading from the line, not raw points, follows the guardrail.
- L1-09: MAFY water 1,333; α₂ = 36,24° = answers.py; toward-normal check right.
