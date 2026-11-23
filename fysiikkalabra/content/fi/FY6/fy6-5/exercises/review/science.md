VERDICT: PASS
CONTENT-HASH: 33b9c3bf1b8baf23
SCOPE: delta caption-label,md-paragraphs,numbers,reflow,teacher-figure,typography,wording from 22633f9efb51607f base a5182aa

## Blocking

## Polish
- content/fi/FY6/fy6-5/exercises/solutions.md:5 — L1-01 still writes $\Sigma I_\text{tulo} = \Sigma I_\text{lähtö}$, but the lesson writes $\sum I_\text{tulevat} = \sum I_\text{lähtevät}$. Use the lesson's subscripts.
- content/fi/FY6/fy6-5/exercises/solutions.md:184 — no full stop after "$630\,\text{V}\,\Omega$" before "Nimittäjä on".
- content/fi/FY6/fy6-5/exercises/solutions.md:182 — L3-04 loop rows are the rearranged $U_1 - R_1 I_1 - R_2 I_2 = 0$. The Periaate names $\sum \Delta V = 0$, so the form is correct (C). One opening $\sum \Delta V = 0$ row would match L1-02.

## Checked
- Hash 33b9c3bf1b8baf23 at the start and at the end.
- The previous blocking item is fixed. L1-02 now opens with $\sum \Delta V = 0$, then $U - U_1 - U_2 = 0$, as the lesson writes the law.
- L3-04 Kaava: the node law, both loop equations ($R_1 I_1 + R_2 I_2 = U_1$, $R_3 I_3 + R_2 I_2 = U_2$) and the substitution $R_1R_3I_2 = R_3(U_1 - R_2I_2) + R_1(U_2 - R_2I_2)$ are correct. So are $D = R_1R_3 + R_2R_3 + R_1R_2$ and $I_2 = (U_1R_3 + U_2R_1) : D$.
- Every new Kaava block starts from a basic law ($U_{AB} = V_A - V_B$, the loop law, the node law, Ohm's law) and solves symbolically to the last form. The Sijoitus rows substitute into that form.
- Recomputed in one script with my own formulas, all matching answers.py:
  - 1,2 A; 7,5 V; 3,5 V; 8,0 V; 0,50 A; 60 Ω; −9,0 V; 30 Ω; 1,8 V; 3,0 V; 0,59 A; 40 Ω; −3,0 V
  - L3-04: $I_2 = 0{,}30$ A, $I_1 = 0{,}20$ A, $I_3 = 0{,}10$ A; energy balance 3,3 W = 3,3 W
  - L3-05: $R_\text{k} = 250\,\Omega$; with a 100 Ω load, $V_P = 4{,}0$ V
- The re-cut paragraphs (L3-04, L3-05, L2-08) change no physics. The approved figures ex-branch and ex-branch2 give the values their tasks need.
