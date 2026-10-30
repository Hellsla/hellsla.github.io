VERDICT: FAIL
CONTENT-HASH: 51066ea1dc1a738f

## Blocking
- lesson.md:394 (figure `esimerkki`, figures.py:209 `T_y` lab=(-28, 4)) — A, an ambiguous force name in the model diagram. The $\overline{T}_y$ label (centre 302; 114) sits 16 px from the tip of the solid $\overline{N}$ arrow (290; 124,5) and 28 px from the dashed $T_y$ tip (330; 110). The $\overline{N}$ label is 31 px away, on the far side. In the 390 px capture, the solid normal-force arrow reads as "$\overline{T}_y$" and the dashed component looks unnamed. This breaks the checklist item "each force named unambiguously". It also blurs rule 7 (components are not forces) in the very figure that teaches it. — Put the $T_y$ label right of its dashed arrow, between it and $\overline{T}$ (x ≈ 336–370, y ≈ 100). Or move N to the left of G (cx − 20) with its label on its left, so that nothing solid ends near the $T_y$ label.

## Polish
- sim.js:139 — in push mode at about 40°, the F_x label still touches F's arrowhead (from round 2). — Offset it in push mode.

## Checked
- Slope panel (`suunnat`): N now starts on the bottom face, 11,8 px uphill of its centre (perpendicular offset 0,1 px). Its shaft clears G's shaft and passes 11,9 px from G's tail. N = 79,9 px ≈ G cos 25° = 79,8 px, and F_μ = 37,1 px ≈ G sin 25° = 37,2 px, along the slope from the upper corner. The vector sum is (0; −0,5) px: equilibrium holds. Placing N's tail anywhere on the contact face is physically fine. The caption still matches.
- Other `suunnat` panels: floor G = N = 88 px; lamp T = G = 77 px; balloon F_noste 100 = G 40 + N 60 px, with N pointing down onto the top face.
- `esimerkki` to scale (1,151 px/N): N 71,7 N, T 80,1 N at 35,07°, F_μ 30,0 N, T_x and T_y are consistent.
- `tilanne`: N = G − T sin 30° in pixels (84 = 113 − 29).
- Notation: no \mathbf, \vec or \boldsymbol is left in the lesson, the inquiry, the figures or the sim strings. The overlines sit on vectors and the magnitudes stay plain (N, T sin α, F_x in the equations).
- Recomputed in one script: a = 2,96 m/s², N = 71,8 N, 5,46 m/s²; exp-1: 50 N, 146,2 N, 5,0 and 2,5 m/s²; interpret: 4,89 N, 1,73 N; siirto 22,6 N; check-2 51,2 N (mistakes 39,2, 61,0, 102); check-3 52,0 N and 147,7 N. All agree with lesson-answers.py and the text, and the tolerances admit the 2-figure answers.
- Lift options a–d: each wrong option has exactly one error and its feedback is right. In `virhe`, only F is wrong. Both unchanged.
- The inquiry options, feedback, exit ticket and sim model (N = G ∓ F sin α, a = F cos α / m, frictionless ice stated) are unchanged and correct.
- The `FAIL sims` line in checks.txt does not reproduce: test_sims.py fy4-5 passes now (17 assertions, labels checked, fi, en and fi-easy).
- Hash 51066ea1dc1a738f at start and end.
