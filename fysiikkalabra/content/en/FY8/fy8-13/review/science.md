VERDICT: PASS
CONTENT-HASH: 94744182f94ef619

## Blocking

## Polish
- inquiry.json:364 (tarkistus-2 solution, Reasonableness) — "The radiation in the graph therefore has a slightly higher energy than that of caesium-137" infers photon energy from a 5 cm vs 4 cm half-value thickness, but concrete density and composition vary — soften to "may have a somewhat higher energy, or the concrete is less dense" or drop the sentence. Carried over.
- lesson.md:333 bar label "other natural" vs table row lesson.md:308 "other natural radiation" — the short label is unambiguous because the table directly above, the caption (lesson.md:313) and the aria-label name it in full; "other natural sources" would read as a complete noun phrase if it still fits at 360 px. Taste, not an error.

## Checked
- Only change since the passed version (hash 80734f621c253d2d → 94744182f94ef619): the label key "muu luonnon säteily" in figures.json is now "other natural", redrawn at lesson.md:333 (foreignObject x 92, width 158, right-aligned to the bar origin as before). No bar, number or axis changed.
- Figure capture fy8-13-fig-4-390 (post-change): radon 4.0, other natural 1.1, health care 0.8 mSv/year, bars to scale, axis H_E (mSv/year); the label fits the frame at 390 px.
- Values still agree with the table (4, 1.1, 0.8 mSv, total 5.9), caption (STUK-A263, 0.76 → 0.8) and the aria-label, which keeps "other natural radiation, that is soil, buildings, space and the body's own substances".
- Rest of the lesson unchanged and as approved in the previous report (all recomputed numbers, ICRP 103 weights, sim model, choice items, exit ticket).
- Hash unchanged between start and end.
