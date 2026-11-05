VERDICT: PASS
CONTENT-HASH: b76bee1182410114

## Blocking

## Polish
- exercises.json:274 fy8-1-L3-04 — the table gives I = 0,01 µA at -0,70 V and 0 at -0,80 V, so a careful student reads Us ≈ 0,75 V and gets W = 2,35 eV, not the solution's 2,30 eV (the boxed answer is unaffected) — fix: add "jännite on mitattu 0,1 V:n askelin; estojännite on pienin taulukon vastajännite, jolla virta on nolla", or put 0,01 µA at -0,60 V only.
- exercises.json:274, 352 fy8-1-L3-04 and L3-05 — both are the same quantum-yield model (photons/s from P, electrons/s from I); L3-05 is mostly a replay with three sources — fix: leave the yield as given but make L3-05 test a new idea (e.g. which source sets Us, or the current if source B were replaced by 500 nm).
- exercises.json:107 fy8-1-L2-02 — N = Pλ/hc is still not in the lesson text (carried over); the same 650 nm / 5,0 mW task appears in fy8-4-L2-07 — fix: add one lesson line, and change the numbers in one of the two.
- exercises.json:74 fy8-1-L1-07 — marked "data" but is a two-step calculation with a yes/no conclusion; only part a) is checked — fix: relabel "concept" or put the conclusion (539 nm < 650 nm) into the answer box as a choice.
- solutions.md:56 fy8-1-L1-01..05 (carried over) — all substitutions of one form; the new L1-06/L1-08 now cover the threshold idea, so this can be dropped.

## Checked
- New L1-06 (MC, intensity vs frequency): the correct answer is not the longest or first; each distractor is a real wave-model error with repairing feedback; physics correct.
- L1-07 f0 = 5,56e14 Hz and 539 nm recomputed; L1-08 model answer uses 3,40/1,91/2,28 eV correctly.
- L2-05: least-squares fit of the five points gives h = 6,72e-34 Js, f0 = 5,57e14 Hz, W = 2,34 eV: matches the solution, 5 % tolerance fair for the ±0,02 V scatter.
- L2-06: differences 0,89–0,91 eV, D = 0,90 eV; B has the larger W; parallel-line argument sound.
- L2-07: the three points are exactly linear, slope 4,133e-15 eV/Hz, W = 2,14 eV; the error (intercept read as f0) matches the plan.
- L3-04: Nf = 2,014e15/s, Ne = 1,873e12/s, yield 0,093 %; ratio P2/P1 argument correct.
- L3-05: I = 1,81 µA, Us = 1,10 V, source B correctly rejected; answer 1,8 within 3 %.
- Levels fit (8/7/5), plan items covered, no duplicate of the worked example; every new task has a full solution with Järkevyys.
- Captures (1280 px) checked for L3-04/05: no clipping, equations wrap legibly.
