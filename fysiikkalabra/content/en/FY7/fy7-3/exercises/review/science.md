VERDICT: PASS
CONTENT-HASH: b21795c385640322

## Blocking

## Polish
- exercises.json fy7-3-L2-09 — `"answer": 497.36` has more digits than the slope read from the graph (2 s.f.) justifies, and the solution gives $5.0 \cdot 10^2$. The figure's own fit ($k = 2.465\,\text{mT/A}$) gives $N = 490$, which is still inside the 4 % tolerance. Fix: consider `"answer": 500` (or 497), with the tolerance kept.
- solutions.md fy7-3-L2-05 Reasonableness — "the Earth's field $0.05\,\text{mT}$ is a part of the constant term": only the axial component of the Earth's field enters the reading, so that part is at most $0.05\,\text{mT}$. Fix: "the component of the Earth's field along the sensor is part of the constant term".

## Checked
- I recomputed all 19 numeric answers in one script with my own formulas ($B = \mu_0 I/(2\pi r)$, $B = \mu_0 NI/l$, least-squares fits). All agree with answers.py and exercises.json within tolerance. L1-08 is $314 \to 310$ (1.3 %) and L3-01 is $2.02\,\text{A}$.
- L2-05: the free fit gives $2.512\,\text{mT/A}$ with intercept $0.059\,\text{mT}$, so $\mu_0 = 1.256\,\mu\text{Vs/(Am)}$. The answer 1.26 and the ±4 % window for a fit by eye are fair.
- L3-04: the tangents and their ratios to $I$ match the solution. The fit through the origin gives $16.0\,\mu\text{T}$ (the free fit also gives 16.0). The reasoning for $\tan\alpha \propto I$ and for $\alpha \to 90^\circ$ is correct.
- L3-02: the claim that the field at the centre is 85 % of the long-coil value is verified: $0.8/\sqrt{0.8^2+0.5^2} = 0.848$.
- L3-05: $R = 2.60\,\Omega$, $I = 2.31\,\text{A}$, $N = 318$, $l = 0.175\,\text{m}$ (5.8 diameters), $B = \mu_0 I/d_\text{i} = 5.28\,\text{mT}$. Part d), field halved to $2.6\,\text{mT}$, is correct for a single layer.
- L2-04 (opposite currents: the fields add at the midpoint) and L3-03 (same direction: the zero point is $x = I_1 d/(I_1+I_2)$) are correct. The right-hand-rule reasoning is right.
- Multiple choice: in L1-06 an upward current gives anticlockwise circulation seen from above; in L2-07 the reading is $B\cos 60^\circ = 0.50\,B$; in L2-08 the factor is $3/2$. Each has exactly one correct option, and each distractor's feedback names the actual error.
- Figures: wire-graph-task ($120/r$) gives $60\,\mu\text{T}$ at $2.0\,\text{cm}$, so $6.0\,\text{A}$. coil-fit is readable at $(2.0\,\text{A};\ 5.0\,\text{mT})$ (the line is at 4.97). The alt texts give the grids and do not give the answers away.
- Degree notation (the edit under review): the exercises and solutions write `^\circ` throughout and the table header writes `{}^\circ`. It renders consistently and changes no physics.
- The scope is inside the FY7 contents: the field of a wire and of a coil, and the measurement inside a coil. L3-05 uses $R = \rho L/A$ and $I = U/R$ from FY6, which the scope permits. The model conditions (long wire, long coil, centre of the coil) are stated in the tasks.
- Rounding follows the limiting data; units and magnitudes are realistic (MRI $1.5\,\text{T}$, power line $10\,\mu\text{T}$).
