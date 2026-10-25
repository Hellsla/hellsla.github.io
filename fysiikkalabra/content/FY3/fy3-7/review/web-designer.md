VERDICT: PASS
CONTENT-HASH: 5eaa65a93a7374c7

## Blocking
(none)

## Polish
- sim.js:128 — At m = 1 kg, P = 500 W in the steam phase (T about 114 °C, 360 px) the red dot and the steam segment touch the right edge of the "kiehuu … s" label background (review/fy3-7-wd2-sheet360.png, second tile). Boxes do not intersect, it is only tight. Fix: move the boiling label 6 to 8 units further left when the dot is past the plateau.
- sim.js:129 — The faint ghost curve is hidden behind the light label background, so at P = 3000 W the ghost line looks cut under "kiehuu 75 s" and "sulaa 11 s". Fix: lower the background alpha (225 to about 190) or leave as is.
- lesson.md (constants table) — The table is 262 px wide in a 328 px column at 360 px, first column header "Vesi" is a monospace header; both fine. Fix (optional): a header such as "Aine: vesi" would say more.

## Checked
- python3 scripts/check_layout.py fy3-7 and --width 390: both OK; lint 0 errors.
- DOM order canvas, controls (Lämmitä, Nollaa, sliders), readout, note at 1280, 390 and 360 px.
- Top of canvas to bottom of Lämmitä: 472 px (1280, canvas 400 px), 264 px (390), 244 px (360). With the button bottom at 632 px the canvas top is at 160 / 368 / 388 px, so 0 px of the canvas is under the 54 px sticky nav.
- Sweep with simSetQ and simLabels at 1280, 390, 360 px: m 0,1/0,2/0,5/0,75/1,0 kg x P 500/1000/2000/3000 W x 41 points plus each phase boundary (-1, 0, +1 J): 1060 frames per width, all five phases, 0 label boxes intersecting or leaving the canvas, 0 console errors.
- Canvas text rendered about 11 px or more (design size 11 times ts(), k about 1,85 to 2,04 on a phone); thermometer reading moves up when needed, "t (s)" inside the canvas, every second x label on a phone, no run-together tick labels (review/fy3-7-wd2-sheet360.png, 7 extreme settings).
- Controls: Lämmitä 110x40, Nollaa 93x40, sliders 40 px tall and full width (324 / 294 px at 390 / 360); no control overlaps the canvas.
- Heating-curve SVG: 328 / 358 / 608 px wide at 360 / 390 / 1280, inside the text column; smallest text 10,9 px at 360 and 11,9 px at 390; no text boxes overlap, nothing clipped (review/fy3-7-wd2-svg360.png).
- Constants table: 6 rows, 262 px wide, no horizontal scroll at 360 / 390; rows 45 px high; page scrollWidth equals viewport at all three widths.
- Hash 5eaa65a93a7374c7 before and after the review.
