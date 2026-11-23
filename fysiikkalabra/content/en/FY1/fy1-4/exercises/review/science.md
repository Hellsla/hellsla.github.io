VERDICT: PASS
CONTENT-HASH: 473bd73c289cfb43
SCOPE: delta 8g Formula-step rewrite (en), round 1

## Blocking
- none

## Polish
- none

## Checked
- Delta (work queue 8g): only the Formula steps of solutions.md changed (aligned blocks from the basic equation); every other changed line in the diff is a paragraph split or spacing, no number, sign or unit changed.
- Each new Formula block checked line by line: every equality and rearrangement is algebraically valid and leads to the formula the unchanged Substitution uses.
- Script comparison with the Finnish Kaava steps (which passed science review): same number of aligned rows, inequalities and numerals in every solution.
- answers.py and exercises.json values not in the diff; answers, units and tolerances unchanged from the passed version.
- Hash recomputed at start and end with --exercises --lang en: unchanged.
- Linear-model rearrangements (t = (h-b)/k, b = m1 - kV1, s = s1 + k(t - t1)) valid; cooling slopes compared with absolute values.
