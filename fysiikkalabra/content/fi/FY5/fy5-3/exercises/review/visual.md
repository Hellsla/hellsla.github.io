VERDICT: FAIL
CONTENT-HASH: 9a61a2b67bdaf12c

## Blocking
- [Major] exercises/solutions.md line 201 (Järkevyys, two formulas), 390 and 1280 px — the result is cut inside the number: "2π · 42,16 · 10⁶ m = 2,649" and under it "· 10⁸ m," (same for "3075 m/s · 86 160 s = 2,649 / · 10⁸ m.") — the first row reads as the result 2,649; a value in powers of ten must stay whole — break before the equals sign: `&2\pi \cdot 42{,}16 \cdot 10^{6}\,\text{m} \\ &= 2{,}649 \cdot 10^{8}\,\text{m}` and `&3075\,\text{m/s} \cdot 86\,160\,\text{s} \\ &= 2{,}649 \cdot 10^{8}\,\text{m}` (both fit one row on a wide screen).
- [Major] solutions.md line 304 (Sijoitus), wide form (≥ 700 px) — "Δv = 2π·" then "0,3333 1/s · (1,80 m − 0,60 m) = 2,513 m/s": the "=" is outside the column and the second row reads as a false equation — mark the continuation `\\ &\quad 0{,}3333\,\tfrac{1}{\text{s}}\cdot(…)` so join_wide joins it to "Δv = 2π ·", or fix `mathlayout.join_wide` (shared) so a relation row never joins a continuation row.

## Polish
- [Minor] line 304 at 390 px — the first row is only "Δv = 2π·"; the continuation starts in the equals column, an indent (`&\quad`) would show it continues.

## Checked
- own captures of preview/fy5-3.html at 390 and 1280 px, every details and feedback opened, one tile per block holding a display formula (/tmp/claude-0/-home-user-hellsla-github-io/ec927bcd-bc65-54ed-bfcf-2386619399a5/scratchpad/v/fy5-3-*.png); the standard set has no opened solutions at 390 px: fy5-3-ex-390-2, -390-3, fy5-3-ex-1280-1, -1280-2.
- Delta: lines 144, 163 (×2), 201 (×2), 245, 304. Lines 144, 163 and 245 read well at both widths; nothing clipped at 360/390 px; punctuation inside the last row.

## Scores
illustrations – (not in delta) · typography 2 · Finnish 5 · accessibility 4
