VERDICT: PASS
CONTENT-HASH: e1cbdbd39a48e885
SCOPE: delta added-exercise from 24851d9dbd27e2fd base 8f23aa7ae3bd

## Blocking
(none)

## Polish
- content/en/FY6/fy6-12/exercises/exercises.json (fy6-12-L2-09) — the task text does not say where the positive plate is; a sighted student infers it from where the line ends (5.0 cm, axis running to 5.5 cm), only the alt text states it — add "the positive plate is where the line ends" or give x = 5.0 cm (same note as on the Finnish set).

## Checked
- Delta: only the added exercise fy6-12-L2-09 judged; the rest unchanged per `reviews.py added_exercises`.
- Figure ex-vgraph (figures.py): straight line from (0; 0 V) to (5.0 cm; 250 V) on a 1 cm / 50 V grid; V(1.0 cm) = 50 V and V(5.0 cm) = 250 V lie on grid lines as the solution reads them; nothing marked gives the answer.
- Physics: an electron released from rest moves toward higher potential (to the + plate); only the electric force works, so energy conservation gives ½mv² = eU with U = 200 V; the principle states the sign reasoning correctly.
- Recomputed: v = √(2 · 1.602·10⁻¹⁹ C · 200 V : 9.109·10⁻³¹ kg) = 8.387·10⁶ m/s; answers.py 8.387e6; json 8.39e6; 8.4·10⁶ is 0.15 % off, inside 2 %.
- Non-relativistic model valid: v/c = 2.8 %, stated in the check; the 3.0 kV comparison (3.2·10⁷ m/s) recomputes correctly.
- Solution complete: graph reading, v = √(2eU/m) before numbers, unit check √(C·V/kg) = m/s, rounding reason, reasonableness.
- Matches the revised Finnish task (same data, answer, tolerance and figure).
