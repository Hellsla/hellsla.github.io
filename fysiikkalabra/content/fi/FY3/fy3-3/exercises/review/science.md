VERDICT: PASS
CONTENT-HASH: 839f1b0810ea0dcf
SCOPE: delta added-exercise from e1dd7ab8f7baa8e3 base 81db4a6fd727

## Blocking

## Polish
- exercises/solutions.md (fy3-3-L2-08, Vastaus) — the figure reason "noin yhden kilopascalin tarkkuudella" is fair, but on a 25 kPa grid a reading of ±2 kPa is more realistic; the tolerance still covers that (see Checked), so only the wording could say "1–2 kPa".
- exercises/exercises.json (fy3-3-L1-10) — as before, optional: liquid nitrogen is at −196 °C when it boils at normal pressure ("avoimessa astiassa").

## Checked
- L2-08 now asks for the temperature at $100\,\text{kPa}$, inside the measured range (interpolation, not extrapolation); the linear $p(\theta)$ at constant $V$ and $n$ is stated in the task.
- Recomputed from the figure's data: endpoints $k = 27{,}5/100 = 0{,}275\,\text{kPa/°C}$, $\theta = 25/0{,}275 = 90{,}9\,{}^\circ\text{C}$; least-squares line $90{,}2\,{}^\circ\text{C}$; neighbouring pair (75; 100 °C) $90{,}4\,{}^\circ\text{C}$. answers.py gives 90,9.
- Tolerance 0,08 (83,6–98,2 °C) against the reading error: the start and end pressures each misread by up to ±1 kPa give 87,3–94,5 °C, and by ±2 kPa 83,6–98,2 °C, all accepted; so the tolerance covers a realistic reading error, and the fit and pair methods.
- Cross-check with another correct model: $p \propto T$ from $(0\,{}^\circ\text{C};\ 75\,\text{kPa})$ gives $T = 273{,}15 \cdot 100/75 = 364\,\text{K}$, i.e. $91\,{}^\circ\text{C}$, so the data are consistent with the lesson's model.
- Figure: 75 kPa at 0 °C lies on a grid line, 102,5 kPa just above the 100 kPa line, as the solution says; the description lists the same five points and gives neither the slope nor the answer.
- Solution: "lähes samalla suoralla" now as the guardrails ask; slope from distant points; solved in symbols before substitution; no conversion needed (°C throughout); two figures; the check (between 75 and 100 °C, nearer 100) is real and back-substitution gives 100 kPa.
- L1-10 unchanged: $-196 + 273{,}15 = 77{,}15\,\text{K} \approx 77\,\text{K}$.
- Rest of the set unchanged since PASS; hash same at start and end.
