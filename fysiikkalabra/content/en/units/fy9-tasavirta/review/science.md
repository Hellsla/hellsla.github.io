VERDICT: PASS
CONTENT-HASH: 3c616085eea3df1b

Science review of the English translation of fy9-tasavirta, round 3, 2026-11-04 (source content/fi/units/fy9-tasavirta, PASS). Round 2 hash 21d1b5094a6f3ae4.

## Blocking
None.

## Round-3 checks
- Only change since round 2: the four `\textbf{}` branch headings of the concept map (`kartta`) in `unit.md` are now English after the `figlib.translate()` fix and redraw ("current and resistance", "connections", "power and energy", "source"); only the foreignObject widths changed. All formulas in the map are unchanged and correct (I = Q/t, U = RI, R = rho l/A, series/parallel, sum of potential changes = 0, P = UI = RI^2 = U^2/R, E = Pt, U = E - R_s I, I = E/(R + R_s), Q = It).
- No other text, number, answer or tolerance changed; round-1/2 recomputations (hook, Tutki, tarkistus 2 answer 4.58 V, theory, tasks s1-s6) still apply. Decimal point throughout.
- `check_i18n.py`: en 0 errors. `units.py check`: 77 units ok. `practice.py check`: en/units/fy9-tasavirta OK, 6 tasks, 95 points. `units.py figures fy9-tasavirta --lang en --check`: up to date.

## Polish
1. `sovella/solutions.md` s6 and `teacher.md` cite *Heating and cooling of matter* without the formula suffix of the English chapter title, as the Finnish source does; faithful, no change needed.
