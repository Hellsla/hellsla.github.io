VERDICT: PASS
CONTENT-HASH: 30f6496b8b1e1b29

## Blocking

## Polish
- exercises/solutions.md:99 (L3-01) — "Siksi ulkoradan juoksijan lähtöpaikka on porrastettu eteenpäin": in a race the stagger evens out the distances, it does not keep runners side by side — fix: "Samasta syystä ulkoradan lähtöpaikka on porrastettu: ulompi kaari on pidempi."

## Checked
- One script recomputed all 12 answers from the task text with my own formulas: 2,618; 18,85; 0,25; 0,9802; 7676; 0,4006; 5,984 min; 4523 1/min; 25,0; 7,710; 14,14; 19,23 km/h. They match exercises.json (within tolerance), solutions.md and answers.py output.
- L2-02 (T = 2πr/v), L2-03 (f = v/2πr) and L2-04 (same T, v ∝ r) are solved symbolically before substitution, with conversions written as substitutions.
- L3-01: rinnakkain means the same angular position, so the times are equal and v ∝ r. The model is correct.
- L3-02: a quarter lap turns v̄ by 90°, so |Δv̄| = √2·v = 14 m/s. The check against a half lap (2v) is a real check.
- L3-03: the chain speed is the same on both sprockets, f_t = (r_e/r_t)f_e, and rolling without slipping gives u = 2πRf_t. Correct, and only kinematics (no rotational dynamics).
- Magnitudes are realistic: ISS 7,68 km/s (≈ 92,5 min orbit), grinder, centrifuge, single record at 45 rpm, a 40 m Ferris wheel lap in 6 min.
- Significant figures follow the limiting data, and each reasonableness check recomputes the result another way.
- Scope: only f = 1/T and v = 2πr/T = 2πrf. No ω, no a_n.
- Hash checked at the start and the end: 30f6496b8b1e1b29.
