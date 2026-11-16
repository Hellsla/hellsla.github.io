VERDICT: PASS
CONTENT-HASH: 0123029cc461927a

## Blocking
None.

## Polish
- [Minor] fy4-s1-fbd (fig-3, 390 px), carried from the previous round: the label G_x sits against the right edge of the skier rectangle and is crowded by the dashed component arrow; move it a few px outside the box.
- [Minor] captures: `screenshot.py` captures a Sovella set in Finnish only, so the en page has no review/shots. The two changed places were therefore captured from the built en page (preview/en/FY4-sovella.html) for this review; a `--lang` option for Sovella sets would make the check routine.

## Checked
- Delta, round 2: the diff since the last PASS is two lines of solutions.md (187 and 490), each an inline division chain turned into an aligned block; numbers, units and order unchanged.
- Own captures of the built en page with every solution open, at 360, 390 and 1280 px: s1 d) Model answer ("0.02 m/s^2 : 9.786 m/s^2 ≈ 0.002.") and s3 c) Reasonableness ("7.86 m/s : 0.12 s ≈ 66 m/s^2,"). Opened at readable size: both places at 360 px and at 1280 px.
- 360 px: each chain is two rows in its formula box (the division, then "≈ result"), fully inside the card (formula 51–309 px in a 44–316 px column), "m/s^2" complete, nothing clipped or scrolled; page width 360 px, no horizontal overflow, no KaTeX error. 390 px the same by measurement (63–327 px in 46–344 px).
- 1280 px: each chain is one row in the reading column, the text around it undisturbed.
- The sentence punctuation is set inside the block (full stop after 0.002, comma after 66 m/s^2), and the sentence continues correctly after it ("almost 7g", "An uncertainty in the angle…"); decimal point and units upright with a thin space, division written with a colon.
- Finnish captures (current for the fi hash): contact sheets 2 and 3 for triage, page-390-28 at full size (the same s3 c) block in Finnish): the layout around the block survived.
- Figures are untouched by this diff and were not reopened; the previous round's judgement of them stands.

## Scores
illustrations 4 · typography 5 · Finnish 5 · accessibility 4
