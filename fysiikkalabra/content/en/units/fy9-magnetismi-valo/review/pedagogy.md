VERDICT: PASS
CONTENT-HASH: 3b6f5d5631f07584

## Delta review (round 4)

`git diff dcad1b122 -- content/en/units/fy9-magnetismi-valo lessons/units/fy9-magnetismi-valo` shows only the concept map `kartta` change: figures.json "liike tai virta" → "motion, current" (was "motion or current") and the regenerated foreignObject in unit.md (x 221→230, width 141→132). Nothing else changed. The label still pairs with the branch's two cases (charge, wire), so the map still connects ideas across chapters as before. Branch heads, teacher.md wording, the tasks, the rubrics (6 long problems, 95 points) and the exit ticket are untouched. Verdict unchanged: PASS.

# fy9-magnetismi-valo (en): pedagogy review of the translation, round 3

Scope: changes since round 2 (figure redraw only; the learning design, six diagnostic questions, Apply, Check, exit
ticket and six long problems, 95 points, are unchanged and still consistent with the source per `check_i18n.py`,
en 0 errors).

## Blocking
None. The round-2 note is resolved: the concept map's branch heads now read "forces in a field", "induction",
"light", so teacher.md's "one branch at a time: forces in a field, induction, light" matches the map word for word,
and the map's aria-label uses the same names.

## Polish
None.
