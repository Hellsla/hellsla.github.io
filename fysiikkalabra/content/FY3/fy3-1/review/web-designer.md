VERDICT: PASS
CONTENT-HASH: 28956a3df07f9f05

Measured with Playwright (Chromium) on preview/fy3-1.html at 1280 and 390 px. No breakage: no horizontal overflow, no overlap, maths and sim readable. The findings below are polish; none was applied.
Note on hash: it moved da9ba5eb24ac7a54 -> 3444d0df4b2f6a39 -> 28956a3df07f9f05 during the review only because tests/sims/fy3-1.json was edited by another agent. lesson.md, exercises.json, exit-ticket.json, meta.json and sim.js have unchanged mtimes, and preview/fy3-1-sim.js is byte-identical to sim.js, so the measurements still apply.

1. Sim select is 19 px tall (target >= 40 px) and uses the browser default font (~13 px). The slider is 40 px, so the two controls are uneven. Under 16 px, iOS also zooms the page when the select is focused. Proposal for site.css (not applied):
   #sim-root select{min-height:40px;font:inherit;font-size:1rem;padding:0 .6rem;border:1px solid var(--line);border-radius:8px;background:var(--surface);color:var(--ink)}

2. In-canvas block label overflows its block when the canvas is scaled (390 px: scale 0.54, k = 1.85, ts(13) = 24 canvas px). The block is 36 + 40*sqrt(m/100) = 40 canvas px at 1 kg and 48.6 px at 10 kg, while "1 kg"/"10 kg" at 24 px is about 40-52 px wide. The text touches or crosses the edges (seen in the 390 px canvas at m = 1 and m = 10). At 1280 (k = 1.05) it fits. Proposal for sim.js (not applied):
   const bs = Math.max(36 + 40 * Math.sqrt(m / 100), ts(13) * 2.8);   // block never narrower than its label
   (at k = 1.85 this gives 67 canvas px; the spring bottom stays below y = 290 of 400, so there is no clipping)

3. In-canvas text size at 390 px is fine: the ts() scaling gives 13 px labels (title, "G", block label) and 12 px axis and value labels after scaling (24 and 22 canvas px x 0.54). Target >= 10 px met. Canvas 324 x 216 px; the readout starts 9.6 px below the canvas bottom and the controls 28 px below the readout, so nothing overlaps. Readout, "Massa m" label and note are DOM text at 16 px or more.

4. Bar colours in the canvas are weak as graphics (WCAG 1.4.11, need 3:1 against the 250 grey background): Jupiter 2.53:1, Kuu 2.83:1, Mars 4.27:1, Maa 4.66:1; non-selected bars at alpha 90 are about 1.3:1. Every bar carries a text value and a name, so information is not lost; it is low priority. Proposal for sim.js COLORS (not applied): [[110,110,110],[190,90,60],[47,120,160],[176,120,50]] (Jupiter ~3.6:1, Kuu ~5:1) and raise the non-selected alpha from 90 to 140.

5. Inline SVG (spring scale figure) at 390 px: scale 0.572, labels render at 11.4 px (19.8 px at 1280). It passes (>= 10 px), but is small for the labelled text. Optional lesson.md SVG change (not applied): font-size:24px on the style attribute (13.7 px at 390; the "voiman mukaan" text ends at x ~ 440 of 600, so it still fits).

6. Cosmetic, site.css: at 390 and 1280 the g table is narrower than its bordered white box (content 245 px against 356 px box at 390). The beige header row stops short and the box looks half empty. The table itself fits and does not need to scroll (scrollWidth 356 = clientWidth 356). Proposal (not applied): table thead,table tbody{display:table;width:100%;table-layout:auto}  (keeps the box scroll behaviour for wider tables).

Checked and passing:
- Text column at 1280: paragraph width 566 px at 18.4 px; measured line lengths 76, 68, 73 characters (target 60-75; one line at 76 is a trivial excess). At 390: 39-45 characters per line.
- Horizontal overflow at 390: scrollWidth 390 = clientWidth 390, also with every exercise level and one answer opened (390). At 1280: 1280 = 1280. Only the hidden KaTeX MathML elements extend beyond the viewport, which is expected (visually clipped).
- Maths: 0 KaTeX errors; display formula in a scrollable box (356/356 at 390), inline maths 20.6 px, long example lines wrap normally on a phone.
- Exercises: three <details class="level"> collapsed by default with a visible marker (▸, ▾ when open), each summary 40 px tall and full width, with the count ("5 tehtävää"). Answer summaries 40 px tall. "Siirry lähtölippuun" skip link (40 px tall) and #exit section reachable; the exit ticket answers collapsed with 40 px summaries.
- Tap targets: all 8 links 40 px tall; the narrowest is "FY3" in the breadcrumb at 33 px wide but 40 px tall (acceptable); the slider is 40 px.
- Contrast (WCAG AA): ink/bg 16.2:1, ink-2/bg 7.7:1, ink-2 on bg-tint (table header) 7.1:1, accent-deep on surface 9.1:1, white on pill 9.1:1, canvas text (60 on 250) 10.6:1, canvas title green 9.4:1, red "G" 5.3:1. All above 4.5:1.
