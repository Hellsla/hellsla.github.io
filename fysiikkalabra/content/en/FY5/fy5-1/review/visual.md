VERDICT: PASS
CONTENT-HASH: db0ef52b0d54f6a0

## Blocking
(none)

## Polish
- [Minor] inquiry.json:343 and :359, phone rows — the row `= 12.0 kg · 9.81 m/s² ·` ends with the multiplication dot and the next row starts with `1.50 m`, while every other continuation row in FY5 starts with its operator — write `\\ &\quad \cdot 1.50\,\text{m}\cdot\cos 40^\circ`.
- [Minor] inquiry.json:418, phone rows — `= 4.75 Nm` and `− 2.85 Nm` are on two rows although the pair fits one row at 390 px — drop the `\quad` break there.

## Checked
- Round 3 delta (re-broken calculations only). Own Playwright captures of preview/en/fy5-1.html?ratkaisut=1, every details box open, at 390 and 1280 px, in /tmp/claude-0/-home-user-hellsla-github-io/ec927bcd-bc65-54ed-bfcf-2386619399a5/scratchpad/vis3-en-1/r3/: sheet-fy5-1-les-390-0.png, sheet-fy5-1-les-1280-0.png (opened as combo-fy5-1-0.png, combo-fy5-1-1.png).
- Every formula the branch changed in inquiry.json was located on the page and opened in the sheets; page scrollWidth equals the viewport with the boxes open, no KaTeX error, no script error.
- Hints and model solutions of the barrier and steering-wheel tasks: rows aligned at =, breaks between whole quantities, continuation indented, punctuation stays on the last row, nothing clipped; at 1280 px the rows join.

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 4
