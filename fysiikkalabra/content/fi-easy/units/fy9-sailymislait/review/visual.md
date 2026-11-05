VERDICT: PASS
CONTENT-HASH: c1b7d026abcd2b8a

Visual & editorial review of the Selkeä suomi translation of fy9-sailymislait. I built the preview with `python3 scripts/build.py fy9-sailymislait` (preview/fi-easy/fy9-sailymislait.html) and checked it in Playwright at 390 and 1280 px with every details element open. Reviewer 2026-11-04.

Results:
- No horizontal page scroll at either width (scrollWidth equals clientWidth). The only elements that reach past the edge are inside the stage-nav scroller and KaTeX scroll containers.
- 0 KaTeX errors, no raw `$` text left, no console errors.
- The figures are drawn in fi-easy from figures.json: hero, kartta, tormays, fy4-9/pysaytys, s3-sp and s3-lin. Their labels are readable at 390 px (kartta 358×560, tormays 358×472, graphs about 298 px wide with legible axis labels). They use decimal commas (0,80 m/s, 1,66 s, 0,080 s²/m) and keep the colours: velocity blue in tormays, force red in pysaytys.
- The aria descriptions are translated into short sentences.
- The three tables (air track, braking data, linearised values) fit at 390 px.
- "Luvun tärkeät käsitteet" renders after the opening and before the first stage, with the fixed lead and no note fields.
- LaTeX is used for every quantity and unit, with `\,` before units and `{,}` decimals. The Finnish is correct.

## Blocking
None.

## Polish
1. sovella/tasks.json s3 d), criteria[2] detail: a repeated phrase ("mitatun alueen … mitatun alueen yli"). See pedagogy.md 1 for the fix.
2. sovella/tasks.json s6 d), criteria[3] detail: "järkäleen energiaksi" should say "järkäleen sisäenergiaksi", as in solutions.md.
