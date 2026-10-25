VERDICT: PASS
CONTENT-HASH: 075de96773c33b9f

Round 2, fy3-8 Lämpölaajeneminen. Measured with my own Playwright scripts at 1280, 390 and 360 px (screenshots in review/fy3-8-r2-*.png). The hash was identical at start and end.

## Blocking
(none) The round-1 item is fixed: the worked-example display is now two aligned rows, 356 px content in a 356 px box at 390 px and 326 in 326 at 360 px, no overflow.

## Polish
1. templates/site.css:108 — at 390 and 360 px the last section-nav pill ("Lähtölippu") is cut off at the right edge (it scrolls, with no visible hint) — optional: a fade or a slightly smaller padding so all four pills fit; ignore if you prefer to keep the template as is.
2. sim.js tick labels — the smallest canvas text renders at 10,8 px at 390/360 px (11 px at 1280); this is above the 10 px limit but with no margin, so do not shrink any label further.

## Checked
- check_layout.py fy3-8: OK at 360 and 390 px; lint 0 errors, 0 warnings.
- No horizontal page scroll (scrollWidth equals clientWidth at 1280, 390, 360); all 3 display formulas fit their box at all three widths.
- Text column 71 characters at 1280 px (608 px, 17 px font), 42 at 390, 38 at 360; line height 28 px.
- Lesson SVG (rod figure) fits the column; smallest text 23,7 / 13,7 / 12,5 px rendered at 1280 / 390 / 360.
- Tap targets: 60 interactive elements, none under 40 px high; button 176×40, sliders and select 40 px high, full width at phone sizes.
- Sim order is canvas, controls (button first), readout; controls do not overlap the canvas; the button ends 479 px (390) and 459 px (360) below the canvas top, so canvas and button fit one 640 px screen with the canvas scrolled in.
- Readout: no overflow; the nowrap value+unit spans keep "120 °C", "10 m" and "−0,34 mm" intact at 360 px.
- Sim sweep: 5 materials × L₀ {1, 10, 37, 100} × T {−40, −20, 20, 60, 100, 120} = 120 states at each of 1280, 390 and 360 px; no canvas label leaves the canvas and no two label boxes intersect (0 issues in all three).
- Worked example opened at 360 px: the two-row ΔL display reads cleanly, units upright.
- Contrast and focus styling come from the shared template and were not changed.
