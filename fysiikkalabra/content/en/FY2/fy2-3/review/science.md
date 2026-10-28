VERDICT: PASS
CONTENT-HASH: a161c1cfd0a4c1e1

## Blocking
(none left)

## Fixed
- inquiry.json activities.5 choice 3 feedback — "the same power produces more energy all the time" (could read as 'ever more power') → "the same power keeps adding more energy as time goes on" (Finnish: tuottaa lisää energiaa koko ajan)
- inquiry.json activities.15 mistake 2 feedback — "the energy given in hours" → "the energy given in watt-hours" (1200 Wh)
- figures.json (graph description) — "the 1000 W line of the toaster half as gently" → "rises half as steeply"; "almost horizontally" → "is almost horizontal"; figures redrawn

## Polish
- assets/sims/fy2/fy2-3/sim.js `sig()` writes a decimal comma ({,}) in the readouts even in en — sim-code issue outside the translation, for the teacher.

## Checked
- Translation review against the reviewed Finnish (teacher's decision 2026-10-28): lesson.md (all prose, kWh derivation, table, worked example steps, misconception, summary), inquiry.json (all 18 activities incl. the new sim howto/model/calc, experiments koe-1 and koe-2 with intros, column names, measure labels, values, hints, mistakes, solutions, source_note), exit-ticket.json, meta.json, figures.json against content/fi/FY2/fy2-3. Physics (P = ΔE/Δt, E = P t, 1 kWh = 3.6 MJ, ratios 180×, 15 h, 30 min), units, decimal points, \cdot, chapter titles from courses.json all match.
