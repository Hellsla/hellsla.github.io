VERDICT: FAIL
CONTENT-HASH: 85b6e93f673b2a8b

## Blocking
- lesson.md:213 — (A) The rounding reason is wrong under the house rule P7. The worked example says the area $150\,\text{cm}^2$ "on annettu kahdella numerolla" and gives $F \approx 1{,}8\,\text{kN}$. A given value's trailing zero counts as significant unless the task says otherwise (480 kW has three figures), so the area has three figures, like $12{,}0\,\text{m}$ and $101\,\text{kPa}$. — Give $F \approx 1{,}77\,\text{kN}$ with three figures and a matching reason. The alternative is to make the task say the area is approximate ("noin $150\,\text{cm}^2$") and keep $1{,}8\,\text{kN}$. Update the check line "noin $180\,\text{kg}$" only if the result changes.

## Polish
- inquiry.json pred-1 (wrong options 1 and 3) — The feedback says "Mittauksesi näyttävät …", but these are simulation numbers. The rule is to call them model values, as the correct option and pred-2 already do ("Mallin arvot …"). — Write "Mallin arvot näyttävät …".
- lesson.md:116 — The text says "$\rho g h$ on hydrostaattinen paine eli ylipaine $\Delta p = p - p_0$", but $p_0$ is defined there as the pressure on the surface. The glossary defines ylipaine against the surrounding air pressure, so the two are equal only when $p_0$ is the air pressure. — Add "kun pinnalla on ilmanpaine".
- lesson.md Kaava (line 112–116) — The conditions of $p = p_0 + \rho g h$ (liquid at rest, constant density) are stated in the derivation, the example and the sim's model box, but not next to the formula itself. — Add "levossa olevassa nesteessä, jonka tiheys on vakio".
- lessons/FY3/fy3-4/lesson-answers.py — The file computes only the retrieval item. The numbers of pred-1/2, exp-1 (9,81 kPa/m), siirto (0,757 m), check-2 (890 kg/m³), the worked example and the exit ticket are not computed there, although CLAUDE.md says this file holds the inquiry's and the lesson's numbers. — Add them.

## Checked
- Recomputed every number in one script with my own formulas; all agree: 300 kPa, 294 ≈ 290 kPa, 117 720 / 218 720 Pa, 1765,8 N, 150,1 / 199,1 kPa, 121,6 / 222,6 kPa (+12 %), 9,80 kPa/m, 0,757 m, 10,3 m, 891,9 kg/m³, 2179, 0,892, 29,4 kPa, 1,77 N, 49 kPa. Every numeric mistake value and the sim readouts (node, toFixed) match.
- Hydrostatic derivation from the column weight ($G = \rho A h g$, area cancels): correct, inside FY3 scope (force as a scalar, $G = mg$).
- Isotropy argument, perpendicular force, dam (air pressure on both sides, overpressure grows linearly), barometer (vacuum above the column), eardrum explain: physically right.
- Every choice item (pr-paino, pred-1/2/3, virhe, check-1, check-c2) has exactly one correct option; each distractor is really wrong and its feedback says why.
- exp-1 locks ρ and varies h; exp-2 locks h = 10 m and varies ρ; 1240, 720 and 1025 are reachable with step 5. `simState` has `pOver` and `pTotal` in kPa.
- sim.js implements $p = p_0 + \rho g h$ with $p_0 = 101\,\text{kPa}$ and $g = 9{,}81\,\text{m/s}^2$. Its limits (fixed $p_0$, incompressible liquid at rest, model values) are stated. Arrows drawn on all sides avoid the "pressure acts downwards" picture. The 1280 px capture is correct.
- pressure-depth figure checked to scale: 101 kPa at 0 m and 199 kPa at 10 m, within 1 px. The contact areas in pressure-area are in the ratio 1 : 3, as the caption says.
- The formula section's name matches its laws.
- Hash identical at start and end.
