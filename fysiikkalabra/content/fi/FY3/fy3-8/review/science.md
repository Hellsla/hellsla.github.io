VERDICT: PASS
CONTENT-HASH: 26292e2aed4f183d

## Blocking

## Polish
- inquiry.json johtopaatos.model — "$\Delta l = 6{,}0\,\text{mm}$" stands beside "$12{,}0\,\text{mm}$", while the sim and the predictions say $6{,}00\,\text{mm}$. — Write $6{,}00\,\text{mm}$.
- inquiry.json pred-3 (Bea feedback) and simulaatio.model — "Teoriatiivistelmä". The stage is now Teoria. — Write "Teoria".
- lesson.md:427 — "jäätyessään se laajenee. Siksi jää kelluu ja järvet jäätyvät pinnalta". The lake freezes from the top because of the 4 °C density maximum (line 288); the expansion on freezing explains only why the ice floats. — Give the two causes separately.
- lesson.md:286, inquiry.json olomuodot and check-3 — The gas's larger expansion is put down only to "lähes vapaat" particles. Leaving out the pressure mechanism is acceptable at this level (C). — Consider adding half a sentence on the gas pushing against a constant outside pressure.

## Checked
- Round 1 blocking item fixed. lesson.md:420 now gives the change as "noin $86\,\text{mm}$" and the joint's minimum as $87\,\text{mm}$, rounded up with the reason stated. The sig-fig justification is correct (α and ΔT limit it to two figures).
- One script recomputed every number from the task data with my own formulas. Example: $86{,}4\,\text{mm}$, $0{,}072\,\%$. pred-1 and pred-2: $6{,}00$ and $12{,}0\,\text{mm}$, $0{,}0600\,\%$. olomuodot: $0{,}36$, $2{,}1$, $11$, $34\,\text{cm}^3$. virhe: $27{,}9 \approx 28$ vs $1{,}84\,\text{mm}$, ratio about 15, $0{,}70\,\%$. siirto: $44\,\text{mm}$, mistakes $0{,}044$ and $110$, glass ratio about 41, about $43\,\text{mm}$ with glass. check-2: $23 \cdot 10^{-6}$ from both columns, mistakes 46 and 15,3. Exit ticket: $21\,\text{mm}$. Air/steel γ about 94 ("noin sata"). Steel α of about $10^{-5}$ per kelvin ("sadastuhannesosa"). Everything agrees.
- The new photo (Kruunuvuorensilta liikuntasauma) shows a real expansion joint. Its caption says only that the joint lets the structure move, for example when the temperature changes, which is correct and not overstated.
- Micro-model asymmetry (repulsion is steep, attraction weakens gradually) is correct and consistent across the theory, pred-3, the johtopäätös and check-3. The particles do not grow.
- γ ≈ 3α and its small-change reasoning are right. The limits (about 100 K for solids, a liquid's γ near 20 °C) are stated where the formulas are used.
- The water anomaly, the hole growing, the shrink fit, the bimetal strip and the sagging power lines are physically right.
- Each choice has exactly one correct option, and the feedback on every distractor is correct.
- sim.js implements ΔL = αL₀ΔT with ΔT from 20 °C. The ×100 exaggeration is labelled, the largest real change is 0,23 % (< 0,3 % as claimed), and the model box says the spacing is set from the formula with the vibration drawn symmetric.
- exp-1 and exp-2 vary one parameter with the others locked. simState gives dT, dL and rel.
- The figures (particles, rod, flask) are marked exaggerated, and their labels agree with the text.
