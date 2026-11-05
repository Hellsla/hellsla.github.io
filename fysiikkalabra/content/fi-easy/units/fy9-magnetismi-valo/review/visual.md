VERDICT: PASS
CONTENT-HASH: b053cd2d9ea1dacc

Visual and editorial review of preview/fi-easy/fy9-magnetismi-valo.html, built with `python3 scripts/build.py fy9-magnetismi-valo`. I captured it in Playwright (scripts/_browser) at 390 and 1280 px with every details element opened, including hints, solutions, the model answers and the rubrics. Captures are in /tmp/claude-0/tk/fy9-magnetismi-valo/rv/.

Results: html lang is "fi", the language control reads "Selkeä suomi", and there are no console or page errors. There are 0 .katex-error elements and no raw `$…$` text, no display formula is wider than its box, and the page scrollWidth equals the viewport at both widths. Only the stage TOC strip runs past the edge, and that strip scrolls by design (shared template). All three tables fit at 390 px (319, 135 and 324 of 324 px). Figures at 390 px are 358 px wide for hero, kartta, siirto and ympyra, 324 px for the two FY7 simulation figures and 298 px for s3-B and s3-lin. All are legible at that width. Figure text is in Finnish with a decimal comma (0,50 Ω, 2,0 A, 0,005 %, 2,42 µT·m, b ≈ 11 µT), and the aria-labels are rewritten in plain Finnish and match the drawings. Colours follow the convention: force red, velocity blue, field green. The Luvun tärkeät käsitteet block renders after the opening, with the fixed lead, the terms in bold and the inline LaTeX ($\Phi = BA$, $n = \frac{c}{v}$) typeset. Solutions use the Annettu / Kysytty / Periaate / Kaava / Muunnokset / Sijoitus / Vastaus / Järkevyys blocks. The rubric cards (0/1/2 points) are readable at 390 px. LaTeX rules are kept: \text{} units, \, before units, {,} decimals, \overline{B}, \tfrac and \dfrac as in the source.

## Blocking
None.

## Polish
1. The figure words "sm-aalto" (kartta) and "loivenee" (s3-B) are the only figure texts left in harder register (pedagogy finding 2). Change them in figures.json and re-run the figure step.
2. sovella/solutions.md: two sentences start with "Tai" (s4 Yleisiä virheitä b, s5 b). This is an editorial fix, see pedagogy finding 3.
