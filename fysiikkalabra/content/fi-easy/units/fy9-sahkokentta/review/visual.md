VERDICT: PASS
CONTENT-HASH: 5d7c37ca8b9e6324

## Delta review

Delta review (2026-11-05). `git diff dcad1b122 -- content/fi-easy/units/fy9-sahkokentta lessons/units/fy9-sahkokentta` shows one change only: sovella/tasks.json s1 b, rubric criterion `calculation` (1 p). The long inline formula q = 0,080 m·sqrt(4,93·10^-4 N / 8,988·10^9 N·m²/C²) is now split into $F_\text{s} = 4{,}93 \cdot 10^{-4}\,\text{N}$ ja $k = 8{,}988 \cdot 10^{9}\,\text{N}\cdot\text{m}^2/\text{C}^2$, joten $q = 0{,}080\,\text{m} \cdot \sqrt{F_\text{s}/k} \approx 1{,}87 \cdot 10^{-8}\,\text{C}$ ja $n = q/e \approx 1{,}2 \cdot 10^{11}$. The text is identical to the Finnish source's criterion (check_i18n fi-easy 0 errors; the S2 formula-keeping rule holds).

Visual: rebuilt the preview and checked it in Playwright (scripts/_browser) at 360 and 1280 px with every details open and window.flFitMath run as on the page. No page errors, no KaTeX errors, page scrollWidth = viewport at both widths. At 1280 px the criterion is two lines with nothing cut. At 360 px F_s and k wrap onto their own lines; the q formula is 319 px in a 278 px box, so lesson.js gives it its own horizontally scrolling line (kx-wide). That is the site's supported way and check_layout accepts it: `check_layout.py fy9-sahkokentta --width 360` and `--width 1280` both print OK for preview/fi-easy. Polish (not blocking, should be done in the Finnish source first, because S2 has to keep every Finnish formula): splitting the q formula after $\sqrt{F_\text{s}/k}$ into a second formula $q \approx 1{,}87 \cdot 10^{-8}\,\text{C}$ would remove the scroll at 360 px. I tried that in fi-easy alone, and check_i18n flagged it (formula lost from Finnish), so I reverted it. Content is as committed.

## Earlier review (still valid)

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
