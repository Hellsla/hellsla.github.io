VERDICT: FAIL
CONTENT-HASH: 40981c5ecada8e6f

## Blocking
- inquiry.json:175 (koe-2), inquiry.json:118 (calc) — **B**. The calc box says the end conditions hold in every case: "kiinteässä ja suljetussa päässä poikkeama on nolla, avoimessa päässä suurin". In the model this is true only at the far (undriven) end. At the driven open mouth it is true only near an eigenfrequency. For the closed pipe, U(0) = a·tan(kL), so at 200 Hz and 400 Hz (kL = π, 2π) |U(0)| ≈ 0,06 mm. `marks()` in sim.js then puts an S at the open mouth. Recomputed with the sim's own code: suljettu 200 Hz gives S at both ends and K in the middle (solmuja 2, kupuja 1); 400 Hz gives S at both ends (solmuja 3). Koe 2 tells the student to record exactly these two frequencies and then asks "Missä putken päässä on solmu ja missä kupu?". A student who reads those rows sees a node at the open end, which contradicts the theory. The same artefact shows in koe-3 (avoin 100 Hz: S at the driven mouth) and on the string (kieli 150 Hz: K at the vibrator end, while the theory says both ends are nodes). Fix: condition the calc sentence (at the end away from the source, and at the source only near an eigenfrequency). In koe-2 add "lue päät huipputaajuuksilta", or have the sim mark S/K only when A is near a peak (for example A > 5a).

## Polish
- sim.js setup — the visible control texts ('Tilanne', option labels, 'Nopeus', the note line) are literals rather than `lang` strings. This is a house-rule matter, not physics.

## Checked
- I recomputed every number in one script from the task data with my own formulas: worked example v = 143 m/s and L′ = 0,433 m; siirto 170 Hz with mistakes 113, 227 and 56,7 Hz; tarkistus-2 0,80 m with mistakes 0,40 and 2,4 m; etsi virhe 200 → 100 Hz; koe 1: 100/200/300 Hz, λ = 1,20/0,60/0,40 m; koe 2: 100/300/500 Hz; koe 3: 200/400 Hz. All agree with lesson-answers.py.
- The sim model reproduced independently: peak A = 1/sinh(0,06)·a = 16,7 mm. Off-peak values in the feedback are right (1,0 mm at 50/150/250 Hz on the string and at 200/400 Hz in the closed pipe; 1,41 mm at 150 Hz in the closed pipe). Node counts 2/3/4 match the johtopäätös.
- Experiments: initial values reachable with the slider steps; only f varies; simState carries A, solmut, kuvut and lambda.
- Prediction options: exactly one correct in each; each distractor's feedback is right; the kertaus and tarkistus-1 options are right; the exit ticket answers are right.
- Figures: superposition (incident sin(ωt+ks), reflected −sin(ωt−ks); coincide at t = 0, cancel at T/4; nodes λ/2 apart with one at the wall); solmut (K at λ/4); string modes; the four pipes (L = λ/2, λ, λ/4, 3λ/4); hero (capo at the true third-fret position, fundamental between capo and saddle).
- Theory: end correction, damping and v = 340 m/s are stated; energy transport, n kupua / n+1 solmua and the octave claim for the closed pipe are correct.
- Hash identical at start and end.
