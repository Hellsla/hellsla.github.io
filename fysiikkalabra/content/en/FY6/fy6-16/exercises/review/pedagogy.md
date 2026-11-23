VERDICT: PASS
CONTENT-HASH: a18be3521b5b027b
SCOPE: delta md-paragraphs,numbers,reflow,typography,wording from 6c786ed6b0783012 base 98218de

## Blocking
(none)

## Polish
- Earlier polish items stand unchanged (not touched by this diff).
- The step lines in the long Formula blocks are only a few symbols each; fine at 360 px, nothing clipped.

## Checked
- Diff is the queue 8g change: the Kaava/Formula step now starts from basic-principle equations (P_k = UI_k, I = sum of I_k, Ohm's law per part, U = sum of parts, P = RI^2) and ends in the working formula; the order is principle, then derivation, then result, which a student who could not solve the task can follow.
- Prose changes in solutions are reflow only (one sentence per paragraph); I compared the words removed and added and found no change in meaning, numbers or answers.
- Series-resistance derivation (U_body + U_k) and the step-voltage lines are consistent with the chapter and with the previous chapter's Ohm's law; no step skipped.
- Task texts, levels, counts and answers untouched; level mix as passed earlier.
- Disk check: the aligned blocks render as separate lines in solutions.md (the packet diff shows them collapsed, a display artefact).
- Hash unchanged at start and end.
