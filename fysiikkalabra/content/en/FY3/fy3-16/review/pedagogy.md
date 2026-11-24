VERDICT: PASS
CONTENT-HASH: cd81e3a1006e1a34

## Blocking
(none)

## Polish
1. lesson.md, Worked example, last stage "Reasonableness" — after the check, the same stage carries a second calculation (heat capacity C, then dT/dt = P/C ≈ 19 K/h; capture #9). It is a new step, not a check, and breaks "one step per stage". Fix: give it its own short stage or a "What happens next" block after the example, or drop it (the hook only needs the qualitative answer).
2. inquiry.json, `johtopaatos` criteria — the fourth criterion ("I distinguished the values of the model from measurements") is not asked by the prompt. Fix: add "and what the numbers are based on" to the prompt, or drop the criterion.
3. inquiry.json, `pred-1` — Cem's option is the longest and the only one that states both stages with the reason, so it can be picked by form. Fix: give Aino and Bea clauses of equal specificity, for example Bea's reason about the ice.
4. inquiry.json, `taulukko` — the correct option states the result ("Pt is about 334 kJ in every row") before the student computes any product. Fix: ask for one computed value first (numeric Pt for the 12 K row), then the choice about the pattern.
5. inquiry.json — the slot names coolant, but the student acts on it nowhere in the inquiry; it is theory plus a pysahdy question only. Fix: a short optional interpret task (mass flow from P, c, ΔT) or make sure the exercises cover it.

## Checked
- Hash cd81e3a1006e1a34 at start and end (--lang en).
- Learning path: the hook question is answered only after the student commits to pred-1; the three prerequisites (Q = cmΔT, latent heat, P = UAΔT) are used and not retaught; the slot's goals are met without extras.
- Predictions: both can be refuted by evidence (the graph, the table); each wrong option's feedback repairs its misconception (cold flows, no heat enters, same percentage) and does not give the answer.
- Evidence fits a lesson without a simulation: a graph (read the plateau, E = Pt, about 334 kJ), a table (Pt constant) and a model-values label; the investigation and the theory graph name their different bags (UA).
- Workload is about one hour: 3 core investigation tasks, an optional sauna task, 2 core checks plus calculation, exit ticket with 2 questions.
- Figures (#2–#6): the hero is recognisable and uncluttered; the cool-bag bars use the same scale, with a label as well as colour; the cooling-circuit schematic is legible at 390 px; the theory figures do not answer the predictions.
- Worked example: 7 stages, symbolic first, units converted in its own stage, reasonableness included (see Polish 1).
- Exit ticket and checks: misconception-based distractors, calculation distractors are real slips (only one stage), explain criteria observable.
- Phone captures (#13 Investigate, #9 example): nothing clipped; formulas wrap; the graph is legible.
- Not judged: language of the Finnish version, exercises (reviewed apart).
