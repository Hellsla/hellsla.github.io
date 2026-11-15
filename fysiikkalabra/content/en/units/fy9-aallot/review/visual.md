VERDICT: PASS
CONTENT-HASH: 01488dd1f9e29516
Review of the recognition chart (queue 9c) and the term change against the version passed at 5742dd1f4adca003; full on the chart, delta on the rest.

## Blocking
(none)

## Polish
- [C] The chart title and subtitle begin with a lowercase letter ("how do I tell the law?", "free-body diagram first, ..."); capitalise the title in figures.json (sentence case) if the Finnish title is capitalised.
- [C] teacher.md still says "one branch at a time: oscillators, waves, sound" but the chart has rows; say "one row at a time". f_H keeps the Finnish subscript H (MAFY symbol) in the English chart; fine if teacher-approved, otherwise note it.

## Checked
- Chart PNGs at 360 and 1280 px: 8 rows (spring, pendulum, v=fλ, reinforce, cancel, standing wave, beats, Doppler, decibels). No clipped, overlapping or cramped label; white on #1a4d2e is clearly legible; pill, card, spine and start-box style match the other units.
- Typography: KaTeX, italic variables, upright names and units, subscripts and \overline vectors as in MAFY; decimal point in English.
- aria-label in figures.json is in English, complete, and matches the rows in order and meaning (see Polish for any wording difference).
- Diff: figures.json term and label translations (all present), teacher.md "concept map" -> "recognition chart", other changed lines; terms consistent (sliding friction).
