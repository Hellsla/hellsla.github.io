VERDICT: PASS
CONTENT-HASH: 3ceda54783b971b7

## Blocking
(none)

## Polish
- inquiry.json pred-1 — the correct answer ("doubles") needs the Kelvin scale, which the prerequisites and the Ennusta stage never introduce, so a student can only guess between "12 times" and "doubles"; the feedback teaches it only after commitment. Fix: add one line to the prompt ("0 °C is not the lowest possible temperature; think about what the zero of a scale means") or give the 300 K and 600 K values in the prompt so the reasoning is about the micro model.
- lesson.md (micro-model figure caption, "the length of an arrow shows the speed") — the 1280 px capture shows dots only and no arrows, though the source has them. If the arrows are hidden at some animation phase, the caption and aria-label promise something the student may not see. Fix: keep the arrows always visible, or let the caption say what the student actually sees.
- lesson.md (two photos after the Kelvin paragraph) — the thermometer photo and the liquid-nitrogen photo sit in the right column beside "Limits of the model" and "Kelvin scale", which neither explains. The thermal-equilibrium caption introduces an idea the text never uses, and the nitrogen photo pays off only in check-1. Fix: tie each to its paragraph with one sentence (nitrogen: "very cold, yet still far above 0 K"), or drop the thermometer caption's equilibrium claim.
- inquiry.json johtopaatos — criterion 4 ("I separated the assumptions of the model from the results of the simulation") is not asked by the prompt, though the model answer's last sentence covers it. Fix: add that question to the prompt or remove the criterion.
- inquiry.json exp-1 — the pTheory column is the formula being predicted, so it only confirms the program's arithmetic. The measured column carries the physics: tell the student to base the conclusion on the measured value and use the theory column only for comparison.

## Checked
- Learning path: Pohdinta (tyre), recap, prediction, simulation, theory, example, checks. It matches the slot goals (system and state variables, temperature, micro model, Kelvin scale, absolute zero) and answers the opening question only after the student commits.
- Predictions: three, with pred-2 optional. Each wrong option's feedback names a real misconception (Celsius ratio, speed alone, expanding particles, heat as a substance). pred-3 gives competing explanations that experiment 1 can refute.
- Experiments: V locked in exp-1 and T locked in exp-2, one variable each, measured pressure emerges from counted hits, min 2 readings. Workload is about one lesson with the optional items skipped.
- The worked example is staged in seven steps and has a figure with an axis note; extrapolation figures are consistent (k = 0.37 kPa/°C, −270 °C, check against 136.6 kPa).
- Arithmetic checked in siirto (121.67 kPa; the 404 and 83.8 mistakes are correct), virhe (128 kPa) and check-2 (−273 °C).
- check-1 and check-c2 have misconception-based distractors. check-2 is similar in structure to the example but uses model data, which is acceptable.
- The explain task has a model answer and observable criteria, and the exit ticket tests the core idea.
- 1280 px theory captures: one column with the figure beside its paragraph, no empty column, the Kelvin figure to scale and legible.
- English: no wording errors found. The phone captures were not opened; the layout tests cover them.
