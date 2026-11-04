VERDICT: PASS
CONTENT-HASH: b32f7a442b2e29c4

Visual & editorial review of preview/fi-easy/fy9-koe.html (built with `python3 scripts/build.py fy9-koe`), checked in
Playwright at 390 px and 1280 px with every details element open: no page errors, no KaTeX errors, no raw `$`, no
horizontal page scroll at 390 px (scrollWidth 390), the Tehtäväsanat table wraps cleanly within 358 px, the "Luvun
tärkeät käsitteet" component renders after the opening with the fixed lead and LaTeX in the kulmakerroin entry,
and the Sovella tasks, solutions, rubrics and teacher notes render. All four figures (hero, steps, graph,
fy9-koe-s2-graph) are drawn from figures.json with Finnish labels and decimal commas; every figure description is
translated. Decimal comma and `\,` units are used throughout; the language menu offers Suomi and English.

## Blocking
None.

## Polish
1. Grammar, inquiry.json `activities[32].choices[1].feedback`: "eivät monta fotonia riitä erikseenkään" →
   "eivät monetkaan fotonit riitä erikseen."
2. sovella/tasks.json `tasks[0].text`: "Tien aikana korkeus kasvaa" → "Tien matkalla korkeus nousee".
3. unit.md "Yleisiä virheitä": "Yksikkö jää muuttamatta: km/h jää muuttamatta yksikköön m/s, tai celsiusaste jää
   muuttamatta kelviniksi." repeats *jää muuttamatta* three times; write "Yksikköä ei muuteta: esimerkiksi
   $\text{km/h}$ jää muuttamatta yksikköön $\text{m/s}$ tai celsiusaste kelviniksi."
4. At 390 px the step-card subtitles in the "steps" figure and the point labels in fy9-koe-s2-graph (298 px wide) are
   about 9 px high: readable but small. Shared with the source figures (lessons/units/fy9-koe/figures.py); listed
   under Shared issues, no change needed in the translation.

## Shared issues
- lessons/units/fy9-koe/figures.py: small label size at phone width in "steps" and the Sovella graph (item 4).
