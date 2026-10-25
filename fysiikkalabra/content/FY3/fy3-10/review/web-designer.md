VERDICT: PASS
CONTENT-HASH: f0622edf75e125b6

## Blocking
(none)

## Polish
- content/FY3/fy3-10/sim.js:147 — the subscript "ref" in the axis name p/p_ref is drawn with `ts(10)`, which renders at 9.8 px at 360 px width (below the 10 px target; 10.4 px at 390, 10 px at 1280). Only this label is affected, and the full name is repeated as DOM text in the readout — use `ts(11)` (and shift the baseline offset `ts(3)` if needed).

## Checked
- python3 scripts/check_layout.py fy3-10 and --width 390: OK, no overflow (page scrollWidth equals viewport at 1280, 390, 360).
- Own Playwright measurement of the canvas plus button plus three sliders: 543 px (1280), 479 px (390), 459 px (360) from canvas top to last slider bottom, so they fit one 640 px screen even with the sticky nav; button is first in .controls.
- Sweep of N 20/100/200 x T 100/300/600 x V 25/60/100 (27 combos each at 1280, 390, 360, simAdvance(3) between): no overlapping or clipped canvas text boxes (fillText calls instrumented); the only hit is the 9.8 px "ref" at 360 (Polish).
- Canvas text sizes at 360 px: 10.8 to 14.2 px apart from "ref"; pressure axis ticks and bar value labels stay clear of each other when the axis rescales (extreme N=200, T=600, V=25 screenshot checked).
- Tap targets: button 151x40, sliders 40 px high, nav items at least 40x40; no element under 40 px found at any width.
- Controls sit under the canvas and do not overlap it; labels (N, T, V values) are DOM text of 14.4 px.
- Text column about 67 characters at 1280 px; no wide formulas, figures or tables overflowing at 390 or 360 px.
- Screenshots in review/fy3-10-wd-*.png (git-ignored).
