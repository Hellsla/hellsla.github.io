VERDICT: PASS
CONTENT-HASH: 18f2780582100755

## Blocking

## Polish
- lessons/FY1/fy1-5/figures.py (pick_distance) and exercises.json (L2-08, option D feedback); solutions.md (L2-08 Mallivastaus) — These label the distance walked as "Δs". The lesson defines Δs = s − s₀, and on the way back that is 0 − 6,0 m = −6,0 m, not +6,0 m. Δs equals the distance walked only when the walker moves away from the start. The option is a distractor and stays wrong either way, so nothing here is blocking. — Label the axis "matka (m)" and write "kuljettu matka" without the symbol Δs, or name the condition.
- solutions.md (L2-08 Periaate) — The sentence "kulmakerroin Δs : Δt on nopeus … Nopeus (vauhti) on suoran jyrkkyys" mixes slope and speed. A downward line has a slope whose size is the speed. Optional: write "suoran jyrkkyys kertoo vauhdin".

## Checked
- Round 1 Blocking item is resolved. The −1,0 m/s value and the "etumerkki kertoo suunnan" wording are gone from the solution and from option A. The reasoning is now "paikka pienenee → suora laskee", which agrees with the lesson's positive-velocity convention.
- Option B (pick-vt at +1,0 m/s) is now consistent, because no sign convention is used. Its feedback is correct.
- L2-08 still has exactly one correct option. C runs from 6,0 m, stays level until 4,0 s and then falls to (10 s; 0 m), consistent with 6,0 m / 1,0 m/s = 6,0 s.
- I recomputed all 19 numeric answers with my own formulas in one script, and they match answers.py. L2-05 gives 18,04 m, L3-01 gives 3419,8 vrk, L3-02 gives 41,58 h and L3-04 gives 1,33 m/s.
- The figure captions for pick-away, pick-back and pick-distance match the plotted points, and none gives the answer away.
- The rest of the set is unchanged from round 1: physics, rounding, guardrail wording and notation are all correct.
