VERDICT: PASS
CONTENT-HASH: f775c61f5a128688

## Blocking
(none)

## Polish
- inquiry.json koe-1 and koe-2 "units": "v": "10⁶ m/s" — the Alkutila box (capture #41, #43) prints "vauhti v = 110⁶ m/s", which reads as 110 to the power 6 — fix: print the value as "1,0 · 10⁶ m/s" (or units "m/s" with value "1,0 · 10⁶").
- inquiry.json hook / koe-1 / johtopaatos — the opening question (sorting by mass) is only answered by the theory text and the optional "pohdi"; no experiment varies the particle alone at the same v and B (koe-1 locks "hiukkanen"; koe-2 holds v at E : B so a student never sees a wrong speed deflect) — fix: add an optional step (proton vs deuteron at the same v and B; one speed off E : B in koe-2) and one sentence on mass dependence in the johtopaatos model answer.
- inquiry.json tarkistus-2 + lesson.md "force-dir" — the check repeats the theory figure's geometry (B into the page, v to the right, negative charge goes down), so the answer can be read off the figure — fix: change the geometry (B out of the page, v to the left, curve upward).
- lesson.md r-graph / ennuste-2 — the graph shows r (10,4 cm at 2,0 · 10⁶ m/s) while the simulation and feedback show d = 2r (10,4 cm at 1,0 · 10⁶ m/s); the same number means two things, and ennuste-2 asks about r but the feedback quotes d — fix: say "d = 2r" in the prompt of ennuste-2 and in the graph caption.
- tarkistus-4 criterion 4 and sim control "Nopeus" — "Erotan magneettien tehtävän, radan taivuttamisen, sähkökenttien tehtävästä, kiihdyttämisestä." is hard to parse; "Nopeus" (animation pace) stands next to "Vauhti v" — fix: "Erotan magneettien tehtävän (radan taivutus) sähkökenttien tehtävästä (kiihdytys)."; rename the control "Animaation nopeus".

## Checked
- Path: prior knowledge (qE, qU, uniform circular motion) to F = qvB, circle, r = mv : (qB), selector, spectrometer, accelerator; one lesson's workload
- Predictions 1–3 refutable; wrong-option feedback repairs the misconception and quotes model values; reveal after the experiments
- Simulation at 390 and 1280 px: chamber to scale, d fits for the course's values, readout legible
- Worked example: seven stages, units stage, sanity check; numbers verified (m = 3,32 · 10⁻²⁶ kg, 20,0 u)
- Etsi virhe, siirto (0,225 T) and tarkistus-3 (6,2 cm) recomputed; mistake values match real slips
- Figures legible at 390 px; descriptions give the data without the answer; "track-sign" needed to answer
- Finnish: terms agree with the glossary; cases after number+unit correct
- Exit ticket and explain criteria observable; model answers mark values as model values
