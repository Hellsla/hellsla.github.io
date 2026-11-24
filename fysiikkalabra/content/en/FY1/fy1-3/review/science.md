VERDICT: PASS
CONTENT-HASH: 6b5fc5bd9373a765

## Blocking

## Polish
- lesson.md:180 — `x = x_reading − Δx_sys` works only when the error at the measured value is the same as at the reference (a constant offset). The definition of systematic error ("almost the same in direction and size") covers this, so it is a fair simplification (C), but a short clause would stop a student from correcting, say, a 60 °C reading with an ice-point offset alone — add "when the error is the same size over the whole range" or similar.
- lessons/FY1/fy1-3/lesson-answers.py:989 — `inq-ice-corrected` (62,3 °C − 1,5 °C = 60,8 °C) matches no number in lesson.md, inquiry.json or exit-ticket.json; remove it or use it.
- assets/sims/fy1/fy1-3/sim.js:1040 — `tx()` always writes a decimal comma, so the English page shows `2,18 s`, `0,15 s`, `1,6` while the English text uses points (screenshot fy1-3-sim-390.png); decide the separator from the page language.
- inquiry.json exp-3 solution/hint — quotes `0.0850 s` (four figures) while the readout shows three decimals (`0.085`); quote the value as the table shows it.
- lesson.md:283 — "a cautious uncertainty estimate for the mean" is correct as worded, and the Formula section explains it (half the range describes individual results; the mean's uncertainty is smaller). Keep that explanation next to it so the summary is never read on its own as "the uncertainty of the mean" (guardrail).

## Checked
- I recomputed every number in one script with my own formulas: worked example (19,09 s; 3,1817 s; 0,12 s; 3,77 % → 3,8 %; 5 of 6 results in 3,06–3,30 s), pysähdy (0,2 s), siirto 5,44 g and the mistakes 5,6 / 27,2 / 4,8 / 28, check-2 2,083 % (mistake 4,17 %), exit ticket (19,9 g; 0,1 g; 1,99 %), ice data (1,5 °C; 0,1 °C; ratio 15), gross error (mean shift 0,19 s; half-range 0,09 → 0,62 s, ×6,9). All agree, and so does lesson-answers.py.
- Simulation with its fixed series: exp-1 n = 1 gives −0,22 s, n = 40 gives −0,0005 s, and the half-range is 0,25/0,26 s at n = 5, 10 and 40; exp-2 n = 40 gives a mean of 2,6995 s (0,2995 s); exp-3 gives 0,085 and 0,525 s (ratio 6,18). The ratio is exactly 6 before rounding, so the feedback blaming rounding is right. The hook times are the sim's first readings.
- Experiments: setups isolate the varied parameter; slider steps reach 0,05/0,15/0,30 and +0,30; simState has `mean`, `puoli`, `vir`.
- Each choice item has exactly one correct option; every distractor's feedback is correct.
- Figures: "error-types" is to scale (true value 2,40 s, means 2,41 s and 2,59 s, Δt_sys ≈ 0,19 s); example-plot points, mean and the 3,06–3,30 s bar are at the right places; range-half bar = mean ± half-range; zero-scale 48,7 − 1,2 = 47,5 g.
- Terms follow the guardrails: error vs uncertainty vs resolution, how outliers are handled, the scale-reading wording, and hand timing at about 0,2 s.
- Scope: within FY1's measurement and reliability content; nothing from later courses.
- Sim model box states the model, that the values are model values and the reading rounding; Δt_ran is the per-reading standard deviation, consistent with half-range > Δt_ran.
