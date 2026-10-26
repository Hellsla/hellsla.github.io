VERDICT: FAIL
CONTENT-HASH: c11560dc57c21b89

## Blocking
- inquiry.json pred-1, pred-3 (feedback), exp-1 — the simulation computes p from pV/T = vakio (sim.js lines 3-9: "pressure comes from these formulas, not from counting hits"), so exp-1 cannot refute the prediction; yet the feedback says "Koe tukee tätä", "Mittaukset tukevat", "Mittauksissa paine...", and pred-3 asks which model fits "mittauksia". The student verifies Boyle's law with a program that has it built in; the brief says call simulation numbers model values. Fix: word pred-1/2/3 feedback and exp intros as "simulaation malli antaa" and add one honest step that is evidence (make the ruisku interpret data the evidence for Boyle's law, with pred-3 revealed after it), or make p emerge from counted hits (hits per second, as the brief prefers).

## Polish
- inquiry.json exp-1 intro and table — the experiment table shows p (Pa) and pV (J) while the sim readout and its table show kPa and kPa·ml (5000 kPa·ml); two units for one quantity on one screen. Use kPa/kPa·ml in both, or convert in the sim.
- inquiry.json exp-2 question and virhe — the correct option is the longest and most detailed one in both; shorten it or lengthen the distractors.
- inquiry.json workload — three predictions, two experiments, ruisku, virhe, siirto, 12 exercises and three checks is more than an hour; pred-2/exp-2 (isobaric) could move to fy3-3/fy3-8 revision or the exercises.
- lesson.md fig 3 — the 273 K tick sits under the middle of the data and the dashed line has no 0 K / -273 °C label at the axis; the caption says "mittakaavassa" but the axis has no scale beyond 0 and 273.
- inquiry.json ruisku — data are labelled as example values, good, but "Laske ... pV (tai 1/V)" is left as a loose instruction; give the student a place to enter or a graph to act on.

## Checked
- Opening question answered in Ydinajatus and reflect; prerequisites fy3-4 (kertaus) and fy3-8 (exp-2 question) used.
- Hook, kertaus and predictions: wrong options carry misconception-repairing feedback; speakers Aino/Bea/Cem, correct one not always the same.
- Example is staged one step per stage; exercises levels 1-3 differ from the example, answers and solutions recomputed and correct.
- Exit ticket tests the core idea (Boyle, 1/V graph, kelvin).
- Finnish read through: no errors found; case endings after number+unit correct.
- Captures: figures 1-3 legible at 390; sim, buttons and readout fit at 390 and 1280; exp-2 locked mode shown.
- Prompt for ruisku: row 30 ml outlier arithmetic verified (pV 5430 vs 5040).
