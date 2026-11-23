VERDICT: PASS
CONTENT-HASH: 9aede579190b60ce

## Blocking
None.

## Polish
- fy7-k4 b: the derivative row is gone, as asked. That leaves Periaate's sentence "jännitteen huippuarvo on vuon muutosnopeuden huippu" without the factor $N$: the peak voltage is $N$ times the peak rate of change of the flux. Suggested wording: "huippuarvo on $N$ kertaa vuon muutosnopeuden huippu". The Kaava line $e_0 = NBA \cdot 2\pi f$ itself is right (C/B borderline, not blocking).
- k3 c, k4 c, k6 a, k6 c: every Kaava now ends in a fully simplified form ($P = elBv/R$, $I_1 = P/U_1$, $P_\text{h} = RP^2/U^2$, $t_\text{takaisin} = K/((P_\text{h,A}-P_\text{h,B})tp)$). Sijoitus still substitutes step by step through the earlier forms ($I$, then $F$, then $P$, and so on). The numbers are the same either way. Whether to substitute into the last form is a pedagogy call.
- k6 c: $t$ is the yearly operating time (4000 h) inside the formula for $t_\text{takaisin}$. That is correct, but two quantities share the letter. $t_\text{v}$ or $t_\text{käyttö}$ would be clearer.
- fy7-k3 d (carried over): the counterfactual's "vastus [saisi] lämpöä" could follow P1 ("vastuksen sisäenergia kasvaisi").

## Checked
- Full review of tasks.json, solutions.md and answers.py. Focus: the five changed Kaava steps.
  - Each new symbolic form is algebraically correct and follows from the rows above it: $F = IlB = elB/R$; $P = Fv = elBv/R$; $I_1 = I_2U_2/U_1 = P/U_1$ (ideal transformer: power is conserved); $P_\text{h} = R(P/U)^2$; and $S = (P_\text{h,A}-P_\text{h,B})tp$, from which the payback time follows.
  - k4 b without the derivative still matches the course sheet's form $e_0 = NBA\cdot 2\pi f$.
- I recomputed everything in my own script from the task data, using the new symbolic forms. All values agree with answers.py, tasks.json and solutions.md:
  - k3: 0,30 V, 0,50 A, 0,060 N, 0,15 W; $I^2R$ = 0,15 W.
  - k4: 40 Hz, 12,37 V; $B$ = 0,0516 T (denominator 339,3 m²/s); $N_2$ = 2788 (2789 with 12,37 V); $I_1 = P/U_1$ = 3,72 A, the same as $I_2U_2/U_1$.
  - k6: 600 A and 1,728 MW (14,4 %); 109,1 A and 57,1 kW (0,476 %); $N_1$ = 500; savings 334 175 €/a; payback 8,98 a.
  - Unchanged parts recomputed as spot checks: k1 i 73,7°; k2 read slope 1,72·10¹¹ C/kg; k5 3,327/3,347/3,321 µm and $k_\text{max}$ = 6 (6,26); k7 $b$ = 2,758·10⁻³ m·K, 4,8 %, 9,47 µm, 5269 K, all $\lambda T$ below the literature value.
- Ids, answers and tolerances are unchanged. practice.py check: OK.
- Osa 1 is unchanged: exactly one correct option per item. Scope stays within FY7.
- Hash 9aede579190b60ce at start and end.
