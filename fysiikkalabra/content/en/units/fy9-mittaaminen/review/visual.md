VERDICT: PASS
CONTENT-HASH: a1fbe68e2eac6dea

Round 2 visual and editorial review of the English translation of fy9-mittaaminen. Built with `python3 scripts/build.py fy9-mittaaminen` (preview/en/fy9-mittaaminen.html) and checked in Playwright (Chromium) at 390 and 1280 with every details element opened.

## Blocking

None.

## Polish

None.

## Checked

- Round-1 Blocking 1 (kartta labels overlapping) is fixed: figures.json now maps Mittaus → "Measure" and Tulkinta → "Interpret", unit.md carries the re-applied figure, and the aria description uses the new names. Measured rendered widths of the left-column labels vs their boxes: at 390 Measure 54/76 px, Interpret 58/76 px; at 1280 Measure 94/131 px, Interpret 101/131 px; all other labels fit too. Screenshot at 390 (2×) confirms no overlap with the right column.
- Page at 390 and 1280: scrollWidth equals the viewport, 0 `.katex-error`, no raw `$`, no `d,d` decimal commas, no SVG/table/display maths wider than the viewport, no page or console errors.
- Other figures and tables are unchanged since round 1 (text-only diff), where they were checked at both widths.

## Shared issues

None.
