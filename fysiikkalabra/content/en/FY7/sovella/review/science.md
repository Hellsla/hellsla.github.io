VERDICT: PASS
CONTENT-HASH: 30715bc328c977a1

## Blocking
None.

## Polish
- fy7-s3 c, rubric `conclusion`: the detail adds the 110 kV voltage drop, which part c does not ask for. Mark it optional.
- fy7-s3 e: the force computed with effective currents is the time average; with AC the instantaneous force peaks at twice that. Add "on average" (B, minor; the conclusion holds).
- fy7-s2 e, reasonableness: "felt most on an uphill" assumes the lamp still gets its full power at low speed, but part c's model says U ∝ v. Add that condition (B, minor).
- Still open from round 1:
  - fy7-s5 e: "because violet light travels more slowly" should read "that is".
  - fy7-s2 d: "the core is made of" should read "is usually made of".
  - fy7-s1 e: "up to 10 % below the full value".

## Checked
- 8g Formula steps (every part): each starts from its basic law and solves symbolically before substituting:
  - s1: eU = ½mv²; F_s = F_m → U_s = vB_sd; F_m = ma_r → B, r₁₀, Δx.
  - s2: v = πDf/14; κ = 28NBA/(√2 D), verified; η, P = Fv.
  - s3: R, I, P_h; U = U_R + U_mine; B → F/l, G/l.
  - s4: n₁ sin α_r = n₂ → θ; 2nd = λ/2.
  - s5: a = 1/d.

  The algebra and the stated conditions are correct.
- I recomputed every answer with my own script. All agree with answers.py and the solutions:
  - s1: 7.251·10⁵ m/s, 2.90 kV, 0.207 T, 7.24 cm.
  - s2: 33.3 Hz, 9.90 V, 18.8 and 11.4 km/h, 0.955 N.
  - s3: 9.40 Ω, 846 and 28.0 kW, 17.18 kV, 7.6 cm, 613 t, 0.012 and 8.53 N/m, 3.97 N/m.
  - s4: 1176 °C, 80.44°, 13.84°, ±36 K, 362 nm.
  - s5: 600 lines/mm, 589.1 nm, 586.4–591.8 nm, 20.64/20.70° and 44.84/44.98°.
- Directions: the magnetic force points up and the upper plate is positive; the analyser beam curves up as drawn; opposite currents repel; both film reflections invert.
- Figures: the Planck peak is at 2.000 µm, the signal has a 30 ms period and a 14 V peak, and the fibre angles are marked as exaggerated.
- Scope: FY7 only.
- Points add up, the alternatives are correct, and no data is invented.
