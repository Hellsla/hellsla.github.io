VERDICT: PASS
CONTENT-HASH: c2dcaa79f3905e0c

Round 2 visual and editorial review of preview/fi-easy/fy9-aallot.html (`python3 scripts/build.py fy9-aallot`), checked in Playwright (scripts/_browser) at 390 px and 1280 px with every details element opened. There is no horizontal page scroll (scrollWidth equals the viewport at both widths), no KaTeX error, no raw `$…$` and no console error. The figures are drawn in the language with the decimal comma and fit at 390 px: hero 358 px, concept map 358×651, pilli 358 px, ominaistaajuudet 358 px, naru 324 px, and s3 graphs 298 px. Units use LaTeX with `\,`. teacher.md, the solutions, the rubrics and figures.json are all translated.

## Blocking
None. Round-1 Blocking 1 is fixed: inquiry.json activities[7] now has "Tee näin:\n\n1. …". At both widths it renders as an `<ol>` with three steps, and the screenshot at 390 px is clean. sovella/tasks.json "Toimi näin:\n\n1." has the blank line too.

## Polish
1. Round-1 Polish 2–5 are fixed: the "Ydinajatus" wording, the "$60\,\text{Hz}$:n äänen aallonpituus" feedback, "$8$ täyttä värähdystä" without the doubled number, and "Siksi aallonpituuskin on erilainen". No open items.
