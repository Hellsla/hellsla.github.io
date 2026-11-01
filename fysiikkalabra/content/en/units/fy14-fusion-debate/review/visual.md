VERDICT: PASS
CONTENT-HASH: 2953f276a281a98f

## Blocking
(none) The earlier blocking finding is resolved. The box "Sentence starters for every speech" now renders bold labels (Chair, Opening, Evidence, Rebuttal, Conceding, Question, Closing) with no raw `**` (`selita-390-3`). "That is a fair point, but …" keeps its ellipsis on the same line.

## Polish
1. [Minor] Predictions (`ennusta`, opened at 390). The waiting message still says "Feedback appears when you have read the theory section", but both predictions open with the evidence cards in *Investigate*. `reveal.pending` now exists: set it to "Feedback opens when you reach the evidence cards." on `pred-public` and `pred-origin`.
2. [Minor] Roles table at 390 (`selita-390-1`). "check-ers" is hyphenated and "the rest" wraps. Write "fact-checkers" with a non-breaking hyphen, or shorten "Who" to numbers only.
3. [Minor] The judging paragraph still does not say whether the 0–3 scores or the change in votes decides the winner. Add "The scores give feedback; the vote change decides the winner" (or the reverse).

## Checked
- Fresh captures for this hash (contact sheets, selita-390-1 and 3), and the hero at 390 and 1280: no text, faceless figures.
- Opened myself at 390 and 1280 on the current build:
  - all 5 model answers after writing;
  - all 7 choices with their feedback, including the two new predictions (whose money; where CFS came from), whose options are of similar length;
  - the reworded weakest-argument check.
- The respellings in the French tips use "SYI" for *suis*, as the unit's own u = y rule requires.
- No `.katex-error`, no raw markup, no overflow and no console errors. I recaptured after the latest edits to `inquiry.json` and `teacher.md`. The hash was the same at the end.

## Scores
illustrations 4 · typography 4 · English/French 4 · accessibility 4

## Shared issues
- Narrow table cells at 390 hyphenate automatically, as noted in fy14-fusion-society.
