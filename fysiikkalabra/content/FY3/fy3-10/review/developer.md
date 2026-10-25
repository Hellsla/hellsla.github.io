VERDICT: DONE

Checked lesson.md, solutions.md, exercises.json, answers.py, exit-ticket.json against the rules: 5 staged steps, SVG figures with aria-label in Ydinajatus and Kaava, paragraphs under 120 words, symbolic-first solutions, thin-space units, \textsf{l}, 5/4/3 exercises, answers.py matches every answer. No changes needed there; no answer changed.

sim.js: added a `lab(s, x, y, align)` helper that draws each canvas text with p.text and records {s, x0, y0, x1, y1} (from textWidth, textAscent, textDescent and alignment); every canvas text goes through it, and `window.simState.labels` carries the array every frame. Drawing, physics and controls are unchanged. Position fixes after test_sims.py reported clipping and overlaps:
- bottom texts ("osuma seinään", "V = …") baseline 394 -> 388 (clipped at the canvas bottom);
- ratio level moved down (yL = yT + 8 + ts(14)) so "mitattu/ennuste" no longer overlaps "0,8" and "1,2" at 360 px;
- bar area top BAR.y1 130 -> 165 so bar value labels clear the "p/pref" axis name.
test_sims.py fy3-10: PASS, labels checked at 360, 390, 1280 px.
