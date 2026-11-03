VERDICT: PASS
CONTENT-HASH: 9b7b3cfd647b8aba

## Blocking
(none)

## Polish
- inquiry.json `mittaus` (+ `epavarmuus`) — the figure `fy7-3/coil-fit` is not needed to answer: the text already gives the table and the slope A with its uncertainty, and the solution's "Kuvaajan lukeminen" step re-derives a number the student was handed. Either leave A out of the text (give only the table and "ohjelma sovitti suoran") so the student reads the slope from the figure, or drop the figure from the task.
- inquiry.json `mittaus`, stage tutki — the task needs B = μ0 N I / l and the sum rule for uncertainties, which the theory stage only states afterwards; only hint 2 supplies them. Add one sentence to the task text ("Pitkän käämin keskellä B on suoraan verrannollinen virtaan") or move both tasks after the theory stage.
- inquiry.json `epavarmuus` solution — "tulos on noin 1,25 · 10⁻⁶": 1,2326 : 0,98 = 1,258, so write "noin 1,26 · 10⁻⁶". The aria-label of `coil-field` says "vasen pää eteläpää S": write "vasen pää on etelänapa S".
- lesson.md "Käämin kenttä" / exercises L2-04, L3-01, L3-03 — the lesson never says that fields of several sources add as vectors, yet three exercises depend on it. One sentence in "Ydinajatus" (kenttien vektorisumma) would spare the student from meeting it first in a solution.
- Slot goal "kahden virtajohtimen välinen voima" has no activity here. Fine if fy7-4 owns the force (the lesson stays honest: it does not claim it), but check that fy7-4 does.

## Checked
- Path: Ørsted hook, retrieval, two refutable predictions (stretched coil, coil end), sim, two single-variable experiments with locked parameters, explain, theory after the evidence; the opening question is answered in `pohdi`.
- Prediction feedback cites model values and repairs the misconception (turn count vs turn density; "not homogeneous to the end"); numbers verified (B(2 cm outside end) = 0,36 mT).
- Figures at 390 px (wire-field, fig-7 graph) legible, colour with meaning (current violet, B green, compass tip pink plus shape), alt text carries the data.
- Sim at 390 px: controls, readout, fold-outs and the B(x) graph clear; model assumptions stated at point of use, values called model values.
- Worked example: six single-step stages, units and sanity check; the common-misconception section matches the experiments.
- Exit ticket: Q1 tests the core idea (N·I constant), Q2 tests the right-hand rule for the coil; both answers correct.
- Tarkista: concept check with misconception distractors, numeric with real mistake values, explain with observable criteria.
- Finnish (fi-easy): short sentences, terms explained (tangentti, alkeisalue), case after number+unit correct.
- Workload is on the heavy side for one hour (two experiments plus the LOPS measurement and uncertainty), but the reflect, error-spotting, transfer and third check are optional.
