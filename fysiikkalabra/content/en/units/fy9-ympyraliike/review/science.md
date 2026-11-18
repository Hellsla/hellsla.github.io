VERDICT: FAIL
CONTENT-HASH: 0230c0b74297e942
SCOPE: delta: round 1 fixes (s8 d 7360 N -> 7400 N; en: s9 b criterion translation, "centripetal acceleration" in s8 and figure alt); s1-s7 not re-judged.

## Blocking
- Still open from round 1 (part 2): the s9 figure (content/en/FY5/fy5-2/figures.json, line 22 alt "A cable runs from the outer end of the rod..." and label line 25 "vaijeri": "cable") says "cable" while the s9 task, solutions and criteria say "wire". Align to "wire" (shared chapter file; the FY5 lesson.md has neither term, so no conflict there).
- Resolved: s9 b criterion translated; s8 "centripetal acceleration" now matches the FY5 lesson term.

## Polish
- Round 1 Polish items stay recorded (s9 b 331 N vs 330 N).
- Unit chart (unit.md line 175, figures.json glossary) still says "normal acceleration"; outside this delta, the FY5 lesson accepts it as a synonym.

## Checked
- 7400 N in tasks.json s8 d and solutions.md line 606 (7357 to two figures); 61 % ratio, v_max unchanged. No 7360 left in task files.
- No Finnish remnants in en sovella tasks.json.
- practice.py check OK for fi, en, fi-easy (9 tasks, 142 points); hash unchanged at end.
- No new physics or terms introduced.
