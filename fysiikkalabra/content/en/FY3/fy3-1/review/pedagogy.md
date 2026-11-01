VERDICT: PASS
CONTENT-HASH: 1e44a607914779d5

## Blocking
(none)

## Polish
- lessons/FY3/fy3-1/sim.js:192 — the English title "Same mass, weight in different places" is longer, so the new 292 px cap shrinks it at 390 px to about the size of the axis numbers (smaller than the bar labels, which keep a 10 px floor); still readable in sim-390 — a floor like the value labels', or a shorter en title ("Same mass, different weights"), would help.
- templates/sim-embed.js:43 — the en note "Mass is the same everywhere…" exceeds 15 words, so it folds into a box "Assumptions of the model and explanation" right above "Assumptions of the model": two near-identical headings (pre-existing, not in this diff; fi/fi-easy show the note inline).

## Checked
- Round 3 delta since 4253a4a: only the chart title's position and width cap in sim.js; no text, lang key or lesson content changed.
- sim-390 and sim-1280: title on its own line above G (N), no overlap, bars and labels legible; readout scale sentence still matches the axis 0–248 N.
- Earlier findings hold; check_i18n en: 0 errors. Hash 1e44a607914779d5 at start and end.
