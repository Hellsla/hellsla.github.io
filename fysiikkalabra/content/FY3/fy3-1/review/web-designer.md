VERDICT: PASS
CONTENT-HASH: d47c5d24760dd2a6

## Blocking
(none)

## Polish
- content/FY3/fy3-1/sim.js:46-50 — readout strings ("m = 10 kg", "9,81 m/s²", "0–248 N") still use plain spaces (the only 5 plain number-unit spaces on the page); measured no break in 36 states at 1280, 390 and 360 px, so latent only — use U+00A0 when sim.js is next edited.

## Checked
- Lint 0/0, build ok, hash unchanged start to end (d47c5d24760dd2a6); no console or page errors, no .katex-error, scrollWidth = viewport at 1280, 390, 360 px.
- Canvas chart, 4 bodies x mass 1 and 100 kg x 3 widths (24 states), text boxes captured from fillText (measureText): "asteikko 0–X N" overlaps no other label; nearest is the Jupiter value label, gap 110-146 px (1280), 42-54 px (390 logical, about 21-26 rendered), 24-34 px (360 logical, about 12-17 rendered); the first (Kuu) bar label is never in the scale text's band.
- Scale text is left-aligned beside the top tick of the y axis; rendered size 11,0 px (1280), 10,8 px (390, 360); smallest canvas text 10,0 px (the shrunk "2480 N" label at 360 px), none below 10; nothing past the canvas edge (max x 595 of 600).
- Title sits 12-20 logical px above the scale line, no touching at any width; Voimamittari and weight arrow unchanged and unclipped at 100 kg.
- kN: "1,18 kN" now uses U+00A0 (preview/fy3-1.html:76); all 15 "Vastaus" reveals use U+00A0 (e.g. "39 N", "6,0 cm", "69 kg"); 0 number-unit breaks at 1280, 390, 360 px with all details open (incl. L3-03 text, 26 kg and 9,81 m/s²).
- Sim readout 4 lines at 1280, 5 at 390/360 in all 108 slider states sampled, no break before a unit, no overlap with canvas or controls.
- Tap targets: no link, button, input, select or summary under 40 px at any width; no katex-display, svg, canvas, table or pre wider than the viewport.
- Text column 566 px wide at 18,4 px body font at 1280 (about 65-70 characters), 316 px and 286 px at 390 and 360 px; contrast unchanged (dark text on cream).
- Screenshots review/fy3-1-r5-montage-{1280,390,360}.png (Kuu 1 kg, Jupiter 100 kg, Maa 1 kg), review/fy3-1-r5-chart-*.png, review/fy3-1-r5-full-*.png.
