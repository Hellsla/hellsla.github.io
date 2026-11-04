VERDICT: FAIL
CONTENT-HASH: 4425c0d198ddfcc1

Full visual and editorial review of the English translation of fy9-mittaaminen. Built with `python3 scripts/build.py fy9-mittaaminen` (preview/en/fy9-mittaaminen.html) and checked in Playwright at 390 and 1280 with every details element opened and the reveal buttons clicked.

## Blocking

1. Figure `kartta` (unit.md, The big picture), at both 390 and 1280: the English step names are wider than the left column of the boxes. "Measurement" runs into "reading, Δx, precision" (renders as "Measuremenreading") and "Interpretation" overlaps "k and b with units". Fix in content/en/units/fy9-mittaaminen/figures.json (no code change): shorter labels, e.g. "Mittaus" → "Measure", "Tulkinta" → "Interpret" (or "Meaning"), keeping Graph / Fit / Result; then re-apply the figures (`translate_kit.py apply` or `figures` for the unit) and recheck both widths. Update the kartta aria description if the step names change.

## Polish

1. figures.json "akseli alkaa " → "axis starts at " reads "axis starts at 100 g" in s3-pisteet: fine; "60 ml?" and "check" labels are readable. No action.
2. inquiry.json Starting point 6 choice 2 wording (see science Polish 1).

## Checked

- Captures opened (at 2× for 390): hero, kartta (390 and 1280), anatomia (390, 1280), linearisointi (390, 1280), the Investigate figure (p–θ points), s3-pisteet, s3-sovitus, s5-kuvaaja, s6-kuvaaja; the s1 data table at 390.
- Apart from kartta, all figure labels are English, LaTeX, with decimal points (0.919 g/ml, 0.48 m/s, 2.6 MPa·ml, −1.8 ml), nothing clipped, legible at 390.
- Page at 390 and 1280: scrollWidth = viewport, 0 `.katex-error`, no raw `$`, no page or console errors, no SVG/table/display maths wider than the viewport, no `d,d` decimal commas in the rendered text, no Finnish word in the rendered text.
- LaTeX: every number with unit in prose is LaTeX (`\,\text{…}`), decimal point throughout, no `{,}` left in any file.
- Data tables (s1, s3, s4, s5, s6) have translated headers and fit at 390.

## Shared issues

None.
