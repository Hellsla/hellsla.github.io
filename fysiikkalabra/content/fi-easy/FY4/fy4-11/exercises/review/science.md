VERDICT: PASS
CONTENT-HASH: 1c4ee976ee44ae1c
Mode: full

## Blocking

## Polish
- solutions.md:865–866 (L3-04 c and Järkevyys) — the impact speed at 80 km/h is 14,31 m/s = 51,5 km/h; "noin 51 km/h" comes from rounding 14,3 m/s first — write "noin 52 km/h" (or "noin 51–52 km/h").
- solutions.md:936 (L2-10 Periaate) — "vain yksi vaakasuora voima: kitka" assumes that air resistance is neglected and the road is level; the calculator's text does not say so — add "kun ilmanvastus jätetään huomiotta".
- exercises.json L2-10 — the answer field (69,4 km/h) follows the calculator's parameters as read on 16.11.2026 (1 s, 9 m/s²); the solution says so and tells the student to use the values they read; if the calculator changes, the field must follow.

## Checked
- Hash the same at the start and the end (1c4ee976ee44ae1c).
- All 22 numeric answers recomputed with my own formulas in one script; all inside tolerance and equal to answers.py (L2-05 a = 7,85; L2-06 60,0 km/h; L3-01 36,7 km/h; L3-02 11 253 N; L3-03 35,9 m; L3-04 fit t_r = 1,21 s, a = 5,10 m/s², v_max = 66,0 km/h; L3-05 0,79 m, 10 kN, 18 kN).
- L2-10 b: s_j = v0²/(2a) derived from t_j = v0/a and the triangle; 6,86; 15,43; 27,43; 42,87 m round to the calculator's 7, 15, 27, 43 m; 40 → 80 km/h four-fold.
- L2-10 c: 80 km/h 49,66 m < 50 m (margin 0,3 m, the calculator shows 50 m by rounding, practical conclusion stated); 100 km/h: 22,22 m left, v² = 771,6 − 400,0 = 371,6 m²/s², v = 19,28 m/s = 69,4 km/h; with the rounded 28 m 69,8 km/h, inside tolerance 0.03.
- L2-10 d: ice 164,6 m + 22,2 m = 186,8 m; six-fold braking distance as 9 : 1,5; μ = a/g = 0,92 and 0,15 from ΣF = ma, mass cancels.
- L2-10 e: ABS cannot raise μ; 1,25² = 1,56 (+56 %), calculator 27 → 43 m.
- Source (coordinator's record, 16.11.2026): task gives no reaction time or deceleration (read from Lisätietoa); solution states 1 s, 9 and 1,5 m/s², rounding to a metre and the table values exactly as recorded; solution is dated and names itself an example.
- Fixes: L3-05 answer 18 kN with two figures (Δv = 4,5 m/s), answer 18.0 unchanged; L2-05 "kahden tai kolmen numeron"; L3-06 11 kN (computed 10,5 kN), tolerance 0.05 accepts 11.
- L2-08: exactly one correct option (2 : 4 = 0,50); each distractor's feedback names its error correctly.
- Figures ex-tv-jarrutus (20 m + 25 m = 45 m) and ex-tv-tyyny (17,5 kN − 7,0 kN = 10,5 kN) give the values at grid crossings; descriptions match.
