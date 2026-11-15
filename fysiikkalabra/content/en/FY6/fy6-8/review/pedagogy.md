VERDICT: FAIL
CONTENT-HASH: abbf87ba0442de5e

## Blocking
- lesson.md (whole lesson), inquiry.json — the slot's first LOPS goal, "accumulators and the charging circuit of an accumulator", is not taught or practised. Nothing on rechargeable cells, charging, a charger voltage above E, or the charging current I = (U_charger - E) : (R + R_s). The lithium photo only says "cell". Fix: add a short Key idea subsection with a figure of the charging circuit (the same E and R_s model, the current reversed, energy stored versus internal energy). Add a retrieval-level check, or confirm another chapter owns it and have the teacher change the slot.

## Polish
- inquiry.json kertaus (optional retrieval) — an unrelated two-resistor voltage-law item. House rule: the retrieval belongs to the phenomenon, so ask it through the headlights or a car battery, e.g. the voltage of a load in series with a source.
- inquiry.json koe-1 mistakes (1.0 and 1.2 Ω) — these match only the row R = 1.0 Ω (U : I = R, E : I = R + R_s). A student using R = 2 Ω or 4 Ω gets other values and the repair feedback never fires. Name the row in the hint or add values for the other rows.
- inquiry.json ennuste-2 — the correct option's wording ("because the internal resistances are in parallel") hands over the reasoning that the theory teaches later. State only the outcome and leave the reason to the justification box.
- lesson.md "Batteries in series and in parallel" — "each charge passes through only one battery" is stated without saying that the current is shared equally. Add a clause so the model answer in tarkistus-3 follows from the text.
- inquiry.json workload — 2 predictions, 2 required experiments, the conclusion, the error item, the transfer task, 2 checks and an exit ticket, plus a long exercise list. Close to one lesson; keep koe-3 and tarkistus-3 optional.

## Checked
- Hook (the headlights) is answered in "A car battery at starting" and by the transfer task; the answer is not shown before the commitment.
- The predictions can be refuted by the experiments: koe-1 is refuted by the slope, koe-2 by three connections at a locked R = 1.0 Ω. Each wrong option's feedback repairs its misconception.
- Variables are controlled: koe-1 varies only R, koe-2 only the connection.
- The simulation hides E and R_s, so the student finds them from the fitted line. The numbers are called model values; the assumptions are in the model box.
- Theory figures do not pre-empt koe-1: the theory comes after the investigation, and the ui-graph (0.30 Ω) differs from the experiment data.
- Worked example: seven stages, one step each, data consistent; the reasonableness check is meaningful.
- Find-the-error and transfer: the distractors are real mistakes; hints are progressive; the solutions are complete.
- check-graph task: reading the slope from the fitted line is a sound representation task; the distractors are the U : I and E : I errors.
- Exit ticket tests the core idea, the drop across R_s and the short-circuit current.
- Lab capture at 1280 px: the sim sits beside the experiment, with a readable graph and the controls; the text is behind the three boxes. Exercises and Finnish not judged.
