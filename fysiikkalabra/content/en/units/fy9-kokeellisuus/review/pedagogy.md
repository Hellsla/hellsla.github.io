VERDICT: FAIL
CONTENT-HASH: f655c7b7e62ba973

Delta review (solution practice, 2026-11-12) of the version passed before.

BLOCKING 1: sovella/tasks.json s5 part a, criterion units_precision (line ~495, all three languages) still reads 'rho approx 2680 kg/m3', while solutions.md now answers 2,7e3 kg/m3 (two significant figures; 2680 only as the uncertainty-form in b). Rubric and model solution contradict. Fix: change the detail to 'rho approx 2,7e3 kg/m3 (2677 calculated), two significant figures because V = 70 cm3; 2680 accepted'. The numeric answer 2680 +-2 % still admits 2700. The other changes (unrounded a = 4,1667, force components in s6 c) are good. Same finding in en (tasks.json line 495).

Checked: diff since 761b6673, symbols defined, solved expression equals Sijoitus, answers.py output, tasks.json answer/criteria, cross-language number match.
