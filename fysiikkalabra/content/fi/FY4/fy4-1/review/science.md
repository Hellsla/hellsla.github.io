VERDICT: PASS
CONTENT-HASH: 07b5c7e5baad7bf7

## Blocking

## Polish
- inquiry.json exp-1, exp-3 solution "Vastaus" — they say the readings are "annettu tässä kahdella numerolla", but the sim readout and table show $40{,}0\,\text{m}$, $30{,}0\,\text{m}$, $10{,}0\,\text{s}$ (one decimal). The model values are exact in any case. Fix: give the reason as "mallin arvot ovat tarkkoja; kaksi numeroa riittää" or similar.
- inquiry.json check-3 criteria line 4 — the criterion asks for "paikka ja siirtymä metreinä", but the prompt's data are in km ($4{,}0\,\text{km}$). Fix: "pituusyksikössä (m tai km)".
- lesson.md:218 vs glossary *keskinopeus* — the lesson writes $v_\text{k}$ and the glossary writes $v_\text{ka}$. Use one symbol (MAFY's).
- lesson.md:351 "kappale voi olla edellä ja liikkua silti hitaammin" — "edellä" has no stated direction (guardrail higher-line-ahead is about graphs, so this is not blocking). Fix: add "positiiviseen suuntaan".
- inquiry.json check-3 model — the cyclist's graph also has a horizontal part (the stop at the shop). The rising part assumes the shop lies in the positive direction. One clause would cover both.

## Checked
- Recomputed every number in one script with my own formulas: example 2,5 m/s and 170 m; exp-1 4,0 m/s; exp-3 −3,0 m/s; pred-3 meeting at 6 s, 12 m; siirto 39 m ($x_0 = -11\,\text{m}$, 18 km/h); check-2 13 m (4,8 s); virhe −3,0 m/s; retrieval 15 / 7,5 / 0,25; round trip 16 m, $v_\text{k} = 0$; exit ticket −8 m. All agree with lesson-answers.py, and every mistake value matches its stated error.
- Robot data: least-squares slope 1,494 m/s, intercept 4,10 m, SE 0,029 m/s. This confirms "1,49 ± 0,03" and the fitted line drawn from 4,10 m to 19,10 m. The residuals scatter on both sides.
- Figures to scale: displacement axis 40 px/m (+6 m, −5 m), jogger graph (20 → 120 → 170 m), robot points and line, cart E graph (8 m, 4/6/10 s).
- sim.js implements $x = x_0 + vt$ for cases 1–3 and case 4 out / stand / back (path 16 m, Δx = 0). Path is |v|t. simState gives `xA` and `x2` for every case, and a 0,5 s slider step reaches 0, 4, 6 and 10 s. tapaus is locked and t varied, so each experiment isolates its parameter. The model box states the limits (full speed at once, no friction, case 4's instant reversal).
- Exactly one correct option in each choice item (pred-1..3, exp-2, edestakainen, virhe, check-1, pr-nopeus). Every distractor's feedback is physically right.
- Definitions (paikka, siirtymä, matka, nopeus, vauhti, keskinopeus) agree with the glossary. The vector overline is used for $\overline{v}$ and $\Delta\overline{x}$, with components on the line.
- The worked example is symbolic first, and its $x = x_1 + vt$ is justified by $t_1 = 0$ (stated). The reasonableness check is independent.
- pred-2's "C edellä" states the positive direction, so the guardrail is satisfied.
- Scope: tasainen suoraviivainen liike and graphical analysis only. No later-course physics.
