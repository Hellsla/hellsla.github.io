VERDICT: PASS
CONTENT-HASH: 9f714b739c55bc50
Mode: delta (new exercises L1-06..08, L2-05..07, L3-04..05)
Round: 1

## Blocking

## Fixed
- exercises.json (L3-04 e) and solutions.md (L3-04 Answer): "knowably travelling" was a literal, unnatural rendering of Finnish "tunnetusti"; now "travelling, in a way that can be known, through only one of the slits".

## Polish

## Checked
- Scripted comparison against content/fi: all 20 exercise ids, answers, units, tolerances, correct flags, choice order, kind lists and data-table cells equal; every number in texts, feedback and solutions equal (decimal point in JSON and LaTeX).
- All 8 solutions have the same numbers and steps as the Finnish; no formula or number differs (only the order of 1.5 m and 5 ns in L3-04 Reasonableness, same values).
- Answers rechecked: 3.06 eV, 11.4, 4.85 pm, 6.4e15 1/s, 15.6 s, 1.57e-23 kg m/s.
- Physics terms follow the Finnish (photon, momentum, probability of detection, Compton scattering).
- No Finnish left in en.
- check_i18n.py en: 0 errors.
