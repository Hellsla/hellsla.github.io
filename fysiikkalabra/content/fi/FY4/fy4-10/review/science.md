VERDICT: PASS
CONTENT-HASH: 1b4a6b4ef5557e43

## Blocking

## Polish
- assets/sims/fy4/fy4-10/sim.js:36–48 (fitRun) — the arrows stay readable but can get short. Over the 3924 settings that have a collision, the velocity scale is cut in 150 (wide) and 245 (narrow) of them, to as little as 0,46 (wide) and 0,39 (narrow) of its usual value. The worst case is a chase that ends near the right end, e.g. kimmoisa, 0,60 + 0,60 kg, v1 = 1,0, v2 = 0,5 m/s. There the longest arrow is about 48 px on screen at 1280 px, about 24 px on a 360 px phone (box 294 px), and v1′ = 0,5 m/s is about 12 px, mostly arrowhead. The experiment settings are not cut at all (ratio 1,00). A floor (e.g. 0,6 × the default) combined with a slightly later start position for glider 2 would help, but this is optional.
- lessons/FY4/fy4-10/lesson-answers.py:12 — still says "Velocity Verlet"; model.js uses RK4.
- inquiry.json `simulaatio.calc` — E_sis also counts the bumper's energy when it relaxes off contact (kimmoton). "lasketaan puskurin vaimennuksen tekemästä työstä" leaves that out, though the `model` text covers the velcro case.
- sim.js:224, 242 — the group label *nyt* could read *jälkeen* once the run has ended, to match the readout.

## Checked
- Round-2 blocking item fixed. I wrote my own sweep, not a copy of fitRun (scratchpad r3/sweep_r3.js): it uses the model's own steps up to the end of the collision. It covers 6246 settings per layout, wide and narrow. No arrow tip ever leaves the 0–600 px canvas. No run ends with the gliders in contact and no "after" values (0 cases, down from 153 wide and 245 narrow).
- In the real preview, run through Playwright at 360 and 1280 px, four cases reach "after" with the right values: the round-2 freeze case (0,40 + 0,40 kg, 0 / −0,6 m/s → −0,600 / 0,000), the worst case for scale (→ 0,500 / 1,000), 0,20 + 0,60 kg at 1,0 / −0,9 m/s (→ −1,850 / 0,050), and tarra (→ 0,300 / 0,300).
- Each run uses one scale, so arrows before and after the collision can still be compared. The only arrows hidden for being under 4 px are values of 0,05–0,07 m/s or kg·m/s (6 in wide, 70 in narrow).
- `node tests/models/fy4-10.test.js`: 4791 checks pass.
- I recomputed the experiments in closed form. Elastic: (0,200; 0,800), (0; 0,600), (−0,120; 0,480). Sticky: 0,400 / 0,300 / 0,240 m/s, with E_k′ 0,048 / 0,036 / 0,029 J. Explosion: (−0,632; 1,265), (−0,775; 0,775), (−0,849; 0,566), each with 0,24 J. All agree with the feedback and with lesson-answers.py.
- Lesson numbers check out: worked example 1,14 → 1,1 m/s, with E_k 38,3 → 32,5 kJ (15 %); 0,30 m/s and 0,072 → 0,036 J; v/√2 = 0,42; virhe 0,025 (wrong value 0,475); siirto 1,0 (distractors 0,706 and 5,76); check-2 0,15 (distractors 0,60 and 0,20); kertaus 0,30.
- Physics: conservation is derived from Newton's third law, and its condition (impulse of external forces negligible) is stated in the text, the summary, the exit ticket and the solutions. Explosion and recoil are correct, and so is the billiard argument with its real-world caveat.
- Every choice item has exactly one correct option, and each distractor's feedback is correct.
- The hash is unchanged at the end.
