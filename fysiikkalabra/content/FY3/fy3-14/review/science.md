VERDICT: PASS
CONTENT-HASH: 57ded7224d06dea2

## Blocking
(none)

## Polish
- inquiry.json:johtopaatos model/criteria — uses $\theta_\text{v}$ while lesson.md, the sim and every other activity use $T_\text{v}$ — write $T_\text{v}$.
- sim-spec.md — says "noin 8 s" exponential and "mikä kolmesta tilanteesta"; sim.js has τ = 1,8 s over an 8 s run and four cases (tapaus 1–4) — align the spec with the code.
- lesson.md Esimerkki, Sijoitus — "6,05 °C ≈ 6,0 °C" rounds twice (6,046 → 6,05 → 6,0); write "6,046… °C ≈ 6,0 °C" or just "≈ 6,0 °C".

## Checked
- One Python run recomputed all 12 exercise answers (answers.py matches: 16,7/83,5/25,14/179,6/5,04/13,94/67,7/177,5/333,1/234,0/281,2/−3,50) and every stated answer is within its 2 % tolerance at the data's significant figures.
- Formulas: $Q_\text{v}$, $Q_\text{j}$, all-melts $T$, $m_\text{s}$, and the all-frozen balance (L3-03) derived correctly with their case conditions; FY3 scope (energy conservation, phase change) respected.
- Worked example: 25 140 J vs 17 540 J, T = 6,05 °C; "19 °C without fusion" (19,3), "two thirds" (16,7/25,1) and midpoint 8,0 °C correct; symbolic before substitution.
- Figures: ice/water masses 0,375/0,025 kg and cube areas to scale; bar chart 25,1 / 2,1 + 33,4 = 35,5 kJ at 6 px/kJ; T(T_v) graph kink at 26,6 °C and 40,1 °C at 80 °C on the stated axes.
- Misconception: 15 °C naive vs 24,7 g ice left at 0 °C correct.
- inquiry: ennuste-1 (75,3 g melted, 24,7 g left, 26,6 °C), ennuste-2 (5,9 g vs 18,5 g, Δ 12,6 g, 4,2 vs 33,4 kJ), koe-1 26,6 °C, johtopäätös 62,4 g and 10,1 °C, koe-2 12,6 g, Etsi virhe −25,6 °C / 0,225 kg, siirto 39,9 g with mistakes 43,9 and 438 g, tarkistus-2 40 °C with mistake 56 °C — all reproduced.
- Experiments: koe-1 locks mW, mI, TI0 and varies TW0; koe-2 locks mW, TW0, mI and varies TI0; simState exposes Tf and iceLeftG.
- sim.js: solve() cases 1–4 and Qend per case consistent; stateAt() sequences water cool→freeze→subcool and ice warm→melt→warm so both sides reach Tf; no liquid below 0 °C or ice above it; time course labelled as illustration.
- Exit ticket: 66,8 kJ and 12,5 g melted correct.
- Hash identical at start and end.
