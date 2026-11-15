VERDICT: FAIL
CONTENT-HASH: 84c1d79c5900ea6f
Review of the recognition chart (queue 9c) and the term change against the version passed at dc13071f6130e116; full on the chart, delta on the rest.

## Blocking
- B (row 2, "valo irrottaa elektroneja"): The pill reads $hf = W + E_\text{k}$. The equation holds only for the electrons with the greatest kinetic energy. Kaava writes $hf = W + E_\text{k,max}$, and the aria-label says "elektronin suurin liike-energia", so the pill contradicts both. Fix: write $E_\text{k,max}$ in the pill, for example $E_\text{k,max} = hf - W$ or the Kaava form at a smaller size.

## Polish
- C: Row 8 shows $\dot{H} \propto 1/r^2$, which Kaava gives only as a *Johda itse* result. Showing it as the result of a choice is acceptable, and its condition (pistemäinen lähde) is stated. The aria-label could add "kun väliaine ei vaimenna".
- C: Row 9 $I = I_0 e^{-\mu x}$ is correct for a narrow gamma beam, as in the unit.

## Checked
- Row 1, frequency or wavelength → $E = hf$: matches Kaava.
- Row 3, emission or absorption → $hf = E_\text{y} - E_\text{a}$: matches Kaava.
- Rows 4–5: $N = N_0 e^{-\lambda t}$ and $A = \lambda N$ (decays per second) are correct.
- Row 6, mass defect → $E = \Delta m c^2$: matches Kaava's definition of $\Delta m$ (reactants − products).
- Row 7, radiation type taken into account → $H = w_\text{R} D$: correct.
- Row 8: $1/r^2$ agrees with the unit's derivation $\dot{H}_2 = \dot{H}_1 (r_1/r_2)^2$.
- Row 9: correct, see Polish.
- The aria-label matches every row except row 2, where it says "suurin" and the chart does not.
- The teacher.md change (käsitekartta → tunnistuskaavio, branches → rows) does not touch the physics.
