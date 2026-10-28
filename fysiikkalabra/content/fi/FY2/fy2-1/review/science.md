VERDICT: PASS
CONTENT-HASH: b89b569c29fa26de

## Blocking

## Polish
- inquiry.json (data, text) and lessons/FY2/fy2-1/lesson-answers.py:66 — both now say "simuloitu/simulated example data", which is consistent, but no simulation of the ball exists — optional: "keksitty esimerkkiaineisto, ei oikea koe" in both places.

## Checked
- Round-5 polish applied: the check-2 Periaate now says the thermal energy warms the bulb and its surroundings and that part of it leaves as thermal radiation. This is physically right at FY2 level and consistent with the Järkevyys "loput on lämpöä". The lesson-answers.py comment matches the inquiry's label.
- My own RK4 integration of the tangential equation $\dot v = -g\sin\theta - \mu g\,\mathrm{sgn}\,v$ (0,5 ms step, a different formulation from sim.js) reproduces every model value:
  - exp-1: 63/918, 862/119 and 424/557 J, with the total 981 J;
  - exp-2: mechanical energy 981 → 469 → 143 J and thermal energy 0 → 512 → 838 J, with the total 981 J.
- lesson-answers.py agrees on every number.
- sim.js is unchanged in substance. The bead-on-curve equation with friction force $\mu m g$, the stick test $|\sin\theta|\le\mu$ and thermal energy $=\int \mu m g v\,dt$ are all right. The limits (no air resistance, constant friction per metre) are stated under *Mallin oletukset*.
- Worked example: 840 J − 720 J = 120 J (14 %). The rounding to tens is justified, the solution is symbolic first and the back-check closes.
- Data task: 0,29 J. The step losses are 0,12, 0,10 and 0,07 J, each about one fifth of the energy remaining, as stated. The mistake values are the right traps.
- Transfer task: 335 kJ, so 20 % is useful, which is realistic. Check-2: 2380 J → $2{,}4\cdot10^3$ J, inside the 2 % tolerance, with 4,8 % visible light. Exit ticket: 3,8 kJ.
- Figure 3 is to scale at 0,16 px/J for every segment, and each bar totals 800 J.
- The experiments vary only $t$, with friction and $h_0$ locked, and simState gives Ep, Ek, Eth and Ekok.
- Every correct option and feedback in pred-1/2, exp-1/2, virhe and check-1 is physically right, and so are the johtopaatos and check-3 model answers.
- Scope holds: there are no energy expressions, no work, no $Q=cm\Delta T$ and no efficiency chain.
