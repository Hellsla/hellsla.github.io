VERDICT: PASS
CONTENT-HASH: fc30f2daa21c1b57
SCOPE: delta added-exercise from 0be719f8b69971cc base 81db4a6fd727

## Blocking

## Polish
- solutions.md fy5-6-L1-11 Järkevyys — "Kuu on kevyempi, joten ... pidempää kiertoaikaa" gives only half the reason: the smaller radius shortens the period; the period is longer because the Moon's g at its surface is smaller (T ≈ 2π√(R/g)). Same wording as the passed Finnish; optional.

## Checked
- Delta round 2, fi-easy: reworked added tasks fy5-6-L1-10 (Earth's acceleration from the figure), L1-11 (MAFY Moon probe period, h = 100 km), L2-08.
- Compared by script with the passed Finnish set: answer, unit, tolerance, figure, lookup, level identical; every number in task text and solution the same in fi and fi-easy.
- Recomputed independently: L1-10 r = 149,6 milj. km, a = γM/r² = 5,934 mm/s² -> 5,93; L1-11 r = 1837 km, T = 2π√(r³/γM) = 7065 s = 117,8 min (real low lunar orbits ≈ 118 min); L2-08 √(5250/88) = 7,724 -> 7,7. answers.py agrees.
- L1-10 check v²/r with 29,8 km/s gives the same 5,9 · 10⁻³ m/s²; L1-11 tolerance 4 % covers table differences; L2-08 states the circle as hypothetical and says the circle model does not describe the comet.
- Figure fy5-6/radat: real perihelion/aphelion values, ellipses to scale; description gives the same values, not the answers.
- Rounding reasons (three figures from M or h, two from 88 milj. km) and symbolic-first form right.
- Hash same at start and end.
