VERDICT: PASS
CONTENT-HASH: 1197308b4ca04e20

## Blocking

## Polish
- exercises.json:155 (fy3-1-L1-10) — the stored answer is 316,2 N, but the solution's Vastaus is $316\,\text{N}$ (3 s.f.). The tolerance accepts both, so no student is wrongly marked. Still, the answer shown on the page has one more figure than the solution justifies — consider storing 316 (the ±4 % tolerance already covers MAFY 3,72 and the lesson's 3,71, which gives 315,4 N).

## Checked
- I recomputed all 20 numeric answers in one script with my own formulas. Every one lies within its tolerance of my value. L2-05 used a least-squares fit through the origin (9,80 m/s²). L3-04 used a least-squares $x/m$ (3,61 against the solution's 3,59, which comes from a sum ratio). The answers.py lines compute the right physics.
- G = mg is used everywhere with the lesson's g table. Mass and weight are kept apart, and the spring stretch is proportional to the force with "not over-stretched" stated. Everything stays inside FY3 scope: no Newton's laws are used. In L1-09 the equality F = G comes from the meter reading equalling mg.
- L1-09 force diagrams: B (G down from the centre, F up from the hook face, same length) is the only right one. A (pull missing), C (pull drawn twice) and D (F_k is the third-law partner acting on the meter) each carry exactly the intended error, and their feedback says why.
- L1-06 and L1-07: exactly one option is correct, and every distractor's feedback is physically right.
- The figures spring-points and weight-points give every value the tasks need. Their descriptions list the points without the ratio or g, so neither gives the answer away.
- L2-06 data is consistent: the Moon row gives 1,59 m/s² against the table's 1,62.
- L3-03 is a scale calibrated in kg on Earth and read on Mars. The model is right and the solution is symbolic first.
- L3-05: the leg limit is a force, and the solution gets 1617 − 935 = 682 kg. The Earth comparison (612 kg) is right.
- Significant figures follow the limiting datum in every solution, and the reasonableness checks are real (back-calculation, ratio to Earth's g).
