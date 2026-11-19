VERDICT: FAIL
CONTENT-HASH: 01c407c00c981925

## Blocking
- content/fi-easy/FY1/fy1-3/inquiry.json:545 (check-2 solution, **Vastaus**) — A: "$2{,}1\,\%$. Siinä on kaksi merkitsevää numeroa, koska lähtöarvoissa on kolme" gives the wrong limiting datum and breaks the lesson's own rounding rule. The relative uncertainty is limited by the virhearvio $\Delta t = 0{,}05\,\text{s}$, not by the five measured times; the subtraction $2{,}46\,\text{s} - 2{,}36\,\text{s} = 0{,}10\,\text{s}$ already keeps only two figures, so "three in the data" does not hold. The lesson rounds a virhearvio to one significant figure (two if the first digit is 1) (lesson.md:454, :586), and its worked example gives the relative uncertainty with as many figures as the virhearvio (lesson.md:544: "$3{,}8\,\%$ … kaksi merkitsevää numeroa, kuten virhearviossa"). With $\Delta t = 0{,}05\,\text{s}$ that gives $2\,\%$, as in the version I passed. The Finnish version has the same sentence and its science review fails it on the same grounds. — fix: restore "$2\,\%$. Siinä on yksi merkitsevä numero, kuten virhearviossa $0{,}05\,\text{s}$ (laskimen arvo $2{,}08\,\%$)." If the change was made because the answer check rejects a typed 2 (`answer` 2.08, `tolerance` 0.05), widen the tolerance (for example 0.1) instead of changing the rounding reason; keep fi, en and fi-easy the same.

## Polish
- inquiry.json:545 — if $2{,}1\,\%$ is wanted on purpose, write the virhearvio as $0{,}050\,\text{s}$ (from $0{,}10\,\text{s}/2$), give that as the reason and state the exception next to the rule at lesson.md:454; a larger change than the fix above.

## Checked
- Hash 01c407c00c981925 at the start and the end.
- Recomputed: mean $12{,}00\,\text{s}/5 = 2{,}40\,\text{s}$, $\Delta t = 0{,}05\,\text{s}$, $\varepsilon = 2{,}083\,\%$; lesson-answers.py `inq-check2` = 2,08 matches the key 2.08 (its comment still says "shown answer 2 %").
- The diff changes only the Vastaus sentence; Annettu, Periaate, Kaava, Sijoitus and Järkevyys unchanged and correct.
- Rounding rule lesson.md:454/586 and worked example lesson.md:544 compared with the new sentence: they disagree (above).
- Mistake values 4,2 / 0,05 / 0,021 and their feedback still correct.
