VERDICT: PASS
CONTENT-HASH: 96380ddc9d785d43

## Blocking

## Polish
- [Minor] inquiry.json johtopaatos — "Write on the basis of your table" now sits directly under the phone-measurement card and its $E$ table; "Write on the basis of your table from Experiment 1" removes the doubt.
- [Minor] optional boxes — summaries read "OPTIONAL · Extension: …" (two labels for one status), and the opened theory box repeats its title; harmless, could be trimmed at template level.
- [Minor] inquiry.json virhe (untouched text, only the title changed) — the student's quoted chain is a `kx-wide` scroller at 360/390 px, cut mid-formula with no scroll cue; one line as required, a shorter quote would read better.
- Tooling (not content): `scripts/screenshot.py fy7-15` crashes at `.worked .all-steps` because the worked example now sits in a closed optional box; captures were taken with an equivalent Playwright script.

## Checked
- Hash at start 16cd6d2d00ffe824; lesson.md and inquiry.json were edited at 11:57 during the review (three-polariser experiment to core, misconception wording), so I rebuilt, re-captured and reviewed that edit too; end hash 96380ddc9d785d43, stable.
- Captures of preview/en/fy7-15.html at 360, 390, 1280 px, every stage closed and with all boxes open: Investigate (phone measurement card with table and choice, Conclusion with the "Core" tag), Explain (Common misconception, new Summary bullets, scene, opened Extension boxes with theory, Experiment 1 task and fit task), Apply (3D cinema core task, three Extension boxes), Check (2. Explain with tag, Extension laser task), exit ticket with both answers open.
- Programmatic check at 360/390/1280, closed and open: no inline KaTeX on two lines, no page-level horizontal overflow; only wide inline maths is the `kx-wide` scroller in #virhe.
- Core tag and Extension boxes: clean spacing, titles wrap inside the box at 360 px, nothing clipped.
- Changed English fluent and consistent (transmission axis, analyser, polarised), quantities in LaTeX with decimal point.

## Scores
illustrations 5 · typography 5 · English 4 · accessibility 4
