VERDICT: PASS
CONTENT-HASH: d64245a72386bc55

## Blocking
- none

## Polish
- [Minor] sim chart at 390 px — "1 000" now ends about 2 px from the axis, with no tick, and the data dot sits at the end of the label, so label and dot almost touch while "0" keeps its tick — optional: a slightly smaller tick-number size on a phone so the tick and a 4 px gap fit.

## Checked
- Delta: only the chart's tick-number drawing in assets/sims/fy2/fy2-1/sim.js changed.
- fy2-1-sim-390.png, opened whole and the chart cropped at 4x. "1 000" is complete and not clipped, and it is readable. It is no longer cut at the left edge of the canvas. The dashed gridline marks the value. The "0" tick, the t ticks, the axis titles and the surrounding layout are intact.
- fy2-1-sim-1280.png: "1000" with its tick is unchanged, with no regression. The decimal comma and spacing follow the sim exception.
- The rest of the page is untouched by the diff. I did not reopen the other captures.
- Hash at start and end (--lang fi-easy): d64245a72386bc55, matching the stamp.

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 5
