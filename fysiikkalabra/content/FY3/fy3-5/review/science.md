VERDICT: PASS
CONTENT-HASH: de5a8ebe1ca2e4cf

## Blocking

## Polish
- inquiry.json:113 (`kokeile.calc`) — "$v_x' = 2u - v_x$" is right only with the x axis along the piston's motion; the sim's piston is on the right and moves in −x (sim.js:3–4, `bounce = 2w − vx`, w = −u), where the same reflection reads $v_x' = -2u - v_x$. The axis is never stated, so a student who reads x from the picture gets a speed that shrinks by 2u — add "kun x-akseli osoittaa männän liikkeen suuntaan" (or write $|v_x'| = |v_x| + 2u$).
- inquiry.json:112 — $T_2 = T_1(V_1/V_2)^{\gamma-1}$ is beyond FY3's central contents; acceptable inside the closed model box as a check of the model, keep it out of the theory and tasks.

## Checked
- Diff since cb4b8f4: only `kokeile.model` and `kokeile.calc` changed; answers.py, exercises.json, lesson.md and sim.js unchanged, so the round-1 recomputation (12 exercises, transfer 5,4 J, check-2 30 J, exit ticket 180 J) still holds.
- New model sentence: "työ vaihtelisi noin 11–15 J" with other random initial states matches the round-1 seed sweep (11,2–15,2 J); attributing the 330 K vs 329 K gap mainly to N = 40 is now correct.
- Adiabat check 293 K · (4/3)^0,4 = 328,9 K; sim 329,7 K within that scatter.
- `calc`: u/w mix-up of round 1 removed; remaining statements (W = force × distance, ΔU = Q + W, ΔT = W/C, piston 50× and 3,5× slower than particles) unchanged and correct.
- Hash identical at start and end.
