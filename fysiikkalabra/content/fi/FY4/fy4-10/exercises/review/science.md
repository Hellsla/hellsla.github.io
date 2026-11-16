VERDICT: PASS
CONTENT-HASH: 21ead76999d37875
SCOPE: delta added-exercise from daa17f1403857258 base abdc9e095e4f
## Blocking

## Polish
- exercises.json fy4-10-L2-10 and solutions.md — the source date reads 16.11.2026, while this review ran on 15.11.2026. Fix: confirm the reading date before publication.
- solutions.md fy4-10-L2-10 c) — the rounding note explains $-0{,}26$ only for elasticity $0\,\%$. Fix: add that at $50\,\%$ the exact velocities $-0{,}6875$ and $0{,}0625\,\text{m/s}$ also give $-0{,}25\,\text{kg}\cdot\text{m/s}$.
- solutions.md fy4-10-L2-10 b) — the simulation also shows each ball's momentum ($-0{,}63$ and $0{,}38\,\text{kg}\cdot\text{m/s}$ at $100\,\%$); naming them would complete "vertaa simulaation näyttämiin arvoihin".

## Checked
- Only fy4-10-L2-10 judged (added exercise); the other tasks are as passed.
- Source: screen Tutki 1D, the controls Arvot, Liike-energia, Lisää tietoja, Seinä and Elastisuus, the default values ($0{,}50\,\text{kg}$, $1{,}00\,\text{m/s}$; $1{,}50\,\text{kg}$, $-0{,}50\,\text{m/s}$) and the shown results at $100\,\%$, $50\,\%$ and $0\,\%$ agree with the coordinator's record of version 1.1.25.
- Recomputed with my own model (coefficient of restitution 1, 0,5 and 0): velocities $-1{,}25$ and $0{,}25$; $-0{,}6875$ and $0{,}0625$; $-0{,}125\,\text{m/s}$; momentum $-0{,}25\,\text{kg}\cdot\text{m/s}$ in each; kinetic energy $0{,}4375$, $0{,}1211$ and $0{,}0156\,\text{J}$. The solution's values from the shown two-decimal velocities ($0{,}1217$ and $0{,}0169\,\text{J}$; $-0{,}255$ and $-0{,}26\,\text{kg}\cdot\text{m/s}$) follow, and the difference is explained as display rounding.
- Losses $72\,\%$ and $96\,\%$; momentum changes $\mp 1{,}125\,\text{kg}\cdot\text{m/s}$ at $100\,\%$: correct.
- The answer depends on the student's values: the solution says so, gives the method, then a dated example with the defaults.
- Conditions stated: no friction, Seinä off, so no external force along the track; the simulation is called a model.
- d) Newton III, equal and opposite impulses, momentum a vector, kinetic energy a scalar; kinetic energy becomes internal energy and sound (never "lämmöksi"); total energy conserved.
- Terms kimmoisa and täysin kimmoton törmäys as in the chapter; "elastisuus" only as the control's name.
- Hash 21ead76999d37875 at the start and at the end.
