VERDICT: PASS
CONTENT-HASH: e15d7cb149da0d0d
none

## Blocking
None.

## Polish
- fy5-s3 d, Kaava: the chain goes from $E_\text{k,max} = E_\text{p,max}$ and $m_\text{eff}$ straight to $v_\text{max} = A\sqrt{k/m_\text{eff}}$. One row $\tfrac12 m_\text{eff}v_\text{max}^2 = \tfrac12 kA^2$ before the solved form would show the simplification the way the rubric's equation criterion states it. Not an error.
- fy5-s3 d: the task says to use the added mass read from the c graph (14 g). The solution's main model uses $m_\text{j}/3 = 15\,\text{g}$, and Hyväksytään myös accepts 14 g (same 0,43 m/s). This is consistent and not changed in this round. It would read more cleanly if the Kaava/Annettu named both values once.

## Checked
I recomputed every number with my own formulas in one script (scratchpad fy5s.py). All agree with answers.py and with the solutions:
- s1: r = 21,0 m; m_tip = 2579 kg; M0 = 412 kNm, 608 kNm with +2 t; Δm_v,max = 1,92 t; tip load then 3,06 t; v = 1,466 m/s; tanθ = 0,01043, θ = 0,598°; shift 0,157 m.
- s2: v_Io = 17,34 km/s; γM from each moon is 1,27·10¹⁷ m³/s²; M = 1,90·10²⁷ kg; synchronous r = 1,60·10⁸ m, height 88,7·10³ km.
- s3: LSQ slope 1,982 s²/kg, intercept 0,0278 s²; residuals ≤ 0,0047 s²; k = 19,9 N/m (read) and 20,0 N/m (static); origin-forced fit 18,9 N/m; added mass 13,9 g; v_max = 0,433 m/s (massless 0,446); T ≈ 0,73 s.
- s4: f = 250 Hz; L = 0,686 m; v' = 335,8 m/s, f' = 244,75 Hz, Δf = 5,25 Hz; L₂ = 94,0 dB; t_v = 1,0 h; P = 0,127 W.

The rewritten Kaava steps (s1 a, b, e; s2 b, c; s3 b, d; s4 b, c, d) each start from the basic laws: M = Fr with F = mg, ΣM = 0, ΣF_x = ma_n, ΣF_y = 0, gravity as the central force, T = 2π√(m/k), the energy balance, v = fλ with L = λ/2, I = P/(4πr²) and the dB definition. Each simplifies symbolically to the form the Sijoitus uses, and every algebraic step is correct. The signs and moment directions agree with the Periaate. Each Kaava agrees with its rubric's equation criterion (s1 a, b; s1 e fbd_equations; s2 c r³; s3 b; s4 b, c). The scope is FY5 (no ω or rotational dynamics) and γ is used. The Sijoitus steps, answers, rubrics and point sums are unchanged. Hash identical at start and end.
