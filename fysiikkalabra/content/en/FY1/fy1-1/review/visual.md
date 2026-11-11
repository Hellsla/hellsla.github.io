VERDICT: PASS
CONTENT-HASH: 09da6a2ea3b09622

## Blocking
- none

## Polish
- [Minor] fy1-1-sim-390.png — "human" and "blue whale" labels sit only about 4 px apart in the shrunk label row. They do not overlap, so this is acceptable. Optionally widen the gap.

## Checked
- Delta: the only change is in sim.js. A shrunken label is now measured at its own font size, which fixes overlapping label rows. The lesson.md change is the teacher-approved figures category, which needs no review.
- Opened fy1-1-sim-390.png and fy1-1-sim-1280.png. The label row (ant, euro coin, football, human, blue whale, with their values) is legible, with no overlap or clipping at either width. The values are LaTeX with units. The map bar and the controls are intact.
- I did not open the other captures. The diff does not touch them, and the sim captures show the layout survived.

## Scores
illustrations 5 · typography 5 · Finnish 5 (English text reviewed) · accessibility 4
