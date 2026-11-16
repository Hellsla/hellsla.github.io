VERDICT: PASS
CONTENT-HASH: 73d5f564adacfc16

## Blocking
None.

## Polish
- fy7-s2 d, solution "Conclusion": "the iron core is made of thin insulated sheets" is stated as fact, but the task says only "an iron core". Write "is usually made of" (B, minor; the rubric does not ask for it).
- fy7-s1 e: "varies by as much as 10 %" can be read as a ±5 % spread. The argument needs about 9 % below the full energy. Saying "up to 10 % below the full value" removes the doubt.
- fy7-s1 d, reasonableness: "much larger than the size of the slit" refers to a slit width the task never gives. Say "a slit of a few millimetres" or drop the comparison.
- fy7-s5 e, solution: "greater for violet ... because violet light travels more slowly in glass" just restates n = c/v. It is not a cause. Write "that is, violet light travels more slowly".
- fy7-s4: part a keeps three significant figures (peak on a grid line), but part e gives two for the same 2.0 µm. Both are justified, but the reasons should read the same.

## Checked
- I recomputed every answer and intermediate value with my own formulas, independently of answers.py, and compared them side by side. All agree within rounding:
  - s1: v 7.251·10⁵ m/s, U_s 2.90 kV, B 0.207 T, Δx 7.24 cm, m₁₀/m₁₁ 0.910.
  - s2: f 33.3 Hz, U 9.90 V, 18.8 and 11.4 km/h, F 0.955 N; a 1 % grade gives 8.8 N.
  - s3: R 9.40 Ω, losses 846 and 28.0 kW, 17.2 kV, 0.47 %, 4540 mm², 7.6 cm, 20 and 613 t, 0.012 and 8.53 N/m, G/l 3.97 N/m.
  - s4: 1449 K and 1176 °C, α_r 80.44°, θ 13.84° (also via √(n₁²−n₂²)), ±36 K, 362 nm, reflection maxima and minima at 500, 667 and 400 nm.
  - s5: least-squares slope 6.003·10⁻⁴ nm⁻¹ (600 lines/mm), 589.1 nm, ±2.7 nm, He/Na angles 20.64/20.70° and 44.84/44.97°.
- s5 data: all seven angles follow from d = 1666.7 nm and the NIST wavelengths to within 0.1°. The source_note says they are simulated.
- Directions: qv̄×B̄ points up in the selector, so the upper plate is positive, and the analyser beam curves upward as drawn. Opposite currents repel. Both film reflections invert the wave (1.00 → 1.38 → 1.50).
- Figures: the spectrum peak is at 2.000 µm (Planck curve, T = 1449 K). The signal has a 30 ms period and a 14 V peak. The fibre figure is marked "angles exaggerated", and the grating line passes (1300; 0.780).
- Scope: everything falls within the FY7 contents and scope notes (selector, mass spectrometer, e₀ = NBA·2πf, effective values, Wien, TIR, thin film, grating). W = qU and P = Fv come from earlier courses. Nothing from FY8.
- The points of every part's criteria add up to the part's points. Each criterion asks only for what the task gives. The accepted alternative methods are correct, and every tolerance covers a correctly rounded answer.
