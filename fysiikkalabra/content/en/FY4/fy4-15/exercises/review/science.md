VERDICT: PASS
CONTENT-HASH: 75e6a84b83ca6804
Mode: full (translation review against the reviewed Finnish set)
Round 1

## Blocking
(none)

## Fixed
(none needed: the English text already matched fi in every number and was natural)

## Polish
- [Minor] L2-03 text and solution use $850\,\textsf{l}$ as in fi; check_i18n requires the same formula, so it stays. If the Finnish is changed to litres in words or $\text{L}$, change en with it.

## Checked
- All 20 ids, kinds, answers, units, tolerances, choices (order, correct flag) and table cells equal fi in exercises.json for the 8 new tasks L1-06..08, L2-05..07, L3-04..05.
- Every number in text, choices, feedback and captions matches fi apart from decimal point (en) versus comma (fi).
- solutions.md: every number in all new sections matches fi; formulas pass check_i18n parity.
- Physics terms right: head, flow rate, rated power, efficiency, pumped-storage plant, tailwater; units MWh, GWh, kW correct.
- Part-b/c model answers (L2-06, L3-04, L3-05) carry the same reasoning and values as fi (4.3, 11.3, 8.1, 86 %, 6.00 h).
- No Finnish left in en. check_i18n en: 0 errors. Hash unchanged (no edits).
