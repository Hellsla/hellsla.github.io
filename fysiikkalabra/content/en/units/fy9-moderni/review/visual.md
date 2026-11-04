VERDICT: PASS
CONTENT-HASH: 3e3f4a33c6a16ade

Visual & editorial review, round 3, of the English translation of fy9-moderni. Preview rebuilt with
`python3 scripts/build.py fy9-moderni` -> preview/en/fy9-moderni.html and checked in Playwright
(scripts/_browser.launch) at 390 and 1280 px with every details element open: scrollWidth 390/1280 (no horizontal
overflow), no console errors, 0 .katex-error, no raw `$` in the rendered text. All 8 figures screenshotted and
inspected at both widths (hero, kartta, fotonit, puolitus, fy8-10/kayra-points, fy8-11/sidosenergia-luku,
fy9-moderni-s3-p, fy9-moderni-s3-fit): all labels English, decimal points, readable, nothing clipped.

## Blocking
1. FIXED (round-2 Blocking 1). scripts/figlib.py translate() now covers `\textbf{}` and the concept map was
   redrawn: the branch headings read "the photon and the atom", "the nucleus", "radiation and people"; the headings
   fit inside their boxes at 390 and 1280 px. No other `\text`/`\textbf` label in unit.md is Finnish.

## Polish
2. sovella/solutions.md keeps `### Yleisiä virheitä` / `### Hyväksytään myös`: correct, they are parse keys
   rendered as "Common mistakes" / "Also accepted". No change.
