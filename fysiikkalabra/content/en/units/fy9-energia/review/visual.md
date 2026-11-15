VERDICT: PASS
CONTENT-HASH: ea3f9b67dd2e79b6
Review of the recognition chart (queue 9c) and the term change against the version passed at 0f8592564d0f83bc; full on the chart, delta on the rest.

## Blocking
(none)

## Polish
- [C] The chart title and subtitle begin with a lowercase letter ("how do I tell the law?", "free-body diagram first, ..."); capitalise the title in figures.json (sentence case) if the Finnish title is capitalised.
- [C] teacher.md says "one example for each branch"; use "each row".

## Checked
- Chart PNGs at 360 and 1280 px: 8 rows (closed system ... work). No clipped, overlapping or cramped label; white on #1a4d2e is clearly legible; pill, card, spine and start-box style match the other units.
- Typography: KaTeX, italic variables, upright names and units, subscripts and \overline vectors as in MAFY; decimal point in English.
- aria-label in figures.json is in English, complete, and matches the rows in order and meaning (see Polish for any wording difference).
- Diff: figures.json term and label translations (all present), teacher.md "concept map" -> "recognition chart", other changed lines; terms consistent (sliding friction).
