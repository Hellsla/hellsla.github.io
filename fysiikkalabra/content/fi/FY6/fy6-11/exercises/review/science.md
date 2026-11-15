VERDICT: FAIL
CONTENT-HASH: 89113b856cde041c

## Blocking
- solutions.md:109 — L3-01 (A, rounding reason against P7 b): the answer "$3{,}4 \cdot 10^{2}\,\text{V}$, pyöristettynä kahteen merkitsevään numeroon jännitteen $450\,\text{V}$ tarkkuuden mukaan" treats $450\,\text{V}$ as two figures. Under the teacher's rule, trailing zeros are significant, so $450\,\text{V}$ has three, and the counts $3e$, $4e$ are exact — fix: answer $338\,\text{V}$ ($337{,}5\,\text{V}$), three figures as in $450\,\text{V}$.
- solutions.md:119 — L3-02 (A, P7 b): "$4200\,\text{km/s}$ … kaksi merkitsevää numeroa" reads as four figures — fix: $4{,}2 \cdot 10^{3}\,\text{km/s}$ eli $4{,}2 \cdot 10^{6}\,\text{m/s}$.

## Polish
- solutions.md:18 — L1-02: "$1{,}0 \cdot 10^{2}\,\mu\text{N}$ eli $100\,\mu\text{N}$, kaksi merkitsevää numeroa": the second form reads as three figures under P7 (b). You could drop "eli $100\,\mu\text{N}$" or write "eli $0{,}10\,\text{mN}$".
- solutions.md:208 — L3-04: the answer $1{,}60 \cdot 10^{-19}\,\text{C}$ (three figures) comes from masses with two figures, and no rounding reason is given. You could add one sentence: "kolme merkitsevää numeroa, koska keskiarvo viidestä tuloksesta" — or round to $1{,}6 \cdot 10^{-19}\,\text{C}$ as the data allow.

## Checked
- I recomputed all 17 numeric answers in one script with my own formulas (E = F/q, F = qE, E = U/d, F/G, v = √(2eU/m), q = mg·tanα/E, q = mgd/U with integer multiples, y = ½a(L/v₀)²). All agree with answers.py and exercises.json; my own counts are n = 2, 3, 1, 4, 3, giving $e = 1{,}602 \cdot 10^{-19}\,\text{C}$.
- L2-05: the products $E \cdot d$ are 408, 393, 408, 390, 408 and 393,6 V; sum 2400,6 V, mean 400,1 V.
- L2-07: the deviations are 0,7; 1,2; 2,0; 3,7 and 45,2 %, so the uniform points are x = 0–6 cm; their mean field is $2{,}98 \cdot 10^{4}\,\text{V/m}$ against $U : d = 3{,}0 \cdot 10^{4}\,\text{V/m}$.
- L3-05: $y = 1{,}67\,\text{mm}$, which is less than $2{,}5\,\text{mm}$. At double the voltage the drop hits the plate at $x = 8{,}7\,\text{mm}$. The electric force is 1360 times the weight ("noin 1400" is fine).
- P7 (b) elsewhere: 600 V (three figures, not named as limiting), and 70 mV, 20-kertainen, 50 V and 15 kV (two figures) are justified correctly.
- L1-09: the maximum voltage $7{,}5\,\text{kV}$ is exact from 3,0 kV/mm · 2,5 mm, so P7 (c) needs no rounding.
- L1-05: the fitted line (30 µN/nC) reaches the grid crossing (4,0 nC; 120 µN). The figure data and the description agree, and the figure does not reveal the slope.
- L2-08 force diagrams: object = the grain; interactions = Earth and the field only (vacuum). B shows G and F_s both down with F_s ≈ 2·G, matching $2{,}0 \cdot 10^{-11}\,\text{N}$ and $9{,}8 \cdot 10^{-12}\,\text{N}$. Each `wrong=` figure carries only its one intended error (F_s along E; v drawn as a force; G left out).
- L1-06, L1-07: exactly one correct option, and every distractor's feedback is right physics.
- L3-03 equilibrium uses components of the tension, not a double count. Scope (Coulomb's law and the uniform field) and notation ($\overline{E}$, $\overline{F}_\text{s}$, E = U : d) match the brief.
