VERDICT: PASS
CONTENT-HASH: 4a6a45e6ddeaa9ce

## Blocking

## Polish
- solutions.md:201 — L3-05 b) still writes $5{,}2 \cdot 10^{4}\,\text{s} : 3600\,\text{s/h} = 14{,}5\,\text{h}$ (the rounded value gives $14{,}4\,\text{h}$; unrounded $14{,}46\,\text{h}$). This was in the earlier report and is not part of this diff. The final $14\,\text{h}$ is right. (carried over; untouched by this change)

## Checked
- Delta: exercises.json, 1 task text(s): each changed line differs from the passed version only by the removed prefix "Esimerkkiaineisto: " (and the capital of the next letter), checked mechanically line by line.
- No number, unit, symbol, table value, answer, tolerance or solution changed; the previous quantitative checks stand.
- Data provenance: removing the badge follows the teacher's rule (no provenance badge on example or simulated data); no task now claims a real published source it lacks.
- `reviews.py hash fy6-1 --exercises` the same at start and end.
