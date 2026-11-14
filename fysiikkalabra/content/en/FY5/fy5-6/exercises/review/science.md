VERDICT: PASS
CONTENT-HASH: 16c8b891104d7a49
SCOPE: delta added-exercise from 0b8adf1d8e82e8e4 base 81db4a6fd727

## Blocking

## Polish

## Checked
- The hash was the same at the start and the end. Round 6: I checked the round-5 fixes. The diff changes only L1-11's unit and hint and L1-10's reasonableness check.
- exercises.json:136 (L1-11): the unit is now "m/s²", which matches the task. g = γM/r² = 1.448 m/s² → 1.45, as in answers.py and the Finnish version.
- The L1-11 hint is now singular, because only the Moon's mass is looked up (VERIFIED value 7.346·10²² kg). The 4 % tolerance fits.
- L1-10: "less than a thousandth" is right, because 5.93·10⁻³/9.81 = 6.0·10⁻⁴. The answer 5.93 mm/s² is unchanged.
- The answer, unit and tolerance of every exercise equal the Finnish set's. The numbers in the solutions of L1-10, L1-11 and L2-08 are the same as in the Finnish version.
