VERDICT: PASS
CONTENT-HASH: c5fef9077a48f7ca

Pedagogy re-review of fy14-magnetic-confinement (2026-11-01), after "Fixes after review" (commit cf5a329b) and the simulation fix (commit 7561f2b5). Rebuilt. Playwright at 390 px:
- exp-mirror records 10° and 20° as *escapes*, 40° and 80° as *trapped*;
- the readout shows $\mu$, $\sin^2\theta = 0.12$ and $B_0/B_{\max} = 0.25$, but no verdict and no 30° rule;
- the `calc` box now gives only the mirror ratio;
- no console errors.

## Earlier findings
- **Polish 1 is done.** `review`, `exp-particles` and `find-error` are within ±30 %.
- **Polish 2 is done.** `check-2` is a new case (an electron moving up, ⊙, answer left). The distractor "to the right" carries the sign misconception.
- **Polish 3 is done.** The trapped/escapes verdict now appears only in the student's table after recording, so it is evidence. The rule is left for the student to infer.
- **Polish 5 is done.** The French corner uses the shared style, with Finnish *nj*.
- **Polish 4 (workload) still holds.** This is the heaviest unit of the four, but the optional tasks keep the core path to 75 minutes.

## Blocking
None.

## Polish
1. `check-1`: the correct option ("Its speed stays the same all the time.", 38 characters) is now the shortest by about 25–35 % (the distractors have 48–52). Lengthen it slightly, for example "Its speed stays the same, only its direction changes." (52 characters).

## Checked
- Predictions: committed before the simulation and revealed only after 3 rows each. Both experiments can refute their predictions.
- The conclusion is gated on both experiments, with a word bank and starters.
- The single-particle model is separated from collective plasma behaviour.
- teacher.md has plans for fast pairs and for running out of time.

Hash update (2026-11-01): the only change since this review is the placement of the canvas label cards in `assets/sims/fy14/magnetic/sim.js` (commit 3735b0fa). It is layout only and does not change the pedagogy.
