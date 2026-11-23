VERDICT: PASS
CONTENT-HASH: 7b67e96be537b1db
none

## Blocking
None.

## Polish
- fy5-k7 c, Kaava: the step from $L_2$ to the level at the ear ($L_\text{korva} = L_2 - 12\,\text{dB}$) and the $n$ formula appear only in the Sijoitus. Adding $n = \dfrac{L_2 - 12\,\text{dB} - 85\,\text{dB}}{3\,\text{dB}}$ to the chain, as e does, would make the Kaava complete.
- fy5-k6 c, Kaava: $T$ is used for the Celsius temperature in $v_T = 331\,\tfrac{\text{m}}{\text{s}} + 0{,}6\,\tfrac{\text{m}}{\text{s}} \cdot T$. The text defines it, so this is not an error, but $T$ elsewhere in the exam is a period or an absolute temperature; $\vartheta$ or $t_\text{C}$ would avoid the clash.
- fy5-k3 a and k5 b, Kaava: these were left as a single row with "ja" joins, unlike the derived chains of k3 b and d. This is correct physics and a choice of form only.

## Checked
I recomputed every number of the solutions, the options and the figures in one script (scratchpad koe.py). All agree with answers.py and with the solutions:
- k1: M = 30/22,5/18 Nm (36 without the angle); F = 2,4·10⁻⁷ N; λ = 0,34 and 1,5 m; Δs/λ = 1,5; 93 dB.
- k2: F_A = 1635 N and N = 2616 N (also from moments about A); x = 0,533 m, so 0,667 m from A; 262 N with the diver at B; k = 6540 N/m, T = 0,602 s = 2π√(x/g).
- k3: F = 33,56 N, 85,5 %; v = 7604 m/s, T = 94,9 min, a_n = 8,39 m/s²; v(400 km) = 7671 m/s.
- k4: T² values; LSQ slope 4,016 s²/m and intercept 0,088 s²; g = 9,83 m/s² (fit and read points); r = 2,2 cm; single-point g = 9,11 m/s² (too small, as stated).
- k5: v = 215,6 m/s; 392 and 588 Hz; λ_air = 1,75 m; 43,9 dB.
- k6: 333 m/s; fit through the origin 336,2 m/s against the theory value 335,8 m/s; 2,9 % and 0,67 %; 12,7 dB; λ = 0,11–1,1 m.
- k7: I = 2,0·10⁻² W/m², ratio 63; 7,5 min; 2,0 h; 95,0 dB; 12,7 h; d 150 % (126 % + 24 %; 151 % unrounded); e 9,9 % (40,3 h).

The rewritten Kaava chains (k2 b, c, d; k3 b, d; k5 d; k7 a) start from ΣM = 0, ΣF_y = 0, kx = mg, F_g = ma_n, the gravitation law and the definition of the level. Each simplifies symbolically to the form the Sijoitus uses, every step is correct, and each matches its rubric's equation criterion.

The Osa 1 keys are right, with exactly one correct option and real-error distractors. The Doppler figure (B high to low through f₀ at t = 0) and the oscillation figure (C = −sin) match the keys. The force diagrams are right: on the board the bolt force points down and N is the sum of the three downward forces; on the camera gravity is the only force, with v and a as separate arrows.

The scope is FY5 with γ and no ω. The limits of the noise model are stated. The hash is identical at start and end.
