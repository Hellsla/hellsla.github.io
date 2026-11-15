VERDICT: FAIL
CONTENT-HASH: 29511f4151251bcf

## Blocking
- lesson.md:160, 224; inquiry.json:76, 106, 107, 109, 227, 250; exit-ticket.json:7 — **A (definition, guardrail "Energy into heat", FY3–FY9, task texts included)**: power "muuttuu lämmöksi" / "lämmöksi muuttuva teho" in the theory, the formula section, ennuste-jannite, the sim's text, howto and calc, the siirto prompt and solution, and the exit ticket. Heat is energy in transfer, not something the energy becomes. These fi-easy sentences are not on docs/physics-phrases-known.tsv, and the sim note in sim.js already says it right ("sisäenergiaksi muuttuva teho"), so the lesson contradicts itself. — Fix: "johdossa sisäenergiaksi muuttuva teho" or "teho, joka muuttuu johdossa sisäenergiaksi ja siirtyy lämpönä ympäristöön", once and the same everywhere. The loss-graph aria-label (lesson.md:235) can match.

## Polish
- lesson.md:209 — the photo caption writes $P = RI^2$ for the loss, but the lesson's symbol is $P_\text{h}$ ($P$ is the transmitted power). Use $P_\text{h} = RI^2$.
- lesson.md:361 — the summary's "Kaksinkertainen siirtojännite pienentää häviöt neljäsosaan" should say "kun teho ja johto pysyvät samoina" (line 231 says so).
- inquiry.json siirto mistakes — add the value 2400 for $RI$ given in volts without converting. Only 2,4 is caught now.
- lesson.md:302 (three-phase) — "noin 1,73-kertaisen tehon" assumes the same $\cos\varphi$ in both models. The two-wire $P = UI$ implies $\cos\varphi = 1$. Fine as context, outside the core.

## Checked
- One `python3 -I` run against lesson-answers.py: every number matches my own formulas. Worked example $N_1 = 1980$, $I_1 = 81{,}82 \to 82\,\text{A}$, $9{,}0\,\text{MW}$ both sides. Sim table 4000/2000/1000/500 A, 96/24/6,0/1,5 MW, 48/12/3,0/0,75 %. Virhe $2{,}7\cdot10^{10}\,\text{W}$ vs $1{,}5\,\text{MW}$, distractor 27 kW, $RI = 3{,}0\,\text{kV}$. Siirto 720 kW with its three mistakes. Check 2 gives 0,26 A, with 5,0 A and 95,8 A as mistakes. Exit ticket 11,5 V and 1/9.
- The loss-graph is to scale: the polyline is within 0,9 px of $100\,\% \cdot RP/U^2$ over 70–400 kV, and the 12 / 3,0 / 0,75 % markers are right.
- Sim: $I = P/U$, $P_\text{h} = RI^2$, $R = 0{,}040\,\Omega/\text{km} \cdot l$. "Mahdoton" when $RI \ge U$ is the same as $P_\text{h} \ge P$ (30 kV and below at 200 MW, 150 km). simState gives I, Ph, osuus. Koe-1's initial values can be reached on the sliders, and locking P and l isolates U.
- Predictions: one right option each (0 V; neljäsosaan), and every feedback's numbers are right. The kertaus, virhe and check-1 distractors are really wrong and their feedback says why.
- Transformer figure: closed core, $N_1 > N_2$ for a step-down, the flux arrows go one way round. The DC-pulse explanation and $U_1 I_1 = U_2 I_2$ are tied to resistive load / ideal.
- Grid values: 400/220/110 kV, 20 kV, 400/230 V. Efficiency over 99 %. The Fingrid 2 % is sourced. Scope is inside the FY7 transformer and transmission content.
