VERDICT: FAIL
CONTENT-HASH: 8499e7663496ab66

## Blocking
- inquiry.json:545 (task "3. Laskeminen", solution, Vastaus) — the stated reason for the rounding is wrong and contradicts the lesson's own rule. "kaksi merkitsevää numeroa, koska lähtöarvoissa on kolme" does not follow (three-figure data would give three figures, 2,08 %, or the rule would give the error estimate's figures), and lesson.md:454, 544 and 586 teach that the uncertainty is given with the figures of the error estimate (here 0,05 s has one: 2 %; in the worked example 0,12 s has two: 3,8 %). Rule 7(6) asks for the reason for the number of figures, and a student who cannot solve the task reads a false one. Fix: "**Vastaus:** $2{,}1\,\text{\%}$ (laskimen arvo $2{,}08\,\%$). Suhteellinen epävarmuus on karkea arvio, joten kaksi merkitsevää numeroa riittää; myös $2\,\%$ on oikein, koska virhearvio $0{,}05\,\text{s}$ on yhden numeron arvio." (Keep `answer` 2.08 and tolerance 0.05, which accept 2,1 but not 2; or raise the tolerance to 0.1 so that 2 % is accepted as the text says.) Write units as $2{,}1\,\%$ in LaTeX.

## Polish
- inquiry.json:545 — the earlier version (2 %) matched the lesson's rule but failed the checker's tolerance (|2 - 2,08| > 0,05); the real inconsistency is rule vs tolerance. Align the two, as in the fix above, instead of changing the reason.

## Checked
- Diff is one line: the Vastaus of the numeric task changed from 2 % to 2,1 %; Annettu, Periaate, Kaava, Sijoitus, Järkevyys unchanged and consistent (mean 2,40 s, Δt 0,05 s, 2,08 %).
- Prompt, hints and mistake feedback (4,2; 0,05; 0,021) still fit the answer 2,08.
- Worked example's rounding rule (lesson.md:454, 544) read for consistency with the new line; this is the conflict above.
- Rest of the lesson not re-judged; the earlier PASS holds for it.
