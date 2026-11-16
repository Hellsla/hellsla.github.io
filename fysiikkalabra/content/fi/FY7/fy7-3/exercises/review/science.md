VERDICT: PASS
CONTENT-HASH: 74e9158eec247049

## Blocking

## Polish
- content/fi/FY7/fy7-3/exercises/solutions.md:39 — (B, minor) L1-04 Järkevyys: "toisen johtimen vastakkaissuuntainen virta heikentää kenttää ... joten johdon kenttä on silloin vielä pienempi" does not hold at every point $5\,\text{mm}$ from one conductor: between the conductors, or close beyond the other one, the fields add. — say "kauempana johdosta" only, or "useimmissa kohdissa johdon ulkopuolella".
- content/fi/FY7/fy7-3/exercises/exercises.json:285 — L2-09 `answer` 497.36 has five figures, but the solution answers $5{,}0 \cdot 10^2$. The tolerance 4 % covers both 490 (exact fit slope 2,465 mT/A) and 500. — think about `"answer": 500` (or 497), to match the solution's rounding.

## Checked
- Recomputed all 17 numeric answers in one script with my own formulas (B = μ0I/(2πr), B = μ0NI/l, tan α = B_j/B_h, R = ρL/A). Each agrees with answers.py and exercises.json within its tolerance; the largest gap is L2-09, 490 vs 497 (1,4 %).
- L2-05: the least-squares slope is 2,512 mT/A with intercept 0,059 mT, so μ0 = 1,256 µVs/(Am). The solution's eye fit agrees. The 4 % tolerance suits a hand fit.
- L2-06: B·r = 161/158/164 µT·cm. c) is 53,7 → 54 µT; d) is 322 µT. The shortcut 79·2/3 = 52,7 is still inside the 3 % tolerance.
- L2-09/L2-10 figures: the fit line at 2,0 A reads 4,97 ≈ 5,0 mT. The curve 120/r gives 60 µT at 2,0 cm. The figures and their descriptions do not give the answers away.
- L3-02: N = 4775 and L = 15,0 km. The finite-coil factor 0,8/√(0,8²+0,5²) = 0,848 matches the "noin 85 %" remark, and the task states the long-coil assumption.
- L3-04: the tangents 0,315–1,570 and the fit through the origin give k = 0,3127 1/A, so B_h = 16,0 µT. The c) reasoning (arctan saturates, approaches 90°) is right.
- L3-05: N = 318, l = 0,175 m, R = 2,60 Ω, I = 2,31 A, B = 5,28 mT. d) is right: N:l stays the same and I halves, giving 2,6 mT.
- L3-01 geometry: a N–S wire above the compass gives a horizontal E–W field, so tan 30° = B_j/B_h and I = 2,02 A.
- Choices: L1-06 (counterclockwise seen from above, reverses with the current), L2-07 (cos 60° = 0,50) and L2-08 (3/2 = 1,5; 1,51 → 2,26 mT) each have exactly one correct option, and every distractor's feedback names the actual error.
- All tasks stay in the FY7 scope: no self-induction, no para- or diamagnetism. The symbols and the μ0 notation are those of the brief, degrees are written without a space, and every task with data is marked as example data.
