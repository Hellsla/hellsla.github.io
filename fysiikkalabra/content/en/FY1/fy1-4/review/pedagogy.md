VERDICT: PASS
CONTENT-HASH: 257f7f3f2622b45a

## Blocking
(none)

## Polish
- lesson.md "Linear model" (Key idea) — uses "slope" and "constant term" before the Formula section defines them, and the opening hook never says the lesson will show where a line's equation comes from — add one clause ("the line y = kx + b, explained in the next section") or move the sentence on slope/constant term after the formula.
- lesson.md Worked example, stages 1-2 — titled "Fitting a line" but the line arrives already drawn; the student never sees how it was placed (points on both sides, roughly equal) — add one sentence in Principle saying how the line was chosen by eye, using the same criteria as the sim.
- inquiry.json johtopaatos — `after` includes koe-3, but the model answer and criteria never mention data set 3 (a pattern of deviations means the line does not fit), which is a stated learning goal — add a criterion and one sentence to the model answer.
- inquiry.json koe-1, ennuste-1, simulaatio — the RMS quantity is called "mean deviation"; the name suggests a plain average and clashes with "deviations above and below cancel" in the text — call it "typical deviation d" or say once that squaring prevents cancelling.
- inquiry.json koe-3 question, last option ("all the deviations are about the same length") — a weak distractor that no student would pick; replace with a real misconception, e.g. "it fits, because the best-fit line gives a smaller d than any other line".

## Checked
- Opening question is answered by the conclusion and the reflection; slot goals (graph, linear model, fit, slope) covered, nothing beyond FY1 scope.
- Predictions 1 and 2 can be refuted by experiments 1 and 2; each wrong option's feedback repairs its misconception and cites numbers; I recomputed d for k = 0.3, 0.5, 0.6 and for b = 0 vs about 61 g: all match.
- Experiment 3 (coffee) shows the curved case; the pattern of deviations (up at the ends, down in the middle) is correct for a convex cooling curve.
- Worked example arithmetic (k 8.0, b 20, t 2.5 min) and seven stages, one step each, are correct; reasonableness uses the table.
- Cyclist graph reading checked against SVG coordinates: P1 (1.0 h; 20 km), P2 (3.0 h; 50 km), b = 5 km, 35 km at 2 h; plant and hiker answers (20 days, 7.0 h) and their wrong-value feedback (25, 16, 8.3, 5.5) are correct.
- Find-the-error item is diagnostic and its correct option names the fix; exit ticket tests the core idea (equation from two points; meaning of b and proportionality).
- Checks: concept, representation, calculation, explain with criteria; optional items keep the core path to one lesson of work.
- Captures (390 px): figures sit beside their paragraphs, example stages readable, sim controls and readout understandable, nothing clipped in contact-1.
- Options carry no letter or position references; no speaker is right most of the time.
- Exercises not judged (reviewed apart); glossary still lacks "linear model" and "fitting a straight line" (developer task).
