VERDICT: PASS
CONTENT-HASH: 536d455eb8f2210b
Mode: light (teacher 2026-11-07, "kevyt katselmointi": round-2 diff since edb368de4 only)

## Blocking
- none

## Polish
- L1-02: "384 400 km on … tarkka arvo" follows the teacher's convention, but a measured mean distance is not exact. "käsitellään tarkkana" would be better.

## Checked
- diff exercises.json, solutions.md, answers.py (L1-02 rounding reason, L3-05).
- Recomputed L3-05: t_A = 2,34·10⁶ J : 85,0 W = 7,647 h, t_B = 6,111 h, difference 1,536 h → 1,5 h (key 1.5, tolerance 0,03 covers 1,455–1,545).
