VERDICT: PASS
CONTENT-HASH: 4161a9356eed0c2b
Mode: full (translation review against the reviewed Finnish set; new YO-skill task L2-08 (force diagram selection, dust particle in a uniform field))
Round 3

## Blocking
(none)

## Polish
(none)

## Checked
- Fixed: nothing needed; the new task already matched the Finnish.
- Parity script over all of exercises.json against fi: same keys, ids, kind lists, fbd flag, correct flags, choice order, figure ids, units, tolerances, answers; every number equals the Finnish (only the order of two given quantities differs in a few English/fi-easy sentences, no change of meaning).
- New task L2-08 (force diagram selection, dust particle in a uniform field): recomputed by hand from the task text; the correct option and every distractor's feedback state the same physics and numbers as fi.
- solutions.md: same sections and same numbers as fi for all tasks (the new solution follows the same steps and reaches the same result).
- Figure alt texts in figures.json carry the same four descriptions; the subscript maps s -> e in en ($F_\text{e}$ in task, feedback and solution), as in the existing en text; fi-easy keeps $F_\text{s}$.
- Terms and notation as in the lesson; natural English, decimal point.
- check_i18n: 0 errors (en); build.py fy6-11 succeeds.
