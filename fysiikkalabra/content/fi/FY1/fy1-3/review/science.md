VERDICT: FAIL
CONTENT-HASH: 8499e7663496ab66

## Blocking
- content/fi/FY1/fy1-3/inquiry.json:545 (check-2 solution, **Vastaus**); the same sentence in content/en/FY1/fy1-3/inquiry.json and content/fi-easy/FY1/fy1-3/inquiry.json — A: the new answer "$2{,}1\,\%$, kaksi merkitsevää numeroa, koska lähtöarvoissa on kolme" gives the wrong reason and breaks the lesson's own rounding rule. The limiting value is the virhearvio $\Delta t = 0{,}05\,\text{s}$, not the five times. The subtraction $2{,}46\,\text{s} - 2{,}36\,\text{s} = 0{,}10\,\text{s}$ already keeps only two figures, so "three in the data" does not hold. The lesson rounds an uncertainty to one significant figure (two if the first digit is 1) (lesson.md:454, :586), and in the worked example it gives the relative uncertainty with as many figures as the virhearvio (lesson.md:544: "$3{,}8\,\%$, kaksi merkitsevää numeroa kuten virhearviossa"). With $\Delta t = 0{,}05\,\text{s}$ that gives $2\,\%$, which is what the version I passed said. — fix: go back to "$2\,\%$, yksi merkitsevä numero kuten virhearviossa $0{,}05\,\text{s}$ (laskimen arvo $2{,}08\,\%$)" in all three languages. If the reason for the change was that the answer check rejects 2 (`answer` 2.08, `tolerance` 0.05), widen the tolerance so that a typed $2$ counts as right (for example 0.1). Do not change the rounding rule in the solution to fit the check.

## Polish
- inquiry.json check-2: if $2{,}1\,\%$ is wanted on purpose, write the virhearvio as $0{,}050\,\text{s}$ (from $0{,}10\,\text{s}/2$) and give that as the reason, and state the exception to the rule on lesson.md:454. That is a larger change than the fix above.

## Checked
- Hash 8499e7663496ab66, the same at the start and the end.
- Recomputed: mean $12{,}00/5 = 2{,}40\,\text{s}$, $\Delta t = 0{,}05\,\text{s}$, $\varepsilon = 2{,}083\,\%$; lesson-answers.py `inq-check2` = 2,08, matching the key 2.08.
- The diff changes only the Vastaus sentence; Annettu, Periaate, Kaava, Sijoitus and Järkevyys are unchanged and correct.
- Rounding rule on lesson.md:454/586 and worked example lesson.md:544 compared with the new sentence: they disagree (above).
- Mistake values 4,2 / 0,05 / 0,021 and their feedback are still correct.
