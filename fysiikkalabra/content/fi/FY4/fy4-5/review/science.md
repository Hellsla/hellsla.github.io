VERDICT: PASS
CONTENT-HASH: cbfcf1ce4bc5e912

## Blocking

## Polish
- sim.js:139 — in push mode at about 40°, the F_x label still touches the arrowhead of F (carried over from rounds 2–3). — Offset the label in push mode.

## Checked
- Round-3 blocker fixed (figures.py:209, lesson.md:394). The $\overline{T}_y$ label (centre 326; 94) now sits above its dashed tip (330; 110), 16 px away, and 47 px from the N tip. In the 390 px and 1280 px captures each label names exactly one arrow. The components are dashed and T is solid, so rule 7 reads correctly.
- `esimerkki` is to scale and was not changed apart from the label. N is 71,7 N, T is 80 N at 35°, F_μ is 30 N, and T_x and T_y are consistent. The aria-label matches.
- Slope panel of `suunnat`: N is perpendicular to the bottom face and starts uphill of where G crosses it. The friction arrow leaves the uphill bottom corner (528,5; 157,3) and points up the slope. The forces sum to zero.
- Other `suunnat` panels: floor (N = G), lamp (T = G), and the helium balloon (the ceiling's N points down, F_noste = G + N).
- `tilanne` and `komponentit`: N < G for an upward pull. F_x and F_y are dashed, from the point where F acts.
- Recomputed in one script: example a = 2,96 m/s², N = 71,8 N, no friction 5,46 m/s², T_y = 45,9 N. exp-1: 146,2 N, 50 N, 5,0 and 2,5 m/s². Interpret: 4,89 N. Siirto: 22,62 N. Check-2: 51,2 N, with the mistakes 39,2, 61,0 and 102 N. Check-3: 52,0 N and 147,7 N. All agree with lesson-answers.py and the text.
- Predictions, `virhe`, the lift options a–d, check-1, the model answers and the exit ticket are all correct. Exactly one option is right in each, and each distractor's feedback is right.
- The sim model is N = G ∓ F sin α and a = F cos α / m on frictionless ice, and the text says so. It matches calc/model, and exp-1 isolates α.
- The `FAIL sims` line in checks.txt does not reproduce. test_sims.py fy4-5 passes in fi, en and fi-easy.
- The hash is cbfcf1ce4bc5e912 at both start and end.
