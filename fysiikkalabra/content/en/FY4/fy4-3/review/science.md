VERDICT: FAIL
CONTENT-HASH: acc4496ba0b0ba9e

Light delta review (teacher 2026-11-07): the diff against origin/main and what it touches.

## Blocking
- lesson.md:602 — A: Tulos says the air resistance 96 kN has two significant figures "like the engine force 48 kN"; by the teacher's rule (2026-11-07) the integer 48 kN is exact, so 48 kN cannot limit precision, and this now contradicts fy4-4:602 and fy4-5:438 — state that 48 kN is taken as exact, so 96 kN = 2·48 kN is exact (no rounding), as in fy4-1:475

## Polish
(none)

## Checked
- lesson.md:606 Järkevyys: vector sum of thrust and air resistance zero at every constant velocity; air resistance grows with speed so greater constant speed needs greater thrust: correct causality (Newton 1), removes the old misleading "result does not depend on speed"
- 2·48 kN = 96 kN recomputed; 850 km/h correctly unused
