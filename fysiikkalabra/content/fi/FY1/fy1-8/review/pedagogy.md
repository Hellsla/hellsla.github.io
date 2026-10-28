VERDICT: PASS
CONTENT-HASH: 623e9eb862db9978

## Blocking
- none.

## Polish
- inquiry.json ennuste-1 — the option feedback quotes the pöytäkirja ("kohta Tutki": $0{,}39$ and $0{,}42\,\text{m/s}$) that the student has not yet opened, and the prediction has no `reveal` after the table task. The correct option can be argued from the hook alone (20 %), so it is a fair prediction, but add `"reveal": {"after": "poytakirja-kysymys"}` or move the table numbers out of the feedback so the evidence stays in the Tutki stage.
- lesson.md Kaava — "Epävarmuuden $\Delta t = 0{,}2\,\text{s}$ ja rajan $5\,\%$ yhdistelmällä aikaa pitää olla vähintään $4\,\text{s}$" is clumsy. Write: "Kun $\Delta t = 0{,}2\,\text{s}$ ja raja on $5\,\%$, aikaa pitää mitata vähintään $4\,\text{s}$."
- lesson.md Muuttujat — "mitattava muuttuja: … tässä aika $t$" and "muutettava … tässä matka $s$" is right for this experiment, but a student will have learned that the changed quantity goes on the horizontal axis; the graafi task explains the exception, so add a pointer here ("kuvaajassa aika on silti vaaka-akselilla, ks. kohta Tutki") to avoid the surprise.
- inquiry.json suunnittele — one task asks for question, hypothesis, three variable types, range, repeats and the log in a single prompt; split the prompt into a numbered list (the model answer already follows that order).
- exit-ticket / tarkistus-2 — $\varepsilon$ is defined in the lesson as $\Delta t : t$ without $\cdot 100\,\%$, but the check and the Kaava text give it in percent; one half-sentence in Kaava ("kerrottuna sadalla prosentteina") would make both consistent.

## Checked
- Hand-checked: table rows ($\bar{t}$, $\Delta t$, $\varepsilon$, $v$) for all five distances; $t_\text{min} = 4\,\text{s}$, $s_\text{min} = 1{,}68\,\text{m} \to 1{,}7\,\text{m}$; Etsi virhe $2{,}4\,\text{m}$; siirto $14\,\text{m}$; kertaus $4{,}74 \pm 0{,}15\,\text{s}$; tarkistus-2 $2{,}0\,\%$, whose solution's "2 %" also passes the answer check.
- Opening question is answered: A's $1{,}0\,\text{s}$ has $20\,\%$ uncertainty, B's longer times have $3\,\%$; the Tutki tasks and the example use the same rule.
- Activities fit the topic (no simulation needed): data from a log, a graph with error bars, a fair-test judgement, a planning task with model answer and the real investigation ("tee-itse").
- Example has seven stages, symbolic first; Järkevyys cross-checks with $\varepsilon \approx 4{,}9\,\%$ and the bad $0{,}50\,\text{m}$ choice.
- Choice items have exactly one correct option; mistakes ($2{,}4$, $2{,}1$, $0{,}14$, $10$, $4{,}0$, $0{,}02$) are real slips with repairing feedback.
- Hypothesis wording ("tukea, ei todistettu") and the tarkistus-3 task teach the right strength of conclusion; glossary terms consistent; Finnish correct.
- Workload on the upper edge (optional items carry it); figure captures were not present, so figure legibility was not judged visually.
- Hash unchanged at the end.
