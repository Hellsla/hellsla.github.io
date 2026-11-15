VERDICT: PASS
CONTENT-HASH: 3f3066119fcda820

## Blocking

## Polish
- lesson.md:209 (photo caption): the loss is written $P = RI^2$, but everywhere else it is $P_\text{h} = RI^2$, and $P$ is the transmitted power. Fix: write $P_\text{h} = R I^2$.
- inquiry.json `virhe`, the kilovolt distractor: $400^2 : 6{,}0 \approx 26\,667$, so "$27\,\text{kW}$" only comes out if that number is read as watts. Its feedback is still correct. Fix (optional): write the distractor's number as the one that arithmetic gives.
- The sim legend and `lang/fi-easy.json` (`selite`) say "johdossa lämmöksi muuttuva teho", but the lesson, the experiment and the sim box say "sisäenergiaksi". This is not wrong, because the glossary says "muuttuu lämmöksi ympäristöön". Fix: use one wording in both places.
- lesson.md `grid` figure: the sähköasema goes from $400\,\text{kV}$ straight to $20\,\text{kV}$, while the text names the $110\,\text{kV}$ alueverkko step. The figure is schematic and says it is not to scale, so this is a C. Fix (optional): add "(110 kV)" or "vaiheittain" to the aria-label.

## Checked
- I recomputed every number in one script with my own formulas: worked example ($N_1 = 1980$, $I_1 = 81{,}82\,\text{A}$, both $9{,}0\,\text{MW}$), the four sim voltages (I, P_h, share), ennuste-2, johtopäätös, virhe ($2{,}67\cdot10^{10}\,\text{W}$, $1{,}5\,\text{MW}$, $RI = 3{,}0\,\text{kV}$), siirto (720 kW, 2,2 %, the three mistake values), tarkistus-2 (0,2609 A, 5,0 A, 95,83 A) and the exit ticket (11,5 V, 1/9). All agree with lesson-answers.py.
- The loss graph is to scale: the curve points at 70, 100, 200 and 400 kV match $100\,\% \cdot RP/U^2$ to within 0,5 px. The labels 12 %, 3,0 % and 0,75 % are right.
- The transformer figure: the core is closed, the flux arrows go round in one consistent direction, it has more primary turns and is labelled as a step-down transformer, and it says it is not to scale.
- Models and their conditions: ideal transformer stated; $P = UI$ for a resistive load; effective values; the two-wire model is named at every point of use; three-phase $P = \sqrt3\,UI\cos\varphi$ is given as context and the 1,73 factor is correct. No self-induction (within the scope note).
- Causality: flux changing → the same emf per turn → $U \propto N$. A DC primary gives zero output after the switching transient. Loss $RI^2$ with $I = P/U$, and the $U^2/R$ misconception is handled correctly (the voltage across the line is $RI$).
- sim.js implements $R = 0{,}040\,\Omega/\text{km}\cdot l$, $I = P/U$, $P_\text{h} = RI^2$ and $N_2:N_1 = U:20\,\text{kV}$. The "impossible" condition $RI \ge U$ is the same as $P_\text{h} \ge P$, and the sim says so. Its values are called model values.
- koe-1: P and l are locked, U is the only thing that varies. The slider steps reach 50, 100, 200 and 400 kV, P = 200 and l = 150. simState gives I (A), Ph (MW) and osuus (%).
- Exactly one correct option in each of kertaus, ennuste-dc, ennuste-jannite, virhe and check-1. Every distractor's feedback names the right physics.
- The model answers (johtopäätös, tarkistus-3) and the summary agree with the theory. Magnitudes are realistic: generator about 20 kV, grid voltages 400/220/110 kV, transformer efficiency over 99 %, losses about 2 %.
- The content hash was the same at the start and at the end.
