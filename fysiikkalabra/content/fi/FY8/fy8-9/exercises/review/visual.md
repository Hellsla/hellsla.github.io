VERDICT: PASS
CONTENT-HASH: 040c97f3f731fe50
SCOPE: delta reflow from cac0fd5db47fb84c base cf5f907

## Blocking
(none)

## Polish
- [Minor] Sijoitus blocks with a \cdot continuation: the block shows a mid-row "=" (e.g. fy8-6 "hc = 6,626·10^-34 J s / · 2,998·10^8 m/s = 1,9865·10^-25 J m,", fy8-10-11 "E_B = a / · (c)² = a / · 8,98800·10^16 m²/s² = 2,04479·10^-11 J"). The "=" is not in the aligned column and a continuation row such as "· (2,998·10^8 m/s)² = 2,27502·10^-28 kg" reads like an equation of its own. Fix: put each "=" on its own row (the source already does); if the build merges rows, adjust mathlayout so a "=" row stays a row of its own. Readable, so it does not block.
- [Minor] The comma after a block ("... J m,") is inside the last row as agreed, and the answer lines read cleanly.

## Checked
- No capture of this lesson opened; judged by the same shared component as fy8-1, 2, 6, 10 and 16, whose captures I opened (see the other lessons' reports). Source of the aligned blocks read only. If its blocks differ in kind, ask again.
- Across the opened captures: blocks sit inside the card, no clipping, equals signs aligned in ordinary chains, fractions and units upright with a thin space, decimal comma, sentence marks inside the last row, words and numbers unchanged.

## Scores
illustrations 4 · typography 4 · Finnish 5 · accessibility 4
