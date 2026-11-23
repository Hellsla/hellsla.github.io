VERDICT: PASS
CONTENT-HASH: 6c4d981f2b165061

## Blocking
None. The three round-1 items are fixed:
- s1 d: the drift velocity is now "less than a millimetre per second, about 0.07 mm/s". I get 0.074 mm/s for 0.5 A in 0.5 mm² Cu.
- s4 a: now "an object of mass 1.0 kg", which rises 1.51 m.
- s4 a: the rounding reason is now three figures from 300 V and 330 µF (P7), giving 14.9 J. Part b gives 6.86 J and 46.2 % to match.

## Polish
- fy6-s3 b: the answer is 13.4 m/s with a 0.03 tolerance, but the solution's rounded answer of 13 m/s is 3.1 % off. That is outside the tolerance. Use tolerance 0.04, or keep 13.4 in the Answer line.
- fy6-s2 Hyväksytään myös, item 3: part d now asks for the lamp voltage itself, so "may also be calculated" is stale (carried over from round 1).
- fy6-s1 c Principle: "heat is produced both in the resistor and inside the battery" should say energy is transferred as heat (P1 wording; carried over from round 1).
- fy6-s4 b Substitution: the fraction is computed as 0.46, but the Answer line gives 46.2 %. Write 0.462 so the two agree.

## Checked
- I recomputed every solution number in my own script, from the task data with my own formulas. All of them agree with answers.py and the rubrics:
  - s1: fit −1.194 V/A and 4.598 V; largest residual 0.020 V; 3.8 A; 0.50 A, 2.0 W, 0.30 W, 13 %; ±0.08 Ω; creep 0.06 Ω.
  - s2: 2.5 A; 10.0 V; 16.7 W, 8.3 W and 5.0 W, summing to 30 W; 1.76 A, 1.41 V, 10.6 V, 18.7 W, 2.5 W; 4.29 A, 8.57 V, 14.7 W (2.9 times 5.0 W).
  - s3: 3.0·10⁵ V/m; 1.8·10⁻⁷ N; weight 2.2 %; field 0.1 of breakdown; 13.4 m/s; 450 m/s²; 14 %; 3.1·10⁻⁸ J; 3.24·10⁻⁹ N (1.8 % of F, 0.82 mg).
  - s4: 14.85 J; 7.99 J; 6.86 J; 46.2 % against 27 %; 26.4 A; 6.9 kW; 0.099 C; 0.30 A.
- Models and conditions:
  - s1: EMF with internal resistance. The bias from discharge (current rising with time) has the right direction, and the warming effect is stated as uncertain.
  - s2: constant-resistance lamps with a series cable. The fuse's operating time is stated as a simplification, and the fuse protects the cable.
  - s3: uniform field and the energy principle, with the assumptions stated. The terminal-speed picture is plausible (droplet r ≈ 46 µm). Coulomb's law for point charges, with r ≫ size.
  - s4: E = ½CU², ΔQ = CΔU. The stored-charge hazard is described as an idealised estimate.
- Energy wording: the air's internal energy is transferred as heat (P1).
- Significant figures follow P7.
- Scope: within FY6. Capacitors are qualitative only (no exponentials, no connections), and Coulomb's law and the fuse are in the central contents.
- Assessment:
  - Every part's criterion points add up to its part points (15/15/16/14).
  - Each criterion asks only what the task gives and asks.
  - Other methods are accepted, the tolerances cover the accepted ranges, and the data is declared invented.
- Figures: the meters are placed correctly; current flows + → −; the s1 graph line passes through (0.10; 4.48) and (0.60; 3.88) with E = 4.60 V; the field points from +60 kV to ground.
