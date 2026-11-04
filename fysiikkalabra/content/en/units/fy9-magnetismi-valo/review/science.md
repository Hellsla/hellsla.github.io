VERDICT: PASS
CONTENT-HASH: b3d1941baccbd2d3

# fy9-magnetismi-valo (en): science review of the translation, round 2

Scope: the round-1 fixes against the reviewed Finnish source. Round 1 had no Blocking science finding; the full
recomputation of every number (round 1) still holds, because the round-2 changes touch only wording: inquiry.json
lt-4 and rata feedback, solutions.md s2 common mistakes item 3, figures.json "paperiin" and three concept-map heads.
`check_i18n.py` en: 0 errors; `units.py figures fy9-magnetismi-valo --lang en --check`: up to date.

## Blocking
None.

## Polish
None remaining. Round-1 Polish 1 (s2 "multiplied into the power") is fixed: "the attenuation in decibels is divided
by ten and the power is multiplied by that number" states the error correctly. Round-1 Polish 2 is fixed: the
`ympyra` figure now says "$\overline{B}$ into the page", the same as the reused FY7 figure. The new figures.json
entries "forces in a field", "induction", "light" are physically correct names of the three branches.
