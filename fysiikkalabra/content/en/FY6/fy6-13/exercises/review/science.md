VERDICT: PASS
CONTENT-HASH: e9e7e93f13bca666
SCOPE: delta md-paragraphs,numbers,typography,wording from 5c922b90294f7d20 base 5b3ca4f

## Blocking

## Polish
- solutions.md (fy6-13-L3, defibrillator) Formula: $t$ stands for both the charging time ($Q = It$) and the discharge time ($P = \tfrac{W}{t}$), and $Q = CU$ appears twice in the chain. This is not wrong, because the substitution uses $5.0\,\text{ms}$. — Write $t_\text{discharge}$ in $P = \tfrac{W}{t}$ and drop the repeated row.
- solutions.md (fy6-13-L2-09 d): "no chemical reaction takes place" holds for the chapter's plate capacitor (carried over from the earlier report; C).

## Checked
- Every new Formula step starts from a basic relation: the definition $C = \tfrac{Q}{U}$, $W = \tfrac{1}{2}QU$ with $Q = CU$ leading to $W = \tfrac{1}{2}CU^2$, $E = \tfrac{U}{d}$, $P = \tfrac{W}{t}$, $Q = It$. Each then solves for the asked quantity in symbols before any number is substituted. The notation matches the glossary and lesson ($W$, $C$, $Q$, $U$, $E_\text{max}$, $\varepsilon_0 \varepsilon_\text{r}$).
- Derivations: the disconnected-capacitor $\Delta W = \tfrac{1}{2}Q(U_2 - U_1)$ is valid because $Q$ is constant. The connected-source $\Delta Q = (\varepsilon_\text{r} - 1)C_1 U$ uses $C_2 = \varepsilon_\text{r} C_1$. The defibrillator chain $U = \tfrac{I}{C}t = kt$ gives $C = \tfrac{I}{k}$. The plate area combines $d = \tfrac{2U}{E_\text{max}}$ with $C = \tfrac{\varepsilon_0 \varepsilon_\text{r} A}{d}$. All are correct.
- One script recomputed every number in the diff: 4.23 mC, 320 V, ε_r 3.73, 100 µF, 72.9 s, 15.0 µJ, 1.518 µC, 0.50 mm, 217 cm², 144 mJ, 3.40 mJ, 63.4 mJ, 150 µF, 243 J, 48.6 kW, 18 s, 4.18 mJ, 0.607 mJ (ratio 6.89), 367.5 µJ, 72 mJ and 9.6·10⁵. All agree, and no number changed.
- The paragraph splits and re-breaks keep the same numbers, signs and units in the same order.
- The physics is unchanged: there is still no exponential function and no capacitor connections.
- The hash was read at the start and at the end and did not change.
