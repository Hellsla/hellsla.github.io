VERDICT: PASS
CONTENT-HASH: 29511f4151251bcf

## Blocking

## Polish
- lesson.md:160, 224, 235 (aria); inquiry.json:76, 106, 107, 109, 227, 250; exit-ticket.json:7 — "muuttuu lämmöksi" / "lämmöksi muuttuva teho" breaks the guardrail "Energy into heat" (P1). It is not blocking here: these are the same sentences as in the version that passed before, and docs/tyojono.md item 18 already schedules them, FY7's translations included (docs/audits/2026-11-15-oikoluku.md §4, §11 FY7 fy7-8). The FY7 round is PR #617. — Fix in item 18: "johdossa sisäenergiaksi muuttuva teho", the same wording everywhere.
- lesson.md:209 — the photo caption writes $P = RI^2$ for the loss, but the lesson's symbol is $P_\text{h}$ ($P$ is the transmitted power). Use $P_\text{h} = RI^2$.
- lesson.md:361 — the summary's "Kaksinkertainen siirtojännite pienentää häviöt neljäsosaan" should say "kun teho ja johto pysyvät samoina" (line 231 says so).
- inquiry.json siirto mistakes — add the value 2400 for $RI$ given in volts without converting. Only 2,4 is caught now.
- lesson.md:302 (three-phase) — "noin 1,73-kertaisen tehon" assumes the same $\cos\varphi$ in both models. The two-wire $P = UI$ implies $\cos\varphi = 1$.

## Checked
- One `python3 -I` run against lesson-answers.py: every number matches my own formulas. Worked example $N_1 = 1980$, $I_1 = 81{,}82 \to 82\,\text{A}$, $9{,}0\,\text{MW}$ both sides. The sim table at 50, 100, 200 and 400 kV. The virhe numbers. Siirto 720 kW with its three mistakes. Check 2 gives 0,26 A, with 5,0 A and 95,8 A as mistakes. Exit ticket 11,5 V and 1/9.
- The loss-graph is to scale: the polyline is within 0,9 px of $100\,\% \cdot RP/U^2$ over 70–400 kV, and the 12 / 3,0 / 0,75 % markers are right.
- Sim: $I = P/U$, $P_\text{h} = RI^2$, $R = 0{,}040\,\Omega/\text{km} \cdot l$. "Mahdoton" when $RI \ge U$ is the same as $P_\text{h} \ge P$ (30 kV and below at 200 MW, 150 km). simState gives I, Ph, osuus. Koe-1's initial values can be reached on the sliders, and locking P and l isolates U.
- Predictions: one right option each (0 V; neljäsosaan), and every feedback's numbers are right. The kertaus, virhe and check-1 distractors are really wrong, and their feedback is right.
- Transformer figure: closed core, $N_1 > N_2$ for a step-down, the flux arrows go one way round.
- Grid values (400/220/110 kV, 20 kV, 400/230 V, efficiency over 99 %) are right, the Fingrid 2 % is sourced, and scope stays inside FY7.
