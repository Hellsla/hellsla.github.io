VERDICT: PASS
CONTENT-HASH: 623e9eb862db9978

## Blocking

## Polish
- inquiry.json:22 kertaus — the correct option reports the mean as "4,74 s ± 0,15 s" with half the range "epävarmuuden yksinkertaisena arviona". The guardrail treats half the range as an estimate of the scatter, not the uncertainty of the mean. tarkistus-2 (line 289) already adds "Keskiarvon oma epävarmuus on yleensä tätä pienempi"; one such clause in this feedback would make the two items consistent.
- lesson.md:6 — "väite pätee vasta, kun sitä on testattu" says that testing makes a claim true. "väite hyväksytään vasta, kun …" says what is meant.
- inquiry.json graafi — the line through the origin is justified (the clock starts at the start line). A free fit of the five means gives a slope of 0,431 m/s and an intercept of −0,05 m, which is consistent with hand-timing offsets. This is optional: one sentence in the solution saying that the origin constraint is a model choice.

## Checked
- One-script recomputation: record table (means 1,27/2,47/3,60/4,73/5,93 s, half-ranges 0,15/0,15/0,10/0,15/0,15 s, ε 12/6,1/2,8/3,2/2,5 %, v 0,39/0,41/0,42/0,42/0,42 m/s); hook 0,50 and 0,42 m/s; kertaus mean 4,74 s and half-range 0,15 s; worked example t_min 4 s, s_min 1,68 → 1,7 m, check 4,05 s → 4,9 %, 0,50 m → 17 %; virhe 0,024 vs 2,4 m; siirto 10 s → 14 m (mistakes 0,14 and 10); graafi 2,1/5,0 = 0,42 m/s (mistakes 2,4 and 2,1); tarkistus-2 2,0 %; exit 10 s. All agree.
- Least-squares slope through the origin is 0,419 m/s, which matches the drawn line (slope 0,419) and the read point (5,0 s; 2,1 m).
- Figures to scale: the setup's 2,00 m span is 300 px at 150 px/m; the ε(t) curve passes through 20 % at 1 s, 5 % at 4 s and 2 % at 10 s; the graafi points and ±Δt bars sit at the table values.
- ennuste-1 feedbacks are right: A 0,50 ± 0,10 m/s contains B's 0,42 m/s, and B's spread is about ±0,01 m/s. Each choice item has exactly one correct option.
- Variable roles (muutettava s, mitattava t, s still on the vertical axis for the slope) are consistent across the theory, figure, graafi text and exit ticket.
- Outlier handling and "tukea, ei todistettu" follow the guardrail wordings (theory, misconception, exit ticket 3, tarkistus-3).
- The suunnittele model answer names rolling resistance and the 4 s / 1,6 m minimum correctly.
- Hash identical at start and end.
