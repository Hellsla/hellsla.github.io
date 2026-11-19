VERDICT: FAIL
CONTENT-HASH: 3af2e018ab288946

## Blocking
- inquiry.json ennuste-1 / koe-1 — the key experiment cannot refute its prediction. The sim does not measure the engine's efficiency; it returns the 25 % constant that the lesson itself feeds in. The student's guess ("60 %", "90 %") is checked against a programmed input, not against evidence, and the task's own intro admits this. The 75 % answer is a division of two numbers the program derived from 25 %. The brief calls this "confirming the program's arithmetic". — Fix: make the prediction something the evidence can decide. For example, predict from the sankey picture how the useful arrow compares across devices at the same P_o, or ask which device needs a higher P_o for the same P_a, and use a sourced table (named source and year) for the real petrol engine value. Alternatively, make the core prediction the time-invariance of η, which is physics the student can derive, and promote ennuste-2 and koe-2 from optional.

## Polish
- inquiry.json ennuste-1 prompt — the "Hint: ... do the engine and exhaust pipe get hot?" before commitment steers toward the answer and makes the prediction easier to guess. Fix: drop the hint or move it to the feedback.
- inquiry.json koe-2 question — the prompt gives "the ratio P_a : P_o is 5 %" and then asks for the ratio of energies; the answer is in the prompt. Fix: ask the student to compute both ratios from the table and the sim readout.
- inquiry.json tarkistus-3 — criterion 4 (an example with numbers) is not asked for by the question. Fix: ask for a numerical example, or drop the criterion.
- Tutki capture at 1280 px shows two closed boxes with the same content ("Assumptions of the model and explanation" and "Assumptions of the model") and the experiment-1 sim opens on a lamp (the lock is applied only after Set up). Fix: remove the duplicate box and make clear Set up is needed.
- lesson.md "Efficiency tells..." paragraph is about 130 words with several ideas (conservation, causes of loss, heater, motor). Fix: split under a subheading.

## Checked
- Path and prerequisites: build on fy2-3 (E = Pt); the slot's goal (η by energy or power) is met and no FY3 content (no Q = cmΔT, no chain efficiencies).
- Opening: the lamp question is answered by the Sankey figure and the table, not disclosed before the prediction.
- Figures: hero, lamp and pair figures are legible at 390 px and to scale; colour is paired with labels.
- Worked example is staged in seven steps with a unit conversion and a reasonableness check.
- Misconception feedback (ratio inverted, "energy disappears", high power = high efficiency, heater) names the error and repairs it.
- Concept checks use misconception-based distractors; the heater check separates purpose from the loss idea.
- Exit ticket tests the core idea (η from E, P, power vs efficiency); its model answers are complete.
- Workload fits one lesson; the optional items are marked.
- Exercises were not judged (reviewed apart).
- The hash was the same at the end.
