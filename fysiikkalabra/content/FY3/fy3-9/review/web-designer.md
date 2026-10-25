VERDICT: PASS
CONTENT-HASH: cf20356e5007c164

## Blocking
None.

## Polish
- lesson.md:27 — SVG labels (p, V, 1/V) render at 11,4 px at 390 px and 10,4 px at 360 px, barely above the 10 px floor — raise font-size on the `<svg>` from 20px to about 26px (about 14 px on phones).
- lesson.md:27 — known, with the fixer: the (1/V, p) panel shows 6 points against 8 in the (V, p) panel.
- sim.js:78 — the legend note (thin line, dashed line, red dot) sits below the table, which is 467 px tall with 10 rows at 360 px, so the legend is a screen away from the canvas — create the note before `table` in setup.
- templates (tab nav) — at 360 px the sticky tab bar clips "Lähtölippu" (scrolls sideways); acceptable, only for the human's template work.

## Checked
- check_layout.py fy3-9 OK at 360 and 390 px; no horizontal page scroll at 1280, 390, 360 px.
- Text column 67 characters per line at 1280 px; 40 and 36 at 390 and 360 px.
- After the "Simulaatio" tab at 390 px: canvas 216 px and "Tallenna mittaus" (y 337–377) in one 640 px screen; at 360 px canvas 196 px, button y 317–357.
- Canvas text rendered size (fillText hook): smallest 11,0 px at 1280, 10,8 px at 390 and 360 px.
- Sweep of all modes (incl. the 1/V view), slider extremes plus 4–6 values, at 1280, 390, 360 px: 0 text overlaps, 0 clipped texts; extremes at 360 px inspected by eye.
- 10-row table at 360 px: five columns fit, rows 41 px, 17 px type; the eleventh save shows "taulukko on täynnä".
- Tap targets at 360/390 px at least 40 px (22 px checkbox sits in a 40 px label row); smallest body type 14,4 px.
- Formulas, exit ticket and closed exercise levels fit 390 px; hash identical before and after.
