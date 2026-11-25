VERDICT: PASS
CONTENT-HASH: 196d7db3114314b7

## Blocking

## Polish
- exercises/solutions.md (the single-photon double-slit task, line ~297) — the block uses $\tfrac{N}{t}$ as the photon rate and then $t = \tfrac{5000}{r}$ as the total time. The symbol $t$ means two things. Writing $\dot N$ or $t_\text{mittaus}$ would separate them. This clash was there before the change. (carried over; untouched by this change)

## Checked
- Delta: exercises.json, 4 task text(s): each changed line differs from the passed version only by the removed prefix "Esimerkkiaineisto: " (and the capital of the next letter), checked mechanically line by line.
- No number, unit, symbol, table value, answer, tolerance or solution changed; the previous quantitative checks stand.
- Data provenance: removing the badge follows the teacher's rule (no provenance badge on example or simulated data); no task now claims a real published source it lacks.
- `reviews.py hash fy8-4 --exercises` the same at start and end.
