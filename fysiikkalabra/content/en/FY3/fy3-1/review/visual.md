VERDICT: PASS
CONTENT-HASH: 199db6cdf206c390

## Blocking
(none) Delta resolved: line 214 now sets "$1\,\text{N} = 1\,\text{kg}\cdot\text{m/s}^2$" as one formula (theory-1280-2: equals sign in maths type, no body-type gap). The bar chart's separate "chart scale" caption is gone; the y axis now closes with its full-scale value 248 at the tick and the gridline, and "G (N)" sits above the axis. At 390 px (sim-390, exp-exp-1-390, exp-exp-2-390, zoomed 4x) the axis title, the 248 tick label, the chart title and the Jupiter value label "248 N" are clearly apart; nothing clips. At 1280 px (sim-1280, lab-1280-1) the same holds. The readout sentence "The scale of the bar chart 0–248 N is the weight of this mass on Jupiter" still explains the scale, so no information was lost.

## Polish
- [Minor] lesson.md Weight, line 223: "($1.62 : 9.81 \approx 0.17 \approx 1 : 6$)" still breaks inside the formula after "1.62 :" at 1280 px (theory-1280-2). Group it (`{1.62 : 9.81}`) or give the ratio its own short sentence.
- [Minor] inquiry.json (scale-of-a-force-meter and Moon 12 N feedbacks): divisions are still written with a slash ("$5.6 / 1.6 …$", "$12\,\text{N} / 1.62\,\text{m/s}^2$"). Use `:` for a written division, as the lesson does.
- [Minor] sim-390/sim-1280/exp captures: the disclosures "Assumptions of the model and explanation" and "Assumptions of the model" still read as duplicates. Merge them or rename one (e.g. "Explanation").
- [Minor] lesson.md / inquiry.json: "(m/s²)" and "in m/s²" are still plain-text units beside KaTeX $\text{m/s}^2$ in the same sentence (theory-1280-2). Optional: `$\text{m/s}^2$` so the sentence uses one typeface.
- [Minor] exp-exp-1-390 / sim-390: on the narrow canvas, "Earth" and "Jupiter" almost touch under the bars, and grass tufts show between the body labels and the legend. Optional: a slightly smaller label size or a little more gap below the bar row.

## Checked
- sim-390, sim-1280: new y-axis end value 248 and the "G (N)" title, gridline, chart title, value labels.
- exp-exp-1-390, exp-exp-2-390 (cropped and zoomed 4x): no collision of 248 / G (N) / title / "248 N".
- lab-1280-1: the simulation beside the experiments. The chart labels are small but readable, and the layout is intact.
- theory-1280-2: the single formula on line 214, the table, the ratio line and figure 4.
- contact-1 (#1–#12): top, figures, example and stages unchanged and intact.

## Scores
illustrations 5 · typography 4 · Finnish (English text) 4 · accessibility 4
