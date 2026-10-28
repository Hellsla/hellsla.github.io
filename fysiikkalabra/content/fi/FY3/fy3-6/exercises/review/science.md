VERDICT: PASS
CONTENT-HASH: 13bc0d2daf5f4e53

## Blocking

## Polish
- exercises.json:90 — "2000 m²" is plain text while every other value with a unit is inline LaTeX — write `$2000\,\text{m}^2$`.
- exercises.json:98 — "1,0 m³" is plain text — write `$1{,}0\,\text{m}^3$`.
- solutions.md:49 — the comparison with "nestemäistä vettä" over the same −22 → −4 °C interval is a hypothetical a student may find odd (water is not liquid there) — say "saman lämpötilan muutoksen tekeminen samalle massalle vettä (nesteenä)" or compare c directly.

## Checked
- All 12 answers recomputed with my own formulas from the task texts (Q = cmΔT, energy balance, Pt = cmΔT, column per m², equal C = cm); all agree with answers.py and exercises.json to rounding.
- Significant figures: every answer has two, set by the limiting datum named in its solution; a student rounding to two figures stays inside the 2 % tolerance (L2-03 53,75 → 54, L1-04 −35,2 → −35).
- Q = cmΔT condition (no change of state) is stated or met in every task: L1-05 ice stays below 0 °C, L2-03 no boiling, L3-01 evaporation excluded in the task.
- Sign conventions match the brief's lesson: L1-04 signed Q < 0; L1-02 heat released given as positive with $T_\text{alku} - T_\text{loppu}$.
- Equilibrium tasks (L2-01, L2-04, L3-01) use the lesson's $c_1 m_1 (T_1 - T) = c_2 m_2 (T - T_2)$; L3-01 justifies the stones' final temperature 40 °C as asked.
- Celsius substitution in the weighted mean is justified correctly (shift of scale shifts the result equally).
- Reasonableness checks are real checks: L2-01 energy balance 160·17,4 = 40·69,6; L3-01 ratio 5,24/8,67 ≈ 0,60; L3-03 ratio 5,2/1,6 ≈ 3,3; L2-04 heat capacity ratio 7,45.
- Data realistic: c values from the lesson table, sand 1600 kg/m³, 18 MJ/m² daily absorbed solar energy, kettle 2,4 kW.
- All physics inside FY3 scope; notation as in the lesson.
- Hash identical at start and end.
