VERDICT: PASS
CONTENT-HASH: 536cade809f2b051

Round 3, preview/fy3-3.html. Measured with own Playwright script (screenshots in review/fy3-3-*.png).

1. Text column: 608 px wide at 1280, 17 px font, about 67 characters per line (OK, 60-75). At 390 the column is 358 px, about 40 characters, which is normal for a phone.
2. Horizontal overflow: none at 1280, 390, 360 or 320 (documentElement.scrollWidth equals the viewport width each time; no element outside a scroll container extends past it).
3. Maths: 0 .katex-error elements and no raw LaTeX in the page. Display formulas and inline maths are readable in the 390 screenshot.
4. 7-column table (θ, 0, 20, 40, 60, 80, 100): header and data cells have identical left edges and widths (91:79, 170:57, 227:54 ... at 1280). At 390 the table is display:block with overflow-x:auto, clientWidth 356 against scrollWidth 394, so it scrolls inside itself while the page does not scroll (at 320: 286 against 394). The header row is JetBrains Mono and the data row is Plus Jakarta Sans. This is a minor style inconsistency, not a defect.
5. SVG figure: viewBox 600 wide, scale 0.597 at 390 and 0.547 at 360, so label text renders at 14.3 px and 13.1 px (above the 10 px target). The role=img aria-label is present. There is no <figcaption>; the line "Pisteet asettuvat suoralle:" above the figure serves as the caption. The labels −270, 0, 100, 137, p = 0 are all visible and unclipped.
6. Simulation: sliders are 40 px high and their labels 64 px (275 px wide at 1280, 324 px at 390). The readout (T = 300 K, p ≈ 115, speed line), the two slider labels and the note are stacked in order with no overlap (the note's top is below the second slider). Canvas is 324x216 at 390 (scaled 0.54). Thermometer labels "600 K", "100 K" and "300 K" are inside the canvas and not clipped. In-canvas text is p5 text scaled with ts(), about 11-12 px at 390, in grey 90 on a light background, roughly 6:1. The numeric readout is DOM text at 16 px, and the note is 14.4 px.
7. Exercises: all 18 <details> elements (3 levels plus answers) are closed by default; summaries are 40 px high. The exit ticket (#exit, "Lähtölippu") is reachable at the bottom of the page and its answer is collapsible.
8. Contrast (390): body 16.1:1, note 8.6:1, th 7.1:1, summary and link green 9.1:1 / 8.2:1, slider labels 17.9:1. The slider accent #1a4d2e is dark green on a light track, well above 3:1 for non-text. All checked colours pass.
9. Tap targets: no a/button/summary/input/select smaller than 40 px in height at 390 (0 found). Smallest text is 12.8 px.

Minor, non-blocking: the monospace header against the sans data cells in the table (item 4); the figure has no <figcaption> (item 5).
