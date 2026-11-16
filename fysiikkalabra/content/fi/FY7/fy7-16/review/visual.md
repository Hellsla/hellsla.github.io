VERDICT: FAIL
CONTENT-HASH: 4ca9f81619c9ed4a

## Blocking
- [Major] inquiry.json `mittaus-lataus`, solution step Sijoitus (own captures at 352, 390 and 1280 px; the official `fy7-16-stage-tutki-390-3.png` shows the solution closed) — on a phone the rows are set as "= (21,01 Wh − 14,26 Wh)/14,26 Wh", then "· 100 % = 6,75 Wh/14,26 Wh", then "· 100 % = 47,34 %": the factor "· 100 %" stands in the left-hand column before the aligned `=`, so rows 2 and 3 read as equations whose left side is "· 100 %". At 1280 px (the solution sits in a ~370 px column) the joined form breaks as "= … · 100 % = 6,75 Wh/14,26 Wh" / "· 100 % = 47,34 %", is shrunk to fit and touches the box edge — ambiguous notation in a model solution; a factor is separated from its fraction and the `=` signs are not in one column — keep each "· 100 %" on the row of its fraction, every row starting with `=`: `\begin{aligned} &= \dfrac{21{,}01\,\text{Wh} - 14{,}26\,\text{Wh}}{14{,}26\,\text{Wh}} \cdot 100\,\% \\ &= \dfrac{6{,}75\,\text{Wh}}{14{,}26\,\text{Wh}} \cdot 100\,\% \\ &= 47{,}34\,\% \end{aligned}` (if row 1 is too wide at 352 px, put `&\quad \cdot 100\,\%` indented on its own row, never in the relation column), and make sure the form shown in the narrow column at 1280 px is this one.

## Polish
- [Minor] `mittaus-lataus` hint 3 (352 px) — the break falls inside the bracket, "(21,01 Wh / − 14,26 Wh) : 14,26 Wh."; readable.

## Checked
- batch delta review: every re-broken chain of inquiry.json rendered from preview/fy7-16.html with all boxes open and inspected as crops at 352, 390 and 1280 px (own captures; the repository's 390 px captures keep hints and solutions closed) and the official fy7-16-stage-tutki-390-3.png; glyph-to-edge distance measured at 352–412 and 1280 px: nothing clipped, row breaks follow the rule, joined rows read well at 1280 px except the blocking item.
