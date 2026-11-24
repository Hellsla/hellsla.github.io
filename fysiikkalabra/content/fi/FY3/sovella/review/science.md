VERDICT: FAIL
CONTENT-HASH: 263ecc828495dd29

## Blocking
1. **fy3-s3 c, Kaava (B, models and conditions).** The new first row `Δp_s V_s = nRT` is presented as the basic equation, but it is the ideal gas law only for n = the amount of air taken from the tank (n_alku − n_loppu), at the same V_s and T. The Kaava does not say this, and n is not defined anywhere in the solution. A pressure difference, written down from gauge readings, goes straight into pV = nRT. This invites the gauge-pressure-in-the-gas-law error, and the step behind the rubric's total-pressure criterion is missing. Fix: start from the tank's two states, `p_alku V_s = n_alku RT`, `p_loppu V_s = n_loppu RT`, `n = n_alku − n_loppu`, so `(p_alku − p_loppu) V_s = nRT`, with p_alku − p_loppu = Δp_s. Then go on with `pV = nRT` at depth, as now.

## Polish
- s1 c: the change removed the definitions of P_a (antoteho = veden saama teho) and P_o (ottoteho = säteilyn teho). Now no text names them. The irradiance stays a number (800 W/m²) inside the symbolic chain; a symbol such as I would keep the chain symbolic. The substitution computes P_o first and does not use the last form η = P/(I A).
- s3 c: the substitution uses V and then t. It does not use the last symbolic form t = Δp_s V_s/(p q).

## Checked
- Each changed Kaava: s1 b, s1 c, s1 d, s2 a (linear interpolation), s2 c (E = Pt → ηE = rm), s2 d (Q_luovutettu = Q_vastaanotettu first), s3 a and s3 c. All are correct, except the condition in s3 c above. Each ends in the form that is substituted (except the two Polish items) and matches the rubric's `equation` details.
- My own script recomputed every number from the task data: P 237 W (the 5-min secant gives 229 W), η 0,594, loss 119 W, T 117,0 °C, m 0,127 kg, fraction 0,0315, steam 43 g and 73 l, p 248,15 kPa, V₂ 10,32 cm³, 14,74 l, 725 l, 36,3 min, 89 min, and the body-temperature warming 1,11 (about 10 %). All agree with answers.py, the solutions and the tolerances. Numbers and answers are unchanged, as stated.
- The scope stays in FY3, and units and significant-figure reasons are unchanged.
- The content hash is the same at the start and at the end.
