VERDICT: PASS
CONTENT-HASH: 6fc6fb8caaf31946
Review of the recognition chart (queue 9c) and the term change against the version passed at e8a6f31d617c0812; full on the chart, delta on the rest.

## Blocking
(none)

## Polish
- C: The pill $\varepsilon = \Delta x/\bar{x}$ omits the Kaava's $\cdot 100\,\%$. Both forms are correct, so this is not a finding; the factor could be added if space allows.
- C: The start box says "mistä tunnistan lain?" while the aria-label says "mitä menetelmää". This unit's rows are methods rather than laws, so the aria wording fits better.

## Checked
- Row 1, repeated measurement → $\bar{x} \pm \Delta x$: matches Kaava (best estimate is the mean, $\Delta x$ is half the range in this course).
- Row 2 → relative uncertainty $\Delta x/\bar{x}$: matches Kaava.
- Row 3, one outlying result → karkea virhe, check it: matches the text (do not delete it without a reason).
- Row 4, deviation always in the same direction → systematic error, repeating does not remove it: correct and matches the text.
- Row 5, points on a line → $y = kx + b$. Row 6, steepness → $k = \Delta y/\Delta x$ from two far-apart points of the line: matches Kaava (read from the line, not from the measured points).
- Row 7, slope uncertainty → steepest and shallowest lines (ääriviivat), $\Delta k$ = half the difference: matches the anatomia figure and its text.
- Row 8, curve → new quantity, $s$ vs. $t^2$: matches the linearisation section (from rest, so slope $a/2$).
- The aria-label states the same physics as each row and adds nothing that contradicts the unit.
- The diff contains only the chart in figures.py and its SVG in unit.md. No other text changed.
