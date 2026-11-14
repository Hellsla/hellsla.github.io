VERDICT: PASS
CONTENT-HASH: 5c531bbbd7f99c5c
SCOPE: delta added-exercise from 44acd46636ba9d0f base 81db4a6fd727

## Blocking
- none

## Polish
- content/fi/FY1/fy1-8/exercises/solutions.md:192 — "(tarkemmin $1{,}37\,\text{km}$)" is slightly below the computed minimum of 1,3736 km. A minimum should not be rounded down. Write "tarkemmin $1{,}374\,\text{km}$", or drop it, since the answer is rounded up on purpose.

## Checked
- fy1-8-L1-10 only (delta, added exercise; round 2). The hash was the same at the start and the end.
- I recomputed it myself: t_min = Δt/ε_max = 0,2 s / 0,05 = 4,0 s, and s = vt = 343,4 m/s · 4,0 s = 1373,6 m = 1,3736 km. This matches the answers.py value and the key.
- Round 1 Blocking fixed: the wrong "kaksi merkitsevää numeroa kuten 0,2 s" is gone. The answer 1,4 km is now explained as a design estimate rounded up so that the 5 % limit is met, as in the lesson's worked example.
- Round 1 language Polish applied ("suhteellinen epävarmuus saa olla").
- MAFY speed of sound in air at 20 °C (343,4 m/s) and the hint's table are right. The model is solved symbolically first, and the check back (0,2/4,0 = 5 %) is a real one.
- The shown 1,4 km is 1,9 % from the key, inside the tolerance of 0,04.
