VERDICT: FAIL

Scope: preview/fy3-2.html built from templates/lesson.html + templates/site.css (no files edited). Measured with Playwright/Chromium at 390x844 and 1280x900. Screenshots: review/fy3-2-390.png, review/fy3-2-1280.png, review/fy3-2-390-sim.png, review/fy3-2-390-exercises-open.png.

The only FAIL cause is finding 1 (in-canvas sim text unreadable on a phone). Nothing else is broken: no horizontal overflow, no overlap, maths fits.

## Passes (measured)
- Horizontal overflow at 390 px: documentElement scrollWidth 390 = clientWidth 390; body 390. KaTeX display equations: scrollWidth 358 = clientWidth 358 (no inner scroll needed). No visible inline KaTeX sticks out past the 16 px gutter. (Elements reported past 390 are only KaTeX's visually hidden MathML copy.)
- Sim controls vs canvas: canvas bottom 4272 px, controls top 4280 px (8 px gap) at 390; 3211/3219 at 1280. No overlap. Controls block is 205 px tall at 390 (sliders stack).
- Exercises collapsible by level: 3 `details.level`, closed by default; 15 nested `details.answer`. Collapsed, exit ticket starts 219 px below the exercises heading (4517 -> 4736 at 390; 3314 -> 3533 at 1280), so it is visible in the same screen. With Taso 1 opened it moves to 5464 (+728 px at 390), all open 6886 (+2150 px). Acceptable because default is closed, but see finding 5.
- Contrast (WCAG AA, 4.5:1 text): #2f6f9f on #fff = 5.39; on #f3f7fa (blockquote) = 5.00; #666 on #fff = 5.74; #222 on #f3f7fa = 14.8. In-canvas grey (90) on 250 = 6.6, canvas blue on 250 = 5.17, red arrow on 250 = 5.31. All pass.
- Range inputs: 176 x 40 px (min-height holds). All 18 `summary` elements: 40 px high (358 px / 318 px wide at 390). "Vedä" button 77 x 63 px.
- Maths at 390: all three display equations render fully inside the 358 px column; the SVG figure scales to 358 x 179 with its labels legible (viewBox text 16 px * 0.6 = ~9.6 px, borderline, see finding 6).

## Findings

1. FAIL: in-canvas text unreadable on phone. Canvas is fixed 600x400 and scaled by CSS to 358x239 at 390 px (scale 0.597). Resulting rendered text sizes: readout "W = F·s", "P = W/t" 16 px -> 9.5 px; "Tehty työ..." 13 px -> 7.8 px; axis/metre labels and "0 J / 600 J" 11-12 px -> 6.6-7.2 px; "W = pinta-ala" 13 px -> 7.8 px. The two key outputs (W and P) exist only in the canvas, so a phone user cannot read them without zooming. Also p5 wraps the font string in quotes (ctx.font is `12px "system-ui, sans-serif"`, verified), which is an invalid family, so canvas text falls back to serif (visible in fy3-2-390-sim.png).
   Proposal (sim.js is the human/producer's file; not applied): move W and P into the DOM and keep canvas text decorative, and fix the font:
   ```js
   // setup(), after createCanvas
   const readout = p.createDiv('').parent('sim-root').class('readout'); // place before controls
   // draw(): readout.html(`W = F · s = ${fi(W,0)} J<br>P = W / t = ${fi(P,1)} W<br><small>Tehty työ: ${fi(Wdone,0)} J</small>`);
   p.textFont('Arial'); // instead of 'system-ui, sans-serif' (p5 quotes the string)
   // optional: scale canvas text so it is >= 11 px on screen
   const k = Math.max(1, 600 / document.getElementById('sim-root').clientWidth);
   p.textSize(11 * k);
   ```
   ```css
   #sim-root .readout{font-size:1rem;line-height:1.5;margin:.5rem 0;font-variant-numeric:tabular-nums}
   ```
   Drop the three readout lines at y=30/54/78 from the canvas afterwards, which also frees the top-left area.

2. Text column too wide on desktop. Paragraphs are 736 px wide at 1280 (`body{max-width:46rem}`), measured 76-87 characters per full line (mean 82, over 4 paragraphs). Target is 60-75. At 390 px it is 27-44 chars (mean ~37): normal for a phone, not a fault.
   ```css
   body{max-width:40rem}            /* 640 px content -> ~71 chars/line at 18 px */
   ```
   The 600 px canvas and the 600 px-viewBox SVG still fit. Optionally `body{font-size:clamp(17px,1.1vw + 14px,19px)}` does not change the measure and is not needed.

3. Nav links are too small to tap. "Fysiikkalabra" 88 x 17 px, "FY3" 27 x 17 px (requirement 40 px). They sit side by side separated by only " › ".
   ```css
   nav a{display:inline-block;padding:12px 8px;margin:-12px -8px}  /* 41 px target, layout unchanged */
   ```
   (or `nav{display:flex;align-items:center;gap:.25rem}` with `nav a{min-height:40px;display:inline-flex;align-items:center;padding:0 .5rem}`).

4. Button border below 3:1 non-text contrast. `#sim-root button{border:1px solid #999}` on white is 2.85:1 (WCAG 1.4.11 needs 3:1).
   ```css
   #sim-root button{border-color:#767676}   /* 4.54:1 */
   ```

5. Collapsed `details.level` and `details.answer` show no disclosure marker. `summary{display:flex}` removes the default triangle, so "Taso 1/2/3" look like plain headings (see fy3-2-390.png, the three bare lines under "Tehtävät"). Students may not realise they open. There is also no count of tasks.
   ```css
   summary::before{content:"▸";display:inline-block;width:1.2em;color:#2f6f9f;flex:none}
   details[open]>summary::before{content:"▾"}
   details.level>summary{border-bottom:1px solid #d5dde3}
   ```
   and in the template, e.g. `<summary>Taso 1 <span class="count">5 tehtävää</span></summary>` (the `.count` class already exists in site.css but is unused). To keep the exit ticket reachable when a level is open, consider a link `<a href="#exit">Siirry lähtölippuun</a>` after the exercises heading, or placing `#exit` before `#exercises` (+728 px at 390 per opened level).

6. Sim sliders are only 176 px wide on a 358 px column (label min-width 11rem, flex-wrap). Short sliders make fine values (0.5 steps over 1-20) hard to hit with a thumb. Same row: the "Vedä" button stretches to 63 px height beside the third slider.
   ```css
   #sim-root label{flex:1 1 11rem}                 /* sliders grow to full width when wrapped */
   #sim-root .controls{align-items:end}
   #sim-root button{align-self:end}
   ```

7. Minor: worked-example SVG labels render at ~9.6 px at 390 px (16 px text in a 600-unit viewBox scaled by 0.6). Proposal: set `font-size:20px` in the SVG source in lesson.md (about 12 px on phone, 24 px at 1280 where the figure is 736 px wide), or cap the figure with `svg{max-width:36rem}`.

8. Informational: `git status` shows `tests/sims/fy3-2.json` modified (not by this reviewer). This run only added this report plus review/fy3-2-390-sim.png and review/fy3-2-390-exercises-open.png beside the two standard screenshots.
