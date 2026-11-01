VERDICT: PASS
CONTENT-HASH: 14be3bd2753d402e

## Blocking
(none) This is a re-review after commit c6532e4f. The earlier Polish is resolved:
- The table cells are shorter, and the explanations are now in a paragraph under the table.
- Quantities are in LaTeX.
- The check-2 option names the 2016 baseline.
- Frames 1–2 are lettered lists.

## Polish
1. [Minor] The claims table at 390 (`stage-tutki-390-5/6`). The verdict column is about 50 px wide, so "cor-rect today" and "needs con-text" hyphenate over three lines. Fix: give the column `white-space: nowrap`, or shorten the verdicts to one word each ("correct", "outdated", "context") and explain the categories once above the table.

## Checked
- Fresh build and captures for this hash: top and intro at 390 and 1280, every stage at 390 and 1280, contact sheets.
- The sort and sponsor items now sit in Investigate before the table.
- Prediction 1 offers bare years.
- The video component: the click-to-load layout and the youtube-nocookie iframe, as in the earlier review. Playback is not possible in the sandbox.
- Playwright: no `.katex-error` and no overflow. The only raw `$` are currency signs in the source titles.

## Shared issues
(none new)

## Scores
illustrations 4 · typography 4 · English/French 4 · accessibility 4
