VERDICT: FAIL
CONTENT-HASH: af964d5101852359

## Blocking
- inquiry.json:509 (activity `data`, text and question) — the text says the fitted line "on piirretty ajatuksissa" and the task asks the student to "lue sovitetulta suoralta toinen piste kuvaajasta", but the figure (fig-1 capture) shows six dots and no line; hint 2 ("suora päättyy noin paikkaan 19 m") refers to a line nobody can see. Fitting a line through noisy points is the lesson goal "analysoida graafisia esityksiä mittausaineistosta", and the student is left to imagine the key object, so the step cannot be followed or checked. — Draw the fitted line (x = 4,1 m + 1,5 m/s · t) in the figure, thin and in the figure's second colour with a label, or have the student place the line first and compare. Drop "piirretty ajatuksissa".

## Polish
- inquiry.json:628 — "mittauskilpi" is not a word; write "rinteessä on mittaustolppa, jonka kohdalla paikka on 0".
- exercises.json fy4-1-L3-01 and inquiry.json (edestakainen feedback) — "keskivauhti" is asked for and used but never defined in lesson.md (only "vauhti" = |v|); add one sentence under Kaava: keskivauhti = matka / aika, and contrast it with keskinopeus.
- Figures at 390 px (fig-3, fig-5, fig-1 captures): tick and variable labels render at about 10-11 px, small for print-quality-on-phone; the fig-5 right-hand labels (v > 0, v = 0, v < 0) are the smallest. Raise the font size or the viewBox crop so labels stay about 12 px at 360 px.
- Sim canvas (sim-390 capture): axis numbers and legend are about 9 px and not LaTeX; the figure rule does not reach the canvas, but the phone reader cannot read the graph axes without zooming.
- exp-1 to exp-3 all end in "read two rows, divide"; the simulation computes the formula it tests (the packet warns about this). The (t,x) graph drawing itself is not acted on: ask in one experiment for a predicted point read off the drawn graph at a given t before the table is filled.

## Checked
- Opening question (distance 4 km, displacement 0) is answered in reflect, check-3 and the edestakainen item; it is not disclosed before commitment.
- Figures: all six redrawn with LaTeX labels, units and the axes; displacement and round-trip figures are simple, uncluttered, and colour is always paired with a sign or text (Δx = +6 m / −5 m, v > 0 / = 0 / < 0).
- Graphs in the example (20, 120, 170 m; dashed extrapolation) match the staged worked example: five steps, one idea each, symbolic before numeric.
- Prediction options are distinct, wrong ones repair the misconception; exp-2 and exp-3 can refute their predictions (model values A 2,0, C 2,0, D -3,0 m/s).
- Exercises: level 1 one formula, level 2 unit conversion and inversion, level 3 reasoning; none repeats the example; solutions in LaTeX with Annettu/Kaava/Sijoitus/Järkevyys.
- Exit ticket tests sign of displacement, slope sign and distance versus displacement: the core idea.
- 1280 px: Tutki shows the simulation beside the experiments and the layout is balanced; 390 px: controls and readout fit with no clipping.
- Workload: three experiments, two data items and exercises is a full but one-hour lesson.
- Finnish: symbols in prose are set as maths; case forms after numbers and units correct.
