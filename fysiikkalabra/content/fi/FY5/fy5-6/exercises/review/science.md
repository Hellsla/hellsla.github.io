VERDICT: PASS
CONTENT-HASH: fcb321d5570d6cec

## Blocking

## Polish
- content/fi/FY5/fy5-6/exercises/solutions.md:285 (L2-09, Vastaus) — "saman taulukon uloimmilla planeetoilla suhde poikkeaa noin 1–3 %": from the fact-sheet values T²/a³ differs from the Earth's by −1,3 % (Saturn), −0,3 % (Uranus) and −2,5 % (Neptune), so the stated range is not right for Uranus — write "enintään noin 2,5 %".

## Checked
- The hash was the same at the start and at the end.
- I recomputed all 23 numeric answers in one script with my own formulas (v = √(γM/r), T = 2πr/v, a = γM/r², r³/T² fits). Every answer is within 0,4 % of my value, inside its tolerance.
- L2-09 against the source notes: every a and T in the solution's table (Mercury–Jupiter: 57,9/88,0 … 778,5/4331) is the value the NASA fact sheet gave. The task says "Syventävä tehtävä." as the teacher decided. The law is stated in the task and derived from the chapter's circular model.
- L2-09 numbers: the a³ and T² columns and T²/a³ = 0,0399…0,0398 (spread under 0,4 %) are right. The slope 0,040 read from (100; 4,0) and (400; 15,9) is right. k = 2,97·10⁻¹⁹ s²/m³ gives M = 1,99·10³⁰ kg. T_Mars = 365,2 d · (228,0/149,6)^1,5 = 687,12 d, and with 227,9 it would be 686,67 d (the solution says 686,7).
- L2-09 is not tied to the source's numbers: the solution says that another choice of planets or a later reading gives slightly different values. Part d) always uses Earth and Mars, and the 2 % tolerance covers 365,25 d (687,2 d).
- L2-09 physics: the origin of the line is justified (no constant term), Kepler III holds for ellipses with the semi-major axis, and the assumption that the planet's mass is negligible is stated. This is a fair simplification (C).
- L1-09 distractors: 0,0036 h (square root forgotten), 0,24 h (km under the root) and 460 h (divided by 60) are each reproduced by the stated error.
- L3-04: the ratios are 2,67/2,71/10,8/2,67·10¹⁸. Planet d's ratio is about four times the others, so its period should be T_d = 15,7 d. Leaving it out is justified and documented, as the guardrails require.
- In L1-06 the "88 %" is right ((6371/6771)² = 0,885). Weightlessness is described as free fall with no support force, and no centrifugal force is used.
- Figure fy5-6/radat gives 147,1–152,1 and 88–5250 milj. km, the values L1-10 and L2-08 read. Its alt text has the same values.
