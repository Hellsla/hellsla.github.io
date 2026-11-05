VERDICT: PASS
CONTENT-HASH: cc10e5fca522a7b1

## Delta review (2026-11-04, previous hash 678dc353273487b6)
The only change is that the "Maa" label in the tilanteet figure moved 28 px to the right (figures.py, and the redrawn SVG in unit.md). `git diff HEAD` shows nothing else. The tasks, rubrics, points (95), hints and feedback are unchanged. The figure still means the same thing for the student: the satellite panel, with the Earth labelled. Still PASS.

Round 2 (delta review of round 1 fixes; round 1 hash fc0aa5da26550049). Pedagogy review of fy9-ympyraliike.

## Round 1 Blocking: verified fixed
1. unit.md "Tasainen ympyräliike": the summary now gives the instantaneous condition (no tangential force at the highest and lowest points). A student can follow s6 b–d and tarkistus-1 from the summary without a gap. The s6 b Periaate uses the same idea.
2. inquiry.json lumilapio, Sijoitus: "takakäden suhteen", which is consistent with the pivot choice that the task teaches.

## Polish: verified
- 3: The Tutki tolerance is now 0,07, so a coarse graph reading (about 11,3 h) is accepted.
- 4: s3 d now reads "Mikä on lyhin kierrosaika, jolla alustaa saa pyörittää tällä kärryllä ja etäisyydellä?".
- 5: teacher.md Nopeat asks for a speed, and the answer is a speed.
- 7: s5 a now reads "Laske kiven massa raportin mittauksista", so it no longer gives part b away.
- 9: tarkistus-1 uses $F$ for the chain force.
- 6 and 8 are left as they were, for the developer's stated reasons. Both were Polish, so this is acceptable.

## No new problems
The task counts, the points (15/15/20/15/15/15, 95 in all) and the links are unchanged. `practice.py check` passes. In the built page the new text renders and has no console errors.
