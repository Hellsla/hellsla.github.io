VERDICT: PASS
CONTENT-HASH: 4ee5450452140e8b
Mode: full (translation review against the reviewed Finnish set)
Round 1

## Blocking
(none)

## Fixed
- exercises.json L3-05 d): "the wavelength shorter than which a photon can release" changed to "the wavelength below which a photon can release" (same meaning, natural English).

## Polish
(none)

## Checked
- All 8 new exercises (L1-06..08, L2-05..07, L3-04..05) and the 12 older ones compared with content/fi by script: ids, levels, kinds, answers, units, tolerances, correct flags, choice order, data-table cells and figure id are identical.
- Every number in exercises.json and solutions.md has the same multiset as in fi per exercise (decimal sign normalized); formulas pass check_i18n parity.
- Re-derived by hand: L1-08 14; L2-05 289/400 = 72.25 % and 92.0 % at 0.15 nm; L2-06 40/80/120 Hz; L2-07 expected 200 vs 205; L3-04 slope 13.6 eV, n = 3..6, 397 nm; L3-05 590.5 nm and 241.2 nm. All agree with the answers.
- Conditions and hedges kept: chosen probability, 90 % boundary, about every tenth, at least the ionisation energy.
- No Finnish left in en (grep); data cells use a decimal point (0.00–0.05 nm etc.), LaTeX uses a point.
- check_i18n.py en: 0 errors.
