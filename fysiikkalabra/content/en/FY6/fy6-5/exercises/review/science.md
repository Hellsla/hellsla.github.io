VERDICT: PASS
CONTENT-HASH: 424e9d97bbd2962e
SCOPE: delta md-paragraphs,numbers,reflow,teacher-figure,typography,wording from 17c2425172d0b70e base b5600a6

## Blocking
- none

## Polish
- exercises/solutions.md:200 — a full stop is missing after "$630\,\text{V}\,\Omega$" before "The denominator". The old sentence "units left out" went with the rewrite, so units are now carried, which is fine.

## Checked
- The hash moved during the review, from c213d2c7a9fbfcfb (the packet) to 424e9d97bbd2962e: an uncommitted edit to the fy6-5-L3-04 Formula chain. That hunk was reviewed too. Multiplying $I_2 = I_1 + I_3$ by $R_1R_3$ gives $R_1R_3I_2 = R_3(U_1 - R_2I_2) + R_1(U_2 - R_2I_2)$, so $I_2D = U_1R_3 + U_2R_1$ with $D = R_1R_3 + R_2R_3 + R_1R_2$. This is correct.
- The new chains start from the right basic laws: $\Sigma I_\text{in} = \Sigma I_\text{out}$, $\Sigma U = 0$ around a loop, and $U_{AB} = V_A - V_B = RI$. The divider has unloaded, loaded and solving parts, ending in $R_\text{L} = R_\text{p}R_2/(R_2 - R_\text{p})$.
- The new symbolic-first substitutions were recomputed: $V = R_2U/(R_1 + R_2) = 8.0\,\text{V}$, $V_- = -(R_2 + R_3)U/\Sigma R = -9.0\,\text{V}$, $V = -R_1U/(R_1 + R_2) = -3.0\,\text{V}$, $V_C = 3.0\,\text{V}$, $R_2 = 40\,\Omega$, branch sum $0.59\,\text{A}$, $I_2 = 630 : 2100 = 0.30\,\text{A}$, and $V_P = 4.0\,\text{V}$ (100 Ω load) and $5.0\,\text{V}$ (250 Ω load). All agree with answers.py.
- The reasonableness sentences only moved into their own paragraphs (for example "R3 twice the current of R2", line 114). Nothing was lost.
- Signs and zero points of potential are unchanged from the version I passed.
- Content hash checked at the start and at the end (see the first item).
