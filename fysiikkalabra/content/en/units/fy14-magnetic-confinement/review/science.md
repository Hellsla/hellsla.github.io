VERDICT: PASS
CONTENT-HASH: 78ca43a94673e3d9

## Blocking
None.

## Polish
1. **`inquiry.json` alpha-task, Reasonableness.** "about 340 times the energy of the deuteron in the worked example ($10\ \text{keV}$)": the worked example never gives this energy. Add the step: "($\frac{1}{2}mv^2 = 1.67 \cdot 10^{-15}\ \text{J} \approx 10\ \text{keV}$)".
2. **`inquiry.json` simulation `model`.** "all speeds below 4 % of the speed of light" is true of the sim, whose maximum is $10^{7}$ m/s, or 3.3 % of c. The alpha task's 3.5 MeV alpha (outside the sim) moves at 4.3 % of c. The solution's "about 4 %" is fine, but "below 4 %" should not be quoted for it.
3. **`inquiry.json` simulation `howto`.** The *Electric field* checkbox shows the $E \times B$ drift, which the theory never names. Add one clause, for example "the centre of the circle then drifts sideways, the same way for ions and electrons, which is how the separated charges in a ring push the plasma outward". The *Torus* section can then refer back to it.

## Checked
- Recomputed with CODATA 2022 values. Worked example: $r = 4.17$ mm, $T = 26.2$ ns, 38 million turns per second. Proton at $2.0 \cdot 10^{6}$ m/s: 20.9 / 10.4 mm and 65.6 / 32.8 ns at 1 / 2 T. Deuteron 41.7 mm and alpha 41.5 mm; electron 0.0114 mm. Alpha at 3.5 MeV: $v = 1.299 \cdot 10^{7}$ m/s, $r = 5.08$ cm. The mistake 10.2 cm (charge $e$) is correct. Mirror with $R_m = 4$: loss cone 30°.
- Force direction (check-2): $q\,\overline{v} \times \overline{B}$ with $\overline{v}$ to the right and $\overline{B}$ into the page gives a force up the page and anticlockwise motion. This agrees with the figure, the model (`uniform()`) and the sim's force arrow ($F = q(v_yB_z, -v_xB_z)$).
- Mirror physics: $\mu$ is conserved, $\sin^2\theta \ge B_0/B_{\max}$. The theory, sim and model text agree. `node tests/models/magnetic.test.js` runs 708 checks, all OK. In Playwright at the experiment values, `simState` gives $r$ = 41.8, 20.9, 10.4, 5.22 mm at 0.5, 1, 2, 4 T, and $T$ halves with each step. At 10° and 20° the proton escapes (`escaped` true, `trapped` false); at 30–80° it is trapped and does not escape. Each experiment varies only one parameter; the others are locked.
- Single-particle vs collective: the *Collective* section, check-3 and the sim's note state the model's limits (collisions, self-fields, turbulence, instabilities, ZETA 1958). Toroidal drift: the grad-B and curvature drift separates the charges, and $E \times B$ moves the plasma outward. The cause is correct.
- Tungsten melts at about 3400 °C (3422). Van Allen belts 1958.
