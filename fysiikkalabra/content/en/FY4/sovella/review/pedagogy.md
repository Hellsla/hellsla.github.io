VERDICT: PASS
CONTENT-HASH: ec85c073c6b06f71

## Blocking
None.

## Polish
- fy4-s1 b: the part is kind "word" but asks for a drawn diagram. Fine for self-assessment, but the criteria "detail" could say what to compare (a diagram may be drawn on paper).
- fy4-s1 part c: the part c task text says "Determine the coefficient of sliding friction". Since the term change was the task, the term is correct and consistent in tasks, solutions and figure description (sliding friction, F_mu, "liukukitka" in the Finnish alt text). No "kinetic friction" remains; the remaining "kinetic" hits are all kinetic energy.
- fy4-s2 d: criterion 3 (assumptions) and 4 (conclusion) accept two different design values; good, but the model answer could say outright that the 17.2 m/s value is the safe upper bound.

## Checked
- Term change 8m: grepped tasks.json, solutions.md, figures.json and figures.py for kinetic friction/kineettinen/liukukitka; only sliding friction (EN) and liukukitka (FI) appear, and the Finnish alt text matches the English.
- Independent application: s1 (real-feeling measurement data, two tables, graph, fbd, model fit, systematic error from air resistance), s2 (zip line, choice between energy conservation and work-energy, compare two instructors' models), s3 (collision plus sliding, momentum and friction chained, police report to interpret). No heading or prompt names the model or formula; the model choice is itself rewarded (transfer criteria).
- Rising demand within each task (a to d/e), 3 tasks, varied contexts (data analysis, energy, momentum); workload fits a 2 op course (about an hour each, slightly heavy for s1 with its five parts).
- Rubrics: points sum per part, criteria observable, no points for irrelevant things; unit and precision criteria fit data precision.
- Solutions: full, with the diagram before equations in s1 c, reasonableness checks, accepted alternatives, and real common mistakes (mu = a/g on a slope, N = mg, forward force, double counting components, energy conserved in the inelastic collision).
- Force-diagram plan: s1 b is a draw-alone task, with fbd criteria and no forward force given away.
- Coverage docs/coverage/FY4.md: no gaps listed ("–" in every row); tasks are named in each competence row.
- Hash recomputed with --lang en equals the packet hash.
