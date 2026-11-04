VERDICT: FAIL
CONTENT-HASH: de4f8e04a55c5fa3

Visual & editorial review, round 2, of the English translation of fy9-voimat. Built with python3 scripts/build.py fy9-voimat (preview/en/fy9-voimat.html) and checked in Playwright (chromium headless) at 390 and 1280 px with all details opened: scrollWidth 390/1280 (no horizontal scroll), 0 KaTeX errors, no raw $ in text, no console or page errors, no decimal commas. The slope figure now reads "the situation" / "free-body diagram" and is readable at 390. check_i18n en: 0 errors; units.py figures fy9-voimat --lang en --check: up to date.

## Blocking
1. NOT FIXED (round-1 Blocking 1). unit.md concept map (figure kartta, Theory summary): the four bold headings are still Finnish on the English page at 390 and 1280: "voimakuvio ensin", "Newtonin lait", "voimat", "erikoistilanteet". The translations were added to figures.json, but they have no effect: lessons/units/fy9-voimat/figures.py draws the headings as \textbf{...} (lines 90 and 97) and scripts/figlib.py translate() substitutes only inside \text{}, \mathrm{} and \textsf{} (regex r"(\\(?:text|mathrm|textsf)\{)"). The SVG cannot be fixed by hand in unit.md, because check_i18n then reports "figures differ from figures.py". Fix needed outside the translation folder (owner of scripts/ or lessons/): either add textbf to the figlib.translate regex (and to the MISSING check), or draw the headings as \textbf{\text{...}} in figures.py; then run python3 scripts/units.py figures fy9-voimat --lang en. The same gap affects every FY9 unit's concept map in en (aallot, energia, kaasut, lampo, magnetismi-valo, moderni, sahkokentta, sailymislait, tasavirta, ympyraliike all still show Finnish \textbf headings).

## Polish
1. Round-1 Polish 1 ("situation picture" -> "the situation") is done, in the label and in the aria-label.
2. s3 graph at 390 px: the orange "F0 ≈ 0.24 N" label is cramped near the axis (source figure, same in Finnish).
3. Small label text (about 11 px at 390) in the two-panel figures; readable, a larger size in figures.py would help (source issue).
