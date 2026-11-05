VERDICT: PASS
CONTENT-HASH: 78c57d65fbb8f279

## Delta review (2026-11-04)
Only change since round 3 (`git diff HEAD`, the only modified file under content/en/units/fy9-sahkokentta and nothing under lessons/units/fy9-sahkokentta): sovella/tasks.json s1 b) rubric `calculation` detail, where the long inline $q = 0.080\,\text{m}\cdot\sqrt{\dfrac{4.93\cdot10^{-4}\,\text{N}}{8.988\cdot10^{9}\,\ldots}}$ is split into $F_\text{s} = 4.93\cdot10^{-4}\,\text{N}$ and $k = 8.988\cdot10^{9}\,\text{N·m}^2/\text{C}^2$, so $q = 0.080\,\text{m}\cdot\sqrt{F_\text{s}/k} \approx 1.87\cdot10^{-8}\,\text{C}$. It mirrors the fi source line exactly (check_i18n en: 0 errors). Preview rebuilt; Playwright at 360 and 1280 px with all details open and lesson.js flFitMath run: scrollWidth 360/1280, 0 KaTeX errors, no page errors. At 360 px the rubric now shows two short lines that fit and the q line becomes a scrolling formula row (kx-wide, 319 px in a 278 px box), the intended behaviour; at 1280 px all three formulas fit on the line. check_layout.py --width 360 and --width 1280: OK for preview/en/fy9-sahkokentta. New Polish 3 below.

Visual & editorial review, round 3, of the en translation of fy9-sahkokentta. 2026-11-04. Preview `python3 scripts/build.py fy9-sahkokentta` → preview/en/fy9-sahkokentta.html, checked in Playwright (scripts/_browser.launch) at 390 and 1280 px with all details opened: scrollWidth 390/1280 (no horizontal scroll), 0 KaTeX errors, no console or page errors, no decimal comma in the page text, no Finnish words in the page text except the language-switcher label "Selkeä suomi". All 9 figures captured one by one at both widths (hero, fy6-12/ex-vgraph, kartta, kipina, levyt, fy6-13/ex-qu, s1-fbd, s3-cd, s3-lin): readable, English labels, decimal points.

## Blocking
None. Round-2 Blocking 1 is FIXED: the concept map `kartta` now draws the branch headings in English ("charge and force", "field and potential", "capacitor", "components and safety"), after figlib.translate() gained \textbf and the en figures were regenerated; check_i18n en reports 0 errors.

## Polish
1. Coordinates still use the Finnish semicolon: tasks.json s3 c) criteria[0] "$(0.20; 93)$ and $(1.00; 376)$", inquiry.json activities[7] solution "(5.0 cm; 250 V)", solutions.md s3 c)/d). English uses a comma, but these are formulas compared with the source by check_i18n; optional.
2. At 390 px the off-canvas table of contents links lie outside the viewport (hidden menu); no horizontal scroll results. No action.

3. sovella/tasks.json s1 b) `calculation`: at 360 px the $q = \ldots \approx 1.87\cdot10^{-8}\,\text{C}$ formula still scrolls sideways (about 41 px) inside the rubric. Acceptable by the kx-wide design; it must stay identical to the fi source, so no action.
