VERDICT: FAIL
CONTENT-HASH: 27001dbbab8eaed1

Visual & editorial review, round 2, of the en translation of fy9-sahkokentta. 2026-11-04. Preview `python3 scripts/build.py fy9-sahkokentta` → preview/en/fy9-sahkokentta.html, checked in Playwright (scripts/_browser) at 390 and 1280 px with all details opened: scrollWidth 390/1280 (no horizontal scroll), 0 KaTeX errors, no console errors, no decimal comma in the page text. Figures captured one by one at 390 px (hero, kartta, kipina, levyt, s1-fbd, s3-cd, s3-lin): readable, decimal points. Round-1 Polish 3 and 4 are fixed (teacher.md figure ids, rubric wording, "own capacitance").

## Blocking
1. NOT FIXED from round 1. unit.md, figure `kartta` (concept map, Theory summary): the four branch headings are still drawn in Finnish, "varaus ja voima", "kenttä ja potentiaali", "kondensaattori", "komponentit ja turvallisuus" (seen in the 390 px capture). figures.json now has the four translations ("charge and force", "field and potential", "capacitor", "components and safety"), but they are not used: lessons/units/fy9-sahkokentta/figures.py line 183 draws the heading as `\textbf{…}`, and scripts/figlib.py `translate()` (line 56) only translates `\text{}`, `\mathrm{}`, `\textsf{}`. The fix cannot be made in the translation files: check_i18n requires unit.md figures to equal the regenerated ones, so a hand edit of the SVG fails. Fix (shared): add `textbf` to the regex in figlib.translate (and in visible_len), then `python3 scripts/units.py figures fy9-sahkokentta --lang en`; or draw the heading in figures.py as `\textbf{\text{…}}`. Then rebuild and re-review.

## Polish
2. Coordinates still use the Finnish semicolon: tasks.json s3 c) criteria[0] "$(0.20; 93)$ and $(1.00; 376)$", inquiry.json activities[7] solution "(5.0 cm; 250 V)", solutions.md s3 c)/d). English uses a comma. These are formulas; change only if check_i18n accepts them.
3. At 390 px the off-canvas table of contents links lie outside the viewport (hidden menu); no horizontal scroll results. No action.

## Shared issues
- scripts/figlib.py `translate()` does not cover `\textbf{}`, so bold figure labels stay Finnish in every translation; the same regex feeds translate_kit's figures.json extraction and check_i18n's figure check, so it is not reported as missing either (here the strings were added to figures.json by hand and are still unused).
