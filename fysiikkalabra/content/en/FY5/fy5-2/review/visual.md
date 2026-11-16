VERDICT: PASS
CONTENT-HASH: 1d94e72d6e2343e4

## Blocking
(none)

## Polish
- [Minor] inquiry.json:342, phone rows — short results such as `2.00 m − 1.50 m = 0.50 m` and `294.3 N · 2.00 m = 588.6 Nm` break before = although they fit one row at 390 px — let them stay on one row.

## Checked
- Round 3 delta (re-broken calculations only). Own Playwright captures of preview/en/fy5-2.html?ratkaisut=1, every details box open, at 390 and 1280 px, in /tmp/claude-0/-home-user-hellsla-github-io/ec927bcd-bc65-54ed-bfcf-2386619399a5/scratchpad/vis3-en-1/r3/: sheet-fy5-2-les-390-0.png, -390-1.png, sheet-fy5-2-les-1280-0.png (opened as combo-fy5-2-1.png, combo-fy5-2-2.png).
- Every formula the branch changed in inquiry.json was located on the page and opened in the sheets; page scrollWidth equals the viewport with the boxes open, no KaTeX error, no script error.
- Diving-board hint and model solution: `· 0.50 m`, `· 2.50 m`, `+ m_p g · 0.50 m` and `− 588.6 N` are indented continuation rows that start with their operator; aligned at =; nothing clipped; rows join at 1280 px.

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 4
