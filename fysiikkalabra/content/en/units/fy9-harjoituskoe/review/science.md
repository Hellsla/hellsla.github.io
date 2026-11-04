VERDICT: PASS
CONTENT-HASH: 1e30cf3d05232256

Science review (round 2) of the English translation of fy9-harjoituskoe (source content/fi/units/fy9-harjoituskoe/, reviewed).

## Blocking
None (round 1 had none).

## Polish
1. [Minor, for the source] sovella/tasks.json s1 b: the conversion detail sits under `units_precision` and the result under `calculation`, as in the source. If the source changes, the translation should follow.

## Round-1 fixes verified
- s5 b criterion 0 now reads "rays at larger angles of incidence are totally reflected" (matches solutions.md).
- s3 c detail now reads "a relative change of $0.028\,\%$".
- I changed s3 c "by how many per cent has it changed?" to "by what percentage has it changed?" myself (wording only).

## Checked
- The round-2 diff against the round-1 text touches only wording (s3 c, s5 b, s7 b, s10 a, s10 e criterion, the s8 figure description); no number, formula, unit, answer, tolerance, point or correct option changed. The round-1 recomputation of every result (s1–s10 and Part I) therefore still holds.
- check_i18n.py: en 0 errors.
- The preview has no comma decimals and no KaTeX errors.
