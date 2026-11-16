VERDICT: PASS
CONTENT-HASH: 933f1ee951dbae7a

## Blocking
(none)

## Polish
- [Minor] inquiry.json:333 — at the inline join `fλ= 2.0 Hz` the space before `=` is narrower than after it — known join spacing; collect with the PR's Polish.
- [Minor] inquiry.json:333 — the page splits the task text into two paragraphs inside the student's quotation (after “The wavelength is 0.50 m.”); the same on main, outside this diff — keep the quotation in one paragraph when the task is next edited.

## Checked
- Delta, round 3 (English): the student's quoted formula in Example 2, inquiry.json:333, now consecutive inline formulas.
- Opened fy5-10-les-v-ctx-390.png and fy5-10-les-v-ctx-1280.png: `v = fλ= 2.0 Hz · 0.50 m` | `= 1.0 m/s.”` wraps inside the sentence, the break before a relation, the closing quotation mark and `Where is the error?` follow on the same line; choices below intact, nothing clipped.
- - Own Playwright captures from the current preview/en pages (?ratkaisut=1, every details box open, hidden feedback and model boxes revealed) at 390 and 1280 px in /tmp/claude-0/-home-user-hellsla-github-io/ec927bcd-bc65-54ed-bfcf-2386619399a5/scratchpad/vis3-en-7/; measured in the same run: page scrollWidth equals the viewport, no KaTeX error, no formula past its box.

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 5
