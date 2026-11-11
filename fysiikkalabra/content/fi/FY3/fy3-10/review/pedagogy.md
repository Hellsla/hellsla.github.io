VERDICT: PASS
CONTENT-HASH: 42bda478c0fafe59

## Blocking

(none)

## Polish

- (Round 2: exp-2 tolerance widened to 0.1, now 45–55; item resolved.)
- inquiry.json `pred-1` — "Päättele: kaksi palloa" sits in Tutki after the weighing, so the opening balloon question is never committed to before the evidence; Ennusta only covers N vs p. Fix: either move a version of this question into Ennusta, or rename the reflect prompt so it does not call it a prediction.
- inquiry.json Tutki — nine activities (weighing, comparison, pred-1, sim, two experiments, table, laske-r, explain) plus the later stages make more than an hour. `taulukko` and `laske-r` overlap with exp-1/2 and the Kaava derivation. Fix: mark `taulukko` optional, or merge it with `laske-r`.
- lesson.md Ydinajatus paragraph 1 (about 140 words) and the sim paragraph (about 130 words) go over the 120-word guide; "liike-energia" is FY4 scope, so write "hiukkasten keskimääräinen vauhti" or "liike". The balloon photo sits between the sim and the combined-gas-law paragraph, which it does not explain; move it next to the siirto task or the example.
- `siirto` solution — "tämä ero kantaa pallon" brings in buoyancy without a step; say "nosteen perusta, jota ei tässä lasketa" or drop the sentence.

## Checked

- Learning path: weighing, then m/M for four gases, then R, then pV = nRT. The slot goal "ratkaiseminen tilanyhtälöstä" is met by the example, `siirto` and `check-2`, with no extra scope beyond the points above.
- The weighing data is consistent (m/M 0,2064–0,2076 mol); noise is declared, and the feedback states the measurement-precision argument rather than just the answer.
- pred-n: four options, each wrong one with misconception feedback; exp-1 can refute it (N is varied, T and V locked); the reveal comes after two rows.
- exp-2 is a challenge with distinct mistake feedback (√2, N×4, N/4); the hint ladder is progressive.
- The simulation capture at 390 px is legible: text sits behind Käyttöohje, Mallin oletukset and Laskennan selitys, and there is a speed control.
- The worked example has seven stages with units converted first and a reasonableness check that returns to the opening question.
- `virhe` and `check-c2` test the Celsius/Kelvin and unit-mix misconceptions with misconception-based distractors; the exit ticket tests n = pV/RT.
- `johtopaatos` and `check-3` criteria are observable and match what is asked; the model values are separated from the example data.
- Finnish: terms agree with the glossary; no case errors found in the sample.
- Hash unchanged at the end of the review. Exercises not judged (reviewed separately).
