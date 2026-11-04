VERDICT: PASS
CONTENT-HASH: 1e3ebaffa0ccf48f

Science review, round 2, of the en translation of fy9-sailymislait, 2026-11-04.

Round 1 found no Blocking science issue. Since then only three things changed: figures.json gained three heading words, and two inquiry.json strings were reworded (activities.15.hints.0, activities.18.choices.1.feedback). None of them changes a number, an answer, a tolerance, a formula or a correct flag. `check_i18n.py` reports 0 errors for this unit (the only en error is in fy9-ympyraliike). `practice.py check` is OK (6 tasks, 95 points). The round-1 number comparison and recomputation still hold. The figures still use a decimal point.

## Blocking
None.

## Polish
1. Not changed since round 1: the stopping distance is still written $s_\text{p}$ (2 times in unit.md, 12 in sovella/solutions.md, and in the s3 graph labels), while the English chapter fy4-11 uses $s_\text{stop}$. This can't be fixed through figures.json, because the key "p" would also rename $E_\text{p}$, so the figure part needs a change in figures.py. The text could change on its own, but then text and graph would disagree, so it is better left alone.
2. Not changed since round 1: the ratio colon ($|\Delta p| : \Delta t$, $\mu = a : g$) is a typography question for the whole project. See the visual report.
