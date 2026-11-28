VERDICT: PASS
CONTENT-HASH: e33eeabe0760019d

## Blocking

## Polish
- lessons/FY1/fy1-3/lesson-answers.py:38 — `inq-ice-corrected` (62,3 °C − 1,5 °C = 60,8 °C) computes a number that no lesson or inquiry text uses — delete it, or add the correction step to the ice-water data task if it was meant to be there.
- content/fi/FY1/fy1-3/inquiry.json:283,291 — exp-3 gives the smaller half-range as $0{,}0850\,\text{s}$, but the readout shows three decimals (0,085), and the solution itself says the second digit is already uncertain — write $0{,}085\,\text{s}$ in the hint and the solution.
- content/fi/FY1/fy1-3/inquiry.json:291 — exp-3 says "Hajonta on suoraan verrannollinen satunnaisvirheen suuruuteen". In the model this holds only before the readings are rounded to 0,01 s (the answer's own Järkevyys step says so) — add "mallissa ennen pyöristystä".

## Checked
- Recomputed every number in one script from the task data and the sim's G series. All match lesson-answers.py: exp-1 at n = 1/5/40 gives ero −0,22 / +0,076 / −0,0005 s and puoli 0 / 0,25 / 0,26 s; exp-2 at n = 40 gives mean 2,6995 s, ero 0,2995 s; exp-3 ratio 6,18 → 6,2; coin 5,44 g and the mistakes 5,6 / 27,2 / 4,8 / 28,0; check-2 2,08 % (mistake 4,2 %); worked example 19,09 s, 3,1817 s, 0,12 s, 3,77 % → 3,8 %; exit ticket 19,9 g and 1,99 % → 2 %; ice data mean 1,5 °C and ratio 15.
- The karkea feedback numbers are right: the mean shifts by +0,19 s, the half-range goes from 0,09 s to 0,62 s, and 3,07 s is 0,05 s below the next result.
- With the tolerances read as relative (docs/inquiry.md), the listed mistakes fall outside the accepted range, and the rounded answers (2 %, 6,2) fall inside it.
- Definitions follow the guardrails: mittausvirhe has a sign; epävarmuus is positive and not a hard limit; resoluutio is kept apart from epävarmuus; the half-range is a simple estimate of scatter and a conservative bound for the mean, not called the uncertainty of the mean; the outlier rule uses the guardrail wording. The correction $x = x_\text{lukema} - \Delta x_\text{sys}$ is consistent with the sign of the error.
- The figures that say "mittakaavassa" are to scale. error-types: means 2,406 s and 2,592 s at x = 208,5 and 342,5 (about 715 px/s). example-plot: dots at their values, and the bar covers 3,06–3,30 s.
- The zero-scale figure is right: 48,7 g − 1,2 g = 47,5 g.
- sim.js implements the stated model $t_i = T + \Delta t_\text{sys} + \Delta t_\text{sat} g_i$, rounded to 0,01 s, with a fixed series (sd 0,96, so "tyypillinen poikkeama" is fair). simState gives mean, puoli and vir. The experiments lock the right parameters (exp-1/2: sat and sys; exp-3: n and sys), and the reset defaults match.
- Each prediction, experiment, data task, mistake-spotting item and check has exactly one correct option, and each distractor's feedback is right.
- Theory, summary, model answers and exit ticket agree with each other. Scope stays within FY1 (measurement and how reliable it is).
