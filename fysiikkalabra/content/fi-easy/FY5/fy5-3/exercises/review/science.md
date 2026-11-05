VERDICT: PASS
CONTENT-HASH: f83462eeec7a31b4
Mode: full (translation review against the reviewed Finnish set)
Round 1

## Blocking
(none)

## Fixed
- solutions.md L1-07 Answer line: removed a redundant second sentence repeating "two significant figures" (kept the meaning of the Finnish).

## Polish
(none)

## Checked
- Script comparison of exercises.json with content/fi: ids, levels, kinds, answers, units, tolerances, correct flags, choices, data cells and every number in texts, choices and feedback are identical (decimal point in JSON/LaTeX where fi has comma where relevant).
- solutions.md: 770 numbers each, sequence equal to fi; formulas and substitutions unchanged.
- New tasks L1-06..08, L2-05..07, L3-04..05: physics (tangent velocity, T=1/f, v=2πr/T, mean of 5 timings, satellite speeds, r=R cosφ, CD groove) matches fi; re-derived answers 0.020 s, 0.21 mm/s, 3.2 m/s, 3.07 km/s, 16 m/s, 250 m/s, 75 min.
- Terms: plain Finnish (selkosuomi): short sentences, terms explained (kierrosaika, pyörimistaajuus, ratanopeus), numbers with decimal comma in text and {,} in LaTeX as in fi.
- check_i18n.py fi-easy: 0 errors.
