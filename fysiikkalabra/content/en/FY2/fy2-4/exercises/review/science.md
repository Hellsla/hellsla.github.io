VERDICT: PASS
CONTENT-HASH: 1d2e344571e5d8dc
SCOPE: delta md-paragraphs,numbers,reflow,teacher-figure,typography,wording from 0742e66b95ebc481 base b5600a6

## Blocking

## Polish
- content/en/FY2/fy2-4/exercises/solutions.md:144 (fy2-4-L1-07) — the Formula line was left in Finnish: "Energian säilyminen … josta". — Write "Conservation of energy $E_\text{o} = E_\text{a} + E_\text{h}$, so $E_\text{h} = E_\text{o} - E_\text{a}$". This is a translation fix; the physics is right. The language owner should fix it before publication.
- content/en/FY2/fy2-4/exercises/solutions.md:154 (fy2-4-L1-08) — the same problem: "Hyötysuhteen määritelmä … josta". — Write "Definition of efficiency $\eta = P_\text{a}/P_\text{o}$, so $P_\text{o} = P_\text{a}/\eta$".

## Checked
- I ran the hash `--exercises --lang en` at the start and at the end. Both times it was 1d2e344571e5d8dc.
- I recomputed all 20 numeric answers with my own formulas: 85 %, 30 %, 3.0 W, 2000 J, 4.0 kJ, 9.0 kJ, 200 kW, 78.8 %, 96 kJ, 54 W, 0.228 kWh, 45 kW, 4.29, 79.2 %, 25 %, 1.5, 2083 s, 180 J, 3.14 and 6.89 kWh. All of them agree with answers.py and exercises.json within tolerance.
- The rewritten Formula lines start from the definition $\eta = E_\text{a}/E_\text{o}$ (or with powers), from conservation $E_\text{o} = E_\text{a} + E_\text{h}$ and from $E = Pt$. Each derivation is algebraically right and is solved symbolically before substitution.
- L1-02: the step $\eta = P_\text{a}t/(P_\text{o}t) = P_\text{a}/P_\text{o}$ states its condition, constant power.
- L3-01: device B's useful energy is found from conservation and then put into the definition. This is correct.
- L3-05 (error analysis): the heat share is the same on every row, $1510/2160 = 0.70$, so scaling it to a year is justified. The efficiency is $650/2160 = 30\,\%$.
- L3-04: $E_\text{p} = Vh$ with $32\,\text{MJ/l}$ gives 53.3 kWh, and the ratio is $53.3/17 = 3.1$. The limits of the model (production losses not included) are still stated.
- fy2-4/grid (teacher-approved picture): 8, 2 and 6 squares with $\eta = 0.25$ in figures.py. L3-03 reads $6/8 \cdot 240\,\text{J} = 180\,\text{J}$, and L2-09 gives 25 %.
- The diff introduces no guardrail break (A or B). Efficiency stays at most 100 %, and only one device's efficiency is treated, which is within FY2 scope.
