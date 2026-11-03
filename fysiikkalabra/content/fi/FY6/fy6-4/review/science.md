VERDICT: FAIL
CONTENT-HASH: 9ec8522d9ac8e1c9

## Blocking
- assets/sims/fy6/fy6-4/sim.js:91 — **A**: `Math.min(360, 600 * w.I)` caps the dot speed at 0.6 A in each wire separately, so above that the main-wire dots are no longer the sum of the branch dots. That sum is the lesson's central idea (I = I1 + I2) and what `howto` and sim-spec promise. It happens inside koe-2's vary range: with 6 V, R1 = 100 Ω and R2 = 10 Ω, the main wire (660 mA) moves as fast as branch 2 (600 mA), while branch 1 moves at 36 px/s. At 12 V with 10 Ω || 10 Ω all three wires look the same. — Fix: one common scale factor, e.g. `k = Math.min(1, 0.6 / C.I)` and `v = 600 * w.I * k`.

## Polish
- content/fi/FY6/fy6-4/lesson.md:102 — "energiaa muuttuu lämmöksi, ja siksi … on jännite" reads as reversed causation. Suggest: "Vastuksen jännite kertoo, kuinka paljon kunkin varauksen sähköistä energiaa muuttuu siinä lämmöksi."
- content/fi/FY6/fy6-4/inquiry.json:85 — the 120 mA answer to ennuste-2 assumes an ideal battery, and the student sees the prompt before the model text. Add "ihanteelliseen".
- content/fi/FY6/fy6-4/inquiry.json:320 — the not-inverted error gives 0.5985 A, within 2 % of the mistake value 0.6, so that student gets "otit huomioon vain rinnakkaisosan", which is the wrong diagnosis. Combine the two feedbacks.
- sim.js (rinnan) and the parallel figure — a node dot is drawn at a corner where the wire does not branch, (Rx, T) and (476, 86).

## Checked
- I recomputed in one script and compared with lesson-answers.py: example 0.225 → 0.23 A, virhe 12 Ω, siirto 0.30 A (mistakes 0.109/0.60), tarkistus-2 5.4 V (3.6/4.5/9.0), exit ticket 115 Ω and 40 Ω, kertaus 60 mA, misconception 0.20 A. All agree.
- Koe-1 and koe-2 model values agree with the sim's solve(); the measured simState keys exist; mode, U and R1 are locked, so only R2 varies.
- Every choice item has exactly one correct option, and all distractors and feedback are correct.
- Graph to scale: series 100→300 Ω, parallel up to 66.7 Ω, and the points at R2 = 100 Ω are in the right place.
- Circuit figures: polarity, conventional current, and the R2 || R3 topology of the mixed, task and siirto figures are correct.
- Conditions stated: ideal battery, ideal wires, constant resistance. The mechanism is charge conservation plus a new path for each branch.
- Scope: FY6 "vastusten kytkennät"; power appears only qualitatively, as the glow.
