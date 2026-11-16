VERDICT: PASS
CONTENT-HASH: e4e94f09bf8bc686

## Blocking
- none

## Polish
- [Minor] inquiry.json:362 — on a phone `B` stands alone on the first row above `= fraction`; correct and readable, the wide fraction leaves no room beside it.
- [Minor] inquiry.json:362 (untouched) — the numerator under the root still breaks before `· 20 000 V`.

## Checked
- batch delta review: queue 5d reflow, round 2. Page rebuilt (build.py fy7-2) and every changed formula of inquiry.json captured from preview/en/fy7-2.html at 360, 390 and 1280 px with every box, hint, solution and choice feedback forced open; the 390 and 1280 px sheets were read at full size. Round-1 Critical resolved: the "She writes" block of Example 2 is again three separate equations (qU, v, r), each with its own left side, identical to main; seen at 390 and 1280 px. Measured at all three widths: no formula wider than its box, no page overflow, no KaTeX error, no raw LaTeX, no lone punctuation line (the closing full stop or comma is set inside the block). Source compared with main: the same tokens in the same order; every new row starts with a relation, a sign or between whole quantities. Hash identical at the end. Figures were not re-judged.
