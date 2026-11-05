VERDICT: PASS
CONTENT-HASH: 4e2d8a8bd9bccb80

## Delta review
Delta review, 2026-11-05, previous hash 3c616085eea3df1b. `git diff dcad1b122 -- content/en/units/fy9-tasavirta lessons/units/fy9-tasavirta`: the only change is the concept-map (`kartta`) branch heading "current and resistance" -> "current, resistance" (figures.json label and the redrawn foreignObject in `unit.md`, width 226 -> 206); nothing else changed.
- Physics unchanged: the heading still names the first branch (I = Q/t, U = RI, R = rho l/A); all map formulas identical. `units.py figures --lang en --check`: up to date; `check_i18n.py`: 0 errors.
- Verdict: PASS.

## Earlier report (round 3)
Science review of the English translation of fy9-tasavirta, round 3, 2026-11-04 (source content/fi/units/fy9-tasavirta, PASS). Round 2 hash 21d1b5094a6f3ae4.

## Blocking
None.

## Round-3 checks
- Only change since round 2: the four `\textbf{}` branch headings of the concept map (`kartta`) in `unit.md` are now English after the `figlib.translate()` fix and redraw ("current and resistance", "connections", "power and energy", "source"); only the foreignObject widths changed. All formulas in the map are unchanged and correct (I = Q/t, U = RI, R = rho l/A, series/parallel, sum of potential changes = 0, P = UI = RI^2 = U^2/R, E = Pt, U = E - R_s I, I = E/(R + R_s), Q = It).
- No other text, number, answer or tolerance changed; round-1/2 recomputations (hook, Tutki, tarkistus 2 answer 4.58 V, theory, tasks s1-s6) still apply. Decimal point throughout.
- `check_i18n.py`: en 0 errors. `units.py check`: 77 units ok. `practice.py check`: en/units/fy9-tasavirta OK, 6 tasks, 95 points. `units.py figures fy9-tasavirta --lang en --check`: up to date.

## Polish
1. `sovella/solutions.md` s6 and `teacher.md` cite *Heating and cooling of matter* without the formula suffix of the English chapter title, as the Finnish source does; faithful, no change needed.
