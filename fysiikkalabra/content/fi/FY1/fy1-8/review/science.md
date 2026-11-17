VERDICT: PASS
CONTENT-HASH: 22df881b050e2722

## Blocking
- none

## Polish
- none

## Checked
- batch delta review: new data recomputed: sum $12{,}2\,\text{s}$, mean $2{,}44\,\text{s}$, half the range $(2{,}6 - 2{,}3) : 2 = 0{,}15\,\text{s}$. lesson-answers.py prints the same. The correct option still calls half the range a simple estimate of the uncertainty, not the uncertainty of the mean, which follows the guardrails. Rounding: 2 figures in the uncertainty because its first digit is 1, and the mean to the same decimal. Distractors (the largest reading, no uncertainty given) stay wrong, and their unchanged feedback still fits. Exactly one option is correct. Hash the same at the start and the end.
