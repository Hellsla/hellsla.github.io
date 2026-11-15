VERDICT: PASS
CONTENT-HASH: bbc2878b1964517a

## Blocking
None.

## Polish
- fy4-s2 a) Järkevyys ("osa energiasta muuttuu lämmöksi") and b) Järkevyys ("yli puolet energiasta muuttuu lämmöksi") break the P1 guardrail (heat-into): better "muuttuu sisäenergiaksi, joka siirtyy lämpönä ympäristöön". Both are listed in `docs/physics-phrases-known.tsv` for work queue 18, so they do not block 8m.
- fy4-s3 e) "Laskettu arvo on siis alaraja" is true of that one assumption only. The closing paragraph puts it right, so this is a C-level point.

## Checked
- Term change 8m: every friction in the set is now sliding friction ("liukukitka", "liukukitkakerroin") in tasks.json (s1 b and c), solutions.md (s1 b and c, s3 a), the fy4-s1-fbd alt text and figures.py. No "liikekitka" is left. No static friction occurs in the set, so "täysin kehittynyt lepokitka eli lähtökitka" is not needed. Skis and locked tyres do slide, so the term is right.
- Recomputed in one independent script: slopes 0,3895 and 0,2447; μ_A 0,0301 and μ_B 0,0449; g sinα 0,684 and g cosα 9,786; Δμ 0,0020; ±0,1° moves both μ by 0,0017; the quadratic fit gives a₀ 0,449 (a line would give 0,55), μ_A0 0,0241 and Δμ 0,0060 (≈ 1/5, ≈ 3 × 0,002). s2: 17,16 m/s (61,8 km/h); 9123 J and 3889 J; 29,08 N (4,8 % of the weight); 57 % lost; 13,57 m/s (13,58 m/s with 29 N). s3: 7,86 m/s (28,3 km/h) and μg 7,36 m/s²; 13,64 m/s (49,1 km/h); kinetic energy 158 kJ → 91 kJ (42 % lost); 4455 N, 6,68 × the weight; friction impulse 2605 N·s (11 %), v_B up to 15,2 m/s; μ < 0,50 would be needed for under 40 km/h. Everything agrees with answers.py and the solutions.
- Tolerances cover the accepted ranges ("Hyväksytään myös": slopes, a₀ 0,43–0,47, rounded intermediate values). The points add up: 19, 14 and 16.
- Physics: N = mg cosα, friction against the motion, no forward force, acceleration drawn apart from the forces and the components marked as such. The voimakuvio fence values (706,32; 704,60; 21,19 N) are correct. The direction of the drag bias in s1 d and e is right. s2: the wire's force does no work, and the reasoning on the models in d is sound. s3: momentum is conserved in the short collision, the collision is perfectly inelastic, and the whiplash and impulse reasoning is right.
- Scope: all within FY4 (air resistance is fy4-14). Data honestly labelled.
