VERDICT: FAIL
CONTENT-HASH: 966bf8e0880f415b
SCOPE: delta added-exercise from 9b2ee0bf44613b3e base 81db4a6fd727

## Blocking
- fy5-16/exercises/exercises.json (L1-09, L2-09) with figure fy5-16/scale — **A** (the figure cannot be read to the tolerance). The ladder labels only 20, 40, 60, 85, 100 and 120 dB. The lawnmower and rock-concert markers sit between labelled ticks with no minor ticks, and the alt text says "noin 90 dB" and "noin 105 dB". With 3 dB halving, a 1 dB misreading moves the answer about 26 %: 89/91 dB gives 3,17/2,0 h, and 104/106 dB gives 5,95/3,75 min. That is far outside the 2 % tolerance. Fix: draw a task variant of the scale in figures.py that writes the level at each marker ("90 dB", "105 dB"), or one with labelled ticks every 5 dB, and use it in both tasks.
- fy5-16/exercises/solutions.md (L1-09, Järkevyys) — **A**. The text says "Taso 90 dB on … (91 dB, 2 h) ja … (88 dB, 4 h) välissä lähempänä jälkimmäistä", but 90 dB is nearer 91 dB, and 2,5 h is accordingly nearer 2 h. Fix: "lähempänä edellistä (91 dB), ja 2,5 h on kahden ja neljän tunnin välissä lähempänä kahta tuntia".

## Polish
- fy5-16/exercises (L2-09 vs L2-07) — L2-09 (105 dB, minutes) does the same computation as L2-07 (109 dB, minutes) apart from the figure reading. It is acceptable, but it adds little beyond the reading.

## Checked
- The model is the lesson's equal-energy rule t_v = 8 h/2ⁿ with n = (L − 85 dB)/3 dB, and 85 dB is correctly called the upper action value.
- L1-09: 90 dB gives n = 5/3 and t_v = 2,52 h, so 2,5 h (recomputed).
- L2-09: 105 dB gives n = 20/3 and t_v = 480 min/101,6 = 4,72 min, so 4,7 min (recomputed). Its check (20 dB is about 100-fold, so 4,8 min) is right.
- The figure's marker positions (figures.py) are at exactly 90 and 105 dB. The alt text has the same values.
- answers.py agrees with exercises.json.
- The hash was the same at the start and at the end.
