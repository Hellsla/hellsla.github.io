VERDICT: PASS
CONTENT-HASH: 7fd2046853f3baf4

## Blocking

## Polish
- inquiry.json:339 (data, solution, Vastaus) — "Mittauspisteet poikkeavat suorasta noin $0{,}1\,\text{m/s}$" overstates the scatter: the five points lie within 0,04 m/s of the line v = 9,81·t (least-squares slope through the origin 9,78 m/s², standard error about 0,04 m/s²). The estimate of 0,2 m/s² is fair, but it comes from reading the graph (±0,1 m/s at 0,50 s), not from the scatter — base the estimate on the reading resolution, or say "alle 0,1 m/s".
- inquiry.json:116 (simulaatio.model) — the air model could name its form in a few words (the drag grows with the square of the speed, so a ball approaches its terminal speed). As written ("sitä enemmän, mitä nopeammin") it is correct at this level; this is optional. (carried over; untouched by this change)

## Checked
- Delta: inquiry.json, the title of the optional data step: each changed line differs from the passed version only by the removed prefix "Esimerkkiaineisto: " (and the capital of the next letter), checked mechanically line by line.
- No number, unit, symbol, table value, answer, tolerance or solution changed; the previous quantitative checks stand.
- Data provenance: removing the badge follows the teacher's rule (no provenance badge on example or simulated data); no task now claims a real published source it lacks. The step text still says "simuloitu esimerkkiaineisto, ei oikea koe" and `source` stays `simulated`.
- `reviews.py hash fy1-6` the same at start and end.
