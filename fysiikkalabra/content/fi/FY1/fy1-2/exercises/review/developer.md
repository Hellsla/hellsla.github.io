VERDICT: DONE

Round 1, draft: exercise bank 5/4/3 to 8/7/5 (plan P2 +3/+3/+2). Existing ids, answers and solutions unchanged except one lint fix (below).

exercises.json: added L1-06 (MC, base unit), L1-07 (km/h to m/s by substitution), L1-08 (MC, unit of density from the formula); L2-05 (data, speeds in km/h, m/s and knots, find the fastest), L2-06 (data and error, a table column with the wrong unit), L2-07 (error, pupil's formula t = qV exposed by a unit check); L3-04 (dimensional analysis of the pendulum period, then a prediction), L3-05 (data, manufacturer's kWh/MJ and W/kW, refute the claim). All have kind; MCs have 4 options each with own feedback.

solutions.md: 8 new complete solutions (MC ones Kysytty, Periaate, Mallivastaus). Touched one existing line: L2-02 Järkevyys, plain "1 mm" made maths (PLAIN_QTY error once the file counts as edited).

answers.py: new answers computed from the task data (L3-05 gives 1,54 h, answer 1,5 h with tolerance 0,03).

Checks: lint_lesson.py fy1-2 0 errors (1 old Kaava warning in L1-01); check_solutions.py fy1-2 ok.
