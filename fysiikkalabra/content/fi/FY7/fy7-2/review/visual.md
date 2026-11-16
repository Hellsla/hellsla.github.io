VERDICT: PASS
CONTENT-HASH: 660e1899027dc8bc

## Blocking

## Polish
- [Minor] inquiry.json siirto, Sijoitus (352 and 1280 px) — the stacked numerator's second row reads "·20 000 V" with no space after the dot, because the row starts with a bare `\cdot` — write `{} \cdot 20\,000\,\text{V}` so the multiplication dot keeps its spacing.

## Checked
- batch delta review: every re-broken chain of inquiry.json rendered from preview/fy7-2.html with all boxes open and inspected as crops at 352, 390 and 1280 px (own captures; the repository's 390 px captures keep hints and solutions closed); glyph-to-edge distance measured at 352–412 and 1280 px: nothing clipped, row breaks follow the rule, joined rows read well at 1280 px.
