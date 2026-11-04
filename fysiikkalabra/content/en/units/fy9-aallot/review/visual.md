VERDICT: FAIL
CONTENT-HASH: cc28e1607c126903

Visual & editorial review (round 2) of the English translation of fy9-aallot. Preview built with `python3 scripts/build.py fy9-aallot` → `preview/en/fy9-aallot.html`, checked in Playwright (`_browser.launch`) at 390 and 1280 with all details, hints, solutions and rubrics opened. Reviewed 2026-11-04.

## Checks
- No horizontal scroll at 390 or 1280 (scrollWidth = clientWidth), 0 `.katex-error`, no raw `$`, no console or page errors.
- Round-1 Blocking 2 is FIXED: the `ominais` figure now shows N/A marks and the legend "N node, A antinode" (figures.json `"S": "N"`, `"K": "A"`); checked at 390.
- pilli, hero, the y–t graph and both s3 graphs remain readable at 390 with decimal points.

## Blocking
1. NOT FIXED (round-1 Blocking 1): `kartta` (concept map, unit.md "Key idea") still draws the three branch headings in Finnish, **värähtelijät**, **aallot**, **ääni**, on the English page (seen in the built SVG as `\textbf{värähtelijät}` etc., and at 390 px). The translations are already in `figures.json` ("oscillators", "waves", "sound"), but `scripts/figlib.py` `translate()` still only rewrites `\text`, `\mathrm`, `\textsf` (line 56), so they are never applied. Fix (shared, outside the translation files): add `textbf` to that regex, `(\\(?:text|textbf|mathrm|textsf)\{)`, then rebuild. Nothing in `content/en/units/fy9-aallot/` can fix it; this unit's own files are ready.

## Polish
2. `ominais` at 390: the N/A letters and legend are about 14 px; acceptable but small (as in the source).
3. Solutions "in the unit $\text{m/s}$" → "in $\text{m/s}$" would be more natural English (optional house style).

## Shared issues
- `scripts/figlib.py` `translate()` ignores `\textbf{}` (Blocking 1); it hits every unit whose figures.py uses `\textbf`, in en and fi-easy.
