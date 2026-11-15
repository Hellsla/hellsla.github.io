VERDICT: PASS
CONTENT-HASH: 3ccad76c26d15915

## Blocking
(none)

## Polish
- lesson.md:122 (Key idea, "Boyle's law can be verified experimentally") — one paragraph of about 150 words, over the 120-word limit; split after "...room temperature." so that the graph step (new column 1/V, straight line) is its own paragraph.
- sim readout (fy3-9-sim-390.png) — English page shows `100,0 kPa`, `293,15 K`, decimal commas; use points in English. The sim also has two boxes, "Assumptions of the model and explanation" and "Assumptions of the model"; merge them.
- inquiry.json exp-2 `question` — it first asks the student to calculate ml/K and a fraction, then offers a choice about where γ comes from; the choice cannot record the calculation. Make the prompt the single choice question and move the calculation to the intro.
- inquiry.json ruisku — the student is told to "calculate a new column pV (or 1/V)"; the slot skill is the 1/V column and the straight-line graph, so ask for 1/V explicitly and let pV be the check, otherwise 1/V is met only in the conclusion and the sim's toggle.
- Workload is near an hour's limit; pred-3 and exp-2's γ question could be optional.

## Checked
- Path: prerequisites p = F/A (retrieval with a syringe), thermal expansion of gases (γ for air linked to V/T in exp-2); opening bag question is answered by Boyle's law and the worked example uses its own 101 → 78 kPa data.
- Slot goals met: Boyle's law verified, inverse proportionality graphically, new column 1/V, isothermal/isobaric/isochoric named.
- Predictions refutable: pred-1 (ratio 2 vs 1.5 or 4) and pred-2 (Celsius ratio vs kelvin) against a sim whose result is pV/T = const; model/calc boxes state that it does not prove the law, and the syringe table with one deviant row supplies the real-data side.
- Syringe data checked: pV = 5040 except 5430 at 30 ml; the correct option (warming) and the leak distractor are consistent with the numbers.
- Variable control: exp-1 locks mode and temperature, exp-2 locks the mode and keeps the pressure by a weight.
- Distractors are misconceptions (50 % rule of thumb, Celsius ratio, 1 ml per degree, line through origin); error-spotting item has the upside-down ratio.
- Worked example seven stages, symbolic first, pV check; siirto and the graph exercise solutions followed step by step.
