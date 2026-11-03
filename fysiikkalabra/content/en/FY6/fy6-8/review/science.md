VERDICT: PASS
CONTENT-HASH: 6e1a3a1c07f6e7a5

## Blocking
(none)

## Polish
- [Minor] Term: the Finnish "lähdejännite" is rendered "source voltage" throughout (the course convention, see fy6-5), while the title says "Electromotive force". Fixed: the first definition now reads "source voltage $E$ (also called its electromotive force, or emf)", so title and body meet.
- [Minor] Figure `potential`: the axis word "kohta" is "place" (a short-word fit for a 70-unit label). Acceptable: it names the position along the loop, and "position" would overflow the viewBox. "point" would be an equal alternative.

## Checked
- Every `$...$` of lesson.md, inquiry.json, exit-ticket.json equals the Finnish one (script, decimal point vs comma normalised); the figure subscripts R_\text{s}, I_\text{k} stay as drawn.
- All numbers in prose, options, feedback, hints, model answers, criteria and the worked example equal the Finnish (script over every string): 1.58/1.45 V, 4.0 Ω, 0.36 Ω, 4.4 A, 1.333/1.455/2.286 V, 0.20 Ω, 12.6 V, 10.4 V, 3.20 V/0.40 Ω, 1.60 V/0.10 Ω.
- Physics statements identical in meaning: model, U = E - R_s I, I = E/(R + R_s), I_k = E/R_s, graph slope -R_s, series sums, parallel R_s1/n, extrapolation caveat, car starting, short-circuit hazards; terms terminal voltage, internal resistance, short circuit, load resistor, source voltage correct.
- Prediction keys, correct options and numeric answers unchanged (keys and `answer` fields compared with the Finnish).
- Fixed a leak of Finnish into the experiment cards ("paristo: new battery", "kytkin: kiinni"): `names` paristo/kytkin and `values.kytkin` now battery / switch / open / closed.
- Figure descriptions in figures.json read correctly in English; no Finnish left in lesson.md (only glossary keys in meta.json, intentional).
