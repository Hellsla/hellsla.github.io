VERDICT: PASS
CONTENT-HASH: 46a45e2ca835c026
SCOPE: delta: new Sovella itsenäisesti tasks fy9-voimat-s7 (skydiver) and s8 (lift and force plate) with solutions, answers.py and the changed intro sentence; s1-s6 not re-judged (en).

## Blocking
- (none)

## Polish
- s8 b) Sijoitus: the printed chain `(-1,14 m/s²) · 2,0 s = -2,29 m/s` does not multiply out (-1,14 · 2,0 = -2,28); the value comes from the unrounded a = -1,1433. Write a = -1,143 m/s² in the chain or say "(laskettu tarkalla arvolla a = -1,143)". Same in all languages.
- s8 d) Järkevyys sums to 12,25 m (2,29 + 6,87 + 3,09) while the Sijoitus row gives 12,2 m; 12,25 would round to 12,3. Use 12,23 (unrounded parts 2,287 + 6,860 + 3,087) or round the same way in both.
- s7 d) the criterion and the solution give k ≈ 0,31 kg/m in one place and 0,315 / 0,3147 in the next; use 0,3147 (or 0,315) consistently.
- s7 precision wording: a) and c) justify two significant figures "kuten luetuissa nopeuksissa", but 18,6 and 44,5 m/s have three; the true limit is Δv = 6,0 m/s (a2) and F_v with two figures. Reword the reason; the answers themselves are right.
- Task text gives m = 75 kg (s7) but the solution uses 75,0 kg; make one of them match.
- Intro lists "Newtonin lait, voimakuviot, kitkan, kaltevan tason, kytketyt kappaleet ja ilmanvastuksen" but not the lift/support force that s8 covers; consider adding "tukivoiman" (optional).

## Checked
- Recomputed with answers.py and by hand: s7 a1 = 18,6/2 = 9,3, a2 = 6,0/4 = 1,5 m/s²; F_v = 75·(9,81 - 1,5) = 623 N (85 % of mg = 736 N); v_r = 44,5·sqrt(736/623) = 48,4 m/s; k = 0,3147 kg/m; v_r' = 55,8 m/s, ratio sqrt(100/75) = 1,155 (15 %); points (0,0), (2; 18,6), (6; 40,4), (8; 44,5), (10; 46,4), (12; 47,3) all in the figure alt text of fy4-14/hyppy-vt-points. Model F = kv² stated in the task; secant at 8 s is a fair estimate.
- s8: mg = 735,75 N; a = (650 - 735,75)/75 = -1,143; v(3 s) = -2,287; a(6.0...8.7) = +0,857; stopping time 2,67 s, consistent with 2,7 s at the stated precision; s = 0,5·(7,7 + 3,0)·2,287 = 12,23 m; figure (fy4-16/ex-hissi) values 650 N and 800 N match the task. Part e explanation (N, not weight; a not v) is correct.
- Task text does not reveal solution structure; figure REUSE marked safe; alt text names (t, v, N) equal the task's; results rounded to data precision; unit language-neutral (same numbers and answers in fi, en, fi-easy).
- `practice.py check units/fy9-voimat` OK for all three languages; check_layout at 360 px OK (only the 2 known clipped formulas, not in s7/s8). Hash unchanged at start and end.
