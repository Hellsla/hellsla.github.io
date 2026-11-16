VERDICT: PASS
CONTENT-HASH: 3a8f9887abba8d2c

## Blocking
(none)

## Polish
- [Minor] inquiry.json:389 — at the inline joins the multiplication dot sits tight against the unit (`4.0 cm·` at the row end) and `= 3.804 cm` follows `0.9511` with uneven space — known join spacing; collect with the PR's Polish.

## Checked
- Delta, round 3 (English): the substitution of the sine example, inquiry.json:389, now consecutive inline formulas.
- Opened fy5-7-les-sin-0-390.png and fy5-7-les-sin-0-1280.png: at 390 px the rows read `x = 4.0 cm·` | `sin(2π · 0.50 Hz · 0.40 s)` | `= 4.0 cm · sin 1.257` | `= 4.0 cm · 0.9511 = 3.804 cm`; the dot ends the first piece, no row starts with a bare dot, every break is between whole quantities; at 1280 px two rows, nothing clipped. Answer box below intact.
- - Own Playwright captures from the current preview/en pages (?ratkaisut=1, every details box open, hidden feedback and model boxes revealed) at 390 and 1280 px in /tmp/claude-0/-home-user-hellsla-github-io/ec927bcd-bc65-54ed-bfcf-2386619399a5/scratchpad/vis3-en-7/; measured in the same run: page scrollWidth equals the viewport, no KaTeX error, no formula past its box.

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 5
