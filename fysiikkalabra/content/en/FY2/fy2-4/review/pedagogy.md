VERDICT: FAIL
CONTENT-HASH: 85be4e6f81859eff

## Blocking
- inquiry.json activity `johtopaatos`, criteria[2] — "I said that the losses of a petrol engine are a large part of the power taken and that they are heat" does not match the question (experiment 2, an incandescent lamp, energy vs power, time cancelling), and the model answer never mentions the petrol engine. koe-1 and ennuste-1 are optional, so many students will not have met the engine. The student cannot meet the criterion from what they wrote or from the model answer. Fix: replace it with a criterion about the question, e.g. "I said that the remaining 95 % of the lamp's energy was losses, mostly heat", which the model answer already states.

## Polish
- lesson.md "Efficiency tells the share of the useful part" — the second paragraph is about 150 words and holds three ideas (the 100 % limit, why real devices are below it, motor/heater/lamp comparison); split it, and put the table's lead-in sentence on its own line (reading-column rule, about 120 words at most).
- lesson.md "Common misconception" — "The energy leaving an incandescent lamp is equal to the energy entering it: 3 W of light and 57 W of heat" mixes energy and power. Say "the power leaving the lamp equals the power entering it".
- inquiry.json `ennuste-2` / `koe-2` — the sim only computes ratios at a constant efficiency, so the experiment confirms the arithmetic and cannot refute the "efficiency decreases" option; the feedback says so honestly. Fine as designed, but the explanation `johtopaatos` should say once that the evidence is the calculation, so students do not take it for a measurement.
- inquiry.json `koe-1` is optional while `ennuste-1` reveals after it; if both are skipped, the only prediction left is ennuste-2, whose answer is derivable at once. Consider making koe-1 core, because it is the only place where the engine's 25 % is met as data.
- inquiry.json `tarkistus-3` and `lahtolippu` — the exit ticket (3 items) after a 4th optional explain adds up to about 90 minutes of work. Keep the reflect, virhe and tarkistus-3 optional so the core path stays one hour.

## Checked
- Learning path: it builds on fy2-3 (E = P t); the opening question (where the energy goes, how to measure how good a device is) is answered by the Key idea, the Sankey figure and the formula; the slot's goals only, with no FY3 content (no chain of efficiencies, no Q = cmΔT).
- The hook gives numbers but not the answer; the retrieval item `kertaus` has misconception-based distractors, each with its own feedback.
- Prediction options are misconception-based (an engine like a kettle, a lamp or an intermediate value); feedback repairs the misconception and does not just state the answer.
- Experiments lock the device and P_o and vary only t; the controlled variable is clear.
- The worked example has seven stages, one step each, symbolic first, with a reasonableness check; it is not repeated in the exercises.
- The Sankey figures sit after their paragraphs, aria-label descriptions carry the data without the answer, and the lamp/pair figures are needed for the comparison.
- The 20 % solar-panel transfer task has three hints and mistakes of real kinds (forgetting η, 60 s for 1 h).
- Tarkista checks (concept, representation of heater and calculation) test concepts; the heater item tests "heat can be useful".
- The simulation text is behind the named boxes; the visible lead is under 30 words; the model values are marked as typical values, not measurements.
- English wording: terms consistent; the exit ticket tests the core idea (η, losses, power is not efficiency).
