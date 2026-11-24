VERDICT: PASS
CONTENT-HASH: 173a60e96e09d058

## Blocking

## Polish
- solutions.md (L3-03) — the Kaava block writes $f_\text{valo} = c/\lambda$ but no row for $f_\text{q}$, which is given. That is correct, but one clause ("$f_\text{q}$ on annettu") would make it read as complete. (carried over; untouched by this change)

## Checked
- Delta: exercises.json, 4 task text(s): each changed line differs from the passed version only by the removed prefix "Esimerkkiaineisto: " (and the capital of the next letter), checked mechanically line by line.
- No number, unit, symbol, table value, answer, tolerance or solution changed; the previous quantitative checks stand.
- Data provenance: removing the badge follows the teacher's rule (no provenance badge on example or simulated data); no task now claims a real published source it lacks.
- `reviews.py hash fy8-7 --exercises` the same at start and end.
