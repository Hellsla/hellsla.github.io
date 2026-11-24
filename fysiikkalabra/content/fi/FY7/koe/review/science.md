VERDICT: PASS
CONTENT-HASH: addb9d598021ee63

## Blocking
None.

## Polish
- k3 c and k4 c: each Kaava now ends in its fully simplified form ($P = elBv/R$, $I_1 = P/U_1$), but Sijoitus still goes through the intermediate quantities ($I$, then $F$, then $P$; and $I_2$, then $I_1 = I_2U_2/U_1$). These parts ask for those intermediate quantities, so this is defensible. Substituting $I_1 = P/U_1$ directly would match the Kaava's last row (3,72 A either way). Whether to change it is a pedagogy call.
- k6 c: Sijoitus gives $S = 334\,200\,\text{€}$ and then divides by "$334\,200\,\text{€/a}$". Writing the yearly saving as €/a in both places would be more consistent. The Muunnokset row computes energies rather than converting units; that is harmless.
- fy7-k3 d (carried over): "vastus [saisi] lämpöä" in the counterfactual could follow P1 ("vastuksen sisäenergia kasvaisi").

## Checked
- Full review of tasks.json, solutions.md and answers.py, focused on the round-2 edits.
- k4 b:
  - Periaate now says the peak voltage is $N$ times the peak rate of change of the flux (correct).
  - Kaava runs $\Phi = BA\cos(2\pi ft)$ → $e_0 = NBA\cdot2\pi f$ → $B = e_0/(NA\cdot2\pi f)$.
  - Sijoitus is one chain: $17{,}5\,\text{V}/339{,}3\,\text{m}^2/\text{s} = 0{,}0516\,\text{T}$. The unit m²/s·T = V works out.
- k6 c:
  - Operating time is now $t_\text{käyttö}$ and is distinct from $t_\text{takaisin}$.
  - The Kaava chain $S = (P_\text{h,A}-P_\text{h,B})t_\text{käyttö}p$, $t_\text{takaisin} = K/S$ is algebraically right.
  - The Muunnokset and Sijoitus rows start with their quantity ($E_\text{A}$, $E_\text{B}$, $S$, $t_\text{takaisin}$).
- k3 c, k4 c, k6 a: the symbolic forms $F = elB/R$, $P = elBv/R$, $I_1 = P/U_1$ (ideal transformer, power conserved) and $P_\text{h} = RP^2/U^2$ are correct.
- I recomputed the numbers in my own script, using the final symbolic forms. They agree with answers.py, tasks.json and solutions.md:
  - k3: 0,30 V, 0,50 A, 0,060 N, 0,15 W; $I^2R$ = 0,15 W.
  - k4: 40 Hz, 12,37 V, 0,0516 T; $N_2$ = 2789 with 12,37 V (2788 unrounded, within tolerance); $I_1$ = 3,72 A.
  - k6: 600 A, 1,728 MW (14,4 %); 109,1 A, 57,1 kW (0,476 %); $N_1$ = 500.
  - k6 c: 6912 and 228,5 MWh; $S$ = 334 175 €/a; payback 8,98 a.
  - Spot check of k2 b: slope read from the graph 1,81·10⁻⁵ m²/V gives 1,72·10¹¹ C/kg.
- The other parts and Osa 1 are unchanged from the passed version:
  - Exactly one correct option per item.
  - Scope stays within FY7.
  - Ids, answers and tolerances are unchanged.
- practice.py check: OK. Hash addb9d598021ee63 at start and end.
