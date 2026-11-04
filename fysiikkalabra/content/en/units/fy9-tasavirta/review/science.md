VERDICT: PASS
CONTENT-HASH: 21d1b5094a6f3ae4

Science review of the English translation of fy9-tasavirta, round 2, 2026-11-04 (source content/fi/units/fy9-tasavirta, PASS).

## Blocking
None.

## Round-2 checks
- Only change since round 1: two reworded sentences in `inquiry.json` (hook text, tarkistus 2 prompt). The tarkistus 2 data (0.30 A / 4.40 V, 0.80 A / 4.10 V) and answer 4.58 V, tolerance 0.02, are unchanged; E = 4.40 + 0.30 * 0.60 = 4.58 V with R_s = 0.30 V / 0.50 A = 0.60 Ohm.
- `check_i18n.py`: en 0 errors. `practice.py check`: en/units/fy9-tasavirta OK, 6 tasks, 95 points. `units.py figures fy9-tasavirta --lang en --check`: up to date.
- Round-1 recomputations of every number (hook, Tutki, theory, tasks s1-s6) still apply; terminology (emf, internal resistance, terminal voltage, short-circuit current, resistivity, internal energy) unchanged and correct. Decimal point throughout.

## Polish
1. `sovella/solutions.md` s6 and `teacher.md` cite *Heating and cooling of matter* without the formula suffix of the English chapter title, as the Finnish source does; faithful, no change needed.
