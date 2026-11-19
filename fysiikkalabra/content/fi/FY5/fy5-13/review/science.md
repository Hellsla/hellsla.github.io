VERDICT: PASS
CONTENT-HASH: dc3f62700100266d

## Blocking

## Polish
- inquiry.json:273 (johtopäätös model): "Suljetussa päässä oli aina solmu ja avoimessa kupu" holds for the peaks, but the koe-2 table also records 200 Hz and 400 Hz, and at those the sim shows a node at the open end (U(0) = a·tan kL = 0). Write "huipuissa suljetussa päässä oli solmu ja avoimessa kupu" so that the model answer matches what the student saw.
- assets/sims/fy5/fy5-13/sim.js:68 with the open pipe: A rises toward the lower end of the slider (2,7 mm at L = 0,40 m, 50 Hz) because cot kL diverges as f → 0 (the uniform n = 0 motion). It is harmless, but a student may read it as a resonance below f1. One clause in the `model` box would cover it, or clamp the open pipe's f to above about 0,3 f1.
- inquiry.json `model` box: off resonance the driven end moves by a and is marked K (string at 50 Hz: "Solmuja 1, kupuja 1", K at the vibrator). This is correct steady-state physics, but one sentence ("taajuuksilla ominaistaajuuksien välissä täryttäjän pää liikkuu eniten") would stop students reading it as a broken "päät kiinni" condition.

## Checked
- I recomputed in one script with my own formulas: the worked example (v = 2Lf1 = 143 m/s, L' = 0,433 m), the error spotting (100 Hz), the transfer task (170 Hz; the mistakes 113, 227 and 56,7 are right), check 2 (0,80 m; the mistakes 0,40 and 2,4), the misconception (2,40 m). All agree with lesson-answers.py.
- I reproduced the sim model: the peaks are 16,7 mm (1/sinh 0,06). Between them A is 1,0 mm (string 50, 150 Hz; closed pipe 200, 400 Hz) and 1,41 mm (closed pipe 150 Hz). There are 2, 3 and 4 nodes at 100, 200 and 300 Hz; the closed pipe gives 1, 2, 3 nodes and kupuja at 100, 300, 500 Hz, and the open pipe peaks at 200 and 400 Hz. Every number in the prediction feedback and the conclusion matches.
- Experiments: tila and L are locked, plus v for the string (for a pipe the sim fixes v = 340 m/s). f is the varied quantity. simState carries A, solmut, kuvut and lambda.
- The boundary conditions are right: a displacement node at a fixed or closed end, an antinode at an open end. The end correction is stated and left out, and v = 340 m/s is stated.
- Superposition figure (figures.py): incident A sin(ωt+ks) and reflected −A sin(ωt−ks) give 2A cos ωt sin ks, with a node at the wall. The sum's swing is in phase with the travel animation, and the three rows are at 0, T/8 and T/4.
- The node/antinode figure (λ/2 and λ/4 brackets), the string modes and the four pipe modes (cos πu, cos 2πu, cos πu/2, cos 3πu/2) all have the right node positions and labels.
- Each prediction has exactly one correct option, and every distractor's feedback names the actual error.
- The exit ticket (3 K, 4 S; the clarinet an octave lower), tarkistus-1 and the tarkistus-3 model all agree with the theory.
- Causality: resonance builds through reflections that arrive in phase, tension raises v, and a heavier string has a lower v. No energy-transport claim breaks the guardrails.
- Scope: standing waves and eigenfrequencies of a string and a pipe are FY5 central content, and the lesson stays inside it.
