VERDICT: FAIL
CONTENT-HASH: 9ec8522d9ac8e1c9

## Blocking
- assets/sims/fy6/fy6-4/sim.js:91 — **A**: the dot speed `Math.min(360, 600 * w.I)` saturates at 0.6 A in every wire separately. So when the current is large, the main-wire dots stop being the sum of the branch dots, and that sum is the lesson's central idea (I = I1 + I2) as well as what `howto` and sim-spec promise ("haarojen pisteet summautuvat"). You can reach it inside koe-2's own vary range: U = 6 V, R1 = 100 Ω, R2 = 10 Ω gives I = 660 mA, but the main wire moves at 360 px/s, the same as branch 2 (600 mA), while branch 1 moves at 36 px/s. At 12 V with 10 Ω || 10 Ω all three wires move at the same speed. In single mode, 0.6 A and 1.2 A look the same. — Fix: scale every wire by one common factor, e.g. `k = Math.min(1, 0.6 / C.I)` and `v = 600 * w.I * k`, so the proportionality holds whatever the current (or lower the gain so the maximum of 2.4 A stays under the cap).

## Polish
- content/fi/FY6/fy6-4/lesson.md:102 — "energiaa muuttuu lämmöksi, ja siksi … on jännite" reads as if the cause runs backwards. Better: "Vastuksen jännite kertoo, kuinka paljon kunkin varauksen sähköistä energiaa muuttuu siinä lämmöksi."
- content/fi/FY6/fy6-4/inquiry.json:85 — the answer to ennuste-2 (120 mA) holds only for an ideal battery, and the student meets the prediction before the model text. Add "ihanteelliseen" to the prompt; the wrong option's feedback already relies on this.
- content/fi/FY6/fy6-4/inquiry.json:320 — the not-inverted error, 12 V : (20 Ω + 1/60 + 1/30), gives 0.5985 A, which falls within 2 % of the mistake value 0.6. A student who made that error gets the feedback "otit huomioon vain rinnakkaisosan", which does not describe their mistake. Consider a combined feedback.
- assets/sims/fy6/fy6-4/sim.js (rinnan) — a node dot is drawn at the corner (Rx, T), where the wire does not branch; the lesson figure does the same at (476, 86). It is harmless but could be dropped.

## Checked
- Recomputed in one script with my own formulas, next to lesson-answers.py: worked example 40 Ω → 0.225 A → 0.23 A, virhe 12 Ω, siirto 0.30 A with mistakes 0.109/0.60, tarkistus-2 5.4 V (mistakes 3.6/4.5/9.0), exit ticket 115 Ω and 40 Ω, kertaus 60 mA, misconception 0.20 A. All agree.
- Koe-1 and koe-2 model values (40/30/20 mA; I1 = 60 mA; 180/120/90 mA; 33.3/50/66.7 Ω) agree with the sim's solve(), and the simState keys I1mA, I2mA, U1, U2, ImA and R exist in every mode.
- Experiments lock mode, U and R1 and vary only R2: the parameter is isolated.
- Every choice item has exactly one correct option, each distractor is really wrong, and every feedback is right.
- Graph: "mittakaavassa" holds. Series 100→300 Ω, parallel 0→66.7 Ω, and the points at R2 = 100 Ω (200 Ω and 50 Ω) sit at the right pixels.
- Circuit figures: battery polarity, conventional current + → −, the junctions, and the R2 || R3 topology of the mixed and siirto-mixed figures are all correct.
- Conditions stated: ideal battery, wires with no resistance, resistance independent of temperature (Ydinajatus, sim model, example).
- Causality: charge neither vanishes nor piles up, a parallel branch is a new path, and a home's appliances get the same mains voltage.
- Scope: within FY6 "vastusten kytkennät"; power appears only qualitatively (the glow), with a pointer to its own chapter.
