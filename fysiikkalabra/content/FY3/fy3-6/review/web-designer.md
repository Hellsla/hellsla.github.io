VERDICT: FAIL
CONTENT-HASH: dc46dfd6cdc26576

## Blocking
- sim.js:28-39 — On a phone the Upota button is about 950 px below the top of the canvas (390x844: canvas top 3307, button bottom 4259; same at 360x640) because the DOM order is canvas, readout (325 px), five controls. When the student taps Upota the canvas is 400 px above the viewport, so embed's IntersectionObserver has paused the sketch and the student sees nothing. After scrolling up, the animation has jumped ahead (simState.t = 4.9 s, measured 0.6 s after scrolling back; it was 0 s after 3.5 s of waiting). The central interaction fails on a phone. — Fix: create the controls before the readout, with Upota first, so canvas + button fit in one 640 px screen; keep the T line and the long readout below. Also clamp the step in line 55, `tAnim += Math.min(p.deltaTime, 100) / 1000`, so a resume after a pause cannot skip the motion.

## Polish
- sim.js:106,94 — at 360 and 390 px the label "kappale 100,0 °C" is crossed by the hanging string (x = 135, y from 76). Fix: start the string below the label (y >= ts(18)+ts(19)+6) or shorten the label.
- sim.js:121 — with a cold body (0 °C aluminium, water 20 °C, Teq 17,5 close to the top of the axis) the "T" label at 360 px touches the legend word "kappale". Fix: move the legend left or put the T label under the line when Teq is within 15 % of the top.
- sim.js:34-38 — at 1280 px the slider labels wrap with the value alone on the second line ("0,30 / kg", "T_k = 0,0 / °C"). Fix: make the labels nowrap, or flex-basis about 14rem.
- sim.js:57-79 — the readout is 325 px tall at 390 px (8 lines) and pushes the controls out of reach. Fix: shorten it; drop the "Lämpömittarit nyt" line, which the canvas already shows.

## Checked
- Build and lint are clean; 0 console errors; no horizontal scroll at 1280, 390 or 360 px, including with the solutions open (pageOverflow 0).
- Sim, cold (0 °C Al) and hot (100 °C Cu), before, at 1.5 s and after the full 10 s with a tall viewport: ends at T = 17,5 and 24,6 °C, both curves meet the dashed line, water and body colours change; no clipped text.
- Canvas text is rendered at about 11-13 px at 390 and 360 (sim.js scales it); the T label does not clip at the right edge (25 °C, 70 °C, 17,5 °C).
- Controls: sliders, select and Upota are 40 px tall; Upota is 92 px wide; controls do not overlap the canvas.
- Table: 184 px wide, rows at least 34 px tall, 17 px text, no overflow at 360.
- Bar chart SVG: scales to the column (358 and 328 px); smallest text 11,9 and 10,9 px; labels do not collide; contrast is fine (currentColor on the page background).
- Solutions: all 3 open at 390 and 360, 284-314 px wide; summary 40 px tall; no KaTeX display overflow; answer field 120x40 and Tarkista 87x40.
- Text column width is the site-wide template, not lesson-specific (not judged).
- Screenshots are in review/fy3-6-wd-*.png (git-ignored).
