VERDICT: PASS
CONTENT-HASH: c367bdde3ea32b84
SCOPE: delta md-paragraphs,numbers,typography from 48f32a459da5ae07 base 5b3ca4f

## Blocking

## Polish
- solutions.md:207 (defibrillator task, Kaava) — one block uses $t$ for two different times: the charging time in $Q = It$ and $U = kt$, and the 5,0 ms discharge time in $P = \tfrac{W}{t}$. Here $Q = CU$ also appears twice. Fix: write $P = \tfrac{W}{\Delta t}$ or $t_\text{purk}$, and drop the second $Q = CU$ (C: the physics and numbers are right).
- solutions.md (fy6-13-L2-09 d) — the earlier note still applies: "ei tapahdu kemiallista reaktiota" holds for the chapter's plate capacitor. Adding "tässä mallissa" would keep it exact (C).

## Checked
- Every new Kaava block starts from a law the lesson teaches ($C = \tfrac{Q}{U}$, $E = \tfrac{U}{d}$, $C = \tfrac{\varepsilon_0\varepsilon_\text{r}A}{d}$, $W = \tfrac12 QU$ with $Q = CU$, $P = \tfrac{W}{t}$). Each one is solved in symbols down to the form that is substituted into, and it uses the lesson's symbols ($W$ for energy, $E$ for field strength).
- Each derivation is correct: $C = \tfrac{2W}{U^2}$, $t = \tfrac{CU^2}{2P}$, $\Delta W = \tfrac12 Q(U_2-U_1)$ at constant $Q$, $\Delta Q = (\varepsilon_\text{r}-1)C_1U$ with $C_2 = \varepsilon_\text{r}C_1$, $d = \tfrac{2U}{E_\text{max}}$, $A = \tfrac{Cd}{\varepsilon_0\varepsilon_\text{r}}$, and $U = \tfrac{I}{C}t$ from $Q = It$ and $Q = CU$.
- I recomputed every substitution near the diff in one script: 4,23 mC, 320 V, 3,73, 100 µF, 72,9 s, 15,0 µJ, 1,518 µC, 217 cm², 144 mJ, 3,40 mJ, 150 µF, 243 J, 4,86·10⁴ W, ratio 6,89, 367,5 µJ and 72 mJ. All agree.
- The split paragraphs (L2 graph task, L3 c, L2-09 a and d) keep the same sentences, numbers and order. No reasoning step was lost.
- Scope still holds: no exponential function and no capacitor connections.
- The hash was the same at the start and at the end.
