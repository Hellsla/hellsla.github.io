VERDICT: PASS
CONTENT-HASH: 6c4d981f2b165061

## Blocking
None. The round-1 items are fixed:
- s1 d: drift velocity now ≈ 0.07 mm/s (I get 0.074 mm/s).
- s4 a: now "mass 1.0 kg" (rises 1.51 m).
- s4 a: three figures under P7, so 14.9 J; part b matches (6.86 J, 46.2 %).

## Polish
- s3 b: the answer is 13.4 with tolerance 0.03, but the solution's "13 m/s" is 3.1 % off. Use tolerance 0.04.
- s2 Hyväksytään myös, item 3: stale, because part d now asks for the lamp voltage.
- s1 c Principle: "heat is produced" should say energy is transferred as heat (P1).
- s4 b Substitution: the fraction is 0.46 but the answer gives 46.2 %. Write 0.462.

## Checked
- My own script recomputed every number. It agrees with answers.py and the rubrics:
  - s1: fit −1.194 V/A and 4.598 V; residual 0.020 V; 3.8 A; 0.50 A; 2.0 W; 0.30 W; 13 %; ±0.08 Ω; creep 0.06 Ω.
  - s2: 2.5 A; 10.0 V; 16.7 + 8.3 + 5.0 = 30 W; 1.76 A; 10.6 V; 18.7 W; 2.5 W; 4.29 A; 8.57 V; 14.7 W.
  - s3: 3.0·10⁵ V/m; 1.8·10⁻⁷ N; weight 2.2 %; 13.4 m/s; 450 m/s²; 14 %; 3.1·10⁻⁸ J; 3.24·10⁻⁹ N (0.82 mg).
  - s4: 14.85 J; 7.99 J; 6.86 J; 46.2 % against 27 %; 26.4 A; 6.9 kW; 0.30 A.
- Models and conditions:
  - s1: EMF with internal resistance; the bias from discharge has the right direction.
  - s2: constant-resistance lamps with a series cable; the fuse's operating time is stated as a simplification.
  - s3: uniform field with the energy principle, assumptions stated; the terminal speed is plausible (r ≈ 46 µm); point charges.
  - s4: E = ½CU², ΔQ = CΔU; the hazard is an idealised estimate.
- P1 wording for energy into the air; significant figures follow P7.
- Scope: within FY6.
- Assessment: the points add up; each criterion asks only what the task gives; other methods are accepted; the data is declared invented.
- Figures: current + → −; the s1 line passes through (0.10; 4.48) and (0.60; 3.88) with E = 4.60 V; the field points from +60 kV to ground.
