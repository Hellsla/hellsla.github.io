VERDICT: PASS
CONTENT-HASH: 4e2d8a8bd9bccb80

## Delta review
Delta review, 2026-11-05, previous hash 3c616085eea3df1b. `git diff dcad1b122 -- content/en/units/fy9-tasavirta lessons/units/fy9-tasavirta`: the only change is the concept-map (`kartta`) branch heading "current and resistance" -> "current, resistance" (figures.json label and the redrawn foreignObject in `unit.md`, width 226 -> 206); nothing else changed.
- Preview rebuilt; Playwright at 360 and 1280, all details open: gap between "current, resistance" and grey "quantities" is 39 px at 360 and 73 px at 1280 (was an overlap of 15 / 28 px); no clipping, 0 `.katex-error`, no page errors, scroll width = viewport. `check_layout.py fy9-tasavirta --width 360` and `--width 1280`: OK for preview/en/fy9-tasavirta.
- Verdict: PASS.

## Earlier report (round 3)
Visual and editorial review of the English translation of fy9-tasavirta, round 3, 2026-11-04. Preview rebuilt with `python3 scripts/build.py fy9-tasavirta` -> `preview/en/fy9-tasavirta.html`; Playwright (`scripts/_browser.launch`) at 390 and 1280, all details opened, all 7 figures captured.

## Blocking
None.

## Round-2 Blocking findings
1. Concept map `kartta` branch headings in Finnish: FIXED. `figlib.translate()` now covers `\textbf{}`; after the redraw the headings read "current and resistance", "connections", "power and energy", "source" at 390 and 1280. "current and resistance" fits beside "quantities" at 390 px without overlap or clipping; no Finnish characters remain in `unit.md`.

## Checks
- No console or page errors, 0 `.katex-error`, no raw `$`, no decimal comma in the page text, scroll width equals the viewport (390 / 1280), `<html lang="en">`.
- Other figures (hero, `mokki`, `napa`, lamp curve, s3 U(I) with "(1.20 A; 3.75 V)" and "E ≈ 4.63 V", s3 I_k with "measuring range" and "I_k ≈ 6.3 A") readable, English, decimal point; unchanged since round 2.
- `units.py figures fy9-tasavirta --lang en --check`: up to date.

## Polish
None.
