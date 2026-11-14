VERDICT: FAIL
CONTENT-HASH: bbb52739624f488e

## Blocking
- solutions.md:239 (L2-09, Sijoitus) — A: "(0,89 − 0,29) : (0,60 − 0,20) = 0,60 : 0,40 = 1,49" is false; 0,60 : 0,40 = 1,50 — fix: read the line to three decimals as answers.py does (0,294 and 0,890: 0,596 : 0,40 = 1,49, α₂ = 22,6°), or keep the two-decimal readings and write k = 1,50, α₂ = 22,5°. Both are in the 3 % tolerance.

## Polish

## Checked
- Delta: L1-09 and L2-09 added; hash identical at start and end.
- L1-09: MAFY water 1,333; α₂ = asin(sin 52,0° : 1,333) = 36,24° = answers.py; the toward-normal check is right.
- fit figure: least-squares line of the drawn data has slope 1,4895 and intercept −0,004, so the line is at 0,294 (0,20) and 0,890 (0,60) as answers.py assumes; acrylic 1,49 right.
- Physics of L2-09: sin α₁ = (n₂/n₁) sin α₂ gives slope n₂ with n₁ = 1,00; reading from the line, not raw points, follows the guardrail.
