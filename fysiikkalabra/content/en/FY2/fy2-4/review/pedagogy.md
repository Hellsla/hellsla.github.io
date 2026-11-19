VERDICT: PASS
CONTENT-HASH: da144a33e701c6ed

## Blocking
(none)

## Polish
- inquiry.json `johtopaatos` criterion 3 ("efficiency of the incandescent lamp is about 5 %, so only a small part is useful") now matches the question's data and the model answer (5 % and the remaining 95 % losses), so the round-3 blocking item is closed. It is a little beyond the literal prompt (calculation and why time does not matter); naming "so the rest, 95 %, was losses" would make it fully observable. Taste only.
- lesson.md "Efficiency tells the share of the useful part": second paragraph is about 150 words with three ideas; split it and put the table's lead-in on its own line.
- lesson.md "Common misconception": "The energy leaving an incandescent lamp is equal to the energy entering it: 3 W of light and 57 W of heat" mixes energy and power; say "the power leaving equals the power entering".
- inquiry.json `koe-1` is optional while `ennuste-1` reveals after it; consider making it core, since it is the only place the engine's 25 % is met as data.
- Workload: with `pohdi`, `virhe`, `tarkistus-3` optional the core path stays about one hour; keep them optional.

## Checked
- Learning path: builds on fy2-3 (E = P t), answers the opening question (where the energy goes, how to measure a device), only the slot's goals, no FY3 content.
- Hook gives numbers but not the answer; retrieval item has misconception-based distractors with own feedback.
- Predictions: misconception-based options, feedback repairs rather than restates; ennuste-2 honestly says the sim only repeats the constant-efficiency assumption.
- Experiments lock device and P_o and vary t only; the conclusion states the values are model values.
- Worked example: seven stages, symbolic first, reasonableness check, not repeated in exercises.
- Sankey figures sit after their paragraphs; aria-labels carry data without the answer.
- Transfer task has three hints and real mistake values (forgot η, 60 s for 1 h); virhe item tests the inverted ratio.
- Tarkista: concept, heater (heat as benefit) and calculation items test concepts; exit ticket tests η, losses, power is not efficiency.
- Simulation text sits behind Käyttöohje, Mallin oletukset, Laskennan selitys; lead under 30 words.
- English terms consistent; hash identical at start and end.
