VERDICT: PASS
CONTENT-HASH: 8cec3736a94d62df

## Blocking

## Polish
- lesson.md:181 — "viivästyttää signaalia vähän enemmän kuin pelkkä matka antaisi odottaa": the delay is 1,47 times the vacuum time (5,74 ms against 3,91 ms), so "vähän" understates it. Write "noin puolitoista kertaa niin kauan".
- inquiry.json:58, 322, 326 — "Kokonaisheijastus" → "kokonaisheijastuminen" (the glossary term), as in fi.

## Checked
- Round-2 change: in the graph SVG, "vesi" is now at (113,5; 185,5), below-left of its dot (183,5; 174), and "lasi" is at (240,5; 154), above-right of its dot (228,5; 190,5). Each label is beside its own point and clear of the curve. The coordinates are the same as fi. Note that the shot fig-11 (01:00) predates the fix and still shows the old placement.
- One script recomputed every number of lesson-answers.py with my own formulas, and they all agree: 41,7°, α_r 48,8/41,8/24,4/80,57/42,51/63,98°, sim α 90/83,26/80,59/79,93/70,25°, koe-1 limit 14,03 → 14, siirto 5,743 ms and its mistakes, virhe 40,6°, check-2 69,98°, exit 38,7°.
- The multiset of numbers in lesson.md, inquiry.json and exit-ticket.json is identical to fi. The correct flags, initial states, locked parameters and numeric answers are the same as in fi.
- The fi-easy sim strings (angle, readouts, legend) match the model. sim.js is unchanged from the version that passed.
- Predictions: exactly one correct option each, and every distractor's feedback is right. koe-1 and koe-2 each isolate their varied parameter.
- Definitions, the n1 > n2 condition, angles from the normal and the fibre mechanism are consistent in the theory, summary, checks and exit ticket.
