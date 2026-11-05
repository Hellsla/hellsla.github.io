VERDICT: PASS
CONTENT-HASH: b346ed8b9e1ca0c5

Visual & editorial review, round 3, of the English translation of fy9-energia. Preview preview/en/fy9-energia.html (python3 scripts/build.py fy9-energia), Playwright (Chromium via scripts/_browser.launch) at 390 and 1280 px, all details opened, every svg[data-fig] screenshotted.

## Blocking
None.

## Round-2 findings
1. FIXED. Concept map `kartta`: branch headings now read **power**, **efficiency**, **source of energy** (unit.md lines 221, 231, 241, after scripts/figlib.translate() gained `textbf`). At 390 px and 1280 px the headings fit their boxes, nothing overlaps, and the widest ("source of energy") has room to spare.

## Checks done
- 390 and 1280 px: scrollWidth equals the viewport, 0 KaTeX errors, no unrendered $...$, no svg/table/display formula wider than the viewport, no page errors, no Finnish letters (ä, ö) in any figure text.
- Figures looked at: hero (no text), Investigate bar chart (P (MW), P0–P3), `ketju` (η1 = 0.90, η2 = 0.45, η3 = 0.98, 500/450/203/198 MW, losses 50/248/4 MW, electricity, boiler / steam cycle / generator and transformer), borrowed fy2-4 grid (electric motor, electricity, kinetic energy, heat (losses)), task 3 graph (E (kWh), T (°C), 230 kWh, 12 kWh, k ≈ −4.9 kWh/°C): all English with decimal points and readable at 390 px.
- Round-1 Polish 2–4 (hero, task 3 graph and ketju descriptions) remain fixed.

## Polish
None.
