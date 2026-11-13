VERDICT: PASS
CONTENT-HASH: 2d86ef406e58a1c7
SCOPE: delta added-exercise from bf811b5954b48e62 base 89bcb63b7431

## Blocking

## Polish
- exercises/solutions.md (fy3-7-L2-09, Kuvaajan lukeminen) — "(alkupiste on origossa, $0\,\text{kJ}$)": the start point is $(0\,\text{kJ};\ -16\,{}^\circ\text{C})$, not the origin. Write "alkupisteessä $Q = 0\,\text{kJ}$".
- exercises/solutions.md (fy3-7-L2-09, Vastaus) — the reason for "hyväksytään $2020\ldots2150$" is that the heat is read from a grid crossing, but an exact crossing gives no reading spread. The range is in fact the 3 % tolerance. Say so, or drop the range.
- exercises/exercises.json (fy3-7-L1-09) — as in round 1: "sitoo ihosta" assumes that all the heat of evaporation comes from the skin. Optional: "Oleta, että kaikki lämpö tulee ihosta."

## Checked
- Round-1 blocker fixed: the start temperature $-16\,{}^\circ\text{C}$ is now in the task text, and the student reads only $Q = 20\,\text{kJ}$ at the crossing $(20\,\text{kJ};\ 0\,{}^\circ\text{C})$ of the 20 kJ / 10 °C grid.
- L2-09 recomputed: $c = Q/(m\Delta T) = 20\,000\,\text{J}/(0{,}60\,\text{kg} \cdot 16\,\text{K}) = 2083\,\text{J/(kg·K)}$, which matches answers.py. Tolerance 0,03 (2021–2146) accepts $2{,}1 \cdot 10^3$.
- L2-09 physics: $Q = cm\Delta T$ is used only on the rising part, before any melting. The solution is complete (symbols first, kJ → J, two figures from 0,60 kg), and the check against $c_\text{vesi}$ and the energy balance is real.
- L1-09 unchanged since round 1: $Q = rm = 840\,\text{kJ/kg} \cdot 0{,}0050\,\text{kg} = 4{,}2\,\text{kJ}$, MAFY value as verified then; the remark that the boiling-point value applies is right.
- Figure description lists the same points; it does not name the parts or give $c$ or $s$.
- In FY3 scope; rest of the set unchanged since PASS; hash same at start and end.
