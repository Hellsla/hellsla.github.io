VERDICT: PASS
CONTENT-HASH: 6d3b03bfad9f4e90

## Blocking
(none)

## Polish
- [Minor] inquiry.json, quiz prompt “A student calculated…” — uneven spacing at the joins of the inline pieces (known).

## Checked
- Round 3 delta (re-broken calculations only). Own Playwright captures of preview/en/fy5-5.html?ratkaisut=1, every details box open, at 390 and 1280 px, in /tmp/claude-0/-home-user-hellsla-github-io/ec927bcd-bc65-54ed-bfcf-2386619399a5/scratchpad/vis3-en-1/r3/: sheet-fy5-5-les-390-0…2.png, sheet-fy5-5-les-1280-0…1.png (opened as combo-fy5-5-1.png, combo-fy5-5-2.png).
- Every formula the branch changed in inquiry.json was located on the page and opened in the sheets; page scrollWidth equals the viewport with the boxes open, no KaTeX error, no script error.
- Quiz prompt with the student’s calculation as consecutive inline formulas: it wraps inside the sentence at both widths, the `·` ends the first line and no line starts with a bare dot, the fraction and `≈ 4400 m/s²` stay together, “What is wrong with the solution?” follows on the same line.

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 4
