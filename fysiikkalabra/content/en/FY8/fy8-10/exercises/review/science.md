VERDICT: PASS
CONTENT-HASH: 6afc032326200d35
Mode: full (translation review against the reviewed Finnish set)
Round 1

## Blocking
(none)

## Fixed
- exercises.json L2-05, L2-06, L3-04, L3-05 `text` — the translation held a literal backslash-n (`\\n\\n`) where fi has real line breaks, so the task text showed `\n\n` on the page (visible in open-exercises-L2-1280-5 and L3-1280-4 captures) and the a)/b)/c) parts ran together; replaced with real newlines (the same line breaks as fi).

## Polish
- solutions.md L3-03 reasonableness — "where the mass defect is almost one per cent" follows the reviewed fi wording; left as is.

## Checked
- Compared with content/fi by script: ids, levels, kinds, answers, units, tolerances, correct flags, data table cells, and every number in texts, choices, feedback and solutions.md (184 lines each, numbers equal per line; decimal point in en JSON and LaTeX where fi has a comma).
- All 8 new exercises (L1-06..08, L2-05..07, L3-04..05) read in full in en against fi; one correct option each in L1-06, L1-08, L2-07, and the distractor feedback names the same error as fi.
- Re-derived key answers: L1-07 0.511 MeV, L2-05 nickel-62 8.795 MeV, L2-06 31.99 MeV (3 electrons, 1.53 MeV), L3-04 Q 173.3 MeV and 7.11e10 J, L3-05 4.9e20 kg; all agree with fi.
- check_i18n.py en: 0 errors after the fix.
- No Finnish left in en (grep for ä/ö and Finnish words).
