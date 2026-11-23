VERDICT: PASS
CONTENT-HASH: 9aede579190b60ce

## Blocking
None.

## Polish
- k4-b Kaava: with the derivative row removed the chain jumps from $\Phi = BA\cos(2\pi f t)$ to $e_0 = NBA \cdot 2\pi f$. Periaate names the law and the teacher's sheet gives $e_0$, so a student can follow, but house rule "start from the basic principle" is not shown in the chain. Open it with $|e| = N\Delta\Phi/\Delta t$ and add one sentence in Periaate ("vuon muutosnopeuden huippu on $BA \cdot 2\pi f$"), or accept $e_0$ as the sheet's given formula.
- "Substitute into the last symbolic form" is not followed in four Sijoitus steps, although the Kaava steps themselves now simplify to the end:
  - k3-c: $F = IlB$ and $P = Fv$ are computed stepwise from the numbers, not from $F = e\,lB/R$ and $P = e\,lBv/R$ (the Järkevyys check $I^2R$ is good).
  - k4-c: $I_1$ is substituted from $I_2 U_2/U_1$, not from the final $P/U_1$.
  - k6-a: $P_\text{h} = RI^2$ is used, not $RP^2/U^2$ (the intermediate $I$ is still a worthwhile printed step).
  - k6-c: the substitution uses $(E_\text{A}-E_\text{B})p$ from Muunnokset, not the final $(P_\text{h,A}-P_\text{h,B})\,t\,p$.
  The numbers and answers are right, so this is only consistency; either substitute into the last form or keep the stepwise lines and label the intermediate result.
- k6-c: $t$ is both the 4000 h of operation and the base of $t_\text{takaisin}$; rename the payback time $T_\text{takaisin}$ or $n$ to avoid reading the same letter two ways.
- k6-c: $P_\text{h,B}$ is given as $57{,}1\,\text{kW}$ in Annettu and $0{,}0571\,\text{MW}$ in Muunnokset; consistent, but the rounding is visible in the answer ($334\,200$ vs $334\,175$). Harmless.

## Checked
- Read the Kaava, Sijoitus and Vastaus of the five changed steps (k3-c, k4-b, k4-c, k6-a, k6-c) and their neighbours in the packet.
- Symbolic chains end in one closed form for the asked quantity: k3-c $F$, $P$; k4-c $N_2$, $I_1 = P/U_1$; k6-a $P_\text{h} = RP^2/U^2$; k6-c $S$ and $t_\text{takaisin}$. Each starts from a basic law or the stated principle (except k4-b above).
- Rubric points and answers unchanged: all numbers match the answers.py output (0,30 V; 0,06 N; 0,15 W; 12,37 V; 2788; 3,72 A; 600 A; 1,728 MW; 334 175 €; 8,98 a).
- Finnish, notation (overline, units in LaTeX, decimal comma) and the Muunnokset/Järkevyys steps in these parts are intact. The change causes no new misconception and no jump a student cannot follow beyond the k4-b note.
