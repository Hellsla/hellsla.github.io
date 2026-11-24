VERDICT: PASS
CONTENT-HASH: 1f755be05cba69e8

## Blocking

## Polish
- inquiry.json koe-3 question — the prompt hard-codes "Pienin saavutettu poikkeama on noin 5,8 °C", but b is locked at 80 °C, so the student's own minimum may differ from a true best-fit d. Say "kun $b = 80\,{}^\circ\text{C}$" or let the student quote their own table value.
- inquiry.json ennuste-1 / koe-1 — the polyline option cannot be tested in the simulation (it only moves a straight line); the refutation is carried by the feedback numbers (slopes 0,2 … 0,8). Acceptable, but the experiment intro could invite the student to compare the red segments with the jagged slopes between neighbouring points.
- simulaatio / lesson.md "Suora sovitetaan" — the sim's criterion is the smallest d (RMS), the lesson's is a visual one ("pisteitä molemmin puolin, lähellä kaikkia"). A sentence in `calc` or the conclusion saying that by eye the two give nearly the same line would stop "paras suora = pienin d" from becoming the only rule. "Keskimääräinen poikkeama" for an RMS value is also loose; "neliöllinen keskipoikkeama" is more exact if the glossary allows it.
- Workload — two predictions, three experiments with at least three rows each, a sim, an explain task, the example, three checks and an exit ticket is near the upper limit for one lesson. Koe 3 could go inside "Lisää tutkittavaa" if the lesson runs long.
- inquiry.json ennuste-2 — the prompt already says the line is extended to V = 0 and names the container ("mittalasin ja nesteen yhteismassa"). This is fair, since the student has to reason about it, but the correct option is the most elaborate one. Shorten it a little to even the lengths out.

## Checked
- Path: retrieval (random error), then prediction, then experiment, then theory, then example and exercises. The hook's question is answered by the conclusion and the reflect task, and the slot's three goals are all covered.
- Predictions can be argued from the data before the evidence. Every wrong option's feedback is gated on commitment and repairs the misconception with numbers (polyline, forcing the line through a point, b = 0).
- Experiments can refute their predictions: d has a clear minimum near k = 0,5 m/s and b ≈ 61 g, and Koe 3 shows a pattern in the deviations. Variable control is clear and the locks are stated.
- Koe 3 and its question teach "a small d does not mean the model fits" (the direction of the deviations); this is the central lesson of the model.
- The worked example (kettle) has seven stages, one step each, with a figure showing A, B and the 40 °C dashed construction. Its numbers are consistent: the maximum deviation is about 1 °C, and the interval check is correct.
- Etsi virhe and the transfer task have realistic distractors (Δt/Δs, s/t through the origin, mixing up k and b) with feedback that names the error. The figure task works: the coordinates are read from the grid, and the aria-label gives the same data without computing k.
- Checks and exit ticket test the concept (b ≠ 0 means not proportional) and the calculation. The explain criteria are observable and match the question.
- Captures: the sim at 390 and 1280 px is legible, with usage, assumptions and computation behind closed boxes. The experiments sit beside the sim at 1280 px. The kettle figure at 390 px is small but legible.
- Finnish: terms (kuvaaja, kulmakerroin, suoran sovitus, lineaarinen malli) match the glossary; no case errors found.
- Exercises not judged (own review).
