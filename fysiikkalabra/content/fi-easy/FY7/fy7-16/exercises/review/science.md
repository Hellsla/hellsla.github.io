VERDICT: PASS
CONTENT-HASH: 04ccd2767440e5a9
Mode: full (translation review against the reviewed Finnish set)
Round 1

## Blocking
(none)

## Fixed
- L2-05 and L3-04 texts: "lineaarinen interpolointi" now explained in plain words in the task text itself ("laskea arvo kahden mittauspisteen väliltä suoran avulla"); numbers and answers unchanged.

## Polish
(none)

## Checked
- All 8 new exercises (L1-06..08, L2-05..07, L3-04..05) and all older ones compared with content/fi by script: ids, levels, kinds, answers, units, tolerances, correct flags, choices, data table cells and every number in texts and feedback are identical (decimal point in en; decimal comma in fi-easy as in fi).
- solutions.md of the new tasks read against fi: every number, formula and result the same (0.5036 mW, 15.05 km, 12.86 mm, 0.2003 dB/km, 1 %, 13.28 mm, 42.43 kHz; powers 2.59/2.07/1.29 kW).
- L1-06: exactly one correct option; distractor feedback names the same misconception as fi.
- Language is selkosuomi: short sentences, terms (pyörrevirta, interpolointi, pienimmän neliösumman menetelmä) explained in the solutions.
- check_i18n.py fi-easy: no errors for fy7-16 (en run shows 1 pre-existing error in fy7-13/exercises/solutions.md, outside this task).
