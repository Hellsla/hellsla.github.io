VERDICT: PASS
CONTENT-HASH: 7e7678c3184e7153

## Blocking
None.

## Polish
None. The Laajennus now limits the supply's series resistance to charging. The OO tuki line suggesting trying several function types is fine.

## Previous polish, now fixed
- The Laajennus fits a line with a free intercept: $\tau = (R + r)\cdot C$, and the slope is still $C$. Correct.
- teacher.md gives the direction of each error source. $R_\text{V}$ across C gives $\tau = C\cdot\dfrac{R R_\text{V}}{R + R_\text{V}}$, so $C$ is too small, most at large $R$. Leakage also makes $C$ too small, most at large $R$. Series $r$ makes $C$ too large, most at small $R$, and shows up as the intercept. All correct.
- Charging linearisation uses the measured final voltage as $U_0$, and the page notes that $D$ in the exponential fit handles this. Correct.

## Checked (unchanged physics re-verified)
- **Model and conditions.** These are correct: $Q = Cu$, $\Delta u = -\dfrac{u}{RC}\cdot\Delta t$, $\tau = RC$ with $\Omega\cdot\text{F} = \text{s}$, and $u = U_0\mathrm{e}^{-t/\tau}$, with $0{,}37$ per $\tau$ and the tangent meeting the axis at $\tau$. Charging uses $U_0 - u$. The assumptions (no current through the meter, no leakage, small series resistance) are stated in the theory text for all modes.
- **Restructure.** The model block is now O only. The OO "Tarkista mallisi" box repeats the same formulas correctly. Mode I builds the model from the stated rate of change. Prediction 2 is now asked in all modes, and the theory supports its answer (the same time).
- **Fits.** $A\mathrm{e}^{-Bt}+D$ with $\tau = 1/B$, and $\ln u$ against $t$ with slope $-1/\tau$. $\Delta\tau/\tau = \Delta B/B$. The choice of $t = 0$ does not matter.
- **Uncertainty.** $\Delta C/C = \Delta\tau/\tau + \Delta R/R$. Overlap is read as "sopusoinnussa", not as proof.
- **Safety.** It covers polarity (consistent with the circuit), the voltage limit from the marking or the teacher with no invented value, discharging through R, no shorting, the meter's range and low voltage only.
- **Circuit.** A charges and B discharges through R. V is across C, and the curved plate is −.
- **Figures.** They are unchanged. The model graphs have no points, and the hero's screen is empty.
- **Card p. 9.** All its points are covered.
