VERDICT: PASS
CONTENT-HASH: 0f93c41c66c174c7

## Blocking

## Polish
- lessons/FY1/fy1-3/lesson-answers.py:31,35 — the comments say "relative error" — rename to "relative uncertainty" to match the renamed term.
- lesson.md:534 (Yleinen virhekäsitys) — "satunnais- ja systemaattinen virhe kuuluvat myös taitavan mittaajan tulokseen" could read "...vaikuttavat myös taitavan mittaajan tuloksiin".
- Spelling of "virhe-arvio" and "virhearvio" varies (lesson.md, inquiry check-2 solution, exit ticket) — pick one.

## Checked
- Round 2: `git diff HEAD~2` touches only lesson.md:537. The Tiivistelmä now says "Jokaiseen mittaustulokseen liittyy epävarmuutta. Virhettä ei yleensä tunneta…", which matches Ydinajatus and the guardrail's split between error and uncertainty. The round-1 Blocking item is resolved, and the glossary entry mittausvirhe was aligned too.
- Round 1, unchanged since: I recomputed every inquiry and example number in one script, including the sim series G with rounding: exp-1 −0,22 / +0,076 / −0,0005 s, half-range 0,25–0,26 s; exp-2 0,30 s; exp-3 6,18; example 3,18 ± 0,12 s, 3,8 %; check-2 2,08 %; transfer 5,44 g; ice 1,5 / 0,1 °C; outlier 0,09 → 0,62 s; exit ticket 19,9 g and 2 %.
- The sim's model and simState keys hold, the experiments lock the right parameters, and every choice has exactly one correct option. The figure numbers agree with figures.py.
- "Suhteellinen epävarmuus" is used the same way in the theory, the example, check-2 and the exit ticket.
