VERDICT: DONE

exercises.json (fi, fi-easy, en): L1-10 replaced by a MAFY lookup of the heating value of petrol, E = Hm, m = 2,0 kg, answer 86 MJ, tolerance 0,04, lookup MAFY kept, id kept, no "isolated" wording. L2-08: story changed from skater to sledge (figure kept), "prosentin tarkkuudella" added.
solutions.md (fi, fi-easy, en): new complete L1-10 solution (H = 43 MJ/kg, source named, tolerance for table differences, quantities as LaTeX). L2-08: sledge wording, "half-way" reasoning removed (per the coordinator's addition only the sum check 600 J + 100 J = 700 J remains, so the C comparison went too), rounding justified as whole percents from readings to 100 J.
lessons/FY2/fy2-1/answers.py: L1-10 = 43 * 2.0 = 86.

Not fixable here: the figure fy2-1/kitka-pylvaat is still drawn and described as a skater in a half-pipe; the task text now speaks of a sledge and points A, B, C.
Checks: lint_lesson 0 errors, check_solutions ok, check_lesson all ok.
