VERDICT: FAIL
CONTENT-HASH: edd01c91e24f237e

## Blocking
- content/FY3/fy3-9/sim.js (canvas labels) — at 390 px (fy3-9-sim-390.png, fy3-9-exp-exp-2-390-1.png) the KaTeX labels shrink with the canvas to about 7 px: the thermometer ticks (150 °C … −50 °C), the graph axis numbers (50, 100, 200, 40, 80, 200, 400) and the gauge scale (0/200/300 and "kPa") cannot be read, and in the gauge the "kPa" and the figure "100" sit under the needle hub. The graph is the point of the lesson (read p off the curve, follow the dashed line to the origin in exp-2), so a phone student cannot do it. Fix: draw canvas text at a size that is at least about 11 px after scaling (scale font by the canvas-to-CSS ratio, fewer ticks: 0/100/200/300 and 0/50/100 ml), put the gauge unit outside the dial, and keep the live values in the text readout below, which is legible.
- Same cause at 1280 px (fy3-9-lab-1280-1.png): in the narrow sim column tick labels are about 9 px and the gauge "100" collides with the needle; fix with the same minimum size.

## Polish
- Readout, 390 px: "Vakio pV = 100,0 kPa · 50,0 ml = 5000 kPa · ml" breaks between "·" and "ml"; use a non-breaking thin space, or wrap the whole product.
- exp-1 table shows p in Pa while the simulation readout shows kPa; the intro explains it, but one unit throughout (kPa, pV in kPa·ml) would remove the conversion the student must hold.
- Ennusta 1/2 feedback says "Mallin arvoissa ..." for every option, which is repetitive; a shorter lead ("Koe 1 antoi ...") reads better.
- exp-2 question mixes two tasks (compute ml/K and the relative share) with a choice about the origin of γ; consider splitting so the calculation is a numeric item.
- ruisku item: the 30 ml row's "nopea puristus" is given in the text, so the diagnosis is partly disclosed; remove "Yhden mittauksen kohdalla ..." sentence's cause and let the choice carry it.

## Checked
- Learning path: hook, retrieval (F = pA), three predictions, two guided experiments, syringe data with a 1/V column, theory, example, transfer, three checks, matches the slot goals (Boylen todentaminen, 1/V graph, new column); one lesson's workload.
- Predictions are refutable by exp-1/exp-2; options carry their own feedback; no answer shown before commitment.
- Experiments lock the controlled quantities and vary one; the sim's computed values are called model values, and the syringe data are labelled example values.
- Figures (micro-boyle, iso-processes, boyle-graphs, absolute-zero) are placed after their paragraphs and legible in the 390 px captures.
- Worked example has five stages, symbolic first, units, sanity check; not repeated in exercises.
- Exercises: 5/4/3, contexts varied, level 3 needs two ideas; exit ticket tests the core ideas (Boyle, 1/V graph, kelvin).
- Finnish: terms agree with the glossary; case after number+unit correct in the text read.
- 1280 px wide layout: sim beside experiments, readable line width, no overlap outside the canvas.
- Only the canvas text legibility blocks; hash unchanged at end.
