VERDICT: PASS
CONTENT-HASH: 78c9fab025692b2a

## Blocking
- none

## Polish
- [Minor] inquiry.json:193 — the split inline chain (`… 2.0 mWb` / `= −20 mWb`) wraps cleanly on a phone; where both pieces share a line the second piece's `=` has no relation space on its left. `${} = …$` would restore it.

## Checked
- batch delta review: queue 5d reflow, round 2. Page rebuilt (build.py fy7-5) and every changed formula of inquiry.json captured from preview/en/fy7-5.html at 360, 390 and 1280 px with every box, hint, solution and choice feedback forced open; the 390 and 1280 px sheets were read at full size. Round-1 Critical resolved: in the find-the-error task A and |e| are again separate equations, identical to main; seen at 390 and 1280 px. The feedback row `|e| = 200 · 0.30 T` / `· 6.0 · 10⁻⁴ m² : 0.050 s` / `= 0.72 V.` breaks between whole quantities. Measured at all three widths: no formula wider than its box, no page overflow, no KaTeX error, no raw LaTeX, no lone punctuation line (the closing full stop or comma is set inside the block). Source compared with main: the same tokens in the same order; every new row starts with a relation, a sign or between whole quantities. Hash identical at the end. Figures were not re-judged.
