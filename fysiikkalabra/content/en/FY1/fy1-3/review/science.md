VERDICT: PASS
CONTENT-HASH: 97e76b1902e96d98

## Blocking

## Polish
- content/en/FY1/fy1-3/inquiry.json:exp-2 solution (Answer) — "two decimal places like the mean in the table": the sim readout and table show the mean to three decimals ($2.700\,\text{s}$ at $n = 40$, model $2.6995\,\text{s}$). Say "like the true time and the readings", or quote the mean as the table shows it.
- content/en/FY1/fy1-3/lesson.md:505 and Summary — "for the mean $\Delta x$ is a cautious estimate" is correct (C), but it stays close to the guardrail "never call half the range the uncertainty of the mean". Keep the wording "cautious (too large) estimate" and do not shorten it to "the uncertainty of the mean".

## Checked
- Round-2 finding fixed: check-2 Answer is back to "$2\,\%$, one significant figure like the error estimate $0.05\,\text{s}$ (calculator value $2.08\,\%$)". Relative tolerance 0.1 accepts 2, 2.1 and 2.08 and rejects the listed mistakes 4.2, 0.05 and 0.021.
- Recomputed in one python run from the sim's G series: hook readings 2.18/2.45/2.68/2.67/2.40 s; exp-1 n=1 difference −0.22 s, n=40 difference −0.0005 s, half range 0.25 s (n=5) and 0.26 s (n=40); exp-2 n=40 mean 2.6995 s, so the difference is 0.30 s; exp-3 0.525/0.085 = 6.18, tolerance 0.03 rejects the mistake 6.
- Worked example: 19.09 s, 3.18 s ± 0.12 s, 3.77 % → 3.8 %. The interval 3.06–3.30 s holds five of the six results.
- karkea: 4.31 s moves the mean by +0.19 s and the half range goes from 0.09 to 0.62 s, as its feedback says.
- siirto: 5.44 g; the mistake values 5.6, 27.2, 4.8 and 28 are correct and their feedback is right.
- Exit ticket: 19.9 g, Δm = 0.1 g, 0.09/4.52 = 1.99 % ≈ 2 %. Thermometer data: mean 1.5 °C, half range 0.1 °C, a ratio of 15.
- The terms (measurement error with a sign, uncertainty positive and not a strict limit, resolution vs uncertainty, rule for gross errors and outliers, half range as a scatter estimate) match the guardrails.
- Systematic error: $\Delta x_\text{sys} = \bar{x}_\text{ref} - x_\text{true}$ and $x = x_\text{reading} - \Delta x_\text{sys}$ have the right sign. The zero-scale figure shows 48.7 − 1.2 = 47.5 g.
- sim.js uses the model the model box gives: reading rounded to 0.01 s, fixed series. lesson-answers.py matches it.
- Each experiment's locked and varied parameters isolate one variable. Exactly one option is correct in every choice item.
- Content hash 97e76b1902e96d98 at the start and at the end.
