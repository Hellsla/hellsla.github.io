VERDICT: PASS
CONTENT-HASH: c60d30a7c0a9a6ea

## Blocking

## Polish
- inquiry.json `koe-1`/`ennuste-2` — the experiment only computes t = d/c, and prediction 2 hands over "10^7 km in 33 s", so the student multiplies and the sim confirms the arithmetic. Fix: give only the AU time (8.3 min) and ask for 10^9 km, or have the student first estimate the travel time of a distance given in AU.
- inquiry.json `ennuste-1` — the prompt says "more than a hundred times farther" and 8 min is given, so the answer is one multiplication away. Fix: drop the "hundred times" and let the student find the ratio from the Voyager distance in AU.
- inquiry.json `hook`/`koe-1` — AU is used (the hook, d (AU) in the tables, prediction feedback) before the theory defines it. Fix: add "1 AU is about the Earth–Sun distance" to the hook or the sim lead.
- inquiry.json `simulaatio` text — the lead is about 38 words (limit 30) and sits under the closed boxes, and the canvas axis says "Gm" while the readout says km. Fix: shorten the lead, put it above the controls, and mention Gm = 10^6 km in the howto.
- lesson.md "A unit for every scale" — the atom (10^-10 m) is paired with the nm (10^-9 m), so the value is 0.1 nm, which contradicts "a unit is chosen so the value is easy to read". Fix: say "0.1 nm" in the row or add a note. The workload (two predictions, two experiments, interpret, theory, example, 20+ exercises) is at the top of an hour: make the second prediction and experiment optional.

## Checked
- Learning path: the hook question (why the same distance has different units) is answered in the conclusion explain and the reflection. The slot goals (quantity, SI, prefixes, significant figures, conversions) are all in the theory. The prerequisites are only powers of ten.
- Prediction options are plausible, each wrong option's feedback repairs its own error, and each experiment can refute its prediction.
- Sim at 390 px (capture #2 and koe-1): controls, readout and model values are clear and the Käyttöohje/Mallin oletukset/Laskennan selitys boxes are closed. The slider needs a precise setting to n = 8.00 on a phone, but the buttons and the title make it workable.
- Hero figure (#3): the Sun, planets, Voyager and three rulers of different spacing are recognisable and uncluttered. It shows the Miksi question without giving the answer.
- Worked example (Neptune): seven stages, one step each, symbolic first, reasonableness check present. It does not repeat the exercises or the Mercury check.
- Find the error (km² → m²) and the sig-figs choice have misconception-based distractors, and the feedback explains the error rather than restating the answer.
- Transfer task (AU/a): three progressive hints, real mistake values, a full solution. Checks 1–3 and the exit ticket test the core ideas (unit vs quantity, conversion).
- The explain criteria are observable and match the prompts. The model values are labelled model values with their source.
- The exercise set was not judged here. The hash was the same at the start and the end.
