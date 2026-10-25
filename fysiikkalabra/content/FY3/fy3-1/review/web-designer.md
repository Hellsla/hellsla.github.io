VERDICT: PASS
CONTENT-HASH: 8fb367b0d6fd83e0

Round 3 (final). Page: preview/fy3-1.html. Measured with own Playwright script (Chromium, widths 1280/390/360/320, DPR 2 on phones). Hash identical before and after the review. Screenshots in review/ (project root): fy3-1-390.png, fy3-1-1280.png, fy3-1-top-320.png, fy3-1-sim-320-jup100.png and siblings. No blocking defects; findings below are all non-blocking polish.

## Checked and OK (measured)
- Text column at 1280: article p is 566 px wide at 18.4 px Fraunces; 71-76 characters per line (mean of full lines 71.4 / 72.3 / 76 / 72; one line max 80). Inside 60-75, at the upper edge. At 390: 41-43 chars/line (phone, expected).
- Horizontal overflow: documentElement.scrollWidth == clientWidth at 1280, 390, 360 and 320. The only elements past the viewport edge are KaTeX's hidden MathML nodes and the table's own scroller (see 2).
- Maths: 7 .katex nodes, 0 .katex-error, 0 visible katex exceeding the viewport at any width, 20.6 px.
- Table header "Taivaankappale / g pinnalla (N/kg)" and breadcrumb: text-transform none (no forced capitals), JetBrains Mono 12.8 px / 11.84 px, colour rgb(71,76,91). 
- Tap targets: no a/summary/select/input below 40 px in either dimension at any width (breadcrumb links, nav, footer, skip link, summaries all >= 40 px). Select 40 px high, range input 40 px high.
- Sim layout: readout, controls and note sit below the canvas (gap 10 px to readout, nothing overlaps the canvas) at all widths; labels stack full width at <= 390.
- In-canvas text rendered size (glyph px x canvas scale): 1280 min 10.5; 390 min 10.8 (labels 11.9-13.0, title 12.9, subtitle 10.8); 360 min 10.8; 320 min 10.1 for the default state (see 3 for the exception).
- Mass-label block: "100 kg" spans x 63-157 of 600 at 320 (inside canvas, block grows to label width). Bar-chart title spans x 245-595 of 600 at all widths (shrunk to fit, not clipped). Value labels do not collide with neighbours (4+ canvas px gaps).
- Weight arrow at 100 kg on Jupiter: arrow tip y = 270+6+110 = 386 of 400, G label at y 336; inside the canvas (confirmed in fy3-1-sim-320-jup100.png). Arrow also verified for 1 kg, 10 kg Maa, 100 kg Kuu: proportional, min 3 px.
- Exercises: three <details class="level">, closed by default, "▸" marker (turns into "▾" when open), clicking opens. Exit ticket: skip link "Siirry lähtölippuun" scrolls #exit to y = 94 px below viewport top at 390. Exit ticket answers are collapsible with markers too.
- Contrast (text): every text element measured at 390 has >= 5:1 against its background (ink 14,23,30 on cream; crumbs 71,76,91; accent-deep 20,83,45). Canvas text 60,60,60 on 250: 10.6:1; title 26,77,46: 9.4:1. All pass AA.
- SVG figure label size: 20 px in a 600 viewBox -> rendered 20.3 px at 1280, 11.9 px at 390, 10.9 px at 360, 9.6 px at 320.

## Findings (non-blocking)
1. Bar fill contrast vs background (non-text 3:1, WCAG 1.4.11). Bars are drawn at alpha 200/255 when not selected. Blended on the 250 canvas: Kuu 3.22, Maa 3.18, Mars 3.02, Jupiter 2.64 (full opacity Jupiter 3.61). The default view (Maa selected) therefore shows a Jupiter bar at 2.64:1. Mitigated because every bar is labelled with name and value, so no information is colour-only. Proposal (sim.js, bar fill): use full alpha and mark the selected body with an outline instead:
   `p.fill(COLORS[i][0], COLORS[i][1], COLORS[i][2]); if (i === idx) { p.stroke(30); p.strokeWeight(2); } else p.noStroke();`
   and darken Jupiter to `[160, 105, 35]` (about 4.4:1 on 250).
2. Table header clipped at 320 px: the table scrolls inside itself (scrollWidth 305 > clientWidth 286) and the last ")" of "g pinnalla (N/kg)" touches the right edge; at 390 and wider it fits (356/356). Not overflow of the page. Proposal (site.css): `th{font-size:.74rem;letter-spacing:0} @media (max-width:360px){th,td{padding-inline:.6rem}}` or shorten the header to "g (N/kg)" in lesson.md.
3. At 320 px one value label drops to 9.3 px rendered ("2480 N" at 100 kg Jupiter, also "162 N" style labels on large masses): the shrink rule `if (p.textWidth(vt) > bw + 12) p.textSize(ts(12) * (bw + 12) / p.textWidth(vt))` fires for the widest label while the other labels stay at 10.2-11.3 px. Proposal: floor the shrunk size, `p.textSize(Math.max(ts(12) * (bw + 12) / p.textWidth(vt), 10 * k))`, and widen the label slot by reducing the bar gap from 16 to 12 (`bw = BARS.w / 4 - 12`).
4. SVG figure labels fall below 10 px at 320 (9.6 px) and are 10.9 px at 360. Proposal (lesson.md inline SVG): raise font-size from 20 to 24 and shorten the second note to "voiman mukaan" at x=302 (check it still fits 600 wide; it ends near x=500 at 20 px, about 590 at 24 px), or give the svg `style="min-width:340px"` inside the existing scroll-free layout.
5. Number format inconsistency in the readout versus the chart and table: readout shows "g = 24,80 N/kg" and "G = m · g = 2480,0 N" while the table and bar labels show 24,8 and 2480 N. Proposal (sim.js): `fi(g, g < 10 ? 2 : 1)` and `fi(G, G < 100 ? 1 : 0)` to match the bar labels.
6. Cosmetic, 320 px: bar category labels "Maa" and "Jupiter" nearly touch (gap about 5 canvas px). Proposal: shorten nothing, but with the gap change in 3 (bw = w/4 - 12) the label slots widen; or draw category names at ts(11).
