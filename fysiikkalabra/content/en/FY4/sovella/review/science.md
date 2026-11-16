VERDICT: PASS
CONTENT-HASH: ec85c073c6b06f71

## Blocking
None.

## Polish
- fy4-s2 a) and b) Reasonableness: "part of the energy changes into heat" and "more than half of the energy changes into heat" go against guardrail P1. The rule is that energy becomes internal energy, which is transferred to the surroundings as heat. The Finnish source has the same two sentences, and `docs/physics-phrases-known.tsv` (rows 9–10) lists them for work queue 18. Fix the English with the Finnish then, for example: "…changes into internal energy, which is transferred to the surroundings as heat". This is not blocking in this round, because the teacher deferred it to queue 18.

## Checked
- Round 1, work queue 8m. Diff against origin/main for en FY4/sovella: "kinetic friction" became "sliding friction" in tasks.json (s1 b fbd_forces, s1 c text), in solutions.md (s1 b bullet, s1 c Find, s3 a Principle) and in the figures.json alt text of fy4-s1-fbd. No other change. Grep: no "kinetic friction" or "liikekitka" is left in the en set or in figures.py. The term is right in all of them: the skis slide on the snow and the locked tyres slide on the asphalt, so $F_\mu = \mu N$ applies in both.
- Full recomputation in my own script (numpy fits, my own formulas), compared with answers.py:
  - s1: the fits give 0.3895 and 0.2447. The read slopes 0.39 and 0.245 give μ 0.030 and 0.045. The accepted slope ranges give μ 0.028–0.032 and 0.043–0.046. Δμ from ±0.02 m/s² is 0.0020, and from ±0.1° it is 0.0017.
  - s1 e: the quadratic fit gives a₀ = 0.449, μ₀ = 0.0241 and Δμ = 0.0060. The drag model k = 0.00432 agrees with ½ρC_dA/m = 0.00434. a₀ − kv² at v ≈ 3.6 m/s gives 0.393, consistent with run A. After the correction μ_B falls less than μ_A, so the claim in d) that the advantage is "at least as large" holds.
  - s2: 17.16 m/s (61.8 km/h). E_p = 9123 J, E_k = 3889 J, F = 29.08 N (4.8 % of 608 N), and 0.574 of the energy is lost. Part c gives 13.57 m/s, and 13.58 m/s with 29 N. With F ∝ m the speed is 11.2 m/s.
  - s3: v′ = 7.861 m/s (28.3 km/h), and the deceleration is 7.36 m/s². v_B = 13.64 m/s (49.1 km/h). E_k goes from 158.2 kJ to 91.2 kJ (42 % lost). F = 4455 N, 6.68 mg. The friction impulse is at most 2605 N·s (11 %), so v_B ≤ 15.2 m/s. The speed would be under 40 km/h only if μ < 0.50, which supports "clearly smaller".
- The physics is right in every part: the FBD (G, N and F_μ only, with components, not double-counted), N = mg cos α, the cable force doing no work, the work–energy principle with the zero level at the brake, momentum almost conserved, and the impulse and whiplash reasoning. The tolerances, the rounding reasons and the accepted alternatives hold. Every rubric criterion asks only what its task gives, the points add up, and the scope is FY4.
- The content hash is the same at the start and the end.
