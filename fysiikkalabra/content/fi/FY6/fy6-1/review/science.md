VERDICT: PASS
CONTENT-HASH: b92c444bea98ff05

## Blocking

## Polish
- content/fi/FY6/fy6-1/lesson.md:42 — "Virtaa ei synny paristossa" can read as "the battery does not drive the current"; the point is that no charge is created — write "Varausta ei synny paristossa eikä virta kulu lampussa".
- content/fi/FY6/fy6-1/inquiry.json:311 (siirto) — energy from the battery is computed with the battery voltage and the *motor* current; with a motor controller the two currents differ — say "akusta kulkee keskimäärin 8,0 A:n virta" so that E = UIt applies to the battery as stated.
- assets/sims/fy6/fy6-1/sim.js:1164 — the electron dots are drawn moving through the cells too; inside a battery charge is carried by ions, not by the wire's electrons. A level-appropriate simplification (C), but a short note in the `model` box ("paristojen sisäistä toimintaa ei kuvata") would prevent the picture.

## Checked
- Recomputed in one script with my own formulas (e = 1,602176634 · 10⁻¹⁹ C): worked example 180 C and 1,1 · 10²¹ electrons, 6,24 · 10¹⁸ e/C, sim Q for 1–3 cells × 1–2 lamps (1,00/2,00/3,00 C; halved with two lamps), exp-1 0,200 A and mistakes 20 / 5, exp-2 0,100 A, siirto 432 kJ (7,2 kJ, 12 000 C, 0,12 kWh), check-2 5400 C (90, 1350, 1,5 Ah), exit 6,0 J — all match lesson-answers.py.
- Sim: I = U/(n·15 Ω); dot counting at A (top, before lamps) and B (right wire, after lamps) is exact for every setting (float test over 2000 phases); electrons move against the conventional direction; Q_A = Q_B declared as a model property; constant-resistance lamp and neglected internal resistance stated.
- exp-1/exp-2: initial states, locks and varied parameter isolate cells resp. lamps; simState gives QA, QB.
- Predictions, exp-2 question, kertaus, check-1: exactly one correct option, every distractor's feedback right (incl. electrons passing B before the lamp).
- Etsi virhe figure: lamp loop returns to the + side, − terminal open — correct option unique.
- check-3 figures: a lamps+switch in loop (correct), b resistors, c switch on a dead-end branch — feedback right.
- Figures: polarity (long thin +), current arrows + → − around every loop, electrons opposite to I, battery/lamp symbols IEC.
- Drift speed "alle mm/s" (≈ 0,04 mm/s for 0,25 A in 0,5 mm² Cu); signal "lähes valon nopeudella" a fair C.
- U = E/Q with the internal-resistance condition stated; exit ticket consistent.
- Scope: FY6 central contents (voltage and current in DC circuits, circuit diagrams); no later-chapter physics required.
