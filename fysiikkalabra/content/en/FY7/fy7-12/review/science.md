VERDICT: PASS
CONTENT-HASH: c3d2878255784b71

## Blocking

## Polish
- lesson.md:159 — "the fibre delays the signal slightly more than the distance alone would suggest": the factor is 1.47 (5.74 ms against 3.91 ms in siirto), so "slightly" understates it — write "about one and a half times as long as in a vacuum".

## Checked
- Round-2 changes: in the graph, "water" now sits below-left of the dot at (183.5, 174), and "glass" sits above-right of the dot at (228.5, 190.5). Each label is beside its own point and clear of the curve (capture fig-11 confirms this). The points are to scale. The new legend ("Dashed lines are normals. Not to scale.") is still correct.
- sim.js is unchanged from the version that passed. It implements sin θ = n1 sin θ1, α = 90° − θ1, sin α_r = n2/n1, and the leak at β. "Angle of incidence on the end face θ" is correct, because the axis is the face's normal.
- One script recomputed every number in lesson-answers.py with my own formulas, and all of them agree: 41.7°, α_r 48.8/41.8/24.4/80.57/42.51/63.98/71.08°, sim α 90/83.26/80.59/79.93/70.25°, koe-1 limit 14.03 → 14, siirto 5.743 ms with mistakes 3.907/2.658/0.005743, virhe 40.6°, check-2 69.98° with mistakes 20.02° and 0.9396, exit 38.7°.
- The multiset of numbers in lesson.md, inquiry.json and exit-ticket.json (outside SVG markup) is identical to fi. The correct flags, initial states, locked parameters and numeric answers are the same as in fi.
- Predictions: exactly one correct option each, and the distractor feedback is right. koe-1 and koe-2 each isolate their varied parameter.
- Definitions, the n1 > n2 condition, angles measured from the normal, and fibre guidance by total internal reflection (not a mirror) are consistent across the theory, summary, checks and exit ticket.
