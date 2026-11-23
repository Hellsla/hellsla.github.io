VERDICT: FAIL
CONTENT-HASH: 8d806aafb6c72eb4

## Blocking
1. **fy6-s1 d, solutions, creep paragraph (A):** drift velocity "of the order of millimetres per second" is too large. (0.6 A in 0.5 mm² Cu: ≈ 0.09 mm/s). Write "less than a millimetre per second" or drop the number.
2. **fy6-s4 a, Reasonableness (A, definition):** "an object with a weight of one kilogram" treats weight as a mass. Write "an object of mass 1.0 kg". The 1.5 m is right.
3. **fy6-s4 a, Answer, rounding reason:** "at most two or three figures" gives no reason. Under P7, 300 V and 330 µF have three figures, so the answer is 14.9 J. Give that, or state the values are two-figure; align part b.

## Polish
- fy6-s2 Hyväksytään myös, item 3, "the voltage of the lamps may also be calculated": part d now asks for this voltage, so the line is stale.
- fy6-s2 figure: it labels the cable R_k and has the Finnish "sulake", but the en text uses R_c.
- fy6-s1 c Principle: "heat is produced" should be "energy is transferred as heat".
- fy6-s3 c criterion 1: credit any correct air-resistance explanation. without requiring drag ≈ electric force.

## Checked
- All solution numbers, recomputed in my own script. They agree with answers.py and the rubrics:
  - s1: fit −1.194 V/A, 4.598 V, largest residual 0.020 V; 0.50 A, 2.0 W, 13 %, ±0.08 Ω, creep 0.06 Ω, 3.8 A.
  - s2: 2.5 A, 16.7 W, 30 W balance; 1.76 A, 10.6 V, 18.7 W, 2.5 W; 4.29 A, 8.6 V, 14.7 W.
  - s3: 1.8·10⁻⁷ N, weight 2 %, 13.4 m/s, 14 %, 3.1·10⁻⁸ J, 3.2·10⁻⁹ N (0.82 mg).
  - s4: 14.85 J, 6.86 J, 46 % against 27 %, 26.4 A, 6.9 kW, 0.30 A.
- Models and their conditions:
  - EMF with internal resistance; the drift bias from rising current over time has the right direction.
  - Constant-resistance lamps with a series cable; what the fuse does.
  - Uniform field with the energy principle; Coulomb's law for point charges.
  - Capacitor energy, ΔQ = CΔU, and the stored-charge hazard.
  - Formula steps start from the basic equations.
- Scope: within FY6 (no exponentials, no capacitor connections).
- Assessment: the points add up in every part, the criteria match the tasks, other methods are listed, data declared invented.
- Figures: meters placed correctly, current + → −, field from +60 kV to ground.
