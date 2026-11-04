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
- none

## Polish
1. (Carried over) inquiry.json Tutki "Vastaus B": Sijoitus line break at 390.
2. (Carried over) Esimerkki stage labels vs the steps figure.
3. (Carried over) fy9-koe-s2-graph tick numbers ≈ 10 px at 390.
4. review/shots.md still names fy12-koe capture files from the earlier round; regenerate it with the next capture run (not part of the hash).

## Checked
- `python3 scripts/build.py fy9-koe` (preview only; site/ untouched). Playwright at 390 and 1280, all details open: no `.katex-error`, no raw `$`, no page errors, no broken images, no horizontal scroll.
- Captures of "Koe ja ajankäyttö" at 390 and 1280: the three-item Osa list renders as a bulleted list with bold labels, wraps cleanly at 390, and the time budget's minutes render as KaTeX (`$360\,\text{min}$` etc.). No `×`; no division in the new text.
- LaTeX: every number with a unit in the new text is in LaTeX (minutes; "kuusi tuntia" is a word). Points (pistettä, p) and task counts are counts, written as plain numbers like elsewhere on the site.
- SVG ids (`fy9koe-h-*` etc.): every `url(#…)` resolves; `units.py figures` and `practice.py figures` up to date.
- Finnish: read the new paragraphs in full; after the fixes above no language issues.

## Shared issues
None.
