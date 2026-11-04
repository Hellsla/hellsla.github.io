VERDICT: PASS
CONTENT-HASH: 271c1d1ab8c947a2

Visual & editorial review (round 3) of the English translation of fy9-aallot. Preview built with `python3 scripts/build.py fy9-aallot` → `preview/en/fy9-aallot.html`, checked in Playwright (`_browser.launch`) at 390 and 1280 with all details opened; every figure (hero, kartta, pilli, ominais, y–t graph, s3 T–l and T²–l) screenshotted and inspected. Reviewed 2026-11-04.

## Checks
- Round-2 Blocking 1 FIXED: `scripts/figlib.py` `translate()` now covers `\textbf`; the redrawn `kartta` shows **oscillators**, **waves**, **sound** (built SVG has `\textbf{oscillators}` etc., no Finnish), readable at 390 and 1280.
- No horizontal scroll at 390 or 1280 (scrollWidth = clientWidth), 0 `.katex-error`, no raw `$`, no console or page errors. The only ä/ö text on the page is the language switcher's "Selkeä suomi" (intended). No Finnish text inside any figure SVG.
- All figures readable at 390 with decimal points and English labels; aria-labels are English.
- `### Yleisiä virheitä` / `### Hyväksytään myös` in sovella/solutions.md are practice.py structural markers, rendered via lang/en.json as "Common mistakes" / "Also accepted"; correct as is.

## Blocking
None.

## Polish
1. `ominais` at 390: the N/A letters and legend are about 14 px; acceptable but small (as in the source).
2. Solutions "in the unit $\text{m/s}$" → "in $\text{m/s}$" would be more natural English (optional house style).
