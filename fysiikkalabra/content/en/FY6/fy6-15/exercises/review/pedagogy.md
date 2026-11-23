VERDICT: PASS
CONTENT-HASH: 6d9f156039ba10f2
SCOPE: delta md-paragraphs,numbers,typography,wording from 8b0aab82c5c21690 base 5b3ca4f

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
