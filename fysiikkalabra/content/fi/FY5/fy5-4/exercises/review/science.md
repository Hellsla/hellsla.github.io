VERDICT: PASS
CONTENT-HASH: 4b2e59499271c581

## Blocking

## Polish
- exercises.json:272 (fy5-4-L3-04) — the new wording says a_n "laskettiin nopeudesta ja radan muodosta", and part a) then asks for the radius from v and a_n. That is circular. Write instead "kiihtyvyysanturin lukemasta on vähennetty painovoiman osuus", or "normaalikiihtyvyys mitattiin anturilla (painovoiman vaikutus poistettu)".
- solutions.md (L3-04 Vastaus) — gives ≈ 260 N with two significant figures, but the answer box stays 257.4. That is within the 2 % tolerance, so fine. Optionally set the answer to 260 so that it matches the solution.
- solutions.md (L3-04 Järkevyys) — the energy check could name its source: "mekaanisen energian säilyminen: ½mv₁² = ½mv₂² + mg·2r".

## Checked
- Round-1 Blocking fixed. In L3-04 the bottom row is 27,2 m/s and 53,2 m/s², so r = 13,91 m against 13,90 m from the top row. v₁² − v₂² = 543,8 and 4gr = 545,6 m²/s², so the data now agree with energy conservation. N_ala = 3780,6 N = 6,42 mg, N_ylä = 257,4 N, v_min = 11,68 m/s < 14,0 m/s.
- Round-1 Blocking fixed. L1-08 now starts from 1,0 m/s² and gives 9,0 m/s² ≈ 0,92 g. The task and its reasonableness check now agree.
- L2-05: on a smooth table the weight and the table's support force cancel, and the horizontal string tension is the only horizontal force, so the model is exact. Least squares gives 25,0 g and the line through (49; 1,53) gives 24,98 g; the solution states that it was drawn by eye.
- L3-05: the algebra step (divide the equations, then divide by cos α) is correct, and the wording "rata on vaakasuora ympyrä" is clear. v₀ 48,2, v_max 97,29 and flat 81,3 km/h are unchanged.
- I ran answers.py: every value matches exercises.json (L1-08 9.0, L3-04 257.4).
- The 1280 px capture of the L3-05 solution with display math renders cleanly; the 360 px layout check is OK.
- Unchanged tasks and the round-1 findings (MC options, L2-06, L2-07, scope, 8/7/5) still hold.
