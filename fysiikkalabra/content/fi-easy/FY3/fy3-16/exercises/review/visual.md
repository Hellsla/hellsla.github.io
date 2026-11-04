VERDICT: PASS
CONTENT-HASH: 367c32d54eaac2ac

## Blocking
(none)

## Fixed
- solutions.md fy3-16-L1-08 Conversions — typo "joulejaan" → "jouleina" (the Finnish source wording "jotta energia on joulejaan" was also simplified into two short sentences).

## Polish
- none

## Checked
- Data tables (L2-05, L2-06, L3-04): caption, column headers and cells translated; numbers and units identical; the table renders without overflow in the screenshots (fy3-16-open-exercises-L2/L3 captures).
- LaTeX identical to the Finnish except translated subscripts (`T_\text{out}` / `T_\text{ulko}`) and decimal point vs comma where the language requires it.
- Units are wrapped in `\text{}` with thin spaces as in the Finnish; no Finnish left in en.
- Plain Finnish (selkosuomi): short sentences, terms explained (nettomääräisesti eli kokonaisuutena, lämmönjohtavuus); no step or reasoning removed.
- check_i18n.py: 0 errors.
