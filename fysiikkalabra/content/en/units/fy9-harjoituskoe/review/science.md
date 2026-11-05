VERDICT: PASS
CONTENT-HASH: 5bf67fc9ccdd56f9

Science review (round 3) of the English translation of fy9-harjoituskoe (source content/fi/units/fy9-harjoituskoe/, reviewed).

## Blocking
None (rounds 1 and 2 had none).

## Polish
1. [Minor, for the source] sovella/tasks.json s1 b: the conversion detail sits under `units_precision` and the result under `calculation`, as in the source. If the source changes, the translation should follow.

## Round-2 changes verified
- The only change since round 2 is inquiry.json activities 2–11 `"fold": "Osa I"` → `"Part I"` (git diff: 10 lines, nothing else). It is a label; no number, formula, unit, answer, tolerance, point or correct option changed, so the round-1 recomputation of every result (s1–s10 and Part I) still holds.

## Checked
- check_i18n.py: en 0 errors (it now treats `fold` as text). units.py check: 77 units ok. practice.py check: en/units/fy9-harjoituskoe 10 tasks, 165 points, same as fi.
- The preview (390 and 1280, all details open) has no comma decimals, no raw `$` and no KaTeX errors.
