VERDICT: PASS
CONTENT-HASH: 371d5bb766d58f79

## Blocking

## Polish
- exercises/solutions.md:109 (L3-02) — The stated assumption "pyörrevirran oma kenttä jätetään huomiotta" is far from true at these numbers. An 8 cm loop has $L \approx 0{,}3\,\mu\text{H}$, so $\omega L \approx 0{,}045\,\Omega$, about the same as $R = 0{,}050\,\Omega$; the real power would be roughly half. The assumption also makes $P \propto 1 : R$, while the lesson says a high-resistance steel bottom heats better. The assumption is stated in the task, so this is not an error. One clause in Järkevyys ("todellisuudessa pyörrevirran oma kenttä pienentää virtaa, joten tulos on yläraja") would avoid a wrong picture.
- exercises/solutions.md:99 (L3-01) — "107 km sopii vahvistinväliin 50–100 km:n luokkaa": 107 km is just outside the quoted range. Write "on hieman yli tyypillisen 50–100 km:n".

## Checked
- All twelve answers recomputed independently in one script, and all agree: 9,0 dB; 6,02 dB; 1,6 kW; 0,60 µWb; 72 %; 3,519 V; 150 km; 5,24 min; 2,464 kWh; 10 amplifiers; 1,596 kW; 0,441 ms.
- answers.py computes the same physics as the task texts.
- L3-01: the spans are rounded up (10,55 → 11) and there are spans − 1 amplifiers. The task names both ends, so this is unambiguous.
- L3-02: $e_0 = 2\pi f B_0 \pi r^2$, the effective value $e_0 : \sqrt 2$, and $P = U^2 : R$ as the mean power. Effective values are in scope (teacher's FY07 sheet).
- L2-03: $Q = cm\Delta T$ is valid because the water stays liquid up to 100 °C (the solution says so). 85 % is stated as an assumption.
- L1-03 and L1-05 state their modelling assumptions in the task. The guardrail efficiency wording holds (below 100 %, the losses named).
- L2-04 and L3-01 use real data with named sources (Ravenscraft/OneZero 2020; Cinia 2016, C-Lion1 1172 km).
- Every solution has all seven steps, solves for the unknown symbolically before substituting, and converts units correctly. Each rounding is justified by the limiting datum.
- The Järkevyys checks are real checks (halvings per 3 dB, unit analysis, estimates with round numbers).
- The notation matches the lesson brief: $A = aL$, $A = 10\,\text{dB}\cdot\lg(P_0 : P)$, $e_0 = N\cdot 2\pi f\cdot\Phi_0$.
