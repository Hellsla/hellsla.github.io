VERDICT: PASS
CONTENT-HASH: 259dd438b58d9b7c

## Blocking

## Polish
- content/en/FY5/fy5-5/inquiry.json:343 — the transfer task now works with the force F = γMm/r², but the feedback for 6378 still gives the reason as "$g \propto \tfrac{1}{r^2}$". That is correct (F = mg), but it brings back the extension quantity g on the core path. The Finnish has the same line — use $F \propto \tfrac{1}{r^2}$ in both.

## Checked
- Transfer task: F(R+h) = ½F(R) gives (R+h)² = 2R², so h = (√2 − 1)·6378 km = 2641.9 km → 2640 km (answer, unit and tolerance unchanged). M and m cancel, as the solution says; the hints and the reasonableness check (6378/9020)² = 0.500 are right.
- The extension note on "Gravitational field strength" names the next subsection correctly (*The field on different celestial bodies*, line 339). Its core path (Newton's law, and weight at the Earth's surface = the gravitational force) is correct at this level (rotation ignored, a C simplification).
- Summary: "weight at the Earth's surface is the gravitational force, G = mg", and the extension line keeps g = γM/r² as the acceleration of free fall, unit m/s². Consistent with the theory.
- learn/deepen split: the field-strength goal has moved to "deepen", and "Find the error" (a g calculation) is now titled Extension. This is consistent.
- Exit ticket: the re-broken chain gives 6.7·10⁻¹¹ N with the same numbers and units.
- lesson-answers.py: the comment change only; the value 2642 km is unchanged.
- Compared with the Finnish (lesson.md 285, 692; inquiry.json 343): the same physics and numbers.
- Hash unchanged at start and end.
