VERDICT: PASS
CONTENT-HASH: ab3a7a9c0b52be41
Mode: delta (new task fy2-8-L2-08 only)
Round: 2

## Blocking
- none

## Fixed
- exercises.json L2-08 option 2 feedback: "a more efficient equipment" -> "more efficient equipment" (grammar).

## Polish
- none

## Checked
- fy2-8-L2-08 (exercises.json and solutions.md) against the reviewed Finnish: same table (5 rows, E and m), uncertainty 10 kt, correct option (2020 to 2024, 100 kt = 10 x 10 kt), exactly one correct flag, same five choices in the same order, tolerance and kinds equal.
- Recomputed: 520 - 420 = 100 kt; 520 - 515 = 5 kt < 10 kt; intervals 510-530 and 410-430 kt do not overlap (2020/2021 intervals 510-530 and 505-525 do); slope -25 kt/a x 10 a from 420 gives 170 kt for 2034; 1000 GWh in both years sits in column E.
- Each distractor still has one error and feedback that names it (wrong uncertainty comparison, unsupported cause, extrapolation, wrong column); no feedback gives a false number.
- Solutions section keeps Find / Principle / Model answer as in fi; numbers equal.
- English decimal point not applicable (integers only); natural English: "uncertainty range", "over-interpreting", "extrapolating too far".
- check_i18n.py: nothing for fy2-8; build.py fy2-8 succeeds.
