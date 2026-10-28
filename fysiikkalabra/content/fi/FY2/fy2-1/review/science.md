VERDICT: PASS
CONTENT-HASH: 05722b7dff864e40

## Blocking

## Polish
- inquiry.json:772 (check-2 solution, Järkevyys): "loput on lämpöä". Much of the rest leaves the bulb as infrared radiation, which is radiant energy, not thermal energy. Fix: add one clause such as "(osa siitä lähtee lämpösäteilynä)" so that the solution matches the radiant-energy form in Ydinajatus. (This was raised in round 3 and is still open.)
- lessons/FY2/fy2-1/lesson-answers.py:865: the comment calls the bounce data an "invented example", but inquiry.json says "simuloitu esimerkkiaineisto" with `source: simulated`. No simulation of the ball exists, so "simuloitu" slightly overstates it. Fix: harmonise both, for example "keksitty esimerkkiaineisto, ei oikea koe". (This was raised in round 3 and is still open.)

## Checked
- Round-3 blockers are fixed. Data hint 2 now reads $E_\text{lämpö} = E_\text{alussa} - E_\text{mek}$ with $E_\text{mek}$ defined as the mechanical energy at the end, which is consistent with the solution. The table header $E_\text{mek}\ (\text{J})$ and the bounce counts $0$–$3$ are now LaTeX.
- Round-3 polish items that are fixed: the virhe feedback now says "Tavallisissa kitkajarruissa" (regenerative braking is no longer contradicted), and the aria-label of figure 1 says "hyllyn reunalla", the same as lesson.md:107.
- My own script integrates the tangential equation $\dot v = -g\sin\theta - \mu g\,\mathrm{sgn}\,v$ with RK4 at a 0,5 ms step and applies largest-remainder rounding. It reproduces every model value:
  - exp-1: 63/918, 862/119 and 424/557 J;
  - exp-2: mechanical energy 981 → 469 → 143 J and thermal energy 0 → 512 → 838 J;
  - the total stays 981 J throughout.
- lesson-answers.py agrees on every number.
- sim.js `accel` is the correct bead-on-$y=h(x)$ equation with friction force $\mu m g$, and the stick test $|\sin\theta|\le\mu$ is right. Thermal energy $=\int\mu m g v\,dt$. The constant friction per metre is stated under *Mallin oletukset*.
- Worked example: 840 J − 720 J = 120 J, which is 14 % of the start energy. Rounding to tens of joules is justified, and the back-check closes.
- Data task: 0,29 J. The step losses are 0,12, 0,10 and 0,07 J, each about one fifth of the energy remaining, as stated. The mistake values 0,31, 0,60 and 0,12 J are the right traps.
- Transfer task: 335 kJ. The useful 85 kJ is 20 % of 420 kJ, which is realistic for muscle. Check-2: 2380 J → $2{,}4\cdot10^3$ J, inside the tolerance, with 4,8 % visible light. Exit ticket: 3,8 kJ.
- Figure 3 is to scale: 0,16 px/J for every bar, and the middle skater sits at 0,375 of the depth (300/800 J). Figure 2: the narrow arrow is *valo* and the wide one *lämpöenergia*.
- The experiments vary only $t$, with friction and $h_0$ locked. simState gives Ep, Ek, Eth and Ekok. In exp-1, $t = 1{,}0$ s really is near the bottom ($h \approx 0{,}13$ m).
- Every correct option and feedback in pred-1/2, exp-1/2, virhe and check-1 is physically right, and so are the model answers of johtopaatos and check-3.
- Scope holds: there are no $E_\text{k}$/$E_\text{p}$ expressions, no work, no $Q=cm\Delta T$ and no efficiency chains, and the kJ conversions are done by substitution.
