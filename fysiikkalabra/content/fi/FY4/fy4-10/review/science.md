VERDICT: FAIL
CONTENT-HASH: 0c23e9f95fa7ef1f

## Blocking
- inquiry.json:415 (*Etsi virhe*, feedback on the correct option): A. The feedback says "Opiskelijan tulos on suurempi kuin kummankaan vaunun alkunopeus". That is false: the wrong result 0,475 ≈ 0,48 m/s is larger than 0,40 m/s but smaller than 0,60 m/s. The argument it gives for the error therefore fails. Fix: write "Opiskelijan tulos on suurempi kuin oikealle liikkuvan vaunun alkunopeus $0{,}40\,\text{m/s}$, mikä on mahdotonta, kun vasemmalle liikkuva vaunu jarruttaa sitä."

## Polish
- lesson.md:69: "muuttuu impulssin $\overline{F}\,\Delta t$ verran" applies the constant-force expression to a bumper force that varies. The paragraph's last sentence rescues it. Fix: write "Jos voima on vakio, …".
- Notation versus *Liikemäärä ja impulssi*: that chapter uses an unprimed $v$ for the velocity after; this one uses it for the velocity before. Fix: add one bridging line.
- lang/fi.json sims.fy4-10 "lukemat": "Nyt: $v_1$, $v_2$" reuses the symbols of the initial-velocity sliders. Fix: rename them.
- inquiry.json:455 siirto Järkevyys: "Kokemus vahvistaa tuloksen" is not a check. Fix: drop it.

## Checked
- The hash was 0c23e9f95fa7ef1f at the start and at the end. Since round 3 (commit 1d224137), only inquiry.json:10 changed in the lesson files. The sim and lesson-answers.py are unchanged since round 2.
- inquiry.json:10 now reads "vakiosuuruisen kokonaisvoiman impulssi … $\Delta\overline{p} = \Sigma\overline{F}\,\Delta t$". It is correct and agrees with lesson.md:64, the kertaus prompt and the previous chapter. The round 3 Blocking item is resolved.
- I recomputed every number in one script with my own closed-form formulas. All of them agree with lesson-answers.py, the sim values and the feedback: exp-1 (0,40/0,30/0,24 m/s; E_k' 0,048–0,029 J), exp-2 (0,20/0,80, 0/0,60, −0,12/0,48), pred-3 (0,63/1,26 m/s), virhe 0,025/0,475, check-2 0,15, siirto 1,0 (and every listed mistake value) and the worked example 1,14 m/s with 38,3 → 32,5 kJ (15 %).
- sim.js uses the constants of lesson-answers.py (k = 300 N/m, c = 0 / 3,0 / critical, 4,0 cm spring, 0,2 ms steps). Momentum conservation emerges from equal and opposite forces. simState gives u1, u2, pJ and EkJ.
- The experiments vary only m₂. Each choice item has exactly one correct option, and the other feedbacks are correct.
- The conservation condition (negligible external impulse) is stated in the lesson, the summary, the example, siirto, check-2, check-3 and the exit ticket.
- The third-law derivation, billiards, clay ball and Earth, and the explosion energy are correct. The figures match their scale claims.
- Scope stays within FY4: one-dimensional collisions only.
