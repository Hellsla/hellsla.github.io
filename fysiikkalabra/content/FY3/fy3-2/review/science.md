VERDICT: PASS
CONTENT-HASH: e1ab5e19c7f4b103

## Blocking

## Polish
- inquiry.json:92 — pred-2 feedback on "Työ ja teho pysyvät samoina" says "mittausten mukaan", but these are simulation values, which the brief says to call model values — write "mallin arvojen mukaan".
- inquiry.json:65 — "Nelinkertainen työ vaatisi, että sekä voima että matka kaksinkertaistuvat" is too strong, because quadrupling only the distance also gives four times the work — write "syntyisi esimerkiksi, jos sekä voima että matka kaksinkertaistuisivat".
- sim.js:997 — at 390 px the enlarged "W = pinta-ala" title is cut off at the top edge of the canvas (shots/fy3-2-exp-exp-2-390.png). This is cosmetic only — move it down or shrink it when k > 1.

## Checked
- All 12 exercise answers were recomputed independently and match exercises.json and answers.py within the 2 % tolerance (L2-03 250,155 kJ → 250 kJ; L3-02 588,6 J → 590 J; L3-03 45,4 min → 45 min). The Järkevyys checks in solutions.md hold (36,7 m; 1962 J; 8,34 kN; 16,7 N).
- Formulas: W = Fs carries its condition (constant force along the motion), and work as the area under (s,F) uses rectangles, triangles and trapezoids. W = Gh = mgh holds for a lift at constant speed, and P = W/t = Fv for steady motion. None of them uses E_k, E_p, cos α or Newton's laws, so they stay within the FY3 scope.
- Worked example: solved symbolically first, ½·40 N·0,20 m = 4,0 J, with an average-force cross-check. Figure 4 really is to scale (0,20 m ↔ 400 px, 40 N ↔ 200 px). Figures 1–3 are physically right: the carrying force is perpendicular to the motion (W = 0), the lifting force is parallel to it, and A₁ + A₂ are drawn correctly.
- Inquiry numbers: 98 N; 600/1200 J; 120 → 30 W; 1960 J ≈ 2,0 kJ; check-1 gives 1 : 3 (areas 5 and 15 units); check-2 gives 180 J, with distractors 240 and 120; siirto gives 240 W, with mistakes 9,6 and 0,24. Each correct option is right, and each wrong option's feedback is physically sound.
- Joule table: 19,6 J per drop. The Q/W ratios of 0,990–0,992 match "about one per cent" and heat loss as the cause. The table is labelled as illustrative values, not measurements.
- Experiments: exp-1 locks F and t and varies s; exp-2 locks F and s and varies t. Both start from F = 60 N, s = 10 m, t = 5 s, and simState gives W and P at those values. The setups isolate the varied parameter.
- sim.js implements W = Fs and P = W/t at constant speed (friction equal to the pull, so the work becomes heat). Nopeus changes only the pace of the animation. Its limits are stated in `model`. `test_sims.py fy3-2` passes now (22 assertions, sweep finite), so the "FAIL sims" in the packet does not come from this lesson.
- pred-3 / hook / exit ticket: W = 0 for horizontal carrying at constant speed (air resistance neglected), and 98 J for lifting 10 kg by 1,0 m. The two lifts do the same work, and the faster one needs twice the power.
- Content hash was e1ab5e19c7f4b103 at both start and end.
