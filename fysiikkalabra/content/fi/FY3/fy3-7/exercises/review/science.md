VERDICT: FAIL
CONTENT-HASH: bdc0541fa16d2777

## Blocking
- exercises/exercises.json (fy3-7-L2-09) + solutions.md "Kuvaajan lukeminen" — A (assessment): the start temperature $-16\,{}^\circ\text{C}$ is not on a grid crossing, as the solution claims. In `fy3-7/melting-curve` the T grid is 10 °C, the axis starts at an unlabelled −20 °C, and the first point sits between the −20 and −10 lines (shot L2-12). Reading it as −15 or −17 °C gives $c = 2222$ or $1961\,\text{J/(kg·K)}$, 6–7 % off, while the tolerance is 0,03 (2021–2146). The answer hangs on a value the figure does not let the student read. — Fix (keeps the figure, which L1-05 also uses): give the start temperature in the task text ("Jään alkulämpötila on $-16\,{}^\circ\text{C}$") and keep reading only $Q = 20\,\text{kJ}$ from the figure, or widen the tolerance to what a reading of ±1 °C allows (about 0,07). Correct "ruudukon risteyksestä" in the solution either way.

## Polish
- exercises/exercises.json (fy3-7-L1-09) — "sitoo ihosta": the model assumes that all the heat of evaporation comes from the skin (part comes from the air and from the ethanol's own cooling). B-type, mild at this level; optional "Oleta, että kaikki lämpö tulee ihosta."

## Checked
- MAFY value verified on mafytaulukot.fi (*Aineiden olomuodon muutokset*): etanoli $r = 840\,\text{kJ/kg}$ at its boiling point 78,4 °C, as the solution uses.
- L1-09 recomputed: $Q = rm = 840\,\text{kJ/kg} \cdot 0{,}0050\,\text{kg} = 4{,}2\,\text{kJ}$; answers.py agrees; with 855 kJ/kg 4,3 kJ, inside tolerance 0,04.
- L1-09 solution notes rightly that the table value holds at the boiling point and is somewhat larger at skin temperature; g → kg conversion shown; comparison with water (11 kJ) a real check.
- L2-09 recomputed with the figure's own data: $c = 20\,000\,\text{J} / (0{,}60\,\text{kg} \cdot 16\,\text{K}) = 2083\,\text{J/(kg·K)}$; answers.py agrees; physics ($Q = cm\Delta T$ only on the rising part, no melting) right.
- Figure code: (0; −16), (20; 0), (220; 0), (300; 31,9) consistent with $c_\text{jää} \approx 2100$, $s \approx 333\,\text{kJ/kg}$, $c_\text{vesi} \approx 4180$ for 0,60 kg; description lists −16 °C, so only sighted readers lack the value.
- Both within FY3 (latent heat, heating curve).
- Rest of the set unchanged since PASS; hash same at start and end.
