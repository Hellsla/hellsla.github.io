VERDICT: FAIL
CONTENT-HASH: 1f33dc6f42ab4ce9

## Blocking
- sim.js:46-47 — At 390 px the readout (5 lines wrapped to 240 px) sits between canvas and controls, so canvas top to bottom of "Lämmitä" is 611 px (390) or 639 px (360). The sticky section nav takes 54 px, so with the button on screen 37 px (390) to 65 px (360) of the canvas is hidden under the nav; canvas and button never fit one 640 px screen (screenshots review/fy3-7-wd-phone360-btnview.png, ...390-btnview.png). Fix: create `controls` before `readout` (canvas, sliders, buttons, then readout); then canvas+button span about 410 px. Shortening the readout (the two "kestää" lines) would also help.
- sim.js:77,112,123,124 — The `ts()` scale (k about 1.85 at 390, 2.04 at 360, text rendered 10-11 px) makes canvas text collide on a phone (sweeps review/fy3-7-wd-sweep-360-*.png; 1280 px is clean for all phases and the four extreme settings):
  1. Thermometer reading ("−10 °C", "100 °C") overlaps the container label ("vesi ja höyry", "jää ja vesi") and the chart's "120" tick label.
  2. x tick labels run together ("20004000", "1000 15002000" with tMax 2000-8000 s).
  3. "t (s)" baseline at y 399 of 400, clipped at the canvas bottom edge.
  Fix: cap k at about 1.4 or give the layout room (labels at 11 px design size, thermometer reading lower/left-aligned, container label centred over the container only), draw every second x tick when k > 1.5, and move "t (s)" up (CH.y0 + ts(28) at most).

## Polish
- lesson.md:34-43 (SVG) — At 360 px the 17-unit labels render 9.3 px ("jää", "höyry") and "jää" touches the y axis; raise font-size to 22 for those and move "jää" right of x=80.
- sim.js:103 — "kuumennin 3000 W" starts 7 px from the canvas edge at 360 px; fine at 390.
- sim.js:128 — The "kiehuu … s" label sits on the faint ghost curve at 360 px; give it a light background or place it above the line by 12 units.
- sim.js (bubbles) — At m = 1 kg a bubble can be drawn on the container's top edge at the start of boiling.

## Checked
- 1280/390/360 px: no horizontal scroll (scrollWidth equals viewport); KaTeX overflows only in hidden MathML.
- All tap targets (links, sliders, buttons, summaries) at least 40 px at all three widths.
- Sliders 40 px tall, full width at 390/360; Lämmitä 110x40, Nollaa 93x40; no control overlaps the canvas.
- Lämmitä click starts the animation; canvas keeps running while the button is in view (t advanced 92 s in 1.5 s).
- Sweep with simSetQ at mid and boundary points of all five phases for m/P = 0.1/3000, 1/500, 0.1/500, 1/3000, 0.5/1000 at 1280: nothing overlaps or clips; text 11-15 px.
- Text column about 60 characters at 1280 (566 px at 18.4 px); body text colour rgb(20,23,30) on light background.
- Heating-curve SVG layout: fits the column at 390 and 360 (width 358/328 px), nothing clipped (slopes not judged).
- No console errors at any width.
- Hash 1f33dc6f42ab4ce9 before and after the review.
