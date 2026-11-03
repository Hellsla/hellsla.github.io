VERDICT: FAIL
CONTENT-HASH: d390f27b68875a74

## Blocking
- exercises/exercises.json:8 (fy5-2-L1-01) — A: the new crowbar task asks for a force and the answer is 960, but "unit" is still "m" (left over from the old seesaw task), so the page shows 960 m — set "unit": "N".

## Polish
- exercises.json (fy5-2-L1-01) — the moment arms 0,050 m and 0,60 m are used for vertical forces, so they must be horizontal distances; add "vaakasuunnassa" as was done for L1-03 (a tilted crowbar's distances along the bar are not the arms).

## Checked
- L1-01 recomputed: F_n = 80 N · 0.60 m / 0.050 m = 960 N; answers.py matches; the force diagram in the solution (hand down, nail pulls the claw down on the other side, fulcrum up) is right.
- L1-03 now gives the handles' horizontal distance (round 1 polish fixed); 207 N unchanged.
- L2-04 added elbow joint force: 448.65 − 49.05 − 15 = 384.6 N downward (compression), correctly reasoned from ΣF = 0.
- L2-03 new figure "hylly": to scale (edges 48 : 216 px = 0.400 : 1.80 m, front edge 12.5° from vertical, CoM directly above P, legs d/2 and h/2 drawn); the new solution geometry gives tan α = d/h correctly; 12.5° unchanged.
- L3-02 now says the cable goes to the wall above the hinge; new figure "kyltti" to scale (cable slope 152.5/264 → 30.0°, sign at the outer end); T = 196 N unchanged.
- L3-01 and L2-02 solution wording changes only; numbers unchanged (3.33 m, 560 N).
- All other answers unchanged and recomputed in round 1; answers.py output agrees with exercises.json.
