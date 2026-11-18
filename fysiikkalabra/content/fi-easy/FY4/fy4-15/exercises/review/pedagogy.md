VERDICT: PASS
CONTENT-HASH: 775b15e10f821e0e
Mode: full

## Blocking
None.

## Polish
1. solutions.md, fy4-15-L2-08 Mallivastaus: the calculation uses $P = \tfrac12\eta\rho A v^3$ from Periaate with no Kaava step, unlike every other solution, which derives it from $m = \rho A v t$ and $E_\text{k} = \tfrac12 mv^2$. The later sentence on $\tfrac12 v^2$ and $\rho A v$ does the reasoning, but move it before the calculation or add the one-line chain used in L2-07.
2. solutions.md, L2-02 and L3-04 Järkevyys: "teoreettisen ylärajan $59\,\%$" and L1-01 "Imatran $192\,\text{MW}$" are not explained in the exercise; a student who did not meet them does not know what they are. Name the limit (Betzin raja) with one clause or drop the comparison.
3. exercises.json, fy4-15-L2-08 first distractor feedback ends "lukuarvo $10^3$ on $100$ kertaa $10$": unclear. Corrected: "Kun $v = 10\,\text{m/s}$, $v^3 = 1000$ on $100$ kertaa suurempi kuin $v = 10$, joten oikea teho on noin $100$ kertaa tämä tulos."
4. "esimerkkiaineisto" or "esimerkkiarvot" in task text (L2-05, L2-06, L2-08, L3-04, L3-05): cut per the 2026-11-13 rule on provenance; keep tables and captions.
5. solutions.md, fy4-15-L1-09 Vastaus gives $1100\,\text{kW}$ while the box answer is 1117 kW; add "(tarkemmin $1117\,\text{kW}$)" so a student entering 1117 sees a match.

## Checked
- Opened exercises.json and solutions.md whole (9 + 10 + 5 tasks; counts met) and the five-point table in L2-05 and L3-04; the figure description of tehokayra-pisteet (via figcat) for the values 511, 1017, 1285, 1637 and 144 kW.
- Recomputed all answers: 15,89 MW; 235 kJ; 92 %; 480 kW; 18 MWh; 2,92 MW; 180 kJ; 1117 kW (rho 1,29); 96,5 m³/s; 44,9 %; 40,7 kW; 5,73 MWh; 5,48 GWh; 18,8 GWh (4,3-fold May to August); 242 kW; 1,96 MW; 61,3 MWh; 1,61 vs 2,37; 3,375; 3,90; 5,10 m; 40 % (mean P/v³ 1,252); 1,04·10⁶ m³ (240 MWh, 6,0 h). All match.
- Every Kaava starts from $E_\text{p} = mgh$, $m = \rho Q t$, or $m = \rho A v t$ and $E_\text{k}$, and ends in the working formula; the ratio tasks (L3-01, L3-02) cancel symbols before substituting.
- L2-07 error analysis: the unit check ($\text{kg/s}$ is not W) shows the missing $v^2$; the factor 49 closes the check.
- L2-08 distractors each map to a named slip (v, v², unconverted km/h) and the numbers agree (20 kW, 196 kW, 91,6 MW).
- L3-04 and L3-05 are multi-part with a model answer for each part (verbal parts included): applicability limit at nominal power; why pumped storage suits wind.
- Level mix: L1 one step or lookup, L2 conversions, tables, graph reading, L3 scaling reasoning, model testing, storage; none repeats the worked example (120 m rotor, 9,0 m/s).
- Finnish and case after number+unit correct; MAFY lookup task names the table.
- Captures not opened: text and formula order only.
- Hash the same at start and end.

## Scores
Level fit 5/5. Task clarity 4/5. Solution completeness 4/5. Finnish 4/5. Feedback quality 4/5.
