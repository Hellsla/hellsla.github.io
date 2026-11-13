VERDICT: PASS
CONTENT-HASH: 2afc0aba92faf652
SCOPE: delta added-exercise from bfb2af3a6b840af5 base 81db4a6fd727

## Blocking
- none

## Polish
- none

## Checked
- This review covers fy1-2-L1-10 only (delta, added exercise, round 4). The hash was 2afc0aba92faf652 at the start and at the end.
- I recomputed the answer myself: t = s/c = 3,844·10⁸ m / 2,998·10⁸ m/s = 1,28219 s (1,28222 s with the exact c). Rounded to three figures this is 1,28 s. answers.py prints 1.28 and exercises.json has 1.28, so all three agree.
- Significant figures: the data have four figures, and the teacher chose to give the answer to three. The solution gives a physical reason for that: the table value is a centre-to-centre mean, and the signal's real path is not exactly that distance. The reason holds. The path from the Moon's surface to the Earth's surface is about 376 300 km, which gives 1,255 s, about 2 % less than the answer. So the fourth figure carries no meaning, and the intermediate value 1,282 s shown before rounding is fine.
- Tolerance 0,04 is relative, so the accepted range is 1,229…1,331 s. This range takes in the surface-to-surface value, the four-figure 1,282 s, 1,3 s and the MAFY table's own c. The solution's "noin ±4 %" matches it.
- MAFY table Aurinkokunta: the Moon's mean distance is 384 400 km. The hint and the solution name the same table. The km → m conversion is right, and t = s/c is stated symbolically before substitution, in the lesson's notation.
- Physics: the radio signal travels at c in vacuum. Using the mean centre-to-centre distance is a fair simplification (category C), and the solution now states it. The reasonableness check is a real order-of-magnitude check. The task stays within the FY1 scope.
