VERDICT: PASS
CONTENT-HASH: bfb82ec10be5d89c
SCOPE: delta 8g Formula-step rewrite (en), round 1

## Blocking
- none

## Polish
- content/en/FY1/fy1-6/exercises/solutions.md:109 (fy1-6-L3-02) — the new block stops at t2 = v2/g with g still numeric; the passed version simplified to t2 = v2 t1/v1 (house rule: simplify symbolically to the end) — add the row t2 = v2 t1/v1, same in Finnish.

## Checked
- Delta (work queue 8g): only the Formula steps of solutions.md changed (aligned blocks from the basic equation); every other changed line in the diff is a paragraph split or spacing, no number, sign or unit changed.
- Each new Formula block checked line by line: every equality and rearrangement is algebraically valid and leads to the formula the unchanged Substitution uses.
- Script comparison with the Finnish Kaava steps (which passed science review): same number of aligned rows, inequalities and numerals in every solution.
- answers.py and exercises.json values not in the diff; answers, units and tolerances unchanged from the passed version.
- Hash recomputed at start and end with --exercises --lang en: unchanged.
- g = Delta v/Delta t = v/t used only in tasks whose Given says the object starts from rest (checked L1-01..05, L3-05 and the Moon hammer); L3-04 keeps v = gt valid only for time from the start of the fall.
- (Finnish re-review after its fix pending; this verdict covers the en text as it is.)
