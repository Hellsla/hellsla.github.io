VERDICT: PASS
CONTENT-HASH: 1e44a607914779d5

## Blocking

## Polish
- [Minor] lesson.md Weight, line 223: "($1.62 : 9.81 \approx 0.17 \approx 1 : 6$)" still breaks inside the formula after "1.62 :" at 1280 px (theory-1280-2). Group it (`{1.62 : 9.81}`) or give the ratio its own short sentence.
- [Minor] inquiry.json (scale-of-a-force-meter and Moon 12 N feedbacks): divisions are still written with a slash ("$5.6 / 1.6 …$", "$12\,\text{N} / 1.62\,\text{m/s}^2$"). Use `:` for a written division, as the lesson does.
- [Minor] sim-390/sim-1280/exp captures: the disclosures "Assumptions of the model and explanation" and "Assumptions of the model" still read as duplicates. Merge them or rename one (e.g. "Explanation").
- [Minor] lesson.md / inquiry.json: "(m/s²)" and "in m/s²" are still plain-text units beside KaTeX $\text{m/s}^2$ in the same sentence (theory-1280-2). Optional: `$\text{m/s}^2$` so the sentence uses one typeface.
- [Minor] exp-exp-1-390 / exp-exp-2-390 / sim-390: on the narrow canvas "Earth" and "Jupiter" almost touch under the bars, and the English chart title, the longest of the three languages, is shrunk to roughly tick-label size (legible, small). Optional: a shorter title ("Same mass, different weights") and a little more gap between the bar names.

## Checked
- Hash 1e44a607914779d5 at start and end; stamp.txt matches, captures current. Delta: sim.js bar-chart title only (8 px higher, width capped to the chart).
- exp-exp-1-390 and exp-exp-2-390 (chart cropped and zoomed 4×): "Same mass, weight in different places" sits on its own line above "G (N)", inside the canvas; "G (N)", the top tick "248" and the Jupiter "248 N" are clear of it and of each other.
- sim-390: same; nothing overlaps or clips.
- sim-1280 (chart zoomed 2×) and lab-1280-1: title centred well above the bars; axis, gridlines, value labels, planet names and legend intact; experiments column unchanged.
- Rest of the page unaffected by a sim.js title change; the layout around the simulation survived in all four captures.

## Scores
illustrations 5 · typography 4 · Finnish (English text) 4 · accessibility 4
