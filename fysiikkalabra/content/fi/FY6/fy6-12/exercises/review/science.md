VERDICT: PASS
CONTENT-HASH: 9f84f4124a537fa5
SCOPE: delta added-exercise from 4703625fe3ccea47 base 8f23aa7ae3bd

## Blocking

## Polish
- exercises.json (fy6-12-L2-09) — the task text does not say where the positive plate is. A sighted student must infer it from where the drawn line ends (x = 5,0 cm, with the axis running on to 5,5 cm); only the alt text states it. Add "positiivinen levy on kohdassa, johon suora päättyy", or give x = 5,0 cm, so the reading is not ambiguous.

## Checked
- Hash 9f84f4124a537fa5 at start and end; only fy6-12-L2-09 was judged (delta added-exercise).
- The figure in figures.py is a straight line from (0; 0 V) to (5,0 cm; 250 V) on a 1 cm and 50 V grid. V(1,0 cm) = 50 V and V(5,0 cm) = 250 V both lie on grid lines, as the solution reads them.
- Physics: the electron is negative, so released from rest it moves towards higher potential, to the + plate. Only the electric force works, so ½mv² = eU with U = 200 V. The direction, the sign and energy conservation are consistent with the brief.
- Recomputed: v = √(2·1,602·10⁻¹⁹ C·200 V : 9,109·10⁻³¹ kg) = 8,387·10⁶ m/s, which equals answers.py and the json. The tolerance of 2 % fits the answer to 2 significant figures.
- The non-relativistic formula is valid: v/c ≈ 2,8 %, as the reasonableness check says. Gravity is negligible, which the brief states.
- The solution is complete: the graph reading is shown, v = √(2eU/m) is written before the numbers, the units come out (√(C·V/kg) = m/s), and the rounding reason is stated.
- It is not a repeat of the worked example (3,0 kV from rest) or of L1-05 (proton energy only). It adds a reading of U from the graph and a start at a point between the plates.
