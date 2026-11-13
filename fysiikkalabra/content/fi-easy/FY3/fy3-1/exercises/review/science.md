VERDICT: PASS
CONTENT-HASH: e406b191af20f91d
SCOPE: delta added-exercise from c7c51e40b053e747 base 81db4a6fd727

## Blocking
(none)

## Polish
- none

## Checked
- The diff since the version I passed touches only fy3-1-L2-08's solution: the slope is now written as g = G/m = 5,0 m/s² (no N/kg, in line with the house rule), the accepted range is now 58,2–61,8 N, which is exactly 60 N ± 3 % and matches the tolerance 0,03, and "suuremman" is corrected to "suurempi".
- L2-08 recomputed from figure weight-points: (4 kg; 20 N) and (10 kg; 50 N) give g = 5,0 m/s², and G = 12 kg · 5,0 m/s² = 60 N. answers.py gives 60. The extrapolation past 10 kg is justified by G ∝ m on one celestial body.
- L1-10 unchanged: G = 85,0 kg · 3,72 m/s² = 316,2 N, so 316 N. The lesson's 3,71 m/s² is inside the 4 % tolerance.
- My script compared fi-easy with the Finnish set: all 23 answers, units, tolerances and figure ids are identical, and so are the numbers in every task text and solution section.
- The answers.py values agree with exercises.json within rounding of the shown answers.
- Hash the same at start and end.
