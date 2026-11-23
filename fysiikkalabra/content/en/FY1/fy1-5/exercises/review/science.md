VERDICT: PASS
CONTENT-HASH: 2ccd524b645fe8c9
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
- Delta s = vt, s - s0 = vt, 2d = Delta s, meeting time t = v2 t0/(v2 - v1) derived step by step correctly. (Finnish re-review after its fix pending; this verdict covers the en text as it is.)
