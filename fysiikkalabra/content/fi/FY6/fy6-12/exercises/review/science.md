VERDICT: PASS
CONTENT-HASH: fb8bc2ae3ac4c6db
SCOPE: delta added-exercise from 4703625fe3ccea47 base 8f23aa7ae3bd

## Blocking

## Polish
- content/fi/FY6/fy6-12/exercises/exercises.json (fy6-12-L2-09) — the task text does not say where the positive plate is; a sighted student infers it from where the line ends (5,0 cm, axis running to 5,5 cm), only the alt text states it. Add "positiivinen levy on kohdassa, johon suora päättyy" or give x = 5,0 cm.

## Checked
- Hash fb8bc2ae3ac4c6db at start and end; delta round 2: only fy6-12-L2-09 judged.
- Figure: straight line from (0; 0 V) to (5,0 cm; 250 V) on a 1 cm and 50 V grid; V(1,0 cm) = 50 V and V(5,0 cm) = 250 V lie on gridlines as the solution reads them.
- Physics: the negative electron released from rest moves towards higher potential, to the + plate; only the electric force works, so ½mv² = eU with U = 200 V.
- Recomputed: v = √(2 · 1,602·10⁻¹⁹ C · 200 V : 9,109·10⁻³¹ kg) = 8,387·10⁶ m/s; answers.py and json agree; tolerance 2 % fits two figures (8,4·10⁶ is 0,15 % off).
- Non-relativistic formula valid (v/c ≈ 2,8 %, stated in the check).
- Solution complete: graph reading, v = √(2eU/m) before numbers, unit check √(C·V/kg) = m/s, rounding reason.
