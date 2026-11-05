VERDICT: PASS
CONTENT-HASH: 19398d9c8f78c89c
Mode: full (translation review against the reviewed Finnish set)
Round 2
## Blocking
(none)

## Fixed
- exercises.json L1-02: "in one boiling" -> "each time it boils water" (natural English).
- solutions.md L2-02 reasonableness: "an ordinary boiling of a kettle" -> "an ordinary kettle boil".

## Polish
(none)

## Checked
- Task wording keeps the Finnish structure: given data, sub-questions a/b/c, and the sentence naming which part the answer field takes, in every multi-part task.
- Choice feedback names the same error type as fi (power, current, price distractors); solutions keep all seven steps and the reasonableness check.
- English is natural; no Finnish left (grep for ä/ö/snt/vrk clean); units translated (c/kWh, h/d, example data).
- Numbers and answers equal to fi, see science.md.
- Delta (answer-step first line now starts with the boxed value): checked each added value against the solution result and exercises.json answer/tolerance, same unit, decimal point; the line reads well and agrees. Values: L2-05 730 kWh (733.65 tol 2 %). L2-06 335 W. L2-07 300 kWh (299.3 tol 5 %). L3-04 0.93 €. L3-05 13 a (12.96 tol 2 %).
