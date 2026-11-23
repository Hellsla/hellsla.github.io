VERDICT: PASS
CONTENT-HASH: 3771cf2b226387d4

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
- rho = m/V rearrangements, equal-mass ratio, mean density, wire length L = m/(rho pi r^2), two-metal mixture V_Cu = (m - rho_Al V)/(rho_Cu - rho_Al) all valid.
