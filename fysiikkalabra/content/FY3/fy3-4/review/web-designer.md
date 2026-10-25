VERDICT: FAIL
CONTENT-HASH: 7acacc6c963e7a3a

## Blocking
1. content/FY3/fy3-4/sim.js:102-111 — at 390 and 360 px the chart reading ("up" branch, h > 4) is drawn over the y-axis and its tick labels. Measured and seen in screenshots (review/fy3-4-r2hi-360-h6-r1300-full.png): "178 kPa" sits on top of the tick "200". It happens for h = 4.5 to 8 m at every density, in both checkbox states (for example 1000 kg/m³, 5 m: "150 kPa" over "150"). The text is 12 px on screen but about 83 units wide in the 600-unit drawing, so left-above placement does not fit when px − 10 − width < CH.x0 (330). At 1280 px it is fine. — Use the up branch only when px − 10 − lw ≥ CH.x0 + 4; otherwise put the reading right of and below the dot (left-aligned at px + 8, baseline py + ts(16)), keeping it clear of the dashed p₀ line.
2. content/FY3/fy3-4/sim.js:105 and :124 — deep settings (h ≥ about 17.5 m at 390/360; h ≥ 18 at ρ = 1000, h ≥ 19 at 700) have the red dashed horizontal guide running through the reading ("278 kPa" struck through, see fy3-4-r2hi-360-h18-r1000-full.png). At h = 20 the reading sits inside the dot, the top dashed guide and the end of the blue line (fy3-4-r2hi-390-h20-r1000-full.png: "297 kPa" touched by the line end and the guide). Also at 1280 px at h = 20 the "297 kPa" and "196 kPa" readings touch the guide. — For h > about 16 put the reading below the line, right-aligned at px − 6 with the baseline at py + rise·width + ts(14), or give the text a background-coloured halo (stroke 3 px in the canvas background colour before fill) and keep it off the line.
3. content/FY3/fy3-4/sim.js:96 — "h (m)" is cut by the red vertical guide for h about 15.5 to 19.5 m at 360/390 px (guide x = X(h) falls inside the right-aligned label ending at x = 567). Seen in fy3-4-r2hi-390-h19-r1000-ov.png. — Draw the axis title after the guide with a halo, or move it below the axis next to the tick labels' row end, or hide it while the guide is within its width.

## Polish
1. sim.js:58-59 — at h = 0 and 1 m the depth bracket on the right of the pool shrinks to a tick, so "h" appears as "–h" or "Ih". Draw the "h" label only when h ≥ 2.
2. Template: text column is 31–34 characters at 390/360 px (61 at 1280); a template property, noted again.

## Checked
- Round-1 items fixed: lesson SVG labels "h (m)", "p = p₀ + ρgh", "ilmanpaine p₀" no longer overlap or cross the line at 1280 and 360 px (no text boxes overlap; minimum 11,5 px on screen at 360).
- Sim h = 0, both checkbox states, ρ 700/1000/1300, at 1280/390/360: the 101 kPa and 0 kPa readings are under the dashed line or above the h axis, grey p₀ label clear. OK.
- Sim h = 1, 2, 3, 4 m, both states, ρ 700/1000/1300, at 1280/390/360: no overlaps (hooked fillText and stroke, measured). OK.
- Sim canvas text 10,8 px on screen at 360/390 and 11 px at 1280. Over 50 states swept per width (h 0–20 in 0,5 m steps, three densities, both states).
- No horizontal page scroll at 1280, 390, 360 (scrollWidth equals viewport). Checkbox row 40 px high (the 24 px box is inside it).
- Controls do not overlap the canvas at any width.
