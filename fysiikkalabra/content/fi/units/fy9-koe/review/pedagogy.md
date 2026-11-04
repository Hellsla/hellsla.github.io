VERDICT: PASS
CONTENT-HASH: 8cf0da264f14bed3

Delta review of (1) the course rename FY12 → FY9 and (2) the exam-structure text the teacher confirmed on 4.11.2026 (unit.md "Sähköinen koe" and "Ajankäyttö ja tehtävien valinta", teacher.md "Kokeen tiedot"), commit 3052d352, plus the small fixes I made during this review (listed below). Previous all-PASS hash: 210723c3675594ef.

Rename: every other file of `content/fi/units/fy9-koe/` and `lessons/units/fy9-koe/` (review/ excluded) at 3052d352 equals its 47782fdd version with `fy12`→`fy9` and `FY12`→`FY9` replaced, and nothing else. No `fy12` remains in the sources or the preview.

Fixes made in this review:
- unit.md, Osa III: "kehität siitä päätelmiä" → "teet siitä päätelmiä" (natural Finnish).
- unit.md, Ajankäyttö: "Jos voit valita, valitse tehtävät, joiden …" → "Osissa II ja III valitset tehtävät itse: valitse ne, joiden …" (the conditional contradicted the now-stated structure, where choosing is always part of Osat II and III).
- unit.md, Ajankäyttö: "Jaa aika tehtävien pisteiden suhteen" → "Jaa aika suunnilleen tehtävien pisteiden mukaan" ("suhteen" was wrong; the budget that follows is not strictly proportional, 3 / 2,3 / 2,75 min per point, so "suunnilleen").
- teacher.md, Kokeen tiedot: "6 h" → "$6\,\text{h}$".

## Blocking

None.

## Polish

1. sovella/tasks.json: the four example tasks are worth 15, 16, 14 and 16 p. Now that the page says Osa II tasks are 15 p and Osa III tasks 20 p, giving s1 and s3 15 p (Osa II type) and s2 and s4 20 p (data / design, Osa III type), and saying so in the intro, would tie the examples to the exam structure. Within the brief's 12–20 p range, so not Blocking.
2. inquiry.json Tutki: the practice item is marked "(6 p.)"; fine as a sub-part, but a learner may now compare it with the 15/20 p tasks. Optional: "**Tehtävän kohta (6 p.)**".
3. (Carried over) earlier Polish items (Esimerkki stage labels) still apply.

## Checked

- Consistency: no sentence in unit.md, inquiry.json, exit-ticket.json, tasks.json, solutions.md or teacher.md still says the page gives no exam numbers; the only conditional ("Jos voit valita") was fixed. teacher.md's 75-minute plan and the kertaustesti workload are unchanged.
- The structure text is learner-facing and actionable: what each Osa asks (Osa I mixed short items, Osa II compare/assess/apply, Osa III data), how many to choose, and a time budget that adds up. It keeps the advice to check the current rules from YTL, and teacher.md dates the confirmation (4.11.2026).
- Course mentions read "FY9"; chapter links are named, never ids, and resolve.

## Shared issues

None.
