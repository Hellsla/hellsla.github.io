VERDICT: PASS
CONTENT-HASH: 330f0b13549100e6
SCOPE: delta md-paragraphs,numbers,reflow,typography,wording from 3e3a82389aa5eced base 3768fde

## Blocking

## Polish
- solutions.md:211 (defibrillator, Kaava) — one block uses $t$ both for the charging time ($Q = It$, $U = kt$) and for the discharge time ($P = W/t$, 5,0 ms), and $Q = CU$ appears twice. The numbers are right, but a student can mix up the two times. Write $t_\text{lataus}$ and $t_\text{purku}$ (or $\Delta t$) and drop the repeated row.
- solutions.md:222 (teflon/glass, Kaava) — the block opens with the derived $U = \tfrac{1}{2} E_\text{max} d$. Under queue 8g it should open from $E = \tfrac{U}{d}$ with $E = \tfrac{1}{2} E_\text{max}$, as the solution at line 117 does.
- The earlier polish items on L2-09 d) (the chapter title *Lähdejännite ja sisäinen resistanssi*, "tässä mallissa") still apply. The text is unchanged.

## Checked
- The diff (the packet's flattened version) was read against the file on disk. Every changed Kaava line is an `aligned` block with one equation per row, and each starts from the basic law ($C = Q/U$, $W = \tfrac12 QU$ with $Q = CU$, $E = U/d$, $C = \varepsilon_0\varepsilon_\text{r}A/d$, $Q = It$, $P = W/t$) before the solved form.
- Each symbolic chain is algebraically right: $C = 2W/U^2$, $t = CU^2/(2P)$, $\Delta W = \tfrac12 Q(U_2-U_1)$ for the isolated capacitor, $\Delta Q = (\varepsilon_\text{r}-1)C_1U$, $d = 2U/E_\text{max}$, $A = Cd/(\varepsilon_0\varepsilon_\text{r})$, $\Delta W = \tfrac12 C(U_2^2-U_1^2)$.
- One script recomputed every number in the diff's context: 4,23 mC; 320 V; 3,73; 100 µF; 72,9 s; 15,0 µJ; 1,518 µC; 217 cm²; 144 mJ; 3,40 mJ; 150 µF / 243 J / 48,6 kW; 6,89; 367,5 µJ; 72 mJ. All agree.
- The notation ($W$ for energy, $E$ for field, $U_\text{max} = E_\text{max} d$) matches the brief.
- The paragraph splits (L2-07 model answer, L2-09 a/d) only cut the text: the same sentences, numbers and units in the same order.
- No exponential function and no capacitor connections appear (scope notes).
- Hash read at start and end: unchanged.
