VERDICT: PASS
CONTENT-HASH: b3d2c2bde898a57e

Visual & editorial review of the Selkeä suomi translation of fy9-sahkokentta. Preview built with
`python3 scripts/build.py fy9-sahkokentta` → preview/fi-easy/fy9-sahkokentta.html, checked in Playwright
(scripts/_browser) at 390 and 1280 px with every details/answer/solution opened.

Results: no page errors, no KaTeX errors, no raw `$…$` left in text, no horizontal page scroll at 390 (scrollWidth 390; the
only wider boxes are the stage navigation's own scroller). No display formula overflows its box. All nine figures render
in the page language with decimal commas (hero, kartta, kipina, levyt, the two chapter graphs, s1 force diagram, s3 C(d)
and C(1/d) graphs). At 390 px the labels stay legible (kartta 358 px wide, figure text ≥ about 11 px; the force diagram
keeps red force arrows, green field lines). Aria-labels are the Selkeä suomi descriptions from figures.json. The three
tables (s2 dielectrics, s3 data, s5 report in a blockquote) fit at 390 with no inner scroll. *Luvun tärkeät käsitteet*
shows after the prior-knowledge box, before stage 1, with the fixed lead text and the five terms; the formulas in it render.
LaTeX rules hold (units in `\text{}`, `\,` before units, `\cdot` products, `{,}` decimals, `\overline` vectors).
Finnish is correct and consistent with the source's terminology.

## Blocking
None.

## Polish
1. inquiry.json activities[7] hint 2 "miksi energiaksi…" is ambiguous (see pedagogy 1).
2. sovella/tasks.json source notes "luvut ovat keksitty esimerkki" – number agreement (see pedagogy 4).
3. teacher.md Arviointi "Osa III:n tyyppinen" → "osan III kaltainen".

## Shared issues
- The stage navigation shows the English label "Exit ticket" in the Finnish UI (lang file / template, not this unit).
