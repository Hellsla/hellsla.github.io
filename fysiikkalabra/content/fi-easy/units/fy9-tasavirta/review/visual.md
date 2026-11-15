VERDICT: FAIL
CONTENT-HASH: 9441c766eb5c2f62
Review of the recognition chart (queue 9c) and the term change against the version passed at ccddd23e0bb39d09; full on the chart, delta on the rest.

## Blocking
- [Major] figures.json (fi-easy, kartta) — the start-box subtitle "piirrä ensin kytkentäkaavio, katso sitten tunnusmerkki" is wider than the box and is clipped at both ends at 360 and 1280 px — essential text unreadable — shorten to e.g. "piirrä kytkentä ensin, sitten tunnusmerkki" (the Finnish original's text, which fits).

## Polish
(none)

## Checked
- Chart at 360 px (fy9-tunnistus/fy9-tasavirta-fi-easy-360.png): every row's sign, arrow label and pill read in full, no clipped or overlapping label, white on #1a4d2e legible, pill style matches the other units, KaTeX subscripts and \overline vectors render.
- ARIA_KARTTA/figures.json aria-label is Finnish and lists every row of the chart.
- Friction terms: no liikekitka left in the unit's fi-easy texts.
