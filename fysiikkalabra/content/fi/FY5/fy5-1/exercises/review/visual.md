VERDICT: FAIL
CONTENT-HASH: ba02a105b1db547f

## Blocking
- [Major] exercises/solutions.md line 119 (Sijoitus, ΣM), wide form (≥ 700 px) — shown as "ΣM = 30 N · 0,50 m / − 40 N · 0,20 m = 15 Nm − 8,0 Nm / = 7,0 Nm": the second row carries an equals sign outside the column and reads as a false equation of its own — misreadable on a laptop or projector; breaks the rule "each further = in one column" — write the continuation as `\\ &\quad - 40\,\text{N}\cdot 0{,}20\,\text{m}` (join_wide then gives "ΣM = 30 N · 0,50 m − 40 N · 0,20 m" and the two "=" rows under it), or fix `mathlayout.join_wide` (shared) so a relation row never joins a continuation row. The 390 px form is good.

## Polish
- [Minor] solutions.md line 201 at 390 px — "0,90" ends a line and "-kertainen" starts the next; keep the hyphen with the number (non-breaking join in the build).

## Checked
- own captures of preview/fy5-1.html at 390 and 1280 px, every details and feedback opened, one tile per block holding a display formula (/tmp/claude-0/-home-user-hellsla-github-io/ec927bcd-bc65-54ed-bfcf-2386619399a5/scratchpad/v/fy5-1-*.png); the standard set has no opened solutions at 390 px: fy5-1-ex-390-1, fy5-1-ex-1280-1.
- Delta: all six lifted formulas (lines 119, 149 ×2, 201, 211 ×2). Nothing clipped at 360/390 px; commas and full stops sit inside the formula; the single-row formulas of 149, 201 and 211 read well at both widths.

## Scores
illustrations – (not in delta) · typography 3 · Finnish 5 · accessibility 4
