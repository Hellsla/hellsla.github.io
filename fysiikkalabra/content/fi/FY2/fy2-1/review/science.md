VERDICT: FAIL
CONTENT-HASH: 777e6ca1f82f84e5

## Blocking
- inquiry.json:253 (data, hint 2): the hint says $E_\text{lämpö} = E_\text{alussa} - E_\text{lopussa}$, with $E_\text{lopussa}$ used for the mechanical energy at the end. The lesson defines $E_\text{lopussa}$ as the *total* energy at the end, and $E_\text{alussa} = E_\text{lopussa}$ is the law itself, so a student who applies the lesson's formula gets $0\,\text{J}$. Fix: write it as the solution does: $E_\text{lämpö} = E_\text{alussa} - E_\text{mek}$ (with $E_\text{mek}$ the mechanical energy after three bounces).
- inquiry.json:244 (data table): the header unit "(J)" and the bounce counts 0–3 are still plain text. That breaks the teacher's everything-in-LaTeX rule, which last round's fix only half met. Fix: `Mekaaninen energia $E\ (\text{J})$` (the sim axes use this form) and `$0$` … `$3$`.

## Polish
- inquiry.json:342 (virhe, the "chemical energy" option): "Jarrutuksessa ei tapahdu kemiallisia reaktioita" is false for an electric or hybrid car, whose regenerative braking charges the battery. FY2 students may know this. Fix: "Tavallisissa kitkajarruissa ei …".
- inquiry.json:436 (check-2 solution): everything except visible light is called *lämpöenergia*, and much of it leaves as infrared radiation. Fix: one clause such as "(osa siitä lähtee lämpösäteilynä)", so the radiant-energy form from Ydinajatus stays consistent.
- lesson.md:21 (aria-label of figure *energialajit*): it says "kallion reunalla oleva pallo", but the text (lesson.md:11) says "Hyllyn reunalla". Fix: use one word in both places.
- lesson-answers.py:865: the comment calls the bounce data an "invented example", while inquiry.json says "simuloitu esimerkkiaineisto". Fix: harmonise the two (both are fine as the data is marked as non-measured).

## Checked
- I wrote my own script that integrates the tangential equation $m\dot v = -mg\sin\theta - \mu m g\,\mathrm{sgn}\,v$ with RK4 at a 0,5 ms step (not the sim's 2 ms step, on $x$). After largest-remainder rounding it reproduces every model value: exp-1 63/918, 862/119, 424/557 J; exp-2 mechanical 981 → 469 → 143 J, thermal 0 → 512 → 838 J, total 981 J. lesson-answers.py agrees.
- I re-derived sim.js `accel` from that equation, and it is correct. The friction heat is $\int \mu m g v\,dt$. The stick condition $|\sin\theta| \le \mu$ is right, and the constant-per-metre friction is stated under *Mallin oletukset*.
- Example: 120 J, which is 14 % of 840 J. The rounding and the energy back-check are right. Data: 0,29 J. The step losses 0,12 + 0,10 + 0,07 J (each about one fifth) are correct.
- Transfer: 335 kJ, about 4 times the useful 85 kJ, which is realistic for muscle. Check-2: 2380 J → $2{,}4\cdot10^3$ J, inside the tolerance, with 4,8 % visible light. Exit ticket: 3,8 kJ.
- Figure 2 (round-2 blocker) is fixed: the narrow arrow is *valo* and the wide one *lämpöenergia*.
- Figure 3 is to scale: 0,16 px/J for every bar, and the middle skater sits at 0,375 of the depth, where $E_\text{p}$ is 300 J of 800 J.
- The experiment status line and the table are now typeset (template `typeset`, shot exp-2-390-2).
- Each experiment varies only $t$, with friction and $h_0$ locked. simState holds Ep, Ek, Eth and Ekok.
- Every correct option and every feedback in pred-1/2, exp-1/2, virhe, check-1 and check-3 is physically right.
- Scope holds: no $E_\text{k}$/$E_\text{p}$ expressions, work, $Q = cm\Delta T$ or chains. I found no ×, the division is written with a colon, and the kJ conversions are done by substitution.
