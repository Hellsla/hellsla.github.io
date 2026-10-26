VERDICT: PASS
CONTENT-HASH: 585aca35478c9485

## Blocking

## Polish
- inquiry.json:112 (`kokeile.model`) — "simulaatio antaa 330 K, koska mäntä ei liiku äärettömän hitaasti": over other seeds the slow push gives 11,2–15,2 J (324–335 K), and at a quarter of the speed it still scatters ±1 J, so the 0,3 J gap to the adiabat is mostly the fluctuation of 40 particles, not the piston speed — say "koska mäntä ei liiku äärettömän hitaasti ja hiukkasia on vain 40".
- inquiry.json:113 (`kokeile.calc`) — mixes $u$ and $w$: "nopeudella $u$ … $v_x' = 2w - v_x$" with $w$ never defined for the student — write $v_x' = -2u - v_x$ (or define $w = -u$).
- inquiry.json:112 — $T_2 = T_1(V_1/V_2)^{\gamma-1}$ is beyond FY3's central contents; acceptable inside the closed "Mallin oletukset" box as a check of the model, but keep it out of the theory and the tasks.

## Checked
- All 12 exercise answers, the transfer task (5,4 J, mistakes 6,6 and 599,4), check-2 (30 J) and exit ticket 1 (180 J) recomputed independently: all match answers.py and exercises.json; signs follow ΔU = Q + W with W done on the system throughout.
- Worked example and every solution: symbolic before substitution, signs justified, magnitudes realistic (L3-02 h = 1,699 m).
- Sim physics: 2D translational + Gamma(3/2) internal energy gives f = 5, γ = 1,4; wall re-emission uses the cosine law and a Beta(3/2, 3/2) translational fraction, which is the correct flux-weighted equilibrium split in 2D; piston reflection v' = 2w − v makes W exact work.
- Ran sim.js headless: slow insulated push W = 13,14 J, T = 329,7 K, ΔT = 36,6 K; adiabat predicts 328,9 K, W = 12,83 J (agrees within finite-N scatter). Fast: W = 19,06 J, ΔT = 53,1 K; ΔT/W = 2,786 K/J = 1/C in both. ΔU = Q + W to 1e-14.
- Conducting slow push: W = 12,37 J, Q → −12,37 J, T → 293 K, p = 1,333 p₀ (isothermal ideal 12,11 J; the gas is ~2 K warm during the push). All inquiry feedback numbers (13,1/19,1 J, 37/53 K, 2,8 K/J, 12,4 J, 1,33) match.
- Experiments isolate their variable (koe-1 locks walls, koe-2 locks speed); simState carries W, Q, dU, dT, T, p.
- Scope: first law only; work as F·s, no FY4 content.
