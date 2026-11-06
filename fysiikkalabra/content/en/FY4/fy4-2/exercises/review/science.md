VERDICT: PASS
CONTENT-HASH: d2e456cbde8ae349
Mode: full (translation review against the reviewed Finnish set; new task fy4-2-L2-08)
Round 1

## Blocking
(none)

## Fixed
- exercises.json fy4-2-L2-08: feedback of three distractors reworded from the literal 'Here it has been ...' to natural English (no change of content).

## Polish
(none)

## Checked
- Script comparison of exercises.json with content/fi: all ids, levels, kinds, answers, units, tolerances, correct flags, choice order and every number in all strings are identical (decimal point in en); new task fy4-2-L2-08 included.
- Correct option and distractor feedback of fy4-2-L2-08 carry the same physics and numbers as fi; solutions.md section has the same lines, formulas and results.
- No Finnish left in en (grep); no wrong-language text. check_i18n.py: nothing for this chapter; build.py succeeds.
