VERDICT: PASS
CONTENT-HASH: 1d8ca5724c6f80b9

## Blocking
- none

## Polish
- [Minor] fy3-10 sim, first moments after load or reset: the diff (`if (!top) [top, tStep] = scale(1)`) changes only the axis shown before the first settled average. No capture shows that moment, because the screenshots are taken after settling. I judged it from the source and the settled captures. The pressure axis is 0 to 1.5 in the settled state, so the 1, 2 or 5 · 10ⁿ scale rule gives a sensible starting axis. If it can be checked cheaply, glance at the first second after a reset to confirm the bar and gauge are not clipped.
- [Minor] Carried over from the previous report and still open: the bar height and gauge needle keep moving while the number is hidden during settling. The readout says it is settling, so this is acceptable.

## Checked
- Delta review: the diff is a single line in `lessons/FY3/fy3-10/sim.js` (the axis before the first settled average).
- Opened `fy3-10-sim-390.png` and `fy3-10-sim-1280.png`. At both widths the axis labels (0, 0,5, 1,0, 1,5) are present, with a decimal comma on the canvas, which is allowed. The "1,04" label sits above the bar, the dashed reference line is at 1,0, and the gauge, legend, "hits/s" label and V arrow are intact. There is no clipping or overlap. The slider labels and readout render as KaTeX with upright units. The collapsible boxes are in order and nothing overflows horizontally.
- Text, figures and exercises are unchanged, so I did not reopen them.

## Scores
illustrations 5 · typography 5 · Finnish 5 · accessibility 4
