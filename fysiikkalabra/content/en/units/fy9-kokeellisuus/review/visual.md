VERDICT: PASS
CONTENT-HASH: 4208bb67071dc3d5

Visual & editorial review of the English translation of fy9-kokeellisuus. Built with python3 scripts/build.py
fy9-kokeellisuus (preview/en/fy9-kokeellisuus.html) and checked in Playwright at 390 and 1280 px with every details
element open: html lang="en", no page-level horizontal scroll (scrollWidth = clientWidth at both widths), 0 KaTeX
errors, no raw dollar signs, no console errors, no Finnish left in visible text (the "Yleisiä virheitä" / "Hyväksytään
myös" structural headings render as "Common mistakes" / "Also accepted"; the language menu shows Suomi and Selkeä
suomi as it should). All five figures (hero, kartta, virhe, fy9ko-s4-graph, fy9ko-s6-graph) are drawn in English with
decimal points (0.10 s^2, 3.21 s^2, 0.80 m, 7.2 m, 0.12 s^2/m), all words in \text{}, readable at 390 px as in the
source; their descriptions are translated. All numbers and units are in LaTeX with \, before units and the decimal
point; the millilitre keeps the m\textsf{l} convention of the source. Tables (spring measurement, pendulum, braking)
render; the 4-column spring table at 390 px scrolls inside its wrapper (365 px in 324 px) with the fade hint, the same
as the Finnish page.

## Blocking
None.

## Polish
1. Terminology consistency: teacher.md says "Tasks" for the part the page calls "Exercises" (see pedagogy Polish 1).
2. "between X–Y" (inquiry.json check-1, solutions.md s5 c) -> "between X and Y".
3. "ten swings" -> "ten oscillations" (unit.md formula section, exit ticket q2, tasks.json s4, solutions.md s4) for
   unambiguous English.
