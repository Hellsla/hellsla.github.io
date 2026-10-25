VERDICT: FAIL
CONTENT-HASH: b275331a1317e321

## Blocking
- lesson.md:38-39 — inline SVG graph: the x tick label "10" (x=520, middle-anchored) and the axis title "h (m)" (x=570, end-anchored, same y=284) overlap and read as "1h(m)" at 1280, 390 and 360 px — move the axis title right/up (e.g. "h (m)" at y=240 above the axis end, or text-anchor start at x=535) so it clears the tick label.
- lesson.md:41 — same SVG: the label "p = p₀ + ρgh" (x=330, y=80) is crossed by the plotted line itself (line passes y≈70-80 around x=440-470) so "ρgh" is struck through — move it clear of the line (e.g. below-right of the line at x=380, y=140, between the line and the dashed p₀ line, or above-left at x=150, y=60).
- sim.js:100 and sim.js:107-108 — chart at h = 0 m (the default test position, ρ any, box unchecked): the red reading "101 kPa" (drawn at px+10, py+16) lands on the grey "p₀ = 101 kPa" label (CH.x0+6, Y(P0)+16); at 1280, 390 and 360 px the two strings print over each other and are unreadable — at small h skip or move the grey p₀ label (e.g. draw it above the dashed line at the right end) or put the reading above-left.
- sim.js:107-108 — with "Näytä vain ylipaine" ticked and h = 0 m, the reading "0 kPa" (px+10, py+16) overlaps the x tick labels "0" and "5" below the axis (visible at 360 px, same at 390) — place the reading above the point (py - 10) when py is at the bottom of the chart.

## Polish
- sim.js controls (1280 px): the density label wraps to two lines ("(vesi)") and the three controls sit on one row with misaligned labels/sliders; give the density slider more width or put the checkbox on its own row.
- Chart axis title "h (m)" (sim.js:96) touches the red dashed vertical line at h = 20 m; draw it a few px left.
- Body text column is 62 characters at 1280 px (OK) but 31-34 at 390/360 px — site-wide template property, not a lesson defect.

## Checked
- Content hash b275331a1317e321 unchanged at start and end; lint 0 errors.
- No horizontal page scroll at 1280/390/360, also with all details opened; no pageerror.
- No <table> in this lesson (nothing to check); KaTeX display equations fit without scrolling at all widths; solutions (3) readable, 12-14 px+ wrapped, no clipping.
- Sim canvas scales 600→324 (390) / 294 (360) px; canvas text drawn with ts() so it renders at about 11 px; readout is DOM text at 16 px.
- Slider rows 40 px high, checkbox row 40 px (box itself 24 px, label wraps it), summary/button/nav targets at least 40 px.
- Sim values correct at 0 m, 20 m + 1300 kg/m³ (356,1 kPa, 3,53x), and over-only (axis 0-300 kPa, line through origin); controls do not overlap canvas.
- Inline SVG scales to 13 px (390) and 12 px (360) text, uses currentColor, readable contrast.
- Nav is a horizontal scroller at 360 px ("Lähtölippu" partly off-screen, scrolls), 40 px tall.
