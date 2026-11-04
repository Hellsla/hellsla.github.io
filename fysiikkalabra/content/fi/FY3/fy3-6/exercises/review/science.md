VERDICT: PASS
CONTENT-HASH: 9d41b59b9d2f10be

## Blocking

## Polish
- solutions.md:126 (L2-05 Järkevyys) — "neste vastaanottaa 30 378 J" from 30 000 J supplied, "joten häviöt ovat pienet": energy received cannot exceed energy supplied, so the 1 % gap is scatter from the example data or the drawn line. It does not measure losses. — Say "ero on mittaushajonnan suuruinen, joten häviöt ovat tällä välillä pienet". Line 125 b) "poikkeaa vain noin 2 %" should be about 1 % (4138 compared with 4190).
- exercises.json:254 / solutions.md:190 (L3-04) — the check uses room temperature 20,0 °C, which the task never states (it only follows from the start reading). — Add "Huoneen lämpötila on 20 °C" to the task.
- solutions.md:203 (L3-05) — "kolme merkitsevää numeroa …, tulos pyöristettynä kahteen" gives no reason for using two. — Say that k varies between intervals by about ±3 %, so the second digit is the last meaningful one. "pienet erot johtuvat pyöristyksestä" would be clearer as "lukemien 0,1 °C:n tarkkuudesta".
- solutions.md:137 (L2-06) — "Öljyn c jää veden arvoa pienemmäksi, kuten nesteiden vertailussa pitääkin" states no reason. — Use "vedellä on tavallisista nesteistä suurin c" or drop the sentence.
- exercises.json:217 (L2-07) — the setup (hot metal into water, equilibrium temperature) is the same as L2-04 and the lesson example. The error-analysis part a) is what makes it new. — Optionally change the context (for example a hot iron nail into tea) so it reads as less of a repeat.

## Checked
- I recomputed all 19 answers in one script (my own formulas from the task text). They agree with answers.py and exercises.json within rounding.
- L2-05: the end-point line (0 s; 20,0) to (300 s; 34,5) passes the table rows, and a least-squares fit gives c = 4118 J/(kg·K). Both are within the 3 % tolerance of 4100.
- L2-06: steady increments (A 4,4–4,6 K, B 2,0–2,5 K per 30 s), c_oil = 2083 J/(kg·K). This is realistic for oil.
- L3-04: the data match Newton-type losses with k ≈ 2 W/K (simulated series 25,6 … 63,6 °C). The loss power is 81 W, and the a)/c) reasoning holds.
- L3-05: k is 0,599, 0,587, 0,612, 0,582, 0,614 and 0,590 W/K. The data match τ ≈ 35 min, so the conclusion "malli sopii" is right.
- L1-06 MC: exactly one correct option, and each distractor's feedback is right. L1-07 (78 K) and L1-08 (C = 540 J/K, 32 kJ) are correct.
- Q = cmΔT is used only where there is no change of state. L3-04 b) states that heating is linear only while losses are small (guardrail).
- Notation (c, m, ΔT, C = cm, T_loppu/T_alku) matches the lesson. The levels match the plan in docs/exercise-bank/FY3.md (heating curve → c, two curves → which is water, heat-loss reduction, curving curve, cooling model).
- L3-04 and L3-05 render at 1280 px without overflow (aligned equations fit).
- The figure and the wording of the existing tasks are unchanged.
