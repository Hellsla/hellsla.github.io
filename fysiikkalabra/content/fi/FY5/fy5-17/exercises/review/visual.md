VERDICT: PASS
CONTENT-HASH: caaeaa93666bca57

## Blocking
(none)

## Polish
- [Minor] fy5-17-L2-08 — the correct choice's feedback is now very short (65 characters against 168–170) and the correct reason is still marginally the longest (93 against 83–90); both show only after answering, so only a note: give the correct choice one more clause.

## Checked
- Round 2 after commit 4ff432a8f. Rebuilt with `python scripts/build.py fy5-17`; own script (vr5_newtask_probe.py, scratchpad) re-rendered the new task at 390 px after the page scripts ran, with answer, feedback and solution open: document scrollWidth 390, no clipped element outside a scroll box. Image of the card read (fy5-14, fy5-16 and fy5-17 renders re-made; fy5-17 re-read, the other two checked by measurement and by the diff text).
- From text only: the round-2 diff, option and reason lengths.
- Stage-1 feedback no longer reveals the reason; the 3-kertainen computation moved to the reason feedback; "noin" dropped from the answer; the solution row for $d_\text{B}$ (317 px in a 304 px scrolling line, by design) is the only wide formula; no overflow.
- Delta only: the changed task and solution; no figure.

## Scores
illustrations n/a (no figure) · typography 4 · Finnish 5 · accessibility 5
