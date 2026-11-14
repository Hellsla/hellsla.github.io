VERDICT: PASS
CONTENT-HASH: f379aaf2fc31bb49
SCOPE: delta added-exercise from 32e78172ab301d83 base 81db4a6fd727

## Blocking

## Polish
- solutions.md:287 (L1-11): the substitution divides by the rounded value 3,15 · 10⁷ s and writes = 29,89 km/s, but that division gives 29,92. Either write the exact $T = 3{,}1536\cdot 10^{7}\,\text{s}$ or write ≈ 29,9 km/s. The answer is not affected.
- exercises.json:269 (L2-08): "tekee $20\,\tfrac{1}{\text{min}}$" names no quantity. Write "pyörii pyörimistaajuudella $20\,\tfrac{1}{\text{min}}$", as the brief does.

## Checked
- The hash was the same at the start and at the end. Only L1-10, L1-11 and L2-08 were judged.
- One script recomputed every added answer: L1-10 gives 2π·1,80/5,0 = 2,262 m/s; L1-11 gives 2π·1,50·10⁸ km / (365·86 400 s) = 29,89 km/s; L2-08 gives 2π·(20/60 1/s)·1,20 m = 2,513 m/s. All three equal answers.py and exercises.json.
- Figure data: the radii are 0,60 m and 1,80 m at 80 px/m with labelled dimension lines. Both tasks read them. Neither task gives away the other: L1-10 asks for v_B at T = 5,0 s, and L2-08 asks for a difference at another rate.
- MAFY task L1-11: the value 150·10⁶ km is the VERIFIED row fy5-3 of docs/mafy-arvot.tsv, and the hint names only the table (*Aurinkokunta*). With 149,6·10⁶ km the answer is 29,81, which is inside 4 %. The ±4 % in the solution matches `tolerance` 0.04.
- Sig figs: L1-10 and L2-08 have 2 (5,0 s and 20 1/min), and a student's 2,3 or 2,5 stays inside 2 %. L1-11 has 3.
- Notation ($v = 2\pi r/T = 2\pi r f$, f in 1/s) is the brief's. No angular quantities are used, as the scope requires.
