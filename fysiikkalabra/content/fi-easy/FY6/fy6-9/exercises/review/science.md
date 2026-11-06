VERDICT: PASS
CONTENT-HASH: 47c6ed01597a514a
Mode: full (translation review against the reviewed Finnish set; new YO-skill task L1-09 (units: which expression is the stored energy))
Round 4 (re-review after the L1-09 unit-line rewording, commit 72e243f47)

## Blocking
(none)

## Polish
(none)

## Checked
- Fixed: nothing needed; the new task already matched the Finnish.
- Parity script over all of exercises.json against fi: same keys, ids, kind lists, fbd flag, correct flags, choice order, figure ids, units, tolerances, answers; every number equals the Finnish (only the order of two given quantities differs in a few English/fi-easy sentences, no change of meaning).
- New task L1-09 (units: which expression is the stored energy): recomputed by hand from the task text; the correct option and every distractor's feedback state the same physics and numbers as fi.
- solutions.md: same sections and same numbers as fi for all tasks (the new solution follows the same steps and reaches the same result).
- Terms and notation as in the lesson; Selkeä suomi per NOTES.md §12 (difficult words explained in the sentence, short sentences, no step dropped, decimal comma).
- check_i18n: 0 errors (fi-easy); build.py fy6-9 succeeds.
- L1-09 solution unit lines ("The unit of $UQ$ is ..." / "Lausekkeen $UQ$ yksikkö on ...") and inline tfrac checked against fi: same four units, same physics; check_i18n 0 errors, build fy6-9 ok.
