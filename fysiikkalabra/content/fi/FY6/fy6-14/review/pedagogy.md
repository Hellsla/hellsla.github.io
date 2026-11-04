VERDICT: PASS
CONTENT-HASH: 2c1c2a557074f30d

## Blocking
(none)

## Polish
- inquiry.json koe-2 intro (~l.187) — "Missä lähteen jännite on estosuunnassa?" is awkward and half-gives the answer — "Kuinka suuri osa lähteen jännitteestä on LEDin yli estosuunnassa?" (or just "Mitä jännitteille tapahtuu?").
- inquiry.json tarkista-2 (~l.574) — the check uses the same panel as the lesson (6 V, 200 mA, knee at 5 V, 0,9 W), so it can be answered by recall, not by reading the graph — change Ik and Ut (e.g. 3,0 A, 21 V) or ask for the power at the knee.
- lesson.md, figure "teho" — label "maksimiteho" differs from the term "maksimitehopiste" — use the term.
- inquiry.json ennuste-2 prompt — the sentence "Pienellä vastuksella virta on suuri, suurella jännite on suuri" already states both ends; the student only has to pick "the middle". Remove it so the prediction is a real one.
- Workload is near the upper limit (diode, LED, series resistor, solar cell, efficiency; 3 core experiments plus 2 optional): keep koe-4 and koe-5 optional.

## Checked
- Path: prerequisite (Ohm, Kirchhoff, P = UI) is retrieved; the opening question (reverse LED, series resistor, panel power) is answered by koe-2, koe-1 and koe-3 and revisited in "pohdi".
- Ennuste-1 and ennuste-2 are refutable by koe-1 and koe-3 (min 3 and 5 rows); every wrong option's feedback repairs its misconception with model values.
- The LED-circuit and solar-cell experiments hold one variable each; model values are labelled as model values; the sim emerges from the operating point (not only a formula).
- Sim at 390 px: circuit diagram, graph with operating point, controls and readout are readable; colour legend in text.
- Theory figures (suunnat, ominaiskayra, kenno, etuvastus, teho) are legible at 390 px, descriptions carry the same data without the answer.
- Worked example has one step per stage and a sanity check; the "Etsi virhe" item targets R = U : I.
- Transfer task (panel to battery) has three progressive hints and real common-mistake feedback.
- Finnish and glossary terms (päästösuunta, estosuunta, kynnysjännite, etuvastus) consistent; number+unit cases correct.
- Exit ticket tests the reverse direction and the Isc x Ut mistake; both are core ideas.
