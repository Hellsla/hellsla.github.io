VERDICT: PASS
CONTENT-HASH: d3bbbfc30db75858
## Blocking
(none)

## Polish
- assets/sims/fy6/fy6-13/sim.js:81 (lang sims.fy6-13.lukemat_lap) — the connected-breakdown readout names Q and W as 'values calculated with the ideal model before breakdown', but they are Q = CU and W = QU/2 at the present voltage above the limit, not at the limit — say 'as the ideal model gives them (without breakdown)' — wording only; the point (these are model values, not measurements) reaches the student.

## Checked
- Delta judged on the readout change only; the rest was passed earlier and the diff does not touch it.
- The breakdown readout now separates C, U, E, E_max from the model-only Q and W; the label is consistent with the mallirajaus note below it and with the burnt state (normal readout, Q = 0).
- Q and W no longer read as real stored values during a spark, which repairs a misconception the earlier readout invited.
