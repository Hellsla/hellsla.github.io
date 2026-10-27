VERDICT: FAIL
CONTENT-HASH: bf9755f9a0d272c5
## Blocking
- solutions.md:78 (L2-03) — wrong rounding claim: $-1{,}2\,\text{kJ} - (-2{,}0\,\text{kJ}) = 0{,}8\,\text{kJ}$ is known to 0,1 kJ, i.e. one significant figure, not "kaksi … kuten tiedoissa" (NOTES §2). — Fix: "$800\,\text{J} = 0{,}8\,\text{kJ}$; erotus tunnetaan sadan joulen tarkkuudella kuten tiedot, joten yksi merkitsevä numero."
- solutions.md:104 (L3-02) — principle rests on "liike-energia ei muutu" and "potentiaalienergia $mgh$"; $E_k$, $E_p$ are FY4 (scope note). — Fix: constant speed, so the rope pulls with $F = G = mg$; over height $h$ the rope/wheel does $W_1 = Fh = mgh$ on the water.
## Polish
- solutions.md:48 (L1-05) — "kuten luvussa 85 J" is the product rule; say "kokonaisina jouleina, koska molemmat siirrot tunnetaan kokonaisina jouleina" as in L1-01/03/04.
- solutions.md:68 (L2-02) — "(kolmas numero on nolla)" is unclear; say 180 kJ is known to 10 kJ, so 160 kJ has two figures.
- L2-04 Vastaus — the reason for two figures is that $W = 10\,\text{kJ}$ is known to 1 kJ; say so.
## Checked
- All 12 answers.py values, siirto 5,4 J, check-2 30 J, example 110 J, exit 180 J recomputed: all match; mistake values (6,6; 599,4; 230; 10) match their stated errors.
- Sign convention ΔU = Q + W (work on the system) consistent across lesson, figures, inquiry, exercises, solutions, sim.
- Sim run in Playwright: slow insulated W = ΔU = 13,14 J, T 329,7 K; fast 19,06 J, ΔT 53,1 K; slow conducting W 12,38 J, Q −12,38 J, T 293,15 K, p 1,333 p₀ — every number in pred-1/2, koe-2, johtopäätös holds; 1/0,359 = 2,79 K/J.
- 293·(4/3)^0,4 = 328,9 K, C·ΔT = 12,8 J: model text right.
- Sim physics: v' = 2w − v; cosine-law re-emission, Beta(3/2,3/2) split and Gamma(3/2) internal energy correct for 2+3 dof; conducting wall T₀/T scaling sound; speed ratios 1/53, 1/3,5 as stated.
- Experiments isolate the varied parameter; simState gives measured keys.
- Example and every solution: principle and reason, symbolic first, conversions right, real reasonableness checks.
- L3-01/L3-03 ideal-gas U(T, n) reasoning right and in scope.
- Figures qualitative, marked "ei mittakaavassa", signs right.
