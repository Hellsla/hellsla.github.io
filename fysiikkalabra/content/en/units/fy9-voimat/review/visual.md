VERDICT: PASS
CONTENT-HASH: 150352cafe9aca15

Visual & editorial review, round 3, of the English translation of fy9-voimat. scripts/figlib.py translate() now also substitutes inside \textbf{} and the en figures were redrawn (commit 433d9adba). Since round 2 only figure SVG markup in unit.md changed (concept map heading boxes and the slope figure label positions); no text, formula, number or answer changed. Built with python3 scripts/build.py fy9-voimat (preview/en/fy9-voimat.html) and checked in Playwright (scripts/_browser.launch) at 390 and 1280 px with all details open: scrollWidth 390/1280 (no horizontal scroll), 0 KaTeX errors, no raw $ in the text, no console or page errors, no decimal commas. Every figure was looked at (hero, fy4-14/vt, kartta, kalteva, fy9-voimat-s3-graph). python3 scripts/units.py figures fy9-voimat --lang en --check: up to date. check_i18n: en 0 errors; units.py check: 77 units ok; practice.py check: en/units/fy9-voimat 6 tasks, 95 points OK.

## Blocking
None.
1. FIXED (round-2 Blocking 1). The concept map (kartta, Theory summary) now shows the headings "free-body diagram first", "Newton's laws", "forces" and "special cases" in English at 390 and 1280 px. They fit their boxes and are readable, and the aria-label is English.

## Polish
1. s3 graph at 390 px: the orange "F0 ≈ 0.24 N" label is still cramped near the axis (a source figure issue, the same in Finnish).
2. Label text in the two-panel slope figure is small at 390 px (about 11 px). It is readable, but a larger size in figures.py would help (a source issue).
3. Concept map, special cases: the side label "connected" could read "connected bodies". This is optional, since the aria-label already says "connected bodies".
