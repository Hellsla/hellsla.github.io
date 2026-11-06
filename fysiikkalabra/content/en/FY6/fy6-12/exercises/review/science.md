VERDICT: PASS
CONTENT-HASH: 24851d9dbd27e2fd
Mode: full (translation review against the reviewed Finnish set; new YO-skill task L2-08 (error-finding, potential vs potential difference, eV))
Round 3

## Blocking
(none)

## Polish
(none)

## Checked
- Fixed: fy6-12-L2-08 row 2 wording ("is the smaller, the higher the potential is" -> "is smaller at a higher potential"); numbers untouched.
- Parity script over all of exercises.json against fi: same keys, ids, kind lists, fbd flag, correct flags, choice order, figure ids, units, tolerances, answers; every number equals the Finnish (only the order of two given quantities differs in a few English/fi-easy sentences, no change of meaning).
- New task L2-08 (error-finding, potential vs potential difference, eV): recomputed by hand from the task text; the correct option and every distractor's feedback state the same physics and numbers as fi.
- solutions.md: same sections and same numbers as fi for all tasks (the new solution follows the same steps and reaches the same result).
- Terms and notation as in the lesson; natural English, decimal point.
- check_i18n: 0 errors (en); build.py fy6-12 succeeds.
