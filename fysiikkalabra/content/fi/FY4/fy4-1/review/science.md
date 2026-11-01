VERDICT: FAIL
CONTENT-HASH: bb655d3ae81a61dd

## Blocking
- inquiry.json:198 (exp-1 solution, Vastaus) and inquiry.json:310 (exp-3 solution, Vastaus) — **A**: the rounding reason "simulaation mallin arvot esitetään kahdella numerolla" is false. sim.js formats every position with `tx(x, 1)`, so the readout and table show 40,0 m, 16,0 m, 30,0 m (three significant figures; see shots/fy4-1-exp-exp-1-390-1.png). The answers 4,0 and −3,0 m/s are right, but the stated reason contradicts what the student sees. — Give a true reason, e.g. "mallin arvot ovat tarkkoja; nopeus ilmoitetaan kahdella numerolla kuten tunnin muut tulokset", or write 4,00 / −3,00 m/s from the 0,1 m readout.
- inquiry.json:84 (pred-2 prompt; correct option "C pysyy koko ajan 20 m edellä") and inquiry.json:206 (exp-2 intro "C lähtee A:n edestä") — **B**: under the motion-graph guardrail (higher-line-ahead), "edellä" holds only when both carts move in the positive x direction, and pred-2 says only "samaan suuntaan". — Write "ajaa positiiviseen suuntaan yhtä nopeasti kuin A" in the pred-2 prompt. The exp-2 intro then follows from it.

## Polish
- lesson.md:5 — the hero shows a loop around a lake, but the Miksi line, the hook and the round-trip figure use a straight there-and-back ride to the shop. Both have Δx = 0, but on a loop the 1-D x axis does not apply. Consider a straight road in the hero, or say in the caption that the start and end points are the same.
- inquiry.json:532 (check-3 model) — in the hook he stops to buy milk, so his graph also has a horizontal part. Add "ja kaupassa vaakasuora osa".
- inquiry.json check-3 criteria — the units criterion says "paikka ja siirtymä metreinä", but the task's distances are in km. Write "pituusyksikössä (m, km)".

## Checked
- Recomputed every number in one script: exp-1 4,0; exp-3 −3,0; A and D meet at t = 6 s, x = 12 m; pulkka v = 5,0 m/s, x(10 s) = 39 m, x₀ = −11 m; check-2 13 m and 4,8 s; example 2,5 m/s, 170 m ≈ 1,7·10² m, 9 km/h; path of E 16 m; pr-nopeus 7,5 m/s. Every mistake value (2,0; 40; 3,0; 30; 1,9; 1,3; 0,67; 50; 74; 5,0; 25; 37) is the stated wrong method.
- Robot data: least-squares slope 1,494 ± 0,029 m/s, intercept 4,10 m, x(10 s) = 19,04 m. The SVG line runs from (0; 4,1) to (10; 19,1) m to scale, so "hieman alle 20 m" holds.
- Edestakainen figure geometry (0→8 m in 4 s, rest until 6 s, back to 0 at 10 s) matches sim.js `pos` for case 4. `path` gives 16 m and `vel` changes sign correctly.
- sim.js implements x = x₀ + vt for cases 1–3 with the stated speeds. simState carries xA and x2. The 0,5 s slider step reaches t = 4,0 / 6,0 / 10 s. The model box states the simplifications (instant full speed, no friction or size).
- Each experiment locks tapaus and varies t, so the setups isolate the comparison.
- Every prediction, Etsi virhe, check-1 and edestakainen item has exactly one correct option, and each distractor's feedback is right.
- Definitions (paikka, siirtymä, matka, nopeus/vauhti, keskinopeus = Δx/Δt) agree with the glossary and the exit ticket. The vector notation (overline, components on a line) follows the FY4 scope.
- The slope is read from the fitted line, not from neighbouring raw points, in line with the guardrail.
- Worked example: solved symbolically first, the rounding reason is sound, and the reasonableness check is real.
- Hash is the same at the start and at the end.
