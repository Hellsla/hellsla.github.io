VERDICT: FAIL
CONTENT-HASH: 86c8c78f68c7e9d1
SCOPE: delta caption-label,md-paragraphs,numbers,reflow,teacher-figure,typography,wording from 22633f9efb51607f base a5182aa

## Blocking
- content/fi/FY6/fy6-5/exercises/solutions.md:15 — (B, consistency with the lesson) L1-02 now opens with $\Sigma U = 0$. The lesson states the voltage law as $\sum \Delta V = 0$, where the potential changes are signed ($+U$ in the source, $-RI$ in a resistor). Its summary says the same. A sum of voltages $U$ written as zero, with no signs, is false. It also differs from the law named in the task's own Periaate. Fix: write $\sum \Delta V = 0$ on the first row. The next row, $U - U_1 - U_2 = 0$, is right.

## Polish
- content/fi/FY6/fy6-5/exercises/solutions.md:5 — L1-01 writes $\Sigma I_\text{tulo} = \Sigma I_\text{lähtö}$, but the lesson writes $\sum I_\text{tulevat} = \sum I_\text{lähtevät}$. Use the lesson's subscripts.
- content/fi/FY6/fy6-5/exercises/solutions.md:182 — L3-04 jumps from the loop equations to $I_2 = (U_1R_3 + U_2R_1)/D$. The step that puts $I_1$ and $I_3$ into $I_1 + I_3 = I_2$ is missing. One row ($\tfrac{U_1 - R_2I_2}{R_1} + \tfrac{U_2 - R_2I_2}{R_3} = I_2$) would show it.
- content/fi/FY6/fy6-5/exercises/solutions.md:184 — no full stop after "$630\,\text{V}\,\Omega$", and a stray `\quad` sits in the D row.

## Checked
- Hash 86c8c78f68c7e9d1 at start and end. Delta: the Kaava blocks of 16 tasks, three re-cut Sijoitus rows, split paragraphs (L3-04, L3-05, L2-08) and the figure pictures the teacher approved.
- Every other new block starts from the lesson's laws in its own form: $U_{AB} = V_A - V_B$, signed loop equations, the current law. All are algebraically correct.
- Recomputed: L3-04 $D = 2100\,\Omega^2$, $I_2 = 0,30$ A, $I_1 = 0,20$ A, $I_3 = 0,10$ A. The energy balance holds: sources 3,3 W = resistors 3,3 W.
- Also recomputed: L3-05 $R_\text{k} = 250\,\Omega$ at $V_P = 5,0$ V; L3-01 −9,0 V; L2-07 −3,0 V; L2-02 8,0 V; L3-03 7,2 V → 9,0 V.
- The re-cut Sijoitus rows (L2-02, L3-01, L2-07) substitute into the last symbolic form and keep their answers.
- answers.py runs; answers unchanged.
