VERDICT: PASS
CONTENT-HASH: b8c0ac45df8ef0e0
SCOPE: delta: new tasks s8 and s9 (text, solutions, criteria), answers.py s8/s9, changed intro sentence; s1-s7 not re-judged.

## Blocking
- (none)

## Polish
- s8 d: 7360 N has more figures than the data (0,50); use noin 7400 N.
- Terms agree with the task (vaijeri, kyltti, tanko, normaalikiihtyvyys) in the fi-easy figure alt texts; "vauhdilla" in s8 versus "nopeus" elsewhere in the same task is a small term variation, acceptable for selkeä suomi.

## Checked
- s8 recomputed: r = 15^2/3,0 = 75 m; second graph point 20 m/s, 5,3 m/s^2 -> 75 m (curve a = v^2/75 in figures.py); F = 1200*3,0 = 3,6 kN; mu g = 4,905; v_max = 19,18 m/s = 69,0 km/h; F_max = 5,89 kN, need/max = 61 %; d: 4500 N and 7357 N, ratio unchanged. Physics sound (static friction, no centrifugal force, mass cancels).
- s9 recomputed: T = 19,5*9,81/0,500 = 382,6 N; H = 331,3 N; V = 14,7 N; F_s = 331,7 N at 2,5 deg; end-moment check V = m_t g/2 = 14,7 N; m_s,max = 29,08 kg; d: T = 270,5 N (-29 %), H' = 191,3 N, hinge force falls (about 192 N). Direction of change and explanation correct.
- Task text does not reveal solution structure (no 'phases', 'twice', no 'use moments about the hinge'); s9 d "perustele laskemalla ja selitä" is neutral.
- Points: s8 4+3+5+3 = 15, s9 6+5+3+3 = 17; `practice.py check units/fy9-ympyraliike` OK for fi, en, fi-easy (9 tasks, 142 points). answers.py s8/s9 blocks match tasks.json values.
- Intro: nine tasks, equilibrium/circular motion/gravitation, task 7 note: correct.
- Figures fy5-4/kuvaaja-a (point 15 m/s, 3,0) and fy5-2/kyltti (L 1,20 m, 30,0 deg) match the task data.
- Gap: captures (shots.md) contain no screenshot of s8/s9 (the sovella stage captures show the older worked examples); 360 px layout with solutions open not judged by me, left to the visual reviewer / check_layout.py. Calculation chains are written as aligned rows in the source.
