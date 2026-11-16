VERDICT: PASS
CONTENT-HASH: 439634de4b2d47e2

## Blocking
- none

## Polish
- [Minor] solutions.md (fy7-8-L2-10, Answer) — after the boxed value the text reads as a fragment: “Is the power loss at the line voltage …” (recorded in round 1). Write: “This is the power loss at …”.
- [Minor] solutions.md (fy7-8-L2-10, Reasonableness) — `P_\text{h} \sim 1 : U^2`: the site mostly writes proportionality with `\propto`.

## Checked
- Delta (queue 5d reflow), round 2. The packet's inventory has no phone capture of the opened solutions, so own captures were made from preview/en/fy7-8.html (rebuilt with build.py) with every solution open at 360, 390 and 1280 px; the 390 and 1280 px sheets of every solution step and task text the diff touches were read at full size (S-Efy7-8-390-*.png, S-Efy7-8-1280-*.png in the session scratchpad).
- Measured at all three widths over the whole exercise section: no formula wider than its card or scrolling in its box (so nothing of docs/clipped-formulas.tsv clips on this page in these captures), no page overflow, no KaTeX error, no raw LaTeX, no lone punctuation line.
- Source against main: the same tokens in the same order outside any new exercise; every new row starts with a relation, a sign or between whole quantities; the older aligned blocks are unchanged.
- Round-1 Major resolved: part c “Saving” of fy7-8-L3-04 now reads `= (43 440 MWh − 13 140 MWh)` / `· 50 €/MWh` / `= 30 300 MWh · 50 €/MWh` / `= 1.515 · 10⁶ €` on a phone and three rows at 1280 px, every relation at the start of its row.
- 390 px (three sheets) and 1280 px (three sheets): L2-06, L3-01, L3-02, L3-04, L3-05, including `0.6 kW` / `+ 2.03 · 10⁻⁴ kW⁻¹` / `· (54.35 kW)²` / `= 1.2 kW,`. New exercise fy7-8-L2-10 in full at 390 px (N-fy7-8-390-1/2.png) and its first half at 1280 px (N-fy7-8-1280-1.png): source line with the Fingrid link, language note and reading date, parts a)–d), answer box, the solution steps with their fractions and roots inside the card.
- Hash identical at the end.

## Scores
illustrations 5 · typography 4 · Finnish 4 · accessibility 5
