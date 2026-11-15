VERDICT: PASS
CONTENT-HASH: 52fabbb87f61e010

## Blocking

## Polish
- exercises/exercises.json:48 (L1-06) — "Kuviossa viivat ovat…" but the task has no `figure`; the text alone carries the information, so the task works — write "Ajatellaan kuviota, jossa…" or attach a field-line figure.
- exercises/solutions.md:208 (L3-04) — the estimate $1{,}60 \cdot 10^{-19}\,\text{C}$ is asked in b) but the Vastaus labels it "c)" — label b) and c) separately.
- exercises/exercises.json:377 (L3-05) — "Kenttä poikkeuttaa pisaraa sivuun" with horizontal plates: the deflection is vertical, toward a plate — write "kohti toista levyä".

## Checked
- All 19 numeric answers recomputed independently in one script (E = F/q, F = qE, E = U/d, qU/d = mg, v = √(2eU/m), q = mg tanα/E, Millikan q = mgd/U, y = ½(qE/m)(L/v₀)²): every one agrees with exercises.json and answers.py; L1-05 by my least-squares slope through the origin $2{,}99 \cdot 10^{4}\,\text{N/C}$ (−0,2 %).
- L3-04: charges $3{,}20;\ 4{,}84;\ 1{,}59;\ 6{,}38;\ 4{,}83 \cdot 10^{-19}\,\text{C}$, $n = 2, 3, 1, 4, 3$, ratios $1{,}60$–$1{,}61$, mean $1{,}602 \cdot 10^{-19}\,\text{C}$; sign negative from the upper positive plate — correct.
- L3-05: $F/G \approx 1360$, $a = 1{,}33 \cdot 10^{4}\,\text{m/s}^2$, $t = 0{,}50\,\text{ms}$, $y = 1{,}67\,\text{mm} < 2{,}5\,\text{mm}$; doubled voltage hits at $4{,}3 \cdot 10^{-4}\,\text{s}$ after $8{,}7\,\text{mm} < 10\,\text{mm}$ — all right; air resistance neglect stated.
- L2-05 products $E d$ 408/393/408/390/408/394 V, mean 400 V; L2-07 deviations 0,7/1,2/2,0/3,7/45 %, mean $2{,}98 \cdot 10^{4}\,\text{V/m}$; the edge fall-off (≈4 % one gap inside the edge, ≈half at the edge) is physically plausible.
- L2-08 force diagrams: B (G and $\overline{F}_\text{s}$ both down, $F_\text{s}/G = 2{,}04$, arrows 2 : 1, acceleration down) is the only right one; A (force along E), C (velocity drawn into the diagram, otherwise correct) and D (weight omitted) each carry exactly the one error their feedback names.
- L1-06, L1-07: exactly one correct option; every distractor's feedback is right (density = strength, lines are not charges, $\overline{F} = q\overline{E}$ against E for negative q, uniform field still exerts a force).
- Conditions stated where used: uniform field only between wide plates away from the edges (L2-04, L2-06), vacuum for the electron and dust grain, weight negligible only when shown (L3-05 a, L2-08 D).
- Significant figures per P7: 450 V three figures → 338 V (L3-01); 600 V three, limited by 0,040 m (L1-03); L1-09 limit 7,5 kV exact, no rounding direction needed.
- Magnitudes realistic (membrane 70 mV, air breakdown 3 kV/mm, fields below breakdown, Millikan masses ~10⁻¹⁵ kg, electron 1,4 % of c); scope inside FY6 and prerequisites (FY4 kinematics in level 3).
- Hash identical at start and end.
