VERDICT: PASS
CONTENT-HASH: 24d1a9be543a99e0

## Blocking

## Polish
- lesson.md:387 and inquiry.json hook — "Hyppääjä osuu alustaan samalla nopeudella" is stated as fact, while check-3's model answer says "oletetaan". The top of the mat is higher than the ground, so the speed is only about the same. You could say "likimain samalla nopeudella" in both places. This is a C-level simplification and the same in content/fi.

## Checked
- Full review against content/fi/FY4/fy4-9: the same concepts, formulas, sign conventions and conclusions. The changed answer paragraph (lesson.md:387) and check-3's model answer now say it the right way: the same impulse of the net force, a longer stopping time, a smaller average net force and also a smaller average force from the surface (net force plus weight), so less strain and a lower risk of injury. No "pieni voima ei vahingoita" claim is left.
- Recomputed in one script, analytically, and confirmed with model.js and lesson-answers.py. Exp-1: Δt = (π/2)√(m/k) gives 0,0393, 0,0785 and 0,157 s, F_max = v√(mk) gives 80, 40 and 20 N, and I = −2,00 N·s each time. Exp-2 (bounce): −4,00 N·s, v₂ = −2,00 m/s and Δt = 0,157 s. Exp-3: 28,3, 40 and 56,6 N, with p₀ = 1, 2 and 4 kg·m/s. The half-sine average is 2/π ≈ 0,64 F_max.
- Example: 3,48 kg·m/s and 870 N; the weight 0,569 N is about 1/1500 of that; the sign error gives 145 N. Siirto: 80 N, with the mistakes 4,0, 0,20 and 800 N, about 8 kg's weight, and 400 N for a stiff hand. Check-2: 5,4 N·s gives 12 m/s, 43 km/h and an average of 450 N. Retrieval 1,5 m/s; Etsi virhe −4,0 kg·m/s; figures 9,0, 9,0 and −4,5 kg·m/s, and −4,0 kg·m/s.
- Sim: the crushable pulse gives I = mv, and its crush distance is ∫v dτ. simState has the keys dt, Fmax (a magnitude), I, v2, dp and p1. Each experiment locks the other parameters.
- Every choice has exactly one correct option, and every distractor's feedback is right. The exit ticket agrees with the theory.
