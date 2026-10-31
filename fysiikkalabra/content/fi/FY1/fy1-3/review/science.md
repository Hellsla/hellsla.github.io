VERDICT: FAIL
CONTENT-HASH: bdba60dae225e358

## Blocking
- content/fi/FY1/fy1-3/lesson.md:537 — (A, internal consistency) The summary still says "Virhe kuuluu jokaiseen mittaukseen.", the claim this change removed from Ydinajatus (line 282 now says "Tulos poikkeaa yleensä hieman..." and "Jokaiseen mittaustulokseen liittyy epävarmuutta"). The error of one result is unknown and can by chance be zero. What every result has is uncertainty. The summary contradicts the theory and the guardrail's split between mittausvirhe and mittausepävarmuus. — Fix: replace the sentence with "Jokaiseen mittaustulokseen liittyy epävarmuutta." (or "Tulos poikkeaa yleensä oikeasta arvosta.").

## Polish
- glossary.json "mittausvirhe" (outside this lesson's hash, but shown with its terms) — still reads "Pieni virhe kuuluu jokaiseen mittaukseen." — align it with the new wording of the theory.
- lessons/FY1/fy1-3/lesson-answers.py:31,35 — the comments say "relative error" — rename to "relative uncertainty" to match the renamed term.
- lesson.md:534 (Yleinen virhekäsitys) — "satunnais- ja systemaattinen virhe kuuluvat myös taitavan mittaajan tulokseen" — could read "...vaikuttavat myös taitavan mittaajan tuloksiin" so it matches the uncertainty wording.
- Spelling of "virhe-arvio" and "virhearvio" varies (lesson.md, inquiry check-2 solution, exit ticket) — pick one.

## Checked
- Recomputed every inquiry and worked-example number in one script with my own formulas, including the sim's fixed series G with rounding: exp-1 n=1 −0,22 s, n=5 +0,076 s, n=40 −0,0005 s, half-range 0,25–0,26 s; exp-2 2,6995 s → 0,30 s; exp-3 0,525/0,085 = 6,18; example 3,18 ± 0,12 s, 3,8 %; check-2 2,08 %; transfer 5,44 g and every listed mistake value; ice data 1,5 °C / 0,1 °C; outlier task 0,09 → 0,62 s, shift 0,19 s; exit ticket 19,9 g and 2 %.
- Relative tolerances accept the rounded answers the solutions give (check-2: "2" lies within 5 % of 2,1).
- sim.js and simState implement t_i = T + Δt_sys + Δt_sat·g_i; the measured keys mean/puoli/vir exist; each experiment locks the right parameters.
- Every choice has exactly one correct option, and its feedback is right. Term use (error, uncertainty, resolution, half-range as a cautious estimate) follows the guardrails, and so do the outlier wording and the resolution vs hand-timing point.
- The renamed term "suhteellinen epävarmuus" is used the same way in the theory, the example, check-2 and the exit ticket.
- Figure numbers (means 2,407 / 2,594 s, offset 0,19 s; scale 1,2 g → 47,5 g) agree with figures.py.
