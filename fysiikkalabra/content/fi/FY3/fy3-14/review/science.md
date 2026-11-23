VERDICT: PASS
CONTENT-HASH: d6e581ceff728ce3

## Blocking

## Polish
- lesson.md:169 (energy-balance figure) — the label $s\,m_\text{j}$ sits inside the pale, unmelted part of the bar only, so a reader can take $s m_\text{j}$ to mean the ice left unmelted rather than the whole light-blue segment from $2{,}1$ to $35{,}5\,\text{kJ}$ — move the label down into the solid light-blue part or add a bracket over the whole segment.
- lesson.md:316 — "sulaminen vie kaksi kolmasosaa veden luovuttamasta lämmöstä ($16{,}7$ / $25{,}1\,\text{kJ}$)": the water actually gives off $18{,}8\,\text{kJ}$ (the same paragraph says so). $25{,}1\,\text{kJ}$ is what it could give off cooling to $0\,{}^\circ\text{C}$ — say "siitä lämmöstä, jonka vesi luovuttaisi jäähtyessään $0\,{}^\circ\text{C}$:seen", or use $16{,}7/18{,}8$.
- lesson.md:332 (Tiivistelmä) — the formula $m_\text{s} = (Q_\text{v} - c_\text{j} m_\text{j}\Delta T_\text{j})/s$ is given under "Jos $Q_\text{v} < Q_\text{j}$" and turns negative in case 3 — add "kun $Q_\text{v} \ge Q_\text{j,läm}$", as the Kaava section does.
- inquiry.json simulaatio.howto — "Lopputila kertoo neljästä tapauksesta yhden" reads as though the readout names the case, but sim.js shows no case line (sim-spec.md asks for one) — add the line to the readout or reword the sentence to say the end state is one of four cases.
- inquiry.json siirto.solution "Vastaus" — the explanation of why the answer has three figures ("kolmannen numeron tuhansien paikkaan") is muddled. The point is that $8{,}0\,{}^\circ\text{C}$ enters only through $T_\text{l}-T = 14{,}0\,\text{K}$ (absolute ±0,1) and a small term in the denominator — say that.

## Checked
- One script recomputed every number from the task data with my own formulas: Ydinajatus 79,7 K; before-after figure 24,7 g / 0,375 kg; energy-balance figure 25,1 / 2,1 / 35,5 kJ; graph 26,57 °C, 40,07 °C at 80 °C (pixels 252,8 and 69,6 to scale); worked example 6,05 °C with the energy check 18,8 = 18,8 kJ; misconception 15 °C. All agree.
- Predictions: ennuste-1 24,7 g, 75,3 g, threshold 26,6; ennuste-2 5,9 / 18,5 / 12,6 / 81,5 g, 31,4 kJ, 1/8. Each has exactly one correct option, and every distractor's feedback is correct.
- koe-1 and koe-2: each locks the right parameters and varies only one; their values are reachable with the slider steps; Tf and iceLeftG are in simState. The numerics 26,6 °C and 12,6 g are right, and so is the model answer (62,4 g, 10,1 °C).
- virhe −25,6 °C and 0,225 kg; siirto 39,9 g with mistakes 43,9 and 438 g; tarkistus-2 40,06 °C with mistakes 56 and 35; exit ticket 66,8 kJ and 12,5 g. All right.
- sim.js covers all four cases. My derivation of the case-4 balance matches the code, and so does Qend for each case. In the animation the thermometer reading at the end equals Tf. Liquid water is never shown below 0 °C. The bar scale reaches at most 209 kJ, under 250 kJ.
- Boundary cases follow the guardrails: Q_v = Q_j gives exactly 0 °C (≥) in the Kaava section, the summary, the figure caption and ennuste-1. The case where all the water freezes is kept everywhere.
- Melting is described as raising the interaction energy between particles (guardrail wording). The 0 °C claim is tied to normal pressure in the summary. The model box says the animation's pace is illustration only.
- check-c2: water at 0 °C freezes onto a −18 °C cube. Freezing releasing energy is right.
- The lesson stays within the FY3 central content (changes of state, conservation of energy), with no later-course physics.
