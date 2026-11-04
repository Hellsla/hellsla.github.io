VERDICT: FAIL
CONTENT-HASH: a7033a860cc7acce

Visual & editorial review, round 2, of the English translation of fy9-energia. Preview preview/en/fy9-energia.html (python3 scripts/build.py fy9-energia), Playwright (Chromium) at 390 and 1280 px, all details opened.

## Blocking
1. NOT FIXED. unit.md, figure `kartta` (concept map): the three branch headings are still Finnish, **teho**, **hyötysuhde**, **energian lähde** (screenshot at 390 px and 1280 px; unit.md lines 221, 231, 241: `$\textbf{teho}$` ...). The translations ("power", "efficiency", "source of energy") have now been added to figures.json, but scripts/figlib.py translate() still only rewrites `\text{}`, `\mathrm{}` and `\textsf{}` (regex `(\\(?:text|mathrm|textsf)\{)`), so redrawing does not use them, and check_i18n line 207 forbids hand-editing the figure in unit.md. Fix (in shared code, outside this reviewer's scope): add `textbf` to that regex in scripts/figlib.translate (and to visible_len), then python3 scripts/units.py figures fy9-energia --lang en. No change is needed in this unit's translation files after that.

## Shared issues
- Same `\textbf{}` gap in every FY9 concept map: content/en/units/fy9-{aallot,kaasut,lampo,magnetismi-valo,moderni,sahkokentta,sailymislait,tasavirta,voimat,ympyraliike}/unit.md all still show Finnish branch heads.

## Round-1 Polish
2. Hero description "chimney and its cooling tower": fixed.
3. Task 3 graph description "(−20 °C, 191 kWh)": fixed (comma in English text; LaTeX unchanged).
4. ketju description "A to-scale energy flow diagram ...": fixed.

## Checks done
- 390 and 1280 px: scrollWidth equals the viewport, 0 KaTeX errors, no unrendered $...$, no svg/table/display formula wider than the viewport, no page errors.
- Other figures (hero, Investigate chart, ketju, borrowed grid, task 3 graph) English with decimal points, as in round 1.
