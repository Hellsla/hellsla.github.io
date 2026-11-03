VERDICT: PASS
CONTENT-HASH: 0fa18964780034d5

## Blocking
(none) The earlier blocking finding is resolved. The `power` chart is rebuilt:
- Every label is now 16.6 px at 390 and 28 px at 1280 (measured in the browser).
- The captions are in ink and there are no subscripts.
- The grid bar is drawn honestly as a range: a solid bar to 110 MW, a pale dashed range to 620 MW, and "peaks".
- The aria-label matches the drawing.

## Polish
1. [Minor] `power` chart: the 620 label above the dashed range and the "500" label above the fusion bar are the only value labels outside their bars. This is consistent and readable; no change needed unless the author wants "110–620" written once under the bar.

The earlier Polish is resolved:
- The given-line equalities are braced.
- The Reasonableness gives "about 400 MW".
- The tritium Answer is now a full sentence.
- D–T is in LaTeX.
- The criteria numbers are in LaTeX.

## Checked
- Fresh build and captures for this hash: top and intro at 390 and 1280, every stage at 390 and 1280, contact sheets.
- The `power` chart at 2× at 390.
- The `iter` explorer over HTTP at 390 and 1280. The markers measure 17 px at 390 and 20 px at 1280, and they are readable. Selecting the toroidal field coils from the drawing (keyboard) opens its panel 13 px under the drawing, with LaTeX key numbers and sources.
- Playwright: no `.katex-error`, no raw `$` and no overflow.

## Shared issues
- `fx/iter.js`: in the drawing, the cryostat's shapes cover some inner parts for a pointer (a click on the toroidal field coil marker was caught by the cryostat group). Raise the markers above the part shapes (draw them last, `pointer-events` on the marker), so a tap on any number selects that part.

## Scores
illustrations 4 · typography 4 · English/French 4 · accessibility 4

## Re-check 2026-11-01: photographs
- Screenshots at 360, 768 and 1280 px (details opened, image loaded); check_layout.py OK at 360 and 1280 px; figure gaps 20 px above and 24 px below, no overflow, credit on its own line and legible.
- Coil-factory photo ends the section and sits clearly above the 'Words of the machine' matching task.

## Re-check 2026-11-03: vacuum-vessel photo
The teacher's own vacuum-vessel photo sits after the coil photo; checked at 390, 1280 and 1920 px (check_layout OK, image and caption fit, credit legible).
