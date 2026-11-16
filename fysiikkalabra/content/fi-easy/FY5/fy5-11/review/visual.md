VERDICT: PASS
CONTENT-HASH: 807038d1606df951

## Blocking

## Polish
- [Minor] inquiry.json:387 (Järkevyys) — the piece `+(180° − 2 · 55°)` starts with a binary `+` set tight against the bracket, and at 390 px it begins a row; readable — collect with the PR's Polish.

## Checked
- Delta review, round 3: inquiry.json line 387, `(180° − 2·35°) + (180° − 2·55°) = 110° + 70° = 180°` as consecutive inline formulas.
- Opened sheet-390-c.png (fy5-11-inq-390-0.png): three rows, breaks between whole brackets and before `=`; degree signs intact, full stop follows `180°`.
- Opened sheet-1280-c.png (fy5-11-inq-1280-0.png): break before `= 110° + 70° = 180°`.
- Own Playwright captures (deviceScaleFactor 2) of preview/fi-easy/fy5-11.html?ratkaisut=1, every details box opened, at 390 and 1280 px, in /tmp/claude-0/-home-user-hellsla-github-io/ec927bcd-bc65-54ed-bfcf-2386619399a5/scratchpad/vis3-easy-7/.
- Page at both widths: scrollWidth = clientWidth, no KaTeX error nodes, no page errors.
- Punctuation after a display formula sits inside the formula box; no line starts with a bare comma, full stop or dot.

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 5
