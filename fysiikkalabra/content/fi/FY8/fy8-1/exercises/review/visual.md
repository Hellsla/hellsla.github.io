VERDICT: PASS
CONTENT-HASH: 8a04121185cb5a08
SCOPE: delta reflow (long solution formulas lifted onto their own line, aligned blocks)

## Blocking
(none)

## Polish
- [Minor] Sijoitus blocks with a \cdot continuation: the block shows a mid-row "=" (e.g. fy8-6 "hc = 6,626·10^-34 J s / · 2,998·10^8 m/s = 1,9865·10^-25 J m,", fy8-10-11 "E_B = a / · (c)² = a / · 8,98800·10^16 m²/s² = 2,04479·10^-11 J"). The "=" is not in the aligned column and a continuation row such as "· (2,998·10^8 m/s)² = 2,27502·10^-28 kg" reads like an equation of its own. Fix: put each "=" on its own row (the source already does); if the build merges rows, adjust mathlayout so a "=" row stays a row of its own. Readable, so it does not block.
- [Minor] The comma after a block ("... J m,") is inside the last row as agreed, and the answer lines read cleanly.

## Checked
- Opened at 1280 px: fy8-1 L2-1280-8 (ΔE card, aligned blocks, fractions in one column). The 390 px layout is covered by check_layout 360/390 (passed), no 390 px exercise capture exists.
- Across the opened captures: blocks sit inside the card, no clipping, equals signs aligned in ordinary chains, fractions and units upright with a thin space, decimal comma, sentence marks inside the last row, words and numbers unchanged.

## Scores
illustrations 4 · typography 4 · Finnish 5 · accessibility 4
