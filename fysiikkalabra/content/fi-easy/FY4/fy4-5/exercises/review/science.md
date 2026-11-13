VERDICT: PASS
CONTENT-HASH: 39fa6ca1548ab474
SCOPE: delta added-exercise from d3c1fc3f51b9ecfb base 7db0992d648a
## Blocking

## Polish
- lessons/FY4/fy4-5/figures.py ruutu_vinot — the figure's description still says "Jääkiekko … neliö" while the task and solution (fi and fi-easy) say "kappale" — say "Kappale" in the description too (shared with fi; not physics).

## Checked
- L2-08: components from figures.py, F_1 = (10, 12) N, F_2 = (−4, −4) N on the 2,0 N grid; ΣF_x = 6,0 N, ΣF_y = 8,0 N, ΣF = 10 N, a = 10 N / 2,5 kg = 4,0 m/s² (recomputed); direction atan(8/6) = 53° from +x toward +y, stated as in fi.
- Model: frictionless horizontal ice seen from above, weight and normal force cancel vertically, so only the two drawn horizontal forces count; conditions stated in the task.
- Solution's voimakuvio block: |F_1| = 15,62 N at 50,19°, |F_2| = 5,657 N at 225°, a at 53,13°: agree with the figure; scale-bar 4,0 N = 2 squares right.
- Sanity check (21,3 N > 10 N, 6-8-10 triangle) correct; two significant figures justified.
- All 22 tasks: answer, unit, tolerance, figure, data and correct options equal the Finnish set; answers.py agrees.
