VERDICT: PASS
CONTENT-HASH: d31013346dd6f94d

## Blocking
(none) Round-1 blockers are fixed: pred-3 now points to Teoriatiivistelmä (the stage that exists), the activity texts and the experiments' Alkutila lines and table headers carry symbols as maths, and the "W = pinta-ala" label no longer sits on the canvas top in the plain sim capture.

## Polish
- Simulation canvas and DOM readout (W = F · s, "Voima F = 60 N", axis labels) stay plain interface text; per NOTES.md §1 this awaits the teacher's decision, not a defect of the lesson.
- fy3-2-exp-exp-1-390.png — in the experiment's embedded sim at 390 px the "W = pinta-ala" label still overlaps the "F (N)" axis label (clear only in fy3-2-sim-390.png) — shorten the label or move it right of the axis title.
- Experiments' Alkutila line: "Vakiona: F, t ." leaves a stray space before the full stop at 390 px (a maths-span/line-wrap artefact) — keep the full stop inside the sentence's nowrap run.
- Both experiments only compute W = Fs and P = W/t, so they check the program's arithmetic more than the physics; the Joule table (interpret) is what carries real measurement. Acceptable for this slot; a later round could add noisy data to the table.
- Exit ticket question 1 asks "kuinka suuren työn kannatteleva voimasi tekee yhteensä" and answers about 98 J although only the lifting phase counts; consider "kuinka suuren työn nostovoima ja kannatteleva voima tekevät yhteensä" so the wording matches the answer.

## Checked
- Path Pohdinta → Ennusta → Tutki → Teoriatiivistelmä → Sovella → Tarkista → Tehtävät; hook question answered by pred-3, reflect and the figure.
- Predictions refutable by exp-1 and exp-2 (min 2); pred-3 honestly marked as not testable in the sim.
- Wrong-option feedback repairs the misconception without disclosing the answer beforehand.
- Worked example staged one step per stage, with a plausibility check; error-spotting item targets the 8,0 J slip.
- Exercises levels 1-3 differ from the example; exit ticket tests the core idea.
- Joule table labelled as example values, simulation values as model values; model simplifications stated.
- Speed control: howto states it changes only the animation pace, W and P unchanged.
- Phone captures at 390 px: no clipping, controls readable; 1280 px lab layout puts experiments beside the sim.
- Finnish and case after number+unit correct in the text I read.
