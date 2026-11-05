VERDICT: PASS
CONTENT-HASH: 351a2dfbe36ac039

Mode: translation review (fi-easy (NOTES.md section 12)) against the reviewed Finnish. Round 2, new task fy3-12-L2-08.

## Blocking
(none)

## Polish
- None.

## Checked
- fy3-12-L2-08 recomputed independently: door 60 W, roof 216 W, windows 288 W, wall 459 W (UA = 2.0, 7.2, 9.6, 15.3 W/K, DeltaT = 30 K); order door < roof < windows < wall. Equals fi.
- Answer, unit, tolerance, kind, order/statements/choices, correct flags and their order equal fi.
- solutions.md of L2-08: every number, unit and formula equals fi; decimal comma kept.
- Physics and scope unchanged; no Finnish-only terms left.
- No translation fix needed. check_i18n.py shows nothing for fy3-12; build.py fy3-12 succeeds.
