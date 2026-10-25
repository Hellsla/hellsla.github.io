VERDICT: PASS
CONTENT-HASH: dd2bfcc89612b522

## Blocking
(none)

## Polish
- content/FY3/fy3-1/solutions.md (every "number unit", 0 U+00A0 in file) — a line can still break between number and unit at 390 and 360 px ("4,995 / kg", "18 / N"); use a non-breaking space, a lint rule candidate.
- content/FY3/fy3-1/sim.js:84-85 — at 360 px, Jupiter 100 kg the value label "2480 N" now sits exactly on the 10,0 px floor (99 kg: 10,36); legible, no change needed unless the floor is raised to 10,5.
- templates (optional) — the sim readout is 5 lines at 390 and 360 px (4 at 1280), the scale sentence taking two; fine, no change needed unless it grows further.

## Checked
- Lint 0/0, build ok; no console or page errors, no .katex-error, no raw $ in opened solutions; scrollWidth = viewport at 1280, 390, 360 px.
- Voimamittari SVG in Ydinajatus: fits its column at all widths (608, 358, 328 px wide), nothing clipped (>= 12 px margin to the viewBox edge, weight arrow tip and "G = m g" inside), arrow sits under the block. SVG text 20,3 px at 1280, 11,9 at 390, 10,9 at 360. Screenshots review/fy3-1-r3-svg-{1280,390}.png.
- Canvas text by fillText transform, Maa 10, Kuu 1, Mars 37, Jupiter 100, 99, 1 kg: min 11 px at 1280, 10,8 px at 390, 10,78 px at 360 (scale line); at Jupiter 100 kg and 360 px the "2480 N" label is exactly 10,0 px, 99 kg 10,36 px, 390 px 11,0 px. Nothing outside the canvas.
- Chart y axis ends at full scale with a tick; top bar and its label clear of the title and scale line at 390 and 360 (review/fy3-1-r3-sim-{360,1280}-Jupiter-100.png).
- Readout (m, g, G, scale line), select and slider stacked below the canvas without overlap at 390/360 (gaps 9,6 px); side by side below the canvas at 1280.
- Text column 67 chars at 1280 (608 px), 40 at 390, 36 at 360 (phone limit).
- Section nav (nav.toc): each tap activates the right tab and the tab ends inside the viewport at all three widths.
- Tap targets: 0 links, buttons, inputs, selects or summaries under 40 px at any width; select and slider 40 px high.
- Opened solutions: 21 details, no horizontal overflow at any width.
