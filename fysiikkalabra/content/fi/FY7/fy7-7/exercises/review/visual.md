VERDICT: FAIL
CONTENT-HASH: c2299a6720da2db8

## Blocking
- [Major] figure:fy7-7/pick-u50-t25, pick-u50-t40, pick-u71-t25, pick-u71-t40 — the y-axis label "e (V)" is placed above the viewBox (foreignObject y=-16.5, axes top at y=40) and is cut in half by the SVG edge in all four option figures, at 390 px (2x render checked) — the quantity and unit of the vertical axis are essential and the label reads as a smudge — fix: raise the top of Axes (e.g. corner y=60, shift the figure or enlarge the viewBox height) so the label sits inside the viewBox.

## Polish
- [Minor] L1-09 — options display as B, A, D, C (shuffled with their letters); solution and feedback refer to letters, so read in order the letters jump. Keep letters in display order or name the options by their content.
- [Minor] pick figures — the y tick "−10" is not labelled though the range is stated as −10 V…10 V; the tick fonts are about 11 px at 390 px.
- [Minor] solutions.md L1-09 — long closing paragraph packs four options in one block; split per option.

## Checked
- Render of fy7-7-L1-09 at 390 px: four option figures (same axes, violet sine, B correct 7,1 V and 25 ms), all feedback, solution with fractions: no horizontal overflow (path elements beyond the box are clipped by the SVG); 2x close-up of one figure showed the clipped y label.
- Text only: 2x2 design (peak 5,0 vs 7,1 V, period 25 vs 40 ms) catches the effective-value and f-as-ms mistakes; correct feedback gives the values, not a separate reason stage; figure descriptions are full; L3-03 paragraph split read from diff.

## Scores
illustrations 3 · typography 4 · Finnish 5 · accessibility 4
