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

1. (Carried over) inquiry.json testi-20 third distractor: optional "…jos käämissä kulkisi tasavirta paristosta".

## Checked

- Structure arithmetic: 1 + 7 + 3 = 11 tasks; 1 + 4 + 2 = 7 answered; 20 + 4 · 15 + 2 · 20 = 120 p. The unit.md list, the "Yhteensä 120 pistettä" sentence and teacher.md agree.
- Time budget: 6 h = 360 min; 360 − 50 = 310 min; 60 + 4 · 35 + 2 · 55 = 60 + 140 + 110 = 310 min. Consistent. Strict proportionality would give 310 : 120 ≈ 2,6 min/p, i.e. about 52 / 39 / 52 min; the chosen 60 / 35 / 55 is a reasonable rounding that favours the many short items of Osa I and the data work of Osa III, and the text now says "suunnilleen".
- No other number in the unit changed; the earlier full recomputation stands. answers.py runs, `practice.py check units/fy9-koe` passes (4 tasks, 61 p).

## Shared issues

- `docs/figures/catalog.json` still lists `fi:units/fy12-*` sources (outside the unit).
