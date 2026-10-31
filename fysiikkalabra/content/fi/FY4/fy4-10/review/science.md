VERDICT: FAIL
CONTENT-HASH: 7ab0c273e39f0f3d

## Blocking
- assets/sims/fy4/fy4-10/sim.js:81 (`if (outside()) R.done = true`) — **A**. The round-1 item is fixed: in my sweep of every control setting (6246 per layout, wide and narrow), no arrow tip ever leaves the 600 px picture, and the red force arrows stay inside too. But the new check also stops the run while the gliders are still touching, so `after` is never set and the readout shows "Jälkeen: …" with the collision frozen half-way (E_p ≠ 0). This happens in 153 settings in the wide layout (chase collisions that start near x ≈ 1,6 m; v2 > 0) and in 245 settings in the narrow layout. 74 of the narrow cases are plain head-on settings into a glider at rest, e.g. kimmoisa, 0,40 + 0,40 kg, v1 = 0, v2 = −0,6 m/s: the v̄1 arrow starts at X = 132 px and is 124 px long, so it crosses the 6 px margin as soon as glider 1 is pushed 2 cm to the left. Another 15 narrow settings lose a collision before contact. If the stop is simply skipped during contact, tips overshoot by up to 69 px, so that is not enough. — Fix: at `restart()`, run the model once to its "after" moment (it is cheap) and set VS/PS so that every tip stays inside through that run. Alternatively, never end a run between `contact` and `after`, and shrink the narrow scale (e.g. 110 px) so it has room.

## Polish
- lessons/FY4/fy4-10/lesson-answers.py:12 — still says "Velocity Verlet"; model.js uses RK4 (unchanged from round 1).
- inquiry.json `simulaatio.calc` — E_sis also includes the energy of the bumper left compressed (velcro) and of the spring relaxing off contact (kimmoton); add "ja puristuneeksi jääneen puskurin energiasta".
- sim.js pChart/eChart — the group label *nyt* could read *jälkeen* once the run ends, to match the readout.

## Checked
- The experiments of inquiry.json, in both layouts, all reach "after" before the run stops. Elastic (0,40 kg → m2 0,20/0,40/0,60): (0,200; 0,800), (0; 0,600), (−0,120; 0,480). Sticky: 0,400/0,300/0,240 m/s with E_k′ 0,048/0,036/0,029 J. Explosion: (−0,632; 1,265), (−0,775; 0,775), (−0,849; 0,566), p = 0, E_k′ 0,24 J. All match my closed forms and the feedback texts.
- No arrow is outside the picture at the start of any setting. While drawn, every tip stays ≥ 0 px from the canvas edge.
- `node tests/models/fy4-10.test.js`: 4791 checks pass (momentum exact, E_k + E_p + E_sis = E0, E_sis ≥ 0).
- Model: F on glider 2 and −F on glider 1, never pulling. Velcro uses critical damping and sticks at v_rel = 0, with E_p → E_sis. The explosion holds ½·300·0,04² = 0,24 J. The energy column stays at the dashed E0.
- Lesson numbers recomputed: example 1,14 → 1,1 m/s, 38,3 → 32,5 kJ (15 %); 0,30 m/s, 0,072 → 0,036 J; v/√2 = 0,42; virhe 0,025; siirto 1,0 (0,706 explained); check-2 0,15.
- The choice items each have one correct option, and every distractor's feedback is right. Conservation conditions are stated throughout.
- The hash is unchanged at the end.
