VERDICT: FAIL
CONTENT-HASH: 9659167e822811b0

## Blocking
- exercises.json fy5-16-L2-07 (b), solutions.md fy5-16-L2-07 — the answer is printed in the lesson's own worked example: its Järkevyys step says "Ilman suojaimia sallittu aika olisi $8\,\text{h} : 2^5 = 15\,\text{min}$" at 100 dB. The task therefore repeats the example (n = 5, 8 h / 32 = 15 min) and a student can copy the result from the lesson. Fix: change the level to one the lesson does not use, e.g. 103 dB: student "18 dB : 3 dB = 6, 8 h : 6 = 1,3 h", correct n = 6, 8 h / 64 = 0,125 h = 7,5 min (answer 7,5, unit min, tolerance 0,02); update text, solutions (Annettu, Sijoitus, Vastaus, Järkevyys: 80 min wrong is 10-fold too long) and the step list 8 h -> ... -> 7,5 min (six halvings). Avoid 94, 97, 100, 106 dB (used in the lesson, L2-02, L3-04, L3-05, L1-04).

## Polish
- fy5-16-L2-07 as it stands, the student's wrong value 1,6 h equals the correct answer of fy5-16-L3-05 b) (1,6 h) and the level 100 dB is also L3-05 a); the fix above removes this coincidence.
- fy5-16-L3-04 b) and L3-05 b) both ask for a dose with protectors, as does the worked example; fine at level 3, but L3-05 c) (distance plus plugs) is the more distinct of the two.
- fy5-16-L2-06 Järkevyys — "Siksi tulos on positiivinen" is not a check; state that 11,8 dB is the difference of 25,2 and 13,4 dB and less than the largest attenuation.

## Checked
- Round 1 Blocking (L2-07 dB-addition duplicate of fy5-15-L1-07 / L2-02 / old L1-02) is resolved: the new task is a new error (dividing time by n instead of 2^n) and its direction is explained (1,6 h is about six times too long); its one remaining problem is the item above.
- Round 1 Polish applied: L2-06 text now gives "Este on 3,0 m korkea" and the solution compares λ = 2,7 m with it; L1-06 option 2 is now "Puhujaa pyydetään puhumaan hiljempaa" with a repairing feedback; L3-04 answer text says "noin 340 %".
- Recomputed: 60,3 % (T 1,51 s and 0,599 s); 11,8 dB; D = 3,375, 5,26 dB, 87 dB case D = 1,57; 100 dB, 92 dB, 1,59 h, 190 %, 47 %; L2-07 15 min. All match their solutions. "Graph" kind not used; stated assumptions (6 dB per doubling, constant attenuation) agree with the explanations; values come from tables, not figures.
- Levels fit the plan; inside FY5 scope; no other duplicate in fy5-1..15 (the known overlap fy5-15-L1-07 vs old L2-07 is gone); solutions step by step, aligned blocks render, Finnish correct, 360 px check ok.
