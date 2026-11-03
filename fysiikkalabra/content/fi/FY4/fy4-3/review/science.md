VERDICT: PASS
CONTENT-HASH: 6fbcfad746372fc8

## Blocking

## Polish
- lessons/FY4/fy4-3/figures.py:270 (collision_data) — at t = 0,15 s sin² is ~1e-32 > 0, so noise is added and both sensors read positive (+0,03 N, +0,01 N): the one point where the readings are not opposite, while the inquiry feedback (tormays) says they mirror each other at every instant — gate the noise on `F > 1e-6`.
- assets/sims/fy4/fy4-3/sim.js:1190 — the (t, v) graph stops at 6 s, so a frictionless run with v0 ≤ 2 m/s (push + 12 m slide > 6 s) leaves the graph before the run ends; tmax 8 or scale to the run.
- assets/sims/fy4/fy4-3/sim.js:1264 — the readout `t` is time since release while the graph's `t` includes the push; the howto says this, but naming it `t_liuku` in the readout would avoid a mismatch with the graph.
- lesson.md Esimerkki, Yksikkömuunnokset — "tulos saadaan suoraan kilonewtoneina: 48 kN = 48 000 N" states a conversion that is then not used; drop the second clause or use it.

## Checked
- Recomputed in one script: F_v = 2·48 kN = 96 kN; sim push a = 9,0 m/s², hand force 130/110/100/90 N; slides 1,125/2,25/4,5 m in 0,75/1,5/3,0 s; frictionless 12 m in 4,0 s; G = 98,1 N; exp-1 answer s = ½mv0²/5,0 N = 9,0 m (and its mistakes); siirto 680 N (mistakes 160, 420, 0). All match lesson-answers.py and the texts.
- sim.js: release at x = 0, lane end at 12 m from release, so s and tl in simState match the 12 m / 4,0 s claims; friction only while moving; exp-1 locks v0 and varies only pinta.
- Collision data (figures.py): peak −4,02/+3,94 N at 0,10 s, contact 0,05–0,15 s, 0,07 s ≈ ∓1,4 N as the feedback says; signs right (A pushed left, B right).
- Force figures (curling, luistelijat, auto, kone, malli-lamppu): forces, directions, points of application, equal arrows where net force is zero (kone: F_v = F_1 + F_2), third-law pairs on separate diagrams, velocity blue and off the body; no forward force on the curling stone.
- First law stated with zero net force, vakionopeus including direction and rest; third law: equal, opposite, same kind, different bodies; G and N on the book correctly not a pair (check-2, Yleinen virhekäsitys).
- Conditions stated: rolling resistance neglected for the car, air neglected for the box/conveyor, frictionless surface flagged as a thought experiment, model values named.
- Every choice item has exactly one correct option; distractor feedback correct (hevonen–kärry, conveyor belt without friction at constant velocity, mass vs force in collision).
- check-3 lamp: two forces, criteria and model answer correct; exit ticket answers agree with the theory.
- Scope within FY4 "kappaleiden vuorovaikutus ja voima sekä Newtonin lait"; second law only previewed.
- Hash identical at start and end.
