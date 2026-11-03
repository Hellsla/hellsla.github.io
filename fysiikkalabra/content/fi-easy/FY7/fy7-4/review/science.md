VERDICT: PASS
CONTENT-HASH: 5b563d37c08fe2f9

## Blocking

## Polish
- glossary.json "virtasilmukka" — "Magneettikentässä silmukan vastakkaisiin sivuihin kohdistuu vastakkaissuuntaiset voimat" carries the same unstated condition just fixed in meta.json (false in the speaker's radial field, lesson.md:132). The glossary is shared and outside this lesson's hash, so it does not block here — add "Homogeenisessa" there too when the glossary is next edited.

## Checked
- git diff since the passed body (2bf948f7..HEAD): only meta.json:27 changed; hash identical at start and end.
- meta.json:27 "virtasilmukka": "Homogeenisessa kentässä ... vastakkaiset voimat" — last round's B finding resolved, now consistent with lesson.md:132 (radial field, all forces along the axis) and lesson.md:86 (pole-gap motor field).
- meta.json:23 "sähkömoottori": field turns the current loop, electrical → kinetic energy; losses omitted (C).
- meta.json:31 "kaiutin": alternating current in the coil as the cause, coil and cone driven back and forth, cone makes the sound; matches lesson.md:132.
- meta.json:35 "magneettinen voima": force of a field on a current-carrying wire; consistent with lesson.md:174 and fy7-2.
- Key concepts agree with each other and with the Tiivistelmä (lesson.md:314).
- Spot recompute with own formulas: worked example F = 6,98 N ≈ 7,0 N; sim Δm(6,0 A) = 2,45 g; jumper cables 0,60 N; check-2 0,40 / 0,20 N; virhe 0,15 N; exit ticket 0,30 N — all agree with lesson-answers.py.
