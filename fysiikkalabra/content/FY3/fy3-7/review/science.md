VERDICT: PASS
CONTENT-HASH: b0f6e4ca25a0ebc8

## Blocking

## Polish
- exercises.json:22, solutions.md:23 — about 5 cm of ice (45 kg/m², so 15 MJ/m² lost in one night, roughly 350 W/m²) is a lot for "syksyn ensimmäinen pakkasyö", and the Järkevyys line calls it typical — say "kova pakkasyö" or use about 15–20 kg/m², or soften the check line.
- solutions.md:87 — "Muutama kauhallinen jäähdyttää kiviä kymmeniä kelvinejä" understates the result: one ladle alone gives 27 K — write "Jo yksi kauhallinen jäähdyttää kiviä kymmeniä kelvinejä (kunnes kiuas lämmittää ne taas)".
- inquiry.json:111–120 — pred-3 cites the simulation as evidence against Aino and Cem and for Bea, but the sim has the plateau built in (`stateAt`). The real evidence is that the plateau's length is proportional to m with no losses in the model. Bea's feedback could add that the micro-model is the explanation, which the sim does not test.
- lesson.md phase-diagram SVG — the vaporisation curve leaves the triple point with zero slope. The sublimation curve is steeper there, which is correct, but a small positive slope would look less odd. The figure is labelled a kaavakuva, so this is taste.

## Checked
- All 12 exercise answers recomputed independently, and they match answers.py and exercises.json. Every solutions.md line and Järkevyys figure (90 %, 24 %, 87 %, 2,7 kg, 21 °C, 2,45/2,67 MJ/kg, 60 W) also checks out.
- Worked example: r = Pt/Δm is solved symbolically first and gives 2,34 MJ/kg. The loss explanation is correct: the loss makes r too large.
- Lesson numbers: the ratios 6,8 and 5,4 and the "0→80 °C" claim (79,7 K) are correct. Q = sm and Q = rm come with their conditions (constant pressure, ΔT = 0), and both are in FY3 scope.
- Heating-curve SVG: the slopes of the ice, water and steam segments follow c (2,0 : 1 : 2,1) on one consistent Q scale. The plateaus are labelled not to scale. The Q labels are on the correct plateaus.
- Phase-diagram SVG: the solid–liquid line tilts left (water). Low pressure gives a lower boiling point ("vuori" is left of 100 °C).
- Inquiry: pr-lampo 209,5 kJ, with the 2,1 kJ and 419 kJ distractors explained correctly. pred-1 1130/565 s, pred-2 83,5/565 and 167/1130 s (ratio 6,8), virhe 66,8 kJ, siirto 188 W (mistakes 27,8 and 11 300), check-2 0,597 kg (mistakes 0,677 and 4,04), check-3 2260 + 264 J (×9,6, "lähes kymmenen").
- exp-1 locks m and varies P; exp-2 locks P and varies m. simState gives tMelt and tBoil, and the initial values are within the slider ranges.
- sim.js: the stage energies, stateAt, the ice and water fractions and Q = Pt are correct. The 1280 px capture matches the computed breakpoints (21, 188, 398, 1528, 1558 s). The no-loss and steam-stays assumptions are stated in the note and the inquiry model text.
- Exit ticket and Tiivistelmä agree with the theory.
- The hash was the same at the start and at the end.
