VERDICT: PASS
CONTENT-HASH: 6a91c39269e0ec4c

## Blocking

## Polish
- lesson.md:214 — The MAFY name "tehonkulutus johtimessa" stands beside $P = UI$, but here $P$ is the power the plant sends and $U$ is the transmission voltage, not the voltage across the line. This is the misconception the section warns against. Line 217 defines the symbols correctly, so no wrong picture should remain (C). Teacher's call: leave this line unnamed in docs/fy7/kaavanimet.tsv, or add "(lähetetty teho, ei johdossa kuluva teho)" to line 217.
- inquiry.json `siirto` solution, Järkevyys — The check compares one line's $2{,}2\,\%$ loss with Fingrid's national figure of about $2\,\%$ of the electricity used. Say "suuruusluokaltaan samaa kuin koko kantaverkossa" so the comparison is clearly only a check of magnitude.

## Checked
- Recomputed every number in one script, with my own formulas: worked example (1980 turns, $81{,}8\,\text{A}$, $9{,}0\,\text{MW}$ on both sides), sim values at 50/100/200/400 kV (4000/2000/1000/500 A, 96/24/6,0/1,5 MW, 48/12/3,0/0,75 %), the graph's labelled values and its $24{,}5\,\%$ top at 70 kV, `virhe` ($2{,}7\cdot10^{10}\,\text{W}$; $1{,}5\,\text{MW}$; $RI = 3{,}0\,\text{kV}$), `siirto` 720 kW and its three mistake values, tarkistus-2 ($0{,}261\,\text{A}$; 5,0 A; 95,8 A), exit ticket (11,5 V; 1/9). All agree.
- Transformer: mechanism (changing flux in a closed core, the same EMF per turn), the ideal ratio with its conditions (ideal, effective values, power conserved), no output with DC except at switching, real losses and laminated core. Correct and consistent with the glossary.
- Loss model: $P_\text{h} = RI^2$ with $I = P/U$. The $U^2/R$ misconception is explained by its true cause (only the drop $RI$ is across the line). The two-wire simplification is stated, and three-phase $P = \sqrt3\,UI\cos\varphi$ is given with the line-to-line voltage.
- ennuste-dc and ennuste-jannite: exactly one correct option each. Every distractor's feedback is physically right, and the cited model values match the sim.
- Koe 1: P and l are locked and only U varies. The initial state is valid (not `mahdoton`), and `simState` provides I (A), Ph (MW) and osuus (%) as the table labels say.
- sim.js uses the same model as sim-spec and the `model`/`calc` boxes. The `mahdoton` test $RI \ge U$ is the same as $P_\text{h} \ge P$. The bars and readout are consistent.
- Explain model answers (johtopaatos, tarkistus-3) match the theory. The sim's numbers are called model values.
- Grid voltages (400/220/110 kV, 20 kV, 400/230 V), the 2 % loss source and the charger are accurate and within FY7 scope.
- Hash checked at the start and the end, unchanged.
