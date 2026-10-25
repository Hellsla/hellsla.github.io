VERDICT: PASS
CONTENT-HASH: fc5375c46d696bd5

Round 2, web-designer. Page: preview/fy3-1.html. Hash checked before and after the review: unchanged (fc5375c46d696bd5). Measured with Playwright (Chromium 1243) at 1280 and 390 px, plus 320/360/375/412 for the canvas.

Passed checks (measured)
- Text column at 1280: 608 px wide, 17 px type, real lines hold 70, 70, 72, 72, 73 characters (target 60-75). At 390: 358 px, 34-47 characters per line.
- Horizontal overflow: scrollWidth = clientWidth = 390 (and 1280). The only elements with right edge > 390 are the visually hidden KaTeX MathML nodes (clip 1 px), not visible content. 0 `.katex-error`; display and inline maths fit (widest inline formula 352 px in 358 px column, wraps after the relation sign).
- g table: 2 columns, 358 px wide at 390, scrollWidth 356, no sideways scroll, 17 px cells, header 12.8 px.
- Sim controls at 390: select 324x40 px at y=4276, slider 324x40 px at y=4348, readout y=4171-4243; canvas ends y=4161. No overlap with the canvas (10 px gap) or each other (select and slider labels stack, 8 px apart). At 1280 the two are side by side, 275x40 each.
- In-canvas text rendered at 390 (canvas scaled 0.54, k=1.85): 11 px text draws at 10.8 px, 12 px at 11.9 px, 13 px at 13.0 px. At 320-412 px the range stays 10.8-13.2 px, so the >= 10 px target holds.
- "m kg" label inside its block at 390: smallest mass "1 kg" 45 px in a 67 px block; largest "100 kg" 72 px in a 76 px block (stroke included). Verified in screenshots at m = 1, 37, 41, 100 and all four bodies.
- Bar value labels at 390: smallest gap between neighbouring value labels is 10 canvas px (about 5 CSS px) at m = 41; name labels gap 20 px. No collisions.
- SVG figure at 390: scale 0.597, its 20 px labels render at 11.9 px. At 1280 they render at 20.3 px.
- Exercises: `<details class="level">` and the answer details are 40 px tall, `list-style: disclosure-closed` shows the triangle marker; exit ticket anchor `#exit` exists and "Siirry lähtölippuun" link goes to it. Exit ticket sits at the page end with three collapsible answers (40 px each).
- Contrast, DOM text: lowest of all text styles is 7.13:1 (table header), body 16:1. Canvas text: dark grey (60) on 250 = 10.6:1, green title 9.4:1, red G 5.3:1, block label 11:1.
- Bars, non-text 3:1: selected bars Kuu 4.9, Mars 4.3, Maa 4.7, Jupiter 3.6 (all >= 3). Unselected bars (alpha 150 of 255) are 2.0-2.3:1, below 3:1 for the shape itself, but every bar has a text value ("162 N") and a name under the axis, and the selected body is stated in the DOM readout, so no information depends on colour. Acceptable, see finding 5.
- Tap targets >= 40 px high everywhere. Only the breadcrumb link "FY3" is 33 px wide (40 px high).

Findings (none blocking at 390 px; applies to narrower phones and small polish)

1. Sim canvas breaks below about 375 px width (WARN, template/sim). The canvas text size is scaled by k = 600/clientWidth, but the fixed anchors are not. Measured:
   - 360 px: block label "100 kg" is 81 px wide in a 76 px block (overflows the block, seen in screenshot), and the title "Sama massa, paino eri paikoissa" spans x = 222-618 in a 600 px canvas (right end clipped, "paikoiss").
   - 375 px: label 75 px in a 76 px block (no margin), title spans 237-603 (3 px clipped).
   - 320 px: label 93 px vs block 87 px, title 193-647, neighbouring bar value labels overlap by 7.5 canvas px.
   At 390 px the label has only 4 px of slack and the title ends at x = 596 of 600. Proposal in sim.js:
   ```js
   const bs = Math.max(36 + 40 * Math.sqrt(m / 100), p.textWidth(`${m} kg`) + 16);   // after p.textSize(ts(13))
   // title: shrink to fit
   p.textSize(ts(13)); let t = 'Sama massa, paino eri paikoissa';
   if (p.textWidth(t) > BARS.w + 40) p.textSize(ts(13) * (BARS.w + 40) / p.textWidth(t));
   ```
   or shorten the title to "Paino eri paikoissa" and keep the explanation in the DOM note (that text is already in `.note`).

2. Uppercase transform corrupts units and the formula (cosmetic, site.css). `th{text-transform:uppercase}` renders the table header "g pinnalla (N/kg)" as "G PINNALLA (N/KG)" (wrong unit case, 12.8 px), and `.crumbs` shows "PAINO G = MG". Proposal:
   ```css
   th{text-transform:none;letter-spacing:.02em}
   .crumbs{text-transform:none}
   ```
   or only uppercase the first word via a class. Low effort, lesson content untouched.

3. Block label has no visual margin at the largest mass (390 px: text 72 px, inner block width about 70 px after 3 px stroke). Same fix as 1 (+16 px padding in `bs`).

4. Breadcrumb link "FY3" is 33 x 40 px (width below 40). Proposal: `.crumbs a{display:inline-block;min-width:40px;text-align:center}` or `padding:0 .4rem`.

5. Unselected bars are 2.0-2.3:1 against the canvas (3:1 wanted for graphical objects where the shape carries meaning). Values and names are printed on each bar, so this is not a failure. Proposal: draw the unselected bars at alpha 200 (about 3.0:1) or add a 2 px stroke in the body colour:
   ```js
   p.fill(c[0], c[1], c[2], i === idx ? 255 : 200);
   if (i !== idx) { p.stroke(c[0], c[1], c[2]); p.strokeWeight(1.5); }
   ```
   and mark the chosen bar with a bold name label as a second cue.

6. Minimum-mass bars are 2 px high (Kuu 1 kg: 0.14 px proportional, drawn 2 px), which look like a line on the axis. This is intended per sim-spec; no change needed. Optional: draw bars under 4 px with a 1 px outline so they read as bars.
