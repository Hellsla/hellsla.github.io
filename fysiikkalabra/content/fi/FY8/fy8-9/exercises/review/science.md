VERDICT: PASS
CONTENT-HASH: 796546d7348c683e

## Blocking

## Polish
- exercises.json:124 fy8-9-L2-05 — `kind` says "graph" and the plan asks to plot on a log scale and read T½, but the task only subtracts and gives the 320 s quarter shortcut; no graph is drawn or read. The plan's `pa-points` graph task is also missing. Add "piirrä nettopulssimäärät logaritmiasteikolla" to b) or drop "graph" from `kind`.
- solutions.md:116 fy8-9-L2-05 — "kolme merkitsevää numeroa kuten pulssimäärissä": a two-point estimate where net 64 has a scatter of about ±8 (√N) gives T½ to about ±8 %; justify 149 s as a rounded estimate, or give ≈150 s (the full log fit gives 150 s).
- solutions.md:186 fy8-9-L3-05 c) — the task asks which process "vähentää kehon säteilyaltistusta enemmän". Decays inside the body are what give the dose, so physical decay does not reduce exposure the way excretion does. Suggest "kumpi prosessi pienentää kehon jodi-131-aktiivisuutta nopeammin" and base the answer on λ_bio = 0,140 1/d > λ_fys = 0,086 1/d. The 50,1 % vs 16,4 % comparison shows only the combined effect.
- lessons/FY8/fy8-9/answers.py:13, 23, 33 — stale comments: 16,28 % (is 16,29), "0,6943 -> 0,694" (is 0,6953 → 0,695), 6,96 % (is 6,97). The values themselves are right.
- solutions.md fy8-9-L3-02 — still justifies three figures "kuten ajassa 10,0 min"; the limiting datum is the net count rate 200 (two figures). Carried over from the earlier round.

## Checked
- All 19 numeric answers recomputed independently in one script: all match answers.py/exercises.json within tolerance.
- L2-05 log fit 150 s; L2-06 net data fit 60 s, gross reaches 100 at 70,2 s (student's 70 s right); L2-07 80/10 = 8,0, 33,2 1/s, 5,4 %.
- L3-04 data = 800·2^(−t/6 h) + 200·2^(−t/64,8 h) within 1 %; late pairs give 2,60–2,68 d (in tolerance); b), c) consistent.
- L3-05 T_eff 3,065 d, T_bio 4,96 d, λ-sum check right, assumption stated.
- L1-06 one correct option, feedback right; L1-07, L1-08 level 1, no duplicates; notation as in the lesson.
