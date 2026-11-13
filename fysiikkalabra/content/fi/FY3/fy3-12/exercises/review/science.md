VERDICT: PASS
CONTENT-HASH: bce692fc39b201a9

## Blocking

## Polish
- exercises/exercises.json (fy3-12-L2-09, text) and solutions.md (fy3-12-L2-09, Periaate) — multiplying $102\,\text{W/m}^2$ by the whole surface area is exact because the figure's values are means over the whole sphere (only the day side is lit). The task says only "neliömetriä kohti ilmakehän ylärajalla", and "Tehon jakautuminen on tasaista keskiarvoa" is vague. Write "keskimäärin koko maapallon pintaa kohti" in the task (as L2-04 says "keskimäärin") and in the principle "teho on keskiarvo koko maapallon pintaa kohti, joten kokonaisteho on keskiarvo kertaa ala".
- lessons/FY3/fy3-12/answers.py:281 — the comment "# Added exercises (teacher 2026-11-12 …)" appears twice (lines 281 and 283); keep one.

## Checked
- All 19 numeric answers recomputed in one script with my own formulas (P = UAΔT with parallel parts, E = Pt, Q = cmΔT, albedo balance, the two-layer model); every one agrees with answers.py and the stored answer, and the stored 2–3 figure values stay inside their tolerances.
- L2-09 (new two-step form): $102 \cdot 5{,}1 \cdot 10^{14}\,\text{W} = 5{,}20 \cdot 10^{16}\,\text{W} = 52\,\text{PW}$, 30 % of the incoming $174\,\text{PW}$; reading from the figure (the reflected arrow is labelled), conversion and check are right; two figures from $5{,}1 \cdot 10^{14}$.
- L3-03: "lämpökerroin" is now defined in the task (kWh of heat per kWh of electricity), not called an efficiency, as the guardrails ask; $W = (U_1 - U_2)A\Delta T\,t/\varepsilon = 2755/2{,}8 = 984\,\text{kWh}$; the model answer says the pump moves heat and does not create it; the direct-electric comparison ($\varepsilon = 1$) is right.
- L1-09: MAFY pine $\lambda = 0{,}14\,\text{W/(m·K)}$ (docs/mafy-arvot.tsv VERIFIED); $U = \lambda/d$ is given in the task, as it is not in the lesson.
- L3-05: both balances give $S = 239/(1 - f/2) = 398\,\text{W/m}^2$; the interpolation gives 16,3 °C, and Stefan–Boltzmann gives 16,4 °C, so the example table is consistent; model limits named.
- L2-07: the least-squares line through the origin gives $U = 0{,}350$ and the origin is justified physically.
- Choices L1-06, L1-07, L1-08: exactly one correct option each, every distractor really wrong and its feedback right; L2-08 order (60, 216, 288, 459 W) correct.
- Figure earth-flows: 341 and 102 labelled, the asked arrow a "?"; the description gives the same values and not 239.
- Hash same at start and end.
