VERDICT: PASS
CONTENT-HASH: 1eceddd9c27ef416
SCOPE: delta added-exercise from d7be126d63bbf8b3 base 81db4a6fd727

## Blocking
- none

## Polish
- none

## Checked
- Added task fy1-2-L1-10 only; hash (--exercises --lang en) 1eceddd9c27ef416 at start and end.
- Table value 384 400 km (MAFY Aurinkokunta, mean centre-to-centre distance) correct; c = 2.998·10^8 m/s given in the task.
- t = s/c for a signal at constant speed c in vacuum; km → m conversion right; solved symbolically before substitution.
- Independent recompute 1.28219 s → 1.28 s = answers.py 1.28 = exercises.json answer; unit s.
- Three significant figures now justified in the solution by the mean, centre-to-centre distance (previous Polish item resolved); surface to surface gives 1.255 s, inside the ±4 % tolerance (1.229–1.331 s).
- Tolerance 0.04 fits a table lookup and a student rounding to three figures.
- Reasonableness check (4·10^8 m over 3·10^8 m/s, a little over 1 s) is a real check.
- Inside FY1 scope (s = vt with c); no guardrail issue.
