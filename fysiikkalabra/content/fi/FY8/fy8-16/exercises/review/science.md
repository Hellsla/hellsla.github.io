VERDICT: FAIL
CONTENT-HASH: f6246ca290795a6d
Mode: delta (new tasks L2-09 and L3-06 on figure fy8-16/hubble-t; "(esimerkkiaineisto)" removed from two table captions)

## Blocking
- solutions.md:315 (fy8-16-L3-06 c, second paragraph; same in en and fi-easy) — **A**: "esimerkiksi $z = 3{,}00$ antaisi $v = 3{,}00\,c$, mikä on mahdoton galaksin nopeudeksi". The answer rests on the claim that a recession speed above $c$ is impossible. That is wrong in cosmology. At $z = 3$ the real recession speed (distance growth rate) is above $c$, and that does not break relativity, because space itself expands, which is exactly what the brief's lesson teaches ("avaruus itse laajenee"). Students are left thinking "$v > c$ is impossible, so the formula fails". The real reason is that $v = cz$ is a small-$z$ approximation, and at large $z$ the link between $z$ and speed depends on the expansion history. — Fix: as in L3-05 b, say that $v = cz$ is only the small-$z$ approximation the lesson gives ($z < 0{,}1$), so for $z \gg 0{,}1$ the result cannot be taken as the galaxy's speed: the formula no longer holds there, and the true relation is not linear. If the $3{,}00\,c$ example stays, call it a sign that the approximation has broken down, and drop "mahdoton galaksin nopeudeksi".
- solutions.md:312 (fy8-16-L3-06 Vastaus; en, fi-easy) — **A** (internal inconsistency in the rounding reason): the answer is $4{,}2 \cdot 10^{2}\,\text{Mpc}$ (two figures), but the next sentence says "Kolme merkitsevää numeroa". The limiting datum is $0{,}10\,c$ (two figures), so two figures is right. — Fix: "Kaksi merkitsevää numeroa kuten rajassa $0{,}10$; $H_0 = 72{,}0$ kolmella numerolla". Keep "noin $416\,\text{Mpc}$" only as an unrounded value, or drop it.

## Polish
- none

## Checked
- I recomputed both answers in my own script: L2-09 gives $z = 0{,}035253$, $v = 10\,569\,\text{km/s}$ and $d = 146{,}79\,\text{Mpc}$, the same as answers.py. L3-06 gives $d = 0{,}10c/H_0 = 416{,}39\,\text{Mpc}$, also the same. Both tolerances are 2 %. Rounding L2-09 to three figures and L3-06 to two keeps the student inside the tolerance.
- The figure's line uses lesson-answers `t2-H0` $= 18000/250 = 72$, the same value the solutions read. A least-squares fit through the origin of the nine T2 points gives $72{,}4$, so the drawn line is a fair fit. Reading it at the grid point is right, and the figure gives away neither answer.
- L2-09: $z = 0{,}035$ is under $0{,}1$, so $v = cz$ is valid. Its 147 Mpc sits between the points at 120 and 160 Mpc, whose speeds (8300 and 11 900 km/s) bracket $v$. Three figures follow from $\Delta\lambda = 15{,}3\,\text{nm}$. The solution goes symbolic first: $d = cz/H_0$.
- L3-06 c, first part: the extrapolation is stated (285 Mpc to 416 Mpc, $\times 1{,}46$), and so is its unproven assumption, which follows the guardrail on extrapolation. The top of the axis, 21 000 km/s, corresponds to $z = 0{,}070$.
- The task texts state the $z < 0{,}10$ condition, $c$, the axis end and the farthest point. Both tasks stay inside the FY8 scope and use the brief's notation.
- Removing "(esimerkkiaineisto)" from the captions follows the house rule (no provenance badge on example data). No physics changed.
- en and fi-easy carry the same numbers. The two findings above are present in all three languages.
- Hash at start and end: f6246ca290795a6d.
