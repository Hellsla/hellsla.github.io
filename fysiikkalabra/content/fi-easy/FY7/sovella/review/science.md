VERDICT: PASS
CONTENT-HASH: 7627be825e67e9d3

## Blocking
None.

## Polish
- fy7-s2 c: the answer is 11,4 km/h with a tolerance of 0,03, but the solution's own rounded answer "≈ 11 km/h" (and the lower end of "Hyväksytään myös 11–12 km/h") is 3,6 % away. Widen the tolerance to 0,05 or give the answer as 11,4 km/h.
- fy7-s2 d (criterion 3 and the model answer): in a hub dynamo the magnet ring turns with the hub shell, so the field in the shell barely changes and the shell is a poor example of where eddy currents arise. The alternating flux runs through the stationary core and the other stator metal parts. Name those parts instead of "napaan".
- fy7-s4 c Järkevyys: "linssi, joka kokoaa valon kapeaksi keilaksi" is vague. The point is that the light has to reach the fibre's end face inside a cone of half-angle ≈ 13,8°.
- fy7-s2 e Järkevyys: "hitaammin ajettaessa sama teho vaatii suuremman voiman" holds only if the lamp's power stays 3 W at lower speed. Add "jos valon teho pysyy samana".

## Checked
One script recomputed every number from the task data with my own formulas. All of them agree with answers.py and the solutions, mistakes included:
- s1: v, E, U_s, B, r₁₀, Δx = 7,24 cm, v₁₀ and the ratio 0,910.
- s2: f, U, v = 5,236 m/s, v_min, F = 0,955 N.
- s3: R = 9,40 Ω, both losses, U_k, the area and diameter, the masses, F/l and G/l.
- s4: 1449 K, ±36 K, α_r, θ (= arcsin √(n₁² − n₂²)), d = 362 nm and the visible maxima and minima.
- s5: the slope through the origin is 6,003·10⁻⁴ 1/nm, every angle comes back to its rounded value, λ = 589 ± 3 nm, and the He/Na angles agree in both orders.

Physics: the force directions (upper plate positive, the analyser bends the beam the same way), the pole count, e₀ ∝ f, Lenz drag with P = Fv, repulsion of opposite currents under AC, the black-body peak and emissivity, the phase changes at both reflections, the visible tail of Planck's curve, and grating vs. prism.

Scope is FY7 only, with no self-induction. Points equal the criteria sums, and each criterion asks only what its part asks. The figures are correct, and the s5 data is declared as simulated. The hash was the same at the start and the end.
