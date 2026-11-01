VERDICT: PASS
CONTENT-HASH: 9c862ad14f6e60cb

Pedagogy re-review of fy14-binding-energy (2026-11-01), after the "Fixes after review" in review/developer.md (commit 7843fefa). I rebuilt the page and tested it in Playwright at 390 px. `check_layout.py --width 360` is all OK, and the page has no console errors, no raw `$` and no `.katex-error`.

## Earlier findings: all resolved
- Polish 1 (explorer):
  - The explorer question now asks students to compare silver-107 or tin-120 ($A \approx 112$) with iron-56, and to say whether fusing two iron nuclei would climb the curve. So the investigation can now test and refute `pred-iron`.
  - `explorer-findings` has a matching criterion.
  - The explorer no longer preselects helium-4, so it does not hand out the $B$ of helium-4 before the student's own `mass-data` calculation has a reason to matter.
- Polish 2: the extension is now a D + He-3 calculation the student can do. `li6` is in the explorer's reactions.
- Polish 4: in `check-3`, the correct option now gives a reason ("because medium nuclei are bound best"), like the distractors. It is 42 characters against 38 and 29: the longest, but within the length rule.
- Shared issue (overlapping labels): the explorer now highlights only H-2, He-4 and Fe-56, so there are fewer labels. The visual reviewer will judge the result.

## Polish (not blocking)
1. `inquiry.json` `check-3`: the shortest distractor (29 characters) is 31 % shorter than the correct option. To balance it, lengthen it a little, for example "$^{4}\text{He}$, because it is so very stable".

## Checked again
- Predictions:
  - `pred-mass` and `pred-iron` lock on commit with no feedback.
  - They open with `theory-main` and `theory-curve`.
  - Nothing earlier on the page answers them.
- The model answers stay closed until the student writes something.
- The worked example is staged.
- The theory is about 550 words.
- The checks still target real misconceptions, and the new 22.2 MeV distractor in `check-2` is a realistic power-of-ten error.

## Re-check 2026-11-01: photographs
Meitner portrait in People, after the fission tasks and theory; the caption adds nothing a later check question asks. Clear and concise. No lesson ids, no ×, British spelling.
