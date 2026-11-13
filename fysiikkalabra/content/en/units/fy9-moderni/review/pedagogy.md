VERDICT: PASS
CONTENT-HASH: 2b347105827eead3
Delta review (merge of #523 solution practice into #522, 2026-11-13) of the version passed at 4a4554bfe169b358.

## Blocking
(none)

## Polish
- Task s5 part a: the solution plots $(t, \ln N)$ and reads the endpoints of a fitted line (0; 5.993) and (300 s; 4.635), but there is no worked graph of it, unlike the other graph tasks of the unit. A small figure with all 11 points and the line would let the student check their own plot.
- The bullet "- in part a the two-endpoint calculation ..." under Hyväksytään myös starts in lower case, unlike its neighbours.
- $E_0 = 13.6\,\text{eV}$ in s2 is a good change; no remarks.

## Checked
The changed s5 method (fit of $\ln N$ against $t$, $T_{1/2} = 153\,\text{s}$) against tasks.json (answer 153, tolerance, criteria, accepted 151, range 147-159 s), part b ("about 153 s") and the source note (generated with 153 s): consistent. The method fits the course (decay law, linearisation) and uses all 11 points, a better lesson than the two endpoints. Other hunks: $E_0$, $H_\text{a}$, $m_\text{a}$, $m_\text{U}$, work function $W = -eb$, $f_0 = -b/k$.
Read the diff hunks of this unit for how #522 notation and #523 symbolic-first solutions interact: no symbol used with two meanings inside one solution, no duplicated derivation, no contradiction with the unit text, LaTeX balanced, the answer lines still match the substitutions, and the formula still precedes the numbers (CLAUDE.md Lesson form 7). Staging of the worked solutions (Given, Find, Principle, Formula, Conversions, Substitution, Answer, Reasonableness) is intact.
