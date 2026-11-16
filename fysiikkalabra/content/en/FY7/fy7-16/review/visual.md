VERDICT: PASS
CONTENT-HASH: 52c038434adbf573

## Blocking
- none

## Polish
- [Minor] inquiry.json:325 — the left side `increase` is still text above the formula whose rows begin with `=` (recorded in round 1).

## Checked
- batch delta review: queue 5d reflow, round 2. Page rebuilt (build.py fy7-16) and every changed formula of inquiry.json captured from preview/en/fy7-16.html at 360, 390 and 1280 px with every box, hint, solution and choice feedback forced open; the 390 and 1280 px sheets were read at full size. Round-1 Major resolved: the B0 substitution now breaks `: (12 · 1.1 · 10⁻³ m²` / `· 2π · 1.40 · 10⁵ Hz)` between whole quantities and fits its box at 360 and 390 px; one row at 1280 px. Measured at all three widths: no formula wider than its box, no page overflow, no KaTeX error, no raw LaTeX, no lone punctuation line (the closing full stop or comma is set inside the block). Source compared with main: the same tokens in the same order; every new row starts with a relation, a sign or between whole quantities. Hash identical at the end. Figures were not re-judged.
