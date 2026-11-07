VERDICT: FAIL
CONTENT-HASH: 103a331487484b75

Light delta review (teacher 2026-11-07): the diff against origin/main and what it touches.

## Blocking
- lesson.md:438 — A: Tulos says the precision of both results is limited by g = 9,81 m/s², but a = (T cos α − F_μ)/m uses no g; with 12 kg, 80 N, 30 N and 35° exact, a = 2,961… is not limited by any datum — say that a is computed from exact values and given to three figures, and that g limits only N

## Polish
(none)

## Checked
- lesson.md:438 recomputed: T_x = 65,53 N, T_y = 45,89 N, a = 35,53/12 = 2,961 m/s², N = 117,72 − 45,89 = 71,83 N: 2,96 m/s² and 71,8 N correct
- N limited by g (3 s.f.): correct
- Järkevyys: 71,8 + 45,9 ≈ 118 N, frictionless 65,5/12 ≈ 5,5 m/s²: consistent with the new values; no stale 3,0 m/s² / 72 N / 46 N elsewhere (inquiry.json, exit ticket)
