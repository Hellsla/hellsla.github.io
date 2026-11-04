VERDICT: PASS
CONTENT-HASH: fbf82dd8d638f8de

Visual & editorial review, round 2, of preview/fi-easy/fy9-koe.html (built with `python3 scripts/build.py
fy9-koe`), checked in Playwright at 390 px and 1280 px with every details element open: no page errors, no KaTeX
errors, no raw `$`, no horizontal scroll at 390 px (scrollWidth 390). All four figures render (358/358/358/298 px
at 390; 576/608/608/569 at 1280) with Finnish labels and decimal commas. The "Luvun tärkeät käsitteet" box renders
after the opening with all five concepts (incl. the new *merkitsevä numero* and LaTeX in *kulmakerroin*). The only
"d.d" patterns in the text are task numbers (1.1-2 …) and a date; numbers use decimal comma and `\,` units.

## Blocking
None.

## Polish
1. Round-1 Polish 1–3 are done ("eivät monetkaan fotonit riitä erikseen", "Tien matkalla korkeus nousee",
   "Yksikköä ei muuteta: esimerkiksi …").
2. At 390 px the step-card subtitles in "steps" and the point labels in fy9-koe-s2-graph are about 9 px high:
   readable but small; shared with the source figures, no change in the translation.

## Shared issues
- lessons/units/fy9-koe/figures.py: small label size at phone width in "steps" and the Sovella graph.
