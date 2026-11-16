VERDICT: FAIL
CONTENT-HASH: 95f2bf8f83ac5346

## Blocking
- [Major] inquiry.json, Esimerkit solutions (Esimerkki "puomi" Sijoitus; ohjauspyörä Sijoitus), wide form (≥ 700 px) — the build joins the next "= …" row onto the continuation row, so the page shows "1,50 m · cos 40° = 117,72 N · 1,149 m" and "− 15 N · 0,19 m = 4,75 Nm − 2,85 Nm" as rows of their own: an equals sign outside the column and a row that reads as a false equation — on a laptop or projector the chain is misread, and the house rule (left = right on one row, each further = in one column) is broken — write the continuation row in the form join_wide knows (`\\ &\quad 1{,}50\,\text{m}\cdot\cos 40^\circ`, `\\ &\quad - 15\,\text{N}\cdot 0{,}19\,\text{m}`) so it joins the row before it, or fix `mathlayout.join_wide` (shared change) so a relation row never joins a row that continues a right side. The 390 px form is good.

## Polish
- [Minor] same chains at 390 px — the continuation "1,50 m · cos 40°" starts in the equals column, left of the factors above it; `&\quad` would also indent it.

## Checked
- own captures of preview/fy5-1.html at 390 and 1280 px, every details and feedback opened, one tile per block holding a display formula (/tmp/claude-0/-home-user-hellsla-github-io/ec927bcd-bc65-54ed-bfcf-2386619399a5/scratchpad/v/fy5-1-*.png); the standard set has no opened solutions at 390 px: fy5-1-lesson-390-1, -390-2, fy5-1-lesson-1280-1.
- Delta: Pohjatiedot feedback (F sin 30°), hint 3 and Sijoitus of both guided examples. Nothing clipped at 360/390 px (measured, no row past its box); punctuation sits inside the last row.
- Feedback formula and hint rows read well at both widths.

## Scores
illustrations – (not in delta) · typography 3 · Finnish 5 · accessibility 4
