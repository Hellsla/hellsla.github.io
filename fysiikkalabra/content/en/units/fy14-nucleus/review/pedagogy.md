VERDICT: PASS
CONTENT-HASH: c3553fea1e86a21a

Pedagogy re-review of fy14-nucleus (2026-11-01), after the "Fixes after review" in review/developer.md (commit 7843fefa). Page rebuilt and tested in Playwright at 390 px. `check_layout.py --width 360` is all OK, with no console errors, no raw `$` and no `.katex-error`.

## Earlier findings: all resolved
- Polish 1: in `pred-heavy`, the correct option is now 54 characters and the distractors 61 and 48, so all three are in balance.
- Polish 2: builder task 6 now says that neutrons cannot cancel charge but add attraction. This gives `pred-glue` some evidence from the investigation.
- Polish 3: the options are balanced. The correct option is no longer the longest in `pred-glue` (a near tie, 70 against 70), `find-error` or `check-3`.

## Polish (not blocking)
None new.

## Checked again
- Predictions:
  - `pred-neutron`, `pred-glue` and `pred-heavy` lock on commit with no feedback.
  - They open only when `theory-main` (`pred-neutron`) or `theory-forces` (the other two) comes on screen.
  - The hook, the Why line, the hero and the review feedback do not give the answers.
- The model answers stay closed until the student writes something.
- The theory is about 520 words.
- The teacher notes are unchanged and still have a realistic 75-minute plan.
