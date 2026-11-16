VERDICT: PASS
CONTENT-HASH: 6a72c489fde97bd9

## Blocking

## Polish
- lesson.md:152, lesson.md:212 (and the loss-graph aria-label), inquiry.json:76, 106, 107, 109, 227, 250, exit-ticket.json q2: "muuttuu lämmöksi" breaks guardrail P1 ("muuttuu sisäenergiaksi, joka siirtyy lämpönä ympäristöön"). The lesson contradicts itself here: the sim's legend line and the siirto solution's Periaate already say "sisäenergiaksi". These sentences are listed in docs/physics-phrases-known.tsv, so work queue 18 owns them and they are not blocking in this round. Fix them in one pass for theory, the sim boxes, the prompts and the exit ticket.
- sim.js scene(): the town-side label is always $20\,\text{kV}$. In the model the step-down transformer receives $U - RI$, so at $50\,\text{kV}$ with $200\,\text{MW}$ the town voltage would be about $10\,\text{kV}$ with the inverse ratio. Either add "jännitehäviö jätetään huomiotta jännitteen osalta" to Mallin oletukset, or show the receiving voltage. Either way it is a C-level simplification.
- sim.js state(): when `mahdoton` is true, simState still reports `Ph` and `osuus` (600 MW, 300 %). The readout hides them, but if an experiment ever records them at 20 kV the table would show impossible values. Clamp them, or keep 20 kV out of experiment ranges (koe-1 does).
- lesson.md:311 (Jännite lasketaan vaiheittain): "puhelin ei ole johtavassa yhteydessä sähköverkkoon" holds for an isolated (galvanically separated) charger. That is true of approved chargers but is the condition. Consider "turvallisessa laturissa".

## Checked
- One script recomputed all 35 numbers in lesson-answers.py with my own formulas, and every one agrees: worked example $N_1 = 1980$, $I_1 = 81{,}8\,\text{A} \to 82\,\text{A}$, $9{,}0\,\text{MW}$ both sides; sim values at 50/100/200/400 kV; virhe $2{,}7\cdot10^{10}\,\text{W}$ vs $1{,}5\,\text{MW}$; siirto $720\,\text{kW}$ and its three mistakes; check-2 $0{,}26\,\text{A}$ and 95,8 A; exit $11{,}5\,\text{V}$ and 1/9.
- Sim in the browser (preview/fy7-8.html): simState at koe-1's values gives I, Ph, osuus = 2000 A/24 MW/12 %, 1000/6,0/3,0, 500/1,5/0,75, which match the model answer. At 20 kV it gives `mahdoton` ($RI = 60\,\text{kV} \ge U$), and the condition $RI \ge U \Leftrightarrow P_\text{h} \ge P$ is right. koe-1 locks P and l and varies only U.
- Loss graph is to scale: the curve's pixels match $100\,\% \cdot RP/U^2$ at 70, 100, 150, 200 and 400 kV, and the labelled points are exact.
- Transformer physics: equal emf per turn, $U_1 : U_2 = N_1 : N_2$, $I_2 : I_1$ from power conservation stated for a resistive load, DC gives zero after the switching pulse, laminated core and eddy currents, efficiency over $99\,\%$.
- The $U^2 : R$ misconception is treated correctly in theory, the prediction feedback, Etsi virhe (voltage drop $RI = 3{,}0\,\text{kV}$) and the mistake feedback.
- Three-phase box: $P = \sqrt3\,UI\cos\varphi$, line-to-line voltage, factor 1,73, and the two-wire model declared for the calculations.
- Grid facts: 400/220/110 kV, the 110 kV and 20 kV steps, 400 V/230 V low voltage, generator 20 kV, Fingrid loss figure with its source.
- Predictions and checks: each has exactly one correct option, every distractor's feedback is right, the explain model answers match the theory, and sig figs are justified.
- Scope: everything is within the LOPS FY7 "muuntaja ja energian siirto"; no self-induction.
