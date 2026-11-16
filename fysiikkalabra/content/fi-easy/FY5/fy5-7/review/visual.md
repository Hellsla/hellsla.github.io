VERDICT: PASS
CONTENT-HASH: da0056510d600e1c

## Blocking

## Polish
- [Minor] inquiry.json:389 (Sijoitus, $x = 4{,}0\,\text{cm}\cdot$ | $\sin(\dots)$) — the trailing `·` sits tight against `cm` with no space before it, and the joins `0,9511= 3,804 cm` have uneven spacing around `=` (known join spacing) — collect with the PR's Polish.

## Checked
- Delta review, round 3 (Selkeä suomi): inquiry.json line 389, the worked solution's Sijoitus chain as consecutive inline formulas. lesson.md does not differ from main in this branch (formula names and figures approved by the teacher are already on main; not judged again).
- Opened fy5-7-inq-390-0.png: four rows, breaks only between whole quantities (`4,0 cm·` | `sin(2π · 0,50 Hz · 0,40 s)` | `= 4,0 cm · sin 1,257` | `= 4,0 cm · 0,9511 = 3,804 cm`); the `·` ends the first row, no row starts with a dot; nothing clipped.
- Opened fy5-7-inq-1280-0.png (in sheet-1280-a.png): two rows, break before `=`.
- Own Playwright captures (deviceScaleFactor 2) of preview/fi-easy/fy5-7.html?ratkaisut=1, every details box opened, at 390 and 1280 px, in /tmp/claude-0/-home-user-hellsla-github-io/ec927bcd-bc65-54ed-bfcf-2386619399a5/scratchpad/vis3-easy-7/.
- Page at both widths: scrollWidth = clientWidth, no KaTeX error nodes, no page errors.
- Punctuation after a display formula sits inside the formula box; no line starts with a bare comma, full stop or dot.

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 5
