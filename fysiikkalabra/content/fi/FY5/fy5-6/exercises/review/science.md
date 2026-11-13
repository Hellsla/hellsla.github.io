VERDICT: FAIL
CONTENT-HASH: aa6dd2419517254c
SCOPE: delta added-exercise from 1ae57cce87a7a6fc base 81db4a6fd727

## Blocking
- solutions.md:234, exercises.json:275 (L2-08) — A: the rounding is not justified. The perihelion 88 milj. km has 2 sf, and the aphelion is "noin 5250", so the ratio has 2 sf: 7,7. The solution says "noin 7,72-kertainen, kolme merkitsevää numeroa" and gives no reason. — Fix: answer 7,7, limited by 88 milj. km (2 sf), and set `answer` 7.7. A student's 7,7 is already inside the tolerance.

## Polish
- solutions.md:224 (L1-11): "kolme merkitsevää numeroa kuten taulukon massassa" is not the reason, because the table mass 7,346·10²² kg has 4 sf. The limiting datum is the height 300 km. Name it.
- L1-10 gets the same Earth orbital speed as L1-08 (29,8 against 29,79 km/s), by another method. That is fine, and the solution's last line says so. L1-11 is close to L1-05 (a lunar orbiter); the table lookup is what is new.

## Checked
- The hash was the same at the start and at the end. Only L1-10, L1-11 and L2-08 were judged.
- Recomputed: L1-10 gives √(γ·1,99·10³⁰ kg / 1,496·10¹¹ m) = 29,80 km/s; L1-11 gives √(γ·7,346·10²² kg / 2,037·10⁶ m) = 1,551 km/s; L2-08 gives √(5250/88) = 7,724. All three equal answers.py.
- The figure's numbers agree with the real values. Earth: 147,1–152,1 milj. km. Halley: 88 and about 5250 milj. km (0,586 au and 35 au). Each value is labelled in the drawing and in the description. The two tasks read different halves of the figure, so neither gives the other away.
- MAFY task L1-11: the Moon's mass 7,346·10²² kg and radius 1737 km are VERIFIED rows fy5-6, and the hint names only the table. The ±4 % in the solution matches `tolerance` 0.04. r = R + h is used, as the brief warns.
- L2-08 states the hypothetical circular orbits and says that Halley's real orbit is an ellipse, so the model is not misapplied.
- Notation (γ, M, r, $v=\sqrt{\gamma M/r}$) is the brief's.
