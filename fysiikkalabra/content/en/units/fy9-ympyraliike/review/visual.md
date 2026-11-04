VERDICT: FAIL
CONTENT-HASH: 0a2f409485a4a88c

Visual and editorial review of the English translation of fy9-ympyraliike, round 2 (source PASS at 678dc353273487b6). Reviewer 2026-11-04.

Preview rebuilt with `python3 scripts/build.py fy9-ympyraliike` (preview/en/fy9-ympyraliike.html) and checked in Playwright at 390 and 1280 px with every details element opened: no horizontal page scroll (scrollWidth = viewport at both widths), no KaTeX errors, no raw `$…$`, no console errors. All eight figures captured at both widths; labels readable at 390 px, decimal points throughout, force red, velocity blue, acceleration orange. Round-1 Polish 2 (`$\overline{G}_\text{b}$`) and Polish 3 ("A merry-go-round") are fixed.

## Blocking
1. **Not fixed: the concept map (unit.md, figure `kartta`) still shows the Finnish headings tasapaino, ympyräliike and gravitaatio** (capture at 390 and 1280 px; unit.md lines with `$\textbf{tasapaino}$` etc.). The translator added "tasapaino" → "equilibrium", "ympyräliike" → "circular motion", "gravitaatio" → "gravitation" to figures.json, but the figure is drawn by lessons/units/fy9-ympyraliike/figures.py with `r"\textbf{" + head + "}"`, and `scripts/figlib.py` `translate()` only translates the contents of `\text{}`, `\mathrm{}` and `\textsf{}`, so the entries are never used. The drawn SVG cannot be corrected by hand in unit.md: I tried it, and check_i18n.py then reports "figures differ from figures.py", so I redrew the figure (`units.py figures fy9-ympyraliike --lang en`) and left unit.md as it was. Fix (shared files, outside this translation): either add `textbf` to the regex in figlib.translate() (and to translate_kit's figure-text extraction), or write the heads in figures.py as `\textbf{\text{tasapaino}}`; then redraw with `python3 scripts/units.py figures fy9-ympyraliike --lang en` (figures.json already has the translations). Check that "circular motion" fits: the label box is 328 px wide, so it fits.

## Polish
None new (see science.md Polish 1 on "does not move", optional).

## Shared issues
- `scripts/figlib.py` `translate()` (and translate_kit's extraction and check_i18n's missing-text check) ignore `\textbf{}`; any figure that draws words in bold stays Finnish in every translation without an error. The fi-easy version of this unit is affected by the same code path (harmless there, since it is Finnish).
