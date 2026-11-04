VERDICT: PASS
CONTENT-HASH: 367c32d54eaac2ac

## Blocking
(none)

## Fixed
- solutions.md fy3-16-L1-08 Conversions — typo "joulejaan" → "jouleina" (the Finnish source wording "jotta energia on joulejaan" was also simplified into two short sentences).

## Polish
- none

## Checked
- Delta review of the 8 new tasks (L1-06..08, L2-05..07, L3-04..05) against the reviewed Finnish: ids, levels, kinds, answers (incl. the text answers of L1-06/07), units, tolerances, correct flags and choice order, data table cells all identical (scripted comparison).
- Every number in exercises.json and solutions.md equals the Finnish (decimal comma normalised to point, `{,}` handled); all 21 solution sections compared one by one.
- Answers recomputed: 250 s, 76 %, 139 W/K, 2.9 h, 480 EUR, 590 kW.
- Feedback of each wrong choice keeps the Finnish physics (no "cold flows", equilibrium, c vs latent heat).
- Plain Finnish (selkosuomi): short sentences, terms explained (nettomääräisesti eli kokonaisuutena, lämmönjohtavuus); no step or reasoning removed.
- check_i18n.py: 0 errors.
