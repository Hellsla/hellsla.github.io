VERDICT: FAIL
CONTENT-HASH: 12a97f81e6e3bc2c

## Blocking
- inquiry.json:89 (pred-2, distractor) — A, assessment: "ero kasvaa suhteessa, kun massa kasvaa" can be read as "the difference grows in proportion to the mass", which is true (565 − 84 = 481 s at 0,25 kg, 1130 − 167 = 963 s at 0,50 kg). So this distractor is not clearly wrong, and a student who reads it that way has two defensible options. Its feedback is about the ratio, not the difference. — Fix: say it is the ratio that grows, e.g. "Kiehuminen kestää pidempään, ja kiehumisen ja sulamisen kestojen suhde kasvaa, kun massa kasvaa."
- inquiry.json:265 (virhe, feedback of the correct option) — A/consistency: "se purkaa hiukkasten välisiä sidoksia" is about melting, and it contradicts the lesson's own model and the guardrail wording used everywhere else (Ydinajatus, Mihin energia menee, pred-3, exit ticket): the energy changes the interactions and raises the interaction energy, and liquid water stays bound together. Saying the bonds are broken brings back the misconception the audit removed. — Fix: "se muuttaa hiukkasten keskinäisiä vuorovaikutuksia ja kasvattaa niiden välistä vuorovaikutusenergiaa."

## Polish
- lesson.md:87 — "kaasussa ne … törmäilevät vain harvoin": molecules in a gas collide very often. The intended point is that they are far apart and move freely between collisions. Suggest "liikkuvat vapaasti kaukana toisistaan".
- inquiry.json:387 (check-2 solution) — the answer is given to three significant figures "koska … teho $1500\,\text{W}$ on annettu kolmella numerolla". 1500 shows two to four, so say that 15,0 min limits it.
- sim.js:8 — the code comment says the plateau energy "breaks the bonds between particles". It is not shown to students, but align it with the model ("raises the interaction energy") at the next sim change.

## Checked
- One script recomputed every number: retrieval (209,5 kJ; distractors 2,1 kJ and 419 kJ), pred-1/2 durations (1130/565 s; 83,5/565 s and 167/1130 s; r/s = 6,77), worked example (2 343 750 J/kg, +3,7 %, 133 g), siirto 188 W (mistakes 27,8 and 11 300), check-2 0,597 kg (mistakes 0,677 and 4,04; 0,54 kg check), check-3 (2260 + 264 J, ratio 9,6), ratios 5,39 and 79,7 K.
- Worked example: solved symbolically from Q_kuum = Q_h. Losses biasing r upwards is the right direction.
- Heating-curve figure: the ice and steam slopes are 1,97 and 1,96 times the water slope, as the caption says. The phase diagram's melting line leans left (right for water), and the mountain point boils below 100 °C.
- sim.js: implements the piecewise Q(T) model with the right constants, Q = Pt, plateaus sm/P and rm/P. The piston and constant pressure are stated in the model box and the spec. simState gives tMelt and tBoil. exp-1 locks m and varies P; exp-2 locks P and varies m.
- Conditions stated: pure substance at constant pressure, open pot versus piston versus rigid vessel, work of expansion (about 7 % of r, "pieni osa").
- Exactly one correct option in each choice. The other distractors' feedback is correct.
- The exit ticket, summary and johtopäätös model answer agree with the theory. The scope is FY3's olomuodon muutokset.
