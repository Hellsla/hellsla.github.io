VERDICT: PASS
CONTENT-HASH: f7ecbe4706b0713d
SCOPE: delta: new tasks fy9-sahkokentta-s7 and -s8 and the changed intro; older tasks s1–s6 untouched

## Blocking
None.

## Polish
- s7: the text never gives the plate gap, and the figure does not mark the positive plate. Part d and the a-solution's check ("over the whole gap 250 V : 0.050 m") rely on the positive plate being at $x = 5.0\,\text{cm}$, $V = 250\,\text{V}$, which a student can only infer from where the line ends. Adding "the plates are $5.0\,\text{cm}$ apart" would remove the guess.
- s7 a, Reasonableness: the comparison with the breakdown field of air does not fit, because the plates are in a vacuum.
- s8 c: the drawn curve gives $U_\text{D}(30\,\text{mA}) \approx 2.25\,\text{V}$ and so $R_\text{min} \approx 125\,\Omega$. This is inside the tolerance and still rounds up to $130\,\Omega$, but it could be listed under the accepted alternatives.
- The shared `graph_read` key's base text talks about a slope from two far-apart points, while s7 c and s8 a/d read single values. The `detail` sets this right.

## Checked
- I ran `units.py hash --lang en` at the start and the end (f7ecbe4706b0713d, unchanged). The packet's checks say `practice.py check: OK`.
- I read the English intro, s7 and s8 in tasks.json and their solutions in the en packet. I compared them line by line with fi: every given value, read value, intermediate, answer, unit, tolerance, point and rubric criterion is the same. Decimal points are used throughout. The physics wording is faithful: "uniform field", "internal energy" (never heat), "series resistor", "characteristic curve" and "energy principle" are all correct.
- My own recomputation (scratchpad `s78.py`, shared with fi) matches every number: E = 5.0 kV/m, a = 2.41e11 m/s², v = 98.2 km/s, V = −50 V; I = 17.27 mA, P_R = 65.6 mW, 63.3 %, R_min = 126.7 Ω, 440 Ω and 110 Ω. It also confirms against the drawn LED curve: self-consistent I = 17.15 mA, U_D = 2.165 and 2.235 V at 5 and 20 mA.
- Directions are right: the field points against x, and the alpha particle accelerates towards the negative plate. Rounding is to the safe side in c. The "Ohm's law" conclusion is correctly limited to a straight line through the origin.
- The intro's topic list ("electrical safety", "semiconductors") fits the set. Unit fields are language-neutral. Scope is FY6/FY4 only.
