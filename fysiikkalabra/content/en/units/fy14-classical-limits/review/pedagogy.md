VERDICT: PASS
CONTENT-HASH: 246a2edfabca8c0a

Pedagogy re-review of fy14-classical-limits (2026-11-01), after the "Fixes after review" in review/developer.md (commit cdc675d6). I rebuilt the page and tested it in Playwright at 390 px.

Browser check:
- Both predictions lock on commit and show no feedback.
- `pred-peak` opens when *Key idea* is on screen, after the curves, the peak table and `curves-talk`. `pred-share` opens when *The ultraviolet catastrophe* is on screen.
- The model answers stay closed while the text box is empty.
- There are no console errors and no `.katex-error`.

## Earlier findings: all resolved
1. `pred-share`, third option: it now reads "The power falls to zero at short wavelengths."; what real objects do is only in its feedback.
2. The `pred-share` prompt no longer gives the "more patterns at short wavelengths" step, so the student has to reason it out.
3. `pred-peak` glosses *black body*.
4. `back-to-predictions` returns to the glowing things the student named at the start.
5. `teacher.md` sets the written biography as the first thing to give as homework.
6. Option lengths: no correct option is the longest any more (`check-1` 50/55/56/49, `check-3` 54/55/46/47, `pred-share` 45/40/42).

## Blocking
None.

## Polish
1. `inquiry.json` `pred-peak`: the distractor "There is no peak: a hotter body radiates equally at all wavelengths." is 68 characters, about 50 % longer than the others. Fix: shorten it to "There is no peak at all." so the four options are closer in length.

## Shared issues
- `templates/inquiry.js` §1 (unchanged): a theory section counts as seen once any pixel of it enters the viewport. This unit is not affected, because each reveal points at the explanation that comes after the evidence.
