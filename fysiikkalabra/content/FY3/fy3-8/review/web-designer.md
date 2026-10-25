VERDICT: FAIL
CONTENT-HASH: f39de205ac113173

## Blocking
- lesson.md:62 — worked-example display formula is 481 px wide in a 326 px (360 px phone) or 356 px (390 px phone) box, so it scrolls sideways and the result "0,0864 m ≈ 86 mm" is cut off (review/fy3-8-390-math.png) — split over two lines with `\begin{aligned}\Delta L &= 12\cdot10^{-6}\,\tfrac1{\text{K}}\cdot120\,\text{m}\cdot60\,\text{K}\\ &= 0{,}0864\,\text{m}\approx 86\,\text{mm}\end{aligned}`. It is the only overflowing formula (solutions opened, 360 and 390 px).

## Polish
- sim.js:71 — the readout breaks "120 °C" over two lines at 360 px — use a non-breaking space between value and unit.
- lesson.md:42 — rod SVG text renders at 10,9 px at 360 px (font-size 20 in a 328 px wide 600-unit viewBox) — raise to 24.
- exercises.json:74 — unit "· 10⁻⁶ 1/K" starts with a lone dot beside the "?" field — use "10⁻⁶ 1/K" (the task already says "yksikössä 10⁻⁶ 1/K").
- At 360 px the L2-04 button wraps under the field because of the long unit; nothing clipped, 40 px targets — no action.

## Checked
- No horizontal page overflow at 1280, 390, 360 px; no console errors; nav tabs 40 px high.
- Canvas 324×216 (390) and 294×196 (360); canvas top to button bottom 479 px (390), 459 px (360), 543 px (1280): fits one 640 px screen, also with the 54 px sticky nav.
- Select, sliders and button are 40 px high; controls sit below the canvas, no overlap.
- Sweep of 5 materials × L₀ {1, 10, 37, 100} × T {−40, −5, 20, 21, 60, 120} (120 states) at 1280, 390, 360 px, every fillText box recorded: 0 text overlaps, 0 labels outside the canvas.
- Smallest canvas text 10,8 px at 390 and 360 px (11 px at 1280); screenshots review/fy3-8-phone-*.png, fy3-8-canvas-*.png read cleanly.
- Hot 100 m aluminium lattice leaves the dashed box as intended, no collision with captions.
- Both tables fit at 360 px (17 px text, 45 px rows); rod SVG scales to 328 px, nothing clipped.
- L2-04 unit "· 10⁻⁶ 1/K" renders correctly (superscript minus) next to the field at all three widths.
- Text column about 34 characters at 390 px (narrow, phone norm).
- Hash unchanged from start to end.
