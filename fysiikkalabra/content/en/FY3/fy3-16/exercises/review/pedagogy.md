VERDICT: PASS
CONTENT-HASH: 7dde9624df498934

## Blocking
(none)

## Polish
- fy3-16-L3-03 — the task now needs rounding up (answer 1.6, tolerance 6 % so 1.51 passes but 1.5 does not), yet the question says only "smallest mass"; add "rounded up to two figures" or a hint, otherwise a student who correctly gets 1.5 sees a wrong mark with no reason.

## Checked
- Delta: the cool-bag answer 1.511 kg is now given as 1.6 kg because the smallest sufficient mass is rounded up, and the solution says why 1.5 kg would not be enough; reasonableness consistent with it; answers.py computes the same (ceil to 0.1).
- The sauna-stone efficiency task's principle now says electricity becomes internal energy transferred as heat; no number changed.
