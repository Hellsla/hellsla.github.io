VERDICT: FAIL
CONTENT-HASH: da8b0d7dc276dfca

## Blocking
- assets/sims/fy6/fy6-4/sim.js:110 draws the hard-coded Finnish label `$\text{sama virta}$` on the canvas, so the English sim shows "sama virta" (capture fy6-4-sim-1280.png, contact-1 #2). The lesson figure "series" has it translated ("same current I"). Fix (outside the translator's remit, assets/): read the label from the sims.fy6-4 strings (add a key such as `samavirta` to lang/fi.json, en.json, fi-easy.json) instead of the literal.

## Polish


## Checked
- Captures contact-1..6: no overflow at 390 or 1280 px, figures (hero, series, parallel, graph, mixed, task) labelled in English, maths renders, experiment tables, select values ("series connection"), titles and the legend box are English.
- Sim legend shortened to 13 words so it is not folded.
- Only Finnish left: the canvas label above.
