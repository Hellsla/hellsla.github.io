VERDICT: PASS
CONTENT-HASH: f1b1e5d7059ef330

## Blocking

## Polish
- solutions.md fy4-7-L3-02 — the angle 40° is given with two significant figures, so the stated reason for three figures (mass and length only) is incomplete. Either give the angle as 40,0° in the task or justify the rounding. 1,4 J stays inside the 2 % tolerance either way.
- solutions.md fy4-7-L2-03 Järkevyys — "kirja on pöydän pinnasta matalammalla kuin lattiasta" is awkward. Suggested wording: "kirja on pöydän pinnan yläpuolella vähemmän kuin lattian yläpuolella".

## Checked
- Recomputed all 12 answers with my own formulas, and all match answers.py and exercises.json: 240 kJ, 196 J, 295 J, 8,48 kJ, −255 J, 422 kJ, 53,6 m/s, 13,5 J, 14,9 m/s, 126 km/h, 1,38 J, 214 J.
- Every solution has all seven stages and solves symbolically before substituting. The conversions are right (90 km/h = 25 m/s, 57 g, the tonne ratio needing no conversion in L3-01).
- The sign convention below the zero level (L1-05) and the zero-level choice (L2-03) are correct.
- The pendulum height h = L(1 − cos α) is correct.
- L3-03: the energy lost is ½mv² − mgh, with the no-push condition stated in the task. The 16 % check is consistent.
- The magnitudes in the reasonableness checks are realistic: a 190 km/h serve, a 54 km/h model plane, 741 kJ for both vehicles.
- Rounding to the data's figures stays inside the tolerance (rounded_ok checks included).
- The physics stays within FY4 scope (E_k, E_p, E_mek; no work–energy theorem needed).
