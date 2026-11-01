VERDICT: FAIL
CONTENT-HASH: f83f09187e7e636a

## Blocking
- [Major] inquiry.json siirto and check-2 solutions, the drawn force diagrams (`.fig.fbd`), open-tarkista-1280-2/3: the diagrams are drawn at about four times the house scale. Measured in the browser, the check-2 diagram is 569 × 961 px at 1280 px, taller than the 900 px screen, and on a phone it is 298 × 499 px for two arrows. Its labels are about 60 px tall. The cause: `scripts/figlib.py` writes an inline `style="max-width:100%"`, and an inline style beats `site.css` `.fig.fbd svg{max-width:min(100%,24rem)}`. — Why it matters: $\overline{G}$ and $\overline{F}_\text{v}$ are never on screen together, yet their equal length is the point of the step, and the solution reads as broken. — Fix: let the 24rem cap win, either `!important` in site.css or no inline max-width on fbdspec output. This is a template fix, so check the other chapters too.

## Polish
- [Minor] inquiry.json pred-1 prompt: "$40$ sekunnin aikana" breaks the standing rule (number and unit as one formula). Fix: "$40\,\text{s}$:n aikana".
- [Minor] lesson.md Esimerkki, Sijoitus: `9{,}81\,\tfrac{\text{m}}{\text{s}^2}` renders as a tiny stacked fraction (example-390-2), unlike $\text{m/s}^2$ everywhere else. Fix: `9{,}81\,\text{m/s}^2`.
- [Minor] lesson.md "Putoava ja nouseva kappale": the two equations of motion appear only inline, and at 390 px "$mg -$ / $F_\text{v} = ma$" breaks across lines (stage-selita-390-3). Fix: set them as a two-row display (falling, positive down; rising, positive up) after the paragraph.
- [Minor] valitse-a…d option figures at 390 px (stage-sovella-390-3): the $\overline{v}$ label touches the dashed divider. Fix: move the label or the divider about 10 px apart.
- [Minor] fig vt: the $60\,\text{kg}$ curve's copper `#b8622d` is close to the acceleration orange. Fix: a colour further from orange, e.g. muted ink.

## Checked
- Contact sheets 1–7 for triage; top-390, intro/theory-1280-1…3 opened at full size.
- fig-2…5-390 (pudotus, vt, ylos, varjo): colours, arrow ratios and labels checked. fig-1 is the hero. fig-7…10 are the option figures.
- example-390-1/2, with the esimerkki figure cropped and enlarged.
- sim-390 and sim-1280; stage-ennusta-390-1, stage-selita-390-3, stage-sovella-390-3, exp-1/exp-3-390.
- open-tarkista-1280-1…3. I measured the force-diagram sizes in a browser at 390 and 1280 px.
- exp-1-390 showed the canvas with giant overlapping KaTeX labels. Four fresh captures rendered correctly, so this was a capture race (screenshot.py waits 1500 ms), not a content defect. exp-3's empty "Käytössä:" is from the box being forced open.

## Scores
illustrations 4 · typography 4 · Finnish 5 · accessibility 3
