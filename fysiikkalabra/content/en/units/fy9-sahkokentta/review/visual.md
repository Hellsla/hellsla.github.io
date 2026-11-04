VERDICT: PASS
CONTENT-HASH: 51ef54c541fe6381

Visual & editorial review, round 3, of the en translation of fy9-sahkokentta. 2026-11-04. Preview `python3 scripts/build.py fy9-sahkokentta` → preview/en/fy9-sahkokentta.html, checked in Playwright (scripts/_browser.launch) at 390 and 1280 px with all details opened: scrollWidth 390/1280 (no horizontal scroll), 0 KaTeX errors, no console or page errors, no decimal comma in the page text, no Finnish words in the page text except the language-switcher label "Selkeä suomi". All 9 figures captured one by one at both widths (hero, fy6-12/ex-vgraph, kartta, kipina, levyt, fy6-13/ex-qu, s1-fbd, s3-cd, s3-lin): readable, English labels, decimal points.

## Blocking
None. Round-2 Blocking 1 is FIXED: the concept map `kartta` now draws the branch headings in English ("charge and force", "field and potential", "capacitor", "components and safety"), after figlib.translate() gained \textbf and the en figures were regenerated; check_i18n en reports 0 errors.

## Polish
1. Coordinates still use the Finnish semicolon: tasks.json s3 c) criteria[0] "$(0.20; 93)$ and $(1.00; 376)$", inquiry.json activities[7] solution "(5.0 cm; 250 V)", solutions.md s3 c)/d). English uses a comma, but these are formulas compared with the source by check_i18n; optional.
2. At 390 px the off-canvas table of contents links lie outside the viewport (hidden menu); no horizontal scroll results. No action.
