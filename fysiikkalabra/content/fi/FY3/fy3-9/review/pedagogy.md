VERDICT: PASS
CONTENT-HASH: 532dc0152871b210

## Blocking

## Polish
- Readout at 390 px (fy3-9-sim-390.png): "Vakio pV = 100,0 kPa · 50,0 ml = 5000 kPa · ml" still breaks before "ml"; keep the unit with its number (non-breaking space) or wrap the whole product.
- exp-1 table gives p in Pa while the readout gives kPa; the intro explains it, but one unit (kPa, pV in kPa·ml) would remove the conversion.
- Ennusta 1/2 feedback starts every option with "Mallin arvoissa ..."; a shorter lead ("Koe 1 antoi ...") reads better.
- exp-2 question mixes two tasks (ml/K and the relative share) with a choice about where γ comes from; split so the calculation is its own numeric item.
- ruisku item: the text already says the 30 ml row was pressed quickly, which gives away the diagnosis; drop the cause and let the choice carry it.

## Checked
- Round 1 blocker, canvas label size: the capture set (fy3-9-sim-390, exp-exp-2-390-1, lab-1280-1) was taken from a stale preview (preview/fy3-9-sim.js older than sim.js, still printing gauge numbers). I rebuilt the preview (sim.js now identical) and recaptured the canvas at 390 and 1280 px.
- 390 px: thermometer ticks (150, 50, −50 °C), graph axis numbers (300/200/100/0, 40, 80), axis names and V, T and p readouts are legible; sim-embed.js floors canvas text at 10 px.
- Gauge: no dial numbers or unit, needle and hub are clear; the reading "100,0 kPa" stands above it, so nothing sits under the needle.
- 1280 px: all labels legible, graph readable, no collisions. The graph, with its dashed lines to the axes, can be read by a phone student, so the exp-2 extrapolation is feasible.
- Learning path, activities, predictions, experiments, figures, example, exercises, exit ticket and Finnish are unchanged since round 1 (inquiry tests pass) and still hold.
- Hash unchanged at start and end.
