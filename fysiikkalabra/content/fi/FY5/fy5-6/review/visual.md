VERDICT: PASS
CONTENT-HASH: 7b29aab8984e04ae

## Blocking
(none)

## Polish
- [Minor] The continuation row starts with "·" here; fy5-1 ends the row before with it.
- [Minor] inquiry.json:365 (etsi-virhe prompt, outside this delta, listed in docs/clipped-formulas.tsv) — with the box open at 390 px the inline "γM = 6,674 · 10⁻¹¹ · 5,97 · 10²⁴ m³/s² = …" still runs to 549 px (capture fy5-6-overflow-390); not judged here.

## Checked
- Round 3, delta: the re-broken chains of inquiry.json (lines 210, 406, 460).
- Own captures from preview/fy5-6.html?ratkaisut=1, all boxes opened, in /tmp/claude-0/-home-user-hellsla-github-io/ec927bcd-bc65-54ed-bfcf-2386619399a5/scratchpad/vis3-fi-1: fy5-6-les-390-1.png, fy5-6-les-1280-1.png, fy5-6-spot-390.png, fy5-6-spot-1280.png (the γT² block of line 460).
- Round 2's blocking item is fixed: the comma sits on the result ("= 3,984 · 10¹⁴ m³/s²," and "= 5,0619 · 10⁻² m³/kg,") at both widths, no third column.
- 390 px: constant with its unit on the first row, "· 5,97 · 10²⁴ kg" and "· (27 540 s)²" indented under it, result aligned at "="; 1280 px: the product joined on one row. Mantissa and power never parted.
- Line 210 sits in an experiment answer; seen in the opened state among the γM blocks of the sheets.

## Scores
illustrations 5 · typography 5 · Finnish 5 · accessibility 4
