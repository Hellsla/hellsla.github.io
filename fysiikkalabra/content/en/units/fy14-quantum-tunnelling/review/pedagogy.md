VERDICT: PASS
CONTENT-HASH: 52dad39318ce6af1

Pedagogy re-review of fy14-quantum-tunnelling (2026-11-01), after the "Fixes after review" in review/developer.md (commit cdc675d6). I rebuilt the page and tested it in Playwright at 390 px.

Browser check:
- Both predictions lock on commit and show no feedback.
- `pred-slits` opens when *Key idea* is on screen, after the slit panels, `slits-talk` and the tunnelling table. `pred-tunnel` opens when *Tunnelling and the Sun* is on screen.
- The model answers stay closed while the text box is empty.
- There are no console errors.

## Earlier findings: all resolved
1. `pred-tunnel` now asks "What do you predict?" about a barrier made twice as wide. Its options are now the classical bounce, "far more rarely", "half as often" and "equally often". So the part that is open to argument, the effect of width, is now what the student predicts. The "half as often" distractor targets the linear-thinking misconception that the factor task and `check-2` later repair.
2. Each option is now a single claim about width, so a student is no longer forced to accept two claims at once.
3. The Reasonableness step of `proton-wave` compares $779\ \text{fm}$ with the turning distance of about $1000\ \text{fm}$.
4. *Tunnelling and the Sun* now says that tunnelling only brings the protons close. The long wait comes from the weak interaction ($\text{p} + \text{p} \to \text{d} + \text{e}^+ + \nu$), which the feedback of `check-3` repeats. This removes the misconception that tunnelling alone makes the Sun slow. The selita sections now run to about 470 words, still within the limit.
5. The correct option of `check-3` has been shortened.

## Blocking
None.

## Polish
1. `inquiry.json` `pred-tunnel`: the correct option (62 characters) is the longest, slightly ahead of 60, 55 and 54. Fix: "It sometimes passes, far more rarely through the wide one." (58).

## Shared issues
- `templates/inquiry.js` §1 (unchanged): a theory section counts as seen once any pixel of it enters the viewport. This unit is not affected.
