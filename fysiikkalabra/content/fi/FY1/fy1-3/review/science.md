VERDICT: PASS
CONTENT-HASH: 25b3b9bd9015b47f

## Blocking

## Polish
- inquiry.json exp-2 solution (Annettu) — it reads the n = 40 mean as $2{,}70\,\text{s}$. The model gives $2{,}6995\,\text{s}$, and the readout shows three decimals, so the student's table may show $2{,}699$ or $2{,}700$. Either is inside the tolerance, but the solution could say "noin $2{,}70\,\text{s}$" — optional.
- lesson.md Esimerkki, Sijoitus — the intermediate $\bar{t} = 3{,}1817\,\text{s}$ is labelled with "=". "$\approx$" would be more exact — optional.

## Checked
- Round 2 blocker fixed in fi, en and fi-easy: check-2 answer "$2\,\%$, one significant figure like the error estimate $0{,}05\,\text{s}$". This matches the rounding rule (lesson.md Kaava, Tiivistelmä) and the worked example. Tolerance 0.1 accepts a typed 2. The mistake values 4.2, 0.05 and 0.021 stay outside it.
- Recomputed in one python call, using my own model of the sim. exp-1: n = 1 gives a difference of $-0{,}22\,\text{s}$, n = 40 gives $-0{,}0005\,\text{s}$, and the half range is about $0{,}25$–$0{,}26\,\text{s}$. exp-2: n = 40 gives $0{,}2995\,\text{s}$. exp-3: $0{,}525/0{,}085 = 6{,}18$, inside 6.2 ± 0.03. siirto: $5{,}44\,\text{g}$, and the mistakes 5.6, 27.2, 4.8 and 28 are distinct. Worked example: $19{,}09\,\text{s}$, $3{,}18\,\text{s}$, $0{,}12\,\text{s}$, $3{,}8\,\%$. Exit ticket: $19{,}9\,\text{g}$, and $1{,}99\,\% \to 2\,\%$. Ice data: mean $1{,}5$, half range $0{,}1$. The hook times match the sim series. lesson-answers.py agrees with all of these.
- Gross-error item: the half range goes from $0{,}09\,\text{s}$ to $0{,}62\,\text{s}$ and the mean shifts by about $0{,}2\,\text{s}$, both correct. Outlier handling follows the guardrail wording: check the result, leave it out only for a found cause, and write the cause down.
- The sim.js reading $t_i = T + \Delta t_\text{sys} + \Delta t_\text{sat} g_i$, rounded to $0{,}01\,\text{s}$, is the same model as the "Mallin oletukset" box and lesson-answers.py. Each experiment locks the right parameters and varies only one.
- Figures are drawn to scale. error-types: means $2{,}41\,\text{s}$ and $2{,}59\,\text{s}$. example-plot: the dots, the mean $3{,}18\,\text{s}$ and the bar $\pm 0{,}12\,\text{s}$ match the data. range-half: the mean marker is at the mean of the dots.
- Terms follow the guardrails: mittausvirhe (with its sign) vs mittausepävarmuus (positive, not a hard limit) vs resoluutio. Half the range is called an estimate of the scatter and a cautious estimate for the mean, never the uncertainty of the mean. Repetition reduces only random error. Scale reading uses the half-division wording with the total-uncertainty caveat.
- check-c2: the right option ($\sim 0{,}2\,\text{s}$, from reaction time) is the only correct one. Each distractor's feedback says why it is wrong.
- data, check-1 and virhe: exactly one correct option each. The systematic-error reasoning (shown only by comparing with a reference) is consistent across the theory, the conclusion model answer, check-3 and the exit ticket.
- Captions: the LIGO sensitivity (far below the size of a nucleus) and the caliper (fractions of a millimetre) are correct.
- Content hash 25b3b9bd9015b47f, the same at the start and at the end.
