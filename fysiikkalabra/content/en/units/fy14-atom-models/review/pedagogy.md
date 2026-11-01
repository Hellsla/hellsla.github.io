VERDICT: PASS
CONTENT-HASH: 98884cb62e662452

Pedagogy re-review of fy14-atom-models (2026-11-01), after the "Fixes after review" in review/developer.md (commit cdc675d6). I rebuilt the page and tested it in Playwright at 390 px.

Browser check:
- Both predictions lock on commit and show no feedback.
- `pred-gold` opens when *Key idea* is on screen, after the gold-foil section, the paths task, the spectra and `compare-spectra`. `pred-jump` opens when *Bohr's quantum atom* is on screen.
- The model answers stay closed while the text box is empty.
- There are no console errors.

## Earlier findings: all resolved
- Blocking 1 is resolved. `pred-gold` now asks what Geiger and Marsden *actually saw*, and Thomson's model is given as the best picture of 1909. The feedback on the Thomson option recognises good reasoning ("That is what Thomson's model predicts … and it is what everyone expected"), and only the evidence settles the question.
- Blocking 2 is resolved. The photon-energy `review` now sits in Investigate, right before `red-line`, where it prepares the calculation. Nothing before `pred-jump` answers it.
- The new pair talk in Think about it (marbles thrown into a closed box) does not give away `pred-gold`. It sets up the scattering idea without saying what the foil does, and its sentence starters are neutral.
- Polish 1–4 are done:
  - the *whereas* sentence is correct;
  - `back-to-predictions` asks the student to check $E_3 - E_2$ against their $1.89\ \text{eV}$;
  - teacher.md points weaker students to the solution of the 5 → 2 task;
  - no correct option is the longest (only in `check-2`, where all four options are the same length).

## Blocking
None.

## Polish
1. `inquiry.json` `hook-talk` says "Write down your idea: you will come back to it", but nothing in the unit returns to the box. Fix: add one sentence to `back-to-predictions`: "How is the gold foil like your closed box, and what was hidden inside it?"

## Shared issues
- `templates/inquiry.js` §1 (unchanged): a theory section counts as seen once any pixel of it enters the viewport. This unit is not affected.

## Re-check 2026-11-01: photographs
Edited: the Rutherford portrait sat between "The figure shows such paths … to scale" and the scatter drawing, splitting the figure from its text; moved it before "In 1911 Rutherford explained the result". It now follows the predictions and does not answer `foil-read`. Bohr portrait in People is fine. No lesson ids, no ×, British spelling.
