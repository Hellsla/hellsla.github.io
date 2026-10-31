VERDICT: PASS
CONTENT-HASH: 2bef441e9537a529

## Blocking
None. The previous blocking point is fixed. UV and IR LEDs are never looked at directly, and UV LEDs are used only with eye protection the teacher provides. This is stated in the student safety list, in the Mittaa safety line, and in teacher.md (Valmistelu and Turvallisuus). The Valon syttyminen method is now limited to visible-light LEDs and says why: IR light cannot be seen, and UV and IR LEDs are not looked at.

## Polish
None blocking. Both earlier polish points are done:
- The band-gap clause is correct for the level: the photon energy is about the band gap, and $eU_\text{k}$ is only an approximation to it.
- The text now says that offsets which differ between materials do change the slope.

## Checked
- **Model:** $E = hf$, $c = f\lambda$, $eU_\text{k} \approx hf$ and $U_\text{k} = \dfrac{hc}{e}\cdot\dfrac{1}{\lambda}$. The slope unit is V·m, and $h = ek/c$ gives J·s. The derivation is now in the O-only "Malli kuvaajaksi" and repeated in the O OO check "miksi juuri nämä akselit". The two agree, as do the alternative axes $eU_\text{k}$ against $f$ (slope $h$) and the curve that appears when λ is on the axis.
- **Model limits:** a band of wavelengths, a threshold that depends on the method, internal resistance, heating, the band gap, and a common offset versus material-dependent offsets.
- **Three threshold methods:** extrapolating the steep part, the light onset (visible LEDs only), and a fixed small current. All are correct with honest trade-offs, and the same method is used for every LED.
- **Uncertainty:**
  - $\Delta h/h = \Delta k/k$, since $e$ and $c$ are exact.
  - The relative uncertainty of $1/\lambda$ equals that of λ.
  - Mode O is now fixed to the steepest and shallowest lines; mode OO chooses between that and the fit's standard error.
  - The values of $e$, $c$ and $h$ are quoted correctly.
- **Grating:** $d\sin\theta = \lambda$ (first order), $d = 1\ \text{mm}/N$ and $\tan\theta = x/L$ match the figure's geometry. The wording on overlapping intervals follows the guardrail.
- **Circuit:** a fixed $R_\text{s}$ plus a rheostat, the LED forward-biased, the ammeter in series and the voltmeter across the LED only. No current limit or resistor value is invented; the teacher gives them.
- **Figures:**
  - The I–U curve and the $U_\text{k}$–$1/\lambda$ graph have no ticks, points or numbers, and both are labelled as models.
  - The rerouted opening illustration is consistent with the circuit, and its meters show no readings.
  - No wavelengths are invented, and students are told not to guess λ from colour.
  - LaTeX labels, \cdot, no \vec.
- **Consistency:** the predictions, the analysis questions, the uncertainty section, the conclusions, the report section, teacher.md (misconceptions and differentiation) and the card on p. 13 agree.
