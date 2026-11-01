VERDICT: PASS
CONTENT-HASH: 39b64ad79916fa8d

## Blocking

## Polish
- lessons/FY1/fy1-3/answers.py:31 - comment says "relative error"; rename to "relative uncertainty" (comment only, number right).

## Checked
- Delta review: the only change since the last PASS is that each solution's Formula line no longer repeats the formula ("already solved for the quantity to find"). No number, symbol or physics changed.
- All numbers in exercises.json (texts, answers, units, tolerances) and solutions.md equal the Finnish source (scripted comparison, decimal comma normalised).
- All 12 answers recomputed: 0.51 s, +0.3 cm, 0.35 s, 47.5 g, 0.5 mm, 4.83 %, 10.67 mm, 12.4 cm, 10, -0.06 s, 2.0 um, 0.26 cm.
- Terms follow the guardrails: signed measurement error, positive uncertainty, half the range as scatter estimate, relative uncertainty.
- Translation (English): same physics and symbols as the source; no Finnish words left.
- check_i18n.py: 0 errors for en.
