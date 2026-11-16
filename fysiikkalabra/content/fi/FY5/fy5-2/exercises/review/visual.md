VERDICT: FAIL
CONTENT-HASH: a4886f2b4d181e2a

## Blocking
- [Major] exercises/solutions.md lines 142 (Kaava) and 177 (Järkevyys), wide form (≥ 700 px) — the first row is pushed right of the second ("mg (x − 5,0 cm)" over "−Mg (50,0 cm − x) = 0,"; "20,0 kg · 2,00 m" over "+60,0 kg · 3,333 m = 240 kg · m,") and the binary minus and plus are set tight as signs — misaligned rows; "−Mg" reads as a negative quantity — mark the continuation `\\ &\quad - M g\,(…)`, `\\ &\quad + 60{,}0\,\text{kg} \cdot …` so the wide form is one row, or fix `mathlayout.join_wide`/`align_equals` (shared).
- [Major] solutions.md line 205 (Sijoitus), wide form — "· 0,9063 = 1547 Nm" and "· 0,4226 = 124,4 Nm." stand as rows: "=" outside the column, the row reads as a false equation — `&\quad \cdot 0{,}9063` (joins the row before), or the same shared fix.

## Polish
- [Minor] line 205 at 390 px — rows starting with "·"; FY5-1 breaks after the dot. One form for the course.
- [Minor] after a lifted Kaava formula the word "josta" stands alone on its row before the solved form; acceptable, noted only.

## Checked
- own captures of preview/fy5-2.html at 390 and 1280 px, every details and feedback opened, one tile per block holding a display formula (/tmp/claude-0/-home-user-hellsla-github-io/ec927bcd-bc65-54ed-bfcf-2386619399a5/scratchpad/v/fy5-2-*.png); the standard set has no opened solutions at 390 px: fy5-2-ex-390-1 … -390-4, fy5-2-ex-1280-1 … -1280-3; review/shots/contact-7.png.
- Delta: all 21 lifted formulas (lines 47–217). Nothing clipped at 360/390 px; every 390 px form has its equals signs in one column; x_pp and T alone on the first row read well; punctuation inside the last row. Single-row formulas good at both widths.

## Scores
illustrations – (not in delta) · typography 2 · Finnish 5 · accessibility 4
