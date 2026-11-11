VERDICT: PASS
CONTENT-HASH: 657d9c21afc1fe02

## Blocking
- none

## Polish
- [Minor] fy3-10 sim.js, starting state: the new line sets the starting axis, so no tick is drawn at 0/0. The shots set has only settled captures, so this was read from the diff, not from a capture. Check once by eye that the axis shows no 0/0 tick right after "Nollaa mittaus".
- [Minor] lesson.md repeats "Silloin" in the kaasuvakio passage (carried over from the earlier report, still open).

## Checked
- Delta review: the only change is one line in lessons/FY3/fy3-10/sim.js (the starting gauge scale, `if (!top) [top, tStep] = scale(1)`). It adds no text and no formula.
- Opened fy3-10-sim-390.png and fy3-10-sim-1280.png: canvas, bar chart, gauge, axis ticks (0, 0,5, 1,0, 1,5), dashed reference line, legend, readout and sliders are intact; nothing is clipped, nothing overlaps, no horizontal overflow; KaTeX units are upright with a thin space; the decimal comma on the canvas is allowed.
- The earlier checks stand: the settling state, the "Luvun tärkeät käsitteet" panel and the earlier text edits.
- The other captures were not opened, because the diff touches nothing else on the page.

## Scores
illustrations 5 · typography 5 · Finnish 4 · accessibility 4
