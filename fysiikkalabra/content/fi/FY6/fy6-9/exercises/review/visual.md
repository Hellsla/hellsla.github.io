VERDICT: PASS
CONTENT-HASH: f4c96813537f2d5f
SCOPE: delta wording from 9074195cdd27281d base e000744

## Blocking
(none)

## Polish
- [Minor] Kaava blocks (level 2 parts 6 and 8, level 3 part 7, level 1 charging-current and internal-resistance tasks) — `\sum \Delta V = 0` renders the sum sign in display size, so the first row is taller than the rest and the row spacing is slightly uneven; the symbol itself reads correctly — optional: `\textstyle\sum \Delta V` or `\Sigma \Delta V`.
- [Minor] Same blocks — the first row is not aligned at `=` with the rows below; as in the previous round, optional. For science: confirm `\sum \Delta V = 0` (potential changes round the loop) is the notation the course wants in place of `\Sigma U = 0`.

## Checked
- fy6-9 exercises at 1280 px, solutions open: level 3 part 7 (staged charging, Kaava block with `\sum \Delta V = 0`), level 2 part 6 (resistance from the graph, Kaava block and Sijoitus), level 1 part 3 (unchanged Kaava block, for comparison).
- `\sum \Delta V = 0` renders in KaTeX without red source, clipping or overflow; the rows below it are unchanged and readable.
- The other changed Kaava blocks (charging current, internal resistance, relative current drop) use the same markup and were not opened separately.

## Scores
illustrations 5 · typography 4 · Finnish 4 · accessibility 5
