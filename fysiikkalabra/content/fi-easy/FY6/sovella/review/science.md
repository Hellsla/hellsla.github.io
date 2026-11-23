VERDICT: FAIL
CONTENT-HASH: 89bc5a4dee475915

## Blocking
- solutions.md fy6-s1 d, *Ryöminnän suuruus* (A, definitions and internal consistency). The task now separates *ryömiminen* (the slow voltage change) from the carriers' *ajautumisnopeus*. The solution writes "Se ei ole sama asia kuin varauksenkuljettajien **ryöminnän nopeus** johtimessa. Se on millimetrien luokkaa sekunnissa." One word stands for both ideas, the mix-up item 20 meant to remove, and it contradicts the task. "Se" can be read as the voltage creep rate, which would make that rate mm/s. Use *ajautumisnopeus* and make clear the figure is the carriers' speed. The size is also high: typical drift is about 0,01–0,1 mm/s ("alle millimetri sekunnissa"). Dropping the magnitude sentence also fixes it.

## Polish
- fy6-s4 a: the rounding reason contradicts itself ("enintään kaksi tai kolme numeroa"). Under NOTES §2, 300 V and 330 µF have three figures (14,9 J), or say why two. 15 J is inside the tolerance.
- answers.py does not compute the drift rate 0,005 V/min (shared with fi).

## Checked
- One script recomputed every number with my own formulas. All agree with tasks.json, the solutions and answers.py:
  - s1: fit −1,194 and 4,598, largest residual 0,0197 V; c: 0,50 A, 2,0 W, 13,0 %; d: ±0,08 Ω and 0,06 Ω.
  - s2: 2,5 A, 16,7 W, 30 W in total; without B: 1,76 A, 10,6 V, 18,7 W, 2,49 W; with C: 4,29 A, 8,57 V, 14,7 W.
  - s3: 1,8·10⁻⁷ N, weight 2,2 %, field 0,10 of breakdown, 13,4 m/s, kinetic energy 13,9 % of the work, 3,24·10⁻⁹ N (0,82 times the weight).
  - s4: 14,85 J, 6,86 J, 46,2 %, 26,4 A, 6,9 kW, 0,30 A.
- The Kaava steps start from basic equations and each derivation is correct: loop rule, the parallel sum from I = I_A + I_B, P = UI with U = RI, W = qU = ΔE_k, Q = CU.
- The reworded sub-parts (s2 c, d; s3 b, c; s4 b, d) are answerable with the same answers. The rubric asks only what the task gives.
- The points add up. The accepted methods are valid. Invented data is labelled.
- Scope is within FY6 and the internal-energy guardrail holds.
- The model graph is consistent: intercept 4,60 V and slope triangle 0,50 A / −0,60 V.
