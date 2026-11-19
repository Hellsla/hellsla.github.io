VERDICT: PASS
CONTENT-HASH: ea654eb5479b015a

## Blocking

## Polish
- inquiry.json koe-2 — the sim still marks S at the driven open mouth at the 200 Hz and 400 Hz rows the student is told to record. The model at x = 0 gives U = a·tan(kL), about 0,06 mm there. The question now asks about the ends at the peaks, and the model answer says "Huipuissa", so this is no longer a contradiction. A short note in the `model` box would still help a student who notices it, for example "Taajuuksilla huippujen välissä täryttäjän tai kaiuttimen pää ei ole kupu."
- sim.js setup — the visible control texts ('Tilanne', the option labels, 'Nopeus', the note line) are literals rather than `lang` strings. This is a house-rule matter, not physics.

## Checked
- Round-1 item resolved. The calc box now says the open end is largest "ominaistaajuuksilla", koe-2 asks about the ends "huipuilla", and the johtopäätös model says "Huipuissa". I recomputed with the sim's own `marks()`: at 100, 300 and 500 Hz, K is at the open mouth (j = 0) and S at the closed end. S/K counts are 1/1, 2/2 and 3/3. The model box also says the kupu is at the mouth "ominaistaajuuksilla".
- One script, with my own formulas next to the lesson's values. Worked example: v = 143 m/s, L′ = 0,433 m, which equals 0,650/1,5. Siirto: 170 Hz; its mistakes 113, 227 and 56,7 Hz are right. Tarkistus-2: 0,80 m; its mistakes 0,40 and 2,4 m are right. Etsi virhe: 200 → 100 Hz, λ₁ = 3,4 m, and the distractor's 400 Hz is right.
- Sim model reproduced. Peak A = a/sinh(0,06) = 16,7 mm. Off-peak values: 1,0 mm on the string at 50, 150 and 250 Hz, and 1,0 mm in the closed pipe at 200 and 400 Hz. The closed pipe gives 1,41 mm at 150 Hz, which matches ennuste-2's "1,4 mm".
- Koe-1: the string has 2, 3 and 4 nodes at 100, 200 and 300 Hz, with λ = 1,20, 0,60 and 0,40 m. Koe-3: the open pipe peaks at 200 and 400 Hz.
- Experiments: each one locks everything except f. The initial values can be reached with the slider steps. simState carries A, solmut, kuvut and lambda.
- Exactly one option is correct in kertaus, both predictions, etsi virhe and tarkistus-1. Each distractor's feedback is right. Both exit-ticket answers are right (3 K / 4 S; the clarinet is an octave lower).
- Theory: the reflection phase, node and antinode spacing, energy transport, resonance, the end correction stated and set aside, v = 340 m/s, and the octave claim for the closed pipe are all right. The summary matches the Kaava section.
- Figures: superposition at t = 0, T/8 and T/4, with nodes λ/2 apart and one at the wall. The four pipes show L = λ/2, λ, λ/4 and 3λ/4. The hero shows the fundamental between the capo and the saddle.
- The sim code implements the stated model: the boundary conditions, eigenfrequencies that emerge instead of being entered, and a speed setting that changes only the pace.
- The hash was the same at the start and the end.
