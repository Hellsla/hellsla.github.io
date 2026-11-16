VERDICT: PASS
CONTENT-HASH: ebf69c1215a515e0

## Blocking
None.

## Polish
- [Minor] Open-solution captures were read mainly at 390 px; the 360 px check is by check_layout.py and my own DOM measurement.

## Checked
- Own 390 px captures of the opened solutions (preview/fi-easy/fy3-15, scratchpad), plus a DOM measurement of every opened formula at 360, 390 and 1280 px (clipping, off-screen, row breaking inside a katex); check_layout.py --width 360 run.
- Reflowed rows read: aligned equals signs in one column, continuation rows begin with an operator, closing comma or full stop stays in the aligned row (fy3-15-L2-05, fy3-10-L1-07 at 1280, fy3-12-L2-02, fy3-13-L2-06, fy3-16-L3-01).
- New task fy3-9-L2-10 and fy3-11-L2-10 read in full at 390 px (source link first, a–d, long solution): typography and Finnish fine.
- Not every changed solution was opened as a capture; the rest by the DOM measurement only.

## Scores
illustrations 5 · typography 4 · Finnish 4 · accessibility 4
