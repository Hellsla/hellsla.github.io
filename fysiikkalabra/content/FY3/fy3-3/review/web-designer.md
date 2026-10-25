VERDICT: FAIL
CONTENT-HASH: 9c6ecf76a631b766

Reviewed preview/fy3-3.html at 1280, 390, 360, 320 px (Chromium 1243, own Playwright scripts). Screenshots in review/ (fy3-3-*.png, git-ignored). Hash checked before and after: unchanged.

Passes: no horizontal page overflow at any width (scrollWidth == clientWidth at 1280/390/360/320); display formulas with fractions render and fit; exercises (3 levels) and exit ticket collapsible with marker, skip link and summaries all 40 px high; sliders 40 px high, full width, readout (fixed 120 px high at 390/320 for all T and V, so no layout shift while dragging) and note sit below the canvas, no overlap; in-canvas V label is 12 px on screen at every width (k scaling works); contrast: body 16.2:1, th 7.1:1, note 8.6:1, summary link 9.1:1, particle #1a4d2e on #fafafa 9.4:1, thermometer fill 4.9:1, thermometer outline and box 10.6:1, canvas grey labels 6.6:1 (all above AA and the 3:1 non-text limit); sim extremes (600 K / 0,5 dm³ and 100 K / 2,0 dm³) behave and the box is not clipped; no console errors.

Findings (FAIL reasons are 1 and 2)

1. FAIL, pressure table: header row and data row columns do not line up. Cause is the last rule of site.css `table thead,table tbody{display:table;width:100%}`, which turns thead and tbody into two separate tables with independent column widths. Measured left edges at 390 px: header 17,98,135,181,227,273,318 vs data 17,96,153,207,255,308,360 (drift up to 42 px; header "100" sits over the data value 129, "80" over 122). At 1280 the drift is up to 17 px (header 230,292 vs data 213,300). Also the header background is only 337 px wide while the body scrolls to 394 px, so the tint stops before the last column. Scrolls inside itself correctly (scrollWidth 394 vs clientWidth 356/326/286), but the pairing θ-p is wrong on phones. Tested fix (injected, verified: both rows then have identical left edges 17,96,153,207,255,308,360 at 390 and 91,170,227,281,329,382,434 at 1280):
   ```css
   /* delete: table thead,table tbody{display:table;width:100%} */
   table{display:block;width:fit-content;max-width:100%;overflow-x:auto}
   ```
   Optional so the 137 column fits at 360 px: `th,td{padding:.5rem .55rem}` (data row min width falls from about 395 px to about 320 px).

2. FAIL, simulation thermometer labels are clipped at the right edge of the canvas at phone widths. In sim.js the labels `'600 K'` and `'100 K'` start at x = tx+14 = 554 of 600; at 390 px the text is scaled with k = 1.85 (22 px canvas units) so it ends beyond x = 600 and the "K" is cut; at 320 px (k = 2.36) only "600" and "100" remain visible (screenshots fy3-3-sim-320-*.png, fy3-3-sim-390-hot-small.png). Proposal (sim.js, thermometer block): put the scale labels to the left of the tube, where there is room (box right edge is at most 444, labels would start near 454 at 320):
   ```js
   p.textAlign(p.RIGHT); p.text('600 K', tx - 14, ty + ts(8)); p.text('100 K', tx - 14, ty + th);
   ```
   or keep them on the right and use `const tx = 500` plus shorter labels `'600'`, `'100'` (unit is already in the label under the bulb).

3. Minor, SVG figure labels small on phones. viewBox 600 wide, font-size 18 -> effective 10.3 px at 390, 9.4 px at 360, 8.2 px at 320 (1280: 17.8 px). Axes, the dashed extrapolated line (to the open circle at -270, "p = 0") and the 6 points are clear at 390; legibility of the labels is marginal at 390 and poor at 320. Dashed/axis strokes (2 px in viewBox) become about 1.1 px at 390. Proposal:
   ```html
   style="max-width:100%;font-family:system-ui,sans-serif;font-size:24px"   <!-- 13.7 px at 390, 10.9 px at 320 -->
   ```
   and stroke-width 3 on the axes/dashed line (4 on the solid segment). Check that "-270" (centred at x=107) and "p = 0" (x=121) do not collide at 24 px: they are on different baselines (282 vs 228), fine.

4. Minor, line length at 1280: article column is 608 px at 17 px, measured 65-81 characters per line (mean about 74) on the long paragraphs; slightly above the 60-75 target on some lines. Proposal: `main.reading{max-width:36rem}` (about 70 characters) if the human wants to tighten it.

5. Minor, text breaking in exercise L2-04: "-173 °C" wraps between number and unit at 390 ("−173 / °C"). Proposal in exercises.json (needs fixer): use `−173 °C` (no-break space) in the text; same idea for other "number unit" pairs.

6. Info (not a defect): at the default state the readout shows p ≈ 104-107 (measured) next to "teoria 100", because the fixed 1,5 s window starts with the seeded particles; students may ask why they differ. A short note in the sim text ("mittaus vaihtelee hieman") would pre-empt it.

Tap targets: all links, summaries, sliders measured >= 40 px high at every width; none smaller found.
