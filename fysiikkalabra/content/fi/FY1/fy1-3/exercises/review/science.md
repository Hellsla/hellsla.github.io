VERDICT: PASS
CONTENT-HASH: f08e184ae3cb1022
SCOPE: delta added-exercise fy1-3-L2-09 (work queue 19), round 1

## Blocking
- none

## Polish
- none

## Checked
- This review covers fy1-3-L2-09 only (a new exercise, judged in full). The other diff line in L1-09 is a spacing change only, with the same numbers. The hash was f08e184ae3cb1022 at the start and at the end.
- I recomputed it myself:
  - t = s/c = 7,30·10⁵ m / 2,998·10⁸ m/s = 2,4350·10⁻³ s.
  - Δt/t = 6,0·10⁻⁸ s / 2,435·10⁻³ s = 2,464·10⁻⁵ = 0,002464 %.
  - cΔt = 17,99 m ≈ 18 m.
  - 18 m / 0,20 m ≈ 90, which the text calls "lähes sata".
  - t/Δt ≈ 40 600.
- answers.py gives 0.0024641, which matches the key 0.002464. The tolerance of 0,03 accepts the two-figure answer 0,0025 % (1,5 % off). Two significant figures, from 60 ns, is the right count.
- I checked the CERN page (fetched 2026-11-16). It has the 730 km distance with a 20 cm uncertainty, a time of flight better than 10 ns using GPS and atomic clocks, and over 15 000 events. It gives "20 parts per million" (the solution's 25 ppm is computed from 60 ns, and it says how the two relate). It also has:
  - the two possible effects found later: the GPS synchronisation oscillator and the optical fibre connector to the master clock;
  - ICARUS's result consistent with c (16 March 2012);
  - Borexino, ICARUS, LVD and OPERA all consistent with c, and the "faulty element of the experiment's fibre optic timing system".
  The model answers a) and c) match the page.
- The systematic vs random reasoning follows the guardrails. Repeating reduces random error, not systematic error, and independent apparatus is needed.
- d): the anomalous result is checked and not discarded, and the theory would change only after independent replication. The thermometer example (80 °C at normal pressure) is sound.
- The light time is computed "tyhjiössä", as the task states. The neutrino's path through rock does not affect the comparison (C).
- The scope (measurement, error types, s = ct) is FY1.
