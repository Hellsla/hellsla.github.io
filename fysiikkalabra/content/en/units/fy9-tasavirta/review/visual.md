VERDICT: FAIL
CONTENT-HASH: 21d1b5094a6f3ae4

Visual and editorial review of the English translation of fy9-tasavirta, round 2, 2026-11-04. Preview rebuilt with `python3 scripts/build.py fy9-tasavirta` -> `preview/en/fy9-tasavirta.html`; Playwright (`scripts/_browser.launch`) at 390 and 1280, all details opened, all 7 figures captured.

## Blocking
1. NOT FIXED since round 1. `unit.md`, figure `kartta` (concept map, Theory summary): the four bold branch headings are still Finnish on the English page at 390 and 1280: "virta ja resistanssi", "kytkennät", "teho ja energia", "lähde" (unit.md lines with `\textbf{...}`). figures.json has the translations ("current and resistance", "connections", "power and energy", "source"), but `scripts/figlib.py` `translate()` still only rewrites `\text{}`, `\mathrm{}`, `\textsf{}` (regex `text|mathrm|textsf`), not `\textbf{}`. This reviewer may not edit scripts/, and hand-editing the generated SVG would be reverted by the next redraw. Fix: add `textbf` to the regex in `figlib.translate` (shared, see Shared issues), then `python3 scripts/units.py figures fy9-tasavirta --lang en` and check that "current and resistance" fits beside "quantities" at 390 px.

## Checks
- No console or page errors, 0 `.katex-error`, no raw `$`, no decimal comma in the page text, scroll width equals the viewport at 390 and 1280, `<html lang="en">`.
- Other figures at 390 px (`mokki`, `napa`, lamp curve, s3 U(I) with "(1.20 A; 3.75 V)" and "$E \approx 4.63$ V", s3 I_k) readable, English, decimal point. Concept map leaf labels (quantities, current, Ohm, wire, Kirchhoff, series, parallel, loop, Joule, power, resistor, energy, battery, terminal voltage, capacity) are English.
- The two reworded inquiry sentences (round-1 Polish) render correctly.

## Shared issues
- `scripts/figlib.py` `translate()`: `\textbf{}` words are never translated, so every FY9 concept map with bold headings stays partly Finnish in en and fi-easy (all of content/en/units/fy9-*/unit.md with a concept map still show Finnish `\textbf` headings). One regex change (`text|textbf|mathrm|textsf`) and a figures redraw per unit fixes all of them.
