VERDICT: PASS
CONTENT-HASH: b294f169a9ddc0c5
SCOPE: delta added-exercise from 366b70447801ec08 base 8f23aa7ae3bd

## Blocking

## Polish
- solutions.md (fy6-10-L2-09, Kuvaajan lukeminen) — on a 1 mN grid a reader cannot see that the curve lies "noin 0,06 mN" above the 5 mN line; that value comes from the model, not from the graph. Write that the reading is about $5{,}0$–$5{,}1\,\text{mN}$ and show that $5{,}0\,\text{mN}$ gives $29{,}8\,\text{nC} \approx 30\,\text{nC}$. The answer and tolerance stay as they are.

## Checked
- Hash b294f169a9ddc0c5 at start and end. I judged only L1-09, L2-09 and L2-10 (delta added-exercise).
- L1-09: I recomputed with the MAFY k = 8,98755·10⁹: F = 0,2247 mN, which equals answers.py. With the lesson's k = 8,988·10⁹ the result is the same to 4 figures. The tolerance of 2 % covers any table edition. The force is repulsive because both charges are positive, as the solution says.
- L2-09: in figures.py the curve is k·(30 nC)²/r². At 4,0 cm it gives 5,056 mN, so q = r√(F/k) = 30,0 nC. A reading of 5,0 mN gives 29,8 nC, inside the 5 % tolerance. The alt text gives the point (4,0 cm; 5,06 mN) but not the charge.
- L2-10: in figures.py, A = 20·20 nC² and B = 20·80 nC². F_A(3,0 cm) = 3,995 mN and F_B(6,0 cm) = 3,995 mN, both on grid lines. q_B = 20 nC·(6/3)² = 80 nC; k and the shared 20 nC cancel correctly. The task states that all charges have the same sign.
- Both curves stay inside the axes: A at 2,9 cm is 4,27 mN, and B at 4,4 cm is 7,43 mN, below 8 mN. The alt text for B ("koko matkan yläpuolella") is true because q_B > 20 nC.
- The added tasks use only Coulomb's law as the brief teaches it, for point charges, or small spheres with r measured between centres. They are in scope.
- Each solution is complete: the symbolic form comes before the numbers (q = r√(F/k), q_B = q_A(r_B/r_A)²), the conversions are given, the rounding follows the data or the reading, and the reasonableness check works back the other way.
