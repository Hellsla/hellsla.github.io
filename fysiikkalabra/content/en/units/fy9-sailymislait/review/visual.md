VERDICT: PASS
CONTENT-HASH: a5ce41b2c877ab0d

Visual and editorial review, round 3, of the en translation of fy9-sailymislait, 2026-11-04.

Method: rebuilt with `python3 scripts/build.py fy9-sailymislait` (preview/en/fy9-sailymislait.html, "reviewed") and opened in Playwright (scripts/_browser.launch) at 390 and 1280 px with every details element open; screenshotted and looked at every figure (hero, collision/bar figure, concept map, buffer force graph, both s3 graphs).

Results:
- No horizontal scroll (scrollWidth 390 at 390 px, 1280 at 1280 px).
- No KaTeX errors, no console errors, no raw `$` in the text, no decimal commas.
- The only Finnish word in the page text is "Selkeä" in the site-wide language switcher (Selkeä suomi), which is intended.
- Figure widths at 390 px: 358 (hero, collision, concept map), 324 (buffer graph), 298 (s3 graphs).

## Blocking
None. Round-2 Blocking 1 is fixed: the concept map `kartta` now draws **energy**, **momentum** and **applications** (HTML contains `\textbf{energy}`, `\textbf{momentum}`, `\textbf{applications}`; no `\textbf{energia|liikemäärä|sovellukset}` remains). The headings fit their boxes at both widths. The redraw changed only these three labels in unit.md.

## Polish
1. Ratio colon "a : b" ($F_\text{avg} = |\Delta p| : \Delta t$, $\mu = a : g$) is Finnish typography; English uses "/" or a fraction. Project-wide decision, left as it is.
2. $s_\text{p}$ for stopping distance (fy4-11 English uses $s_\text{stop}$). See science Polish 1.
3. The s3 graphs (298 px) and buffer graph (324 px) have axis labels of about 10 px at 390 px: readable, but at the limit.
