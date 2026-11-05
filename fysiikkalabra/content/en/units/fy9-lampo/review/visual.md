VERDICT: PASS
CONTENT-HASH: 73381a386f867cdd

Visual & editorial review, round 3, of the English translation of fy9-lampo. Preview built with `python3 scripts/build.py fy9-lampo` (preview/en/fy9-lampo.html) and checked in Playwright (scripts/_browser.launch) at 390 and 1280 px with every details element opened: no console errors, 0 KaTeX errors, no raw `$` in text, no Finnish words (ä/ö) in the rendered page, no horizontal page scroll (scrollWidth 390 / 1280). All five figures inspected at both widths: hero, melting curve, concept map, kayra and s3 graph are readable with English labels and the decimal point (273.15, 0.133 g/W, P_loss ≈ 70 W).

## Round-2 findings
- Blocking 1 (concept-map headings in Finnish): FIXED. After the figlib translate() change and the redraw, unit.md lines 122/130/138/146 contain `\textbf{heating}`, `\textbf{change of state}`, `\textbf{thermal expansion}`, `\textbf{heat transfer}`, and the rendered map shows them at 390 and 1280 px; boxes fit their text.

## Blocking
None.

## Polish
1. s3 d "about 13 %" (solutions) vs "about 12 %" (criterion): mirrors the Finnish source; check_i18n rejects a one-sided en change. Fix in fi first.
