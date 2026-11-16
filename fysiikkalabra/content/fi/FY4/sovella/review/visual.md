VERDICT: PASS
CONTENT-HASH: e8cec9743308859a

## Blocking
- none

## Polish
- [Minor] solutions.md fy4-s1 b) Mallivastaus and fy4-s3 e) Mallivastaus — the bullets render as plain paragraphs starting with a literal "- " (no list markup inside the card; seen again in stage-fy4-s3-390-7) — write them as a real list or drop the hyphens.
- [Minor] fy4-s1-fbd — the $\overline{G}_x$ label touches the edge of the skier rectangle, and the right panel's labels are small at 390 px — move the label clear of the box edge; consider stacking the two panels on a phone.
- [Minor] fy4-s1-drag (seen in page-1280-6) — the orange curve continues as a solid line past the last point ($9\,\text{m/s}$) to about $10\,\text{m/s}$; only the part toward $v = 0$ is dashed — dash the extrapolated end too, or stop at the last point.
- [Minor] fy4-s1-graph — the circled read-off points at $t = 0$ and $t = 8\,\text{s}$ are not explained in the figure or its Kuvaaja line — say in the text that the rings mark the read-off points.

## Checked
- Delta, round 2: since the PASS for 63d1877e57a7774f only two chains in solutions.md changed (lines 187 and 490, now `aligned` blocks); the diff against the previous commit confirms nothing else in tasks.json or solutions.md differs. Captures are current for this hash (stamp.txt).
- stage-fy4-s1-390-7 — s1 d) Mallivastaus at 390 px: $0{,}02\,\text{m/s}^2 : 9{,}786\,\text{m/s}^2$ on the first row, $\approx 0{,}002.$ on the second, both left-aligned inside the formula panel, nothing clipped, the sentence's full stop stays with the result, the text continues cleanly below.
- stage-fy4-s3-390-6 — s3 c) Järkevyys at 390 px: $7{,}86\,\text{m/s} : 0{,}12\,\text{s}$ and $\approx 66\,\text{m/s}^2$ in two rows, units and exponent whole, "eli lähes $7g$" continues the sentence under the block.
- page-1280-6 — s1 d) at 1280 px: the same chain on one row in the reading column, so the break appears only on a phone; the e) part and the drag graph below are undisturbed.
- stage-fy4-s1-390-9 and -10, stage-fy4-s3-390-7 and -8 — the surroundings (Hyväksytään myös, Yleisiä virheitä, rubric, s3 d) and e)): layout intact, no overflow.
- Not reopened: the figures and the remaining captures, judged in the full review of the previous hash; no figure changed.

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
