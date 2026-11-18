VERDICT: PASS
CONTENT-HASH: b1adef22b9b88866

## Blocking
None.

## Polish
- fy7-s4 c (carried from round 2, still open): "kolme merkitsevää numeroa kuten taitekertoimissa" does not hold for θ. θ depends on n₁² − n₂², so n₂ = 1,42 ± 0,005 gives 12,0–15,5°. Either give θ ≈ 14° or justify three figures.
- fy7-s2 c Kaava: N, B and A appear only to cancel in κ. A clause saying they stay constant would help, and the Periaate already says so. Not an error.

## Checked
- Work queue 8g rewrote the Kaava steps. I checked each one symbolically: it starts from the basic law, the derivation is valid, and its last symbolic form is the one the Sijoitus step uses.
  - s1 b: W = eU → ½mv² → v. s1 c: F_s = F_m → E = vB_s → U_s = vB_s d. s1 d: F_m = ma_r → B = m₁₁v/(er), r₁₀ = (m₁₀/m₁₁) r, Δx = 2(r − r₁₀).
  - s2 b: f_p = f/14, v = πD f_p. s2 c: U = NBA·2πf/√2 and f = 14v/(πD) give U = κv with κ = 28NBA/(√2 D), which is correct; κ cancels in the ratio. s2 e: η = P_valo/P_otto with P_otto = Fv gives F = P_valo/(ηv).
  - s3 a and b: R = ρl/A, I = P/U, P_h = RI² = ρ(l/A)(P/U)². s3 c: U = U_R + U_k. s3 e: F/l = IB = μ₀I²/(2πr) and G/l = ρ_Al A g.
  - s4 c: n₁ sin α_r = n₂ sin 90°, β = 90° − α_r, θ = arcsin(n₁ sin β). s4 e: Δs = 2nd = λ/2 → d = λ/(4n); the Periaate states the k = 0 condition. s5 b: slope = 1/d, N = 1 mm/d.
- I recomputed every number from the task data in my own script, side by side with tasks.json and answers.py. All agree:
  - s1: 7,251·10⁵ m/s; 2900 V; 0,2069 T; 7,24 cm; v₁₀ 7,60·10⁵ m/s; mass ratio 0,910.
  - s2: 33,3 Hz; 9,90 V; 18,85 km/h; 11,42 km/h; 0,955 N.
  - s3: 9,40 Ω; 846 kW; 27,97 kW; 17,18 kV; 513 V; 4538 mm²; 7,60 cm; 20 t and 613 t; 0,012 and 8,53 N/m; 3,97 N/m (2,15× the weight; 0,30 %).
  - s4: 1449 K (1176 °C); ±36 K; 80,44°; 13,84°; 362 nm; 2nd = 1000 nm.
  - s5: slope 6,003·10⁻⁴ /nm (600 /mm); 589,1 nm; 586,4 and 591,8 nm; first order 20,64° and 20,70°; second order 44,84° and 44,97°.
- No number, answer, task or rubric changed. The physics, scope, rubrics, point sums and Hyväksytään myös methods are as judged in round 2.
- The content hash is b1adef22b9b88866 at both the start and the end of the review.
