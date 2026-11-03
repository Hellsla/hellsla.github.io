VERDICT: PASS
CONTENT-HASH: d3cb9c05c11ebf1a

Delta review (inquiry.json, 4 lines changed since bb655d3ae81a61dd).

## Blocking

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
- Delta: the exp-1 and exp-3 rounding reason now cites only the given two-digit data (true). The pred-2 correct option and the exp-2 intro now say "edellä positiiviseen suuntaan", which is right whichever way the carts move. Previous blocking items are resolved.
- Second delta (hash d3cb9c05c11ebf1a): the only change is the colon to a comma in the exp-1 and exp-3 Vastaus lines. It is punctuation only, with no physics or number changed.
